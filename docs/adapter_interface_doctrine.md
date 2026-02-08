# Adapter Interface Doctrine (Plugin Law)

Adapters are apps/plugins added to Ndlovu Core (e.g., JobHub, VR Chord Studio).

## Requirements
- Offline‑first operation (queue actions when offline).
- Must log all actions/events for archival (Tamara).
- Must declare permissions: internal‑only vs external‑comm enabled (Monica).

## Adapter Contract (standard)
Every adapter must define:
- Name, version, purpose
- Inputs (commands/events)
- Outputs (actions/results)
- Data touched
- Failure modes + recovery
- Security constraints

## Execution Rule
Adapters cannot bypass the command spine:
Observe → Orient → Decide → Execute → Archive