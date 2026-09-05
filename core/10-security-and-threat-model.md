# M-PIN v2.0

## Core 10 — Security & Threat Model

**Status:** FROZEN **Version:** 2.0 **Document Type:** Normative Core
Specification

------------------------------------------------------------------------

# 1. Purpose

This document defines the security model and threat boundaries of M-PIN
v2.0.

It specifies:

- protected assets;
- trust boundaries;
- security principals;
- threat actors;
- confidentiality requirements;
- integrity requirements;
- authentication and authorization boundaries;
- Friend Folder isolation;
- Session security;
- persistence security;
- replay resistance;
- recovery and revocation boundaries;
- Provider and Device threats;
- security limitations.

M-PIN security is defined by enforceable boundaries rather than by
assuming that every participating system is trusted.

------------------------------------------------------------------------

# 2. Security Thesis

The canonical M-PIN security rule is:

> **M-PIN protects the boundary through which a Friend accesses
> Owner-controlled persistent state.**

M-PIN does not claim to control every action performed inside an
authorized external Friend Runtime.

Conceptually:

``` text
Owner-controlled Persistent State
             │
             ▼
          M-PIN
             │
      security boundary
             │
             ▼
     Authorized Friend
             │
             ▼
       Friend Runtime
The M-PIN boundary MUST determine whether the Friend is authorized to cross that boundary.
```

# 3. Security Objectives

M-PIN v2 seeks to preserve: Confidentiality Integrity Authorization
Isolation Persistence authenticity Session validity Owner continuity
Recovery integrity Portability integrity These properties apply to the
M-PIN boundary. They do not imply that every external service is
inherently trustworthy.

# 4. Protected Assets

Security-relevant M-PIN assets include: M-PIN Identity; Owner Authority;
Friend Identity associations; Friend Folder bindings; Friend Folder
Persistent State; permission metadata; Session authority; Save
authorization; integrity metadata; recovery material; migration
authority; cryptographic material where applicable; security-relevant
configuration. Implementations MUST protect these assets according to
their security role.

# 5. Security Principals

The principal architectural actors are: Owner Friend M-PIN Device
Storage Provider (optional) Additional Profile-specific principals MAY
exist. The security model MUST NOT collapse these principals into one
trust identity merely because one organization or Device hosts several
of them.

# 6. Trust Boundaries

The principal trust boundaries include: Owner ↔ M-PIN M-PIN ↔ Friend
M-PIN ↔ Storage M-PIN ↔ Device M-PIN ↔ Provider Friend ↔ Friend Runtime
where applicable. Different implementations MAY place these boundaries
across different physical components. The logical security properties
remain normative.

# 7. Threat Actors

M-PIN v2 considers at minimum: unauthorized Friend; malicious Friend;
compromised Friend; malicious or compromised Provider; compromised
Device; compromised Storage; network attacker; credential thief; replay
attacker; unauthorized user of a lost Device; attacker modifying Friend
Folder binding; attacker restoring stale state; attacker attempting
unauthorized migration or recovery.

# 8. No Universal Trust Assumption

M-PIN MUST NOT assume: Friend = trusted because registered Provider =
trusted because it hosts M-PIN Device = trusted because Owner used it
before Storage = trusted because it contains .MPIN network = trusted
because connection succeeded Security-sensitive authority MUST be
established through the applicable identity, authorization, integrity,
and Session mechanisms.

# 9. Ownership, Authentication, and Authorization

M-PIN distinguishes: Ownership Authentication Authorization These
concepts MUST remain separate. Successful authentication does not
automatically grant unrestricted authority. Possession of a Device or
storage object does not automatically establish ownership. Provider
administration does not automatically establish Owner Authority.

# 10. Default Deny

M-PIN security follows a default-deny principle. If required authority
cannot be established: DENY is the required result. Examples include:
unknown Friend → deny

invalid binding → deny

invalid Session → deny

missing Save authority → no Commit

integrity failure → reject affected operation

# 11. Fail Closed

Security failure MUST NOT broaden access. If M-PIN cannot establish a
required security property, the affected operation MUST fail closed.
This includes uncertainty concerning: identity; authorization; Friend
Folder binding; Session validity; integrity; Save authority; recovery
authority; migration authority.

# 12. Friend Identity Security

A Friend MUST be verified sufficiently to distinguish it from other
Friends before Friend Folder access is granted. A display name alone
MUST NOT constitute sufficient security identity. Conceptually: Friend
claims: “I am Friend A” ↓ verification ↓ valid / invalid Only a valid
relationship may proceed.

# 13. Friend Impersonation

An attacker pretending to be Friend A MUST NOT obtain Friend Folder A
merely by supplying: Friend A’s name; Folder name; Folder identifier;
public service metadata; another unverified claim. Friend Folder access
MUST depend on the verified Friend relationship.

# 14. Friend Folder Binding Integrity

The association: Friend Identity A ↕ Friend Folder A is
security-sensitive. An attacker MUST NOT be able to modify unprotected
metadata to produce: Friend Identity B ↕ Friend Folder A without the
applicable legitimate authority.

# 15. Friend Folder Isolation

Friend Folder Isolation is a mandatory security property. Canonical
model: Friend A → Folder A Friend B → Folder B Friend C → Folder C The
following MUST be denied by default: Friend A → Folder B Friend A →
Folder C

# 16. Common Storage Does Not Mean Common Visibility

Multiple Friend Folders MAY reside within one M-PIN or physical Storage
environment. That physical co-location MUST NOT create shared Friend
visibility. Conceptually: M-PIN Storage ├── Folder A ├── Folder B └──
Folder C does not imply: Friend A can enumerate/read A+B+C

# 17. Zero Visibility

A Friend SHOULD receive no unnecessary visibility into unrelated Friend
relationships. This includes unnecessary exposure of: Folder names;
Folder identifiers; relationship metadata; payload metadata; Session
metadata. Zero Visibility supports privacy as well as access isolation.

# 18. Folder Discovery Privacy

A Friend SHOULD resolve its own Friend Folder through its verified
binding without receiving an unrestricted directory of all Friend
Folders. Conceptually: Verified Friend A ↓ resolve Folder A rather than:
Friend A ↓ enumerate all Owner relationships ↓ select Folder The exact
discovery mechanism is deferred.

# 19. Confidentiality

M-PIN Friend Folder Persistent State MUST be protected against
unauthorized disclosure. Confidentiality MUST apply to: unauthorized
Friends; unrelated Friends; unauthorized Devices; unauthorized Storage
access; unauthorized Provider operations; network attackers, according
to the applicable implementation boundaries.

# 20. Encryption at Rest

Persistent M-PIN Friend Folder state MUST be protected by encryption at
rest. The exact: encryption algorithm; cipher mode; key hierarchy; key
derivation; key storage; key rotation; key migration remain deferred. A
conforming implementation MUST use security mechanisms appropriate to
its actual deployment and threat model.

# 21. Encryption Does Not Define Ownership

Possession of an encryption key and architectural ownership are related
but distinct concepts. A key may be: rotated; migrated; recovered;
replaced through a legitimate process. The logical Owner and M-PIN
Identity need not change merely because cryptographic material changes.

# 22. Provider Plaintext Boundary

M-PIN v2 does not assume that every Provider implementation is
zero-knowledge. Whether a Provider can access plaintext depends on: key
architecture; execution location; storage design; recovery design;
deployment topology. Therefore the Core MUST NOT claim: Provider can
never see plaintext unless a specific implementation actually provides
and demonstrates that property.

# 23. Provider Authority Boundary

Even where a Provider can technically access infrastructure or
plaintext, Provider administrative capability MUST NOT automatically be
interpreted as legitimate Owner Authority. Technical capability and
architectural authorization are different.

# 24. Data in Transit

Where Friend Folder state or security-sensitive M-PIN data crosses an
untrusted transport, the implementation MUST protect it against
unauthorized observation and modification. The exact transport-security
protocol is deferred. The Core does not mandate one network technology.

# 25. Integrity

M-PIN MUST protect security-relevant state against unauthorized
modification. Protected integrity scope includes, where applicable:
Friend Folder Persistent State; Friend Folder binding; M-PIN identity
metadata; permission metadata; Session metadata; Save authorization;
migration state; recovery state.

# 26. Integrity Is Not Semantic Truth

Integrity means that data has not been accepted after unauthorized or
undetected modification under the applicable integrity model. It does
not prove that Friend-defined content is: factually correct; medically
correct; commercially correct; safe; unbiased; logically meaningful.
M-PIN integrity MUST NOT be represented as semantic certification.

# 27. Structural Validation

M-PIN MAY validate security-relevant structure necessary to preserve the
boundary. Examples include: identity association binding Envelope
structure integrity proof state generation format compatibility M-PIN
does not need to understand the complete Friend payload semantics.

# 28. Session Security

Friend access MUST occur through a valid bounded Synchronization
Session. The Session MUST be associated with the correct: M-PIN Friend
Friend Folder authorization context freshness context A Session MUST NOT
silently change its bound Friend or Folder.

# 29. One Active Friend Security

Within one authoritative active M-PIN continuity: \## only one Friend
may hold active M-PIN synchronization authority at a time. This reduces
simultaneous cross-context access and preserves the established M-PIN
interaction model. It does not imply that only one application process
may exist on the Device.

# 30. Session Termination

After Session termination, the terminated Session MUST NOT retain valid
M-PIN authority. Termination MAY occur because of: Owner action;
revocation; timeout; abnormal disconnect; dependency loss; security
failure; Friend switching.

# 31. Abnormal Disconnect

Loss of a required Session dependency MUST terminate the affected
Session when continued authority can no longer be safely maintained.
Historical USB removal is one concrete example. The generalized security
rule applies to any required dependency.

# 32. Disconnect Is Not Save

Security failure or disconnect MUST NOT create persistence authority.
disconnect ≠ Owner SAVE Unsaved Runtime changes MUST NOT be committed
merely to preserve convenience during failure.

# 33. Replay Threat

An attacker may attempt to reuse: old Session credentials; old Save
authorization; old recovery authorization; old migration authorization;
stale permission material. M-PIN MUST reject security-sensitive
authority outside its valid context.

# 34. Replay Resistance

A conforming implementation MUST provide sufficient replay resistance
for security-sensitive authority. Possible mechanisms MAY include:
nonces; counters; generations; timestamps; token rotation; revocation
state; integrity-protected freshness metadata. The exact mechanism is
deferred.

# 35. Session Reconnection

A terminated Session MUST NOT be revived merely because connectivity
returns. Reconnection requires a new valid Session. Conceptually:
Session 1 ↓ terminated

reconnect ↓ Session 2 Session 2 must establish current authority.

# 36. Save Authenticity

A proposed M-PIN persistence transition MUST be associated with valid
Owner Save authority. A Friend MUST NOT forge: Owner SAVE merely because
it controls Runtime State.

# 37. Save Scope

Save authority MUST apply to the active Friend’s own Friend Folder
persistence transition. It MUST NOT authorize: another Friend Folder;
cross-Friend state modification; M-PIN identity replacement; unrelated
migration; unrelated recovery.

# 38. Atomic Commit Security

Commit MUST be atomic from the perspective of authoritative M-PIN state.
The security-relevant outcomes are: valid State A ↓ valid State B or:
valid State A ↓ failure valid State A remains A partial attacker-induced
state MUST NOT become authoritative.

# 39. Crash and Interruption Threat

An attacker or failure may interrupt persistence at a sensitive moment.
A conforming implementation MUST prevent such interruption from silently
establishing corrupted partial state as authoritative. The exact
crash-safe mechanism is implementation-defined.

# 40. Unauthorized Save

If Save authority is missing, invalid, replayed, revoked, or bound to
the wrong Session: COMMIT MUST NOT PROCEED The previous valid Current
State remains authoritative.

# 41. Current-State Security

Current-State-Only reduces the Core requirement for accumulated M-PIN
version history. However, it MUST NOT be treated as a claim that no
temporary or Backup copies can physically exist. Temporary Commit
staging and protected Backups may exist where required. They MUST NOT
silently become unauthorized active states.

# 42. Backup Security

Backups MUST be protected according to the sensitivity of the Persistent
State they contain. A Backup MUST NOT become an alternate active
authority merely because it contains valid data. Restoration requires
valid recovery authority and freshness/integrity handling.

# 43. Stale Backup Threat

An attacker may attempt to restore an old valid Backup to undo:
revocation; permission changes; newer state; security configuration. A
conforming implementation SHOULD provide sufficient freshness or
recovery controls to prevent stale restoration from silently recreating
invalid authority. The exact mechanism is deferred.

# 44. Offline Clone Threat

Two fully disconnected valid copies may be unable to determine global
active-state uniqueness without coordination. M-PIN v2 does not claim
perfect global clone prevention in this condition. The frozen
requirement remains: one authoritative active continuity Strong globally
coordinated enforcement across disconnected clones is deferred.

# 45. Compromised Storage

An attacker controlling Storage may attempt to: read persistent data;
modify payload; replace binding metadata; roll back state; delete state;
corrupt state. M-PIN security therefore requires confidentiality and
integrity protections independent of assuming Storage is benign.
Availability after destructive Storage compromise depends on Backup and
recovery architecture.

# 46. Storage Deletion Threat

Encryption and integrity cannot prevent an attacker with sufficient
Storage control from deleting all accessible copies. M-PIN MUST NOT
claim otherwise. Data availability requires separate resilience and
Backup mechanisms.

# 47. Compromised Device

A compromised authorized Device may expose: decrypted Runtime data;
credentials; Session material; Owner interaction; locally accessible
M-PIN state. M-PIN v2 does not claim complete protection after total
endpoint compromise. The architecture limits exposure through bounded
authority, isolation, encryption at rest, revocation, Session controls,
and recovery.

# 48. Lost Device

Physical possession of a lost Device MUST NOT automatically establish
legitimate Owner Authority. The implementation SHOULD support
appropriate revocation and recovery. If an attacker also obtains valid
credentials or decrypted state, the security impact depends on the
implementation’s protection model.

# 49. Malicious Friend

A malicious Friend may intentionally attempt to: request excessive
access; impersonate another Friend; enumerate unrelated Folders; read
another Folder; forge Save authority; retain authorized plaintext; copy
data into its own infrastructure; misclassify synchronized data as
Service Records. M-PIN MUST enforce the M-PIN boundary even when the
Friend is not assumed benevolent.

# 50. Authorized Malicious Friend Limitation

If Friend A is legitimately authorized to receive plaintext from Friend
Folder A, M-PIN cannot guarantee that a malicious Friend A will not copy
or misuse that plaintext after receipt. Therefore: M-PIN can control
whether Friend A receives Folder A

M-PIN cannot guarantee what a malicious Friend A does with plaintext
already legitimately received This limitation is fundamental.

# 51. Compromised Friend Isolation

Compromise of Friend A MUST NOT automatically grant authority to: Friend
Folder B Friend Folder C all M-PIN state assuming the M-PIN security
boundary itself remains uncompromised. Friend Folder Isolation limits
the blast radius of a Friend compromise.

# 52. Friend Retention

M-PIN revocation controls future M-PIN authority. It cannot guarantee
retroactive deletion of plaintext already retained by a malicious or
compromised Friend. Any stronger deletion assurance requires additional
Friend-side guarantees outside the frozen Core.

# 53. Service Record Abuse

A Friend may attempt to bypass M-PIN by claiming that every synchronized
payload is an independent Service Record. This is prohibited by the
Service Record anti-loophole rule. A legitimate Service Record requires
an independently valid service, operational, contractual, institutional,
safety, security, or legal basis.

# 54. Service Record Security

Service Records are outside the Friend Folder persistence path, but they
remain subject to the Friend’s own applicable security obligations.
M-PIN does not automatically secure all independent Friend databases
merely because the Friend participates in M-PIN.

# 55. Malicious Provider

A malicious Provider may attempt to: inspect state; modify state; forge
permission; alter binding; impersonate Owner authority; redirect
migration; reactivate revoked access; corrupt recovery; deny
availability. M-PIN MUST NOT treat Provider infrastructure control as
proof of legitimate Owner authority.

# 56. Provider Compromise Limitation

The impact of Provider compromise depends on the implementation. If the
Provider controls plaintext keys, execution, and Storage, compromise may
have severe confidentiality and integrity consequences. If the
implementation separates those capabilities, the impact may be reduced.
M-PIN v2 freezes the authority boundary but does not invent a key
architecture that has not yet been specified.

# 57. Provider Lock-In Threat

A Provider may attempt to make Owner state practically non-portable.
Provider Independence requires that conforming architecture preserve the
possibility of migration/export of M-PIN continuity. Exact export format
and trust protocol remain deferred. Portability is treated further in
Core 11.

# 58. Network Attacker

A network attacker may attempt: interception; modification; replay;
redirection; downgrade; impersonation. Security-sensitive communication
over untrusted networks MUST use appropriate confidentiality, integrity,
authentication, and freshness protection. Exact protocols remain
deferred.

# 59. Downgrade Threat

An implementation MUST NOT silently downgrade required security
properties merely to establish compatibility. For example, failure to
verify a Friend MUST NOT be converted into: “continue without
verification” where verification is required. Compatibility failure MUST
fail closed for the affected security-sensitive operation.

# 60. Unauthorized Device Software

Authorization of a Device does not authorize every process on that
Device. Friend Identity and Session authority remain necessary. A
malicious local application MUST NOT obtain Friend Folder access merely
because it runs on an Owner-authorized Device.

# 61. Credential Theft

Stolen credentials may threaten Owner, Friend, Device, or Provider
authority depending on their scope. Implementations SHOULD limit
credential scope and support revocation or rotation where appropriate. A
credential SHOULD NOT grant broader authority than necessary for its
role.

# 62. Credential Rotation

Credential rotation MAY occur without changing the logical M-PIN
Identity where continuity can be securely established. Rotation MUST NOT
silently reset revoked permissions or Friend Folder bindings.

# 63. Recovery Threat

Recovery is security-sensitive because it may restore powerful Owner
authority. An attacker MUST NOT gain unrestricted M-PIN ownership merely
by invoking a recovery interface. Recovery MUST establish the applicable
recovery authority.

# 64. No Universal Recovery Backdoor

M-PIN v2 does not require a universal Provider, Friend, manufacturer, or
administrator backdoor capable of overriding Owner Authority. A bounded
recovery mechanism MAY exist. Its authority MUST be explicitly defined.

# 65. Authority Recovery vs Data Recovery

Security distinguishes: Authority Recovery ≠ Data Recovery Recovering
legitimate Owner Authority does not reconstruct missing data. Recovering
data does not automatically establish legitimate Owner Authority. Both
may be required.

# 66. Recovery Factor Loss

If all valid recovery factors, keys, and recoverable data are lost,
M-PIN does not promise magical recovery. Security MUST NOT be weakened
by a hidden universal bypass merely to guarantee recoverability.

# 67. Migration Threat

Migration may be attacked through: destination substitution; state
modification; stale-state activation; identity replacement; Friend
Folder rebinding; Provider impersonation. A conforming migration MUST
preserve identity, integrity, binding, and Owner authority.

# 68. Migration Is Not New Ownership

Successful migration from Device, Storage, or Provider A to B SHOULD
preserve: same M-PIN Identity same Owner continuity same Friend Folder
bindings valid Current State Migration MUST NOT silently transfer
ownership to the destination infrastructure operator.

# 69. Cross-Friend Disclosure Threat

Direct cross-Friend Folder access remains prohibited. A future
Owner-Mediated Disclosure mechanism would create additional threats
including: excessive disclosure; recipient impersonation; replay;
purpose mismatch; stale authorization; recipient persistence. Disclosure
remains deferred from Core.

# 70. Disclosure Security Constraint

If Disclosure is standardized later, it MUST NOT weaken the existing
rule: \## A Friend does not gain direct access to another Friend’s
Folder. Selected data transfer and Folder authority remain different
security concepts.

# 71. Profile Security

Profiles MAY add stronger security requirements appropriate to their
domain. Examples include: healthcare institutional authentication;
commerce payment authorization; robot physical safety controls; AI tool
authorization. A Profile MUST NOT weaken Core security invariants.

# 72. Healthcare Security Boundary

M-PIN Owner authentication does not automatically equal: Patient legal
identity proof; medical consent; clinician authorization; institutional
authorization. Healthcare systems MUST maintain the applicable
independent authority boundaries.

# 73. Commerce Security Boundary

M-PIN authorization does not automatically equal: payment authorization;
merchant contractual consent; age verification; fraud approval. Commerce
systems retain those independent security responsibilities.

# 74. Robotics Security Boundary

M-PIN is not a universal robot safety-control bus. M-PIN Session
authority does not automatically authorize physical action. Likewise,
Session termination does not universally define emergency-stop behavior.
Robot safety remains independently enforced.

# 75. AI Security Boundary

An AI Friend’s internal agent or tool MUST NOT receive greater M-PIN
authority than the Friend relationship provides. Friend Folder access
does not automatically authorize: external tool disclosure; model
training; cross-AI memory sharing; cross-Friend access.

# 76. Training Boundary

Authorization to use Friend Folder data during the Friend’s Runtime MUST
NOT automatically be interpreted as Owner authorization for unrelated
model training or other secondary use. Any such use requires an
independent lawful and authorized basis outside the mere existence of
M-PIN synchronization authority. M-PIN access itself is not universal
secondary-use consent.

# 77. Public and Shared Devices

On public or shared Devices, implementations SHOULD prevent residual
M-PIN data or Session authority from becoming available to later users.
Relevant controls MAY include: Session cleanup; transient data cleanup;
credential isolation; reauthentication; Device-specific security
measures. The exact mechanism is implementation-defined.

# 78. Logging

Security logging MAY be used for: authentication events; authorization
decisions; Session establishment/termination; Save/Commit outcomes;
recovery; migration; security failures. Logging SHOULD follow data
minimization.

# 79. Logging Anti-Archive Rule

Security logging MUST NOT become an undeclared archive of complete
Friend Folder payloads. A log MAY record that a Save occurred. It need
not duplicate the entire saved payload merely to prove that event. Where
payload logging is independently required by a legitimate Friend Service
Record obligation, that record must remain subject to the Service Record
boundary.

# 80. Audit Integrity

Where security audit metadata is relied upon for authorization,
recovery, or forensic integrity, it SHOULD be protected against
unauthorized modification. The exact audit mechanism is deferred.

# 81. Availability

M-PIN security includes availability considerations but does not
guarantee uninterrupted service. Threats include: Provider outage;
Storage loss; Device loss; denial-of-service; destructive attacker;
network failure. Portability and Backup can reduce dependence on one
infrastructure component. They cannot guarantee availability under every
failure scenario.

# 82. Denial of Service

M-PIN Core does not guarantee prevention of all denial-of-service
attacks. A malicious Friend or Provider MUST NOT receive additional data
authority merely because it can disrupt availability. Availability
failure and authorization failure remain distinct.

# 83. Security and Portability

Portability MUST NOT require disabling security. Migration/export SHOULD
preserve: confidentiality; integrity; M-PIN identity; Friend Folder
binding; Owner authority. A portable format that exposes all plaintext
without appropriate authorization would not satisfy the security model
merely because it is portable.

# 84. Security and Zero Requirement

Zero Requirement means M-PIN does not mandate one internal Friend
implementation. It does not mean: zero security requirements Friends
remain free internally, but their observable M-PIN-facing behavior MUST
satisfy Core security boundaries.

# 85. Friend Sovereignty and Security

Friend Sovereignty does not authorize a Friend to violate the M-PIN
boundary. The Friend controls: internal service implementation; Runtime;
UX; business logic. M-PIN controls whether M-PIN-owned persistent state
crosses the M-PIN access boundary under valid authority.

# 86. Threat Matrix

# 87. Mandatory Security Requirements

A conforming M-PIN v2 implementation MUST satisfy: \### SEC-001 —
Default Deny Missing or invalid required authority MUST result in
denial. \### SEC-002 — Friend Verification A Friend MUST be verified
before Friend Folder access. \### SEC-003 — Binding Integrity Friend
Identity and Friend Folder binding MUST be protected from unauthorized
reassignment. \### SEC-004 — Friend Folder Isolation One Friend MUST NOT
receive default access to another Friend’s Folder. \### SEC-005 —
Confidentiality Persistent Friend Folder state MUST be protected from
unauthorized disclosure. \### SEC-006 — Encryption at Rest Persistent
M-PIN Friend Folder state MUST be encrypted at rest. \### SEC-007 —
Integrity Unauthorized modification of security-relevant Persistent
State MUST NOT be silently accepted. \### SEC-008 — Session Boundary
Friend M-PIN access MUST occur through valid bounded Session authority.
\### SEC-009 — Replay Resistance Expired, revoked, terminated, or
otherwise invalid security-sensitive authority MUST NOT be accepted
through replay. \### SEC-010 — Save Authenticity M-PIN Commit MUST
require valid applicable Owner Save authority. \### SEC-011 — Atomic
Commit Partial or corrupted persistence transitions MUST NOT become
authoritative Current State. \### SEC-012 — Revocation Revoked M-PIN
authority MUST NOT remain valid for continued M-PIN access. \### SEC-013
— Provider Separation Provider administration MUST NOT automatically
equal Owner Authority. \### SEC-014 — Recovery Separation Recovery
authority MUST be explicitly distinguished from ordinary Friend or
Provider authority. \### SEC-015 — Migration Integrity Migration MUST
preserve applicable identity, binding, integrity, and Owner authority.
\### SEC-016 — No Silent Downgrade Required security properties MUST NOT
be silently bypassed for compatibility. \### SEC-017 — Service Record
Anti-Loophole Service Record classification MUST NOT be used to bypass
M-PIN persistence or isolation boundaries. \### SEC-018 — Fail Closed
Failure to establish a required security property MUST deny or terminate
the affected operation.

# 88. Recommended Security Properties

A conforming implementation SHOULD additionally provide: \### SEC-019 —
Folder Discovery Privacy Unrelated Friend Folder relationships SHOULD
not be exposed during Folder resolution. \### SEC-020 — Metadata
Minimization Security and Session metadata SHOULD be minimized. \###
SEC-021 — Credential Rotation Security credentials SHOULD support safe
rotation where appropriate. \### SEC-022 — Stale-State Protection
Recovery and migration SHOULD resist unauthorized stale-state
activation. \### SEC-023 — Shared-Device Cleanup Temporary M-PIN data
SHOULD be removed or isolated appropriately after use on shared Devices.
\### SEC-024 — Audit Integrity Security-relevant audit information
SHOULD be protected against unauthorized modification. \### SEC-025 —
Provider Portability Provider-based deployments SHOULD preserve a
practical path for secure Owner-authorized export or migration.

# 89. Security Claims M-PIN Does Not Make

M-PIN v2.0 MUST NOT be represented as guaranteeing: that an authorized
malicious Friend cannot retain plaintext; that every Provider is
zero-knowledge; that a totally compromised authorized Device remains
confidential; that deleted Storage can always be recovered; that
disconnected clones can always enforce global single-active state; that
integrity proves semantic correctness; that M-PIN authentication equals
legal identity; that M-PIN authorization equals medical, payment, or
contractual authorization; that M-PIN automatically makes a Friend
legally compliant; that M-PIN prevents every denial-of-service attack.
These limitations are part of the security specification.

# 90. Deferred Security Mechanisms

The following remain deferred: cryptographic algorithms cipher modes key
hierarchy key derivation key rotation protocol key migration protocol
Owner credential format Friend credential format Provider credential
format Device credential format Friend trust registry Provider trust
federation Session token format replay-proof encoding freshness
representation transport security protocol integrity-proof format backup
freshness protocol recovery-factor algorithm remote revocation mechanism
Their deferral does not reopen the frozen security boundaries.

# 91. Security Invariants

The Security & Threat Model is governed by these invariants: \##
Possession is not ownership. \## Authentication is not unrestricted
authorization. \## A Friend is verified before accessing its Folder. \##
One Friend’s authority does not grant another Friend’s authority. \##
Common storage does not create common visibility. \## Persistent state
is encrypted at rest. \## Unauthorized modification must not silently
become valid state. \## A terminated Session does not remain authorized.
\## Replay does not recreate expired authority. \## Runtime modification
does not create Save authority. \## Provider administration is not Owner
Authority. \## Recovery does not require a universal ownership backdoor.
\## Service Records cannot be used as an M-PIN bypass. An authorized
malicious Friend may retain its authorized plaintext; M-PIN does not
claim impossible retroactive control. \## Security uncertainty fails
closed.

# 92. Security Thesis

The complete M-PIN security model can be reduced to: OWNER │ Owner
Authority │ ▼ M-PIN │ ┌─────────────┼─────────────┐ │ │ │ ▼ ▼ ▼ Folder A
Folder B Folder C │ │ │ ▼ ▼ ▼ Friend A Friend B Friend C Only the
verified and authorized Friend crosses the boundary to its own Friend
Folder. The Friend may control its service. The Provider may operate
infrastructure. The Device may host execution. Storage may hold
encrypted state. But none of those facts alone create Owner Authority.
M-PIN does not make every external system trustworthy. It preserves the
boundary so that trust in one relationship does not automatically become
trust in every relationship.

## M-PIN v2.0 — Core 10 / Security & Threat Model

## Status: FROZEN
