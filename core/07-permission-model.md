# M-PIN v2.0

## Core 07 — Permission Model

**Status:** FROZEN **Version:** 2.0 **Document Type:** Normative Core
Specification

------------------------------------------------------------------------

# 1. Purpose

This document defines the permission and authorization model of M-PIN
v2.0.

It specifies:

- how Owner Authority relates to Permission;
- how Friend access is scoped;
- how Friend Folder access is authorized;
- the distinction between authentication and authorization;
- the distinction between Read authority and Save authority;
- how permissions relate to Synchronization Sessions;
- how revocation affects active M-PIN authority;
- how Provider and Device roles are constrained;
- how permission failure is handled.

M-PIN permissions are designed to preserve Owner authority without
taking control of Friend internal operation.

------------------------------------------------------------------------

# 2. Permission Thesis

The canonical M-PIN rule is:

> **Service need does not create authority.**

A Friend may need data to provide a service.

That need does not itself authorize M-PIN access.

Conceptually:

``` text
Friend request
      ≠
Permission
M-PIN access requires the applicable Owner-authorized relationship and valid protocol context.
```

# 3. Permission

A Permission is an Owner-authorized allowance for a defined M-PIN
operation or scope. A Permission may constrain: Friend Friend Folder
operation Synchronization Session validity period persistence authority
other required scope Permission MUST NOT be interpreted as unrestricted
ownership transfer.

# 4. Owner Authority

Owner Authority is the source of authorization for Owner-controlled
M-PIN operations. Conceptually: Owner │ ▼ Owner Authority │ ▼ Permission
│ ▼ authorized M-PIN operation A Friend MUST NOT manufacture Owner
Authority. A Provider MUST NOT manufacture Owner Authority merely
because it controls infrastructure.

# 5. Authentication, Authorization, and Permission

M-PIN distinguishes: Authentication ↓ Who or what is this?

Authorization ↓ May this principal perform this operation?

Permission ↓ What M-PIN authority has been granted for this scope?
Therefore: authenticated ≠ authorized for everything and: authorized for
one operation ≠ authorized for every operation

# 6. Ownership Is Not a Session Permission

Owner status and active Permission are related but distinct. The Owner
may possess architectural ownership authority while no Friend currently
has active synchronization authority. Conceptually: Owner exists │ └──
no active Friend Session is a valid M-PIN state. Ownership does not
require permanent Friend access.

# 7. Friend-Specific Permission

Permission granted to Friend A MUST NOT automatically extend to Friend
B. Permission A │ ▼ Friend A

Permission A ──X──► Friend B This remains true even if: both Friends
belong to the same company; both run on the same Device; both use the
same Provider; both participate in the same workflow.

# 8. Friend Folder Scope

A Friend’s M-PIN permission MUST be scoped to the Friend Folder
associated with that Friend. Canonical relationship: Verified Friend A │
▼ Permission │ ▼ Friend Folder A Not: Friend A │ └── all Friend Folders

# 9. Friend Folder Isolation

Permission MUST preserve Friend Folder Isolation. A valid Permission for
Friend Folder A MUST NOT imply: read Folder B write Folder B enumerate
Folder B modify Folder B delete Folder B unless another explicit Core or
future interoperability rule authorizes the specific operation. M-PIN
v2.0 defines no general cross-Friend Folder permission.

# 10. Permission Does Not Follow Corporate Ownership

If one company operates multiple distinct Friends, Permission remains
Friend-specific. Example: Company X

├── Friend A → Permission A → Folder A └── Friend B → Permission B →
Folder B Corporate ownership MUST NOT collapse those permissions into
one universal company permission.

# 11. Permission Does Not Follow Physical Device

Multiple Friends on one Device remain separately authorized. Device ├──
Friend A → Folder A └── Friend B → Folder B Physical co-location does
not grant cross-Friend authority.

# 12. Permission Does Not Follow Provider

A Provider may host M-PIN infrastructure for multiple Friend
relationships. That role MUST NOT automatically grant the Provider
Friend permissions. Conceptually: Provider infrastructure access ≠
Friend Folder authority Any Provider capability MUST be separately
justified by its defined infrastructure role and security model.

# 13. Permission and Synchronization Session

Friend access to M-PIN occurs through a bounded Synchronization Session.
Conceptually: Owner-authorized Permission + verified Friend + valid
Session ↓ bounded Friend Folder access A Friend MUST NOT treat a
previous authorization as permanent hidden M-PIN access after the
applicable Session authority has ended.

# 14. Session-Scoped Authority

The active Synchronization Session defines the operational context in
which the Friend exercises M-PIN authority. A Session may contain
authority for operations such as: Load Runtime use of loaded state Save
request handling Commit participation according to the applicable
permission model. The exact Session credential representation is
deferred.

# 15. One Active Friend

The permission model preserves the v2.0 invariant: \## One M-PIN, One
Active Friend, One Synchronization Session. M-PIN MUST NOT
simultaneously grant active synchronization authority to multiple
Friends within the same authoritative active continuity. This rule
concerns M-PIN synchronization authority. It does not require unrelated
Friend service processes to stop running.

# 16. Initial Synchronization Permission

When a Friend connects for the first time, the following are distinct
authorization steps: Owner authorizes synchronization ↓ Friend Identity
verified ↓ Friend Folder lookup ↓ Folder absent ↓ Owner authorizes
Folder creation Authorization to attempt synchronization MUST NOT
automatically be treated as authorization to create arbitrary persistent
Friend Folders.

# 17. Friend Folder Creation Permission

Creation of a new Friend Folder requires applicable Owner authorization.
If authorization is denied: Folder absent ↓ creation denied ↓ no Folder
↓ no M-PIN synchronization relationship The Friend MAY continue
independently outside M-PIN according to its own service behavior.

# 18. Returning Friend Permission

A returning Friend does not require creation of another Friend Folder.
Instead: Friend Identity verified ↓ existing binding resolved ↓ Session
authority established ↓ existing Folder used Permission MUST apply to
the existing valid binding.

# 19. Load Authority

Load Authority permits the current authorized Friend Folder state to be
made available to the corresponding Friend Runtime within the active
Session. Conceptually: Permission ↓ Friend Folder A ↓ LOAD Friend A
Runtime Load Authority MUST NOT expose unrelated Friend Folders.

# 20. Read Once

M-PIN preserves the v1 Read Once principle. The Friend obtains the
relevant saved state when the authorized Synchronization Session is
established. Read Once does not mean: one byte read one API call one
Runtime operation It means the Friend does not gain unrestricted
perpetual background access to M-PIN merely because it was once
synchronized.

# 21. Loaded Runtime State

Once valid state has been loaded, the Friend may use it during its
authorized Runtime. The Friend does not require a new M-PIN permission
for every internal computation over the already authorized loaded state.
Conceptually: authorized LOAD ↓ Friend Runtime ↓ Friend internal
processing M-PIN does not control every internal Friend computation.

# 22. Read Authority Is Not Save Authority

One of the central permission distinctions is: \## Read Authority ≠ Save
Authority A Friend’s authority to load its current Friend Folder state
MUST NOT automatically permit it to Commit arbitrary new Persistent
State. Conceptually: LOAD allowed ≠ COMMIT allowed Persistence requires
the Owner-controlled Save boundary.

# 23. Save Authority

Save Authority is the Owner-authorized persistence intent applicable to
the current Friend relationship and Session. Canonical flow: Friend
Runtime State’ ↓ Owner SAVE ↓ Save Authority established ↓ M-PIN
validation ↓ Commit The Friend cannot create Save Authority merely by
generating new Runtime State.

# 24. Save Is Not Friend Write Permission

M-PIN Save MUST NOT be reduced to a generic permanent Friend write
credential. The intended model is not: Owner authorizes Friend once ↓
Friend may persist anything forever The intended model is: bounded
Session + Owner persistence intent + valid Friend/Folder binding ↓
authorized persistence operation

# 25. Friend Internal Save Is Not M-PIN Save

A Friend may use terms such as: save; autosave; draft; sync; store.
Those Friend-internal actions do not automatically have the normative
meaning of M-PIN SAVE. Conceptually: Friend internal autosave ≠ M-PIN
Owner SAVE Only the M-PIN persistence boundary defined by the Core
determines M-PIN Save authority.

# 26. Commit Authority

A Commit may proceed only after the applicable M-PIN persistence
conditions are satisfied. These include, as applicable: valid Owner Save
authority valid active Session correct Friend Identity correct Friend
Folder binding required structural validity required integrity Failure
of a required condition MUST prevent acceptance of the proposed new
Current State.

# 27. Save Target

The semantic target of Save is the current persistent state of the
active Friend’s own Friend Folder. Conceptually: Friend A Runtime ↓
Owner SAVE ↓ Friend Folder A not: Friend A Runtime ↓ Owner SAVE ↓
arbitrary Folder B

# 28. Save Representation

Permission semantics do not require one transport representation. A
conforming implementation MAY persist through: full-state representation
delta transaction chunked update other conforming mechanism The
permission requirement is that the resulting Commit be authorized and
establish the correct new Current State.

# 29. Multiple Saves

A Session MAY contain multiple Owner Saves. Each successful persistence
transition MUST satisfy the applicable Save/Commit authority. Example:
State A ↓ Save ↓ State B ↓ Save ↓ State C The existence of an earlier
Save MUST NOT automatically authorize unrelated future persistence
outside the valid Session and permission context.

# 30. No Save

If the Owner does not authorize Save: Runtime State’ ↓ Session ends ↓ no
M-PIN Commit The previous Friend Folder Current State remains
authoritative. A Friend MUST NOT infer Save permission from Session
termination.

# 31. Disconnect Is Not Save

An abnormal disconnect MUST NOT be interpreted as persistence
authorization. Conceptually: disconnect ≠ Owner SAVE Unsaved Runtime
State remains uncommitted relative to M-PIN.

# 32. Timeout Is Not Save

Session timeout or expiration MUST NOT create Save Authority. Session
expires ↓ authority ends not: Session expires ↓ automatically persist
Runtime

# 33. Permission Expiration

A Permission MAY have a bounded validity period or be bounded by the
Synchronization Session. When the applicable authority expires, the
Friend MUST NOT continue exercising that expired M-PIN authority. The
exact expiration mechanism is implementation-defined.

# 34. Revocation

The Owner MAY revoke M-PIN authority according to the applicable
permission and lifecycle rules. Revocation MUST invalidate the affected
M-PIN authority. Conceptually: active M-PIN authority ↓ Owner revocation
↓ authority invalid A revoked Friend MUST NOT continue using the revoked
M-PIN access channel.

# 35. Revocation and Runtime

Revocation of M-PIN authority does not necessarily terminate the
Friend’s entire independent Runtime. Conceptually: revoke M-PIN access ↓
M-PIN Session authority ends but the Friend may have independent service
behavior outside M-PIN. This preserves Friend Sovereignty.

# 36. Revocation and Loaded Plaintext

If a Friend has already legitimately received plaintext into its
Runtime, revocation cannot guarantee retroactive erasure from a
malicious or compromised Friend. M-PIN MUST NOT claim otherwise.
Revocation controls continued M-PIN authority. It does not provide
impossible retroactive control over every internal copy in an authorized
external Runtime.

# 37. Revocation and Friend Folder

Revoking Friend access does not inherently delete the Friend Folder.
These are distinct operations: revoke authority ≠ delete persistent
state The Friend Folder may remain in M-PIN for later reauthorization,
migration, recovery, or deletion according to applicable lifecycle
rules.

# 38. Revocation and Friend Account

Revoking M-PIN permission does not automatically delete the Friend’s
service account. Likewise, closing a Friend Account does not
automatically define deletion of the M-PIN Friend Folder. The two
systems retain separate lifecycle responsibilities.

# 39. Revocation and Service Records

Revocation of M-PIN access does not automatically delete independent
Friend Service Records. For example, it does not inherently erase:
clinical records; completed transaction records; invoices; regulatory
records; safety records. Service Record lifecycle remains separate.

# 40. Permission Minimization

M-PIN SHOULD authorize only the scope required for the intended M-PIN
operation. Conceptually: required: Friend A → Folder A → active Session

not required: Friend A → every Folder → permanent access This principle
reduces unnecessary exposure.

# 41. Zero Visibility

A Friend has no default visibility into unrelated M-PIN state. A
Permission SHOULD NOT reveal: unrelated Friend Folder names; unrelated
Folder identifiers; unrelated metadata; unrelated payload; unrelated
Session information merely because the Friend has one valid M-PIN
relationship.

# 42. Permission and Folder Discovery

Friend Folder discovery SHOULD resolve the active Friend’s own Folder
from the verified Friend relationship. The Friend SHOULD NOT need
permission to enumerate every Folder merely to find its own.
Conceptually: verified Friend A ↓ resolve Folder A not: Friend A ↓ list
all M-PIN Folders ↓ choose one

# 43. Permission and Payload Semantics

M-PIN Permission governs access to the Friend Folder boundary. It does
not require M-PIN to understand the semantic meaning of every field in
the Friend payload. Conceptually: M-PIN authorizes: access boundary

Friend interprets: payload semantics This preserves semantic neutrality.

# 44. Permission and Service Records

A Friend’s legitimate authority to maintain Service Records does not
create unrestricted M-PIN Permission. For example: Hospital authority to
maintain clinical record ≠ authority to read all M-PIN Friend Folders
and: Merchant obligation to maintain transaction record ≠ authority to
copy entire Commerce Friend Folder

# 45. Provider Permission

A Provider MAY require bounded permissions to perform infrastructure
functions. Examples may include: storing encrypted state; transporting
protocol objects; validating infrastructure metadata; assisting
migration; participating in recovery. Such Provider permissions MUST be
limited to the Provider role. They MUST NOT silently become Friend
permissions or unrestricted Owner Authority.

# 46. Provider Plaintext

The Permission Model does not assume that every Provider implementation
is zero-knowledge. Whether a Provider can access plaintext depends on
the implementation’s key and trust architecture. Therefore: Provider
participates ≠ Provider necessarily sees plaintext

Provider participates ≠ Provider necessarily cannot see plaintext The
exact security property must be established by the implementation.

# 47. Provider Administrator

Provider administrative privileges MUST NOT automatically authorize:
Owner SAVE Friend Folder reassignment cross-Friend access M-PIN identity
replacement unrestricted recovery Any such capability requires an
explicitly defined and authorized role.

# 48. Device Permission

A Device MAY be authorized to participate in M-PIN access. Device
authorization MUST NOT automatically grant every application or Friend
on that Device access to M-PIN. Conceptually: authorized Device ≠ all
software on Device authorized Friend Identity and Friend Folder
permissions remain applicable.

# 49. Device Loss

Loss or theft of a Device MUST NOT be treated as voluntary transfer of
Owner Authority. Possession alone is insufficient. Applicable
authentication, revocation, and recovery controls remain required.

# 50. New Device

A new Device MAY participate in the same M-PIN continuity after the
applicable Owner authority, migration, or recovery process succeeds. The
new Device does not require a new M-PIN merely because it is physically
different.

# 51. Cross-Friend Data Need

A Friend’s legitimate need for information held in another Friend
relationship does not create direct Folder access. Conceptually: Friend
B needs information from Friend A relationship ↓ need exists ≠ Folder A
permission This is a central consequence of Friend Folder Isolation.

# 52. Owner-Mediated Disclosure

Healthcare and Commerce validation identified a possible future
mechanism for selected cross-Friend information transfer. Conceptually:
Friend A │ selected data ▼ Owner authorization │ ▼ Disclosure │ ▼ Friend
B For M-PIN v2.0: Owner-Mediated Disclosure = CANDIDATE DEFERRED FROM
CORE It is not a required Permission Model operation.

# 53. Disclosure Is Not Folder Permission

A future Disclosure MUST NOT be interpreted as granting the recipient
Friend direct permission to the source Friend Folder. The distinction
is: selected authorized data transfer ≠ source Folder access The exact
Disclosure authorization model remains deferred.

# 54. Recipient Persistence

If a future Disclosure mechanism allows a recipient Friend to receive
selected information, receipt alone SHOULD NOT automatically redefine
that information as committed recipient M-PIN Persistent State. Any
persistence into the recipient Friend’s own Friend Folder would remain
subject to the recipient relationship’s applicable M-PIN persistence
rules. This is a compatibility constraint for future Disclosure design,
not a mandatory v2.0 Disclosure protocol.

# 55. Permission Delegation

M-PIN v2.0 does not define unrestricted permission delegation from one
Friend to another. Friend A MUST NOT grant Friend B access to M-PIN
merely because Friend A has access. Conceptually: Owner → Friend A
permission

does not imply

Friend A → Friend B permission Owner authority remains central.

# 56. Internal Agents

An internal agent, subprocess, model, plugin, or tool operating inside a
Friend does not automatically receive greater M-PIN authority than the
Friend. Conceptually: Friend authority ↓ internal agent

agent authority ≤ applicable Friend authority If an internal actor is
modeled as a separate Friend, it requires its own M-PIN relationship.

# 57. Tool Authorization

Authorization for an AI Friend to use its Friend Folder does not
automatically authorize every external tool the AI invokes to receive
that Folder data. Tool access may require separate Friend-side or
Profile-specific authorization. M-PIN Friend Permission MUST NOT be
represented as universal third-party data-sharing consent.

# 58. Legal and Institutional Authority

M-PIN Owner Permission MUST NOT automatically be represented as
equivalent to every external legal or institutional authorization.
Examples include: M-PIN authorization ≠ medical consent

M-PIN authorization ≠ payment authorization

M-PIN authorization ≠ merchant contractual consent

M-PIN authorization ≠ government identity verification unless an
explicit integration establishes the relationship.

# 59. Permission and Transactions

A Friend may execute an external transaction independently of M-PIN
Save. For example: purchase confirmed ≠ M-PIN SAVE and: M-PIN SAVE ≠
payment authorization The Commerce Profile defines this distinction
further.

# 60. Permission and Physical Action

In Robotics: physical action authorization ≠ M-PIN SAVE and: M-PIN
Session termination ≠ automatic physical emergency stop unless the robot
system explicitly defines that behavior independently. M-PIN is not the
robot’s universal safety-control bus.

# 61. Permission and Healthcare Action

In Healthcare, M-PIN Permission to load Owner-controlled state does not
automatically authorize: diagnosis; treatment; prescription; clinical
record modification. Those authorities remain governed by the relevant
healthcare system and Profile.

# 62. Permission Request

A Friend MAY request that the Owner authorize an M-PIN operation. A
request MUST remain distinguishable from approval. Conceptually: Friend
requests Save ↓ Owner decides ↓ approved / denied The Friend MUST NOT
treat presentation of a request as authorization.

# 63. Owner Denial

If the Owner denies a requested M-PIN operation, the operation MUST NOT
proceed under that denied authority. The Friend MAY continue its own
independent service behavior where applicable. M-PIN denial does not
require M-PIN to terminate the entire Friend service unless the Session
or security rules require termination.

# 64. Permission UI

M-PIN v2.0 does not mandate one universal permission UI. An
implementation MAY use: dialog; button; device interaction; secure
confirmation; another interface. The observable authorization semantics
MUST remain conformant. A UI MUST NOT falsely represent a denied or
absent permission as granted.

# 65. Save UI

The exact Save interface is not fixed. However, the implementation MUST
preserve the semantic distinction between: Owner persistence intent and:
Friend internal background persistence The Owner must have a meaningful
way to exercise the persistence decision defined by M-PIN.

# 66. Permission Persistence

M-PIN v2.0 does not require all permissions to be stored forever. Some
permissions may be: Session-scoped operation-scoped time-scoped
persistent configuration depending on the operation. Persistent
permission configuration MUST NOT create hidden perpetual active Session
authority.

# 67. Standing Relationship vs Active Authority

A Friend may have an established M-PIN relationship and existing Friend
Folder while no active Session exists. Conceptually: Friend relationship
exists Friend Folder exists

but

active M-PIN authority = none This distinction is normative.

# 68. Permission State and Friend Folder State

Permission metadata and Friend payload are different categories.
Conceptually: M-PIN Permission State ≠ Friend Payload State An
implementation MAY store permission-related metadata outside the Friend
payload. The Friend MUST NOT be able to rewrite its own authorization
simply by modifying payload content.

# 69. Authorization Integrity

Security-relevant Permission and authorization state MUST be protected
against unauthorized modification. A Friend MUST NOT be able to change:
DENY → ALLOW read-only authority → Save authority Folder A scope →
Folder B scope expired Session → active Session by altering untrusted
payload or local metadata.

# 70. Replay Protection

Previously valid authorization material MUST NOT be reusable outside its
legitimate validity context where doing so would recreate unauthorized
authority. A conforming implementation MUST address replay of relevant:
Session authority Save authorization migration authorization recovery
authorization The exact nonce, counter, timestamp, generation, or token
mechanism is deferred.

# 71. Fail Closed

If M-PIN cannot establish a required authorization condition, the
affected operation MUST fail closed. Examples: Friend Identity uncertain
→ deny

Folder binding uncertain → deny

Session invalid → deny

Save authority absent → no Commit

integrity validation fails → reject affected operation Failure MUST NOT
broaden Permission.

# 72. Permission Logging

An implementation MAY maintain security-relevant audit information
necessary to diagnose or prove permission events. Such logging SHOULD be
minimized to what is necessary for its purpose. Logging MUST NOT become
an excuse to create a hidden full copy of Friend Folder payloads. The
exact audit format is deferred.

# 73. Privacy of Permission Metadata

Permission metadata itself may reveal sensitive relationship
information. For example, knowledge that an Owner has a relationship
with: Hospital Friend Pharmacy Friend specific AI Friend specific
retailer may be privacy-relevant. Implementations SHOULD minimize
unnecessary exposure of such metadata.

# 74. Permission and Portability

When M-PIN migrates between compatible environments, the migration
SHOULD preserve valid permission relationships necessary for continuity
where appropriate. However, stale or environment-specific active Session
authority MUST NOT simply be copied and treated as active at the
destination. Conceptually: relationship configuration may migrate

active Session authority must be re-established

# 75. Permission and Recovery

Recovery SHOULD restore legitimate Owner control over permission
configuration where recoverable. Recovery MUST NOT automatically
reactivate every previously active or revoked Session. Revoked authority
MUST NOT silently become valid merely because an older Backup was
restored. Implementations therefore require an appropriate
freshness/revocation strategy. The exact mechanism is deferred.

# 76. Backup and Permission

A Backup MAY contain permission-related configuration required for
recovery. A Backup MUST NOT be treated as an independently active
authorization source merely because it contains old permission data.
Freshness and current authority remain relevant.

# 77. Malicious Friend

A malicious or compromised Friend may attempt to: request excessive
access; impersonate another Friend; access another Folder; forge Save
authority; replay a Session; retain loaded plaintext; misclassify data
as Service Records. The Permission Model MUST deny authority beyond the
valid Friend relationship. It cannot guarantee deletion of plaintext
already legitimately delivered to a malicious Runtime.

# 78. Malicious Provider

A malicious or compromised Provider may attempt to: alter permission
metadata; forge Owner authorization; rebind Friend Folders; reactivate
revoked authority; redirect migration. The architecture MUST NOT treat
Provider administrative control as proof of legitimate Owner
authorization. Concrete mitigation depends on the implementation’s trust
and key model.

# 79. Malicious Device

A compromised Device may attempt to exercise cached or stolen M-PIN
authority. A conforming implementation SHOULD limit the impact through
applicable: authentication; Session boundaries; revocation; freshness;
integrity; recovery controls. M-PIN v2.0 does not claim perfect
protection after complete compromise of an authorized endpoint.

# 80. Permission Requirements

A conforming implementation MUST satisfy the following requirements.
\### PERM-001 — Owner Authority M-PIN operations requiring Owner
authorization MUST NOT proceed without valid Owner Authority. \###
PERM-002 — Friend-Specific Scope Permission granted to one Friend MUST
NOT automatically extend to another Friend. \### PERM-003 — Friend
Folder Scope Friend access MUST remain scoped to its associated Friend
Folder. \### PERM-004 — No Cross-Friend Default A Friend MUST NOT
receive default access to another Friend’s Folder. \### PERM-005 —
Authentication Separation Authentication MUST NOT automatically imply
unrestricted authorization. \### PERM-006 — Read/Save Separation
Authority to Load Friend Folder state MUST NOT automatically grant Save
or Commit authority. \### PERM-007 — Owner-Controlled Save M-PIN
persistence MUST require the applicable Owner Save authority. \###
PERM-008 — Session Boundary Active Friend access MUST occur within a
valid bounded Synchronization Session. \### PERM-009 — One Active Friend
Only one Friend may hold active M-PIN synchronization authority at a
time within one authoritative active continuity. \### PERM-010 —
Revocation Revoked M-PIN authority MUST NOT remain usable as valid
active authority. \### PERM-011 — No Delegation by Friend A Friend MUST
NOT independently grant its M-PIN authority to another Friend. \###
PERM-012 — Provider Separation Provider infrastructure authority MUST
NOT automatically equal Owner or Friend authority. \### PERM-013 —
Device Separation Device authorization MUST NOT automatically authorize
every Friend or application on that Device. \### PERM-014 — Replay
Resistance Security-relevant authorization material MUST NOT be accepted
outside its legitimate validity context. \### PERM-015 — Fail Closed
Failure to establish required authorization MUST deny the affected M-PIN
operation.

# 81. Recommended Permission Properties

A conforming implementation SHOULD additionally preserve: \### PERM-016
— Minimum Scope Permissions SHOULD expose no more M-PIN authority than
necessary. \### PERM-017 — Discovery Privacy Friend Folder resolution
SHOULD avoid exposing unrelated Friend relationships. \### PERM-018 —
Permission Metadata Privacy Permission metadata SHOULD be protected from
unnecessary disclosure. \### PERM-019 — Explicit Denial Denied Owner
authorization SHOULD result in a clear non-authorized state rather than
ambiguous partial authority. \### PERM-020 — Migration Freshness
Migration SHOULD preserve valid relationships without copying stale
active Session authority as current authority.

# 82. Canonical Permission Flow

OWNER │ ▼ Owner Authority │ ▼ Permission │ ├── Friend scope ├── Friend
Folder scope ├── operation scope └── Session scope │ ▼ Verified Friend │
▼ Synchronization Session │ ▼ Friend Folder │ ▼ LOAD │ ▼ Friend Runtime
Persistence adds a separate Owner decision: Friend Runtime State’ │ ▼
Owner SAVE │ ▼ Save Authority │ ▼ Validation │ ▼ Atomic Commit

# 83. Canonical Denial Flow

Friend requests operation │ ▼ Check identity / binding / permission /
Session │ ├── valid │ ↓ │ proceed within scope │ └── invalid / absent ↓
DENY The denied path MUST NOT silently expand into alternate authority.

# 84. Canonical Revocation Flow

Active Friend Session │ ▼ Owner revokes relevant authority │ ▼ M-PIN
authority invalidated │ ▼ Friend loses continued M-PIN access under that
authority Already committed Persistent State remains governed by its own
lifecycle. Already disclosed plaintext cannot be guaranteed to disappear
from a malicious external Runtime.

# 85. Canonical Permission Boundaries

Owner Permission ≠ Friend request

Authentication ≠ Authorization

Read Authority ≠ Save Authority

Friend Permission ≠ Provider Permission

Device Permission ≠ Friend Permission

M-PIN Save ≠ Friend autosave

M-PIN Permission ≠ medical consent

M-PIN Permission ≠ payment authorization

Disclosure ≠ cross-Friend Folder access

# 86. Permission Invariants

The Permission Model is governed by these invariants: \## The Owner
remains the source of Owner-controlled M-PIN authority. \## A Friend
receives only bounded authority for its own relationship. \## A Friend’s
need for data does not create permission. \## Authentication does not
equal unrestricted authorization. \## Read authority does not equal Save
authority. \## Runtime modification does not create persistence
authority. \## A Friend cannot delegate its M-PIN authority to another
Friend. \## Provider administration does not equal ownership. \##
Revocation ends the affected M-PIN authority, not necessarily the
Friend’s entire service. \## Permission failure fails closed.

# 87. Permission Thesis

The complete M-PIN permission model can be reduced to: Owner │ │ grants
bounded authority ▼ M-PIN │ │ verifies scope ▼ Friend │ │ accesses only
its relationship ▼ Friend Folder and for persistence: Runtime change │ ▼
Owner SAVE │ ▼ authorized Commit │ ▼ new Current State The Friend may
provide the service. The Friend may request access. The Friend may
process authorized data. But: \## the Friend’s service need never
becomes Owner authority by itself.

## M-PIN v2.0 — Core 07 / Permission Model

## Status: FROZEN
