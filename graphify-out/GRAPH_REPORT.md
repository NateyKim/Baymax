[START HERE: required working protocol](../docs/WORKING_PROTOCOL.md) · [Testing protocol](../Baymax-main/TESTING_PROTOCOL.md) · [Contribution route](../CONTRIBUTING.md)

[Feature log](../docs/features/FEATURE_LOG.md) · [Interactive graph](graph.html) · [Rendered feature log](FEATURE_LOG.html)

# Graph Report - Baymax  (2026-11-07)

## Corpus Check
- 208 files · ~165,288 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 46 file(s) not represented in the graph (top: .service 11, (none) 8, .cmd 7)

## Summary
- 1713 nodes · 3122 edges · 112 communities (72 shown, 40 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 108 edges (avg confidence: 0.86)
- Token usage: structural extraction uses no LLM; semantic usage was not reported by the host.

## Community Hubs (Navigation)
- Callable Tools
- Conversation and Audio
- Everyday Support
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Pose and Inference
- SD Card Builder
- Installation and Updates
- Conversation and Audio
- Pose and Inference
- Callable Tools
- Pose and Inference
- Callable Tools
- Runtime and Setup
- Pose and Inference
- Callable Tools
- Runtime and Setup
- Runtime and Setup
- Pose and Inference
- Callable Tools
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Pose and Inference
- Pose and Inference
- Callable Tools
- Runtime and Setup
- Runtime and Setup
- Conversation and Audio
- Callable Tools
- Callable Tools
- Callable Tools
- Family Connections
- Callable Tools
- Runtime and Setup
- Physical Eyes
- Installation and Updates
- Physical Eyes
- Runtime and Setup
- Runtime and Setup
- Callable Tools
- Pose and Inference
- Physical Eyes
- Callable Tools
- Callable Tools
- Callable Tools
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Physical Eyes
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
- Installation and Updates
- Runtime and Setup
- Runtime and Setup
- Conversation and Audio
- Physical Eyes
- Pose and Inference
- Pose and Inference
- Runtime and Setup
- Runtime and Setup
- Installation and Updates
- Physical Eyes
- Callable Tools
- Callable Tools
- Runtime and Setup
- Runtime and Setup
- Callable Tools
- Installation and Updates
- Installation and Updates
- Pose and Inference
- Callable Tools
- Runtime and Setup
- Runtime and Setup
- SD Card Builder
- Installation and Updates
- Pose and Inference
- Runtime and Setup
- Installation and Updates
- Pose and Inference
- Pose and Inference
- Callable Tools
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Runtime and Setup
- Pose and Inference
- Installation and Updates
- Installation and Updates

## God Nodes (most connected - your core abstractions)
1. `START HERE: mandatory working protocol and authority` - 149 edges
2. `VoiceAnalyzer` - 22 edges
3. `Store` - 20 edges
4. `PublicSources` - 20 edges
5. `check()` - 19 edges
6. `Player` - 18 edges
7. `record()` - 18 edges
8. `RknnEngine` - 17 edges
9. `_run_gemini()` - 17 edges
10. `InputEnhancer` - 16 edges

## Surprising Connections (you probably didn't know these)
- `main()` --calls--> `public_configuration()`  [INFERRED]
  devops/clickables/launch.py → Baymax-main/dev_settings.py
- `main()` --calls--> `read_status()`  [INFERRED]
  devops/clickables/launch.py → Baymax-main/runtime_monitor.py
- `main()` --calls--> `public_configuration()`  [INFERRED]
  devops/opi4-flash/payload/ember-hardware.py → Baymax-main/dev_settings.py
- `main()` --calls--> `save_configuration()`  [INFERRED]
  devops/opi4-flash/payload/ember-hardware.py → Baymax-main/dev_settings.py
- `runtime_script()` --calls--> `arm_linux()`  [INFERRED]
  devops/clickables/launch.py → Baymax-main/pc_hardware.py

## Import Cycles
- None detected.

## Communities (112 total, 40 thin omitted)

### Community 0 - "Callable Tools"
Cohesion: 0.05
Nodes (29): ConversationSources, discovery_enabled(), enabled_names(), extend_config(), handle_tool_call(), run_call(), Toolkit, Headlines (+21 more)

### Community 1 - "Conversation and Audio"
Cohesion: 0.05
Nodes (15): ResidualEcho, apply(), audio_ready(), enabled(), Engagement, register(), create(), enabled() (+7 more)

### Community 2 - "Everyday Support"
Cohesion: 0.07
Nodes (19): _at(), _candidates(), _clock(), _days_in_month(), describe(), device_timezone(), _ints(), local_start() (+11 more)

### Community 3 - "Runtime and Setup"
Cohesion: 0.07
Nodes (38): _alert_recipients(), auth_login(), auth_logout(), auth_me(), auth_resend(), auth_signup(), auth_verify(), camera_stream() (+30 more)

### Community 4 - "Runtime and Setup"
Cohesion: 0.07
Nodes (20): _build_transcript(), _collect_segments(), main(), _merge_segments(), _poll_jobs(), _report_failure(), _run_analysis(), _enqueue() (+12 more)

### Community 5 - "Runtime and Setup"
Cohesion: 0.07
Nodes (30): api_key(), _assigned(), card(), check(), core_session(), declared_tools(), disclosure(), image_file() (+22 more)

### Community 6 - "Runtime and Setup"
Cohesion: 0.04
Nodes (22): Mandatory Graphify-first agent instructions, migrate_data.sh script, test_hotspot.sh script, prepare_unit.sh script, late.sh script, Software, chamber simulation, hardware and release evidence, Authoritative repository, stable fixes and owner-selected channels, Professional feature branches, pull requests and review (+14 more)

### Community 7 - "Pose and Inference"
Cohesion: 0.08
Nodes (19): compare_raw(), alignment_rect(), associate(), decode_detections(), decode_landmarks(), Detection, detector_roi(), _iou() (+11 more)

### Community 8 - "SD Card Builder"
Cohesion: 0.11
Nodes (23): asset(), digest(), generate_credentials(), attach(), chroot_down(), chroot_up(), detach(), build_linux.sh script (+15 more)

### Community 9 - "Installation and Updates"
Cohesion: 0.13
Nodes (23): block_ssid(), client_mode(), hostapd_config(), hotspot_name(), join_saved(), log(), main(), network_block() (+15 more)

### Community 10 - "Conversation and Audio"
Cohesion: 0.09
Nodes (5): AddressGate, follow_up_seconds(), is_speech(), names_ember(), _WatchedSession

### Community 11 - "Pose and Inference"
Cohesion: 0.15
Nodes (23): build_dir(), build_rknn(), check(), check_failures(), check_limits(), compare_onnx_tflite(), compare_pipelines(), densify() (+15 more)

### Community 12 - "Callable Tools"
Cohesion: 0.10
Nodes (9): ensure_model(), EyeContact, FaceLandmarks, looking(), presence_enabled(), Proactive, _setting(), startup_enabled() (+1 more)

### Community 13 - "Pose and Inference"
Cohesion: 0.10
Nodes (14): _close_quietly(), create_pose_backend(), driver_hint(), _driver_hint(), _flat(), import_rknnlite(), installed_rknnlite_version(), _open_npu() (+6 more)

### Community 14 - "Callable Tools"
Cohesion: 0.11
Nodes (14): _clean_query(), _covers_query(), download(), fetch_book(), _ia_search(), _keep_only(), _lucene_terms(), _normalise_title() (+6 more)

### Community 15 - "Runtime and Setup"
Cohesion: 0.13
Nodes (14): latest_frames_only(), _draw_angle_graph(), _draw_annotated(), _draw_fall_alert(), _draw_hud(), _draw_skeleton(), _draw_trunk_line(), _ensure_pose_model() (+6 more)

### Community 16 - "Pose and Inference"
Cohesion: 0.15
Nodes (18): compare(), fall_detector(), _jsonable(), main(), pct(), _print_clip(), _print_summary(), _rate() (+10 more)

### Community 17 - "Callable Tools"
Cohesion: 0.13
Nodes (8): CheckIns, enabled(), _last_conversation(), _last_heard(), _path(), _setting(), window(), windows()

### Community 18 - "Runtime and Setup"
Cohesion: 0.13
Nodes (16): _abort_connection(), fall_alert_monitor(), monitor_queues(), _run_gemini(), send_audio_realtime(), _send_cut_off_prompts(), send_video_realtime(), consume_stop_request() (+8 more)

### Community 20 - "Pose and Inference"
Cohesion: 0.13
Nodes (8): cpu_factory(), default_mediapipe_options(), MediaPipeCpuBackend, frames_from(), main(), run(), summary(), Timed

### Community 21 - "Callable Tools"
Cohesion: 0.11
Nodes (12): execute(), execute(), execute(), enabled(), execute(), find_stations(), _miniaudio_source(), open_stream() (+4 more)

### Community 22 - "Runtime and Setup"
Cohesion: 0.19
Nodes (5): log(), main(), read_env(), _requirements(), Updater

### Community 23 - "Runtime and Setup"
Cohesion: 0.18
Nodes (10): test_device(), camera_devices(), check_camera_permission(), _framework(), resolve_camera(), camera_candidates(), configure_audio_backend(), npu_drivers() (+2 more)

### Community 24 - "Runtime and Setup"
Cohesion: 0.17
Nodes (8): _draw_angle_graph(), _draw_fall_alert(), _draw_hud(), _draw_skeleton(), _draw_trunk_line(), _ensure_model(), run(), _text()

### Community 25 - "Pose and Inference"
Cohesion: 0.17
Nodes (6): _by_size(), _finite(), heatmap_hwc(), OnnxEngine, split_detector(), split_landmarks()

### Community 26 - "Pose and Inference"
Cohesion: 0.14
Nodes (4): LandmarkSmoother, LowPass, OneEuro, ssd_anchors()

### Community 28 - "Runtime and Setup"
Cohesion: 0.22
Nodes (8): enabled(), configured_models(), PreflightError, PreflightUnavailable, validate_key(), main(), CredentialError, gemini_key()

### Community 29 - "Runtime and Setup"
Cohesion: 0.18
Nodes (6): audio_catalog(), camera_catalog(), Handler, LocalServer, main(), open_camera()

### Community 30 - "Conversation and Audio"
Cohesion: 0.17
Nodes (6): enabled(), execute(), extend_config(), _level(), _path(), VoiceVolume

### Community 31 - "Callable Tools"
Cohesion: 0.17
Nodes (9): start(), enabled(), extend_config(), handle_tool_call(), prewarm(), warm(), search_enabled(), enabled() (+1 more)

### Community 32 - "Callable Tools"
Cohesion: 0.13
Nodes (6): attach(), _boost(), hold_for_answer(), register(), session_task(), _volume()

### Community 33 - "Callable Tools"
Cohesion: 0.18
Nodes (3): enabled(), FallWorker, _record()

### Community 36 - "Runtime and Setup"
Cohesion: 0.12
Nodes (9): _format_transcript(), _generate_summary(), _keep_transcript_unsaved(), _mark_transcript_saved(), _memory_save_due(), _memory_saver_thread(), _save_memories_on_stop(), _summarise_and_embed() (+1 more)

### Community 37 - "Physical Eyes"
Cohesion: 0.16
Nodes (7): clear_failures(), expected_sensors(), eyes_session(), sensors(), failure_face(), lost_sensor(), _mic_reports()

### Community 38 - "Installation and Updates"
Cohesion: 0.18
Nodes (8): _device_setting(), home(), page_not_found(), profile_exists(), setup(), status(), switch_network(), uplink_iface()

### Community 39 - "Physical Eyes"
Cohesion: 0.28
Nodes (5): LedControl, crashed(), main(), settings(), show()

### Community 40 - "Runtime and Setup"
Cohesion: 0.14
Nodes (7): _download_memory_model(), _load_memory_embedder(), _memory_model_to_download(), _memory_store(), download_model(), missing_packages(), model_present()

### Community 41 - "Runtime and Setup"
Cohesion: 0.24
Nodes (7): main(), portable_diagnostic(), source_group(), check(), fingerprints(), semantic_graph(), main()

### Community 42 - "Callable Tools"
Cohesion: 0.19
Nodes (8): heard(), _listener(), download_model(), heard(), model_path(), _pair(), _vosk_model(), _vosk_recognizer()

### Community 43 - "Pose and Inference"
Cohesion: 0.21
Nodes (7): npu_unavailable_reason(), _open_onnx(), check_passed(), check_section(), load_manifest(), ModelError, verified_files()

### Community 44 - "Physical Eyes"
Cohesion: 0.23
Nodes (6): attach(), AutoEyes, cue(), medical_alert(), reply_cue(), requested()

### Community 45 - "Callable Tools"
Cohesion: 0.15
Nodes (3): check_minutes(), license_name(), Station

### Community 46 - "Callable Tools"
Cohesion: 0.23
Nodes (4): coordinates(), fetch_json(), Location, Weather

### Community 48 - "Runtime and Setup"
Cohesion: 0.26
Nodes (9): use_performance_cpus(), configuration_ready(), configure_once(), main(), pid_alive(), runtime_lock(), runtime_running(), _stop() (+1 more)

### Community 49 - "Runtime and Setup"
Cohesion: 0.15
Nodes (10): _abandon_reply(), _flush_playback(), listen_audio(), audio_callback(), _local_fall_monitor(), _output_callback(), _queue_microphone(), run() (+2 more)

### Community 50 - "Runtime and Setup"
Cohesion: 0.27
Nodes (7): public_configuration(), read_configuration(), save_configuration(), audio_device(), camera_device(), identity(), main()

### Community 52 - "Runtime and Setup"
Cohesion: 0.20
Nodes (8): transcript_overlap(), _append_playback(), receive_audio(), play_reply_audio(), show_reply_text(), _retrieve_memories(), _transcript_add(), transcribe()

### Community 54 - "Family Connections"
Cohesion: 0.23
Nodes (6): deliver_messages(), enabled(), profile_section(), refresh_profile(), register(), session_task()

### Community 55 - "Runtime and Setup"
Cohesion: 0.23
Nodes (3): remote_pose(), remote_face(), Remote

### Community 58 - "Runtime and Setup"
Cohesion: 0.18
Nodes (6): _build_config(), _fire_initiation(), _initiation_memory_hint(), initiation_monitor(), _newest_memories(), _safe_to_initiate()

### Community 59 - "Runtime and Setup"
Cohesion: 0.36
Nodes (9): ensure_environment(), environment_python(), fingerprint(), install_shortcuts(), installation_lock(), main(), requirements_file(), run_checked() (+1 more)

### Community 60 - "SD Card Builder"
Cohesion: 0.24
Nodes (6): anydesk_id(), command(), duration(), Handler, progress(), status()

### Community 61 - "Conversation and Audio"
Cohesion: 0.22
Nodes (5): connection_lost(), extend_config(), on_server_message(), remember(), _tokens()

### Community 63 - "Everyday Support"
Cohesion: 0.31
Nodes (7): available_to_speak(), enabled(), execute(), notify_due(), _playback_active(), register(), session_task()

### Community 64 - "Installation and Updates"
Cohesion: 0.38
Nodes (9): cfg(), pactl_user(), run_gemini_with_retry(), set_audio_levels(), startup.sh script, start_containers(), start_portal_supervised(), start_robot() (+1 more)

### Community 65 - "Runtime and Setup"
Cohesion: 0.27
Nodes (3): enabled(), apply(), voice()

### Community 66 - "Runtime and Setup"
Cohesion: 0.33
Nodes (6): collect_suites(), local_settings_ignored(), __init__(), main(), render_report(), run_sections()

### Community 71 - "Runtime and Setup"
Cohesion: 0.25
Nodes (4): arm_linux(), performance_cpus(), main(), runtime_script()

### Community 72 - "Runtime and Setup"
Cohesion: 0.22
Nodes (3): _boot_status(), _notify_webapp(), _TurnTranscript

### Community 73 - "Installation and Updates"
Cohesion: 0.50
Nodes (7): cfg(), compose(), healthy(), image_id(), log(), ember-update.sh script, wait_healthy()

### Community 74 - "Physical Eyes"
Cohesion: 0.29
Nodes (4): enabled(), execute(), extend_config(), silent()

### Community 76 - "Callable Tools"
Cohesion: 0.32
Nodes (4): main(), recognizer(), response(), speech()

### Community 77 - "Runtime and Setup"
Cohesion: 0.38
Nodes (3): main(), open_camera(), say()

### Community 80 - "Installation and Updates"
Cohesion: 0.53
Nodes (4): closure(), imported_top_level_modules(), main(), root_distributions()

### Community 81 - "Installation and Updates"
Cohesion: 0.60
Nodes (5): cfg(), die(), run(), provision.sh script, step()

### Community 84 - "Runtime and Setup"
Cohesion: 0.53
Nodes (4): desktop_quote(), install(), main(), systemd_quote()

### Community 85 - "Runtime and Setup"
Cohesion: 0.53
Nodes (4): display_connected(), main(), open_monitor(), serve()

### Community 86 - "SD Card Builder"
Cohesion: 0.60
Nodes (4): load(), main(), save(), validate()

### Community 88 - "Installation and Updates"
Cohesion: 0.60
Nodes (3): die(), make_usb.sh script, step()

### Community 90 - "Runtime and Setup"
Cohesion: 0.40
Nodes (3): _audio_writer_thread(), _open_new_segment(), _prune_day_utterance()

### Community 91 - "Installation and Updates"
Cohesion: 0.83
Nodes (3): answer(), erase-confirm.sh script, stop_here()

### Community 100 - "Runtime and Setup"
Cohesion: 0.83
Nodes (4): feature_html(), flush(), flush_paragraph(), inline()

## Knowledge Gaps
- **9 isolated node(s):** `Mandatory Graphify-first agent instructions`, `Software, chamber simulation, hardware and release evidence`, `Authoritative repository, stable fixes and owner-selected channels`, `Professional feature branches, pull requests and review`, `Which branch and pull request to use` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 592 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **40 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `START HERE: mandatory working protocol and authority` connect `Runtime and Setup` to `Callable Tools`, `Conversation and Audio`, `Everyday Support`, `Runtime and Setup`, `Runtime and Setup`, `Runtime and Setup`, `Pose and Inference`, `SD Card Builder`, `Installation and Updates`, `Conversation and Audio`, `Pose and Inference`, `Callable Tools`, `Pose and Inference`, `Callable Tools`, `Runtime and Setup`, `Pose and Inference`, `Callable Tools`, `Runtime and Setup`, `Pose and Inference`, `Callable Tools`, `Runtime and Setup`, `Runtime and Setup`, `Runtime and Setup`, `Pose and Inference`, `Runtime and Setup`, `Runtime and Setup`, `Conversation and Audio`, `Callable Tools`, `Callable Tools`, `Family Connections`, `Physical Eyes`, `Installation and Updates`, `Physical Eyes`, `Runtime and Setup`, `Runtime and Setup`, `Callable Tools`, `Pose and Inference`, `Physical Eyes`, `Callable Tools`, `Runtime and Setup`, `Runtime and Setup`, `Runtime and Setup`, `Family Connections`, `Family Connections`, `Callable Tools`, `Runtime and Setup`, `SD Card Builder`, `Conversation and Audio`, `Everyday Support`, `Installation and Updates`, `Runtime and Setup`, `Runtime and Setup`, `Conversation and Audio`, `Physical Eyes`, `Runtime and Setup`, `Installation and Updates`, `Physical Eyes`, `Callable Tools`, `Runtime and Setup`, `Runtime and Setup`, `Installation and Updates`, `Installation and Updates`, `Runtime and Setup`, `Runtime and Setup`, `SD Card Builder`, `SD Card Builder`, `Installation and Updates`, `Installation and Updates`, `SD Card Builder`, `Runtime and Setup`, `Pose and Inference`, `Callable Tools`, `SD Card Builder`, `Installation and Updates`, `Installation and Updates`, `Runtime and Setup`, `SD Card Builder`?**
  _High betweenness centrality (0.758) - this node is a cross-community bridge._
- **What connects `Mandatory Graphify-first agent instructions`, `Software, chamber simulation, hardware and release evidence`, `Authoritative repository, stable fixes and owner-selected channels` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Callable Tools` be split into smaller, more focused modules?**
  _Cohesion score 0.052184769038701624 - nodes in this community are weakly interconnected._
- **Why does `AddressGate` connect `Conversation and Audio` to `Runtime and Setup`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **Should `Conversation and Audio` be split into smaller, more focused modules?**
  _Cohesion score 0.05254237288135593 - nodes in this community are weakly interconnected._
- **Why does `SemanticEmbedder` connect `Runtime and Setup` to `Runtime and Setup`, `Runtime and Setup`?**
  _High betweenness centrality (0.033) - this node is a cross-community bridge._
- **Should `Everyday Support` be split into smaller, more focused modules?**
  _Cohesion score 0.07080200501253132 - nodes in this community are weakly interconnected._
## Scope and integrity

The graph is documentation, not a hardware certification. Local paths are repository-relative. 913 unresolved/external references (including standard-library imports) are omitted from this project-only view and retained in `UNRESOLVED_REFERENCES.json`; these are not claimed to be missing runtime dependencies. Parallel relationships can collapse in the native undirected view; raw semantic evidence remains in `docs/features/semantic_graph.json`.

Project-view health:

```json
{
  "node_count": 1713,
  "unverified_node_count": 0,
  "raw_edge_count": 3194,
  "non_object_edges": 0,
  "missing_endpoint_edges": 0,
  "dangling_endpoint_edges": 0,
  "external_reference_edges": 0,
  "self_loop_edges": 4,
  "valid_candidate_edges": 3194,
  "exact_duplicate_edges": 0,
  "directed_unique_endpoint_pairs": 3124,
  "directed_same_endpoint_collapsed_edges": 70,
  "undirected_unique_endpoint_pairs": 3123,
  "undirected_same_endpoint_collapsed_edges": 71,
  "same_endpoint_group_count": 69,
  "relation_variant_groups": 68,
  "source_file_variant_groups": 0,
  "source_location_variant_groups": 2,
  "context_variant_groups": 0,
  "post_build_graph_type": "Graph",
  "post_build_node_count": 1713,
  "post_build_edge_count": 3122,
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
  "node_count": 1713,
  "unverified_node_count": 0,
  "raw_edge_count": 4107,
  "non_object_edges": 0,
  "missing_endpoint_edges": 0,
  "dangling_endpoint_edges": 913,
  "external_reference_edges": 0,
  "self_loop_edges": 4,
  "valid_candidate_edges": 3194,
  "exact_duplicate_edges": 0,
  "directed_unique_endpoint_pairs": 3124,
  "directed_same_endpoint_collapsed_edges": 70,
  "undirected_unique_endpoint_pairs": 3123,
  "undirected_same_endpoint_collapsed_edges": 71,
  "same_endpoint_group_count": 69,
  "relation_variant_groups": 68,
  "source_file_variant_groups": 0,
  "source_location_variant_groups": 2,
  "context_variant_groups": 0,
  "post_build_graph_type": "Graph",
  "post_build_node_count": 1796,
  "post_build_edge_count": 4034,
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
