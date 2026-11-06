[Organized OPi4 V1 feature log](../docs/features/FEATURE_LOG.md) · [Interactive graph](graph.html) · [Rendered feature log](FEATURE_LOG.html)

# Graph Report - Baymax  (2026-11-05)

## Corpus Check
- 195 files · ~171,281 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 46 file(s) not represented in the graph (top: .service 11, (none) 8, .cmd 7)

## Summary
- 1841 nodes · 3139 edges · 120 communities (67 shown, 53 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 105 edges (avg confidence: 0.86)
- Token usage: structural extraction uses no LLM; semantic usage was not reported by the host.

## Community Hubs (Navigation)
- Callable Tools
- Physical Eyes
- Pose and Inference
- Runtime and Setup
- Everyday Support
- Runtime and Setup
- Callable Tools
- Runtime and Setup
- Feature Documentation
- Runtime and Setup
- Pose and Inference
- SD Card Builder
- Pose and Inference
- Conversation and Audio
- Runtime and Setup
- Installation and Updates
- Conversation and Audio
- Runtime and Setup
- Pose and Inference
- Callable Tools
- Runtime and Setup
- Callable Tools
- Callable Tools
- Runtime and Setup
- Pose and Inference
- Runtime and Setup
- Callable Tools
- Runtime and Setup
- Runtime and Setup
- Pose and Inference
- Conversation and Audio
- Runtime and Setup
- Runtime and Setup
- Callable Tools
- Conversation and Audio
- Callable Tools
- Callable Tools
- Family Connections
- Callable Tools
- Installation and Updates
- Pose and Inference
- Conversation and Audio
- Callable Tools
- Callable Tools
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Conversation and Audio
- Callable Tools
- Family Connections
- Runtime and Setup
- Family Connections
- Callable Tools
- Runtime and Setup
- Runtime and Setup
- SD Card Builder
- Conversation and Audio
- Callable Tools
- Everyday Support
- Callable Tools
- Installation and Updates
- Runtime and Setup
- Conversation and Audio
- Callable Tools
- Runtime and Setup
- Runtime and Setup
- Installation and Updates
- Callable Tools
- Runtime and Setup
- Runtime and Setup
- Installation and Updates
- Installation and Updates
- Runtime and Setup
- Callable Tools
- Runtime and Setup
- Runtime and Setup
- SD Card Builder
- Installation and Updates
- Callable Tools
- Runtime and Setup
- Runtime and Setup
- Installation and Updates
- Callable Tools
- Callable Tools
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Pose and Inference
- Installation and Updates
- Installation and Updates
- Installation and Updates
- Installation and Updates
- Installation and Updates
- Installation and Updates
- Installation and Updates
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup

## God Nodes (most connected - your core abstractions)
1. `OPi4 V1 organized feature log` - 23 edges
2. `VoiceAnalyzer` - 22 edges
3. `Store` - 20 edges
4. `PublicSources` - 20 edges
5. `check()` - 19 edges
6. `run()` - 19 edges
7. `Player` - 18 edges
8. `RknnEngine` - 17 edges
9. `record()` - 17 edges
10. `InputEnhancer` - 16 edges

## Surprising Connections (you probably didn't know these)
- `runtime_script()` --calls--> `arm_linux()`  [INFERRED]
  devops/clickables/launch.py → Baymax-main/pc_hardware.py
- `main()` --calls--> `public_configuration()`  [INFERRED]
  devops/clickables/launch.py → Baymax-main/dev_settings.py
- `main()` --calls--> `public_configuration()`  [INFERRED]
  devops/opi4-flash/payload/ember-hardware.py → Baymax-main/dev_settings.py
- `main()` --calls--> `save_configuration()`  [INFERRED]
  devops/opi4-flash/payload/ember-hardware.py → Baymax-main/dev_settings.py
- `main()` --calls--> `read_status()`  [INFERRED]
  devops/clickables/launch.py → Baymax-main/runtime_monitor.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Shared pose and fall-check-in flow** — baymax_main_features_toolkits_fall_detection_fall_toolkit, baymax_main_features_toolkits_fall_detection_shared_pose, baymax_main_features_pose_readme_vision_child, baymax_main_features_pose_readme_pose, baymax_main_features_toolkits_fall_detection_fall_checkin [EXTRACTED 1.00]
- **Family messages and everyday reminder sync** — baymax_main_features_toolkits_family_readme_family, baymax_main_features_toolkits_family_readme_app_sync, baymax_main_features_toolkits_family_readme_family_store, baymax_main_features_toolkits_everyday_readme_everyday, baymax_main_features_toolkits_family_readme_confirmed_replies [EXTRACTED 1.00]

## Communities (120 total, 53 thin omitted)

### Community 0 - "Callable Tools"
Cohesion: 0.05
Nodes (29): ConversationSources, discovery_enabled(), enabled_names(), extend_config(), handle_tool_call(), run_call(), Toolkit, Headlines (+21 more)

### Community 1 - "Physical Eyes"
Cohesion: 0.05
Nodes (20): attach(), AutoEyes, cue(), medical_alert(), reply_cue(), requested(), clear_failures(), expected_sensors() (+12 more)

### Community 2 - "Pose and Inference"
Cohesion: 0.05
Nodes (24): compare_raw(), alignment_rect(), associate(), decode_detections(), decode_landmarks(), Detection, detector_roi(), _iou() (+16 more)

### Community 3 - "Runtime and Setup"
Cohesion: 0.06
Nodes (28): public_configuration(), read_configuration(), save_configuration(), audio_catalog(), Handler, LocalServer, main(), configured_models() (+20 more)

### Community 4 - "Everyday Support"
Cohesion: 0.07
Nodes (19): _at(), _candidates(), _clock(), _days_in_month(), describe(), device_timezone(), _ints(), local_start() (+11 more)

### Community 5 - "Runtime and Setup"
Cohesion: 0.07
Nodes (38): _alert_recipients(), auth_login(), auth_logout(), auth_me(), auth_resend(), auth_signup(), auth_verify(), camera_stream() (+30 more)

### Community 6 - "Callable Tools"
Cohesion: 0.05
Nodes (54): Fall package requirements, Optional strict address gate, Whole-frame PCM processing, Conversation and turn-taking, Existing Gemini Live session, Context compression and session resumption, Local speech and latency estimates, WebRTC echo cancellation and cleanup (+46 more)

### Community 7 - "Runtime and Setup"
Cohesion: 0.07
Nodes (20): _build_transcript(), _collect_segments(), main(), _merge_segments(), _poll_jobs(), _report_failure(), _run_analysis(), _enqueue() (+12 more)

### Community 8 - "Feature Documentation"
Cohesion: 0.06
Nodes (51): Independent Ember and Monitor user services, MVP startup and update guide, Opt-in release updater with rollback, On-board device settings, PortAudio / PipeWire / WirePlumber audio packages, Compiler, Python, Git and network system packages, XFCE / LightDM / Xorg desktop packages, Image system package list (+43 more)

### Community 9 - "Runtime and Setup"
Cohesion: 0.07
Nodes (30): api_key(), _assigned(), card(), check(), core_session(), declared_tools(), disclosure(), image_file() (+22 more)

### Community 10 - "Pose and Inference"
Cohesion: 0.08
Nodes (21): ChildPose, _close_quietly(), create_pose_backend(), driver_hint(), _driver_hint(), _flat(), installed_rknnlite_version(), npu_unavailable_reason() (+13 more)

### Community 11 - "SD Card Builder"
Cohesion: 0.11
Nodes (23): asset(), digest(), generate_credentials(), attach(), chroot_down(), chroot_up(), detach(), build_linux.sh script (+15 more)

### Community 12 - "Pose and Inference"
Cohesion: 0.12
Nodes (24): build_dir(), build_rknn(), check(), check_failures(), check_limits(), check_sequences(), compare_onnx_tflite(), compare_pipelines() (+16 more)

### Community 13 - "Conversation and Audio"
Cohesion: 0.10
Nodes (9): ResidualEcho, create(), enabled(), extend_config(), fan_filter_hz(), FanFilter, InputEnhancer, mute_during_reply() (+1 more)

### Community 14 - "Runtime and Setup"
Cohesion: 0.10
Nodes (22): transcript_overlap(), _abort_connection(), listen_audio(), receive_audio(), play_reply_audio(), show_reply_text(), run(), send_audio_realtime() (+14 more)

### Community 15 - "Installation and Updates"
Cohesion: 0.13
Nodes (23): block_ssid(), client_mode(), hostapd_config(), hotspot_name(), join_saved(), log(), main(), network_block() (+15 more)

### Community 16 - "Conversation and Audio"
Cohesion: 0.09
Nodes (5): AddressGate, follow_up_seconds(), is_speech(), names_ember(), _WatchedSession

### Community 17 - "Runtime and Setup"
Cohesion: 0.12
Nodes (16): test_device(), camera_catalog(), camera_devices(), check_camera_permission(), _framework(), resolve_camera(), camera_candidates(), configure_audio_backend() (+8 more)

### Community 18 - "Pose and Inference"
Cohesion: 0.10
Nodes (10): import_rknnlite(), _rknn_engine(), _by_size(), _finite(), heatmap_hwc(), OnnxEngine, RknnEngine, rknnlite_class() (+2 more)

### Community 19 - "Callable Tools"
Cohesion: 0.10
Nodes (9): ensure_model(), EyeContact, FaceLandmarks, looking(), presence_enabled(), Proactive, _setting(), startup_enabled() (+1 more)

### Community 20 - "Runtime and Setup"
Cohesion: 0.10
Nodes (18): _abandon_reply(), _append_playback(), _build_hazard_table(), _draw_angle_graph(), _draw_annotated(), _draw_fall_alert(), _draw_hud(), _draw_skeleton() (+10 more)

### Community 21 - "Callable Tools"
Cohesion: 0.12
Nodes (3): execute(), Player, record()

### Community 22 - "Callable Tools"
Cohesion: 0.11
Nodes (17): enabled(), extend_config(), silent(), execute(), execute(), start(), enabled(), execute() (+9 more)

### Community 23 - "Runtime and Setup"
Cohesion: 0.14
Nodes (24): AI core and webapp container composition, Experimental Docker deployment, Experimental core/webapp containers, Host boot and optional Wi-Fi hotspot tooling, Synthetic Gemini-in-the-loop evaluation, MediaPipe fall detection setup, Integrated v10 MVP installation, Orange Pi board-specific Debian setup (+16 more)

### Community 24 - "Pose and Inference"
Cohesion: 0.15
Nodes (18): compare(), fall_detector(), _jsonable(), main(), pct(), _print_clip(), _print_summary(), _rate() (+10 more)

### Community 25 - "Runtime and Setup"
Cohesion: 0.12
Nodes (24): Editing and validation protocol, Draft PR and software-lead review before merge/deployment, Preserve user edits, import paths and data flows, Board-specific live and fresh-card validation, Orange Pi scope: Pallas-Robotics/Baymax focused branch, Keep credentials, recordings, models and private images out of Git and graphs, Graphify AST extraction plus reviewed semantic document snapshot, Graphify feature map guide (+16 more)

### Community 26 - "Callable Tools"
Cohesion: 0.13
Nodes (8): CheckIns, enabled(), _last_conversation(), _last_heard(), _path(), _setting(), window(), windows()

### Community 28 - "Runtime and Setup"
Cohesion: 0.19
Nodes (5): log(), main(), read_env(), _requirements(), Updater

### Community 29 - "Pose and Inference"
Cohesion: 0.13
Nodes (7): default_mediapipe_options(), MediaPipeCpuBackend, frames_from(), main(), run(), summary(), Timed

### Community 31 - "Runtime and Setup"
Cohesion: 0.11
Nodes (10): _format_transcript(), _generate_summary(), _keep_transcript_unsaved(), _mark_transcript_saved(), _memory_save_due(), _memory_saver_thread(), _memory_store(), _save_memories_on_stop() (+2 more)

### Community 32 - "Runtime and Setup"
Cohesion: 0.17
Nodes (8): _draw_angle_graph(), _draw_fall_alert(), _draw_hud(), _draw_skeleton(), _draw_trunk_line(), _ensure_model(), run(), _text()

### Community 33 - "Callable Tools"
Cohesion: 0.13
Nodes (7): find_stations(), _miniaudio_source(), open_stream(), playable(), public_url(), stream_station(), UnsupportedStream

### Community 34 - "Conversation and Audio"
Cohesion: 0.17
Nodes (6): enabled(), execute(), extend_config(), _level(), _path(), VoiceVolume

### Community 35 - "Callable Tools"
Cohesion: 0.13
Nodes (6): attach(), _boost(), register(), session_task(), tell_gemini(), _volume()

### Community 36 - "Callable Tools"
Cohesion: 0.18
Nodes (3): enabled(), FallWorker, _record()

### Community 38 - "Callable Tools"
Cohesion: 0.19
Nodes (9): _clean_query(), _covers_query(), _ia_search(), _lucene_terms(), _normalise_title(), _rank(), score(), search() (+1 more)

### Community 39 - "Installation and Updates"
Cohesion: 0.18
Nodes (8): _device_setting(), home(), page_not_found(), profile_exists(), setup(), status(), switch_network(), uplink_iface()

### Community 40 - "Pose and Inference"
Cohesion: 0.13
Nodes (4): _Backend, FallbackBackend, PipelineBackend, port()

### Community 41 - "Conversation and Audio"
Cohesion: 0.18
Nodes (5): apply(), enabled(), heard(), _listener(), register()

### Community 42 - "Callable Tools"
Cohesion: 0.23
Nodes (4): coordinates(), fetch_json(), Location, Weather

### Community 44 - "Runtime and Setup"
Cohesion: 0.15
Nodes (7): arm_linux(), latest_frames_only(), performance_cpus(), _ensure_pose_model(), _fall_detection_thread(), _open_pose(), _update_face_visibility()

### Community 45 - "Runtime and Setup"
Cohesion: 0.17
Nodes (6): _download_memory_model(), _load_memory_embedder(), _memory_model_to_download(), download_model(), missing_packages(), model_present()

### Community 48 - "Callable Tools"
Cohesion: 0.23
Nodes (7): cpu_factory(), download_model(), heard(), model_path(), _pair(), _vosk_model(), _vosk_recognizer()

### Community 49 - "Family Connections"
Cohesion: 0.23
Nodes (6): deliver_messages(), enabled(), profile_section(), refresh_profile(), register(), session_task()

### Community 50 - "Runtime and Setup"
Cohesion: 0.23
Nodes (3): remote_pose(), remote_face(), Remote

### Community 53 - "Runtime and Setup"
Cohesion: 0.18
Nodes (6): _build_config(), _fire_initiation(), _initiation_memory_hint(), initiation_monitor(), _newest_memories(), _safe_to_initiate()

### Community 54 - "Runtime and Setup"
Cohesion: 0.36
Nodes (9): ensure_environment(), environment_python(), fingerprint(), install_shortcuts(), installation_lock(), main(), requirements_file(), run_checked() (+1 more)

### Community 55 - "SD Card Builder"
Cohesion: 0.24
Nodes (6): anydesk_id(), command(), duration(), Handler, progress(), status()

### Community 56 - "Conversation and Audio"
Cohesion: 0.22
Nodes (5): connection_lost(), extend_config(), on_server_message(), remember(), _tokens()

### Community 58 - "Everyday Support"
Cohesion: 0.31
Nodes (7): available_to_speak(), enabled(), execute(), notify_due(), _playback_active(), register(), session_task()

### Community 60 - "Installation and Updates"
Cohesion: 0.38
Nodes (9): cfg(), pactl_user(), run_gemini_with_retry(), set_audio_levels(), startup.sh script, start_containers(), start_portal_supervised(), start_robot() (+1 more)

### Community 61 - "Runtime and Setup"
Cohesion: 0.33
Nodes (6): collect_suites(), local_settings_ignored(), __init__(), main(), render_report(), run_sections()

### Community 64 - "Runtime and Setup"
Cohesion: 0.22
Nodes (3): _boot_status(), _notify_webapp(), _TurnTranscript

### Community 65 - "Runtime and Setup"
Cohesion: 0.36
Nodes (7): feature_html(), flush(), flush_paragraph(), inline(), main(), portable_diagnostic(), source_group()

### Community 66 - "Installation and Updates"
Cohesion: 0.50
Nodes (7): cfg(), compose(), healthy(), image_id(), log(), ember-update.sh script, wait_healthy()

### Community 67 - "Callable Tools"
Cohesion: 0.25
Nodes (3): check_minutes(), find_recordings(), license_name()

### Community 68 - "Runtime and Setup"
Cohesion: 0.38
Nodes (3): main(), open_camera(), say()

### Community 70 - "Installation and Updates"
Cohesion: 0.53
Nodes (4): closure(), imported_top_level_modules(), main(), root_distributions()

### Community 71 - "Installation and Updates"
Cohesion: 0.60
Nodes (5): cfg(), die(), run(), provision.sh script, step()

### Community 74 - "Runtime and Setup"
Cohesion: 0.53
Nodes (4): desktop_quote(), install(), main(), systemd_quote()

### Community 75 - "Runtime and Setup"
Cohesion: 0.53
Nodes (4): display_connected(), main(), open_monitor(), serve()

### Community 76 - "SD Card Builder"
Cohesion: 0.60
Nodes (4): load(), main(), save(), validate()

### Community 78 - "Installation and Updates"
Cohesion: 0.60
Nodes (3): die(), make_usb.sh script, step()

### Community 80 - "Runtime and Setup"
Cohesion: 0.40
Nodes (3): _audio_writer_thread(), _open_new_segment(), _prune_day_utterance()

### Community 81 - "Runtime and Setup"
Cohesion: 0.67
Nodes (4): Development and review protocol, Offline, live and lead-review evidence, Software-lead approval before merge/deployment, Offline core and toolkit review gate

### Community 82 - "Installation and Updates"
Cohesion: 0.83
Nodes (3): answer(), erase-confirm.sh script, stop_here()

### Community 85 - "Runtime and Setup"
Cohesion: 0.50
Nodes (4): macOS simulation and hardware verification, Simulated macOS device contract tests, Intel macOS dependency profile, Windows pinned dependency profile

## Knowledge Gaps
- **56 isolated node(s):** `Development and review protocol`, `Desktop setup and device selection`, `Intel macOS dependency profile`, `Shared Orange Pi ARM64 dependency profile`, `Desktop dependency profile` (+51 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 651 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **53 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ChildPose` connect `Pose and Inference` to `Runtime and Setup`, `Runtime and Setup`?**
  _High betweenness centrality (0.127) - this node is a cross-community bridge._
- **What connects `Development and review protocol`, `Desktop setup and device selection`, `Intel macOS dependency profile` to the rest of the system?**
  _56 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Callable Tools` be split into smaller, more focused modules?**
  _Cohesion score 0.052184769038701624 - nodes in this community are weakly interconnected._
- **Why does `PosePipeline` connect `Pose and Inference` to `Pose and Inference`, `Pose and Inference`, `Pose and Inference`?**
  _High betweenness centrality (0.068) - this node is a cross-community bridge._
- **Should `Physical Eyes` be split into smaller, more focused modules?**
  _Cohesion score 0.050203527815468114 - nodes in this community are weakly interconnected._
- **Why does `VoiceAnalyzer` connect `Runtime and Setup` to `Runtime and Setup`, `Runtime and Setup`?**
  _High betweenness centrality (0.050) - this node is a cross-community bridge._
- **Should `Pose and Inference` be split into smaller, more focused modules?**
  _Cohesion score 0.05 - nodes in this community are weakly interconnected._
## Scope and integrity

The graph is documentation, not a hardware certification. Local paths are repository-relative. 887 unresolved/external references (including standard-library imports) are omitted from this project-only view and retained in `UNRESOLVED_REFERENCES.json`; these are not claimed to be missing runtime dependencies. Parallel relationships can collapse in the native undirected view; raw semantic evidence remains in `docs/features/semantic_graph.json`.

Project-view health:

```json
{
  "node_count": 1842,
  "unverified_node_count": 0,
  "raw_edge_count": 3214,
  "non_object_edges": 0,
  "missing_endpoint_edges": 0,
  "dangling_endpoint_edges": 0,
  "external_reference_edges": 0,
  "self_loop_edges": 4,
  "valid_candidate_edges": 3214,
  "exact_duplicate_edges": 0,
  "directed_unique_endpoint_pairs": 3146,
  "directed_same_endpoint_collapsed_edges": 68,
  "undirected_unique_endpoint_pairs": 3140,
  "undirected_same_endpoint_collapsed_edges": 74,
  "same_endpoint_group_count": 67,
  "relation_variant_groups": 66,
  "source_file_variant_groups": 0,
  "source_location_variant_groups": 2,
  "context_variant_groups": 0,
  "post_build_graph_type": "Graph",
  "post_build_node_count": 1841,
  "post_build_edge_count": 3139,
  "post_build_error": "",
  "producer_suppression": {
    "path": "external-package/extract.py",
    "total_sites": 12,
    "sites": [
      {
        "line": 1789,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids = {n[\"id\"] for n in nodes}"
      },
      {
        "line": 2353,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids = {n[\"id\"] for n in nodes}"
      },
      {
        "line": 2355,
        "name": "seen_doc_refs",
        "tuple_arity": 0,
        "sample": "seen_doc_refs: set[str] = set()"
      },
      {
        "line": 3022,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids: set[str] = {n[\"id\"] for n in nodes}"
      },
      {
        "line": 3169,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids = {n.get(\"id\") for n in nodes}"
      },
      {
        "line": 4179,
        "name": "seen_keys",
        "tuple_arity": 0,
        "sample": "seen_keys: set[tuple] = set()"
      },
      {
        "line": 4365,
        "name": "seen_keys",
        "tuple_arity": 0,
        "sample": "seen_keys: set[tuple] = set()"
      },
      {
        "line": 7608,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids: set[str] = set()"
      },
      {
        "line": 7716,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids: set[str] = set()"
      },
      {
        "line": 7795,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids: set[str] = set()"
      },
      {
        "line": 8310,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids: set[str] = set()"
      },
      {
        "line": 8311,
        "name": "seen_edges",
        "tuple_arity": 4,
        "sample": "seen_edges: set[tuple[str, str, str, str | None]] = set()"
      }
    ],
    "error": ""
  },
  "examples": [
    {
      "source": "baymax_main_features_pose_validate_main",
      "target": "baymax_main_features_pose_validate_main_port",
      "edge_count": 3,
      "relations": [
        "contains",
        "indirect_call"
      ],
      "source_files": [
        "Baymax-main/features/pose/validate.py"
      ],
      "source_locations": [
        "L216",
        "L220",
        "L225"
      ],
      "contexts": [
        "",
        "collection"
      ]
    },
    {
      "source": "baymax_main_baymax_agent",
      "target": "baymax_main_baymax_cloud",
      "edge_count": 2,
      "relations": [
        "imports",
        "imports_from"
      ],
      "source_files": [
        "Baymax-main/baymax_agent.py"
      ],
      "source_locations": [
        "L26",
        "L27"
      ],
      "contexts": [
        "import"
      ]
    },
    {
      "source": "baymax_main_baymax_app_login_required",
      "target": "baymax_main_baymax_app_login_required_decorated",
      "edge_count": 2,
      "relations": [
        "contains",
        "indirect_call"
      ],
      "source_files": [
        "Baymax-main/baymax_app.py"
      ],
      "source_locations": [
        "L142",
        "L146"
      ],
      "contexts": [
        "",
        "return"
      ]
    },
    {
      "source": "baymax_main_baymax_app_send_verification_email",
      "target": "baymax_main_baymax_app_send_verification_email_send",
      "edge_count": 2,
      "relations": [
        "contains",
        "indirect_call"
      ],
      "source_files": [
        "Baymax-main/baymax_app.py"
      ],
      "source_locations": [
        "L185",
        "L204"
      ],
      "contexts": [
        "",
        "argument"
      ]
    },
    {
      "source": "baymax_main_baymax_app_camera_stream",
      "target": "baymax_main_baymax_app_camera_stream_relay",
      "edge_count": 2,
      "relations": [
        "calls",
        "contains"
      ],
      "source_files": [
        "Baymax-main/baymax_app.py"
      ],
      "source_locations": [
        "L440",
        "L450"
      ],
      "contexts": [
        "",
        "call"
      ]
    }
  ]
}
```

Raw extraction health before scope filtering:

```json
{
  "node_count": 1842,
  "unverified_node_count": 0,
  "raw_edge_count": 4101,
  "non_object_edges": 0,
  "missing_endpoint_edges": 0,
  "dangling_endpoint_edges": 887,
  "external_reference_edges": 0,
  "self_loop_edges": 4,
  "valid_candidate_edges": 3214,
  "exact_duplicate_edges": 0,
  "directed_unique_endpoint_pairs": 3146,
  "directed_same_endpoint_collapsed_edges": 68,
  "undirected_unique_endpoint_pairs": 3140,
  "undirected_same_endpoint_collapsed_edges": 74,
  "same_endpoint_group_count": 67,
  "relation_variant_groups": 66,
  "source_file_variant_groups": 0,
  "source_location_variant_groups": 2,
  "context_variant_groups": 0,
  "post_build_graph_type": "Graph",
  "post_build_node_count": 1924,
  "post_build_edge_count": 4025,
  "post_build_error": "",
  "producer_suppression": {
    "path": "external-package/extract.py",
    "total_sites": 12,
    "sites": [
      {
        "line": 1789,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids = {n[\"id\"] for n in nodes}"
      },
      {
        "line": 2353,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids = {n[\"id\"] for n in nodes}"
      },
      {
        "line": 2355,
        "name": "seen_doc_refs",
        "tuple_arity": 0,
        "sample": "seen_doc_refs: set[str] = set()"
      },
      {
        "line": 3022,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids: set[str] = {n[\"id\"] for n in nodes}"
      },
      {
        "line": 3169,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids = {n.get(\"id\") for n in nodes}"
      },
      {
        "line": 4179,
        "name": "seen_keys",
        "tuple_arity": 0,
        "sample": "seen_keys: set[tuple] = set()"
      },
      {
        "line": 4365,
        "name": "seen_keys",
        "tuple_arity": 0,
        "sample": "seen_keys: set[tuple] = set()"
      },
      {
        "line": 7608,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids: set[str] = set()"
      },
      {
        "line": 7716,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids: set[str] = set()"
      },
      {
        "line": 7795,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids: set[str] = set()"
      },
      {
        "line": 8310,
        "name": "seen_ids",
        "tuple_arity": 0,
        "sample": "seen_ids: set[str] = set()"
      },
      {
        "line": 8311,
        "name": "seen_edges",
        "tuple_arity": 4,
        "sample": "seen_edges: set[tuple[str, str, str, str | None]] = set()"
      }
    ],
    "error": ""
  },
  "examples": [
    {
      "source": "baymax_main_features_pose_validate_main",
      "target": "baymax_main_features_pose_validate_main_port",
      "edge_count": 3,
      "relations": [
        "contains",
        "indirect_call"
      ],
      "source_files": [
        "Baymax-main/features/pose/validate.py"
      ],
      "source_locations": [
        "L216",
        "L220",
        "L225"
      ],
      "contexts": [
        "",
        "collection"
      ]
    },
    {
      "source": "baymax_main_baymax_agent",
      "target": "baymax_main_baymax_cloud",
      "edge_count": 2,
      "relations": [
        "imports",
        "imports_from"
      ],
      "source_files": [
        "Baymax-main/baymax_agent.py"
      ],
      "source_locations": [
        "L26",
        "L27"
      ],
      "contexts": [
        "import"
      ]
    },
    {
      "source": "baymax_main_baymax_app_login_required",
      "target": "baymax_main_baymax_app_login_required_decorated",
      "edge_count": 2,
      "relations": [
        "contains",
        "indirect_call"
      ],
      "source_files": [
        "Baymax-main/baymax_app.py"
      ],
      "source_locations": [
        "L142",
        "L146"
      ],
      "contexts": [
        "",
        "return"
      ]
    },
    {
      "source": "baymax_main_baymax_app_send_verification_email",
      "target": "baymax_main_baymax_app_send_verification_email_send",
      "edge_count": 2,
      "relations": [
        "contains",
        "indirect_call"
      ],
      "source_files": [
        "Baymax-main/baymax_app.py"
      ],
      "source_locations": [
        "L185",
        "L204"
      ],
      "contexts": [
        "",
        "argument"
      ]
    },
    {
      "source": "baymax_main_baymax_app_camera_stream",
      "target": "baymax_main_baymax_app_camera_stream_relay",
      "edge_count": 2,
      "relations": [
        "calls",
        "contains"
      ],
      "source_files": [
        "Baymax-main/baymax_app.py"
      ],
      "source_locations": [
        "L440",
        "L450"
      ],
      "contexts": [
        "",
        "call"
      ]
    }
  ]
}
```
