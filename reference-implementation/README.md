# M-PIN Reference Implementation v0.1b Verified

A deliberately small executable reference for the frozen M-PIN v2 lifecycle.

> **Runtime belongs to the service process. Persistence belongs to the Owner's decision.**

This package demonstrates:

`Connect → Load → Runtime → Owner SAVE → Validate → Atomic Commit → Disconnect`

and the equally important path:

`Connect → Load → Runtime → No SAVE → Disconnect → Previous Current State remains`

## Why this exists

The goal is not to build an enterprise middleware platform. The goal is to make the core M-PIN semantics executable and testable with as few moving parts as possible.

## Verification status

**Verified on Windows — 9/9 reference conformance tests passed.**

Project-owner execution verification completed on **2026-09-16**:

- Demo execution: **PASS**
- Reference Conformance Tests: **9/9 PASS**

This verifies the limited scope of this Reference Implementation only. It does **not** mean that a production M-PIN Hub, production security stack, networking layer, encryption/key-management system, or full M-PIN product has been completed.

See `VERIFICATION.txt` for the recorded test set.

## Quick start

Requires Python 3.11+ and no third-party packages.

### Windows

Double-click `01_RUN_DEMO.bat`. The window stays open after the run so the result can be reviewed.

To run the conformance-oriented tests, double-click `02_RUN_TESTS.bat`.

### Command line

```bash
python demo.py
```

Run the conformance-oriented tests:

```bash
python -m unittest discover -s tests -v
```

## Minimal example

```python
from mpin_ref import Wallet, SynchronizationSession

wallet = Wallet("OWNER.MPIN.json")

with SynchronizationSession(
    wallet,
    "ai.example",
    owner_authorized=True,
    create_if_missing=True,
    owner_approved_create=True,
) as session:
    state = session.runtime_state
    session.set_runtime_state({"project": "Orbit Task", "frontend": "Svelte"})
    session.owner_save(owner_intent=True)
```

If `owner_save()` is not called, disconnect does not persist Runtime changes.

## Data format

For transparency, v0.1b uses one human-readable JSON file. This is not a proposed final `.MPIN` container format.

```json
{
  "format": "mpin-reference-v0.1",
  "friend_folders": {
    "ai.example": {
      "revision": 1,
      "current_state": {
        "project": "Orbit Task"
      }
    }
  }
}
```

The `revision` is only a freshness/stale-write guard. It is **not** M-PIN history and does not create rollback semantics.

## Scope discipline

This reference intentionally does **not** implement Hub, encryption, recovery, cloud sync, provider hosting, agent frameworks, branch/merge, or time-machine features. Those can be evaluated later without changing what this package is intended to prove.

See `CONFORMANCE.md` for the exact behaviors demonstrated.
