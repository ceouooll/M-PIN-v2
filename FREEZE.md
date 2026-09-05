# M-PIN v2.0 Architecture Freeze

**Status:** FROZEN **Version:** M-PIN v2.0 **Scope:** Core
Architecture + Validation Profiles **Freeze Date:** September 2026

------------------------------------------------------------------------

## 1. Purpose

This document records the architecture freeze boundary of M-PIN v2.0.

The purpose of the freeze is to prevent completed architectural
decisions from being repeatedly reopened through new wording, additional
examples, new industries, or implementation preferences.

M-PIN v2.0 is considered architecturally complete when the requirements
and boundaries recorded below are preserved.

The freeze does not mean that M-PIN can never evolve.

It means:

> **v2.0 stops here.**

Compatible clarification belongs to a later minor version.

Architectural redesign belongs to a future major version.

------------------------------------------------------------------------

# 2. Frozen Core

M-PIN v2.0 Core consists of exactly twelve architecture documents.

``` text
core/

01-scope-and-design-constitution.md
02-core-principles.md
03-terminology.md
04-core-architecture.md
05-owner-and-identity.md
06-friend-and-friend-folder.md
07-permission-model.md
08-session-protocol.md
09-runtime-and-persistence.md
10-security-and-threat-model.md
11-portability-and-recovery.md
12-conformance-specification.md
For v2.0:
Core 01–12 = FROZEN
No additional Core document is required for the v2.0 architecture freeze.
```

# 3. Frozen Profiles

M-PIN v2.0 includes four validation Profiles. profiles/

01-ai.md 02-robotics.md 03-healthcare.md 04-commerce.md Their purpose is
to demonstrate that the same industry-neutral M-PIN Core can be applied
across materially different environments. For v2.0: AI = FROZEN Robotics
= FROZEN Healthcare = FROZEN Commerce = FROZEN Additional industries are
not required for v2.0 completion.

# 4. Canonical Core

The frozen architecture is centered on: Owner M-PIN Friend Friend Folder
Permission Session Runtime Persistence Security Portability Recovery
Conformance An M-PIN Service Provider may exist as an
implementation/deployment role. It is not the architectural Owner.

# 5. Canonical Relationship

The basic M-PIN relationship is: OWNER │ Owner Authority │ ▼ M-PIN │
┌───────────────────┼───────────────────┐ │ │ │ Friend Folder A Friend
Folder B Friend Folder C │ │ │ ▼ ▼ ▼ Friend A Friend B Friend C │ │ │
Runtime Runtime Runtime │ │ │ Native UX Native UX Native UX The M-PIN
Core remains centered on the Owner.

# 6. Frozen Ownership Rule

The persistent Owner-controlled state belongs under Owner authority.
Friend provides service.

Owner owns Owner-controlled persistent M-PIN data.

M-PIN preserves the ownership boundary. This is a frozen architectural
principle.

# 7. Frozen Friend Rule

A Friend remains sovereign over its own service. M-PIN does not control
the Friend’s: business model service policy native UX runtime internal
implementation internal algorithms product evolution data semantics
M-PIN controls the boundary of access to Owner-controlled M-PIN state.

# 8. Frozen Friend Folder Rule

The official v2 Core entity is: \## Friend Folder The canonical
relationship is: \## One Friend, One Friend Folder. A Friend Folder is
an Owner-owned persistent data area associated with a particular Friend.
A Friend does not receive default access to another Friend’s Folder.

# 9. Domain Resolution

A separate Domain entity is not part of the v2.0 Core. Historical v1
uses of Domain terminology remain part of the historical record. They
must not be used to recreate a second data-area abstraction alongside
Friend Folder in v2.0. Friend-specific persistent area ↓ Friend Folder
is the v2 terminology.

# 10. Frozen Synchronization Rule

The canonical synchronization relationship is: \## One M-PIN, One Active
Friend, One Synchronization Session. The standard flow is: Owner
initiates synchronization ↓ M-PIN authentication ↓ Friend identity
verification ↓ Friend Folder resolution ↓ Owner authorization ↓
Synchronization Session ↓ Current saved state loaded ↓ Friend Runtime If
the Friend Folder does not exist, its creation requires Owner approval.

# 11. Frozen Native Experience Rule

M-PIN does not replace the Friend workspace. The Friend continues to use
its existing Runtime and native UX. M-PIN ↓ Synchronization ↓ Friend
Runtime ↓ Friend Native UX M-PIN compatibility does not require a new
universal M-PIN application interface for all Friends.

# 12. Frozen Runtime Rule

Runtime State is temporary relative to M-PIN persistent state.
Persistent State ↓ LOAD Runtime State ↓ Friend processing Runtime
activity alone does not modify M-PIN Persistent State.

# 13. Frozen Persistence Rule

The canonical persistence flow is: Persistent State A ↓ LOAD Runtime
State A ↓ WORK Runtime State B ↓ OWNER SAVE Commit ↓ Persistent State B
Without Owner Save: Persistent State A ↓ Runtime State B ↓ NO SAVE ↓
Session End ↓ Persistent State A Therefore: \## Runtime Change ≠
Persistent Change is frozen.

# 14. SAVE and COMMIT

v2.0 distinguishes: SAVE = Owner’s persistence intent

# COMMIT

technical application of the authorized persistence change A Friend may
request or present a Save action. It may not silently replace Owner
persistence authority.

# 15. Current State Only

M-PIN v2.0 Core preserves the current committed state. The Core does not
require: historical version timeline automatic snapshots rollback
history time travel perpetual archive This does not prohibit protected
backup copies of the current state. Backup and version history are
different concepts.

# 16. Atomic Persistence

A failed Commit must not be accepted as a valid partially written
Current State. Conceptually: A → B

or

A → A not: A → corrupted partial B Atomic Commit is part of the v2
persistence requirement.

# 17. Frozen Permission Boundary

M-PIN access is based on Owner authority. A Friend’s service need does
not itself create permission. Friend wants data ≠ Friend has authority
Authorization must remain bounded by: Friend identity Friend Folder
Session scope Owner authority

# 18. Frozen Isolation Rule

The existence of multiple Friend Folders inside one M-PIN does not
create shared visibility. M-PIN

├── Friend A Folder ← Friend A ├── Friend B Folder ← Friend B └── Friend
C Folder ← Friend C By default: Friend A X Friend B Folder This remains
frozen.

# 19. Frozen Security Boundary

v2.0 requires security appropriate to the M-PIN ownership boundary,
including: protected persistent-state encryption authentication
authorization Friend identity verification Friend Folder isolation
session revocation integrity protection unauthorized Save prevention
fail-closed behavior Exact cryptographic algorithms are not frozen by
the architecture.

# 20. Security Non-Claim

M-PIN does not claim that an authorized but malicious Friend can never
copy plaintext that it legitimately receives during an authorized
Runtime. Once a Friend is legitimately permitted to process plaintext,
M-PIN cannot guarantee control over every action inside a fully
compromised Friend implementation. The architecture limits authority and
exposure. It does not claim impossible control over an authorized
hostile runtime.

# 21. Frozen Device Independence

M-PIN Identity is not tied to one physical device. Device A ↓ same M-PIN

Device B ↓ same M-PIN Device replacement does not inherently create a
new M-PIN.

# 22. Frozen Provider Independence

M-PIN v2.0 distinguishes: M-PIN Standard ≠ M-PIN Service Provider A
Provider may implement M-PIN services. The M-PIN Standard itself is not
defined as the proprietary internal architecture of one required
Provider. Provider migration should preserve the same M-PIN continuity
where technically supported by a conforming implementation.

# 23. Provider Is Optional

The v2 Core does not require all M-PIN deployments to depend on a
permanent centralized Provider. Conceptually valid deployment models may
include: provider-hosted Owner-managed local storage Owner-controlled
cloud storage removable storage other conforming environments The
architecture is defined by behavior rather than one deployment topology.

# 24. Frozen Portability Goal

Changing: Device Storage Location M-PIN Service Provider should not
inherently require creation of a new Owner or new M-PIN identity.
Portability preserves continuity.

# 25. Frozen Recovery Goal

Recovery means restoring legitimate authority to the same M-PIN where
possible. M-PIN distinguishes: Authority Recovery ≠ Data Recovery If all
actual data copies are destroyed, authentication recovery alone cannot
reconstruct the missing data.

# 26. Single Active Continuity

M-PIN may have protected backup copies. That does not mean all copies
may independently act as authoritative active M-PIN instances. The
frozen logical invariant is: multiple protected copies MAY exist

one authoritative active continuity MUST be maintained

# 27. Offline Clone Limitation

v2.0 does not claim that two completely disconnected offline clones can
always be prevented from independently considering themselves active
without any coordination mechanism. Therefore: Single Active is a
normative continuity requirement, not an unsupported claim of globally
perfect offline clone prevention. A stronger enforcement mechanism may
be specified in a future version or implementation profile.

# 28. Frozen Service Record Boundary

v2.0 distinguishes: Owner-controlled M-PIN State ≠ Friend Service Record
Examples of Friend Service Records may include: clinical records
transaction records billing records safety records regulatory records
security records where legitimate service, institutional, or legal
obligations require them.

# 29. Service Record Is Not a Loophole

The Service Record distinction does not mean: Friend may copy all M-PIN
data and call it a Service Record Service Records remain limited to the
Friend’s legitimate independent service responsibilities.

# 30. Frozen Conformance Principle

M-PIN compatibility is based primarily on required observable behavior.
It is not based on mandatory use of one: SDK API language database
runtime cloud provider operating system This preserves Friend
implementation autonomy.

# 31. Zero Requirement

A Friend does not become conformant because it uses a particular
M-PIN-branded technology. It becomes conformant by satisfying the
required behavioral boundaries. This is the frozen Zero Requirement
principle.

# 32. Profile Rule

A Profile may add domain-specific requirements. A Profile must not
weaken the Core. For example: Healthcare requirement X cannot grant
universal access to all Healthcare Friend Folders and: Commerce
requirement X cannot make transaction approval equivalent to M-PIN SAVE

# 33. AI Profile

The AI Profile is frozen as validation that the Core can support AI
services without making M-PIN: an AI model an AI runtime a universal AI
memory pool an agent framework AI remains a Friend.

# 34. Robotics Profile

The Robotics Profile is frozen as validation that Owner continuity can
remain independent of a specific physical robot. The Profile does not
make M-PIN: a robot operating system a motor controller a navigation
system a physical safety controller Robot safety remains independent.

# 35. Healthcare Profile

The Healthcare Profile is frozen with the boundary: Owner M-PIN Health
State ≠ Institutional Medical Record M-PIN does not become an EHR,
medical authority, or medical regulator.

# 36. Commerce Profile

The Commerce Profile is frozen with the boundary: Owner Commerce State ≠
Merchant Transaction Record and: Payment authorization ≠ M-PIN SAVE
authorization M-PIN does not become a marketplace, payment network, or
merchant accounting system.

# 37. Cross-Profile Finding

Healthcare and Commerce both revealed a need for selected information to
move between otherwise isolated Friend relationships. The candidate
model is: \## Owner-Mediated Disclosure Conceptually: Friend A │
selected data ▼ Owner │ explicit authorization ▼ Disclosure │ ▼ Friend B

# 38. Disclosure Status

For v2.0: Owner-Mediated Disclosure = V2-NEW CROSS-PROFILE FINDING
CANDIDATE DEFERRED FROM CORE The concept is recorded. Its exact
normative protocol and schema are not frozen as part of Core 01–12.

# 39. Disclosure Does Not Weaken Isolation

Even if a future Disclosure mechanism is standardized: Disclosure ≠
Cross-Friend Folder Access Friend Folder Isolation remains the baseline.
This constraint is frozen.

# 40. v1 Open Decision 095

The v2 architectural disposition is: Owner SAVE ↓ Friend supplies the
persistent state for its Friend Folder ↓ M-PIN validates required
structural/ authority/integrity conditions ↓ Commit M-PIN does not need
to understand the Friend’s semantic data model. Disposition: RESOLVED
for v2 architecture. The exact delta/full-state encoding strategy is an
implementation matter unless later interoperability requirements
demonstrate otherwise.

# 41. v1 Open Decision 120

The v2 architectural disposition is: Friend payload semantics = Friend
responsibility

minimum M-PIN envelope / identity / integrity structure = M-PIN
responsibility Disposition: RESOLVED IN PRINCIPLE. Exact container and
serialization schema remain deferred.

# 42. Deferred Technical Decisions

The following are intentionally not frozen as architecture-level
implementation choices: exact .MPIN binary/container format
serialization format cryptographic algorithm suite key hierarchy key
rotation protocol key migration protocol recovery-factor implementation
recovery-threshold algorithm Friend credential format Session token
representation heartbeat interval transport protocol Provider discovery
mechanism Provider trust mechanism integrity-proof representation
freshness-counter implementation backup freshness mechanism Disclosure
protocol/schema strong offline single-active enforcement These do not
automatically reopen the v2.0 Core.

# 43. Deferred Does Not Mean Forgotten

DEFERRED means: the architecture boundary is known

but

the exact implementation choice is intentionally not fixed in v2.0 A
deferred item may be addressed by: reference implementation
implementation profile v2.1 future protocol specification v3 depending
on whether it changes the architecture.

# 44. Out of Scope

The following are not required for the M-PIN v2.0 Architecture Freeze:
production server mobile application commercial cloud service hardware
product hospital deployment robot deployment payment integration global
Friend registry certification authority patent filing commercial
licensing model Their absence does not make the v2 architecture
incomplete.

# 45. External Systems

External technologies may be compared with M-PIN. They do not become
part of the frozen M-PIN architecture merely through comparison.
External comparison must not silently alter v1 provenance or v2
normative requirements.

# 46. Freeze Change Rule

A new idea is not sufficient reason to reopen v2.0. The frozen Core
should be reconsidered only if one of the following is demonstrated:
actual internal contradiction

security defect

implementation impossibility

conformance ambiguity that prevents independent implementation

requirement that cannot be represented without violating the existing
Core

# 47. What Does Not Reopen v2.0

The following alone do not justify reopening Core: new industry example
new company new device new AI model new robot new cloud provider
alternative implementation preference different terminology preference
additional business model These should first be tested against the
existing architecture.

# 48. No Repeated LOCK Questions

A previously resolved architectural issue must not be reopened merely by
changing the wording of the question. The process rule is: Already
LOCKED? ↓ YES Does new evidence show: contradiction / security flaw /
implementation impossibility? ↓ NO Do not reopen. This rule exists to
preserve a finite specification process.

# 49. Version Rule

After v2.0 publication: clarification that preserves architecture ↓ v2.1

new optional implementation mechanism ↓ implementation/profile extension
or v2.x

architectural change ↓ v3 v2.0 itself remains the frozen historical
specification.

# 50. Publication Integrity

After public release, corrections should be transparent. Do not silently
rewrite the historical meaning of v2.0. If a correction is required:
identify issue ↓ record correction ↓ version appropriately ↓ preserve
previous public history

# 51. Definition of Done

M-PIN v2.0 Architecture satisfies its completion criteria when: \[✓\]
Core scope fixed \[✓\] twelve Core documents defined \[✓\] terminology
fixed \[✓\] Owner model defined \[✓\] Friend model defined \[✓\] Friend
Folder model defined \[✓\] permission boundary defined \[✓\] Session
model defined \[✓\] Runtime/Persistence separation defined \[✓\]
Owner-controlled persistence defined \[✓\] security/threat boundary
defined \[✓\] portability defined \[✓\] recovery defined \[✓\]
behavioral conformance defined \[✓\] AI Profile validated \[✓\] Robotics
Profile validated \[✓\] Healthcare Profile validated \[✓\] Commerce
Profile validated \[✓\] provenance separated \[✓\] v1 open architecture
issues dispositioned \[✓\] implementation details explicitly deferred
\[✓\] architecture growth stopped

# 52. Architecture Status

M-PIN v2.0

Core 01–12 FROZEN

Profiles 01–04 FROZEN

Owner-Mediated Disclosure CANDIDATE / DEFERRED

Implementation Details DEFERRED

Production Implementation OUT OF SCOPE

Future Architecture v2.1 / v3

# 53. Freeze Declaration

M-PIN v2.0 Core consists of twelve normative architecture documents and
four validation Profiles. The v2.0 architecture is frozen at this
boundary. New industries, implementation techniques, or product ideas
shall not automatically reopen the Core. The Core should be reconsidered
only when an actual contradiction, security defect, implementation
impossibility, or material conformance ambiguity is demonstrated.

# 54. Korean Freeze Declaration

M-PIN v2.0 Core는 12개의 핵심 문서와 4개의 검증 Profile로 구성하며, 이
경계에서 v2.0 Architecture를 동결한다. 새로운 산업 사례·제품
아이디어·구현 방식이 등장했다는 이유만으로 v2.0 Core를 다시 열지 않는다.
실제 모순, 보안 결함, 구현 불가능성 또는 독립 구현을 방해하는 중대한
적합성 모호성이 확인되는 경우에만 후속 버전에서 재검토한다.

# 55. Final Rule

## Finish the version before expanding the architecture.

M-PIN v2.0 is therefore: ARCHITECTURALLY COMPLETE

and

FROZEN

## M-PIN v2.0 — Architecture Freeze Record
