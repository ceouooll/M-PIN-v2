# M-PIN v2.0

## Core 06 — Friend & Friend Folder Model

**Status:** FROZEN **Version:** 2.0 **Document Type:** Normative Core
Specification

------------------------------------------------------------------------

# 1. Purpose

This document defines the Friend and Friend Folder model of M-PIN v2.0.

It specifies:

- what constitutes a Friend;
- how a Friend is associated with a Friend Folder;
- how a Friend Folder is created;
- how an existing Friend Folder is reused;
- what may be stored inside a Friend Folder;
- who owns, interprets, and manages that data;
- how Friend Folder visibility and isolation operate;
- how Friend evolution affects the Folder relationship.

This document defines the canonical persistent relationship between
M-PIN and a Friend.

------------------------------------------------------------------------

# 2. Core Relationship

The canonical M-PIN relationship is:

> **One Friend, One Friend Folder.**

Conceptually:

``` text
M-PIN
  │
  ├── Friend Folder A ↔ Friend A
  ├── Friend Folder B ↔ Friend B
  └── Friend Folder C ↔ Friend C
Each Friend Folder is associated with one Friend relationship.
A Friend MUST NOT receive default access to another Friend's Friend Folder.
```

# 3. Friend

A Friend is an external service principal that participates in M-PIN
under an authorized synchronization relationship. A Friend MAY be an: AI
service; healthcare service; commerce service; robot service;
transportation service; other compatible service. The Friend abstraction
is intentionally service-neutral. M-PIN Core MUST NOT assume that a
Friend is an AI.

# 4. Friend Responsibility

The Friend remains responsible for its own: service Runtime native UX
internal implementation payload semantics business logic
service-specific data management product evolution M-PIN does not become
the Friend’s internal application platform. The Friend continues to
provide its service through its own Runtime and native UX.

# 5. Friend Folder

A Friend Folder is the Owner-owned persistent M-PIN data area associated
with one specific Friend. The Friend Folder is the location in the M-PIN
architecture where that Friend’s Owner-controlled persistent state is
maintained. Conceptually: Owner │ ▼ M-PIN │ ▼ Friend Folder │ ▼ Friend
The Friend Folder belongs to the Owner’s M-PIN continuity. The Friend
uses it under M-PIN authority.

# 6. Friend Folder Is Not Merely a Directory

The word Folder MUST NOT be interpreted as only a visual filesystem
convention. Friend Folder represents a structural: association boundary
access boundary visibility boundary persistence boundary An
implementation MAY physically represent a Friend Folder as: a filesystem
directory; an encrypted object; a database namespace; a storage
container; another conforming structure. The physical representation is
not normative. The architectural boundary is.

# 7. No Separate Domain Entity

M-PIN v2.0 does not introduce a separate Domain entity between M-PIN and
Friend Folder. The normative structure is: M-PIN ↓ Friend Folder ↓
Friend not: M-PIN ↓ Domain ↓ Friend Folder ↓ Friend Historical v1 Domain
terminology remains part of the v1 record. Where it refers to the
Friend-specific persistent area, the v2 canonical term is Friend Folder.

# 8. Owner Ownership

The Friend Folder is Owner-owned M-PIN persistent state. The fact that
the corresponding Friend: creates service data; interprets the data;
modifies working state; defines the payload structure does not transfer
architectural ownership of the M-PIN Friend Folder to the Friend.
Conceptually: Owner owns / authorizes persistence

Friend interprets / operates service data

M-PIN preserves the boundary

# 9. Owner Owns, Friend Manages Its Meaning

M-PIN separates ownership from semantic management. The canonical rule
is: Owner owns the Friend Folder state. Friend understands and manages
the Friend-specific data semantics. M-PIN preserves the ownership and
access boundary. Therefore M-PIN MUST NOT require the Owner to manually
understand the Friend’s internal data model. Likewise, M-PIN itself MUST
NOT need to understand every service-specific field.

# 10. Friend Payload

The Friend Folder contains a Friend-defined payload. Depending on the
Friend, the payload MAY include current persistent representations of:
conversation lists conversation contents Friend memory preferences
settings service configuration documents Owner-created service data
Friend-specific continuity state other Friend-defined persistent data
This list is illustrative. The Core does not define one universal
payload schema for all Friends.

# 11. Historical Content Inside Payload

A current Friend payload MAY contain historical service content. For
example: AI Friend → conversation history

Commerce Friend → order or receipt information

Healthcare Friend → healthcare documents

Robot Friend → Owner-specific configuration or continuity data This does
not violate Current-State-Only. The distinction is: current payload
containing historical service content ≠ M-PIN maintaining historical
versions of the Friend Folder state

# 12. Friend Defines Payload Semantics

The Friend defines the meaning of its payload. For example, only the
Friend may know that a particular structure represents: conversation
ordering memory relationship service preference model-specific context
product configuration robot behavior preference M-PIN does not need to
interpret those meanings to preserve the Friend Folder.

# 13. Friend Defines Service-Specific Structure

The Friend MAY define the service-specific structure of its payload.
M-PIN MAY define minimum surrounding structural requirements necessary
for: M-PIN identity; Friend identity; Friend Folder binding; integrity;
format/version handling; persistence validation. Conceptually: Friend
Folder │ ├── M-PIN-required minimum envelope │ └── Friend-defined
payload The exact Envelope and container format remain deferred.

# 14. Decision 120 Disposition

The architecture-level responsibility boundary is: Friend → payload
meaning → service-specific payload structure

M-PIN → minimum boundary metadata → identity/binding requirements →
integrity requirements → persistence boundary This resolves the
architectural responsibility question represented by v1 Decision 120. It
does not freeze an exact binary format, serialization, or universal
Friend payload schema.

# 15. M-PIN Does Not Semantically Interpret the Folder

M-PIN MUST NOT require semantic understanding of the complete Friend
payload merely to: store it; protect it; associate it with the correct
Friend; load it; validate the M-PIN boundary; Commit it. Conceptually:
M-PIN understands: identity binding authority structure required by
M-PIN integrity

Friend understands: payload meaning service semantics business logic

# 16. Friend Data Is Managed Through the Friend

The Friend is the normal service interface through which its
Friend-specific data is created, interpreted, and modified. M-PIN is not
intended to provide a generic editor for arbitrary Friend payloads.
Conceptually: Owner ↓ Friend native UX ↓ Friend Runtime ↓ authorized
persistence ↓ Friend Folder not: Owner ↓ generic M-PIN editor ↓ manually
edits arbitrary Friend internals This preserves Friend Sovereignty and
data semantics.

# 17. M-PIN Management Boundary

M-PIN MAY expose management functions necessary for the M-PIN
relationship, such as: authorization; connection; revocation; migration;
recovery; Folder relationship status; security state. Such management
functions MUST NOT be interpreted as permission for M-PIN to become the
Friend’s general service-data editor.

# 18. First Synchronization

When a Friend first establishes an M-PIN relationship, M-PIN resolves
whether a Friend Folder already exists. Canonical flow: Friend ↓ Owner
initiates synchronization ↓ Owner authority established ↓ Friend
Identity verified ↓ Friend Folder lookup If no corresponding Friend
Folder exists: Folder absent ↓ Owner approval requested ↓ Owner approves
↓ Friend Folder created ↓ Friend ↔ Friend Folder binding established A
Friend Folder MUST NOT be created without the required Owner
authorization.

# 19. First Folder Creation

Friend Folder creation establishes a new persistent relationship between
the M-PIN and the verified Friend. Creation MUST establish enough
information to preserve: M-PIN association Friend Identity association
Friend Folder identity/binding required security metadata valid initial
persistent state The exact metadata representation is deferred.

# 20. Owner Rejects Folder Creation

If the Owner does not authorize creation of the missing Friend Folder:
Friend Folder absent ↓ Owner rejects creation ↓ no Friend Folder created
↓ no M-PIN synchronization relationship established The Friend MAY
continue operating independently according to its own service behavior.
M-PIN MUST NOT silently create the Folder in the background.

# 21. Initial Friend Folder State

A newly created Friend Folder MAY begin with an empty or Friend-defined
initial valid state. Conceptually: new Friend Folder ↓ initial valid
state ↓ Friend Runtime No historical state is required for a first
relationship.

# 22. Import During First Relationship

A Friend MAY have pre-existing service state outside M-PIN when the
Owner first establishes the M-PIN relationship. If a conforming
implementation supports importing that state, the import MUST preserve:
Owner authorization; correct Friend binding; applicable integrity;
persistence rules. The Core does not require one universal legacy-import
mechanism. Import MUST NOT grant the Friend access to unrelated Friend
Folders.

# 23. Returning Synchronization

When the Friend later reconnects: Friend Identity verified ↓ existing
Friend Folder resolved ↓ binding validated ↓ Synchronization Session
established ↓ Current State loaded The existing Friend Folder MUST be
reused for the same continuing Friend relationship. M-PIN MUST NOT
silently create another independent Friend Folder merely because a new
Session begins.

# 24. Folder Discovery

A Friend SHOULD be able to resolve its own Friend Folder without
requiring the Owner to manually navigate internal Friend Folder names on
every connection. Conceptually: verified Friend Identity ↓ M-PIN
resolves binding ↓ corresponding Friend Folder The exact discovery
mechanism is deferred.

# 25. Folder Discovery Privacy

Resolving one Friend Folder SHOULD NOT require exposing the names,
identities, or metadata of unrelated Friend Folders to the active
Friend. Conceptually: Friend A ↓ resolve Friend Folder A not: Friend A ↓
receive list of: A, B, C, Hospital, Retailer, AI, … unless such
information is independently authorized and required. This
recommendation supports Zero Visibility.

# 26. Friend Folder Naming

A human-readable Folder name MAY exist. The display name MUST NOT be the
sole security binding. For example: folder display name = “ChatGPT” does
not itself prove the identity of the Friend attempting access. Security
relies on the verified Friend relationship and binding.

# 27. Initial Load

After a valid Synchronization Session is established, the current
committed state of the corresponding Friend Folder is made available to
the Friend as required by the synchronization model. Conceptually:
Friend Folder ↓ Current State ↓ LOAD ↓ Friend Runtime The Friend then
interprets the payload through its own service logic.

# 28. Read Once

M-PIN v2 preserves the v1 Read Once principle. The Friend receives the
relevant saved state as part of establishing the authorized Session.
Read Once means the Friend does not obtain unrestricted perpetual
background access to the Friend Folder merely because it synchronized
once. It does not mean the Friend must repeatedly reload the Folder for
every individual Runtime operation.

# 29. Runtime Use

Once loaded, the Friend may use the synchronized state during its
Runtime. Conceptually: Friend Folder State ↓ LOAD ↓ Friend Runtime ↓
Friend native service behavior The Friend MAY create temporary Runtime
State that differs from the saved Friend Folder state. That difference
is expected.

# 30. Runtime State Is Not Folder State

During Runtime: Friend Folder Current State A ↓ LOAD ↓ Runtime State A ↓
WORK ↓ Runtime State B At this point: Runtime State B ≠ Friend Folder
Current State B until a valid Save and Commit occur.

# 31. Owner Save

When the Owner chooses to persist the relevant current Friend state:
Runtime State B ↓ Owner SAVE ↓ M-PIN-level validation ↓ Commit ↓ Friend
Folder Current State B The Friend provides the persistent state or
update representation required by the conforming implementation. The
architectural result is one new valid Current State.

# 32. Full State vs Delta

M-PIN v2 does not require every Save to transmit the complete Friend
payload. A Friend or implementation MAY use: full state delta
transaction chunked update other conforming representation provided that
after successful Commit: Friend Folder ↓ one authoritative valid Current
State exists. Transport optimization MUST NOT silently create M-PIN
version-history semantics.

# 33. No Save

If the Owner does not Save: Friend Folder State A ↓ Runtime State B ↓ NO
SAVE ↓ Session ends ↓ Friend Folder State A remains M-PIN MUST NOT
silently persist Runtime State B merely because: time passed; the Friend
autosaved internally; the Session disconnected; the Friend closed; the
Device disconnected.

# 34. Multiple Saves

A Session MAY contain multiple Owner Saves. Example: Folder State A ↓
Runtime ↓ Save Folder State B ↓ Runtime continues ↓ Save Folder State C
After the final successful Commit, State C is authoritative. The Core
does not require A and B to remain available as M-PIN historical
versions.

# 35. Friend Internal Persistence

A Friend MAY maintain its own internal persistence according to its
service design. Examples may include: temporary server cache draft
autosave service database transaction processing operational log Such
persistence is not automatically M-PIN persistence. The M-PIN Friend
Folder remains governed by M-PIN persistence rules.

# 36. Friend Internal Autosave

A Friend’s internal autosave MUST NOT be interpreted as Owner Save
merely because the word save is used by the Friend. Conceptually: Friend
internal autosave ≠ M-PIN SAVE M-PIN Save has the specific meaning
defined by Core 03 and Core 09.

# 37. Service Record Boundary

Some Friend data may exist outside the Friend Folder as a legitimate
independent Service Record. Examples include: hospital clinical record
merchant transaction record billing record security record regulatory
record Therefore: Friend Folder ≠ all data ever held by Friend and:
Owner-controlled M-PIN State ≠ Friend Service Record

# 38. Service Record Anti-Loophole Rule

The Service Record distinction MUST NOT be used to bypass M-PIN
ownership or persistence boundaries. A Friend MUST NOT copy the complete
synchronized Friend Folder into an independent service database and
label the copy a Service Record merely to avoid M-PIN rules. Only data
legitimately required for the Friend’s independent service, operational,
contractual, security, institutional, or legal responsibilities may
qualify under the Service Record distinction.

# 39. Friend Folder Isolation

A Friend has no default right to another Friend’s Folder. Canonical
model: Friend A ↓ Friend Folder A

Friend B ↓ Friend Folder B Prohibited default relationship: Friend A ↓
Friend Folder B This applies even when the two Friends are operated by
the same company.

# 40. Same Company, Different Friends

Corporate ownership does not automatically merge Friend identities. For
example: Company X

├── Friend A │ ↕ │ Folder A │ └── Friend B ↕ Folder B If A and B are
distinct Friends under the M-PIN identity model, one MUST NOT
automatically access the other’s Folder.

# 41. Same Device, Different Friends

Running multiple Friends on the same physical Device does not merge
their Friend Folder authority. Conceptually: Device ├── Friend A →
Folder A └── Friend B → Folder B Physical co-location is not
authorization.

# 42. Same Provider, Different Friends

Using the same M-PIN Service Provider does not merge Friend Folders.
Provider │ └── hosts infrastructure for M-PIN │ ├── Folder A └── Folder
B Friend A still does not receive default access to Folder B.

# 43. Same Workflow, Different Friends

Participation in one real-world workflow does not remove Friend
isolation. For example: Retailer Friend Payment Friend Delivery Friend
may participate in one purchase. They remain separate Friend
relationships unless a specific authorized interoperability mechanism
provides selected information.

# 44. Friend Cannot Enumerate All Folders by Default

A Friend MUST NOT receive unrestricted enumeration of all Friend Folders
merely because it is connected to M-PIN. The Friend SHOULD receive only
the information required for its own relationship. This supports both
isolation and privacy.

# 45. Friend Cannot Select Arbitrary Folder

A Friend MUST NOT be allowed to bypass its binding by manually supplying
another Friend Folder identifier. Conceptually: Friend A ↓ requests
Folder B by identifier ↓ DENY unless a future explicitly authorized
protocol defines another behavior.

# 46. Cross-Friend Folder Access

Direct cross-Friend Folder access is not part of M-PIN v2.0 Core
interoperability. Therefore: Friend A X Friend Folder B remains the
default invariant. A Friend’s need for information does not alter this
rule.

# 47. Owner-Mediated Disclosure

Healthcare and Commerce Profile validation identified cases where
selected information may need to move between Friends. The candidate
model is: Friend A │ selected information ▼ Owner authorization │ ▼
Disclosure │ ▼ Friend B For v2.0: Owner-Mediated Disclosure = CANDIDATE
DEFERRED FROM CORE It does not grant Friend B access to Friend Folder A.

# 48. Friend Folder Sharing Is Not Disclosure

The following are different: selected authorized Disclosure and: sharing
an entire Friend Folder M-PIN v2.0 does not define direct Friend Folder
sharing as the interoperability mechanism.

# 49. Friend Evolution

A Friend may evolve without requiring a new Friend Folder. Examples
include: new software version new AI model new backend new database new
UX new infrastructure If the service remains the same Friend Identity
and continuity relationship, the existing Friend Folder SHOULD continue
to be used.

# 50. Friend Evolution Autonomy

M-PIN MUST NOT require approval of every internal Friend upgrade. The
Friend MAY evolve independently provided that: Friend Identity remains
valid; existing Folder binding remains valid; M-PIN-facing behavior
remains conformant; Owner persistence and isolation boundaries remain
intact. This preserves Friend Evolution Autonomy.

# 51. Payload Evolution

A Friend MAY evolve its payload structure. If it does so, the Friend
remains responsible for interpreting or migrating its own
service-specific data. M-PIN MAY require enough version or structural
metadata to determine whether the boundary object is valid. M-PIN does
not become responsible for semantic migration of arbitrary Friend data.

# 52. Payload Compatibility

If a new Friend version cannot interpret its existing Friend Folder
payload, that is primarily a Friend compatibility problem. The Friend
SHOULD provide an appropriate migration path where continuity is
intended. M-PIN MUST NOT invent semantic conversions it does not
understand.

# 53. Friend Replacement

A different Friend is not automatically entitled to the previous
Friend’s Folder. Conceptually: Friend A ↕ Folder A

Friend B ↕ Folder B Replacing a service product does not automatically
mean: Friend B ↕ Folder A M-PIN v2.0 does not define universal semantic
Friend-to-Friend migration.

# 54. Friend Identity Change

If a Friend’s identity representation changes while the logical Friend
remains the same, a conforming migration MAY preserve the existing
Friend Folder relationship if continuity can be securely established.
This MUST NOT become an unverified rebinding mechanism. The architecture
distinguishes: credential/identifier rotation from different Friend

# 55. Friend Account Change

A Friend may maintain its own account system. Changing Friend Account
details does not automatically reassign the Friend Folder. Any account
transition affecting access to M-PIN state MUST preserve Owner
authorization and prevent unauthorized exposure.

# 56. Owner Cannot Be Forced to Understand Payload

The Owner’s ownership of the Friend Folder does not require the Owner to
manually interpret proprietary or complex Friend data structures.
Ownership and semantic expertise are different. Conceptually: Owner owns
state

Friend understands state semantics This separation is intentional.

# 57. Owner Access vs Friend Management

Owner authority over the Friend Folder MUST NOT be interpreted as a
requirement that M-PIN provide arbitrary field-level editing of the
Friend payload. Owner management may include: authorize connect
disconnect revoke migrate recover delete where applicable while
service-specific content modification normally occurs through the
corresponding Friend.

# 58. M-PIN Is Not a Universal File Manager

M-PIN MAY have a management interface. That interface does not make
M-PIN a universal semantic file manager for all Friend data. M-PIN’s
architectural role is to preserve: ownership binding permission
isolation persistence security continuity not to reproduce every
Friend’s application behavior.

# 59. Friend Folder Deletion

Friend Folder deletion is distinct from: Session termination Friend
revocation Friend Account deletion Service Record deletion M-PIN
deletion A future implementation MUST treat these as separate lifecycle
operations. The exact deletion UX and retention workflow are not defined
by this Core document. Where a Profile or applicable obligation requires
independent Service Records, deleting a Friend Folder MUST NOT be
represented as automatically deleting those records.

# 60. Friend Folder Portability

Friend Folders are part of M-PIN continuity. A conforming M-PIN
migration SHOULD preserve: Friend Folder identity/binding Current State
required integrity metadata where the same M-PIN is moved between
compatible Devices, Storage, or Providers.

# 61. Provider Migration

Provider migration MUST NOT convert Friend Folders into Provider-owned
service silos. Conceptually: Provider A │ ▼ M-PIN X │ │ migrate ▼
Provider B │ ▼ same M-PIN X │ └── same Friend Folder relationships where
migration succeeds.

# 62. Device Migration

Moving M-PIN to another Device SHOULD preserve the Friend Folder set and
bindings. Device A ↓ M-PIN X ↓ migration/recovery Device B ↓ M-PIN X The
Owner should not have to recreate every Friend relationship merely
because the physical Device changed.

# 63. Recovery

Recovery of M-PIN state SHOULD restore valid Friend Folder relationships
where sufficient recoverable data and authority remain. Recovery MUST
NOT arbitrarily assign recovered Friend Folders to unrelated Friends.
Friend Identity and binding integrity remain applicable after recovery.

# 64. Backup

A Friend Folder MAY exist in protected Backup copies as part of M-PIN
resilience. A Backup copy does not become a separately active Friend
Folder merely because it exists. Restoration must preserve the
one-authoritative-continuity model.

# 65. Folder Integrity

A conforming implementation MUST protect security-relevant Friend Folder
structure and binding metadata from unauthorized modification. An
attacker MUST NOT be able to obtain another Friend’s data merely by
altering: Folder name Friend identifier binding metadata storage path
without satisfying the applicable authority and integrity checks.

# 66. Payload Integrity

M-PIN MUST provide or require sufficient integrity protection to prevent
unauthorized modification of persistent Friend Folder state from being
silently accepted as valid. Exact cryptographic mechanisms are deferred.
Integrity protection does not establish semantic truth.

# 67. Payload Confidentiality

Friend Folder state MUST be protected from unauthorized disclosure
according to Core 10. The corresponding authorized Friend may receive
plaintext necessary for its service. Other Friends MUST NOT receive that
plaintext merely because they share the same M-PIN infrastructure.

# 68. Compromised Friend

If Friend A is authorized to load Folder A and Friend A is compromised,
the attacker may obtain the plaintext legitimately exposed to Friend A.
M-PIN v2.0 does not claim otherwise. However, compromise of Friend A
MUST NOT automatically authorize: Folder B Folder C all M-PIN state
assuming the M-PIN boundary remains intact. This is one of the primary
security benefits of Friend Folder Isolation.

# 69. Compromised Provider

A compromised Provider may threaten data or functions available to that
Provider under the implementation’s trust model. The architecture does
not assume every Provider is zero-knowledge. Provider compromise
nevertheless MUST NOT be treated as legitimate Friend or Owner
authorization.

# 70. Friend Folder and Service Records

The complete Friend data universe may conceptually be: Friend │ ├──
Runtime State │ ├── Owner-controlled Friend Folder State │ └──
legitimate independent Service Records These categories may overlap in
subject matter but differ in architectural responsibility. Their
distinction MUST be preserved.

# 71. AI Example

An AI Friend Folder may contain current persistent state such as:
conversation list conversation content memory settings Owner-created
artifacts service-specific continuity data During synchronization: AI
Friend Folder ↓ AI Friend Runtime ↓ AI native interface Another AI
Friend does not automatically receive this Folder.

# 72. Robotics Example

A Robot Friend Folder may contain Owner-specific persistent state such
as: preferences configuration personalized continuity state
Friend-defined Owner context The Folder does not need to contain: robot
firmware manufacturer proprietary control logic entire robot operating
system merely because those are used by the robot. The Robot Friend
remains responsible for its own service internals.

# 73. Healthcare Example

A Hospital Friend Folder may contain Owner-controlled health-related
state used by that Hospital Friend. It is distinct from the Hospital’s
institutional clinical record. Another Hospital Friend, Pharmacy Friend,
or Healthcare AI Friend does not automatically receive access to it.

# 74. Commerce Example

A Retailer Friend Folder may contain Owner-controlled state such as:
preferences sizes wish information delivery preferences Owner-held
purchase information service settings Merchant transaction records may
remain independent Service Records. A Payment Friend or Delivery Friend
has its own Friend relationship.

# 75. Friend Folder Requirements

A conforming implementation MUST satisfy: \### FF-001 — One Friend, One
Friend Folder Each continuing Friend relationship MUST resolve to its
associated Friend Folder. \### FF-002 — Owner Ownership Friend Folder
Persistent State MUST remain Owner-controlled M-PIN state. \### FF-003 —
Verified Binding Friend Folder access MUST depend on the correct Friend
identity/binding. \### FF-004 — First Creation Authorization A missing
Friend Folder MUST NOT be created without required Owner authorization.
\### FF-005 — Existing Folder Reuse A returning Friend MUST resolve the
existing Folder for the same continuing relationship. \### FF-006 —
Friend Folder Isolation A Friend MUST NOT receive default access to
another Friend’s Folder. \### FF-007 — No Arbitrary Folder Selection A
Friend MUST NOT bypass binding by selecting an unrelated Folder. \###
FF-008 — Friend Semantic Authority The Friend remains responsible for
interpretation of its service-specific payload. \### FF-009 — M-PIN
Semantic Neutrality M-PIN MUST NOT require complete semantic
interpretation of the Friend payload to preserve the M-PIN boundary.
\### FF-010 — Owner-Controlled Persistence Runtime changes MUST NOT
become Friend Folder Persistent State without the applicable Owner Save
and Commit. \### FF-011 — Current-State-Only The Friend Folder has one
authoritative current committed state for the applicable scope; Core
does not require M-PIN version history. \### FF-012 — Native Friend
Management Service-specific data modification SHOULD normally occur
through the corresponding Friend’s native service behavior. \### FF-013
— Service Record Separation Independent legitimate Friend Service
Records MUST remain distinguishable from Friend Folder state. \###
FF-014 — Anti-Loophole Service Record classification MUST NOT be used to
bypass Friend Folder boundaries. \### FF-015 — Portability M-PIN
migration SHOULD preserve Friend Folder bindings and valid Current
State.

# 76. Decision 120 Boundary

For avoidance of doubt, FF-008 and FF-009 do not define the exact
physical Friend Folder schema. M-PIN v2.0 freezes only the
responsibility boundary: Friend owns semantic interpretation and
service-specific payload design

M-PIN owns minimum boundary requirements necessary for identity,
binding, integrity, authorization, and persistence The following remain
deferred: exact .MPIN container exact Friend Folder serialization exact
Envelope schema exact payload encoding

# 77. Canonical First Synchronization

OWNER │ ▼ Initiate Sync │ ▼ Establish Owner Authority │ ▼ Verify Friend
Identity │ ▼ Resolve Friend Folder │ ├── EXISTS │ │ │ └─────────────┐ │
│ └── ABSENT │ │ │ ▼ │ Owner Approval │ │ │ ▼ │ Create Folder │ │ │ ▼ │
Bind Friend │ │ │ └─────────────┘ │ ▼ Open Session │ ▼ Load Current
State │ ▼ Friend Runtime │ ▼ Friend Native UX

# 78. Canonical Returning Synchronization

Verified Friend │ ▼ Resolve existing binding │ ▼ Friend Folder │ ▼
Current State │ ▼ Synchronization Session │ ▼ Friend Runtime

# 79. Canonical Persistence

Friend Folder Current State A │ ▼ Friend Runtime │ ▼ Runtime State B │ │
Owner SAVE ▼ M-PIN Validation │ ▼ Atomic Commit │ ▼ Friend Folder
Current State B Without Save: Runtime State B │ │ Session ends ▼ not
committed to M-PIN

Friend Folder Current State A remains

# 80. Canonical Isolation

                    M-PIN
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
     Folder A      Folder B      Folder C
        │             │             │
        ▼             ▼             ▼
     Friend A      Friend B      Friend C

Friend A ──X──► Folder B Friend A ──X──► Folder C Friend B ──X──► Folder
A

# 81. Model Invariants

The Friend & Friend Folder model is governed by these invariants: \##
One Friend, One Friend Folder. \## The Friend Folder belongs to the
Owner’s M-PIN continuity. \## The Friend understands its payload; M-PIN
preserves the boundary. \## Common storage does not create common Friend
visibility. \## A first Folder requires Owner approval. \## A returning
Friend reuses its existing Folder. \## Runtime State is not Persistent
State. \## No Owner Save means no M-PIN persistence of unsaved Runtime
changes. \## Friend evolution does not inherently require a new Folder.
\## A different Friend does not automatically inherit another Friend’s
Folder. \## Service Records do not create a loophole around M-PIN
ownership.

# 82. Friend Folder Thesis

The complete model can be reduced to: Owner │ ▼ M-PIN │ ▼ Friend Folder
│ │ authorized synchronization ▼ Friend │ ▼ Runtime / Native UX The
Owner owns the persistent M-PIN state. The Friend understands and
operates its service-specific data. M-PIN preserves the ownership,
isolation, and persistence boundary between them.

## M-PIN v2.0 — Core 06 / Friend & Friend Folder Model

## Status: FROZEN
