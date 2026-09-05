# M-PIN v2.0

## Profile 03 — Healthcare

**Status:** FROZEN **Version:** 2.0 **Document Type:** Normative Profile
Specification **Requires:** M-PIN v2.0 Core 01–12

------------------------------------------------------------------------

# 1. Purpose

This Profile applies the M-PIN v2.0 Core architecture to healthcare
environments.

It defines how M-PIN may preserve Owner-controlled persistent continuity
while interacting with:

- hospitals;
- clinics;
- pharmacies;
- laboratories;
- healthcare AI services;
- medical devices;
- healthcare applications;
- other compatible healthcare services.

The Profile preserves a strict distinction between:

- Owner-controlled M-PIN state; and
- independent Healthcare Service Records.

M-PIN does not replace institutional healthcare record systems.

------------------------------------------------------------------------

# 2. Healthcare Thesis

The canonical Healthcare principle is:

> **The Owner may own and control persistent M-PIN healthcare state
> without thereby owning, replacing, or controlling every institutional
> healthcare record created by a healthcare service.**

Conceptually:

Owner │ ▼ M-PIN │ ├── Hospital A Friend Folder ├── Pharmacy Friend
Folder ├── Laboratory Friend Folder └── Healthcare AI Friend Folder

while independently:

Hospital / Pharmacy / Laboratory │ ▼ Healthcare Service Records

The two persistence domains must not be silently collapsed.

------------------------------------------------------------------------

# 3. Owner and Patient

In healthcare, **Owner** and **Patient** are distinct roles.

The same human may be both.

However:

# Owner

architectural authority over the applicable M-PIN

# Patient

person receiving healthcare services

These concepts MUST NOT be treated as universally identical.

------------------------------------------------------------------------

# 4. Owner Authority Is Not Clinical Authority

M-PIN Owner Authority does not automatically establish:

- medical consent;
- clinician authority;
- prescription authority;
- institutional authorization;
- guardian authority;
- insurance authority;
- legal representative status.

Those are governed by the applicable healthcare system, law,
institution, or explicit integration.

------------------------------------------------------------------------

# 5. Patient Identity Is Not M-PIN Identity

Patient Identity and M-PIN Identity remain distinct.

A hospital may need to verify a patient’s identity under its own
healthcare process.

Successful M-PIN authentication does not automatically satisfy every
medical identity requirement.

Likewise:

Hospital patient ID ≠ M-PIN Identity

unless a specific authorized integration defines the relationship.

------------------------------------------------------------------------

# 6. Healthcare Friend

A healthcare organization or service may participate as a Friend.

Examples include:

- Hospital Friend;
- Clinic Friend;
- Pharmacy Friend;
- Laboratory Friend;
- Healthcare AI Friend;
- medical-device Friend;
- health application Friend.

Each Friend remains independently subject to Core identity, Folder,
Session, permission, and persistence requirements.

------------------------------------------------------------------------

# 7. One Healthcare Friend, One Friend Folder

Each healthcare Friend relationship has its own Friend Folder.

Example:

M-PIN ├── Hospital A Folder ├── Hospital B Folder ├── Pharmacy A Folder
├── Laboratory A Folder └── Healthcare AI Folder

Common healthcare purpose does not create a shared Folder.

------------------------------------------------------------------------

# 8. Healthcare Folder Isolation

Hospital A MUST NOT automatically read:

- Hospital B Folder;
- Pharmacy Folder;
- Laboratory Folder;
- Healthcare AI Folder.

Likewise, those Friends MUST NOT automatically read Hospital A Folder.

The fact that the information may be medically useful does not itself
create M-PIN authority.

------------------------------------------------------------------------

# 9. Same Healthcare Network

Two hospitals or clinics owned by the same healthcare network MUST NOT
automatically share M-PIN Friend Folder authority merely because they
have the same corporate parent.

If they are modeled as distinct Friends, their Folder boundaries remain
distinct.

Corporate structure does not override Friend Identity.

------------------------------------------------------------------------

# 10. Healthcare Friend Folder

A Healthcare Friend Folder is the Owner-owned persistent M-PIN area
associated with one healthcare Friend.

Depending on the Friend’s semantics, its Current State may include
Owner-controlled information such as:

- preferences;
- Owner-held documents;
- Owner-held healthcare information;
- service configuration;
- appointment-related state;
- communication state;
- device configuration;
- Owner-held copies of healthcare information;
- other Friend-specific persistent state.

The exact payload is Friend-defined.

------------------------------------------------------------------------

# 11. Healthcare Payload Semantics

The healthcare Friend remains responsible for interpreting its own
Friend Folder payload.

M-PIN does not determine whether a payload object is:

- a diagnosis;
- a medication list;
- a laboratory result;
- a patient-entered note;
- a clinical document;
- an appointment preference;
- a device setting.

M-PIN preserves the architectural boundary around the payload.

------------------------------------------------------------------------

# 12. M-PIN Integrity Is Not Medical Accuracy

M-PIN integrity protection may establish that data has not been
improperly modified within the protected M-PIN mechanism.

It does not establish that the medical content is clinically correct.

For example:

integrity valid ≠ diagnosis medically correct

or:

integrity valid ≠ medication list current

Clinical interpretation remains outside M-PIN Core.

------------------------------------------------------------------------

# 13. Owner-Controlled Healthcare State

Owner-controlled healthcare state is persistent data held within the
Owner’s M-PIN Friend Folder relationship.

The Owner controls M-PIN persistence according to the Core Save model.

This does not mean the Owner can use M-PIN to rewrite every
institutional record about them.

------------------------------------------------------------------------

# 14. Healthcare Service Record

A **Healthcare Service Record** is an independent record legitimately
maintained by a healthcare Friend or institution for purposes such as:

- clinical care;
- prescription handling;
- laboratory operation;
- billing;
- insurance processing;
- audit;
- safety;
- security;
- regulatory obligations;
- legal retention;
- institutional operations.

Such a record may persist independently from M-PIN Save.

------------------------------------------------------------------------

# 15. Owner State vs Healthcare Service Record

Canonical distinction:

Owner-controlled M-PIN state ≠ Healthcare Service Record

Example:

Owner changes a healthcare preference in Runtime ↓ Owner does not Save ↓
M-PIN Current State unchanged

while independently:

Hospital completes a clinical procedure ↓ Hospital may create required
Healthcare Service Record

These outcomes do not contradict each other.

------------------------------------------------------------------------

# 16. No Save Does Not Delete Clinical Reality

If the Owner does not Save M-PIN Runtime changes:

the healthcare institution may still retain legitimate records of care
that actually occurred.

Therefore:

NO M-PIN SAVE ≠ delete institutional record

M-PIN persistence and institutional recordkeeping are separate.

------------------------------------------------------------------------

# 17. M-PIN Deletion Does Not Delete Institutional Records

Deleting:

- an M-PIN;
- a Healthcare Friend Folder;
- Owner-controlled M-PIN content

does not automatically delete independent Healthcare Service Records.

Any right or obligation concerning institutional record deletion is
outside the Core persistence model and subject to applicable law and
institutional rules.

------------------------------------------------------------------------

# 18. Institutional Retention Does Not Grant M-PIN Access

The reverse is also true.

A hospital’s legal or operational need to retain its own Service Record
does not automatically grant it permanent access to the Owner’s M-PIN
Friend Folder.

Institutional retention authority ≠ unlimited M-PIN authority

------------------------------------------------------------------------

# 19. Service Record Anti-Loophole

A healthcare Friend MUST NOT evade M-PIN persistence boundaries by:

1.  loading the entire Friend Folder;
2.  permanently copying the complete synchronized state outside M-PIN;
3.  labeling the copy a Healthcare Service Record;
4.  treating it as unrestricted institutional data

without an independently legitimate healthcare, operational, safety,
contractual, or legal basis.

The Service Record distinction is not a blanket persistence exception.

------------------------------------------------------------------------

# 20. Native Healthcare Systems

M-PIN does not replace:

- EHR systems;
- EMR systems;
- pharmacy systems;
- laboratory systems;
- medical-device software;
- billing systems;
- hospital workflows.

A Healthcare Friend continues to operate its native systems and UX.

M-PIN governs the Owner-controlled persistence boundary.

------------------------------------------------------------------------

# 21. M-PIN Is Not an EHR

M-PIN MUST NOT be described as automatically becoming the authoritative
institutional electronic health record.

A Healthcare Friend may load Owner-controlled M-PIN data into its
Runtime.

That does not automatically make the data:

- clinically verified;
- institutionally accepted;
- legally authoritative;
- complete.

The institution decides how information is used under its own healthcare
responsibilities.

------------------------------------------------------------------------

# 22. Owner Data May Be Stale or Incomplete

A Healthcare Friend MUST NOT assume that M-PIN healthcare data is
necessarily:

- complete;
- current;
- medically verified;
- institutionally authoritative.

The Friend remains responsible for appropriate validation before relying
on it for clinical decisions.

------------------------------------------------------------------------

# 23. First Healthcare Synchronization

Canonical first synchronization:

Owner ↓ initiates Sync ↓ identifies/opens M-PIN ↓ Owner authority
established ↓ Healthcare Friend Identity verified ↓ Friend Folder
resolved ↓ Folder absent ↓ Owner creation approval ↓ Folder created and
bound ↓ Session established ↓ Current/initial state loaded ↓ native
Healthcare Friend Runtime

No healthcare Friend receives a Folder merely because it treats the
Owner.

------------------------------------------------------------------------

# 24. Returning Healthcare Synchronization

For a returning Friend:

Owner ↓ establishes M-PIN authority ↓ Healthcare Friend verified ↓
existing Friend Folder resolved ↓ new Session ↓ Current State loaded ↓
native healthcare workflow

The existing Friend Folder relationship is reused.

------------------------------------------------------------------------

# 25. Healthcare Runtime

Once authorized state is loaded:

Healthcare Friend Folder Current State A ↓ Load ↓ Healthcare Runtime ↓
service interaction ↓ Runtime State B

Runtime State B does not automatically become M-PIN Current State B.

------------------------------------------------------------------------

# 26. Owner Save

Owner-controlled M-PIN persistence follows Core:

Current State A ↓ Load ↓ Healthcare Runtime State B ↓ Owner SAVE ↓
Validation ↓ Atomic Commit ↓ Current State B

This controls M-PIN persistence only.

------------------------------------------------------------------------

# 27. Healthcare Save Is Not Clinical Authorization

Owner SAVE means:

the Owner authorizes the applicable M-PIN persistence transition.

It does not automatically mean:

- consent to treatment;
- authorization of prescription;
- acceptance of diagnosis;
- insurance approval;
- legal signature;
- clinician approval.

Those require their own applicable processes.

------------------------------------------------------------------------

# 28. Healthcare Service Action Is Not Save

A healthcare action does not automatically constitute M-PIN Save.

Examples:

- doctor records diagnosis;
- pharmacy dispenses medication;
- laboratory completes test;
- device measures vital sign;
- hospital schedules procedure.

These may create independent Service Records.

They do not inherently constitute Owner M-PIN SAVE.

------------------------------------------------------------------------

# 29. Cross-Institution Data Need

Healthcare frequently requires data from more than one service.

For example:

Hospital B may need selected information originating from Hospital A.

That practical need does not authorize:

Hospital B ↓ Hospital A Friend Folder

Direct cross-Friend Folder access remains prohibited.

------------------------------------------------------------------------

# 30. Owner-Mediated Disclosure Candidate

Healthcare exposes a need for selected Owner-authorized data transfer
between Friend relationships.

A candidate future mechanism is:

**Owner-Mediated Disclosure**

Conceptually:

Source Friend relationship ↓ Owner selects/authorizes data ↓ Disclosure
↓ Recipient Friend

This is not part of the frozen v2.0 Core.

------------------------------------------------------------------------

# 31. Disclosure Is Not Folder Sharing

A future Disclosure mechanism MUST preserve:

Disclosure ≠ recipient reads source Friend Folder

The recipient receives only the information explicitly authorized under
the Disclosure mechanism.

The source Folder remains isolated.

------------------------------------------------------------------------

# 32. Minimum Necessary Principle

Healthcare Disclosure SHOULD support selection of only the information
required for the intended purpose.

Conceptually:

entire Hospital A Folder ✗

selected medication information ✓

where the Owner and applicable healthcare authorization model permit it.

The exact Disclosure schema remains deferred.

------------------------------------------------------------------------

# 33. Disclosure Authorization

M-PIN Owner authorization alone MUST NOT automatically be treated as
satisfying every legal or clinical consent requirement.

A healthcare implementation may require additional:

- patient consent;
- guardian authority;
- clinician authorization;
- institutional approval;
- legal basis.

Those requirements remain separate.

------------------------------------------------------------------------

# 34. Pharmacy as Separate Friend

A pharmacy may be a Friend separate from a hospital.

Example:

M-PIN ├── Hospital Folder └── Pharmacy Folder

The Pharmacy Friend does not automatically read the Hospital Folder.

Prescription or medication information may move through legitimate
healthcare systems or a future authorized Disclosure mechanism.

------------------------------------------------------------------------

# 35. Laboratory as Separate Friend

A laboratory may likewise be a separate Friend.

A Hospital Friend does not automatically receive the Laboratory Friend
Folder merely because the services participate in the same episode of
care.

External healthcare interoperability may operate independently of M-PIN.

------------------------------------------------------------------------

# 36. Healthcare AI as Separate Friend

A Healthcare AI service may be a Friend separate from the hospital.

Example:

M-PIN ├── Hospital Friend Folder └── Healthcare AI Friend Folder

The Healthcare AI MUST NOT automatically read the Hospital Friend
Folder.

AI usefulness does not override Friend Folder Isolation.

------------------------------------------------------------------------

# 37. Healthcare AI and Disclosure

If selected hospital-originating information is to be provided to a
Healthcare AI, that transfer requires an applicable authorized
mechanism.

It MUST NOT be implemented as unrestricted Hospital Folder access.

AI Profile requirements also remain applicable.

------------------------------------------------------------------------

# 38. Medical Device Composition

A medical device may be:

- a Device;
- a Friend;
- a host for a Friend;
- part of another healthcare Friend’s Runtime.

The exact role depends on the service boundary.

Physical device identity does not automatically establish Friend
authority.

------------------------------------------------------------------------

# 39. Medical Device Friend

Where a medical-device service is modeled as a Friend:

M-PIN ↓ Medical Device Friend Folder ↓ Medical Device Friend ↓ Device
Runtime

the Core Friend Folder and persistence rules apply.

------------------------------------------------------------------------

# 40. Continuous Medical Sensors

A medical device may generate continuous sensor data.

M-PIN does not require every sensor sample to become Owner-controlled
persistent state.

A Friend may process sensor data in Runtime or maintain legitimate
healthcare Service Records where appropriate.

M-PIN persistence follows the applicable Save model.

------------------------------------------------------------------------

# 41. Sensor Observation Is Not M-PIN Save

Examples:

heart-rate measurement blood-pressure reading temperature measurement
continuous glucose observation

do not automatically constitute Owner M-PIN Save.

The relevant Friend determines Runtime semantics.

Independent medical record obligations remain separate.

------------------------------------------------------------------------

# 42. Healthcare Profile Composition

Healthcare Profile MAY compose with:

- AI Profile;
- Robotics Profile;
- Commerce Profile.

For example:

Healthcare Robot ├── Robot Control Friend ├── Healthcare Friend └──
Healthcare AI Friend

Each Friend remains isolated under Core.

------------------------------------------------------------------------

# 43. Healthcare and Commerce Composition

A healthcare transaction may involve:

- Healthcare Friend;
- Pharmacy Friend;
- Payment Friend;
- Insurance-related service;
- Delivery Friend.

These relationships MUST NOT be collapsed into one shared M-PIN Folder
merely because they participate in one workflow.

------------------------------------------------------------------------

# 44. Payment Authorization

M-PIN Owner Authority does not automatically authorize payment.

If a healthcare workflow requires payment:

M-PIN authorization ≠ Payment authorization

Commerce or payment-specific authorization remains separate.

------------------------------------------------------------------------

# 45. Insurance Authority

M-PIN does not automatically establish insurance eligibility, coverage,
or claims authority.

An insurance service may require its own identity and authorization
process.

------------------------------------------------------------------------

# 46. Emergency Access

Healthcare raises legitimate emergency-access questions.

M-PIN v2.0 does not define a universal emergency backdoor that opens
every healthcare Friend Folder.

------------------------------------------------------------------------

# 47. No Universal Emergency Unlock

The following is not part of v2.0 Core:

Emergency declared ↓ all Friends may read all healthcare data

Such a mechanism would violate the default Friend Folder Isolation
model.

------------------------------------------------------------------------

# 48. Candidate Emergency Policy

A future healthcare implementation MAY define an Owner-configured or
otherwise legally valid Emergency Policy.

Such a policy could potentially specify:

- selected data;
- authorized recipient class;
- purpose;
- time limit;
- emergency condition;
- audit requirements.

This remains outside the frozen Core unless separately standardized.

------------------------------------------------------------------------

# 49. Emergency Policy Is Not Unlimited Access

Any future Emergency Policy SHOULD be:

- scoped;
- purpose-limited;
- time-limited where appropriate;
- auditable where appropriate;
- restricted to necessary information.

It SHOULD NOT become a universal M-PIN master key.

------------------------------------------------------------------------

# 50. Emergency Safety Systems

M-PIN MUST NOT prevent a healthcare institution or medical device from
performing legally or clinically required emergency functions that do
not depend on M-PIN authority.

M-PIN is not the sole emergency-control system.

------------------------------------------------------------------------

# 51. Healthcare Security Sensitivity

Healthcare Friend Folder data may be highly sensitive.

Implementations MUST apply the Core requirements for:

- encryption at rest;
- integrity;
- authentication;
- authorization;
- isolation;
- replay resistance;
- Session termination;
- fail-closed behavior.

The exact cryptographic mechanisms remain deferred.

------------------------------------------------------------------------

# 52. Shared Terminal Risk

Healthcare frequently uses shared Devices.

Examples include:

- hospital workstation;
- clinic terminal;
- pharmacy terminal;
- bedside device;
- shared tablet.

One Owner’s M-PIN Session MUST NOT leave usable authority for another
person.

------------------------------------------------------------------------

# 53. Shared Terminal Residual Data

Healthcare implementations SHOULD minimize residual:

- plaintext;
- Session credentials;
- cached Friend Folder content;
- Owner identity metadata

after the applicable M-PIN Session ends.

Exact secure-erasure mechanisms are implementation-defined.

------------------------------------------------------------------------

# 54. Malicious Healthcare Friend

A malicious or compromised Healthcare Friend may misuse plaintext
legitimately loaded from its own Friend Folder.

M-PIN cannot retroactively prevent all misuse after legitimate plaintext
disclosure.

However, compromise of Hospital A MUST NOT automatically grant:

- Hospital B Folder access;
- Pharmacy Folder access;
- Healthcare AI Folder access;
- Owner recovery authority.

------------------------------------------------------------------------

# 55. Compromised Provider

If an M-PIN Provider can access plaintext under the implementation’s
trust model, M-PIN v2.0 does not falsely claim zero-knowledge
protection.

Provider access remains distinct from Owner or Healthcare Friend
authority.

The actual key and trust model must be evaluated separately.

------------------------------------------------------------------------

# 56. Data Provenance

Healthcare Friends SHOULD preserve sufficient provenance to distinguish,
where relevant:

- Owner-entered information;
- Friend-generated information;
- institutionally verified information;
- imported information;
- recovered information.

The exact provenance schema is not standardized in v2.0.

------------------------------------------------------------------------

# 57. Integrity vs Provenance

Integrity and provenance are different.

Integrity asks:

“Was this protected state improperly changed?”

Provenance asks:

“Where did this information come from?”

Neither alone proves medical truth.

------------------------------------------------------------------------

# 58. Portability

Healthcare Friend Folder relationships SHOULD remain portable with the
Owner’s M-PIN across compatible:

- Devices;
- Storage environments;
- M-PIN Providers.

Infrastructure migration does not automatically change the Healthcare
Friend.

------------------------------------------------------------------------

# 59. Provider Migration

Example:

Provider A ↓ M-PIN X ↓ Hospital A Folder

may become:

Provider B ↓ same M-PIN X ↓ same Hospital A Folder

where valid migration succeeds.

Provider B does not become the hospital or Owner.

------------------------------------------------------------------------

# 60. Healthcare Friend Migration

Moving from Hospital A to Hospital B is not Provider migration.

Hospital B is a different Friend unless explicitly modeled otherwise.

Therefore:

Hospital A Folder ≠ Hospital B Folder

------------------------------------------------------------------------

# 61. Patient Transfer Between Hospitals

A patient transferring care from Hospital A to Hospital B does not
automatically transfer M-PIN Folder ownership or access.

Any required medical data transfer must use an applicable healthcare
interoperability, legal, institutional, or future Owner-mediated
mechanism.

------------------------------------------------------------------------

# 62. Recovery

Healthcare M-PIN recovery follows Core 11.

Authority Recovery and Data Recovery remain separate.

Possession of a medical Backup does not establish Owner Authority.

Owner Authority Recovery does not reconstruct destroyed medical data.

------------------------------------------------------------------------

# 63. Recovery and Clinical Records

Restoring an older Healthcare Friend Folder does not roll back a
hospital’s clinical record.

Example:

M-PIN backup restored to earlier state ≠ later surgery did not occur

M-PIN recovery restores Owner-controlled continuity, not external
medical history.

------------------------------------------------------------------------

# 64. Stale Recovery Risk

An older recovered M-PIN state may contain outdated medical information.

Healthcare Friends MUST NOT assume that recovered state is necessarily
current.

Appropriate clinical validation remains necessary.

------------------------------------------------------------------------

# 65. Healthcare Service Failure

If a Healthcare Friend ceases operation, its Friend Folder may remain in
the Owner’s M-PIN.

Another healthcare Friend does not automatically gain semantic or access
rights to that Folder.

Future selected transfer may require an explicit interoperability
mechanism.

------------------------------------------------------------------------

# 66. M-PIN Provider Failure

Failure of an M-PIN Provider is different from failure of the hospital.

Where sufficient valid state and recovery material exist, M-PIN
continuity may be recovered or migrated independently of the failed
Provider.

------------------------------------------------------------------------

# 67. Friend Identity

Healthcare Friend Identity must be sufficiently stable and verifiable to
protect Folder binding.

A mutable display name such as:

“Hospital” “Clinic” “Pharmacy”

is not sufficient by itself as a security identity.

The exact credential format remains deferred.

------------------------------------------------------------------------

# 68. Institutional Change

A hospital may:

- rebrand;
- merge;
- change IT systems;
- replace its EHR;
- change cloud infrastructure.

Such changes do not necessarily create a new Friend.

Whether Friend continuity remains valid depends on the legitimate
service identity relationship.

------------------------------------------------------------------------

# 69. Acquisition Does Not Grant Universal Access

If Hospital Group X acquires Hospital Y, other services in Group X do
not automatically receive Hospital Y’s M-PIN Friend Folder authority.

Corporate acquisition does not override M-PIN Folder isolation.

------------------------------------------------------------------------

# 70. Data Minimization

A Healthcare Friend SHOULD receive only the M-PIN data required for its
authorized relationship.

“More data might be medically useful” is not by itself sufficient M-PIN
authorization.

------------------------------------------------------------------------

# 71. Purpose Limitation

Where selected healthcare information is disclosed or otherwise
authorized for a specific purpose, implementations SHOULD avoid using
that authorization as unrestricted permission for unrelated purposes.

Detailed legal purpose-limitation rules remain outside M-PIN Core.

------------------------------------------------------------------------

# 72. Secondary Use

M-PIN synchronization authority MUST NOT automatically be interpreted as
authorization for every secondary use of healthcare data.

Examples may include:

- advertising;
- unrelated analytics;
- model training;
- sale of data;
- unrelated research.

Such uses require their own applicable basis.

------------------------------------------------------------------------

# 73. Research Use

Healthcare research may have separate consent, institutional, ethical,
or legal frameworks.

M-PIN Owner Save or synchronization alone does not automatically
authorize research use.

------------------------------------------------------------------------

# 74. Healthcare AI Training

Healthcare AI Friend access to its authorized M-PIN Folder does not
automatically authorize training on that data.

The AI Profile training boundary also applies.

------------------------------------------------------------------------

# 75. Regulatory Scope

M-PIN v2.0 Healthcare Profile does not claim automatic compliance with
any specific healthcare privacy, medical-device, or data-protection
regime.

Conformance to this Profile is architectural.

Regulatory compliance requires independent evaluation.

------------------------------------------------------------------------

# 76. Jurisdiction Neutrality

Healthcare law varies by jurisdiction.

M-PIN Core therefore does not define one universal rule for:

- medical consent age;
- guardian authority;
- record retention period;
- emergency disclosure;
- prescription control;
- medical record ownership.

Implementations must apply the relevant external requirements.

------------------------------------------------------------------------

# 77. Healthcare Mandatory Requirements

A Healthcare implementation claiming M-PIN v2.0 Healthcare Profile
conformance MUST satisfy:

### HEALTH-001 — Core Conformance

The implementation MUST satisfy all applicable M-PIN v2.0 Core
requirements.

### HEALTH-002 — Owner / Patient Distinction

The implementation MUST NOT assume that architectural Owner status
automatically satisfies every Patient, guardian, clinical, or legal
authority requirement.

### HEALTH-003 — Healthcare Friend Isolation

Distinct Healthcare Friends MUST NOT automatically access each other’s
Friend Folders.

### HEALTH-004 — Service Record Separation

Owner-controlled M-PIN healthcare state MUST remain distinguishable from
independent Healthcare Service Records.

### HEALTH-005 — No Service Record Loophole

Healthcare Service Records MUST NOT be used as a blanket mechanism to
duplicate the complete synchronized Friend Folder.

### HEALTH-006 — Owner-Controlled M-PIN Persistence

Healthcare Runtime changes become M-PIN Persistent State only through
the applicable Owner Save process.

### HEALTH-007 — Clinical Action Separation

Clinical, pharmacy, laboratory, or device actions MUST NOT automatically
constitute M-PIN Save.

### HEALTH-008 — No Universal Emergency Backdoor

The Profile MUST NOT require a universal emergency mechanism granting
unrestricted access to every Healthcare Friend Folder.

### HEALTH-009 — Medical Accuracy Separation

M-PIN integrity MUST NOT be represented as proof of clinical accuracy or
completeness.

### HEALTH-010 — Recovery Separation

M-PIN recovery MUST NOT be represented as rollback or deletion of
independent Healthcare Service Records.

------------------------------------------------------------------------

# 78. Recommended Healthcare Properties

A Healthcare implementation SHOULD additionally satisfy:

### HEALTH-011 — Data Minimization

Healthcare Friends SHOULD receive only information required for the
authorized relationship.

### HEALTH-012 — Provenance Preservation

Healthcare implementations SHOULD preserve useful provenance for
medically relevant imported or Owner-controlled data.

### HEALTH-013 — Shared Device Hygiene

Shared healthcare Devices SHOULD minimize residual M-PIN plaintext and
credentials after Session termination.

### HEALTH-014 — Staleness Awareness

Healthcare Friends SHOULD account for the possibility that
Owner-controlled or recovered M-PIN data is stale or incomplete.

### HEALTH-015 — Purpose-Bounded Transfer

Any selected cross-Friend transfer mechanism SHOULD be scoped to the
authorized purpose and information.

------------------------------------------------------------------------

# 79. Healthcare Conformance Tests

The following Profile tests supplement the Core suite.

------------------------------------------------------------------------

# 80. HEALTH-TEST-001 — Hospital Isolation

**Precondition**

Hospital A ↔ Folder A Hospital B ↔ Folder B

**Action**

Hospital B requests Folder A.

**Expected**

DENY

------------------------------------------------------------------------

# 81. HEALTH-TEST-002 — Pharmacy Isolation

**Precondition**

Hospital Folder and Pharmacy Folder exist.

**Action**

Pharmacy Friend requests the Hospital Folder under ordinary Pharmacy
authority.

**Expected**

DENY

------------------------------------------------------------------------

# 82. HEALTH-TEST-003 — Healthcare AI Isolation

**Precondition**

Hospital Friend ↔ Hospital Folder Healthcare AI ↔ AI Folder

**Action**

Healthcare AI requests Hospital Folder.

**Expected**

DENY

AI usefulness does not create Folder authority.

------------------------------------------------------------------------

# 83. HEALTH-TEST-004 — No Save After Runtime Change

**Precondition**

Healthcare Friend Current State = A

**Action**

1.  A is loaded.
2.  Runtime changes to B.
3.  Owner does not Save.
4.  Session terminates.

**Expected**

M-PIN Current State remains A.

Independent legitimate Healthcare Service Records may still exist.

------------------------------------------------------------------------

# 84. HEALTH-TEST-005 — Clinical Record Independence

**Action**

Healthcare service performs legitimate care that requires an
institutional record while no corresponding M-PIN Save occurs.

**Expected**

Healthcare Service Record may persist.

Unsaved M-PIN Runtime state does not automatically become M-PIN Current
State.

------------------------------------------------------------------------

# 85. HEALTH-TEST-006 — M-PIN Deletion

**Action**

Owner deletes applicable M-PIN healthcare state.

**Expected**

The action does not automatically erase independent institutional
Healthcare Service Records.

------------------------------------------------------------------------

# 86. HEALTH-TEST-007 — Institutional Retention

**Action**

Hospital retains a legitimate Service Record after M-PIN Session
termination.

**Expected**

Retention does not grant the Hospital continuing M-PIN Friend Folder
authority.

------------------------------------------------------------------------

# 87. HEALTH-TEST-008 — Emergency Request

**Action**

a healthcare Friend declares an emergency and requests every Healthcare
Friend Folder.

**Expected**

No universal Core emergency backdoor grants unrestricted access.

Any separately defined emergency mechanism must use its own applicable
authority.

------------------------------------------------------------------------

# 88. HEALTH-TEST-009 — M-PIN Integrity

**Action**

a Healthcare Friend receives a payload with valid M-PIN integrity.

**Expected**

The Friend may verify the relevant M-PIN integrity property.

It MUST NOT treat integrity alone as proof of medical correctness.

------------------------------------------------------------------------

# 89. HEALTH-TEST-010 — Recovery

**Precondition**

an older Healthcare Friend Folder Backup is legitimately recovered.

**Expected**

the recovered M-PIN state does not automatically rewrite or delete later
institutional Healthcare Service Records.

------------------------------------------------------------------------

# 90. HEALTH-TEST-011 — Provider Migration

**Precondition**

Hospital A Folder exists under M-PIN Provider P1.

**Action**

Owner validly migrates M-PIN to Provider P2.

**Expected**

Hospital A ↔ Folder A relationship remains where migration succeeds.

Provider P2 does not become the Owner or Hospital.

------------------------------------------------------------------------

# 91. HEALTH-TEST-012 — Patient Transfer

**Precondition**

Hospital A ↔ Folder A.

**Action**

Owner begins treatment at Hospital B.

**Expected**

Hospital B does not automatically inherit Folder A.

Required healthcare information transfer uses a separate applicable
mechanism.

------------------------------------------------------------------------

# 92. Healthcare Non-Goals

This Profile does not define:

- universal EHR schema;
- universal medical record format;
- diagnosis rules;
- clinical decision support;
- prescription protocol;
- hospital workflow;
- medical-device control protocol;
- insurance claims protocol;
- healthcare payment protocol;
- universal patient identity;
- universal emergency access;
- legal medical consent;
- record-retention periods;
- automatic regulatory compliance;
- automatic hospital-to-hospital Folder sharing.

------------------------------------------------------------------------

# 93. Deferred Healthcare Mechanisms

The following remain outside the frozen v2.0 Healthcare Profile:

``` text
healthcare Disclosure schema
Emergency Policy schema
patient/guardian authority integration
clinical provenance schema
medical credential format
healthcare Friend trust registry
cross-institution interoperability mapping
medical-device attestation
purpose-bound authorization token
healthcare-specific freshness mechanism
These may be standardized later without weakening Core.
```

# 94. Healthcare Profile Invariants

The Healthcare Profile is governed by these invariants: \## Owner and
Patient are distinct architectural concepts. \## M-PIN authentication is
not universal medical or legal authorization. \## One Healthcare Friend
has one Friend Folder. \## Healthcare usefulness does not override
Friend Folder Isolation. \## Owner-controlled M-PIN state is not the
same as an institutional Healthcare Service Record. \## No M-PIN Save
does not erase healthcare reality. \## Deleting M-PIN state does not
automatically delete institutional records. \## Institutional record
retention does not grant permanent M-PIN access. \## Healthcare Service
Records cannot be used as a blanket persistence loophole. \## M-PIN
integrity is not proof of medical accuracy. \## Healthcare AI is not
automatically authorized to read Hospital Friend Folders. \## A pharmacy
is not automatically authorized to read a hospital’s Friend Folder. \##
Patient transfer does not automatically transfer Friend Folder
authority. \## M-PIN recovery does not roll back clinical history. \##
There is no universal healthcare emergency backdoor in v2.0 Core.

# 95. Canonical Healthcare Architecture

                              OWNER
                                │
                                ▼
                              M-PIN
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼

Hospital A Folder Pharmacy Folder Healthcare AI Folder │ │ │ ▼ ▼ ▼
Hospital A Friend Pharmacy Friend Healthcare AI Friend │ │ │ ▼ ▼ ▼
Native Hospital Native Pharmacy Native AI Runtime Runtime Runtime

Separately:

Hospital / Pharmacy / Laboratory / other institution │ ▼ legitimate
Service Records The Service Record layer is not a shared M-PIN Folder.

# 96. Healthcare Persistence Model

Healthcare Friend Folder Current State₀ │ ▼ Load │ ▼ Healthcare Friend
Runtime │ ▼ Runtime State′ │ Owner SAVE │ ▼ Validation │ ▼ Atomic Commit
│ ▼ Healthcare Friend Folder Current State₁ Without Save: Runtime State′
│ Session termination │ ▼ No M-PIN Commit │ ▼ Current State₀ remains
Independent legitimate Healthcare Service Records may nevertheless
persist.

# 97. Cross-Friend Healthcare Need

Healthcare demonstrates an important distinction: data needs to move
does not mean: Folder boundaries should disappear A future architecture
may support: Source Friend │ selected data │ Owner authorization ▼
Disclosure │ ▼ Recipient Friend while still preserving: Source Friend
Folder ≠ Recipient Friend Folder This requirement helped identify
Owner-Mediated Disclosure as a candidate interoperability primitive. It
remains deferred from the frozen v2.0 Core.

# 98. Healthcare Profile Thesis

M-PIN does not attempt to make the hospital disappear. It does not
attempt to replace the hospital’s record system, legal responsibilities,
clinical judgment, or safety obligations. Instead, it establishes a
separate Owner-controlled persistence boundary. The hospital may
maintain legitimate records of care. The pharmacy may maintain
legitimate dispensing records. The laboratory may maintain legitimate
test records. The healthcare AI may operate its own service. But none of
those facts inherently grants every service access to every part of the
Owner’s M-PIN. The architecture therefore separates: what the
institution must retain from: what the Owner chooses to persist inside
the M-PIN relationship and separates: medical need for selected
information from: unrestricted access to another Friend Folder
Healthcare records may remain institutional. Owner continuity may remain
Owner-controlled. The two do not need to become the same system.

## M-PIN v2.0 — Profile 03 / Healthcare

## Status: FROZEN
