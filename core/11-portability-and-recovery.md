# M-PIN v2.0

## Core 11 — Portability & Recovery

**Status:** FROZEN **Version:** 2.0 **Document Type:** Normative Core
Specification

------------------------------------------------------------------------

# 1. Purpose

This document defines the Portability, Migration, Backup, and Recovery
model of M-PIN v2.0.

It specifies:

- Device Independence;
- Storage Independence;
- Provider Independence;
- M-PIN continuity;
- portability;
- migration;
- authoritative active continuity;
- Backup;
- Authority Recovery;
- Data Recovery;
- recovery integrity;
- migration integrity;
- Provider failure;
- offline clone limitations;
- portability security boundaries.

The purpose is to ensure that Owner-controlled persistent continuity is
not architecturally owned by one Device, Storage location, Friend, or
optional M-PIN Service Provider.

------------------------------------------------------------------------

# 2. Continuity Thesis

The canonical M-PIN continuity rule is:

> **Service may change. Device may change. Provider may change. Owner
> continuity remains.**

Conceptually:

Device A │ Provider A │ Storage A │ ▼ M-PIN X │ ▼ Owner continuity

may become:

Device B │ Provider B │ Storage B │ ▼ M-PIN X │ ▼ same Owner continuity

provided that the applicable migration, identity, authority, integrity,
and recovery requirements are satisfied.

------------------------------------------------------------------------

# 3. M-PIN Continuity

**M-PIN Continuity** is the preservation of the logical M-PIN
relationship across legitimate changes in implementation environment.

Continuity includes, as applicable:

- M-PIN Identity;
- Owner Authority;
- Friend Folder relationships;
- Friend Folder bindings;
- valid Current State;
- required permission configuration;
- required integrity state.

Continuity is not defined by one physical file path or one server.

------------------------------------------------------------------------

# 4. M-PIN Identity and Location

M-PIN Identity MUST remain conceptually distinct from its Storage
location.

Therefore:

M-PIN X on Storage A

may remain:

M-PIN X on Storage B

after a valid migration.

Changing location does not inherently create a new M-PIN.

------------------------------------------------------------------------

# 5. Device Independence

M-PIN MUST NOT be architecturally bound to one permanent Device.

Valid continuity MAY move between:

- PC;
- mobile Device;
- removable storage host;
- robot;
- shared terminal;
- future compatible Device.

A Device is an execution or access environment.

It is not the Owner.

------------------------------------------------------------------------

# 6. Device Change

A valid Device transition may preserve:

same M-PIN Identity same Owner continuity same Friend Folder
relationships same valid Current State

The new Device MUST establish the authority required to use that
continuity.

Physical possession of the new Device alone is insufficient.

------------------------------------------------------------------------

# 7. Storage Independence

M-PIN Persistent State MAY reside in different compatible Storage
environments.

Examples include:

- local storage;
- removable storage;
- Owner-controlled cloud storage;
- Provider-hosted storage;
- another conforming storage environment.

The architecture does not require cloud storage.

------------------------------------------------------------------------

# 8. Local Storage Is Valid

A local-only M-PIN deployment is valid if it satisfies the Core
requirements.

Conceptually:

Owner │ ▼ Local Device │ ▼ M-PIN does not require: mandatory Provider
cloud Provider participation is optional.

# 9. Removable Storage Is Valid

An M-PIN MAY be stored on removable media. Historical examples included
USB storage. The normative principle is Storage Independence rather than
dependence on one removable-media technology. A removable medium may
hold M-PIN state without becoming the Owner.

# 10. Cloud Storage Is Valid

M-PIN MAY use cloud storage. Cloud use does not inherently mean: the
cloud provider owns the M-PIN; the cloud provider becomes the Owner; the
cloud provider becomes a Friend; all Friend Folders become visible to
the cloud operator. Actual confidentiality depends on the
implementation’s key and trust model.

# 11. Provider Independence

Where an M-PIN Service Provider is used: \## M-PIN MUST NOT be
architecturally owned by that Provider. Provider A may implement M-PIN
services. Provider B may independently implement compatible M-PIN
services. A conforming architecture SHOULD preserve an Owner-authorized
path from one compatible Provider environment to another.

# 12. Provider Is Optional

The canonical architecture is not: Owner ↓ mandatory Provider ↓ M-PIN ↓
Friend The architecture may instead be: Owner ↓ local M-PIN ↓ Friend or:
Owner ↓ M-PIN via Provider ↓ Friend Provider is an
implementation/deployment role, not a mandatory Core hop.

# 13. Provider Administration Is Not Ownership

Provider administrative capability MUST NOT automatically equal: Owner
Authority; Friend authority; Save authority; recovery ownership;
permission to rebind Friend Folders; permission to transfer M-PIN
ownership. Infrastructure control and architectural ownership remain
distinct.

# 14. Portability

Portability is the ability to preserve M-PIN continuity across
compatible environments without changing the architectural Owner merely
because the implementation environment changes. Portability may apply
across: Devices; Storage; Providers. Portability does not mean
unrestricted plaintext copying.

# 15. Portability Requirements

A portable M-PIN continuity MUST preserve, as applicable: M-PIN
Identity; Friend Folder identities or equivalent stable bindings;
Friend-to-Folder associations; Current State; required permission state;
integrity; sufficient freshness; Owner-controlled authority. A portable
representation MUST NOT silently convert the destination Provider or
Device into the Owner.

# 16. Portability Is Not Friend Migration

Moving M-PIN from Provider A to Provider B is not the same as replacing
Friend A with Friend B. Conceptually: Provider A ↓ M-PIN X ↓ Friend A
to: Provider B ↓ same M-PIN X ↓ same Friend A is Provider migration. It
does not imply: Friend A → Friend B

# 17. Friend Change

A different Friend normally has a different Friend Folder relationship.
Therefore: Friend A Folder ≠ Friend B Folder Changing services does not
automatically transfer Friend A’s payload semantics or Folder to Friend
B.

# 18. Portability Is Not Semantic Translation

M-PIN portability preserves M-PIN state and relationships. It does not
require M-PIN to translate arbitrary Friend payload semantics. For
example: AI Friend A payload ↓ M-PIN migration ↓ same AI Friend A
relationship is fundamentally different from: AI Friend A payload ↓
automatic semantic conversion ↓ AI Friend B payload The latter is not a
Core portability requirement.

# 19. Portability Is Not Merge

M-PIN v2 does not define automatic merging of separate M-PIN identities
or independent active continuities. Therefore: M-PIN A + M-PIN B ≠
automatic merged M-PIN C Interoperability and portability do not require
identity merge.

# 20. Copy

A physical or logical copy of M-PIN data may be created for: Backup;
migration; transfer; recovery preparation. A copy does not automatically
become a separately authoritative active M-PIN continuity.

# 21. Copy Is Not Ownership Transfer

Copying M-PIN state to another Device or Storage does not itself
transfer Owner Authority. Conceptually: copy bytes ≠ transfer ownership
Valid use still requires applicable identity, authority, and security
conditions.

# 22. Authoritative Active Continuity

M-PIN v2 distinguishes stored copies from the authoritative active
continuity. The canonical rule is: \## At any given valid active
context, one M-PIN continuity is authoritative for active
synchronization. Backups and inactive copies do not automatically become
concurrent active authorities.

# 23. Single Active Continuity

The Single Active M-PIN principle applies to authoritative operation,
not to the physical existence of only one byte-for-byte copy. Therefore
this is valid: Authoritative M-PIN + encrypted Backup + offline recovery
copy provided those copies are not simultaneously treated as independent
active authorities contrary to the Core model.

# 24. Offline Clone Limitation

If two complete M-PIN copies become fully disconnected and each can
operate independently, perfect global enforcement of single-active
continuity may be impossible without coordination. M-PIN v2 explicitly
acknowledges this limitation. Therefore the frozen requirement is: \##
one authoritative active continuity under the conforming operational
model. Strong globally coordinated clone exclusion across completely
disconnected environments is deferred.

# 25. No False Global Guarantee

A conforming implementation MUST NOT claim that disconnected clone
conflicts are mathematically impossible unless its actual architecture
provides the coordination necessary to guarantee that property. The
limitation must remain explicit.

# 26. Migration

Migration is an Owner-authorized transition of M-PIN continuity from one
compatible environment to another. Migration may involve: Device change;
Storage change; Provider change; cryptographic rewrapping;
format-compatible transfer. Migration is a controlled continuity
operation.

# 27. Migration Authorization

Migration MUST require applicable Owner Authority. A Provider, Device,
Storage operator, or Friend MUST NOT independently transfer M-PIN
continuity to a new authority context without the required
authorization.

# 28. Migration Source

The source environment MUST identify the state intended for migration
with sufficient integrity and freshness assurance. A stale or corrupted
copy MUST NOT silently replace a newer valid authoritative state. The
exact freshness mechanism remains deferred.

# 29. Migration Destination

The destination MUST validate the M-PIN continuity sufficiently to
preserve: M-PIN Identity; Owner Authority; Friend Folder binding;
Current State integrity; required security state. The destination MUST
NOT silently generate a new Owner merely because infrastructure changed.

# 30. Migration Atomicity

Migration SHOULD avoid a state in which two environments are
unintentionally accepted as independent authoritative active
continuities. Conceptually: Source authoritative ↓ authorized migration
↓ Destination validated ↓ authority transition ↓ Destination
authoritative The exact migration transaction protocol is deferred.

# 31. Migration Failure

If migration fails before the destination can be safely established as
authoritative, the implementation SHOULD preserve or recover the
previous valid authoritative continuity where possible. Migration
failure MUST NOT silently establish corrupted destination state.

# 32. Provider Migration

Provider migration means: Provider A ↓ M-PIN X ↓ Owner continuity
becomes: Provider B ↓ same M-PIN X ↓ same Owner continuity A Provider
change SHOULD preserve Friend Folder relationships and valid Current
State.

# 33. Provider Migration Does Not Rebind Friends

A Provider migration MUST NOT silently change: Friend A → Folder A into:
Friend A → Folder B or: Friend B → Folder A Friend Folder binding
remains independently protected.

# 34. Provider Migration Does Not Grant Friend Access

Provider B becoming the new infrastructure Provider does not
automatically grant Provider B the authority of any Friend. Likewise,
migration does not create new Friend permissions.

# 35. Device Migration

Moving M-PIN continuity from Device A to Device B MAY preserve the same
logical M-PIN. Device B must establish valid Owner Authority. Device A’s
old active Session authority MUST NOT simply remain valid forever after
migration.

# 36. Storage Migration

Storage migration may involve moving persistent M-PIN state from: local
disk to cloud; cloud to local disk; USB to PC; PC to removable media;
Provider storage to Owner-controlled storage; one compatible storage
system to another. Storage migration MUST preserve required integrity
and identity relationships.

# 37. Session and Migration

M-PIN v2 does not require live migration of an active Synchronization
Session. A conforming implementation MAY: terminate the active Session;
migrate M-PIN continuity; establish a new Session at the destination.
This is sufficient for Core conformance.

# 38. Session Credentials Do Not Automatically Migrate

Active Session credentials SHOULD NOT simply be copied to the
destination and treated as valid current authority. A new environment
SHOULD re-establish Session authority according to Core 08. This reduces
stale and replay risk.

# 39. Backup

A Backup is a protected resilience copy of M-PIN data or state intended
to support recovery. A Backup is not: an active Friend Session; a second
active Owner; ordinary M-PIN version history; automatic rollback
history.

# 40. Backup Scope

A Backup MAY contain: Friend Folder Current State; M-PIN identity
metadata; Friend Folder bindings; permission configuration; recovery
metadata; other state necessary for legitimate restoration. The exact
Backup format is deferred.

# 41. Backup Protection

A Backup MUST receive confidentiality and integrity protection
appropriate to the M-PIN state it contains. Creating a Backup MUST NOT
become a way to produce an unprotected plaintext copy of all Owner state
without applicable authorization.

# 42. Backup Freshness

A Backup may be older than the current authoritative state. Therefore
restoration requires sufficient handling of freshness. The
implementation SHOULD be able to distinguish, where necessary: current
authoritative state from: older valid Backup The exact freshness
representation is deferred.

# 43. Backup Is Not Current State

The existence of Backup State B does not mean: Current State = B unless
a valid recovery process makes B part of the restored authoritative
continuity.

# 44. Backup Is Not Version History

Multiple Backups MAY exist for resilience. That fact does not redefine
M-PIN Core as a version-history system. Backups serve resilience.
Version history serves historical state navigation. M-PIN v2 requires
the former distinction but not the latter feature.

# 45. Recovery

Recovery is the process of restoring legitimate M-PIN continuity after
loss, corruption, credential loss, Device loss, Provider failure, or
another qualifying failure. Recovery is security-sensitive. It MUST NOT
bypass Owner authority merely for convenience.

# 46. Recovery Has Two Dimensions

M-PIN distinguishes: Authority Recovery and: Data Recovery These are
independent problems.

# 47. Authority Recovery

Authority Recovery restores legitimate control over the M-PIN when
normal Owner authentication material is unavailable or unusable.
Examples may include: lost credential; replaced Device; lost
authentication factor; Provider transition. Authority Recovery does not
itself reconstruct missing Friend Folder data.

# 48. Data Recovery

Data Recovery restores valid M-PIN data from available legitimate copies
or Backup material. Examples may include: Storage failure; corrupted
local copy; lost Device containing the primary data; Provider data loss.
Data Recovery does not itself prove that the person invoking recovery
has legitimate Owner Authority.

# 49. Authority Recovery Is Not Data Recovery

Canonical distinction: Owner Authority recovered ↓ data may still be
missing and: Backup data exists ↓ Owner Authority may still need
recovery Both may be required to restore usable M-PIN continuity.

# 50. No Magical Recovery

If all valid copies of data are destroyed: Data Recovery may be
impossible If all legitimate recovery factors and authority material are
lost: Authority Recovery may be impossible M-PIN MUST NOT promise
recovery where the required recovery basis no longer exists.

# 51. Independent Recovery

M-PIN recovery MUST NOT require one particular Friend to remain
operational. For example: AI Friend A unavailable ≠ M-PIN Owner cannot
recover M-PIN The Friend is not the root recovery authority for the
Owner’s M-PIN.

# 52. Provider-Independent Recovery

Where feasible under the implementation’s recovery design, loss of
Provider A SHOULD NOT inherently destroy the Owner’s ability to recover
or migrate M-PIN if sufficient valid state and recovery material exist
elsewhere. This is part of Provider Independence. It is not a guarantee
against total loss of every copy and key.

# 53. No Universal Backdoor

M-PIN v2 does not require: Provider master password; Friend master key;
manufacturer override; universal administrator recovery; hidden Owner
bypass. A recovery system MAY use configured recovery factors. Those
factors must have explicit and bounded authority.

# 54. Recovery Security

Recovery MUST protect against unauthorized takeover. An attacker MUST
NOT obtain M-PIN Owner Authority merely by: knowing an Owner name;
possessing a Backup; controlling a Provider admin account; possessing a
lost Device; claiming the original Device was lost. The exact recovery
proof mechanism is deferred.

# 55. Recovery and Password Change

Changing or recovering a password does not inherently create a new M-PIN
Identity. Conceptually: M-PIN X ↓ credential change ↓ M-PIN X provided
legitimate continuity is established. Logical identity and
authentication material are distinct.

# 56. Recovery and Cryptographic Keys

Cryptographic keys MAY change through legitimate recovery or migration.
Key replacement does not inherently create a new M-PIN. The
implementation MUST preserve sufficient continuity and integrity to
establish that the recovered state belongs to the same legitimate M-PIN
relationship.

# 57. Recovery and Revocation

Recovery MUST NOT silently reactivate previously revoked authority
merely because an older Backup contains old permission metadata.
Example: State at T1: Friend A allowed State at T2: Friend A revoked
Backup from T1 restored The recovery process SHOULD NOT blindly treat
the T1 permission as current without applicable freshness and revocation
handling.

# 58. Recovery and Current State

A recovery process may restore an older valid Backup when newer state is
irretrievably lost. That does not mean the Core provides ordinary
rollback. It means the recovered older state becomes the valid Current
State through a recovery operation.

# 59. Recovery and Service Records

Restoring M-PIN state does not rewrite independent Friend Service
Records. For example: restoring an older Commerce Friend Folder ≠
reversing a completed purchase restoring an older Healthcare Friend
Folder ≠ deleting a hospital clinical record Service Record systems
remain independent.

# 60. Recovery and External Reality

M-PIN recovery MUST NOT be represented as restoring external real-world
state. Examples: a refunded transaction does not become unrefunded; a
robot’s physical action is not undone; a prescription is not legally
reversed; a delivered package is not physically returned. Recovery
restores M-PIN continuity, not history itself.

# 61. Recovery and Friend Payload Semantics

M-PIN MAY restore a structurally valid Friend payload. The Friend
remains responsible for interpreting its semantic content. M-PIN MUST
NOT invent semantic conflict resolution for arbitrary Friend payloads.

# 62. Conflict Between Copies

If multiple copies claim to represent the same M-PIN continuity and the
implementation cannot safely determine the valid authoritative state: do
not silently merge The implementation SHOULD: fail closed; require
explicit recovery resolution; use a defined freshness mechanism; use a
defined migration/reconciliation mechanism. M-PIN semantic neutrality
must be preserved.

# 63. No Automatic Friend Payload Merge

M-PIN MUST NOT attempt: Friend payload A + Friend payload B ↓ semantic
merged payload C unless the relevant Friend itself provides a conforming
semantic mechanism. M-PIN Core does not understand arbitrary Friend
semantics well enough to perform universal merge.

# 64. M-PIN Merge

M-PIN v2 does not define merging two independent M-PIN identities into
one. This remains outside the frozen Core. Future interoperability MUST
NOT be assumed to imply identity merge.

# 65. Portability Between Providers

A conforming Provider-based implementation SHOULD make it possible for
the Owner to obtain sufficient M-PIN state for migration to another
compatible implementation. The exact export package is deferred. The
export path MUST preserve security rather than merely exposing raw
plaintext.

# 66. Exportability

Where a Provider stores the authoritative M-PIN state, Provider lock-in
would conflict with Provider Independence. Therefore Provider-based
implementations SHOULD support Owner-authorized export of the state and
metadata necessary for compatible migration. Exportability does not
require revealing Provider proprietary implementation internals.

# 67. Friend Independence During Provider Migration

A Friend SHOULD NOT need to redesign its entire native service merely
because the Owner changes M-PIN Provider, provided both M-PIN
implementations satisfy the required standard behavior. This follows
from the separation: Friend ≠ M-PIN Provider

# 68. Provider Failure Scenario

Canonical scenario: Provider A unavailable ↓ Owner has valid
Backup/export/ recovery material ↓ Owner establishes authority ↓
Migrate/recover to compatible environment ↓ same M-PIN continuity This
scenario is possible only when sufficient valid recovery material
exists.

# 69. Provider Failure Without Recovery Material

If Provider A is the only location of: M-PIN data; required keys;
recovery factors; and all are irretrievably lost, Provider Independence
cannot reconstruct them from nothing. The architecture therefore
encourages recoverable portability but does not claim impossible
resilience.

# 70. Friend Failure Scenario

If Friend A disappears permanently: Friend Folder A may still remain
Owner-controlled M-PIN state. However, because Friend A owns the payload
semantics, another Friend does not automatically gain the ability or
authority to interpret that Folder. Persistence survival and semantic
usability are distinct.

# 71. Friend Replacement

Replacing a failed Friend with Friend B is not ordinary M-PIN migration.
Friend B normally receives its own Friend Folder. Any future transfer of
selected or translated data must use an explicit interoperability
mechanism. Direct access to Friend A’s Folder remains prohibited.

# 72. Disclosure and Portability

Owner-Mediated Disclosure remains a candidate interoperability
primitive. It is not the mechanism for Provider migration. These
concepts remain distinct: Provider migration = move M-PIN continuity

# Disclosure

potential selected data transfer between Friend relationships Disclosure
remains deferred from Core.

# 73. Portability and Encryption

Encrypted M-PIN state must remain usable after legitimate migration or
recovery. Therefore implementations must account for: key migration; key
rewrapping; credential change; recovery factors; destination
authorization. The exact cryptographic protocol remains deferred.

# 74. Portability and Provider Keys

A design in which only one Provider possesses the sole irreplaceable key
required to use M-PIN state may undermine practical Provider
Independence unless an appropriate migration or recovery path exists.
M-PIN v2 freezes the portability requirement but does not prescribe the
final key hierarchy.

# 75. Portability and Friend Identity

Migration MUST preserve enough Friend Identity association to resolve
each existing Friend Folder correctly after migration. Example: Before
migration: Friend A ↔ Folder A Friend B ↔ Folder B After migration:
Friend A ↔ Folder A Friend B ↔ Folder B The destination MUST NOT require
arbitrary manual Folder selection by a Friend.

# 76. Portability and Permission State

Permission configuration necessary for continuity MAY migrate. However:
persistent relationship configuration ≠ active Session authority Active
Session credentials SHOULD be re-established rather than blindly copied.

# 77. Portability and Current State

Migration SHOULD preserve the latest valid authoritative Current State
available to the migration process. It MUST NOT intentionally activate a
stale copy without explicit recovery semantics. The exact freshness
mechanism is deferred.

# 78. Portability and Backup

A Backup MAY be used as the source of recovery into another Device,
Storage system, or Provider. When that occurs, the operation is:
Recovery + possible Migration not merely ordinary file copying.
Authority and integrity checks still apply.

# 79. Portability and Local-Only Operation

Provider Independence requires that the architecture remain compatible
with implementations that do not require a Provider. Therefore a
conforming standard MUST NOT define the Provider as the sole root of:
M-PIN Identity; Owner Authority; Friend Folder semantics; Friend
relationship existence. A specific implementation may use Provider
services, but the Core architecture remains provider-neutral.

# 80. Portability Requirements

A conforming implementation MUST satisfy: \### PR-001 — Device
Independence M-PIN continuity MUST NOT be architecturally restricted to
one permanent Device. \### PR-002 — Storage Independence M-PIN
continuity MUST NOT require one permanent Storage medium. \### PR-003 —
Provider Optionality M-PIN Core MUST remain implementable without a
mandatory M-PIN Service Provider. \### PR-004 — Provider Independence
Use of one Provider MUST NOT redefine that Provider as the architectural
Owner. \### PR-005 — Identity Continuity Valid migration MUST preserve
the logical M-PIN Identity. \### PR-006 — Friend Folder Continuity Valid
migration MUST preserve Friend Folder relationships and bindings
necessary for continuity. \### PR-007 — Current State Integrity
Migration and recovery MUST NOT silently accept corrupted state as
authoritative. \### PR-008 — Owner Authorization Migration and recovery
operations requiring Owner authority MUST NOT proceed without valid
applicable authority. \### PR-009 — Session Re-establishment A migrated
or recovered environment MUST NOT blindly treat stale active Session
authority as current authority. \### PR-010 — Backup Distinction A
Backup MUST NOT automatically become a concurrent active M-PIN
continuity. \### PR-011 — Authority/Data Recovery Separation Authority
Recovery and Data Recovery MUST remain distinct. \### PR-012 — No
Universal Backdoor Core MUST NOT require a universal Provider or Friend
ownership override for recovery. \### PR-013 — No Semantic Merge M-PIN
MUST NOT automatically semantically merge conflicting arbitrary Friend
payloads. \### PR-014 — No Friend Rebinding Migration MUST NOT silently
rebind Friend Folders to different Friends. \### PR-015 — Service Record
Independence M-PIN recovery MUST NOT be represented as rollback of
independent Friend Service Records or external real-world events. \###
PR-016 — Security Preservation Portability MUST NOT require disabling
the Core confidentiality, integrity, authorization, or isolation
boundaries.

# 81. Recommended Portability Properties

A conforming implementation SHOULD additionally provide: \### PR-017 —
Owner Exportability Provider-based deployments SHOULD provide an
Owner-authorized export path sufficient for compatible migration. \###
PR-018 — Freshness Protection Migration and recovery SHOULD preserve
sufficient freshness information to resist stale-state activation. \###
PR-019 — Migration Atomicity Migration SHOULD minimize unintended
simultaneous authoritative operation of source and destination. \###
PR-020 — Provider Failure Recovery Provider deployments SHOULD support
recovery paths that do not require the failed Provider where practical.
\### PR-021 — Key Portability Cryptographic architecture SHOULD support
legitimate migration or recovery without permanent dependence on one
Provider-held secret. \### PR-022 — Backup Resilience Implementations
SHOULD permit protected Backup arrangements appropriate to the Owner’s
risk model.

# 82. Canonical Device Migration

Device A │ ▼ M-PIN X │ Current State │ ▼ Owner-authorized migration │ ▼
Device B │ ▼ same M-PIN X │ ▼ new Session established Device A does not
remain automatically authorized merely because it once hosted M-PIN X.

# 83. Canonical Storage Migration

Storage A │ ▼ M-PIN X │ ▼ validate state │ ▼ Owner-authorized migration
│ ▼ Storage B │ ▼ same M-PIN X Storage B does not become the Owner.

# 84. Canonical Provider Migration

Provider A │ ▼ M-PIN X │ ├── Friend Folder A ├── Friend Folder B └──
Friend Folder C │ ▼ Owner-authorized migration │ ▼ Provider B │ ▼ same
M-PIN X │ ├── same Friend Folder A relationship ├── same Friend Folder B
relationship └── same Friend Folder C relationship Provider migration
does not merge or replace the Friends.

# 85. Canonical Data Recovery

Primary M-PIN state lost/corrupted │ ▼ Protected Backup exists │ ▼
Owner/Recovery Authority established │ ▼ Backup integrity validated │ ▼
freshness/recovery rules applied │ ▼ Recovered Current State │ ▼ new
active continuity

# 86. Canonical Authority Recovery

M-PIN data still exists │ Owner normal credential lost │ ▼ configured
recovery process │ ▼ Recovery Authority established │ ▼ Owner Authority
restored │ ▼ same M-PIN continuity The exact recovery-factor mechanism
is deferred.

# 87. Canonical Combined Recovery

Device lost │ ├── normal credential unavailable └── primary data
unavailable │ ▼ Authority Recovery + Data Recovery │ ▼ validate identity
/ integrity / binding / freshness │ ▼ restore M-PIN continuity │ ▼
establish new Session

# 88. Portability Threats

Relevant threats include: unauthorized export; Provider lock-in;
destination impersonation; stale-state restoration; migration replay;
Friend Folder rebinding; key loss; Backup theft; Backup corruption;
clone conflict; unauthorized recovery; false ownership transfer. Core 10
defines the general security model. This document applies it to
continuity operations.

# 89. Recovery Threats

Recovery is particularly sensitive because it may bypass normal access
paths. A conforming implementation MUST NOT treat recovery as: security
disabled mode Recovery is itself a security protocol and must preserve
Owner Authority.

# 90. Portability Non-Goals

M-PIN v2.0 does not define: automatic merging of independent M-PINs;
automatic semantic translation between Friends; guaranteed recovery
after total loss of all keys and copies; perfect disconnected-clone
coordination; one mandatory cloud; one mandatory Provider; one mandatory
Backup provider; one live Session migration protocol; one universal
recovery authority; one universal export container.

# 91. Deferred Portability Mechanisms

The following remain deferred: exact .MPIN container portable
serialization export package format Provider discovery Provider trust
federation migration protocol migration transaction format state
generation encoding freshness proof key migration key rewrapping
recovery factor design Backup format Backup freshness protocol clone
coordination conflict resolution protocol secure deletion mechanism
Their deferral does not reopen the frozen continuity architecture.

# 92. Portability Invariants

The Portability & Recovery model is governed by these invariants: \##
The Device is not the Owner. \## Storage is not the Owner. \## The
Provider is not the Owner. \## Changing Device does not inherently
create a new M-PIN. \## Changing Storage does not inherently create a
new M-PIN. \## Changing Provider does not inherently create a new M-PIN.
\## Provider migration is not Friend migration. \## Portability is not
semantic translation. \## Portability is not M-PIN merge. \## A Backup
is not an active M-PIN. \## A copy is not ownership transfer. \##
Authority Recovery is not Data Recovery. \## Recovery is not ordinary
rollback. \## Recovery does not rewrite Service Records or external
reality. \## A universal recovery backdoor is not required. \##
Disconnected clones cannot be claimed to have perfect global
single-active enforcement without coordination.

# 93. Continuity Thesis

The complete M-PIN portability model can be reduced to: OWNER │ ▼ M-PIN
X │ ┌───────────┼───────────┐ │ │ │ ▼ ▼ ▼ Folder A Folder B Folder C │ │
│ ▼ ▼ ▼ Friend A Friend B Friend C The surrounding implementation may
change: Device A → Device B Storage A → Storage B Provider A → Provider
B while the logical continuity remains: same Owner same M-PIN same
Friend Folder relationships same valid persistent continuity when
legitimate migration or recovery succeeds. The M-PIN architecture
therefore separates: where the Owner’s state is implemented from: who
owns the continuity of that state That separation is the foundation of
M-PIN portability.

## M-PIN v2.0 — Core 11 / Portability & Recovery

## Status: FROZEN
