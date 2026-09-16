# M-PIN Reference Implementation v0.1b Verified — Conformance Map

This package is intentionally small. It demonstrates observable M-PIN v2 semantics; it is **not** a production security implementation.

## Demonstrated

| M-PIN v2 invariant / behavior | v0.1 mechanism |
|---|---|
| Owner centrality | Session creation requires `owner_authorized=True`; Save requires explicit `owner_intent=True` |
| One Friend / One Friend Folder | Folder keyed by exact `friend_id` |
| Friend Folder Isolation | A session is bound to one Friend only |
| Bounded Synchronization Session | `SynchronizationSession` has active/terminated lifecycle |
| One Active Friend | Wallet rejects a second active synchronization session |
| Runtime ≠ Persistence | Runtime state is an in-memory copy |
| Owner SAVE | Only `owner_save()` can request M-PIN persistence |
| Save ≠ Commit | Save intent calls validation, then Wallet Commit |
| Atomic Commit | JSON is written to a temporary file, fsynced, then atomically replaced |
| Current-State-Only | Only current state + revision are retained; no state history |
| Disconnect ≠ Save | Disconnect clears unsaved Runtime state without Commit |
| Stale-write protection | Commit checks expected revision before replacing Current State |

## Explicit non-goals in v0.1b

- no M-PIN Hub
- no cloud backup / recovery
- no encryption / key management
- no authentication protocol
- no network transport or REST API
- no AI model dependency
- no LangChain/LlamaIndex/AutoGen integration
- no multi-agent branch/merge
- no rollback/time machine
- no provider infrastructure
- no Friend-native Service Record implementation
- no production-grade crash/recovery journal

These are deliberately excluded so the package proves the smallest core lifecycle first.
