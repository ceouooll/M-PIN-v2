# M-PIN v2.0

## Core 04 — Core Architecture

**Status:** FROZEN **Version:** 2.0 **Document Type:** Normative Core
Specification

------------------------------------------------------------------------

# 1. Purpose

This document defines the canonical architecture of M-PIN v2.0.

It specifies the relationships among:

- Owner;
- M-PIN;
- Friend;
- Friend Folder;
- Synchronization Session;
- Runtime;
- Persistent State;
- Storage;
- optional M-PIN Service Provider.

This document defines architectural relationships and required behavior.

It does not mandate one physical topology, protocol, SDK, API, storage
technology, or cloud architecture.

------------------------------------------------------------------------

# 2. Architectural Thesis

M-PIN separates:

``` text
persistent ownership
        from
service execution
The canonical responsibility model is:
Owner
  │
  │ authority
  ▼
M-PIN
  │
  │ bounded access
  ▼
Friend Folder
  │
  │ authorized synchronization
  ▼
Friend
  │
  ▼
Runtime
  │
  ▼
Native UX
The Friend provides the service.
The Owner retains authority over Owner-controlled M-PIN persistence.
M-PIN preserves the boundary between them.
```

# 3. Core Actors and Components

The canonical architecture contains the following roles and components:
Owner M-PIN Friend Friend Folder Synchronization Session Friend Runtime
Persistent State Storage An implementation MAY additionally include:
M-PIN Service Provider The Provider is optional. It is not a mandatory
architectural center.

# 4. Owner

The Owner is the central authority of an M-PIN. The Owner is responsible
for authority over operations that require Owner authorization,
including as applicable: establishing synchronization; approving first
Friend Folder creation; persistence; revocation; migration; recovery.
The Owner MUST remain distinguishable from: Friend Friend Account Device
Storage Provider Detailed Owner and Identity requirements are defined in
Core 05.

# 5. M-PIN

M-PIN is the Owner-centered persistence and access boundary. Its
architectural responsibilities include: maintaining the M-PIN identity
boundary; associating Friends with Friend Folders; preserving Friend
Folder isolation; enforcing applicable authorization; bounding
Synchronization Sessions; preserving persistence rules; supporting
applicable security properties; preserving portability and recovery
boundaries. M-PIN does not need to provide the Friend’s service.

# 6. Friend

A Friend is the service principal that interacts with M-PIN. The Friend
remains responsible for: service execution Runtime native UX service
semantics payload semantics internal architecture business logic M-PIN
MUST NOT require the Friend to surrender those responsibilities merely
to participate in M-PIN.

# 7. Friend Folder

A Friend Folder is the Owner-owned persistent M-PIN data area associated
with one Friend. The canonical invariant is: \## One Friend, One Friend
Folder. Conceptually: M-PIN

├── Friend Folder A ↔ Friend A ├── Friend Folder B ↔ Friend B └── Friend
Folder C ↔ Friend C Friend Folder is both a persistence association and
an access boundary.

# 8. No Separate Domain Layer

M-PIN v2.0 does not require: M-PIN ↓ Domain ↓ Friend Folder The
canonical structure is: M-PIN ↓ Friend Folder ↓ Friend Historical v1
Domain terminology remains historical terminology and does not create an
additional v2 architectural layer.

# 9. Friend Folder Isolation

Friend Folder relationships MUST remain isolated by default.
Conceptually: Friend A ─────► Friend Folder A

Friend A ──X──► Friend Folder B Friend A ──X──► Friend Folder C The fact
that multiple Friend Folders share: an M-PIN; Storage; a Device; a
Provider MUST NOT grant cross-Friend access.

# 10. Friend Folder Binding

M-PIN MUST maintain a trustworthy association between: verified Friend
Identity ↕ Friend Folder A Friend MUST NOT be permitted to select
another Friend’s Folder merely by supplying its name or location. The
binding mechanism is implementation-defined. The binding property is
normative.

# 11. Storage

Storage contains the persistent representation of M-PIN state. Storage
MAY be implemented through: local storage Owner-controlled cloud storage
removable storage Provider-hosted storage other conforming storage
Storage is infrastructure. Storage MUST NOT become the Owner merely
because it contains M-PIN data.

# 12. Optional Provider

A deployment MAY use an M-PIN Service Provider. Conceptually: Owner │ ▼
M-PIN │ ┌─────────┴─────────┐ │ │ M-PIN functions Storage ▲ ▲ │ │
optional Provider may implement some or both responsibilities The
Provider may supply infrastructure. The architecture MUST remain defined
independently of one mandatory Provider.

# 13. Provider Is Not a Required Hop

The logical architecture MUST NOT be interpreted as: Owner ↓ Mandatory
Provider ↓ M-PIN ↓ Friend for every deployment. A valid implementation
may instead be local or Owner-managed. Provider Independence is defined
in Core 11.

# 14. Friend Runtime

Friend Runtime is the Friend-controlled execution environment. During a
valid Synchronization Session, authorized Friend Folder state may be
loaded into the Friend Runtime. Conceptually: Friend Folder │ │ LOAD ▼
Friend Runtime │ ▼ Native Friend UX M-PIN does not become the Friend
Runtime.

# 15. Runtime State

After loading, the Friend may create or modify Runtime State. Persistent
State A │ │ LOAD ▼ Runtime State A │ │ Friend processing ▼ Runtime State
B At this point: Runtime State B ≠ Persistent State B unless a valid
M-PIN persistence operation occurs.

# 16. Persistent State

Persistent State is the authoritative state surviving according to M-PIN
persistence rules. For a Friend relationship, the Friend-specific
persistent payload resides within that Friend’s Friend Folder. A
Friend’s Runtime does not automatically become authoritative
persistence.

# 17. Canonical Full Architecture

The logical v2 architecture is: OWNER │ Owner Authority │ ▼ M-PIN │
┌──────────────────────┼──────────────────────┐ │ │ │ ▼ ▼ ▼ Friend
Folder A Friend Folder B Friend Folder C │ │ │ │ │ │ authorized isolated
isolated binding binding binding │ │ │ ▼ ▼ ▼ Friend A Friend B Friend C
│ │ │ ▼ ▼ ▼ Runtime A Runtime B Runtime C │ │ │ ▼ ▼ ▼ Native UX A Native
UX B Native UX C Only the Friend participating in the active authorized
Synchronization Session receives active M-PIN synchronization authority.

# 18. Synchronization Session

A Synchronization Session is the bounded M-PIN authorization context
between the M-PIN and one active Friend. The canonical invariant is: \##
One M-PIN, One Active Friend, One Synchronization Session. This means
M-PIN MUST NOT simultaneously grant active synchronization authority to
multiple Friends under the same active M-PIN continuity. The detailed
protocol is defined in Core 08.

# 19. Synchronization Does Not Mean Universal Visibility

Synchronization is Friend-specific. When Friend A synchronizes: M-PIN │
└── Friend Folder A │ ▼ Friend A it MUST NOT imply: Friend A ├── Friend
Folder A ├── Friend Folder B └── Friend Folder C The active Friend
receives only the M-PIN authority applicable to its own relationship.

# 20. First Synchronization

The canonical first synchronization flow is: Friend access initiated ↓
Owner initiates M-PIN synchronization ↓ M-PIN authentication / authority
establishment ↓ Friend Identity verification ↓ Friend Folder lookup ↓
Friend Folder absent ↓ Owner approval for creation ↓ Friend Folder
created and bound ↓ Synchronization Session established ↓
initial/current Friend state synchronized as applicable ↓ Friend Runtime
Friend Folder creation MUST require the applicable Owner authorization.

# 21. Empty First State

A newly created Friend Folder MAY initially contain no prior Friend
state. Conceptually: new Friend Folder ↓ empty / initial valid state ↓
Friend Runtime The absence of previous state is not an error. The Friend
may begin service operation through its normal Runtime and UX.

# 22. Returning Synchronization

For an existing Friend relationship: Owner initiates synchronization ↓
M-PIN authority established ↓ Friend Identity verified ↓ existing Friend
Folder resolved ↓ binding validated ↓ Synchronization Session
established ↓ current committed Friend Folder state loaded ↓ Friend
Runtime The existing Friend Folder MUST be reused rather than silently
creating a new independent Folder for the same binding.

# 23. Initial Read

Once a Session is valid, the corresponding current saved state may be
loaded into the Friend Runtime. Conceptually: Friend Folder ↓ Current
State ↓ LOAD ↓ Friend Runtime This is the v2 expression of the v1 Read
Once principle. The Friend may use the loaded state throughout the
authorized Runtime. Initial Read does not create unrestricted permanent
background access to M-PIN.

# 24. Native UX Restoration

After synchronization, the Friend uses the synchronized state through
its own service. For example: M-PIN Friend Folder ↓ Friend Runtime ↓
Friend interprets its own payload ↓ Friend native interface M-PIN does
not need to render: conversation lists; medical screens; commerce
screens; robot control interfaces merely because their persistent state
is associated with M-PIN.

# 25. Friend Payload Responsibility

The Friend defines the semantic meaning and service-specific structure
of its payload. M-PIN defines only the minimum structural boundary
necessary for M-PIN-level responsibilities. Conceptually: Friend Folder
│ ├── M-PIN-required envelope/binding metadata │ └── Friend-defined
payload M-PIN does not need to semantically interpret the Friend
payload.

# 26. Envelope Boundary

The M-PIN-level Envelope may contain the minimum information necessary
to preserve such properties as: M-PIN identity association Friend
identity association Friend Folder binding format/version identification
integrity information state/freshness information where required The
exact Envelope schema is not frozen in v2.0. The architecture fixes
responsibility, not binary encoding.

# 27. Owner Save

M-PIN persistence requires Owner persistence intent. Canonical flow:
Persistent State A ↓ LOAD ↓ Runtime State A ↓ WORK ↓ Runtime State B ↓
OWNER SAVE Owner Save authorizes the M-PIN persistence process.

# 28. Save Is Not Commit

M-PIN distinguishes: SAVE = Owner persistence intent from: COMMIT =
technical establishment of the new valid Persistent State Therefore:
Owner SAVE ↓ required validation ↓ Commit ↓ new Current State The two
terms MUST NOT be treated as identical architectural events.

# 29. Persistence Validation

Before accepting a new Current State, M-PIN MUST validate the
M-PIN-level conditions required by the architecture. These may include:
valid Owner persistence authority valid Synchronization Session correct
Friend Identity correct Friend Folder binding required structural
validity required integrity validity M-PIN does not thereby become
responsible for all semantic correctness inside the Friend payload.

# 30. Semantic Save Result

The architectural result of a successful Save is one new valid current
Friend Folder Persistent State. Conceptually: Current State A ↓ Owner
Save ↓ Commit ↓ Current State B This rule defines the semantic result.
It does not require every implementation to transmit or rewrite the
entire payload as a full snapshot. A conforming implementation MAY use:
full-state transfer; delta transfer; chunked transfer; transactional
update; another conforming mechanism provided that the authoritative
result is one valid Current State and the mechanism does not introduce
M-PIN version-history semantics contrary to Core 09.

# 31. Atomic Commit

Commit MUST preserve atomic persistence semantics. The valid observable
outcomes are: State A → State B or, if Commit fails: State A → State A
The architecture MUST NOT accept: State A → corrupted partial State B as
the valid Current State.

# 32. Multiple Saves

A valid Synchronization Session MAY contain more than one Owner Save.
Example: State A ↓ Load Runtime ↓ Save State B ↓ continued Runtime ↓
Save State C After the second successful Commit: State C is the
authoritative Current State. M-PIN Core does not require State A and
State B to remain available as version history.

# 33. No-Save Path

If Runtime changes occur without Owner Save: Persistent State A ↓ LOAD ↓
Runtime State B ↓ NO SAVE ↓ Session termination ↓ Persistent State A
remains M-PIN MUST NOT silently commit Runtime State B because the
Session ended.

# 34. Friend Internal Autosave

A Friend MAY have internal autosave or operational persistence unrelated
to M-PIN. For example: Friend Runtime ↓ Friend internal autosave does
not automatically mean: M-PIN Owner Save ↓ M-PIN Commit The Friend’s own
internal persistence model does not redefine the M-PIN persistence
boundary.

# 35. Service Records

A Friend MAY independently maintain legitimate Service Records.
Conceptually: Friend /  
/  
▼ ▼ Friend Runtime Service Record │ │ M-PIN Save path ▼ Friend Folder
Service Records and Friend Folder state are separate architectural
categories. The existence of a Service Record MUST NOT create a bypass
around Friend Folder isolation or Owner-controlled M-PIN persistence.

# 36. Normal Session Termination

A normal Session may end after: Runtime completion; one or more
successful Saves; no Save; explicit Owner termination; other valid
Session completion. At termination: Session authority ↓ terminated The
Friend MUST NOT retain hidden M-PIN Session authority after termination.

# 37. Abnormal Disconnect

An abnormal loss of the conditions required to maintain the Session
terminates the affected M-PIN synchronization authority. Conceptually:
Active Session ↓ disconnect / required condition lost ↓ Session
termination Unsaved Runtime State MUST NOT automatically become M-PIN
Persistent State because of the disconnect.

# 38. Reconnection

After Session termination, reconnection requires a new valid
Synchronization Session. Conceptually: Session 1 ↓ terminated

new connection ↓ new authorization context ↓ Session 2 Session 2 MUST
begin from the current committed Persistent State. Unsaved state from
the terminated Session MUST NOT be treated as committed M-PIN state.

# 39. Session Identity

A terminated Session MUST NOT simply become active again as though its
previous authority never ended. A new Session SHOULD have a
distinguishable Session identity or equivalent freshness context
sufficient to prevent stale Session authority from being replayed. The
exact Session identifier or token format is deferred.

# 40. Revocation

Owner authority MAY revoke M-PIN access according to the applicable
Permission and Session rules. Revocation MUST terminate or invalidate
the relevant M-PIN authority. Revocation of M-PIN access does not
necessarily terminate every independent Friend service process. This
distinction preserves Friend Sovereignty.

# 41. One Active Friend

The one-active-Friend rule applies to M-PIN synchronization authority.
It does not mean: only one Friend application may exist or: all other
services must stop running It means: one M-PIN ↓ one active Friend
synchronization authority ↓ one active Synchronization Session at a
time.

# 42. Backup Copies

M-PIN state MAY have protected backup copies. Conceptually:
Authoritative Current State │ ├── Backup Copy 1 └── Backup Copy 2 Backup
copies do not automatically become active M-PIN continuities.

# 43. Offline Clone Limitation

If two complete copies become fully disconnected and no coordination
mechanism exists, the architecture cannot universally prove to both
sides that only one remains globally active. Therefore v2.0
distinguishes: normative requirement: one authoritative active
continuity

from

implementation problem: global enforcement across fully disconnected
clones M-PIN v2.0 does not make an impossible universal enforcement
claim.

# 44. Device Change

Device replacement does not inherently replace M-PIN. Conceptually:
Device A │ ▼ M-PIN Identity X ▲ │ Device B A new Device must satisfy the
applicable authentication, authorization, and recovery or migration
requirements. The same M-PIN continuity may remain.

# 45. Storage Change

Storage migration does not inherently create a new M-PIN. Conceptually:
Storage A │ │ migrate ▼ Storage B

M-PIN Identity remains X The migration MUST preserve required identity,
integrity, and authoritative-state properties.

# 46. Provider Change

Where Providers are used: Provider A │ │ migrate ▼ Provider B MUST NOT
inherently mean: M-PIN X ↓ new M-PIN Y Provider migration should
preserve the same M-PIN continuity where the participating
implementations support conforming migration.

# 47. Friend Change Is Different

Provider migration MUST NOT be confused with changing Friends. Provider
A → Provider B is infrastructure migration. Friend A → Friend B is a
different service relationship. M-PIN v2.0 does not automatically
semantically translate Friend A payload into Friend B payload.

# 48. Recovery Architecture

Recovery may require restoration of: Owner Authority M-PIN Identity
continuity valid Persistent State Friend Folder bindings where
recoverable material remains. The architecture distinguishes: Authority
Recovery ≠ Data Recovery A successful authority recovery cannot recreate
data that no valid copy retains.

# 49. No Universal Recovery Backdoor

M-PIN architecture MUST NOT require one universal secret bypass capable
of defeating all Owner security merely for recovery convenience.
Recovery mechanisms MAY differ. They MUST preserve the relevant Owner
authority and security boundaries. Exact recovery-factor design is
deferred.

# 50. Provider Administrative Authority

Provider administrative capability MUST NOT automatically equal Owner
Authority. For example: Provider administrator ≠ Owner unless a specific
authorized recovery or operational mechanism explicitly establishes a
bounded role. The architecture does not assume provider administration
is the root ownership credential.

# 51. Cross-Friend Access

The Core does not permit direct cross-Friend Folder access by default.
Conceptually: Friend A X Friend Folder B This remains true even if
Friend A and Friend B: belong to the same company; run on the same
Device; use the same Provider; participate in the same physical
workflow.

# 52. Owner-Mediated Disclosure

Profile validation identified a potential need for selected data to move
between otherwise isolated Friend relationships. The candidate concept
is: Friend A │ selected information ▼ Owner authorization │ ▼ Disclosure
│ ▼ Friend B For v2.0: Owner-Mediated Disclosure = CANDIDATE DEFERRED
FROM CORE It is not part of the required Core architecture.

# 53. Disclosure Is Not Folder Sharing

Any future Disclosure mechanism MUST preserve the distinction: selected
Owner-authorized disclosure ≠ direct access to another Friend Folder The
candidate mechanism does not change the v2.0 Friend Folder isolation
invariant.

# 54. AI Architecture Example

A conforming AI relationship may conceptually appear as: Owner ↓ M-PIN ↓
AI Friend Folder ↓ AI Friend ↓ AI Runtime ↓ AI Native UX The M-PIN Core
does not become the AI model.

# 55. Robotics Architecture Example

A robot environment may contain multiple architectural roles: Physical
Robot Device │ ├── Robot Friend ├── AI Friend └── other Friend Each
Friend relationship remains separately governed by the Core. The
physical Robot Device itself does not automatically receive access to
every Friend Folder.

# 56. Healthcare Architecture Example

A healthcare environment may contain: M-PIN

├── Hospital Friend Folder ├── Pharmacy Friend Folder └── Healthcare AI
Friend Folder The existence of one healthcare workflow does not merge
these Folders. Institutional medical records remain distinct from
Owner-controlled M-PIN state.

# 57. Commerce Architecture Example

A commerce environment may contain: M-PIN

├── Retailer Friend Folder ├── Payment Friend Folder └── Delivery Friend
Folder A Retailer Friend does not automatically gain access to Payment
or Delivery Friend Folders. Transaction authorization is not
automatically M-PIN Save authorization.

# 58. Profile Composition

A real-world system MAY combine Profiles. For example: Physical Robot │
├── Robotics Friend ├── Healthcare Friend └── AI Friend The Profiles may
coexist. Their coexistence MUST NOT weaken: Friend Folder Isolation;
Owner Authority; Session boundaries; persistence boundaries.

# 59. Deployment Topology Independence

The logical architecture does not require one physical deployment
topology. For example, these may all be conceptually possible: Local:
Owner Device └── M-PIN + Storage

Provider-hosted: Owner └── Provider └── M-PIN infrastructure + Storage

Hybrid: Owner Device ├── local M-PIN functions └── remote
Owner-controlled Storage Conformance depends on behavior and boundaries,
not topology alone.

# 60. Architecture Does Not Require Semantic Centralization

M-PIN MUST NOT require all Friend payloads to use one universal business
schema. Conceptually: AI payload → AI-defined semantics Hospital payload
→ Hospital-defined semantics Retail payload → Retail-defined semantics
Robot payload → Robot-defined semantics M-PIN standardizes the boundary
around those payloads rather than their complete internal meaning.

# 61. Architecture Does Not Require Shared Memory

M-PIN may contain persistent state for many Friends. This MUST NOT be
interpreted as: one universal memory visible to all Friends The correct
model is: one Owner continuity

containing

multiple isolated Friend-specific persistent relationships

# 62. Architecture Does Not Require Friend Replacement

A Friend may upgrade: model; application; internal database; algorithm;
infrastructure; product implementation without requiring a new M-PIN
architecture, provided its M-PIN-facing behavior remains conformant and
continuity requirements are preserved.

# 63. Architecture Does Not Require Provider Trust Expansion

Using a Provider does not automatically grant that Provider: Friend
authority; Owner authority; cross-Friend data authority; semantic
control over Friend payloads. Provider capabilities depend on the
implementation and its explicit security model. M-PIN v2.0 does not
claim that every Provider deployment is necessarily zero-knowledge.

# 64. Failure Boundary

When a required security or authority condition cannot be established,
the affected M-PIN operation MUST fail closed. Examples include
inability to validate: Owner authority Friend Identity Friend Folder
binding Session validity required integrity Failure MUST NOT result in
broader access.

# 65. Architectural Validation Boundary

M-PIN validates the conditions necessary for its own boundary.
Conceptually: M-PIN responsibility ├── identity/binding ├──
authorization ├── Session validity ├── structural validity └── integrity

Friend responsibility ├── service semantics ├── payload meaning ├──
business correctness └── native service behavior This separation
preserves Friend Sovereignty.

# 66. Architecture Invariants

A conforming M-PIN v2 architecture MUST preserve the following
invariants. \### A-01 — Owner Centrality The Owner remains the central
authority. \### A-02 — Friend Sovereignty The Friend remains responsible
for its own service and Runtime. \### A-03 — One Friend, One Friend
Folder Each Friend relationship maps to its associated Friend Folder.
\### A-04 — Friend Folder Isolation No default cross-Friend Folder
access. \### A-05 — Verified Binding Friend Folder access depends on
correct Friend identity/binding. \### A-06 — Bounded Session M-PIN
access occurs through bounded Synchronization Session authority. \###
A-07 — One Active Friend Only one Friend holds active M-PIN
synchronization authority at a time. \### A-08 — Runtime/Persistence
Separation Runtime change does not automatically modify Persistent
State. \### A-09 — Owner-Controlled Save M-PIN persistence requires the
applicable Owner Save authority. \### A-10 — Atomic Commit A Commit
establishes a valid new Current State or leaves the previous Current
State authoritative. \### A-11 — Current-State-Only M-PIN Core does not
require version-history semantics. \### A-12 — Native Friend Experience
M-PIN does not replace the Friend’s service Runtime or UX. \### A-13 —
Device Independence M-PIN continuity is not inherently tied to one
Device. \### A-14 — Provider Independence M-PIN Standard is not
inherently tied to one Provider. \### A-15 — Core Neutrality The
architecture remains industry-neutral.

# 67. Canonical First-Use Sequence

OWNER │ │ initiates synchronization ▼ M-PIN │ │ establish Owner
authority ▼ VERIFY FRIEND │ ▼ RESOLVE FRIEND FOLDER │ ├── exists
───────────────┐ │ │ └── absent │ │ │ ▼ │ Owner approval │ │ │ ▼ │
Create + bind Folder │ │ │ └────────────────────┘ │ ▼ OPEN
SYNCHRONIZATION SESSION │ ▼ LOAD CURRENT STATE │ ▼ FRIEND RUNTIME │ ▼
FRIEND NATIVE UX

# 68. Canonical Save Sequence

FRIEND RUNTIME │ │ working state changes ▼ RUNTIME STATE’ │ │ Owner SAVE
▼ VALIDATE │ ├── Owner authority ├── Session ├── Friend binding ├──
structure └── integrity │ ▼ ATOMIC COMMIT │ ▼ NEW CURRENT STATE │ ▼
FRIEND FOLDER The exact data-transfer strategy is
implementation-defined.

# 69. Canonical No-Save Sequence

CURRENT STATE A │ ▼ FRIEND RUNTIME │ ▼ RUNTIME STATE B │ │ no Owner SAVE
▼ SESSION TERMINATION │ ▼ RUNTIME CHANGES NOT COMMITTED │ ▼ CURRENT
STATE A REMAINS

# 70. Canonical Reconnection Sequence

SESSION 1 │ X terminated │ ▼ Current committed state remains │ ▼ new
authentication / authorization │ ▼ SESSION 2 │ ▼ load current committed
state A terminated Session does not regain authority merely because
network connectivity returns.

# 71. Canonical Migration Sequence

Existing M-PIN │ │ authorize migration ▼ validate source state │ ▼
transfer protected state │ ▼ validate destination │ ▼ establish
destination continuity │ ▼ preserve M-PIN identity and Friend Folder
bindings The exact migration protocol is defined by later implementation
work subject to Core 11.

# 72. Architecture Freeze Boundary

The following are architectural decisions in v2.0: Owner-centered
authority Friend Sovereignty Friend Folder as canonical data area One
Friend, One Friend Folder Friend Folder Isolation bounded
Synchronization Session One Active Friend Runtime/Persistence separation
Owner Save Save/Commit distinction Atomic Commit Current-State-Only
Device Independence Provider Independence Service Record distinction
behavioral conformance The following remain implementation-level
deferred matters: exact .MPIN container serialization crypto algorithms
key hierarchy credential format Session token format heartbeat transport
Provider discovery Provider trust mechanism integrity-proof
representation freshness mechanism Disclosure schema strong
offline-clone coordination

# 73. Core Architecture Thesis

The complete M-PIN v2 architecture can be summarized as: \## The Owner
carries persistent continuity through M-PIN. \## Each Friend receives
bounded access only to its own Friend Folder. \## The Friend performs
the service in its own Runtime and native UX. \## Runtime changes remain
temporary relative to M-PIN until the Owner authorizes persistence. \##
A successful Commit establishes one valid current persistent state. \##
Device, Storage, and Provider may change without inherently changing the
Owner’s M-PIN continuity.

## M-PIN v2.0 — Core 04 / Core Architecture

## Status: FROZEN
