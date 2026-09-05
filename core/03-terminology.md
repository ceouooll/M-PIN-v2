# M-PIN v2.0

## Core 03 — Terminology

**Status:** FROZEN **Version:** 2.0 **Document Type:** Normative Core
Specification

------------------------------------------------------------------------

# 1. Purpose

This document defines the canonical terminology of M-PIN v2.0.

All M-PIN v2 Core documents and Profiles MUST use these terms
consistently.

Where historical v1 terminology differs from the v2 vocabulary, the
historical wording remains part of v1 provenance, while this document
defines the normative v2 meaning.

This document defines architectural terms.

It does not mandate a particular programming language, class hierarchy,
file format, protocol encoding, database schema, or user-interface
vocabulary.

------------------------------------------------------------------------

# 2. Normative Language

The key words:

- MUST
- MUST NOT
- SHOULD
- SHOULD NOT
- MAY

are used normatively throughout M-PIN v2.

Informative examples do not override normative definitions.

------------------------------------------------------------------------

# 3. Owner

## Definition

**Owner** is the principal authority over an M-PIN and its
Owner-controlled Persistent State.

The Owner determines whether M-PIN authority is granted for operations
that require Owner authorization.

The Owner is the architectural center of M-PIN.

## Distinction

Owner MUST NOT be treated as synonymous with:

``` text
Friend
Friend Account
Device
Storage
M-PIN Service Provider
A person may use accounts, devices, storage systems, and Providers, but those relationships do not by themselves redefine the architectural Owner.
```

# 4. Owner Authority

## Definition

Owner Authority is the legitimate authority by which an Owner authorizes
M-PIN operations. Examples include authority over: Synchronization
Session establishment; Friend Folder creation; persistence; migration;
recovery; revocation. Owner Authority is an architectural concept. The
exact authentication or credential mechanism used to establish that
authority is implementation-defined unless constrained elsewhere by the
Core. \## Distinction Authentication ≠ Authorization ≠ Ownership
Successful authentication may be necessary to exercise Owner Authority.
It is not itself the definition of ownership.

# 5. M-PIN

## Definition

M-PIN is the Owner-centered architecture and corresponding persistent
continuity boundary through which an Owner-controlled persistent state
may be associated with Friends. Conceptually: Owner │ ▼ M-PIN │ ├──
Friend Folder A ├── Friend Folder B └── Friend Folder C M-PIN separates
persistent data ownership from Friend service execution. \## M-PIN Is
Not M-PIN is not inherently: one AI service; one cloud provider; one
Device; one storage product; one universal Friend UI; one Friend
Runtime.

# 6. M-PIN Identity

## Definition

M-PIN Identity is the stable identity by which one M-PIN continuity is
distinguished from another. M-PIN Identity MUST remain conceptually
distinct from: Device Identity; Friend Identity; Friend Account
Identity; Provider Identity. Changing a Device or compatible Provider
MUST NOT inherently require creation of a new M-PIN Identity. The exact
identifier representation is deferred.

# 7. Friend

## Definition

Friend is an external service principal that interacts with M-PIN under
the applicable Owner authorization and M-PIN protocol boundaries. A
Friend provides a service. Examples may include: AI service; robot
service; hospital service; pharmacy service; commerce service;
transportation service. The Core does not assume one industry. \##
Responsibility A Friend remains responsible for its own: Runtime native
UX internal implementation service semantics business logic product
evolution M-PIN does not become the general operating authority of the
Friend.

# 8. Friend Identity

## Definition

Friend Identity is the identity used by M-PIN to distinguish one Friend
from another for authorization, Friend Folder association, and Session
purposes. Friend Identity MUST be sufficiently stable to prevent one
Friend from being mistaken for another Friend. The exact credential,
registry, certificate, identifier, or trust mechanism is not fixed by
v2.0 Core. \## Security Requirement A claimed Friend Identity MUST NOT
be accepted merely because an untrusted service supplies a familiar
display name. Friend Identity verification is part of the security
boundary.

# 9. Friend Account

## Definition

Friend Account is an account maintained by a Friend for its own service.
Examples include: AI service account hospital portal account retailer
account robot service account \## Distinction Friend Account ≠ Owner
Identity

Friend Account ≠ M-PIN Identity A Friend MAY require its own account
independently of M-PIN. M-PIN does not replace Friend account
management.

# 10. Friend Folder

## Definition

Friend Folder is the Owner-owned persistent M-PIN data area associated
with one specific Friend. The canonical relationship is: \## One Friend,
One Friend Folder. A Friend Folder contains the persistent state that
the corresponding Friend may load and use during an authorized
Synchronization Session. Examples may include Friend-specific:
conversations; memory; settings; preferences; documents; service state;
other persistent data defined by the Friend. The exact payload semantics
are Friend-defined. \## Structural Meaning Friend Folder is not merely a
visual directory. It is a structural: association boundary persistence
boundary visibility boundary access boundary within M-PIN.

# 11. Friend Folder Binding

## Definition

Friend Folder Binding is the association between a verified Friend
Identity and the Friend Folder assigned to that Friend within an M-PIN.
Conceptually: Friend Identity A ↕ Friend Folder A A conforming
implementation MUST prevent a Friend from arbitrarily rebinding itself
to another Friend’s Folder. The exact binding representation is
implementation-defined.

# 12. Friend Folder Isolation

## Definition

Friend Folder Isolation is the rule that one Friend does not receive
default visibility or access to another Friend’s Friend Folder.
Conceptually: Friend A → Friend Folder A

Friend A ✕ Friend Folder B Friend A ✕ Friend Folder C Friend Folder
Isolation remains applicable even when the Folders: exist inside the
same M-PIN; use the same physical Device; use the same Storage; use the
same M-PIN Service Provider. Common infrastructure does not imply common
Friend authority.

# 13. Domain

## v2 Status

Domain is not a separate normative Core entity in M-PIN v2.0. Historical
v1 material may use terms such as: Domain Service Domain One Domain Per
Friend Where those historical terms describe the Friend-specific Owner
data area, the v2 canonical term is: \## Friend Folder This terminology
reconciliation MUST NOT be interpreted as rewriting or deleting the
historical v1 record. \## Prohibited Interpretation A v2 implementation
MUST NOT infer this architecture: M-PIN │ └── Domain │ └── Friend Folder
merely because historical v1 text contains the word Domain. M-PIN v2
Core requires no such additional layer.

# 14. Storage

## Definition

Storage is the physical or logical persistence medium on which M-PIN
data is stored. Storage MAY include: local storage; Owner-controlled
cloud storage; removable storage; Provider-hosted storage; another
conforming persistence medium. \## Distinction Storage ≠ M-PIN

Storage ≠ Owner Storage location does not determine architectural
ownership.

# 15. Device

## Definition

Device is a physical computing or embodied system through which the
Owner, M-PIN, or Friend may operate. Examples may include: personal
computer; phone; tablet; robot; terminal; other computing hardware. \##
Distinction Device ≠ M-PIN Identity M-PIN continuity is not inherently
bound to one Device.

# 16. M-PIN Service Provider

## Definition

M-PIN Service Provider, or Provider, is an optional entity that
implements or supplies M-PIN-related infrastructure. A Provider MAY
supply: hosting; Storage; synchronization infrastructure; authentication
infrastructure; recovery infrastructure; migration infrastructure. \##
Distinction M-PIN Standard ≠ M-PIN Service Provider A Provider is not
automatically the Owner. A Provider is not mandatory for every valid
M-PIN deployment.

# 17. Provider Identity

## Definition

Provider Identity identifies an M-PIN Service Provider where a Provider
participates in the deployment. Provider Identity MUST NOT be treated as
M-PIN Identity. Provider migration therefore does not inherently imply
M-PIN replacement.

# 18. Synchronization

## Definition

Synchronization is the bounded process through which a Friend obtains
authorized use of its associated Friend Folder state and, where
authorized, participates in persistence back to that Folder.
Synchronization does not mean that all M-PIN data becomes visible to the
Friend. Synchronization is Friend-specific.

# 19. Synchronization Session

## Definition

Synchronization Session, or Session, is the bounded authorization
context within which one active Friend interacts with its Friend Folder
through M-PIN. The v2.0 canonical invariant is: \## One M-PIN, One
Active Friend, One Synchronization Session. A Session has a beginning
and termination boundary. Termination ends that Session’s M-PIN access
authority. The exact token or transport representation of a Session is
deferred.

# 20. Active Friend

## Definition

Active Friend is the Friend currently participating in the active
Synchronization Session of an M-PIN. Under the v2.0 Core synchronization
invariant, an M-PIN MUST NOT simultaneously expose active
synchronization authority to multiple Friends. This rule concerns active
M-PIN synchronization. It does not assert that all Friend applications
or unrelated service processes must stop running.

# 21. Runtime

## Definition

Runtime is the Friend-controlled execution environment in which the
Friend provides its service and processes data. Runtime belongs to the
Friend’s service execution responsibility. M-PIN does not require
control of the Friend’s internal Runtime.

# 22. Runtime State

## Definition

Runtime State is temporary or working state used or produced during
Friend execution. Conceptually: Persistent State ↓ LOAD Runtime State ↓
WORK Runtime State’ Runtime State does not automatically become M-PIN
Persistent State. A Friend may maintain its own internal operational
state independently of M-PIN.

# 23. Persistent State

## Definition

Persistent State is the authoritative current M-PIN state that survives
beyond a Synchronization Session according to the M-PIN persistence
rules. For a Friend relationship, the relevant persistent payload
resides within that Friend’s Friend Folder. Persistent State changes
only through a valid persistence operation.

# 24. Current State

## Definition

Current State is the currently authoritative committed Persistent State
for the relevant M-PIN persistence scope. A successful new Commit
replaces the prior authoritative state for that scope. Current State
does not imply M-PIN-managed historical versioning.

# 25. Payload

## Definition

Payload is the Friend-specific persistent content stored within a Friend
Folder. The Friend defines the payload’s: meaning; internal semantic
structure; service-specific content; interpretation. M-PIN does not need
to semantically understand the Friend payload in order to preserve the
ownership, identity, integrity, Session, and persistence boundaries. \##
v2.0 Boundary Friend defines payload semantics and service-specific
structure

M-PIN defines minimum interoperability/security envelope requirements
needed by the M-PIN boundary The exact .MPIN container and serialization
format are deferred.

# 26. Envelope

## Definition

Envelope is the minimum M-PIN-defined structural metadata surrounding or
associated with Friend payload where necessary to preserve M-PIN-level
identity, binding, integrity, persistence, or interoperability
requirements. An Envelope MAY contain information such as: M-PIN
identity reference Friend identity reference Friend Folder
identity/reference state/integrity metadata format/version metadata
other minimum M-PIN-required metadata This list is conceptual. The exact
normative Envelope schema is deferred from the v2.0 Architecture Freeze.
\## Distinction Envelope ≠ Friend payload semantics M-PIN MUST NOT
require semantic interpretation of the entire Friend payload merely to
provide the Envelope.

# 27. Load

## Definition

Load is the operation by which the current authorized Friend Folder
state becomes available to the corresponding Friend Runtime during a
valid Synchronization Session. Conceptually: Friend Folder ↓ LOAD Friend
Runtime Load authority does not by itself grant persistence authority.

# 28. Read Once

## Definition

Read Once is the v1-derived synchronization principle that the Friend
obtains the relevant saved Friend Folder state when the authorized
Synchronization Session is established rather than receiving
unrestricted perpetual background access to M-PIN. Read Once does not
prohibit the Friend from using the loaded state throughout its
authorized Runtime. It does not create permanent M-PIN access after
Session termination. The detailed Session behavior is defined in Core
08.

# 29. Save

## Definition

Save is the Owner-authorized expression of persistence intent for M-PIN
state. Conceptually: Runtime State’ ↓ Owner SAVE ↓ authorized
persistence process Save is an authority event, not merely an internal
write performed by the Friend. \## Distinction A Friend’s internal:
autosave; cache; database write; draft save; transaction write does not
automatically constitute M-PIN Save.

# 30. Commit

## Definition

Commit is the technical operation that establishes the authorized new
M-PIN Persistent State following a valid Save. Conceptually: Owner SAVE
↓ validation ↓ COMMIT ↓ new Current State A Commit MUST satisfy the
applicable authority, Session, binding, integrity, and persistence
requirements.

# 31. Atomic Commit

## Definition

Atomic Commit is the requirement that a persistence operation either
establishes a valid new Current State or leaves the previous valid
Current State authoritative. Conceptually: State A → State B or: State A
→ State A not: State A → partially valid State B Implementation
mechanisms MAY differ. The observable persistence property MUST be
preserved.

# 32. No-Save Termination

## Definition

No-Save Termination is Session termination without an Owner-authorized
M-PIN Save for the unsaved Runtime changes. Conceptually: Persistent
State A ↓ Runtime State B ↓ Session ends without Save ↓ Persistent State
A remains No-Save Termination MUST NOT silently convert Runtime State B
into M-PIN Persistent State.

# 33. Current-State-Only

## Definition

Current-State-Only is the M-PIN persistence rule under which the Core
treats the current committed state as authoritative without requiring
M-PIN-managed historical state versions. It excludes a Core requirement
for: rollback history; automatic version timeline; time travel;
perpetual snapshots. It does not prohibit backups. It also does not
prohibit historical service content inside the current Friend payload.

# 34. Backup

## Definition

Backup is a protected copy used to support resilience or recovery of
M-PIN state. A Backup is not automatically: an active M-PIN; a
historical version exposed to the Owner; a rollback timeline. Multiple
protected Backup copies MAY exist while the architecture preserves one
authoritative active continuity.

# 35. Authoritative Active Continuity

## Definition

Authoritative Active Continuity is the single logical M-PIN continuity
recognized as authoritative for active synchronization and persistence.
The existence of copied or backed-up data does not automatically create
multiple legitimate active continuities. v2.0 does not claim perfect
global enforcement against completely disconnected offline clones
without a coordination mechanism.

# 36. Permission

## Definition

Permission is an Owner-authorized allowance for a defined M-PIN
operation or scope. Permission MAY constrain: Friend; Friend Folder;
Session; operation; time or validity; persistence authority. Permission
MUST NOT be inferred solely from a Friend’s desire to access data.

# 37. Authentication

## Definition

Authentication is the process of establishing that a principal or
credential corresponds to the identity it claims. Authentication may
apply to: Owner; Friend; Device; Provider. Authentication does not by
itself determine all authorization rights.

# 38. Authorization

## Definition

Authorization is the determination that an authenticated or otherwise
established principal has authority to perform a particular operation
under the applicable M-PIN rules. Conceptually: Identity established ↓
Authentication

Operation allowed? ↓ Authorization Authorization MUST remain scoped.

# 39. Revocation

## Definition

Revocation is the withdrawal or invalidation of previously granted M-PIN
access authority. Revocation of M-PIN authority MUST prevent continued
use of that revoked M-PIN authority. Revocation does not necessarily
terminate every independent process inside the Friend’s own service.

# 40. Isolation

## Definition

Isolation is the architectural property that prevents one Friend’s
authorized M-PIN relationship from automatically extending into another
Friend’s relationship or data area. The principal v2 Core isolation
boundary is Friend Folder Isolation.

# 41. Zero Visibility

## Definition

Zero Visibility is the principle that a Friend has no default visibility
into M-PIN data outside the data boundary authorized for that Friend.
Zero Visibility does not mean that an authorized Friend cannot see the
plaintext legitimately supplied to it for its own processing. It means
unrelated M-PIN state is not exposed merely because the Friend is
connected.

# 42. Friend Sovereignty

## Definition

Friend Sovereignty is the principle that the Friend remains responsible
for and autonomous over its own service implementation and evolution.
Friend Sovereignty does not grant the Friend ownership authority over
Owner-controlled M-PIN state.

# 43. Owner Data Sovereignty

## Definition

Owner Data Sovereignty is the architectural principle that
Owner-controlled M-PIN Persistent State remains under Owner authority
rather than becoming provider-controlled persistence merely because an
external service processes it. This principle applies to M-PIN state. It
MUST NOT be used to erase legitimate independent Friend Service Records.

# 44. Zero Requirement

## Definition

Zero Requirement is the principle that M-PIN specifies required behavior
without unnecessarily requiring one internal Friend implementation
technology. Zero Requirement means: minimum required external behavior +
Friend implementation autonomy It does not mean that M-PIN has no
conformance requirements.

# 45. Device Independence

## Definition

Device Independence is the property that M-PIN continuity and identity
are not inherently bound to one physical Device. Moving to another
compatible Device does not inherently create a new M-PIN.

# 46. Provider Independence

## Definition

Provider Independence is the property that the M-PIN Standard and Owner
continuity are not inherently defined by one permanent M-PIN Service
Provider. A Provider MAY implement M-PIN infrastructure. The Standard
remains conceptually independent of that Provider.

# 47. Portability

## Definition

Portability is the ability to preserve the relevant M-PIN continuity
when moving between compatible Devices, Storage environments, or M-PIN
Service Providers. Portability does not mean automatic semantic
migration from one Friend to a different Friend.

# 48. Migration

## Definition

Migration is a controlled transition of M-PIN continuity from one
compatible environment to another. Examples include: Device A → Device B
Storage A → Storage B Provider A → Provider B A valid or successful
Migration MUST preserve the same M-PIN identity and valid Friend Folder
relationships. Migration is distinct from creating a new independent
M-PIN.

# 49. Recovery

## Definition

Recovery is the process of restoring legitimate access or authority to
an existing M-PIN after loss, failure, or credential unavailability
where sufficient recovery material remains. Recovery is not defined as
creating a replacement identity merely because access was lost.

# 50. Authority Recovery

## Definition

Authority Recovery restores the Owner’s legitimate ability to exercise
M-PIN authority. Examples may include restoration after: lost Device;
lost credential; Provider failure. Authority Recovery does not itself
reconstruct missing persistent data.

# 51. Data Recovery

## Definition

Data Recovery restores M-PIN state from an available valid copy, Backup,
or recoverable Storage source. Conceptually: Authority Recovery ≠ Data
Recovery Both may be needed after a failure.

# 52. Service Record

## Definition

Service Record is data independently maintained by a Friend because of
the Friend’s legitimate service, operational, contractual, security,
institutional, or legal responsibilities. Examples may include: clinical
records; transaction records; invoices; billing records; security
records; safety records; regulatory records. \## Distinction
Owner-controlled M-PIN State ≠ Friend Service Record A Service Record
does not automatically belong inside the Friend Folder. A Friend Folder
does not automatically replace a Service Record. \## Anti-Loophole Rule
A Friend MUST NOT classify arbitrary or excessive synchronized M-PIN
data as a Service Record merely to bypass M-PIN persistence or isolation
boundaries.

# 53. Profile

## Definition

Profile is a domain-specific application of the M-PIN Core. A Profile
MAY add requirements required by its environment. A Profile MUST NOT
weaken Core requirements. M-PIN v2.0 defines four validation Profiles:
AI Robotics Healthcare Commerce

# 54. Profile Composition

## Definition

Profile Composition is the application of more than one M-PIN Profile to
a real-world system containing multiple relevant Friend or Device roles.
For example: Healthcare Robot = Core + Robotics Profile + Healthcare
Profile + AI Profile where applicable. Profile Composition does not
merge Friend Folders or remove Core isolation.

# 55. Conformance

## Definition

Conformance is satisfaction of the normative observable requirements of
the M-PIN Core and any applicable Profile. Conformance is primarily
behavioral. Use of a particular M-PIN-branded SDK, API, or Provider does
not alone establish conformance.

# 56. Conforming Friend

## Definition

Conforming Friend is a Friend whose M-PIN-facing behavior satisfies the
applicable Core and Profile requirements. At minimum, this includes
correct behavior concerning: Friend Identity; Friend Folder binding;
isolation; Session boundaries; authorized loading; Owner-controlled
persistence; termination; security requirements. The detailed test suite
is defined in Core 12.

# 57. Conforming Provider

## Definition

Conforming Provider is an M-PIN Service Provider whose M-PIN-facing
infrastructure preserves the applicable Core requirements for the
functions it implements. A Provider MUST NOT claim architectural
ownership merely because it provides infrastructure. A deployment
without a Provider is not non-conforming merely because no Provider
exists.

# 58. Friend Internal Autosave

## Definition

Friend Internal Autosave is a persistence mechanism internal to a
Friend’s own service. It is not automatically an M-PIN Save or Commit.
Conceptually: Friend internal autosave ≠ Owner M-PIN SAVE This
distinction prevents Friend implementation behavior from silently
redefining M-PIN persistence authority.

# 59. Disclosure

## v2.0 Status

Disclosure is a candidate interoperability concept identified during v2
Healthcare and Commerce Profile validation. Conceptually, Disclosure
would permit Owner-authorized selected information to be provided from
one Friend relationship to another without granting direct access to the
source Friend Folder. Friend A │ selected information ▼ Owner
authorization │ ▼ Disclosure │ ▼ Friend B For M-PIN v2.0: Disclosure =
V2-NEW CANDIDATE DEFERRED FROM CORE Disclosure is defined here only to
prevent terminology ambiguity in the Profiles and publication record. It
is NOT a mandatory v2.0 Core protocol.

# 60. Owner-Mediated Disclosure

## Definition

Owner-Mediated Disclosure is the candidate model in which selected
information is provided to a recipient Friend under explicit Owner
authorization without granting that recipient direct access to another
Friend’s Friend Folder. The concept MUST NOT be interpreted as: Friend A
↓ direct access to Friend B Folder The exact Disclosure object,
recipient persistence behavior, authorization model, replay protection,
and protocol remain deferred.

# 61. Interoperability

## Definition

Interoperability is the ability of compatible M-PIN implementations or
service relationships to operate across defined boundaries without
requiring common ownership or shared Friend Folder authority. M-PIN v2.0
does not define interoperability as universal data sharing.

# 62. Envelope Integrity

## Definition

Envelope Integrity is the property that M-PIN-required structural
metadata and its binding to the relevant persistent state can be
validated against unauthorized modification according to the applicable
implementation. The exact integrity-proof mechanism is deferred.

# 63. Fail Closed

## Definition

Fail Closed is the security behavior in which M-PIN denies or terminates
the relevant operation when required authority or security conditions
cannot be established. Examples include inability to establish: Owner
authorization; Friend Identity; Friend Folder binding; Session validity;
required integrity. Failure MUST NOT silently expand authority.

# 64. Replay

## Definition

Replay is the reuse of previously valid authentication, authorization,
Session, Save, or persistence material outside its legitimate validity
context. A conforming security model MUST address replay where replay
could recreate unauthorized M-PIN authority. The exact replay-protection
mechanism is deferred.

# 65. Freshness

## Definition

Freshness is the property used to distinguish the valid current
authority or state from stale, superseded, or replayed material where
required. The exact counter, timestamp, nonce, generation, or equivalent
mechanism is not fixed by the v2.0 Architecture.

# 66. Integrity

## Definition

Integrity is the property that M-PIN state or security-relevant metadata
has not been accepted after unauthorized or undetected modification.
Integrity does not mean semantic truth. For example: cryptographically
intact healthcare data ≠ medically correct healthcare data M-PIN
protects architectural integrity. The Friend remains responsible for the
semantics of its service data.

# 67. Confidentiality

## Definition

Confidentiality is protection against unauthorized disclosure of M-PIN
state. Confidentiality requirements apply according to the relevant
access boundary. An authorized Friend may receive plaintext required for
its own service. That does not authorize unrelated Friends or
infrastructure actors to receive the same plaintext.

# 68. Encryption at Rest

## Definition

Encryption at Rest is cryptographic protection applied to persistent
M-PIN data while stored. M-PIN v2.0 requires protected persistent
storage as specified in Core 10. The exact cryptographic algorithm and
key architecture are deferred. Provider participation MUST NOT be
interpreted as proof that the Provider necessarily lacks plaintext or
key capability unless the implementation explicitly establishes that
property.

# 69. Session Termination

## Definition

Session Termination is the end of the current Synchronization Session
and its M-PIN access authority. Termination may result from: normal
Session completion; Owner action; revocation; abnormal disconnect;
required security failure; other protocol-defined termination condition.
A terminated Session MUST NOT continue as hidden M-PIN authority.

# 70. Abnormal Disconnect

## Definition

Abnormal Disconnect is an unexpected loss of the conditions required to
maintain the Synchronization Session. An Abnormal Disconnect terminates
the affected M-PIN Session according to Core 08. Unsaved Runtime changes
MUST NOT automatically become M-PIN Persistent State because of the
disconnect.

# 71. Friend Data Semantics

## Definition

Friend Data Semantics are the meanings and service-specific
interpretation of the Friend payload. Friend Data Semantics belong to
the Friend. M-PIN MUST NOT require full semantic interpretation of
Friend data merely to enforce the M-PIN ownership boundary.

# 72. Structural Validation

## Definition

Structural Validation is M-PIN-level validation necessary to determine
whether a persistence or protocol object satisfies required structural
conditions. It MAY include validation of: required identity references;
Friend Folder binding; Envelope structure; integrity metadata; Session
authorization; format/version compatibility. Structural Validation does
not mean M-PIN understands the business meaning of every Friend payload
field.

# 73. Semantic Validation

## Definition

Semantic Validation is validation of the service-specific meaning or
correctness of Friend data. Semantic Validation is generally a Friend
responsibility unless a specific Profile or future protocol explicitly
requires otherwise. Conceptually: M-PIN validates boundary / structure /
authority

Friend validates service semantics

# 74. Standard

## Definition

M-PIN Standard is the normative architecture and behavioral
specification defining M-PIN compatibility. The Standard is distinct
from any one implementation, Provider, Friend, Device, or commercial
deployment.

# 75. Implementation

## Definition

Implementation is a concrete technical realization of some or all
M-PIN-defined roles and behavior. Different implementations MAY use
different: software architectures; storage systems; protocols;
cryptographic libraries; operating systems; deployment models. They
remain conformant only if the required normative behavior is preserved.

# 76. Reference Implementation

## Definition

Reference Implementation is a future implementation that may demonstrate
one way to satisfy the M-PIN Standard. A Reference Implementation, if
created, MUST NOT automatically redefine optional implementation choices
as mandatory Core architecture. The v2.0 Architecture Freeze does not
require a production Reference Implementation.

# 77. Core

## Definition

Core is the industry-neutral normative architecture of M-PIN v2.0. The
Core consists of twelve documents: 01 Scope & Design Constitution 02
Core Principles 03 Terminology 04 Core Architecture 05 Owner & Identity
06 Friend & Friend Folder Model 07 Permission Model 08 Session Protocol
09 Runtime & Persistence 10 Security & Threat Model 11 Portability &
Recovery 12 Conformance Specification

# 78. FROZEN

## Definition

FROZEN means that the v2.0 architectural decision is considered complete
for the published version. A FROZEN item is not reopened merely because:
a question is rephrased; another example appears; another industry is
considered; another implementation method is preferred. A future version
MAY change a FROZEN architecture decision when justified by actual new
evidence.

# 79. LOCKED

## Definition

LOCKED is the historical project term used to indicate that a design
decision had been accepted and should no longer be repeatedly
reconsidered during the same specification process. v2 publication
primarily uses FROZEN for version-level status. Historical LOCKED
Decisions remain part of v1 provenance.

# 80. DEFERRED

## Definition

DEFERRED means that the architecture boundary is sufficiently defined
for v2.0, but an exact implementation or protocol choice is
intentionally left for later work. DEFERRED does not mean unresolved
architectural contradiction. Examples include: exact .MPIN container;
serialization; crypto suite; key hierarchy; Friend credential format;
Session token format; Disclosure schema.

# 81. V2-NEW

## Definition

V2-NEW is a provenance classification for a concept or formalization
introduced during v2 rather than silently attributed to v1. A V2-NEW
concept MAY still be compatible with v1 principles. The tag records
provenance, not incompatibility.

# 82. Canonical State Vocabulary

M-PIN v2 uses the following state vocabulary: Friend Folder │ │ contains
▼ Persistent State │ │ current authoritative form ▼ Current State │ │
LOAD ▼ Runtime State │ │ Friend processing ▼ Runtime State’ │ │ Owner
SAVE ▼ Commit │ ▼ new Current State Without Save: Runtime State’ │ │
Session termination ▼ discard relative to M-PIN persistence

Previous Current State remains authoritative

# 83. Canonical Identity Vocabulary

Owner │ ├── Owner Authority │ └── M-PIN Identity │ ├── Friend Identity A
│ ↕ │ Friend Folder A │ └── Friend Identity B ↕ Friend Folder B Device
Identity, Friend Account Identity, and Provider Identity remain separate
concepts.

# 84. Canonical Deployment Vocabulary

M-PIN Standard │ ├── Local Implementation │ ├── Provider Implementation
│ └── Other Conforming Implementation No Provider is implied merely by
the existence of M-PIN.

# 85. Canonical Access Vocabulary

Identity ↓ Authentication ↓ Authorization ↓ Permission ↓ Synchronization
Session ↓ Friend Folder access These terms MUST NOT be collapsed into
one undifferentiated concept.

# 86. Canonical Persistence Vocabulary

Runtime activity ≠ Save

Save ≠ Commit

Commit = authorized establishment of new Current State This distinction
is normative.

# 87. Canonical Isolation Vocabulary

The normative v2 term is: \## Friend Folder Isolation The following MUST
NOT be introduced as separate equivalent Core entities without a future
specification change: Domain Isolation Shared Friend Domain Universal
Friend Data Pool Cross-Friend Workspace Historical v1 Domain terminology
is handled only through the reconciliation defined in this document.

# 88. Canonical Responsibility Boundary

OWNER authority over Owner-controlled persistence

M-PIN ownership / identity / permission / Session / isolation /
persistence boundary

FRIEND service / Runtime / UX / payload semantics / internal
implementation

PROVIDER optional M-PIN infrastructure

STORAGE persistence medium

DEVICE physical execution/access environment These responsibilities MUST
remain distinguishable.

# 89. Terminology Conflict Rule

If another M-PIN v2 document uses a term inconsistently with this
document: Core 01 constitutional invariants MUST be preserved. This Core
03 canonical definition SHOULD govern terminology. The inconsistency
SHOULD be treated as a documentation defect. The defect MUST NOT be
resolved by silently inventing a new architectural entity.

# 90. Terminology Freeze

The terminology defined here is FROZEN for M-PIN v2.0.
Implementation-specific names MAY differ internally. Public claims of
M-PIN v2.0 conformance MUST preserve the architectural meanings defined
here.

# 91. Canonical Summary

Owner central authority

M-PIN Owner-centered persistent continuity boundary

Friend external service principal

Friend Folder Owner-owned persistent area associated with one Friend

Friend Folder Binding verified Friend ↔ Folder association

Friend Folder Isolation no default cross-Friend Folder access

Runtime Friend-controlled execution environment

Runtime State working/temporary service state

Persistent State state surviving according to M-PIN persistence rules

Current State authoritative committed persistent state

Payload Friend-defined persistent content

Envelope minimum M-PIN-defined boundary metadata

Load authorized delivery of current state to Friend Runtime

Save Owner persistence intent

Commit technical establishment of new Current State

Atomic Commit all-or-previous-state persistence property

Synchronization Session bounded M-PIN access context

Permission Owner-authorized operation/scope

Authentication establishment of claimed identity

Authorization determination of permitted action

Provider optional M-PIN infrastructure operator

Storage persistence medium

Device physical computing/embodied environment

Service Record Friend’s legitimate independent record

Portability continuity across compatible environments

Recovery restoration of legitimate continuity/authority

Profile domain-specific application of unchanged Core

Conformance satisfaction of normative observable behavior

# 92. Terminology Thesis

M-PIN owns no Friend service semantics, Friend owns no automatic
authority over Owner persistence, and common M-PIN storage creates no
common Friend visibility. The vocabulary of M-PIN v2.0 exists to keep
those boundaries explicit.

## M-PIN v2.0 — Core 03 / Terminology

## Status: FROZEN
