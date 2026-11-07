# OPi4 V1 feature log

Start with the [working protocol](../WORKING_PROTOCOL.md),
[testing rules](../../Baymax-main/TESTING_PROTOCOL.md) and
[update-channel policy](../UPDATE_CHANNELS.md) before using this inventory.

| Area | Source | Current boundary |
|---|---|---|
| Local offline fall check-ins | `Baymax-main/features/toolkits/offline_fall.py` | Owner opt-in; software injection tests only; chamber/hardware pending |
| Language adaptation | `Baymax-main/features/persona.py` | Owner opt-in guidance; software evidence only |
| Pose and fall calculation | `Baymax-main/features/pose/`, `Baymax-main/fall_detection/` | Local processing; feature/board accuracy requires its own evidence |
| Conversation | `Baymax-main/features/conversational_ability/` | Existing Gemini/audio path; no inference of offline general conversation |
| Experimental stages | `Baymax-main/features/experimental/` | Software, chamber and physical evidence remain separate from channel choice |
| Owners and updates | `devops/opi4-flash/`, `devops/mvp/` | Source/channel preferences; installed updaters differ; no assumed fleet rollback |

This log and the graph are documentation, not release certification. See each
feature README for inputs, outputs, dependencies, external flows and validation.
