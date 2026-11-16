#!/bin/sh
# PROTOTYPE ONLY - run as root on a board you can reach locally (HDMI+keyboard or serial).
# Tests: does a virtual AP (ap0) run while wlan0 stays associated as a client?
# Does not touch ember-wifi-setup, wpa_supplicant.conf or systemd. Ctrl-C cleans up.
# Usage: sudo sh ap-client-concurrency.sh [hotspot-password]   (default: embertest123)
set -u
IW=/usr/sbin/iw
AP=ap0
ADDR=192.168.4.1
PASS=${1:-embertest123}
RUN=/run/ember-apsta-test
mkdir -p -m 700 "$RUN"
rm -f "$RUN/pids"

cleanup() {
    echo "== cleanup"
    [ -f "$RUN/pids" ] && kill $(cat "$RUN/pids") 2>/dev/null
    $IW dev $AP del 2>/dev/null
    echo "== wlan0 after cleanup:"; $IW dev wlan0 link
}
trap cleanup EXIT INT TERM

echo "== capability"; $IW phy phy0 info | sed -n '/valid interface combinations/,/^\s*$/p'
echo "== client link"; $IW dev wlan0 link
FREQ=$(timeout 5 $IW dev wlan0 link | awk '/freq:/{print int($2)}')
[ -n "$FREQ" ] || { echo "wlan0 not associated; connect it first"; exit 1; }
if [ "$FREQ" -lt 3000 ]; then CH=$(( (FREQ - 2407) / 5 )); MODE=g; else CH=$(( (FREQ - 5000) / 5 )); MODE=a; fi
# AP_CHANNEL=6 forces a 2.4 GHz AP on a different channel (tests multi-channel; needed when the client is on a DFS channel).
if [ -n "${AP_CHANNEL:-}" ]; then CH=$AP_CHANNEL; if [ "$CH" -le 14 ]; then MODE=g; else MODE=a; fi; fi
echo "== client on $FREQ MHz -> AP channel $CH (hw_mode=$MODE, same channel as client)"

# Locally administered MAC derived from wlan0 so the two interfaces differ.
MAC=$(cat /sys/class/net/wlan0/address | sed 's/^../02/')
$IW dev wlan0 interface add $AP type __ap || { echo "FAIL: driver refused ap0"; exit 1; }
ip link set $AP address "$MAC" 2>/dev/null
ip link set $AP up
ip addr add $ADDR/24 dev $AP

cat > "$RUN/hostapd.conf" <<EOF
interface=$AP
driver=nl80211
ssid=Ember-APSTA-Test
country_code=US
hw_mode=$MODE
channel=$CH
ieee80211n=1
wpa=2
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
wpa_passphrase=$PASS
EOF
chmod 600 "$RUN/hostapd.conf"

hostapd "$RUN/hostapd.conf" > "$RUN/hostapd.log" 2>&1 & echo $! >> "$RUN/pids"
# Wildcard DNS + a server that answers every URL = phones show the "sign in to network" pop-up.
dnsmasq --keep-in-foreground --conf-file=/dev/null --no-resolv --interface=$AP --bind-interfaces \
    --dhcp-range=192.168.4.10,192.168.4.100,10m --dhcp-option=option:router,$ADDR --address=/#/$ADDR \
    > "$RUN/dnsmasq.log" 2>&1 & echo $! >> "$RUN/pids"
cat > "$RUN/portal.py" <<'EOF'
import http.server as h, sys
BODY = b'<!DOCTYPE html><meta name="viewport" content="width=device-width"><h1>Ember AP+STA test page</h1><p>You reached the board.</p>'
class H(h.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html'); self.send_header('Content-Length', str(len(BODY)))
        self.send_header('Cache-Control', 'no-store'); self.end_headers(); self.wfile.write(BODY)
h.ThreadingHTTPServer((sys.argv[1], 80), H).serve_forever()
EOF
python3 "$RUN/portal.py" $ADDR > "$RUN/http.log" 2>&1 & echo $! >> "$RUN/pids"

sleep 3
echo "== hostapd log:"; tail -n 5 "$RUN/hostapd.log"
echo "== Join Ember-APSTA-Test from a phone, open http://$ADDR/index.html. Watching client health every 5 s..."
while :; do
    LINK=$(timeout 5 $IW dev wlan0 link | awk '/SSID/{print $2}')
    PING=$(timeout 5 ping -c1 -W2 -I wlan0 1.1.1.1 >/dev/null 2>&1 && echo ok || echo FAIL)
    STA=$(timeout 5 $IW dev $AP station dump | grep -c Station)
    echo "$(date +%T) wlan0=${LINK:-DISCONNECTED} internet=$PING ap_clients=$STA hostapd=$(kill -0 $(head -n1 "$RUN/pids") 2>/dev/null && echo up || echo DOWN)"
    sleep 5
done
