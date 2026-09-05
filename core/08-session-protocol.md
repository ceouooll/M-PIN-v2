# M-PIN v2.0

## Core 08 — Session Protocol

**Status:** FROZEN **Version:** 2.0 **Document Type:** Normative Core
Specification

------------------------------------------------------------------------

# 1. Purpose

This document defines the canonical Synchronization Session protocol of
M-PIN v2.0.

It specifies:

- Session establishment;
- Owner Authority establishment;
- Friend Identity verification;
- Friend Folder resolution;
- first-use Folder creation;
- current-state Load;
- active Runtime behavior;
- Save and Commit behavior;
- No-Save behavior;
- revocation;
- abnormal disconnect;
- Session termination;
- reconnection;
- Session security invariants.

The protocol defines observable architectural behavior.

It does not mandate one transport, network protocol, API, SDK,
Session-token format, or heartbeat mechanism.

------------------------------------------------------------------------

# 2. Session Thesis

M-PIN access is bounded.

A Friend does not obtain permanent M-PIN authority merely because it has
synchronized before.

The canonical model is:

``` text
No Active Session
        ↓
Establish Authority
        ↓
Verify Friend
        ↓
Resolve Friend Folder
        ↓
Open Session
        ↓
Load Current State
        ↓
Friend Runtime
        ↓
Save / No Save
        ↓
Terminate Session
After termination:
```

## the terminated Session no longer carries M-PIN authority.

# 3. Synchronization Session

A Synchronization Session is the bounded authorization context through
which one active Friend interacts with its associated Friend Folder. The
canonical v2 invariant is: \## One M-PIN, One Active Friend, One
Synchronization Session. A Session MUST have an identifiable beginning
and termination boundary.

# 4. Session Is Not Friend Runtime

The Synchronization Session and Friend Runtime are related but distinct.
M-PIN Synchronization Session │ ▼ authorized M-PIN boundary

Friend Runtime │ ▼ Friend-controlled service execution A Friend Runtime
MAY exist before or after an M-PIN Session. Termination of the M-PIN
Session does not necessarily terminate the Friend’s entire service
Runtime.

# 5. Session Is Not Friend Account Login

A Friend’s own login Session does not automatically constitute an M-PIN
Synchronization Session. Conceptually: Friend Account Login ≠ M-PIN
Synchronization Session A user may be logged into a Friend while no
M-PIN Session is active.

# 6. Canonical Session States

M-PIN v2 defines the following logical Session states: IDLE ↓
AUTHORIZING ↓ VERIFYING_FRIEND ↓ RESOLVING_FOLDER ↓ ESTABLISHING_SESSION
↓ LOADING ↓ ACTIVE ↓ TERMINATING ↓ TERMINATED During ACTIVE, Save
operations MAY introduce temporary persistence sub-states: ACTIVE ↓
SAVE_REQUESTED ↓ VALIDATING_SAVE ↓ COMMITTING ↓ ACTIVE A failed Save may
return to ACTIVE if the Session remains valid.

# 7. IDLE

IDLE means no active Synchronization Session exists for the relevant
authoritative M-PIN continuity. In IDLE: Active Friend = none Active
Session = none Existing Friend Folders and persistent relationships MAY
still exist.

# 8. AUTHORIZING

AUTHORIZING establishes the Owner authority required to begin
synchronization. The implementation MUST establish sufficient Owner
Authority before granting Friend access to M-PIN. Failure to establish
required Owner Authority MUST return to a non-active state. No Friend
Folder payload MUST be exposed merely because authorization was
attempted.

# 9. VERIFYING_FRIEND

VERIFYING_FRIEND establishes the identity of the Friend requesting the
M-PIN relationship. The Friend MUST be verified sufficiently to support:
correct Friend distinction; Friend Folder binding; permission
evaluation; Session security. A display name alone is insufficient. If
required Friend Identity cannot be established: VERIFYING_FRIEND ↓ FAIL
↓ no Session

# 10. RESOLVING_FOLDER

After Friend Identity is verified, M-PIN resolves the Friend Folder
associated with that Friend. Conceptually: Verified Friend Identity ↓
resolve binding ↓ Friend Folder The Friend MUST NOT receive authority to
choose an arbitrary unrelated Folder.

# 11. Existing Friend Folder

If the Friend Folder already exists: RESOLVING_FOLDER ↓ existing binding
found ↓ binding validated ↓ ESTABLISHING_SESSION The existing Friend
Folder MUST be reused for the continuing Friend relationship.

# 12. Missing Friend Folder

If no Friend Folder exists: RESOLVING_FOLDER ↓ Folder absent ↓ request
Owner approval The system MUST NOT silently create the Folder.

# 13. Folder Creation Approval

If the Owner authorizes creation: Folder absent ↓ Owner approval ↓
create Friend Folder ↓ bind verified Friend ↓ ESTABLISHING_SESSION The
new Folder MUST be bound to the verified Friend relationship.

# 14. Folder Creation Denial

If the Owner denies creation: Folder absent ↓ Owner denies ↓ no Folder
created ↓ no M-PIN Session The Friend MAY continue operating
independently outside M-PIN.

# 15. ESTABLISHING_SESSION

After authority, Friend verification, and Folder resolution succeed,
M-PIN establishes a new Synchronization Session. The Session MUST be
bound to at least the logical context of: M-PIN Owner-authorized
authority Friend Identity Friend Folder Session identity/freshness
context The exact Session object is deferred.

# 16. New Session Identity

A newly established Session MUST be distinguishable from a previously
terminated Session in a way sufficient to prevent stale authority from
being accepted as current authority. Conceptually: Session 1 ↓
terminated

Session 2 ≠ Session 1 authority The exact Session identifier, nonce,
token, generation, or freshness mechanism is deferred.

# 17. LOADING

After the Session is established, M-PIN makes the current authorized
Friend Folder state available to the Friend. Friend Folder ↓ Current
State ↓ LOAD ↓ Friend Runtime Only the active Friend’s own authorized
Friend Folder state may be loaded through that Session.

# 18. Read Once Semantics

The initial Load preserves the v1 Read Once principle. Read Once means:
the Friend receives the relevant saved state for use in the authorized
Session rather than receiving perpetual unrestricted background M-PIN
access. It does not require one physical read operation. An
implementation MAY use: streaming; chunks; multiple protocol frames;
lazy retrieval; another conforming transfer mechanism provided that
these operations remain within the same authorized Session and do not
create hidden post-Session access.

# 19. ACTIVE

After successful Load, the Session becomes ACTIVE. During ACTIVE: the
Friend may use the authorized state in its Runtime; the Friend may
perform its normal service operations; Runtime State may change; the
Owner may authorize one or more Saves; the Owner may terminate or revoke
M-PIN authority; required security conditions must remain valid.

# 20. Active Runtime

Conceptually: Current Persistent State A ↓ LOAD Runtime State A ↓ Friend
processing ↓ Runtime State B Runtime State B is not automatically M-PIN
Persistent State.

# 21. One Active Friend

While Friend A has the active Synchronization Session: M-PIN ↓ Session A
↓ Friend A M-PIN MUST NOT simultaneously establish: M-PIN ├── active
Session A → Friend A └── active Session B → Friend B within the same
authoritative active continuity.

# 22. Second Friend Request

If another Friend requests synchronization while a Session is already
active, M-PIN MUST preserve the one-active-Friend invariant. The
implementation MAY: deny the second request; wait until the active
Session terminates; ask the Owner to terminate/switch the existing
Session; use another conforming behavior. It MUST NOT create two
simultaneous active Friend synchronization authorities.

# 23. Friend Switching

Switching from Friend A to Friend B requires termination of Friend A’s
active M-PIN Session before Friend B becomes active. Conceptually:
Friend A Session ↓ terminate ↓ IDLE / transition boundary ↓ Friend B
authorization ↓ new Friend B Session Switching Friends MUST NOT
implicitly Save Friend A’s unsaved Runtime State.

# 24. SAVE_REQUESTED

When the Owner expresses persistence intent during an active Session:
ACTIVE ↓ Owner SAVE ↓ SAVE_REQUESTED Save authority applies to the
active Friend relationship. The Friend’s own internal autosave does not
cause this state transition.

# 25. Save Request by Friend

A Friend MAY request or suggest that the Owner Save. For example:
Friend: “Save current state?” The request is not itself authorization.
Only the applicable Owner persistence decision establishes M-PIN Save
authority.

# 26. VALIDATING_SAVE

Before Commit, M-PIN validates the required M-PIN-level conditions.
These MUST include as applicable: Owner Save authority active Session
validity Friend Identity Friend Folder binding required structural
validity required integrity M-PIN need not validate all Friend-specific
business semantics.

# 27. Decision 095 Semantic Rule

The semantic target of Save is: \## one new valid current persistent
state for the active Friend Folder. Conceptually: Current State A ↓
Owner SAVE ↓ validated persistence transition ↓ Current State B This
does not mandate one transfer encoding. The Friend MAY convey the
intended state transition through: full state; delta; transaction;
chunked representation; another conforming mechanism. The final
authoritative semantic result MUST be one valid Current State.

# 28. COMMITTING

After Save validation succeeds, the persistence operation enters
COMMITTING. Conceptually: VALIDATING_SAVE ↓ success COMMITTING ↓
Persistent State transition Commit MUST preserve atomic semantics.

# 29. Atomic Commit

The valid Commit outcomes are: State A → State B or, on failure: State A
→ State A The system MUST NOT accept an incomplete corrupted
intermediate state as the authoritative Current State.

# 30. Successful Commit

After a successful Commit: Current State B becomes the authoritative
current persistent state of the active Friend Folder. If the Session
remains valid, the protocol MAY return to: ACTIVE and the Friend may
continue working.

# 31. Multiple Saves

A single Session MAY contain multiple Save cycles. ACTIVE ↓ Save COMMIT
↓ State B ↓ ACTIVE ↓ Save COMMIT ↓ State C ↓ ACTIVE The latest
successful Commit defines the Current State. The Core does not require
earlier committed states to remain available as version history.

# 32. Save Failure

If Save validation or Commit fails, the previous valid Current State
MUST remain authoritative. Conceptually: State A ↓ attempted Save Commit
failure ↓ State A remains The implementation MAY: return to ACTIVE if
the Session remains safe and valid; terminate the Session if required;
request a new Save attempt. It MUST NOT claim the failed state was
successfully committed.

# 33. No-Save Runtime

The Friend may continue Runtime activity without Save. Current State A ↓
Runtime State B ↓ Runtime State C Until Owner Save succeeds: M-PIN
Current State = A

# 34. Session Termination Without Save

If the Session terminates without Save of the current unsaved Runtime
changes: Current State A ↓ Runtime State B ↓ NO SAVE ↓ TERMINATION ↓
Current State A remains M-PIN MUST NOT automatically Commit Runtime
State B.

# 35. Friend Internal Autosave

A Friend MAY internally autosave its own Runtime or Service Record
state. That internal action MUST NOT be interpreted as M-PIN Save.
Friend internal autosave ≠ Owner SAVE The M-PIN Session protocol is
governed by the explicit M-PIN persistence boundary.

# 36. TERMINATING

TERMINATING is the transition in which active M-PIN Session authority is
being closed. Termination processing MAY include: invalidating Session
authority; releasing temporary M-PIN resources; clearing transient
access material; completing required security cleanup; recording minimal
security/audit metadata. Termination MUST NOT silently Save unsaved
Runtime State.

# 37. TERMINATED

TERMINATED means the Session no longer carries valid M-PIN access
authority. After termination: Session access authority = invalid The
Friend MUST NOT continue accessing the Friend Folder through the
terminated Session.

# 38. Termination Does Not Delete Folder

Session termination does not delete the Friend Folder. terminate Session
≠ delete Friend Folder The persistent relationship may remain for a
future Session.

# 39. Termination Does Not Delete Friend Account

Session termination also does not inherently: log the Owner out of the
Friend; delete the Friend Account; terminate the Friend’s entire
service; delete Service Records. M-PIN Session lifecycle and Friend
service lifecycle remain separate.

# 40. Normal Termination

A Session MAY terminate normally because: the Owner ends
synchronization; the Friend ends the M-PIN interaction; the workflow
completes; the Owner switches Friends; the implementation closes the
Session according to policy. Normal termination MUST invalidate
continued M-PIN authority for that Session.

# 41. Revocation

Owner revocation of active M-PIN authority causes the affected Session
authority to become invalid. Conceptually: ACTIVE ↓ Owner revocation ↓
TERMINATING ↓ TERMINATED Revocation MUST NOT be interpreted as automatic
Save.

# 42. Revocation and Friend Runtime

After M-PIN revocation, the Friend MAY continue independent service
execution if its own service permits it. However: continued Friend
Runtime ≠ continued M-PIN authority The Friend MUST NOT continue reading
or writing M-PIN through the revoked Session.

# 43. Abnormal Disconnect

An Abnormal Disconnect occurs when conditions required to maintain the
active Synchronization Session are unexpectedly lost. Examples MAY
include: required Storage becoming unavailable; required removable
storage being disconnected; transport failure; process failure; required
trust/security condition being lost; other implementation-defined loss
of Session continuity. The affected Session MUST terminate.

# 44. Storage Presence Generalization

Historical v1 discussion included physical USB removal as a concrete
termination example. M-PIN v2 generalizes this rule: Loss of a required
Session dependency terminates the Session when that dependency is
necessary to preserve valid M-PIN authority. Thus: USB removed may be
one instance. The Core is not restricted to USB deployments.

# 45. Abnormal Disconnect Is Not Save

The canonical rule is: Abnormal Disconnect ≠ Owner SAVE Therefore:
Current State A ↓ Runtime State B ↓ disconnect ↓ Session terminated ↓
Current State A remains unless State B had already been successfully
committed before the disconnect.

# 46. Disconnect During Commit

If a disconnect occurs while Commit is in progress, Atomic Commit
semantics apply. The resulting authoritative state MUST be either:
previous valid State A or: fully committed valid State B The
implementation MUST NOT accept a partial state as authoritative.

# 47. Reconnection

Network or Device reconnection after Session termination does not revive
the old Session. Conceptually: Session 1 ↓ disconnect ↓ TERMINATED

connectivity restored ↓ new authorization context ↓ Session 2 Session 2
MUST be newly established according to the applicable protocol.

# 48. Reconnection State

A new Session begins from the latest successfully committed Current
State. Example: State A ↓ Runtime B ↓ Save ↓ State B committed ↓ Runtime
C ↓ disconnect On reconnection: LOAD State B not uncommitted Runtime C.

# 49. No Hidden Session

A Friend MUST NOT retain hidden active M-PIN authority after: normal
termination; revocation; Session expiration; abnormal disconnect;
required security failure. A new access attempt requires valid new
Session authority.

# 50. Session Expiration

An implementation MAY define Session expiration. Expiration MUST
terminate or invalidate the relevant Session authority. Expiration MUST
NOT automatically Commit unsaved Runtime State. The exact Session
lifetime is not mandated by v2.0.

# 51. Long-Running Sessions

M-PIN v2.0 does not mandate a universal maximum Session duration.
Long-running Friend operations MAY require Session renewal,
reauthorization, or freshness checks according to the implementation or
applicable Profile. Such renewal MUST preserve Owner Authority and
Session security.

# 52. Session Renewal

A conforming implementation MAY renew a Session without forcing complete
service restart. Renewal MUST NOT: bypass Owner policy; reactivate
revoked authority; change Friend Folder binding; grant additional Friend
scope silently. The exact renewal protocol is deferred.

# 53. Session Freshness

The implementation MUST be able to reject stale Session authority where
reuse could violate security. Possible mechanisms MAY include: nonce
generation counter timestamp token rotation other freshness proof The
mechanism is deferred. The security property is normative.

# 54. Replay Resistance

A terminated, expired, or superseded Session MUST NOT be reusable as
current authority through replay. Conceptually: old Session credential ↓
replay ↓ DENY where the old authority is no longer valid.

# 55. Session Binding

A Session MUST remain bound to the correct: M-PIN Friend Identity Friend
Folder authorization context A Friend MUST NOT use a valid Session for
Folder A to access Folder B.

# 56. Session Transfer

M-PIN v2.0 does not define unrestricted transfer of an active Session
from Friend A to Friend B. Conceptually: Session A → Friend A does not
imply: Session A → Friend B A different Friend requires its own valid
Session.

# 57. Device Transition During Session

If the active execution environment changes Devices, the implementation
MUST preserve or re-establish the required Session security properties.
The Core does not require active Session transfer between Devices. A
deployment MAY instead terminate the old Session and establish a new
Session on the new Device.

# 58. Provider Transition During Session

Provider migration is distinct from active Session transfer. A Provider
migration MAY require Session termination and re-establishment. M-PIN
v2.0 does not require live Session migration between Providers. The
persistent M-PIN continuity may still remain the same.

# 59. Permission Changes During Session

If Owner Permission changes while a Session is active, the Session MUST
NOT continue exercising authority that has been revoked. The
implementation MAY: reduce Session scope; terminate the Session; require
reauthorization. It MUST NOT ignore the revocation.

# 60. Friend Identity Change During Session

If the Friend can no longer be trusted as the same verified Friend
identity required by the Session, M-PIN MUST fail closed. The Session
MUST NOT silently rebind to another Friend identity.

# 61. Friend Folder Binding Change

A Session MUST NOT silently change its bound Friend Folder during active
operation. Conceptually prohibited: Session A ↓ Folder A

then silently

Session A ↓ Folder B A different relationship requires explicit
authorized protocol handling.

# 62. Integrity Failure

If required integrity validation fails during Session operation, the
affected operation MUST fail closed. Depending on severity, the
implementation MAY: reject the object; reject Save; terminate the
Session. It MUST NOT silently accept corrupted or unauthorized state.

# 63. Authentication Failure During Session

Where continued authentication or reauthentication is required and
fails, the implementation MUST deny the affected authority. A failure
MUST NOT broaden the Session’s scope.

# 64. Session and Provider Administration

Provider administrative access does not create a valid Synchronization
Session. A Provider administrator MUST NOT be able to fabricate:
Owner-authorized Session merely through ordinary infrastructure
administration. Any recovery or exceptional role must be separately
defined and bounded.

# 65. Session and Service Records

A Friend may create legitimate Service Records during the same
real-world activity in which an M-PIN Session exists. Those Service
Records remain separate from M-PIN Session persistence. For example:
commerce transaction completes ↓ merchant Service Record may exist

M-PIN Session ↓ Owner has not pressed SAVE ↓ Friend Folder unsaved
Runtime changes are not committed Both statements can be true
simultaneously.

# 66. Session and Physical Action

For Robotics, Session termination controls M-PIN authority. It does not
universally define the robot’s physical safety behavior. Conceptually:
M-PIN Session terminated ≠ universal emergency stop command Physical
safety remains the responsibility of the robot/control system and
applicable Profile.

# 67. Session and Healthcare Action

For Healthcare, an active M-PIN Session permits only the M-PIN access
defined by the Session. It does not itself authorize: treatment;
prescription; clinical decision; institutional record modification.
Those authorities remain independent.

# 68. Session and Commerce Transaction

For Commerce: active M-PIN Session ≠ payment authorization and:
transaction completion ≠ M-PIN Save The Commerce Profile preserves these
boundaries.

# 69. Session and AI Agents

An AI Friend may operate internal agents during its Runtime. Those
agents operate within the M-PIN authority of the Friend unless
separately modeled as Friends. An internal agent MUST NOT use the
Friend’s Session to obtain broader M-PIN authority than the Friend
itself possesses.

# 70. Session Logging

An implementation MAY maintain minimal Session security or audit
metadata. Such logging MAY include information necessary to establish:
Session creation; termination; authorization events; Save/Commit
results; security failures. Logging SHOULD be minimized. Session logging
MUST NOT become a hidden full Friend Folder archive.

# 71. Session Privacy

Session metadata may reveal sensitive relationships. For example: Owner
synchronized with Hospital Friend Owner synchronized with Pharmacy
Friend Owner synchronized with a specific AI Friend may itself be
privacy-sensitive. Implementations SHOULD minimize unnecessary
disclosure of Session metadata.

# 72. Session Recovery

A terminated Session is not recovered as an active Session. Recovery
restores M-PIN continuity or authority as applicable. After recovery, a
Friend establishes a new Session. Conceptually: old Session ↓ terminated

M-PIN recovery ↓ new valid authority ↓ new Session

# 73. Backup and Session State

A Backup MUST NOT be treated as preserving a live active Session merely
because Session metadata was present when the Backup was created. After
restoration, active M-PIN Session authority MUST be re-established
according to current authority and freshness requirements.

# 74. Offline Clone Limitation

If complete M-PIN copies are fully disconnected, universal real-time
enforcement of one active Session across all clones may be impossible
without coordination. Therefore v2.0 requires: one authoritative active
continuity and one active Friend Session within that continuity, while
deferring strong global coordination across disconnected clones. This
limitation MUST NOT be hidden by conformance claims.

# 75. State Machine

The canonical logical state machine is: ┌───────────────┐ │ IDLE │
└───────┬───────┘ │ ▼ ┌───────────────┐ │ AUTHORIZING │
└───────┬───────┘ │ ▼ ┌─────────────────────┐ │ VERIFYING_FRIEND │
└──────────┬──────────┘ │ ▼ ┌─────────────────────┐ │ RESOLVING_FOLDER │
└──────────┬──────────┘ │ ┌──────────────┴──────────────┐ │ │ Folder
exists Folder absent │ │ │ Owner approval │ │ │ │ approve deny │ │ │ │ ▼
└──► IDLE │ Create/Bind │ │ └──────────────┬────────┘ ▼
┌─────────────────────┐ │ ESTABLISHING_SESSION│ └──────────┬──────────┘
▼ ┌──────────┐ │ LOADING │ └────┬─────┘ ▼ ┌──────────┐ ┌───►│ ACTIVE
│◄────────────┐ │ └────┬─────┘ │ │ │ │ │ │ Owner SAVE │ │ ▼ │ │
┌────────────────┐ │ │ │ SAVE_REQUESTED │ │ │ └───────┬────────┘ │ │ ▼ │
│ ┌────────────────┐ │ │ │VALIDATING_SAVE │ │ │ └───────┬────────┘ │ │ ▼
│ │ ┌────────────┐ │ │ │ COMMITTING │───────────┘ │ └──────┬─────┘ │ │
failure requiring │ │ termination │ ▼ │ ┌─────────────┐ └────│ save
failure│ └─────────────┘

ACTIVE / any security-sensitive state │ │ termination / revoke / │
disconnect / fatal failure ▼ ┌─────────────┐ │ TERMINATING │
└──────┬──────┘ ▼ ┌─────────────┐ │ TERMINATED │ └─────────────┘ A
future implementation MAY represent these states differently internally.
The observable transition semantics MUST remain equivalent.

# 76. Session Transition Rules

The following transitions are normative at the architectural level. \##
SP-STATE-001 IDLE → AUTHORIZING requires initiation of a synchronization
attempt. \## SP-STATE-002 AUTHORIZING → VERIFYING_FRIEND requires
sufficient Owner authority for the next step. \## SP-STATE-003
VERIFYING_FRIEND → RESOLVING_FOLDER requires successful Friend Identity
verification. \## SP-STATE-004 RESOLVING_FOLDER → ESTABLISHING_SESSION
requires either: valid existing Folder binding; or Owner-approved
creation and binding. \## SP-STATE-005 ESTABLISHING_SESSION → LOADING
requires valid new Session authority. \## SP-STATE-006 LOADING → ACTIVE
requires successful authorized Load sufficient for the Session. \##
SP-STATE-007 ACTIVE → SAVE_REQUESTED requires Owner Save intent. \##
SP-STATE-008 SAVE_REQUESTED → VALIDATING_SAVE requires a proposed
persistence transition for the active Friend Folder. \## SP-STATE-009
VALIDATING_SAVE → COMMITTING requires successful required validation.
\## SP-STATE-010 COMMITTING → ACTIVE requires successful Commit and
continuing Session validity. \## SP-STATE-011 ACTIVE → TERMINATING may
occur through normal termination, revocation, disconnect, expiration, or
required security failure. \## SP-STATE-012 TERMINATING → TERMINATED
requires invalidation of the terminated Session’s continued M-PIN
authority.

# 77. Protocol Requirements

A conforming M-PIN v2 implementation MUST satisfy: \### SP-001 — Bounded
Session Friend M-PIN access MUST occur through a bounded Synchronization
Session. \### SP-002 — Owner Authority Required Owner Authority MUST be
established before Friend M-PIN access is granted. \### SP-003 — Friend
Verification The Friend MUST be verified before its Friend Folder is
resolved for access. \### SP-004 — Correct Folder Binding The Session
MUST bind the Friend to its correct Friend Folder. \### SP-005 —
Owner-Approved First Creation A missing Friend Folder MUST NOT be
created without required Owner approval. \### SP-006 — Existing Folder
Reuse A continuing Friend relationship MUST reuse its existing valid
Friend Folder. \### SP-007 — Authorized Load Only the authorized Friend
Folder state may be loaded into the active Friend Runtime through the
Session. \### SP-008 — One Active Friend Only one Friend may hold active
M-PIN synchronization authority at a time within one authoritative
active continuity. \### SP-009 — Runtime/Persistence Separation Runtime
changes MUST NOT automatically become M-PIN Persistent State. \###
SP-010 — Owner Save Persistence MUST require applicable Owner Save
authority. \### SP-011 — Save Validation A proposed Commit MUST satisfy
required Session, authority, binding, structure, and integrity checks.
\### SP-012 — Atomic Commit Commit MUST result in a valid new Current
State or preserve the previous valid Current State. \### SP-013 — No
Implicit Save Termination, disconnect, expiration, or Friend switching
MUST NOT implicitly Save unsaved Runtime State. \### SP-014 —
Termination A terminated Session MUST NOT retain valid M-PIN access
authority. \### SP-015 — Reconnection Reconnection after termination
MUST establish a new valid Session. \### SP-016 — Replay Resistance
Expired, terminated, revoked, or superseded Session authority MUST NOT
be accepted as current authority. \### SP-017 — No Silent Rebinding An
active Session MUST NOT silently change its Friend Identity or Friend
Folder binding. \### SP-018 — Fail Closed Failure to establish a
required Session security property MUST deny or terminate the affected
authority.

# 78. Recommended Session Properties

A conforming implementation SHOULD additionally preserve: \### SP-019 —
Discovery Privacy Session establishment SHOULD avoid exposing unrelated
Friend relationships. \### SP-020 — Metadata Minimization Session
metadata SHOULD be minimized to what is necessary. \### SP-021 — Renewal
Safety Session renewal SHOULD preserve existing scope and MUST NOT
revive revoked authority. \### SP-022 — Cleanup Termination SHOULD clear
temporary M-PIN access material no longer required. \### SP-023 —
Dependency Detection Implementations SHOULD detect loss of dependencies
required to preserve Session authority.

# 79. Canonical First Session

Owner ↓ Initiate Sync ↓ Establish Owner Authority ↓ Verify Friend
Identity ↓ Resolve Folder ↓ Folder absent ↓ Owner approves creation ↓
Create + Bind Folder ↓ Create new Session ↓ Load initial/current state ↓
ACTIVE

# 80. Canonical Returning Session

Owner ↓ Initiate Sync ↓ Establish Owner Authority ↓ Verify Friend
Identity ↓ Resolve existing Folder ↓ Validate binding ↓ Create new
Session ↓ Load Current State ↓ ACTIVE

# 81. Canonical Save Cycle

ACTIVE ↓ Runtime changes ↓ Owner SAVE ↓ Validate authority ↓ Validate
Session ↓ Validate Friend/Folder binding ↓ Validate required
structure/integrity ↓ Atomic Commit ↓ New Current State ↓ ACTIVE

# 82. Canonical No-Save Termination

Current State A ↓ ACTIVE ↓ Runtime State B ↓ Owner does not Save ↓
TERMINATING ↓ TERMINATED ↓ Current State A remains

# 83. Canonical Abnormal Disconnect

ACTIVE ↓ required dependency lost ↓ Abnormal Disconnect ↓ TERMINATING ↓
TERMINATED ↓ unsaved Runtime discarded relative to M-PIN persistence If
a Commit had already completed successfully, that committed Current
State remains authoritative.

# 84. Canonical Reconnection

TERMINATED Session 1 ↓ connect again ↓ new authority establishment ↓ new
Friend verification ↓ existing Folder resolution ↓ new Session 2 ↓ Load
latest committed Current State Session 1 is not revived.

# 85. Protocol Non-Goals

M-PIN v2.0 Session Protocol does not define: one network transport; one
REST API; one RPC protocol; one WebSocket requirement; one USB protocol;
one Session-token format; one heartbeat interval; one Session timeout;
one Provider discovery mechanism; one live migration mechanism. Those
are implementation or future protocol decisions.

# 86. Deferred Session Mechanisms

The following remain deferred: Session identifier format Session token
format authentication exchange heartbeat keepalive renewal protocol
transport freshness representation replay-protection encoding Provider
routing dependency-presence mechanism live Session migration Their
deferral does not change the frozen Session semantics.

# 87. Session Invariants

The Session Protocol is governed by these invariants: \## No valid
Session means no active Friend M-PIN synchronization authority. \## A
Friend is verified before receiving Friend Folder access. \## A Friend
accesses only its bound Friend Folder. \## One M-PIN has one active
Friend synchronization relationship at a time. \## Runtime State does
not automatically become Persistent State. \## Owner Save is required
for M-PIN persistence. \## Disconnect is not Save. \## Friend switching
is not Save. \## Termination invalidates the Session. \## Reconnection
creates a new Session. \## A terminated Session cannot silently return
to life. \## Failure of required security conditions fails closed.

# 88. Session Thesis

The M-PIN Session model can be reduced to: Owner Authority ↓ Verified
Friend ↓ Bound Friend Folder ↓ Bounded Session ↓ Load ↓ Friend Runtime ↓
Owner Save? ┌───────┴────────┐ YES NO │ │ ▼ ▼ Commit Terminate │ │ ▼ ▼
New Current Previous Current State State remains The Session exists to
give a Friend enough temporary authority to provide its service without
turning temporary access into permanent ownership.

## M-PIN v2.0 — Core 08 / Session Protocol

## Status: FROZEN
