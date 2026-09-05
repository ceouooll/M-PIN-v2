# M-PIN v2.0

## Core 09 — Runtime & Persistence

**Status:** FROZEN **Version:** 2.0 **Document Type:** Normative Core
Specification

------------------------------------------------------------------------

# 1. Purpose

This document defines the Runtime and Persistence model of M-PIN v2.0.

It specifies:

- Runtime State;
- Persistent State;
- Current State;
- Load;
- Owner Save;
- Save versus Commit;
- validation;
- Atomic Commit;
- multiple Saves;
- No-Save behavior;
- Current-State-Only semantics;
- Friend internal persistence;
- Service Records;
- Backup;
- failure and recovery boundaries.

The purpose of this model is to preserve a strict distinction between
temporary service execution and Owner-controlled M-PIN persistence.

------------------------------------------------------------------------

# 2. Persistence Thesis

The canonical M-PIN rule is:

> **Runtime belongs to the service process. Persistence belongs to the
> Owner’s decision.**

Conceptually:

Persistent State ↓ Load ↓ Friend Runtime ↓ Runtime changes ↓ Owner SAVE?
┌──────┴──────┐ YES NO │ │ ▼ ▼ Commit Discard │ relative to ▼ M-PIN New
Current │ State ▼ Previous Current State remains

Runtime change alone does not create M-PIN persistence.

------------------------------------------------------------------------

# 3. Runtime

**Runtime** is the Friend-controlled execution environment in which the
Friend provides its service.

Runtime may include:

- application processes;
- AI inference;
- service logic;
- temporary memory;
- user interaction;
- internal working state;
- service-specific processing.

M-PIN does not replace the Friend Runtime.

------------------------------------------------------------------------

# 4. Runtime State

**Runtime State** is the working state existing during Friend execution.

Runtime State MAY differ from the saved M-PIN state.

Example:

Persistent State A ↓ LOAD ↓ Runtime State A ↓ Friend processing ↓
Runtime State B

At this point:

Runtime State B ≠ Persistent State B

unless the M-PIN persistence process successfully completes.

------------------------------------------------------------------------

# 5. Persistent State

**Persistent State** is the M-PIN state that survives according to M-PIN
persistence rules.

For a Friend relationship, the Friend-specific persistent payload exists
within the associated Friend Folder.

Persistent State is governed by:

- Owner-controlled persistence;
- Friend Folder binding;
- structural validity;
- integrity;
- Commit semantics.

------------------------------------------------------------------------

# 6. Current State

**Current State** is the authoritative successfully committed Persistent
State for the relevant Friend Folder.

Conceptually:

Friend Folder │ ▼ Current State

M-PIN Core requires one authoritative Current State for the applicable
Friend Folder continuity.

------------------------------------------------------------------------

# 7. Current State Is Not Runtime State

The Current State remains authoritative while Runtime changes are
unsaved.

Example:

Friend Folder Current State = A

Runtime: A → B → C → D

before Owner Save:

M-PIN Current State = A

The existence of newer Runtime information does not itself change M-PIN
persistence.

------------------------------------------------------------------------

# 8. Load

`LOAD` makes the applicable Current State available to the authorized
Friend Runtime within a valid Synchronization Session.

Canonical flow:

Friend Folder ↓ Current State A ↓ LOAD ↓ Runtime State A

Load does not transfer ownership of the Friend Folder to the Friend.

Load grants bounded use according to the active Session.

------------------------------------------------------------------------

# 9. Runtime Modification

After Load, the Friend may modify its working state according to its
normal service behavior.

Example:

Runtime State A ↓ operation ↓ Runtime State B ↓ operation ↓ Runtime
State C

M-PIN does not require authorization for every internal Friend
computation over already authorized Runtime State.

Persistence remains separately controlled.

------------------------------------------------------------------------

# 10. Owner Save

`SAVE` is the Owner’s persistence intent under M-PIN.

It means:

> the Owner authorizes the applicable current Friend state to proceed
> through the M-PIN persistence process.

Canonical transition:

Runtime State’ ↓ Owner SAVE ↓ Validation ↓ Commit ↓ New Current State

SAVE is an authorization event.

It is not itself the technical Commit.

------------------------------------------------------------------------

# 11. Save Is Not Commit

M-PIN distinguishes:

# SAVE

Owner persistence intent

from:

# COMMIT

successful technical establishment of the new valid Persistent State

Therefore:

Owner SAVE ↓ Validation ↓ Commit succeeds ↓ new Current State

A Save request that fails validation or Commit does not establish a new
Current State.

------------------------------------------------------------------------

# 12. Friend May Request Save

A Friend MAY present a Save action or request to the Owner.

For example:

Friend: “Save current state?”

The request itself is not Save authority.

The Owner’s applicable persistence decision is required.

------------------------------------------------------------------------

# 13. Friend Cannot Manufacture Save

A Friend MUST NOT convert its own Runtime activity into M-PIN Save
authority.

The following do not inherently constitute M-PIN SAVE:

- Friend autosave;
- cache write;
- database write;
- model memory update;
- transaction completion;
- application close;
- Session timeout;
- network disconnect;
- Device removal;
- Friend switching.

M-PIN Save has the specific Owner-controlled meaning defined by the
Core.

------------------------------------------------------------------------

# 14. Persistence Proposal

After Owner Save, the Friend or conforming implementation supplies the
representation necessary to establish the intended new persistent state.

This MAY be expressed as:

- full state;
- delta;
- transaction;
- chunked update;
- another conforming mechanism.

The representation is an implementation matter.

The semantic persistence result is normative.

------------------------------------------------------------------------

# 15. Decision 095 Resolution

M-PIN v2 resolves the architectural question represented by v1 Decision
095 as follows:

> **Owner SAVE authorizes a transition from the current valid Friend
> Folder Persistent State to exactly one new valid current Friend Folder
> Persistent State.**

The Friend MAY communicate that transition using a full-state
representation, delta, transaction, or another conforming mechanism.

M-PIN v2 does not require one historical update model or one transport
encoding.

After successful Commit, the semantic result is:

Current State A ↓ Current State B

with State B becoming the single authoritative Current State.

------------------------------------------------------------------------

# 16. Validation

Before Commit, M-PIN MUST validate the M-PIN-level conditions necessary
to accept the persistence transition.

These include as applicable:

- valid Owner Save authority;
- valid Synchronization Session;
- correct Friend Identity;
- correct Friend Folder binding;
- required structural validity;
- required integrity.

Validation MUST fail closed when a required condition cannot be
established.

------------------------------------------------------------------------

# 17. Structural Validation

M-PIN MAY validate structural properties necessary for the M-PIN
boundary.

Examples include:

- required Envelope fields;
- identifier association;
- Friend Folder binding;
- supported format/version information;
- integrity metadata;
- persistence object completeness.

Structural Validation does not require semantic understanding of the
Friend’s entire payload.

------------------------------------------------------------------------

# 18. Semantic Validation

Friend-specific semantic validation remains primarily the responsibility
of the Friend.

For example, M-PIN does not need to understand whether:

- a conversation graph is logically correct;
- a medical field is clinically correct;
- a product preference is meaningful;
- a robot configuration is behaviorally appropriate.

M-PIN integrity does not imply semantic truth.

------------------------------------------------------------------------

# 19. Commit

`COMMIT` is the technical operation that establishes the new valid
Persistent State as authoritative.

A Commit occurs only after required validation succeeds.

Conceptually:

Validated proposed state ↓ COMMIT ↓ New Current State

A Commit MUST preserve Atomic Commit semantics.

------------------------------------------------------------------------

# 20. Atomic Commit

Atomic Commit means the authoritative result is either:

State A → State B

or, if Commit fails:

State A → State A

The system MUST NOT accept:

State A → partial/corrupted State B

as the authoritative Current State.

------------------------------------------------------------------------

# 21. Commit Visibility

A new Current State MUST NOT be treated as successfully established
before the Commit reaches the implementation’s required atomic success
point.

The exact storage transaction mechanism is implementation-defined.

The observable persistence semantics are normative.

------------------------------------------------------------------------

# 22. Commit Failure

If Commit fails:

- the previous valid Current State remains authoritative;
- the failed proposed state MUST NOT be represented as successfully
  saved;
- the implementation MAY permit another Save attempt if the Session
  remains valid;
- the implementation MAY terminate the Session if required for safety or
  integrity.

The failure MUST NOT silently corrupt the authoritative state.

------------------------------------------------------------------------

# 23. Disconnect During Commit

If a required Session dependency fails during Commit, the resulting
authoritative state MUST still satisfy Atomic Commit.

After recovery or reconnection, the valid result MUST resolve to either:

Previous Current State A

or:

Fully committed Current State B

not an accepted partial intermediate state.

------------------------------------------------------------------------

# 24. Multiple Saves

A valid Session MAY contain multiple Saves.

Example:

Current State A ↓ LOAD Runtime ↓ Owner SAVE Current State B ↓ Runtime
continues ↓ Owner SAVE Current State C

After the second successful Commit:

Current State = C

The Core does not require A or B to remain available as historical M-PIN
versions.

------------------------------------------------------------------------

# 25. Current-State-Only

M-PIN v2 preserves the v1 Last-Save-Only / Current-State-Only principle.

The Core persistence model is:

Current Stateₙ ↓ successful Commit ↓ Current Stateₙ₊₁

The new Current State replaces the previous Current State as the
authoritative Friend Folder state.

------------------------------------------------------------------------

# 26. No Core Version History

M-PIN Core does not require:

- version history;
- time travel;
- automatic snapshots of every Save;
- rollback to every prior Save;
- perpetual archival state;
- hidden historical copies.

These features are not part of the normative M-PIN persistence model.

------------------------------------------------------------------------

# 27. Current-State-Only Does Not Mean Content-Only-Present-Time

Current-State-Only applies to M-PIN state versions.

It does not prohibit the current Friend payload from containing
historical service content.

For example, one current AI Friend payload may contain:

- old conversations;
- previous messages;
- persistent memories.

One current Commerce Friend payload may contain:

- prior orders;
- receipts;
- warranty information.

One current healthcare payload may contain:

- historical health documents.

Therefore:

historical content inside Current State ≠ historical M-PIN state
versions

This distinction is normative.

------------------------------------------------------------------------

# 28. No Automatic Rollback

Because M-PIN Core does not define version history, it does not
guarantee automatic rollback to a prior Save.

Recovery from Backup is a different mechanism.

A future optional implementation feature MUST NOT be represented as a
required Core property.

------------------------------------------------------------------------

# 29. Backup Is Not Version History

A **Backup** is a resilience copy intended to recover valid state after
loss or corruption.

Backup does not redefine the normal persistence model as historical
versioning.

Conceptually:

Current authoritative State C │ └── protected Backup

is different from:

State A State B State C State D all maintained as user-facing M-PIN
version history

The latter is not required by Core.

------------------------------------------------------------------------

# 30. Backup May Be Older

A Backup MAY contain an older valid state than the currently
authoritative state.

This does not make the Backup an active historical version.

If restoration is required, freshness and recovery rules determine what
can legitimately become authoritative.

Detailed recovery rules are defined in Core 11.

------------------------------------------------------------------------

# 31. Backup Restoration

Restoring a Backup is a recovery operation, not ordinary Runtime
rollback.

Conceptually:

failure/loss ↓ Recovery ↓ validate recoverable Backup ↓ restore
authoritative continuity

The exact recovery algorithm is deferred.

------------------------------------------------------------------------

# 32. No Save

If no Owner Save occurs:

Persistent State A ↓ LOAD Runtime State A ↓ WORK Runtime State B ↓ NO
SAVE ↓ Session ends ↓ Persistent State A remains

This is a fundamental M-PIN invariant.

------------------------------------------------------------------------

# 33. Discard

`Discard` means unsaved Runtime changes are not committed into M-PIN
Persistent State.

It does not necessarily mean every copy of the Runtime data is
physically erased from every Friend system.

The Friend may have:

- temporary caches;
- legitimate Service Records;
- operational state;
- malicious retained copies.

M-PIN uses `Discard` specifically with respect to M-PIN persistence.

------------------------------------------------------------------------

# 34. Session Termination

Session termination MUST NOT itself trigger M-PIN persistence.

Therefore:

Session end ≠ SAVE

and:

Friend close ≠ SAVE

and:

Device disconnect ≠ SAVE

The previous committed Current State remains authoritative unless a
Commit had already succeeded.

------------------------------------------------------------------------

# 35. Abnormal Disconnect

An abnormal disconnect does not create an exception to Owner-controlled
persistence.

Example:

Current State A ↓ Runtime State B ↓ USB removed / transport lost /
required dependency fails ↓ Session terminates ↓ Current State A remains

if State B had not already been successfully committed.

------------------------------------------------------------------------

# 36. Friend Switching

Switching from Friend A to Friend B MUST NOT implicitly persist Friend
A’s unsaved Runtime State.

Canonical behavior:

Friend A Runtime ↓ no Save ↓ terminate Friend A Session ↓ Friend A
previous Current State remains ↓ establish Friend B Session

Friend switching is a Session operation, not a Save operation.

------------------------------------------------------------------------

# 37. Friend Internal Persistence

A Friend MAY maintain persistence independent of M-PIN.

Examples include:

- service databases;
- caches;
- draft storage;
- operational state;
- transaction systems;
- safety logs;
- institutional records.

Such persistence belongs to the Friend’s own service architecture unless
it is explicitly part of the M-PIN Friend Folder persistence path.

------------------------------------------------------------------------

# 38. Friend Internal Autosave

Friend internal autosave does not equal M-PIN Save.

For example:

Friend Runtime ↓ internal autosave ↓ Friend internal storage

does not imply:

Owner SAVE ↓ M-PIN Commit

The distinction MUST remain visible in conformance behavior.

------------------------------------------------------------------------

# 39. Friend Workspace

M-PIN does not replace the Friend’s normal workspace.

The Friend may maintain temporary or internal working state necessary to
provide the service.

M-PIN’s role is to govern the Owner-controlled persistent boundary, not
to eliminate Friend Runtime architecture.

------------------------------------------------------------------------

# 40. Friend Persistence Autonomy

Friend Sovereignty permits the Friend to maintain internal persistence
necessary for its own service.

However, Friend Persistence Autonomy MUST NOT be used to redefine
Owner-controlled M-PIN Friend Folder state as Friend-owned persistence.

The two categories remain separate.

------------------------------------------------------------------------

# 41. Service Record

A **Service Record** is a legitimate record independently maintained by
a Friend for its own service, operational, contractual, institutional,
safety, security, or legal responsibilities.

Examples may include:

- completed commerce transaction record;
- invoice;
- hospital clinical record;
- prescription record;
- fraud record;
- security audit record;
- robot safety record.

A Service Record is not automatically M-PIN Friend Folder state.

------------------------------------------------------------------------

# 42. Service Record Independence

The same real-world event may affect both:

- M-PIN Friend Folder state;
- Friend Service Records.

Example:

Commerce transaction completed ↓ Merchant transaction record exists

Owner chooses SAVE ↓ updated Owner Commerce Friend Folder may also be
committed

These are separate persistence events.

------------------------------------------------------------------------

# 43. Transaction Is Not Save

A transaction completing outside M-PIN does not automatically authorize
M-PIN persistence.

For example:

payment completed ≠ Owner SAVE

purchase completed ≠ Owner SAVE

refund completed ≠ M-PIN rollback

The Commerce Profile defines these boundaries further.

------------------------------------------------------------------------

# 44. Clinical Record Is Not Save

A healthcare institution may be required to create or maintain a
clinical record independently of M-PIN.

Therefore:

clinical record creation ≠ M-PIN Owner SAVE

and:

no M-PIN SAVE ≠ institution must erase clinical record

The Healthcare Profile defines this distinction further.

------------------------------------------------------------------------

# 45. Physical Action Is Not Save

A robot performing a physical action does not automatically mean the
resulting Runtime state must be persisted to M-PIN.

Therefore:

robot action ≠ M-PIN SAVE

Physical action authority and persistence authority remain distinct.

------------------------------------------------------------------------

# 46. AI Internal Memory Is Not Save

An AI Friend may maintain internal temporary or service-specific memory
mechanisms.

Those mechanisms do not automatically redefine M-PIN persistence.

AI internal memory update ≠ M-PIN Owner SAVE

Only the M-PIN persistence path establishes new M-PIN Current State.

------------------------------------------------------------------------

# 47. Service Record Anti-Loophole

Service Record classification MUST NOT be used to bypass M-PIN
persistence boundaries.

A Friend MUST NOT:

1.  receive the Owner’s complete synchronized Friend Folder;
2.  copy it into independent storage;
3.  label that copy a Service Record;
4.  thereby claim M-PIN persistence rules no longer matter.

Service Records must have an independently legitimate service,
operational, contractual, institutional, security, safety, or legal
basis.

------------------------------------------------------------------------

# 48. Runtime Cache

A Friend MAY use Runtime cache necessary for service execution.

Runtime cache MUST NOT automatically become authoritative M-PIN
Persistent State.

Cache lifetime and cleanup remain Friend implementation matters subject
to applicable security and Profile requirements.

------------------------------------------------------------------------

# 49. Temporary Staging

A conforming M-PIN implementation MAY use temporary staging during
Commit.

For example:

proposed State B ↓ temporary staging ↓ validate ↓ atomic switch ↓ State
B authoritative

Temporary staging does not violate Current-State-Only if it is
implementation machinery rather than exposed M-PIN version-history
semantics.

------------------------------------------------------------------------

# 50. Crash-Safe Persistence

A conforming implementation MUST design Commit so that interruption does
not leave a corrupted partial state as authoritative.

Possible implementation techniques MAY include:

- transactional storage;
- write-then-rename;
- copy-on-write;
- journal-assisted commit;
- object replacement;
- another crash-safe mechanism.

M-PIN v2 does not mandate one technique.

The crash-safe property is normative.

------------------------------------------------------------------------

# 51. Persistence Integrity

Persistent State MUST have sufficient integrity protection to detect or
prevent unauthorized modification from being silently accepted as valid.

The exact cryptographic integrity mechanism is deferred.

Integrity does not prove Friend payload semantic correctness.

------------------------------------------------------------------------

# 52. Persistence Confidentiality

Persistent Friend Folder state MUST be protected from unauthorized
disclosure according to Core 10.

Encryption at rest is required by the M-PIN security model.

The exact encryption algorithm, key hierarchy, and Provider visibility
model remain deferred.

------------------------------------------------------------------------

# 53. Authorized Friend Plaintext

An authorized Friend may receive plaintext from its own Friend Folder as
required to provide its service.

Therefore M-PIN does not claim:

authorized Friend ↓ can never see plaintext

Such a claim would contradict the Runtime model.

The security boundary instead prevents unauthorized and cross-Friend
access.

------------------------------------------------------------------------

# 54. Malicious Authorized Friend

If an authorized Friend is malicious or compromised after legitimately
receiving its own plaintext, M-PIN cannot guarantee that the Friend will
forget or erase that plaintext.

M-PIN can still enforce boundaries around:

- other Friend Folders;
- future Session authority;
- future Save authority;
- revocation;
- M-PIN persistent state.

This limitation MUST remain explicit.

------------------------------------------------------------------------

# 55. Persistence and Revocation

Revoking Friend access does not automatically delete existing Persistent
State.

Conceptually:

revoke Friend authority ≠ delete Friend Folder

The Owner may later:

- reconnect;
- migrate;
- recover;
- delete according to applicable lifecycle rules.

------------------------------------------------------------------------

# 56. Persistence and Friend Account Deletion

Deleting or closing a Friend Account does not automatically define what
happens to the Friend Folder.

Friend service lifecycle and M-PIN persistence lifecycle remain
distinct.

An implementation MUST avoid exposing old Owner-controlled state to an
unauthorized replacement account.

------------------------------------------------------------------------

# 57. Persistence and M-PIN Deletion

Deletion of an M-PIN is a broader lifecycle operation than Session
termination or Friend Folder revocation.

M-PIN deletion MUST NOT be represented as automatically deleting
independent Friend Service Records.

The exact secure-deletion mechanism is outside this document’s frozen
architecture scope.

------------------------------------------------------------------------

# 58. Persistent State and Device Independence

Persistent State belongs to M-PIN continuity, not one Device.

Conceptually:

Device A ↓ M-PIN X / Current State

migration or recovery

Device B ↓ same M-PIN X / Current State

where the applicable migration or recovery succeeds.

------------------------------------------------------------------------

# 59. Persistent State and Storage Independence

Moving M-PIN state between compatible Storage environments MUST NOT
inherently change its semantic ownership or identity.

Storage A ↓ Current State X ↓ migrate Storage B ↓ Current State X

The migration must preserve required identity and integrity.

------------------------------------------------------------------------

# 60. Persistent State and Provider Independence

Where a Provider participates, Provider migration SHOULD preserve the
same M-PIN Current State and Friend Folder relationships.

Provider change does not inherently create new persistent ownership.

Provider A ↓ M-PIN X ↓ migration Provider B ↓ same M-PIN X

where migration succeeds.

------------------------------------------------------------------------

# 61. Provider Persistence

A Provider MAY physically store M-PIN Persistent State.

Physical storage does not make the Provider the architectural Owner.

The Provider’s ability to observe plaintext depends on the
implementation’s key and trust model.

M-PIN v2 does not assume universal zero-knowledge Provider storage.

------------------------------------------------------------------------

# 62. Provider Failure

If a Provider fails, M-PIN recovery depends on whether sufficient valid
state, keys, authority, and recovery material remain available
elsewhere.

Provider Independence is an architectural requirement.

It is not a claim that data can be recovered after every possible loss
scenario.

------------------------------------------------------------------------

# 63. Recovery Is Not Rollback

Recovery restores a valid M-PIN continuity from available legitimate
recovery material.

It is not equivalent to user-facing version rollback.

Conceptually:

Recovery ≠ “show me every old Save”

A Backup may happen to contain an older state.

That does not turn Core persistence into a version-history system.

------------------------------------------------------------------------

# 64. Recovery Cannot Invent State

If no valid copy of a required Persistent State exists, authority
recovery alone cannot reconstruct that data.

Therefore:

Authority Recovery ≠ Data Recovery

and:

successful identity recovery ≠ guaranteed data reconstruction

This limitation is normative.

------------------------------------------------------------------------

# 65. Current State Freshness

When multiple legitimate copies exist for Backup, migration, or
recovery, the implementation MUST have sufficient means to determine
which state may become authoritative.

The exact freshness mechanism is deferred.

Possible mechanisms MAY involve:

- generation values;
- counters;
- integrity-protected metadata;
- trusted coordination;
- other conforming mechanisms.

------------------------------------------------------------------------

# 66. Offline Clone Limitation

Two fully disconnected copies cannot always know which is globally
newest or active without coordination.

Therefore M-PIN v2 distinguishes:

one authoritative Current State within one authoritative active
continuity

from:

perfect global conflict prevention among fully disconnected clones

The latter is deferred.

------------------------------------------------------------------------

# 67. Persistence Conflict

A conforming implementation MUST NOT silently merge conflicting M-PIN
states in a way that invents Friend payload semantics M-PIN does not
understand.

Where conflicting copies cannot be safely resolved structurally, the
implementation SHOULD fail closed or require an explicit
recovery/migration resolution.

M-PIN MUST NOT semantically merge arbitrary Friend payloads.

------------------------------------------------------------------------

# 68. Friend Payload Semantics

The Friend remains responsible for the meaning and service-specific
composition of its payload.

M-PIN persistence operates around that payload.

Conceptually:

Friend-defined payload ↓ M-PIN structural/integrity boundary ↓ Friend
Folder Current State

M-PIN does not become the semantic owner of Friend data formats.

------------------------------------------------------------------------

# 69. Decision 120 Boundary

M-PIN v2 resolves Decision 120 in principle:

Friend: - defines payload meaning; - defines service-specific payload
structure; - manages semantic evolution.

M-PIN: - defines minimum Envelope/boundary metadata; - preserves
identity and binding; - validates required structure; - preserves
integrity; - governs persistence transition.

The exact `.MPIN` container and serialization remain deferred.

------------------------------------------------------------------------

# 70. Payload Schema Evolution

A Friend MAY evolve its payload schema.

The Friend remains responsible for semantic compatibility or migration.

M-PIN MAY reject structurally unsupported or integrity-invalid objects.

M-PIN MUST NOT invent semantic migration rules for arbitrary Friend
payloads.

------------------------------------------------------------------------

# 71. Persistence Envelope

A future concrete implementation may require a minimum persistence
Envelope containing fields conceptually related to:

- M-PIN identity;
- Friend identity;
- Friend Folder identity/binding;
- format/version;
- integrity;
- state generation/freshness.

M-PIN v2 freezes the need for sufficient boundary metadata.

It does not freeze the exact field names or serialization.

------------------------------------------------------------------------

# 72. Disclosure Persistence Boundary

Owner-Mediated Disclosure remains deferred from Core.

If a future Disclosure mechanism is defined, receiving selected data
from another Friend MUST NOT automatically bypass the recipient Friend’s
M-PIN persistence rules.

Conceptually:

Disclosure received by Friend B ↓ Friend B Runtime ↓ Owner SAVE?
┌──────┴──────┐ YES NO │ │ ▼ ▼ possible no automatic Commit to M-PIN
persistence Folder B

This is a compatibility constraint for future interoperability work.

------------------------------------------------------------------------

# 73. Persistence Requirements

A conforming M-PIN v2 implementation MUST satisfy:

### RP-001 — Runtime/Persistence Separation

Friend Runtime State MUST remain distinct from M-PIN Persistent State
until a valid persistence transition succeeds.

### RP-002 — Current State

Each Friend Folder MUST have one authoritative Current State for the
applicable active continuity.

### RP-003 — Owner Save

M-PIN persistence MUST require the applicable Owner Save authority.

### RP-004 — Save/Commit Separation

Owner Save intent MUST remain distinguishable from successful technical
Commit.

### RP-005 — Validation

Commit MUST NOT proceed without required M-PIN-level validation.

### RP-006 — Atomic Commit

Commit MUST establish a complete valid new Current State or leave the
previous valid Current State authoritative.

### RP-007 — No Implicit Save

Session termination, disconnect, timeout, Friend switching, or internal
Friend autosave MUST NOT automatically create M-PIN persistence.

### RP-008 — Multiple Saves

Multiple Saves MAY occur in one valid Session, with each successful
Commit replacing the authoritative Current State.

### RP-009 — Current-State-Only

Core MUST NOT require M-PIN version-history semantics.

### RP-010 — Historical Content Allowed

Current-State-Only MUST NOT prohibit historical service content inside
the current Friend payload.

### RP-011 — Backup Distinction

Backup MUST remain distinct from ordinary M-PIN version history.

### RP-012 — Service Record Distinction

Legitimate independent Friend Service Records MUST remain distinct from
M-PIN Friend Folder persistence.

### RP-013 — Service Record Anti-Loophole

Service Record classification MUST NOT be used to bypass
Owner-controlled M-PIN persistence.

### RP-014 — Integrity

Unauthorized or corrupted persistent state MUST NOT be silently accepted
as valid.

### RP-015 — Friend Semantic Authority

The Friend remains responsible for Friend-specific payload semantics.

### RP-016 — M-PIN Semantic Neutrality

M-PIN MUST NOT require complete semantic interpretation of Friend
payloads to perform its persistence role.

### RP-017 — Recovery Distinction

Recovery MUST NOT be represented as Core version-history rollback.

### RP-018 — Fail Closed

If a required persistence condition cannot be established, the affected
Commit MUST fail closed.

------------------------------------------------------------------------

# 74. Recommended Persistence Properties

A conforming implementation SHOULD additionally preserve:

### RP-019 — Crash Safety

Commit implementation SHOULD remain safe under interruption or process
failure.

### RP-020 — Minimal Staging

Temporary staging SHOULD exist only as necessary for safe Commit and
SHOULD NOT become hidden user-facing version history.

### RP-021 — Freshness Protection

Backup, migration, and recovery SHOULD preserve sufficient freshness
information to reduce stale-state activation.

### RP-022 — Conflict Safety

Unresolvable conflicting copies SHOULD fail closed rather than trigger
semantic merging by M-PIN.

### RP-023 — Provider Portability

Where Providers are used, persistent state SHOULD remain exportable in a
manner sufficient for conforming migration.

------------------------------------------------------------------------

# 75. Canonical Persistence State Machine

The logical persistence state machine is:

CURRENT STATE A │ │ LOAD ▼ RUNTIME STATE A │ │ Friend processing ▼
RUNTIME STATE B │ ├──────────── NO SAVE ─────────────┐ │ │ │ Owner SAVE
▼ ▼ SESSION TERMINATION SAVE REQUESTED │ │ ▼ ▼ CURRENT STATE A
VALIDATING remains │ ├── failure ───────────────► State A remains │ ▼
COMMITTING │ ├── failure ───────────────► State A remains │ ▼ CURRENT
STATE B │ └── becomes authoritative

# 76. Canonical Multiple-Save Flow

Current State A ↓ Load ↓ Runtime ↓ Save ↓ Commit ↓ Current State B ↓
Runtime continues ↓ Save ↓ Commit ↓ Current State C The authoritative
state is C. A and B need not remain available as M-PIN historical
versions.

# 77. Canonical Failure Flow

Current State A ↓ Runtime State B ↓ Owner SAVE ↓ Validation succeeds ↓
Commit begins ↓ failure ↓ Atomic Commit resolution ↓ Current State A
remains authoritative unless the implementation can prove that State B
completed the atomic Commit before failure.

# 78. Canonical Service Record Separation

                    FRIEND
                   /      \
                  /        \
                 ▼          ▼
           Friend Runtime  Service Record
                 │
                 │
                 │ Owner SAVE
                 ▼
              M-PIN
                 │
                 ▼
          Friend Folder
          Current State

The Service Record path and M-PIN persistence path are not the same
path.

# 79. Persistence Non-Goals

M-PIN v2.0 Core does not define: universal autosave; perpetual version
history; time travel; automatic rollback; semantic payload merging; one
database engine; one filesystem; one transaction technology; one backup
provider; one cloud storage system; one serialization format. These are
outside the frozen architectural persistence model.

# 80. Deferred Persistence Mechanisms

The following remain deferred: exact .MPIN container serialization
Envelope schema state generation encoding freshness mechanism
integrity-proof format crypto algorithms key hierarchy atomic-storage
implementation backup format backup freshness protocol
conflict-resolution protocol Their deferral does not reopen the
Runtime/Persistence architecture.

# 81. Persistence Invariants

The Runtime & Persistence model is governed by these invariants: \##
Runtime is not Persistence. \## Load is not ownership transfer. \##
Runtime modification is not Save. \## Save is Owner persistence intent.
\## Save is not Commit. \## A successful Commit establishes one new
authoritative Current State. \## A failed Commit leaves the previous
valid Current State authoritative. \## Disconnect is not Save. \##
Friend switching is not Save. \## Friend autosave is not M-PIN Save. \##
Current-State-Only prohibits Core version-history semantics, not
historical content inside the current payload. \## Backup is not version
history. \## Recovery is not rollback. \## Service Records are distinct
and cannot be used as a persistence loophole. \## M-PIN preserves the
persistence boundary without taking over Friend payload semantics.

# 82. Persistence Thesis

The complete M-PIN persistence model can be expressed as: Persistent
State₀ ↓ Load ↓ Runtime State ↓ Friend processing ↓ Runtime State′ ↓
Owner SAVE ↓ Validation ↓ Atomic Commit ↓ Persistent State₁ Without
Save: Persistent State₀ ↓ Load ↓ Runtime State′ ↓ Session end ↓ Discard
relative to M-PIN ↓ Persistent State₀ unchanged The Friend determines
what the service does. The Owner determines whether the resulting M-PIN
state persists. M-PIN preserves the boundary between those two
decisions.

## M-PIN v2.0 — Core 09 / Runtime & Persistence

## Status: FROZEN
