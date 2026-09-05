# M-PIN v2.0

## Core 12 — Conformance Specification

**Status:** FROZEN **Version:** 2.0 **Document Type:** Normative Core
Specification

------------------------------------------------------------------------

# 1. Purpose

This document defines conformance requirements for M-PIN v2.0.

It specifies:

- what it means to claim M-PIN Core conformance;
- which architectural behaviors are mandatory;
- how Friend, M-PIN, Provider, Device, and Storage implementations are
  evaluated;
- which failures invalidate conformance;
- how Profiles extend Core;
- how negative tests are used;
- which deferred implementation mechanisms do not block architectural
  conformance.

M-PIN conformance is behavioral.

It is not defined by use of one programming language, cloud, SDK, API,
database, operating system, transport, or cryptographic library.

------------------------------------------------------------------------

# 2. Conformance Thesis

The canonical rule is:

> **An implementation conforms to M-PIN when its observable behavior
> preserves the frozen M-PIN Core boundaries.**

Conformance is therefore determined by behavior such as:

``` text
Who owns persistent continuity?
Which Friend may access which Folder?
When does Runtime become Persistent State?
What happens when Owner does not Save?
What happens when a Session ends?
Can Provider or Device authority silently become Owner authority?
Can M-PIN continuity move without changing ownership?
The internal implementation is not the primary conformance criterion.
```

# 3. Normative Language

The key words: MUST MUST NOT REQUIRED SHOULD SHOULD NOT MAY are used as
normative terms. MUST and MUST NOT define mandatory conformance
behavior. SHOULD and SHOULD NOT define recommended behavior that may be
departed from only with a justified implementation reason that does not
violate a mandatory Core invariant. MAY defines permitted implementation
freedom.

# 4. Scope of Conformance

M-PIN v2 Core conformance applies to the architectural behavior defined
in Core 01–12. It does not certify: overall product security; legal
compliance; medical safety; payment compliance; AI quality; robot
safety; business reliability; absence of implementation bugs. Those may
require additional standards, testing, or Profile requirements.

# 5. Conformance Classes

M-PIN v2 recognizes architectural conformance across implementation
roles. A deployment may include: M-PIN Implementation Friend
Implementation Provider Implementation Device Environment Storage
Environment Profile Implementation Not every deployment requires a
separate Provider. Conformance responsibilities depend on the role being
claimed.

# 6. Core-Conformant M-PIN Implementation

A Core-conformant M-PIN implementation MUST preserve the mandatory Core
behaviors relating to: Owner authority; Friend identity and binding;
Friend Folder isolation; bounded Sessions; Runtime/Persistence
separation; Owner-controlled Save; Atomic Commit; Current-State-Only;
security boundaries; portability; recovery; Provider optionality.

# 7. Core-Conformant Friend

A Core-conformant Friend MUST be able to participate in the M-PIN
relationship without violating Friend Sovereignty or Owner Data
Sovereignty. At minimum, the Friend MUST: identify itself sufficiently
for M-PIN binding; operate only against its authorized Friend Folder;
load applicable persistent state through an authorized Session; use that
state in its own Runtime and native UX; preserve the distinction between
Runtime State and M-PIN Persistent State; permit Owner-controlled M-PIN
Save behavior; not treat Friend internal autosave as M-PIN Save; not
access unrelated Friend Folders; not delegate M-PIN authority to another
Friend without explicit future protocol support; preserve applicable
Session termination behavior.

# 8. Friend Conformance Does Not Require Internal Redesign

A Friend does not fail conformance merely because it uses its own:
database; Runtime; UX; account model; internal cache; service
architecture; payload schema; business logic. This follows the Zero
Requirement principle. Conformance concerns the M-PIN-facing boundary.

# 9. No Required SDK

M-PIN v2 Core MUST NOT require one official SDK for conformance. An
implementation MAY use: native code; web protocol; local interface;
cloud interface; removable media; another compatible mechanism. The
observable behavior must remain conformant.

# 10. No Required API Style

M-PIN v2 does not require: REST; GraphQL; RPC; WebSocket; local IPC;
filesystem API; one proprietary protocol. Protocol shape is deferred.
Core semantics are normative.

# 11. No Required Deployment Topology

A conforming deployment MAY be: local-only or: Provider-hosted or:
hybrid or another compatible architecture. A mandatory Provider is not
required.

# 12. No Required Storage Medium

A conforming M-PIN MAY use: local disk; removable storage; cloud
storage; Provider storage; another compatible persistent medium. The
storage mechanism must satisfy the applicable Core security and
persistence properties.

# 13. Owner Conformance Principle

A conforming implementation MUST preserve Owner authority over M-PIN
Persistent State. At minimum: Friend need MUST NOT create Owner
Authority; Device possession MUST NOT create Owner Authority; Provider
administration MUST NOT create Owner Authority; Friend Account ownership
MUST NOT silently replace M-PIN ownership.

# 14. Friend Folder Conformance Principle

A conforming implementation MUST preserve: \## One Friend, One Friend
Folder. This means a continuing Friend relationship resolves to its
associated Friend Folder and does not receive default access to
unrelated Friend Folders.

# 15. Friend Folder Is Not Shared Pool

The following architecture is non-conformant: M-PIN ↓ shared Owner
memory pool ↓ all Friends may read by default unless all such data is
independently modeled under a future explicit Core mechanism. M-PIN v2
Core requires Friend-specific isolation.

# 16. Domain Conformance Rule

A conforming v2 implementation MUST NOT require a separate normative
Domain entity between M-PIN and Friend Folder. Historical v1 Domain
terminology may appear in provenance or compatibility documentation. It
MUST NOT redefine the frozen v2 architecture.

# 17. First Synchronization Conformance

When a Friend has no existing Friend Folder, a conforming implementation
MUST: verify applicable Owner authority ↓ verify Friend identity ↓
determine Folder absent ↓ request required Owner approval ↓ create
Folder only if approved Silent first-Folder creation without required
Owner authority is non-conformant.

# 18. Returning Synchronization Conformance

A returning Friend with an existing valid relationship MUST resolve and
reuse its existing Friend Folder. A new Friend Folder MUST NOT be
silently created for every Session.

# 19. Arbitrary Folder Selection Test

A conforming implementation MUST reject a Friend attempting to select an
unrelated Friend Folder merely by name, path, or identifier. Example:
Friend A ↓ requests Folder B ↓ DENY unless a future explicit
interoperability protocol authorizes a different operation.

# 20. Friend Folder Discovery Conformance

A Friend SHOULD be able to resolve its own Folder through its verified
relationship. The implementation SHOULD NOT require exposure of
unrelated Friend Folder metadata merely to perform discovery. This is a
recommended privacy property.

# 21. Friend Semantic Authority

A conforming Friend remains responsible for interpreting its own payload
semantics. M-PIN MUST NOT require universal semantic knowledge of every
Friend payload.

# 22. Decision 120 Conformance Rule

M-PIN v2 conformance requires the following responsibility boundary:
Friend: payload meaning service-specific payload structure semantic
evolution

M-PIN: minimum required boundary metadata identity and binding
authorization integrity persistence boundary The exact binary/container
schema is deferred. Therefore architectural conformance can be evaluated
before a final universal .MPIN serialization is standardized.

# 23. Runtime Conformance

A conforming implementation MUST distinguish: Friend Runtime State from:
M-PIN Persistent State The existence of changed Runtime State MUST NOT
itself redefine the Friend Folder Current State.

# 24. Load Conformance

A Friend MAY load its current authorized Friend Folder state only within
a valid applicable Session. Load MUST NOT expose unrelated Friend Folder
state.

# 25. Read Once Conformance

A conforming implementation MUST preserve the semantic meaning of Read
Once: Friend access is bounded by the authorized Session and does not
become perpetual unrestricted M-PIN access. Read Once MUST NOT be
interpreted as requiring exactly one physical I/O operation. Streaming
or chunked transfer may conform.

# 26. Save Conformance

A conforming implementation MUST preserve: Owner SAVE ≠ Friend internal
autosave M-PIN Persistent State MUST NOT change merely because a Friend:
autosaves; updates internal memory; writes a draft; completes a
transaction; closes; disconnects.

# 27. Save/Commit Conformance

A conforming implementation MUST distinguish: SAVE = Owner persistence
intent from: COMMIT = successful technical persistence transition An
unsuccessful Commit MUST NOT be represented as successful Save
completion.

# 28. Decision 095 Conformance Rule

The semantic result of a successful Save MUST be: one valid current
Friend Folder state The implementation MAY use: full state; delta;
transaction; chunked state; another conforming representation.
Conformance does not require one transfer strategy. It requires that the
authoritative semantic result be exactly one valid Current State.

# 29. Atomic Commit Conformance

A conforming Commit MUST have one of two authoritative outcomes: State A
→ valid State B or: State A → State A on failure. A partially committed
corrupted state MUST NOT become authoritative.

# 30. No-Save Conformance

The following test MUST pass: Current State A ↓ Load ↓ Runtime changes
to B ↓ Owner does not Save ↓ Session terminates ↓ Current State A
remains If B becomes M-PIN Persistent State anyway, the implementation
is non-conformant.

# 31. Disconnect Conformance

Disconnect MUST NOT imply Save. The following behavior is required:
unsaved Runtime changes + disconnect ↓ no automatic M-PIN Commit unless
the relevant Commit had already completed successfully before
disconnect.

# 32. Friend Switching Conformance

Switching from Friend A to Friend B MUST NOT automatically Save Friend
A’s unsaved Runtime State. The active Friend A Session must terminate
before Friend B becomes the active M-PIN Friend.

# 33. Multiple Save Conformance

A Session MAY perform multiple Saves. Each successful Commit replaces
the authoritative Current State. Example: A → Save → B → Save → C
Current State becomes C. The Core does not require A and B to remain as
M-PIN version history.

# 34. Current-State-Only Conformance

A conforming implementation MUST NOT require Core-level historical state
navigation or rollback. It MAY maintain protected Backup or temporary
Commit staging. Those MUST remain distinguishable from ordinary active
version-history semantics.

# 35. Historical Payload Content Conformance

An implementation MUST NOT reject a Friend payload merely because the
current payload contains historical service content. Examples include:
old AI conversations; past orders; prior receipts; health documents. The
rule is: historical content in current payload is allowed while:
mandatory M-PIN version history is not Core

# 36. Backup Conformance

A Backup MAY exist. A Backup MUST NOT automatically become: a second
active M-PIN; a second active Owner authority; an active Synchronization
Session. Restoration requires the applicable recovery process.

# 37. Service Record Conformance

A Friend MAY maintain legitimate independent Service Records.
Conformance requires that Service Records remain distinguishable from
Owner-controlled Friend Folder persistence.

# 38. Service Record Anti-Loophole Test

A Friend is non-conformant if it uses the following pattern merely to
evade M-PIN persistence: load complete Friend Folder ↓ copy full payload
↓ store permanently ↓ rename copy “Service Record” without an
independently legitimate service, operational, contractual,
institutional, safety, security, or legal basis.

# 39. Session Conformance

A conforming Friend M-PIN interaction MUST occur through a bounded
Synchronization Session. At minimum the protocol must preserve the
semantics of: no active Session ↓ Owner authority ↓ Friend verification
↓ Folder resolution ↓ new Session ↓ Load ↓ Active ↓ Save or No Save ↓
Termination Internal state names may differ.

# 40. One Active Friend Conformance

Within one authoritative active M-PIN continuity: \## only one Friend
may hold active M-PIN synchronization authority at a time. A deployment
that allows simultaneous active Friend A and Friend B M-PIN
synchronization authority over the same authoritative continuity is
non-conformant with v2.0 Core.

# 41. One Active Friend Is Not One Running App

This requirement MUST NOT be interpreted as requiring every other
application on the Device to stop running. The restriction concerns
active M-PIN synchronization authority.

# 42. Session Termination Conformance

A terminated Session MUST lose valid M-PIN authority. The Friend MUST
NOT continue using the terminated Session to: read Friend Folder state;
Commit new state; obtain new M-PIN data.

# 43. Reconnection Conformance

A terminated Session MUST NOT be revived merely because connectivity
returns. Reconnection requires establishment of new valid Session
authority.

# 44. Replay Conformance

A conforming implementation MUST reject replay of: terminated Session
authority; expired Session authority; revoked Save authority; stale
migration authority; invalid recovery authority where the replay would
recreate authority outside its valid context. Exact replay mechanism is
implementation-defined.

# 45. Revocation Conformance

When applicable Owner authority is revoked: continued M-PIN access under
that authority MUST cease Revocation does not require deletion of:
Friend Account; Friend Folder; Service Record; already legitimate
plaintext copies held by a malicious Friend.

# 46. Cross-Friend Conformance

The following MUST fail by default: Friend A → Folder B Friend B →
Folder A The Friend’s business need does not change this rule.

# 47. Same Company Conformance

Two distinct Friends operated by the same company MUST NOT automatically
share Friend Folder authority. Conformance is based on Friend
relationship and binding, not corporate ownership.

# 48. Same Device Conformance

Two distinct Friends on the same Device MUST remain isolated under M-PIN
authority. Device co-location MUST NOT collapse Friend Folder
boundaries.

# 49. Same Provider Conformance

Two Friends using the same Provider MUST remain isolated unless
independently authorized by a future explicit mechanism. Provider
co-location is not Friend authorization.

# 50. Provider Optionality Conformance

A claim that M-PIN inherently requires one specific Provider is
inconsistent with v2.0 Core. A Provider-based implementation may still
conform if it preserves the provider-neutral architecture and applicable
portability requirements.

# 51. Provider Authority Conformance

Provider administrative privileges MUST NOT automatically authorize:
Owner Save; Friend Folder reassignment; cross-Friend access; M-PIN
ownership transfer; unrestricted recovery. If an implementation grants
such authority, it must be explicitly defined under a legitimate
authorized role.

# 52. Provider Plaintext Conformance

M-PIN v2 does not require every Provider to be zero-knowledge. Therefore
Provider plaintext visibility alone does not determine Core conformance.
However, Provider access MUST remain consistent with the
implementation’s declared trust/security architecture and MUST NOT
silently become Owner or Friend authority.

# 53. Encryption-at-Rest Conformance

Persistent Friend Folder state MUST be encrypted at rest. An
implementation that stores ordinary persistent Friend Folder plaintext
without an applicable protective encryption layer is non-conformant with
Core 10. Exact encryption mechanisms are outside v2.0 architectural
conformance.

# 54. Integrity Conformance

A conforming implementation MUST detect or prevent unauthorized
modification of security-relevant M-PIN Persistent State from being
silently accepted as valid. Exact integrity algorithm is deferred.

# 55. Fail-Closed Conformance

If required identity, authorization, Session, binding, integrity, or
Save authority cannot be established, the affected security-sensitive
operation MUST fail closed. Fail-open behavior on a mandatory security
check is non-conformant.

# 56. Device Independence Conformance

A conforming M-PIN architecture MUST NOT define one permanent Device as
the sole architectural Owner. M-PIN continuity MAY move to another
compatible Device through valid migration or recovery.

# 57. Storage Independence Conformance

A conforming architecture MUST NOT require one permanent physical
Storage location as the definition of M-PIN identity. Storage may change
while M-PIN continuity remains the same.

# 58. Provider Independence Conformance

A Provider-based deployment SHOULD support practical Owner-authorized
migration/export sufficient to avoid architectural Provider ownership. A
deployment whose only possible model is: Provider disappears ↓ M-PIN
identity and ownership necessarily cease because the Provider is defined
as the architectural Owner conflicts with Provider Independence. Loss of
all data/keys is a separate recovery limitation and does not itself
prove architectural non-conformance.

# 59. Provider Migration Conformance

A valid Provider migration SHOULD preserve: M-PIN Identity; Owner
continuity; Friend Folder relationships; valid Current State; required
integrity/binding metadata. Provider migration MUST NOT silently become
Friend migration.

# 60. Migration Conformance

Migration MUST require applicable Owner authority and preserve the
relevant identity/binding/integrity properties. Migration MUST NOT
silently transfer ownership to the destination Provider or Device.

# 61. Active Session Migration Conformance

Core does not require live Session migration. The following is
conformant: terminate old Session ↓ migrate continuity ↓ establish new
Session An implementation need not preserve an active Session across
migration.

# 62. Recovery Conformance

A conforming recovery design MUST distinguish: Authority Recovery from:
Data Recovery Possessing data does not automatically prove Owner
Authority. Recovering Owner Authority does not recreate missing data.

# 63. No Universal Backdoor Conformance

M-PIN Core MUST NOT require a universal Provider, Friend, manufacturer,
or administrator override capable of silently assuming Owner ownership.
A specific bounded recovery system MAY exist. It must be explicitly
defined.

# 64. Recovery and Revocation Conformance

Restoring an old Backup MUST NOT blindly reactivate stale revoked
authority where the implementation has the information necessary to
detect that the authority is stale. Recovery SHOULD preserve revocation
and freshness safety. Exact mechanism remains deferred.

# 65. Recovery and External State Conformance

A conforming implementation MUST NOT represent M-PIN recovery as
automatic reversal of external Service Records or real-world events.
Examples: recover older Commerce payload ≠ reverse purchase

recover older Healthcare payload ≠ erase hospital record

recover older Robot payload ≠ undo physical action

# 66. Offline Clone Conformance

M-PIN v2 conformance does not require impossible global coordination
between fully disconnected clones. An implementation MUST nevertheless
preserve the architectural concept of one authoritative active
continuity. If a product claims stronger disconnected-clone guarantees,
those claims must be supported by its actual implementation.

# 67. Conformance and Disclosure

Owner-Mediated Disclosure is not a mandatory v2.0 Core primitive.
Therefore absence of Disclosure support does not fail Core conformance.
Direct cross-Friend Folder access remains prohibited. A future
Disclosure implementation MUST NOT weaken that prohibition.

# 68. Profile Conformance

A Profile defines additional requirements for a domain. A Profile MAY:
add domain-specific actors; add safety requirements; add
legal/institutional boundaries; add domain-specific conformance tests;
add stricter security controls. A Profile MUST NOT weaken Core.

# 69. Core Before Profile

An implementation cannot claim: M-PIN Healthcare Profile compliant while
violating mandatory M-PIN Core behavior. Profile conformance requires
Core conformance plus the applicable Profile requirements.

# 70. Profile Composition

One deployment MAY implement multiple Profiles. Example: Robot platform
├── Robotics Profile ├── AI Profile └── Healthcare Profile Each Friend
relationship remains subject to the Core isolation and authority model.
Profile composition MUST NOT create hidden cross-Friend Folder sharing.

# 71. AI Profile Compatibility

An AI Friend conforms to Core when it: uses its own Friend Folder; loads
authorized current state into its own Runtime; retains native AI service
behavior; does not receive other Friend Folders; persists M-PIN state
only through Owner-controlled Save. The AI Profile adds AI-specific
interpretation and tests.

# 72. Robotics Profile Compatibility

A Robotics implementation conforms to Core when robot-specific Friend
relationships preserve: Friend/Device distinction; Friend Folder
isolation; Owner-controlled persistence; Session boundaries; Device
portability. Core conformance does not certify physical safety.

# 73. Healthcare Profile Compatibility

Healthcare implementations must preserve the distinction between:
Owner-controlled M-PIN state and: institutional Healthcare Service
Record Core conformance does not itself establish medical consent,
clinician authority, or regulatory compliance.

# 74. Commerce Profile Compatibility

Commerce implementations must preserve the distinction between:
Owner-controlled Commerce Friend Folder state and:
merchant/payment/delivery Service Records Core conformance does not
itself authorize payment or establish merchant identity.

# 75. Interoperability Conformance

M-PIN interoperability does not mean all Friends share the same payload
schema. Core interoperability means different conforming Friends and
M-PIN implementations preserve the same architectural rules. Semantic
Friend payload interoperability may require Friend-specific or future
standards.

# 76. Behavioral Interoperability

Two implementations may use different internal architectures and still
interoperate if they preserve equivalent Core behavior. Example:
Implementation A local encrypted container

Implementation B Provider-hosted encrypted object store Both may conform
if: Owner authority remains central; Friend bindings remain valid; Save
semantics match; Session semantics match; portability requirements can
be satisfied.

# 77. Conformance Is Not File-Extension Recognition

A product is not M-PIN-conformant merely because it opens or creates a
file named: something.MPIN Conformance depends on behavior and
boundaries. The .MPIN representation remains
implementation-level/deferred in v2.0.

# 78. Conformance Is Not Branding

A service MUST NOT be considered technically conformant merely because
it uses: the name M-PIN; the word Friend; the word Owner; an M-PIN logo;
similar terminology. Observable behavior determines technical
conformance.

# 79. Conformance Is Not Intent

An implementation that states: “Owner owns the data” but silently
autosaves all Runtime state into M-PIN without Owner Save is
non-conformant. Declared philosophy cannot override contradictory
behavior.

# 80. Conformance Is Not Security Perfection

A conforming architecture may still contain implementation
vulnerabilities. For example: correct Core design + buggy implementation
can still be insecure. Core conformance and implementation security
assessment are related but distinct.

# 81. Conformance Is Not Legal Certification

M-PIN conformance MUST NOT be represented as automatic certification
under: HIPAA; GDPR; medical-device regulation; payment regulation;
consumer law; another jurisdictional regime. Such compliance requires
independent analysis.

# 82. Minimum Validation Suite

M-PIN v2 defines a minimum behavioral validation suite. A Core
implementation claiming full v2.0 conformance MUST pass the applicable
tests below. The tests are conceptual and implementation-neutral.

# 83. TEST-001 — First Friend Folder Creation

## Precondition

M-PIN exists Friend A has no Folder \## Action Friend A initiates first
synchronization. \## Expected Owner authority established. Friend A
verified. Folder absence detected. Owner approval requested. Folder A
created only after approval. Folder A bound to Friend A. \## Fail if
Folder A is silently created without required Owner approval.

# 84. TEST-002 — Existing Friend Folder Reuse

## Precondition

Friend A ↔ Folder A exists \## Action Friend A starts a new Session. \##
Expected Folder A is resolved and reused. \## Fail if A second
independent Folder is silently created for the same continuing
relationship.

# 85. TEST-003 — Cross-Friend Isolation

## Precondition

Friend A ↔ Folder A Friend B ↔ Folder B \## Action Friend A attempts to
read Folder B. \## Expected DENY \## Fail if Friend A receives Folder B
data under ordinary Friend A authority.

# 86. TEST-004 — Folder Enumeration Isolation

## Precondition

Multiple unrelated Friend Folders exist. \## Action Friend A performs
normal Folder resolution. \## Expected Friend A obtains what is required
to resolve Folder A without unrestricted access to unrelated Folder
payloads or authority. \## Fail if Friend A receives cross-Friend Folder
access merely to perform resolution. Full metadata-minimization behavior
may be evaluated as a SHOULD-level privacy property.

# 87. TEST-005 — Read Without Save

## Precondition

Current State = A \## Action Friend loads A. Runtime becomes B. Owner
does not Save. Session terminates. \## Expected Current State = A \##
Fail if B becomes M-PIN Persistent State.

# 88. TEST-006 — Owner Save

## Precondition

Current State = A Runtime State = B \## Action Owner authorizes Save.
\## Expected required Save validation occurs; Commit succeeds; Current
State becomes B. \## Fail if the implementation treats Friend internal
state change alone as sufficient Save authority.

# 89. TEST-007 — Atomic Commit Failure

## Precondition

Current State = A proposed State = B \## Action Commit is interrupted
before safe completion. \## Expected authoritative state resolves to
either: A or fully valid: B depending on the atomic success point. \##
Fail if a corrupted partial B becomes authoritative.

# 90. TEST-008 — Friend Internal Autosave

## Action

Friend performs an internal autosave while no Owner M-PIN Save occurs.
\## Expected M-PIN Current State does not change solely because of
Friend autosave. \## Fail if Friend internal autosave is treated as
M-PIN Save.

# 91. TEST-009 — Disconnect Without Save

## Precondition

Current State = A Runtime State = B \## Action required Session
dependency is unexpectedly lost before Save. \## Expected Session
terminates; B is not automatically committed; A remains Current State.
\## Fail if disconnect causes automatic M-PIN persistence.

# 92. TEST-010 — Reconnection

## Precondition

Session 1 terminated after unsaved Runtime changes. \## Action Friend
reconnects. \## Expected a new Session is established; latest
successfully committed Current State is loaded; old Session authority is
not revived. \## Fail if terminated Session 1 becomes active again
without new authorization context.

# 93. TEST-011 — One Active Friend

## Precondition

Friend A has active M-PIN Session. \## Action Friend B requests active
synchronization. \## Expected M-PIN preserves only one active Friend
synchronization authority. A conforming implementation may deny, queue,
or switch after terminating Friend A. \## Fail if Friend A and Friend B
both retain simultaneous active M-PIN synchronization authority within
the same authoritative continuity.

# 94. TEST-012 — Revocation

## Precondition

Friend A has valid active M-PIN authority. \## Action Owner revokes the
applicable authority. \## Expected Friend A loses continued M-PIN
authority under that Session/permission. \## Fail if Friend A continues
to read or Commit M-PIN state under the revoked authority.

# 95. TEST-013 — Provider Separation

## Precondition

M-PIN uses Provider P. \## Action Provider administrator attempts to act
as Owner without applicable Owner authority. \## Expected Owner-only
M-PIN operations are denied. \## Fail if ordinary Provider admin status
automatically grants Owner Save, cross-Friend access, or ownership
transfer.

# 96. TEST-014 — Device Migration

## Precondition

M-PIN X exists on Device A. \## Action Owner performs valid migration to
Device B. \## Expected where migration succeeds: same M-PIN Identity
same Friend Folder relationships valid Current State preserved new
Session authority established as required \## Fail if Device B becomes a
new Owner merely because it receives the state.

# 97. TEST-015 — Provider Migration

## Precondition

Provider A hosts M-PIN X. \## Action Owner performs supported valid
migration to Provider B. \## Expected where migration succeeds: M-PIN
continuity preserved; Friend Folder relationships preserved; Provider B
does not become Owner; Friends are not silently rebound. \## Fail if
Provider migration is implemented as mandatory new M-PIN ownership.

# 98. TEST-016 — Backup Is Not Active Clone

## Precondition

Authoritative M-PIN plus Backup exists. \## Action Backup is created.
\## Expected Backup is not automatically granted active Synchronization
Session authority. \## Fail if every Backup automatically becomes an
independent active M-PIN.

# 99. TEST-017 — Authority vs Data Recovery

## Scenario A

Owner authority recovered, data unavailable. \## Expected implementation
does not claim missing data has been recovered. \## Scenario B Backup
exists, Owner authority absent. \## Expected implementation does not
treat possession of Backup alone as sufficient Owner authority. \## Fail
if Authority Recovery and Data Recovery are collapsed into one
unconditional operation.

# 100. TEST-018 — Service Record Boundary

## Action

Friend performs an event that legitimately creates an independent
Service Record while Owner does not Save corresponding Runtime changes
to M-PIN. \## Expected Service Record MAY exist; unsaved M-PIN Runtime
state does not automatically become Friend Folder Current State. \##
Fail if the implementation either: claims legitimate independent Service
Records are impossible; or uses Service Record classification as a
blanket loophole to duplicate the complete synchronized Friend Folder.

# 101. Minimum Core Test Result

A full M-PIN v2.0 Core conformance claim requires passing all applicable
mandatory tests: TEST-001 TEST-002 TEST-003 TEST-005 TEST-006 TEST-007
TEST-008 TEST-009 TEST-010 TEST-011 TEST-012 TEST-013 TEST-014 TEST-015
TEST-016 TEST-017 TEST-018 TEST-004 contains both mandatory isolation
behavior and SHOULD-level discovery privacy behavior. The reference
suite contains 18 tests in total. A deployment MAY mark a test Not
Applicable only when the corresponding optional role genuinely does not
exist. Example: Provider migration test may be Not Applicable to a
local-only implementation with no Provider role. Not Applicable MUST NOT
be used to avoid a Core requirement that does apply.

# 102. Negative Testing

M-PIN v2 requires negative conformance testing. It is not sufficient to
demonstrate only successful synchronization. A conforming test suite
MUST verify denial or failure behavior for applicable cases such as:
wrong Friend; wrong Folder; missing Owner approval; no Save; revoked
Session; replayed Session; failed Commit; invalid binding; unauthorized
Provider action.

# 103. Why Negative Tests Are Normative

M-PIN’s primary value lies in preserving boundaries. Many boundaries are
visible only when an operation is denied. Therefore: “the normal path
works” is insufficient proof of conformance. The implementation must
also demonstrate: “the forbidden path does not work” for applicable
mandatory boundaries.

# 104. Friend Qualification Checklist

A Friend claiming M-PIN compatibility SHOULD be able to answer YES to:
Can the Friend be uniquely bound? Can it load only its own Friend
Folder? Can it use the loaded data in its native Runtime? Can the Owner
control M-PIN Save? Can Friend autosave remain distinct from M-PIN Save?
Can the Session terminate without implicit persistence? Can the Friend
operate without reading other Friend Folders? Can the Friend preserve
M-PIN behavior while changing its internal implementation? A NO to a
mandatory boundary indicates non-conformance.

# 105. M-PIN Implementation Checklist

An M-PIN implementation claiming Core conformance MUST preserve: Owner
authority Friend verification Friend Folder binding Friend Folder
isolation Session boundary one active Friend Load semantics Save
semantics Save/Commit distinction Atomic Commit Current-State-Only
encryption at rest integrity replay resistance revocation portability
recovery separation Provider optionality where applicable.

# 106. Provider Qualification Checklist

A Provider claiming to host a conforming M-PIN implementation SHOULD
demonstrate: it is not the architectural Owner; Provider administration
does not automatically equal Owner Authority; Friend Folder isolation
remains intact; migration/export is supported where required by the
deployment; security properties match the declared trust model; Provider
participation does not require Friends to surrender their native
Runtime/UX. Provider zero-knowledge is not a universal Core requirement.

# 107. Profile Qualification

A Profile implementation MUST satisfy: Core mandatory requirements +
Profile mandatory requirements A Profile cannot waive a Core MUST.

# 108. Conformance Levels

M-PIN v2.0 defines the following descriptive claim categories: \## Core
Conformant The implementation satisfies the applicable mandatory Core
requirements. \## Core + Profile Conformant The implementation satisfies
Core plus all mandatory requirements of the named Profile. \##
Experimental Extension The implementation adds behavior not defined by
Core, such as a future Disclosure mechanism. An Experimental Extension
MUST NOT be described as frozen Core behavior.

# 109. Extensions

An implementation MAY add features beyond Core. Examples include:
version history; additional Backup options; richer recovery;
multi-device coordination; Disclosure; Provider federation; Friend
semantic migration. Such features MUST NOT violate frozen Core
invariants.

# 110. Version History Extension

An implementation MAY offer user-facing version history as an extension.
If it does: it MUST NOT claim version history is required by v2.0 Core;
Current State must remain distinguishable from archived versions;
historical copies must be protected appropriately; the extension must
not silently change Owner Save semantics.

# 111. Disclosure Extension

An implementation MAY experiment with Owner-Mediated Disclosure. Such an
extension MUST preserve: Disclosure ≠ direct source Friend Folder access
and SHOULD preserve recipient-side M-PIN persistence rules. Disclosure
remains deferred from v2.0 Core.

# 112. Multi-Active Extension

An implementation that deliberately supports simultaneous active
synchronization with multiple Friends is not simply an extension to v2.0
Core. It changes a frozen architectural invariant. Such a change belongs
to a future architectural version, not a v2.0-conformant extension.

# 113. Shared Folder Extension

An implementation that introduces a universal shared Friend-accessible
Folder as a Core default changes the Friend Folder isolation model. That
is not v2.0 Core conformance. A future explicit data-sharing primitive
must be separately designed.

# 114. Mandatory Provider Extension

An implementation may itself require its own Provider for commercial or
operational reasons. It MUST NOT claim that this commercial deployment
constraint is a universal M-PIN Core requirement. M-PIN Core remains
Provider-optional.

# 115. Conformance Report

A formal M-PIN conformance report SHOULD identify: implementation name
implementation version M-PIN version claimed roles implemented Profiles
claimed mandatory tests performed test result Not Applicable tests and
justification known limitations extensions deferred implementation
choices This improves reproducibility and prevents vague compatibility
claims.

# 116. Declared Trust Model

A Provider-based or security-sensitive implementation SHOULD publish
enough information to describe its trust assumptions. For example: who
may hold encryption keys; whether Provider plaintext access is possible;
how Owner authentication works at a high level; how Friend identity is
established; what recovery authority exists. Conformance does not
require disclosure of exploitable secrets. It requires avoiding
misleading security claims.

# 117. Deferred Mechanisms and Conformance

The following deferred mechanisms do not block architectural Core
conformance if the implementation uses a concrete method that satisfies
the frozen behavior: .MPIN container format serialization cryptographic
algorithm selection key hierarchy Friend credential format Session token
format heartbeat transport Provider discovery freshness encoding
integrity-proof encoding Backup format recovery-factor mechanism A
reference standard may later standardize some of these.

# 118. Deferred Does Not Mean Optional Security

For example: exact replay token format = deferred does not mean: replay
protection = optional Likewise: exact encryption algorithm = deferred
does not mean: encryption at rest = optional The required property is
frozen even where the exact mechanism is not.

# 119. Interoperability Testing

Cross-implementation interoperability testing SHOULD verify that two
compatible implementations can preserve: M-PIN Identity continuity;
Friend Folder binding; Current State; Owner authority; security
properties across supported portability boundaries. Exact wire
interoperability cannot be fully standardized until deferred formats and
protocols are specified.

# 120. Architecture Conformance vs Wire Conformance

M-PIN v2.0 primarily freezes Architecture Conformance. Future work may
define: Wire Conformance Container Conformance Cryptographic Profile
Conformance Provider Federation Conformance Disclosure Conformance These
are not required to declare the v2.0 architecture frozen.

# 121. Conformance and Reference Implementation

A reference implementation MAY be created after the v2.0 architecture
freeze. The reference implementation does not define the architecture by
itself. If a reference implementation conflicts with the frozen Core
documents: Core specification takes precedence until an approved later
version changes the architecture.

# 122. Conformance and Existing Implementations

A product may independently implement behavior similar to parts of
M-PIN. M-PIN conformance requires evaluation against the published
requirements. Similarity alone does not prove: conformance; derivation;
infringement; implementation of the complete architecture.

# 123. Conformance and Intellectual Property

This specification defines technical architecture and behavioral
requirements. It does not itself determine: patent scope; copyright
scope; trademark rights; licensing obligations; infringement. Those
questions are separate from technical conformance.

# 124. Conformance Failure

An implementation is non-conformant with M-PIN v2.0 Core if it violates
any applicable mandatory Core requirement. Examples include: all Friends
read one shared Owner memory pool Friend autosave automatically becomes
M-PIN persistence Provider admin silently becomes Owner Friend A may
access Folder B by default disconnect automatically Saves partial
corrupted Commit becomes authoritative mandatory Provider is presented
as universal Core architecture

# 125. Partial Compatibility

An implementation MAY describe itself as: inspired by M-PIN partially
compatible experimental implements selected M-PIN principles if
accurate. It MUST NOT claim full M-PIN v2.0 Core conformance when
mandatory requirements are not satisfied.

# 126. Conformance Precedence

If there is ambiguity between implementation convenience and a frozen
Core invariant, the frozen Core invariant takes precedence for v2.0
conformance. Examples: convenient autosave vs Owner-controlled
persistence

shared company memory vs Friend Folder Isolation

Provider convenience vs Provider Independence The Core boundary wins.

# 127. Core Document Precedence

M-PIN v2.0 Core consists of: 01 — Scope & Design Constitution 02 — Core
Principles 03 — Terminology 04 — Core Architecture 05 — Owner & Identity
06 — Friend & Friend Folder Model 07 — Permission Model 08 — Session
Protocol 09 — Runtime & Persistence 10 — Security & Threat Model 11 —
Portability & Recovery 12 — Conformance Specification These documents
together define the frozen v2.0 Core.

# 128. Conflict Handling

If an implementation identifies an actual contradiction among frozen
Core requirements, the contradiction SHOULD be documented rather than
silently resolved by changing one rule in implementation. A genuine
architectural contradiction may justify: v2.1 clarification or, if
architecture changes: v3 The implementation MUST NOT quietly redefine
v2.0.

# 129. Reopening Criteria

The frozen v2.0 Core SHOULD be reopened only when one of the following
is demonstrated: actual architectural contradiction; material security
flaw; implementation impossibility; requirement unsupported by the
frozen architecture; another issue requiring Core-level change. New
examples, new industries, or implementation preferences alone do not
reopen Core.

# 130. Conformance Freeze

M-PIN v2.0 conformance is frozen around: Owner sovereignty Friend
sovereignty Friend Folder isolation bounded Session Runtime/Persistence
separation Owner Save Atomic Commit Current-State-Only security
boundaries Device independence Provider independence portability
recovery separation behavioral conformance Future work may standardize
deferred mechanisms without reopening these principles.

# 131. Minimum Conformance Summary

A system cannot claim full M-PIN v2.0 Core conformance unless all of the
following are true: 1. Owner remains the authority over M-PIN
persistence. 2. Friend retains its own Runtime and native UX. 3. One
Friend maps to one Friend Folder. 4. A Friend cannot access unrelated
Friend Folders by default. 5. First Friend Folder creation requires
Owner approval. 6. Returning synchronization reuses the existing Friend
Folder. 7. Friend Folder payload semantics remain Friend-defined. 8.
Runtime State is not Persistent State. 9. Owner Save is required for
M-PIN persistence. 10. Save and Commit remain distinct. 11. Commit is
atomic. 12. No Save leaves the previous Current State unchanged. 13.
Current-State-Only does not require version history. 14. Historical
service content may exist inside the current payload. 15. Friend
internal autosave is not M-PIN Save. 16. Friend access occurs through a
bounded Session. 17. Only one Friend has active M-PIN synchronization
authority at a time. 18. Terminated authority cannot silently remain
active. 19. Replay of invalid authority is rejected. 20. Persistent
Friend Folder state is encrypted at rest. 21. Security-relevant state
has integrity protection. 22. Provider administration is not Owner
Authority. 23. Device, Storage, and Provider changes do not inherently
change ownership. 24. Backup is not an automatically active M-PIN. 25.
Authority Recovery and Data Recovery remain distinct. 26. Service
Records remain separate and cannot be used as a loophole. 27. Provider
is optional at the Core architecture level. 28. Direct cross-Friend
Folder access is not a Core interoperability mechanism. 29. Profiles may
add requirements but may not weaken Core. 30. Conformance is judged by
observable behavior, not branding or internal technology.

# 132. Conformance Thesis

M-PIN v2.0 conformance can be reduced to one question: Does the
implementation preserve Owner-controlled persistent continuity while
allowing each Friend to remain an independent service? The expected
structure is: OWNER │ ▼ M-PIN │ ┌────────────┼────────────┐ │ │ │ ▼ ▼ ▼
Folder A Folder B Folder C │ │ │ ▼ ▼ ▼ Friend A Friend B Friend C │ │ │
▼ ▼ ▼ Native UX Native UX Native UX + Runtime + Runtime + Runtime Each
Friend remains independent. Each Friend sees only its own authorized
persistent relationship. Runtime changes remain temporary until the
Owner chooses persistence. Infrastructure may change without silently
changing ownership. A conforming implementation preserves those
boundaries not only when everything succeeds, but also when access must
be denied.

## M-PIN v2.0 — Core 12 / Conformance Specification

## Status: FROZEN
