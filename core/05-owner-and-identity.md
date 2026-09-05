# M-PIN v2.0

## Core 05 — Owner & Identity

**Status:** FROZEN **Version:** 2.0 **Document Type:** Normative Core
Specification

------------------------------------------------------------------------

# 1. Purpose

This document defines the Owner and identity model of M-PIN v2.0.

It specifies the architectural distinction among:

- Owner;
- Owner Authority;
- M-PIN Identity;
- Friend Identity;
- Friend Account Identity;
- Device Identity;
- Provider Identity.

The purpose of this model is to preserve Owner continuity without making
that continuity dependent on one Friend, account, Device, Storage
location, or M-PIN Service Provider.

This document defines identity responsibilities and invariants.

It does not mandate one credential technology, civil-identity system,
certificate authority, authentication protocol, or account system.

------------------------------------------------------------------------

# 2. Identity Thesis

M-PIN separates identity from infrastructure.

The canonical relationship is:

``` text
Owner
  │
  │ exercises
  ▼
Owner Authority
  │
  ▼
M-PIN Identity
  │
  ├── Friend Identity A ↔ Friend Folder A
  ├── Friend Identity B ↔ Friend Folder B
  └── Friend Identity C ↔ Friend Folder C
The following identities remain separate:
Owner
M-PIN
Friend
Friend Account
Device
Provider
They MAY be technically linked by an implementation.
They MUST NOT be treated as architecturally identical merely because they are linked.
```

# 3. Owner

The Owner is the principal authority over one M-PIN and its
Owner-controlled Persistent State. The Owner is the architectural center
of M-PIN. The Owner MUST remain distinguishable from: Friend Friend
Account Device Storage M-PIN Service Provider A Friend may authenticate
the Owner for its own service. A Device may authenticate a local user. A
Provider may maintain an account. None of these facts alone redefine the
architectural Owner.

# 4. Owner Is Not a Friend Account

A Friend Account belongs to the Friend’s service relationship. For
example: Owner │ ├── Friend Account A ├── Friend Account B └── Friend
Account C The Owner may use multiple Friend Accounts without creating
multiple M-PIN Owners. Likewise: Friend Account ≠ M-PIN Identity A
Friend’s account lifecycle MUST NOT automatically define the lifecycle
of the Owner’s M-PIN.

# 5. Owner Is Not a Device

A physical Device does not become the Owner merely because the Owner
uses that Device. Conceptually: Owner │ ├── Device A ├── Device B └──
Device C Changing or losing a Device MUST NOT inherently create a new
Owner. The Device may participate in authentication or recovery. It does
not define architectural ownership.

# 6. Owner Is Not Storage

The location of M-PIN data does not determine the Owner. Conceptually:
Owner │ ▼ M-PIN │ ├── local Storage ├── cloud Storage └── removable
Storage Moving the persistent representation between compatible Storage
environments MUST NOT inherently change the Owner.

# 7. Owner Is Not the Provider

An M-PIN Service Provider MAY operate infrastructure. That
infrastructure role does not make the Provider the Owner. Conceptually:
Owner │ │ authority ▼ M-PIN

Provider │ └── optional infrastructure Provider administrative authority
MUST remain distinct from Owner Authority.

# 8. Owner Authority

Owner Authority is the legitimate authority by which the Owner
authorizes M-PIN operations. Operations requiring Owner Authority may
include: establishing synchronization; approving first Friend Folder
creation; Save; revocation; migration; recovery; other Owner-controlled
operations defined by the Core. Owner Authority MUST be established
before an operation requiring it is accepted.

# 9. Authentication Is Not Ownership

M-PIN distinguishes: Authentication ≠ Authorization ≠ Ownership
Authentication establishes sufficient confidence in a claimed principal
or credential according to the implementation. Authorization determines
whether a specific operation is permitted. Ownership defines the
architectural authority relationship. Therefore: successful
authentication ≠ automatic unrestricted Owner authority The
authenticated principal must still possess the required authorization
for the requested operation.

# 10. M-PIN Does Not Require Civil Identity

M-PIN v2.0 does not require the Owner to be identified through one
universal real-world civil identity system. The Core does not mandate:
legal name; government identifier; passport; national identity number;
biometric civil registry. An implementation MAY integrate such identity
systems where appropriate. That integration is not a universal M-PIN
Core requirement. The Core requires continuity of legitimate Owner
Authority, not one mandatory real-world identity scheme.

# 11. M-PIN Identity

M-PIN Identity is the stable identity of one M-PIN continuity.
Conceptually: Owner │ ▼ M-PIN Identity X │ ├── Friend Folder A ├──
Friend Folder B └── Friend Folder C M-PIN Identity MUST distinguish one
M-PIN continuity from another. The exact identifier format is deferred.

# 12. M-PIN Identity Stability

M-PIN Identity MUST remain stable across ordinary continuity-preserving
changes where the applicable migration or recovery succeeds. Examples
include: Device A → Device B Storage A → Storage B Provider A → Provider
B These transitions MUST NOT inherently require: M-PIN X → new M-PIN Y
The same M-PIN continuity should remain identifiable as the same M-PIN.

# 13. M-PIN Identity Immutability

Within one continuing M-PIN, its identity MUST NOT be casually
reassigned to represent a different independent M-PIN. Conceptually:
M-PIN Identity X │ └── same continuity not: M-PIN Identity X ↓ silently
reused for unrelated continuity Y This preserves the v1 identity
immutability principle. Implementation-specific identifier rotation MAY
be possible if the architecture can prove continuity of the same logical
M-PIN. The logical identity MUST remain stable even if an underlying
credential or representation changes.

# 14. One Active M-PIN Continuity

The existence of one M-PIN Identity does not imply that every physical
copy of its data is simultaneously authoritative. The logical rule is:
M-PIN Identity X │ └── one authoritative active continuity Protected
backup copies MAY exist. They do not automatically become independent
active M-PINs.

# 15. Backup Identity

A backup of M-PIN X remains a backup associated with M-PIN X. It MUST
NOT automatically become: new M-PIN Y merely because it exists as
another physical copy. If restored legitimately, it participates in
restoration of the same M-PIN continuity, subject to freshness,
integrity, and recovery requirements.

# 16. Offline Clone Limitation

M-PIN v2.0 does not claim that logical identity alone can prevent two
fully disconnected copies from both behaving as active instances without
coordination. Therefore: logical requirement: one authoritative active
continuity

does not imply

perfect global offline clone prevention A stronger coordination
mechanism is an implementation or future protocol matter.

# 17. Friend Identity

Friend Identity identifies the Friend participating in the M-PIN
relationship. M-PIN uses Friend Identity to support: Friend distinction;
Friend Folder resolution; Friend Folder binding; Permission; Session
establishment; security decisions. Friend Identity MUST be sufficiently
stable and verifiable to prevent one Friend from being mistaken for
another.

# 18. Friend Identity Is Not Display Name

A Friend MUST NOT establish identity merely by presenting an arbitrary
familiar name. For example: claimed name: “Friend A” is not sufficient
proof that the service is the legitimate Friend A. A conforming
implementation MUST use an appropriate Friend Identity verification
mechanism. The exact credential mechanism is deferred.

# 19. Friend Identity and Friend Folder

The canonical binding is: Verified Friend Identity A ↕ Friend Folder A
M-PIN MUST resolve Friend Folder access from the verified Friend
relationship rather than allowing an untrusted Friend to freely choose
another Folder. Conceptually prohibited: Friend B │ └── “open Friend
Folder A” without valid authority.

# 20. Stable Friend Binding

Once a Friend Folder has been established for a Friend, later authorized
synchronization SHOULD resolve the existing binding. Conceptually: first
synchronization:

Friend A ↓ Folder absent ↓ Owner approval ↓ Friend Folder A created ↓
binding established

later synchronization:

Friend A ↓ identity verified ↓ existing binding found ↓ Friend Folder A
reused A new independent Friend Folder MUST NOT be silently created on
every synchronization.

# 21. Friend Evolution

A Friend may evolve internally without necessarily becoming a new Friend
Identity. Examples include: software update; AI model update; backend
replacement; database migration; UI redesign; infrastructure change. If
the service remains the same Friend relationship under the applicable
identity rules, the existing Friend Folder MAY continue to be used.
M-PIN does not require a new Friend Folder merely because the Friend’s
internal implementation changes.

# 22. New Friend Identity

A genuinely different Friend MUST NOT silently inherit another Friend’s
Friend Folder merely because: the services are similar; the same company
operates both; one product replaced another; the Owner wants
convenience. Conceptually: Friend A ↕ Folder A

Friend B ↕ Folder B unless a future explicitly authorized migration or
interoperability mechanism defines otherwise. M-PIN v2.0 does not define
automatic semantic Friend-to-Friend migration.

# 23. Friend Account Identity

A Friend Account Identity is the identity used inside the Friend’s own
service account system. It MAY be associated with the M-PIN
relationship. It MUST remain conceptually distinct from Friend Identity
and M-PIN Identity. For example: Friend Identity │ └── service principal

Friend Account Identity │ └── Owner/customer account inside that service
The exact mapping is Friend-defined unless constrained by an applicable
Profile.

# 24. One Friend Account / One M-PIN Binding

Where a Friend uses an Owner-specific Friend Account for
synchronization, the same Friend Account MUST NOT silently bind to
multiple active M-PIN continuities in a manner that violates the
established Owner continuity and binding rules. This preserves the
intent of the v1 one-account/one-M-PIN binding rule. A conforming
implementation MUST prevent ambiguous active bindings. This rule does
not prohibit: migration; recovery; replacement of a lost Device;
restoration of the same M-PIN; legitimate account changes handled
through an explicit continuity process.

# 25. Friend Account Change

Changing a Friend Account does not automatically define what happens to
the Friend Folder. The Friend and M-PIN implementation MUST preserve the
applicable Owner authority and Friend identity boundaries. The Core does
not mandate one universal account-transfer policy. A Friend MUST NOT
silently expose a previous account’s M-PIN state to a new unauthorized
account.

# 26. Device Identity

Device Identity identifies a Device where Device distinction is required
for security, migration, or recovery. Device Identity MAY be used to:
recognize an authorized Device; detect a new Device; support recovery;
support Session security; support migration. Device Identity MUST NOT be
treated as M-PIN Identity.

# 27. Device Replacement

A valid Device replacement flow conceptually preserves: Owner │ ▼ M-PIN
Identity X │ Device A ↓ replacement / recovery ↓ Device B The Device
changes. The M-PIN does not inherently change.

# 28. Device Loss

Loss of a Device MUST NOT automatically transfer Owner Authority to
whoever possesses the Device. A conforming security model SHOULD assume
that physical possession and legitimate Owner Authority are distinct
properties. Conceptually: possession ≠ authentication ≠ authorization ≠
ownership Detailed recovery and threat handling are defined in Core 10
and Core 11.

# 29. Storage Identity

An implementation MAY identify Storage locations or Storage instances
for integrity, migration, freshness, or recovery purposes. Storage
Identity, where used, MUST NOT become M-PIN Identity. Changing Storage
MUST NOT inherently create a new Owner or new M-PIN.

# 30. Provider Identity

Provider Identity identifies an M-PIN Service Provider where one
participates. Provider Identity may be used for: trust establishment;
migration; infrastructure authorization; service discovery; audit.
Provider Identity MUST remain distinct from M-PIN Identity.

# 31. Provider Account

A Provider MAY maintain an account for the Owner. That Provider account
is not the M-PIN Identity itself. Conceptually: Provider Account ≠ M-PIN
Identity If the Owner migrates away from Provider A, loss of the
Provider A account MUST NOT by architectural definition mean that M-PIN
X ceases to exist. Actual migration feasibility depends on valid access
to the required state, keys, and recovery material.

# 32. Provider Migration

Where a conforming migration path exists: Provider A │ ▼ M-PIN X │ ▼
Provider B should preserve: M-PIN Identity; valid Owner continuity;
Friend Folder relationships; applicable security properties;
authoritative Persistent State. Provider migration MUST NOT silently
create an unrelated M-PIN.

# 33. Provider Administrator

A Provider administrator MAY possess infrastructure privileges. Those
privileges MUST NOT automatically equal Owner Authority. Conceptually:
Provider Admin ≠ Owner A bounded administrative or recovery role MAY
exist if explicitly defined by an implementation. It MUST NOT silently
become unrestricted Owner authority.

# 34. Authentication Subjects

M-PIN authentication MAY involve different subjects: Owner Friend Device
Provider These authentication processes serve different purposes. A
successful Friend authentication does not authenticate the Owner. A
successful Device authentication does not automatically authorize every
Owner operation. A successful Provider authentication does not establish
Friend Identity. The roles MUST remain distinguishable.

# 35. Authorization Scope

Authorization MUST be scoped to the relevant operation. Examples
include: authorize Session authorize Friend Folder creation authorize
Load authorize Save authorize migration authorize recovery A broad
authenticated state MUST NOT be interpreted as permanent universal
authorization unless the specification explicitly permits it.

# 36. Owner Save Authority

Owner Save is a persistence authorization event. The system MUST
establish that the Save is associated with valid Owner persistence
authority and the active synchronization context. Conceptually: Owner
Authority + valid Session + correct Friend binding ↓ SAVE authorization
A Friend MUST NOT manufacture Owner Save authority merely because it can
modify Runtime State.

# 37. Recovery Authority

Recovery authority MUST be distinguishable from ordinary Session
authority. A Friend Session credential MUST NOT automatically become a
universal M-PIN recovery credential. Likewise, Provider administrative
access MUST NOT automatically become unrestricted recovery authority.
Recovery is defined further in Core 11.

# 38. Migration Authority

Migration affects M-PIN continuity and therefore requires appropriate
Owner authority. Conceptually: Owner-authorized migration ↓ source
validation ↓ destination validation ↓ continuity preserved A Storage or
Provider actor MUST NOT silently migrate the authoritative M-PIN to an
unrelated destination merely because it controls infrastructure.

# 39. Revocation Identity Boundary

Revocation MUST apply to the authority being revoked. For example,
revoking: Device authority does not inherently mean deleting: M-PIN
Identity Likewise, revoking: Friend Session authority does not
inherently mean destroying: Friend Folder Identity, authority, and data
lifecycle MUST remain separate concepts.

# 40. Identity and Deletion

Deleting a Friend Folder, deleting an M-PIN, closing a Friend Account,
and revoking a Device are different operations. The Core MUST NOT
silently collapse them into one operation. Conceptually: revoke access ≠
delete state

delete Friend Folder ≠ delete Friend Account

close Provider account ≠ destroy M-PIN identity Actual deletion
requirements depend on the applicable Core and Profile rules.

# 41. Identity and Service Records

Owner control of M-PIN Identity does not imply control over every
identity or record inside the Friend. For example, deleting or
recovering an M-PIN MUST NOT automatically be interpreted as deletion or
alteration of: hospital records; merchant transaction records; billing
records; security records; regulatory records. Those may be independent
Friend Service Records.

# 42. Identity and Profiles

Profiles MAY introduce additional identity roles. For example:
Healthcare: Owner Patient Clinician Institution

Commerce: Owner Customer Merchant Payment actor

Robotics: Owner Device Robot Friend Operator

AI: Owner AI Friend Agent Tool These Profile roles MUST NOT silently
redefine the Core Owner, M-PIN Identity, or Friend Folder boundaries.

# 43. Owner and Patient

In Healthcare, Owner and Patient MAY refer to the same real-world
person. They are not automatically the same architectural role. The
Healthcare Profile may require separate legal, clinical, or
institutional authorization. M-PIN Owner authentication MUST NOT
automatically be represented as medical consent or clinical authority.

# 44. Owner and Customer

In Commerce, Owner and Customer MAY refer to the same real-world person.
They remain conceptually distinct roles. M-PIN Owner authorization does
not automatically establish: payment authorization; merchant
authorization; age verification; contractual consent unless an explicit
integration establishes that relationship.

# 45. Owner and Robot User

In Robotics, physical possession or proximity to a Robot Device does not
establish Owner Authority. Conceptually: near robot ≠ Owner

using robot ≠ M-PIN authority The Robotics Profile defines additional
physical-system boundaries.

# 46. Owner and AI User

An AI Friend may maintain its own user/account identity. That account
relationship does not replace M-PIN Owner Authority. An AI model or
agent MUST NOT infer broader M-PIN authority merely from having access
to the Friend’s Runtime.

# 47. Agent Identity

Where an AI Friend operates internal agents or tools, those internal
actors do not automatically become independent M-PIN Friends. They
operate under the Friend relationship unless separately modeled and
authorized as distinct Friends. An internal agent MUST NOT exceed the
M-PIN authority granted to the Friend through which it operates.

# 48. Composite Systems

A single physical system may contain several identities. For example:
Robot Device │ ├── Device Identity ├── Robot Friend Identity ├── AI
Friend Identity └── Provider Identity The physical co-location of these
identities MUST NOT collapse them into one M-PIN authority.

# 49. Identity Continuity

M-PIN identity design SHOULD preserve continuity through normal change.
The principle is: \## Service may change. Device may change. Provider
may change. Owner continuity remains. This does not mean every change is
automatically authorized. It means infrastructure change does not by
itself redefine the Owner’s logical M-PIN identity.

# 50. Identity Portability

A portable M-PIN MUST preserve enough identity continuity to prevent
migration from becoming silent identity replacement. A migration SHOULD
be able to establish conceptually: source M-PIN X = destination M-PIN X
rather than: source M-PIN X → unrelated destination M-PIN Y The exact
proof mechanism is deferred.

# 51. Identity Recovery

Recovery SHOULD restore: same Owner continuity + same M-PIN identity
where sufficient legitimate recovery material exists. Changing a
password, key, Device, or Provider during recovery MUST NOT inherently
mean creating a new logical M-PIN.

# 52. Password and Identity

A password or similar secret MAY be one authentication factor. It is not
itself the M-PIN Identity. Therefore: password change ≠ M-PIN identity
change Likewise: lost password ≠ automatic destruction of logical
identity provided a valid recovery path exists.

# 53. Key and Identity

A cryptographic key MAY participate in M-PIN identity, authentication,
encryption, or integrity. The Core does not require the logical M-PIN
Identity to equal one immutable cryptographic key forever. Key rotation
or migration MAY be compatible with the same logical identity if
continuity can be securely established. The exact key architecture is
deferred.

# 54. Credential and Identity

A credential proves or supports an identity relationship. A credential
is not necessarily the identity itself. Conceptually: Credential A ↓
supports proof of M-PIN Identity X

Credential B ↓ after authorized rotation supports proof of same M-PIN
Identity X This separation enables recovery and secure credential
lifecycle management without forcing logical identity replacement.

# 55. Identity Freshness

Where stale identity or authority material could be replayed, a
conforming implementation MUST have a means to distinguish valid current
authority from invalid stale authority. Possible mechanisms MAY include:
generation values; nonces; counters; timestamps; revocation state; other
freshness mechanisms. The exact mechanism is deferred.

# 56. Identity Integrity

Security-relevant identity associations MUST be protected against
unauthorized modification. This includes, where applicable: M-PIN
Identity ↕ Friend Folder set

Friend Identity ↕ Friend Folder binding An attacker MUST NOT be able to
obtain Friend Folder access merely by modifying unprotected identity
metadata.

# 57. Identity Confidentiality

Not every identity value is necessarily secret. However, an
implementation MUST protect identity-related information where
disclosure would violate M-PIN security or privacy boundaries. The Core
does not require all identifiers to be globally public. The exact
identifier privacy model is implementation-defined subject to Core 10.

# 58. Friend Folder Discovery Privacy

A Friend SHOULD learn only the information required to resolve and use
its own Friend Folder. A Friend SHOULD NOT receive an enumerable list of
unrelated Friend Folder identities merely to discover its own Folder.
This is a privacy-preserving architectural recommendation consistent
with Friend Folder Isolation. The exact discovery mechanism remains
deferred.

# 59. Provider Visibility

Provider participation does not automatically define what plaintext or
identity metadata the Provider can observe. That property depends on the
implementation’s cryptographic and trust architecture. Therefore v2.0
MUST NOT claim: Provider can never see plaintext unless a particular
implementation actually guarantees it. The Core instead requires that
Provider authority not silently exceed the defined M-PIN boundary.

# 60. Identity Collision

A conforming implementation MUST prevent identity collisions from
causing one M-PIN or Friend to be mistaken for another. The exact
identifier generation mechanism is deferred. The required property is:
Identity A must not resolve as Identity B within the relevant trust and
conformance scope.

# 61. Identity Reassignment

A Friend Folder binding MUST NOT be silently reassigned from Friend A to
Friend B. Conceptually prohibited: Friend Folder A ↕ Friend A

then silently:

Friend Folder A ↕ Friend B Any future migration between different Friend
identities would require an explicit architecture or protocol preserving
Owner authority and data semantics. v2.0 does not define such automatic
reassignment.

# 62. Account Takeover Boundary

If a Friend Account is compromised, M-PIN MUST NOT assume that the
attacker thereby possesses unrestricted M-PIN Owner Authority. Likewise,
compromise of M-PIN Owner credentials does not automatically grant every
independent Friend Account credential. The identities are separate
security domains even when integrated operationally.

# 63. Device Compromise Boundary

If an authorized Device is fully compromised while decrypted M-PIN state
is available, confidentiality may be compromised. M-PIN v2.0 does not
claim otherwise. The architecture SHOULD limit persistent authority and
exposure through: authentication; Session boundaries; revocation;
encryption at rest; recovery; applicable Device trust controls. Detailed
threat treatment is defined in Core 10.

# 64. Friend Compromise Boundary

If an authorized Friend is compromised while it legitimately receives
plaintext from its own Friend Folder, that plaintext may be exposed.
M-PIN can still prevent the compromised Friend from automatically
receiving unrelated Friend Folder state. Thus: compromised Friend A may
threaten Friend A authorized plaintext

but does not thereby gain Friend B Folder authority assuming the M-PIN
boundary itself remains uncompromised.

# 65. Provider Compromise Boundary

A compromised Provider may threaten the functions and data accessible to
that Provider under the specific implementation. M-PIN MUST NOT assume
Provider compromise is harmless. At the same time, Provider compromise
MUST NOT be architecturally defined as legitimate Owner Authority.
Threat mitigation depends on the implementation’s key, storage,
authentication, and recovery design.

# 66. Recovery Without Backdoor Ownership

Recovery MUST NOT require redefining a Provider, Friend, or universal
administrator as the permanent hidden Owner. A recovery actor MAY
possess bounded recovery capability. That capability MUST remain
distinguishable from ordinary unrestricted Owner Authority.

# 67. Identity Minimalism

The Core SHOULD require only the identity information necessary to
preserve: continuity; binding; authorization; security; portability;
recovery; conformance. M-PIN SHOULD NOT require universal collection of
unrelated identity attributes merely because they might be useful to a
Friend. This principle supports Provider and Friend neutrality.

# 68. No Universal Identity Broker Requirement

M-PIN v2.0 does not require one global identity provider through which
every Owner and Friend must authenticate. A future ecosystem MAY define
trust registries or identity infrastructure. The v2.0 architecture
requires the identity properties, not one mandatory global operator.

# 69. No Mandatory Provider Root

The trust architecture MUST NOT assume that one M-PIN Service Provider
is the universal root identity authority for every M-PIN deployment.
Local and alternative conforming deployments remain architecturally
possible. Provider discovery and trust federation are deferred.

# 70. Identity and Zero Requirement

The Zero Requirement principle applies to identity implementation. The
Core defines required properties such as: stable distinction
verifiability binding integrity continuity revocation freshness where
required It does not require one universal: certificate format OAuth
flow DID method PKI biometric system hardware token password system An
implementation MAY use such technologies if the Core properties are
preserved.

# 71. Identity and Conformance

Identity conformance is based on observable security behavior. For
example: Friend B claims Friend A identity ↓ verification fails ↓ Friend
Folder A access denied and: Owner migrates from Device A to authorized
Device B ↓ same M-PIN continuity may be restored The exact internal
implementation may differ.

# 72. Required Identity Properties

A conforming M-PIN v2 implementation MUST preserve the following
properties where the corresponding role exists: \### ID-01 — Owner
Distinction Owner MUST remain distinct from Friend, Device, Storage, and
Provider. \### ID-02 — M-PIN Identity One M-PIN continuity MUST have a
distinguishable logical identity. \### ID-03 — Friend Identity Friends
MUST be distinguishable for Folder binding and authorization. \### ID-04
— Binding Integrity A Friend MUST NOT arbitrarily access or rebind
another Friend’s Folder. \### ID-05 — Device Independence Device
replacement MUST NOT inherently require M-PIN replacement. \### ID-06 —
Provider Independence Provider replacement MUST NOT inherently require
M-PIN replacement. \### ID-07 — Credential Separation Credentials MUST
NOT automatically be treated as the logical identity itself. \### ID-08
— Authorization Separation Authentication MUST NOT automatically imply
unrestricted authorization. \### ID-09 — Recovery Continuity Valid
recovery SHOULD restore the same logical M-PIN continuity where
possible. \### ID-10 — No Administrative Ownership Provider
administrative privilege MUST NOT automatically equal Owner Authority.
\### ID-11 — Identity Integrity Security-relevant identity and binding
metadata MUST be protected against unauthorized modification. \### ID-12
— Fail Closed If required identity or authority cannot be established,
the affected M-PIN operation MUST fail closed.

# 73. Canonical Owner Model

                          OWNER
                            │
                     Owner Authority
                            │
                            ▼
                     M-PIN Identity X
                            │
           ┌────────────────┼────────────────┐
           │                │                │
           ▼                ▼                ▼
    Friend Identity A Friend Identity B Friend Identity C
           │                │                │
           ↕                ↕                ↕
      Friend Folder A  Friend Folder B  Friend Folder C

External relationships may additionally include: Owner ├── Device
Identity ├── Friend Account Identity └── Provider Account / Provider
Identity These relationships do not collapse into M-PIN Identity.

# 74. Canonical Device Migration

OWNER │ ▼ M-PIN X │ ├── old Device A │ │ migration/recovery │ ↓ └── new
Device B

Result: M-PIN Identity = X

# 75. Canonical Provider Migration

OWNER │ ▼ M-PIN X │ ├── Provider A │ │ │ │ authorized migration │ ▼ └──
Provider B

Result: M-PIN Identity = X where the migration succeeds under the
applicable security and portability requirements.

# 76. Canonical Friend Binding

Verified Friend A │ ▼ resolve binding │ ▼ Friend Folder A │ ▼ authorized
Session Not: unverified Friend │ ▼ chooses arbitrary Folder

# 77. Canonical Recovery

Owner loses normal access ↓ Recovery procedure ↓ recovery authority
validated ↓ same M-PIN identity restored ↓ valid current state recovered
if recoverable data exists Authority recovery and data recovery remain
separate.

# 78. Identity Non-Goals

M-PIN v2.0 Core does not attempt to define: universal civil identity;
national identity infrastructure; universal Friend registry; one global
Provider registry; one mandatory certificate authority; one biometric
system; one universal account system; one mandatory credential format.
These may be addressed by implementations or future interoperability
work.

# 79. Deferred Identity Mechanisms

The following remain intentionally deferred: exact M-PIN identifier
format Owner credential format Friend credential format Device
credential format Provider credential format key hierarchy key rotation
key migration Friend registry mechanism Provider discovery Provider
trust federation Session token format recovery-factor algorithm
freshness representation identity privacy mechanism Their deferral does
not reopen the architecture-level identity boundaries.

# 80. Identity Invariants

The M-PIN v2 identity model is governed by the following invariants: \##
Owner is not Friend. \## Owner is not Device. \## Owner is not Storage.
\## Owner is not Provider. \## M-PIN Identity is not Friend Account
Identity. \## M-PIN Identity is not Device Identity. \## M-PIN Identity
is not Provider Identity. \## Authentication is not ownership. \##
Authentication is not unrestricted authorization. \## Friend Identity
determines the Friend relationship; it does not grant cross-Friend
Folder authority. \## Changing Device, Storage, or Provider does not
inherently create a new M-PIN. \## Recovery restores continuity where
possible; it does not redefine ownership.

# 81. Identity Thesis

The M-PIN identity model can be reduced to one rule: \## Infrastructure
may change without silently changing who owns the continuity. Service
may change. Device may change. Storage may change. Provider may change.
Credentials may rotate. Where legitimate continuity is preserved: \##
the Owner’s M-PIN remains the same logical M-PIN.

## M-PIN v2.0 — Core 05 / Owner & Identity

## Status: FROZEN
