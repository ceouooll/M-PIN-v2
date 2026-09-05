# M-PIN v2.0

## Profile 04 — Commerce

**Status:** FROZEN **Version:** 2.0 **Document Type:** Normative Profile
Specification **Requires:** M-PIN v2.0 Core 01–12

------------------------------------------------------------------------

# 1. Purpose

This Profile applies the M-PIN v2.0 Core architecture to commerce.

It defines how M-PIN may preserve Owner-controlled persistent continuity
while interacting with:

- retailers;
- marketplaces;
- commerce applications;
- payment services;
- delivery services;
- subscription services;
- physical stores;
- commerce AI;
- commerce robots;
- other compatible commerce services.

This Profile preserves the distinction between:

- Owner-controlled Commerce State;
- Friend Runtime;
- independent Commerce Service Records;
- transaction and payment authorization.

M-PIN does not replace the merchant’s transaction system.

------------------------------------------------------------------------

# 2. Commerce Thesis

The canonical Commerce principle is:

> **The Owner may preserve personal commerce continuity through M-PIN
> without turning M-PIN into the merchant’s transaction ledger or a
> shared customer database for every commerce service.**

Conceptually:

Owner │ ▼ M-PIN │ ├── Retailer Friend Folder ├── Payment Friend Folder
├── Delivery Friend Folder └── Commerce AI Friend Folder

while independently:

Retailer / Payment / Delivery │ ▼ legitimate Commerce Service Records

Common participation in one transaction does not erase Friend
boundaries.

------------------------------------------------------------------------

# 3. Owner and Customer

In commerce, **Owner** and **Customer** are distinct roles.

The same person may be both.

However:

# Owner

architectural authority over the applicable M-PIN

# Customer

person or entity participating in a commercial relationship

The two concepts MUST NOT be silently collapsed.

------------------------------------------------------------------------

# 4. Customer Account Is Not M-PIN Identity

A retailer account, marketplace account, payment account, or delivery
account does not automatically become M-PIN Identity.

Therefore:

merchant login ≠ M-PIN Owner Authority

and:

customer account ≠ M-PIN ownership

unless an explicit compatible integration establishes the relevant
relationship.

------------------------------------------------------------------------

# 5. Commerce Friend

A commerce service may participate as a Friend.

Examples include:

- Retailer Friend;
- Marketplace Friend;
- Payment Friend;
- Delivery Friend;
- Subscription Friend;
- Commerce AI Friend;
- in-store Friend.

Each Friend remains subject to the same Core identity, Folder,
permission, Session, Runtime, and persistence rules.

------------------------------------------------------------------------

# 6. One Commerce Friend, One Friend Folder

Each distinct Commerce Friend relationship has its own Friend Folder.

Example:

M-PIN ├── Retailer A Folder ├── Retailer B Folder ├── Payment Friend
Folder ├── Delivery Friend Folder └── Commerce AI Folder

The Owner’s common ownership of M-PIN does not create a shared commerce
memory pool.

------------------------------------------------------------------------

# 7. Commerce Friend Folder Isolation

Retailer A MUST NOT automatically read:

- Retailer B Folder;
- Payment Folder;
- Delivery Folder;
- Commerce AI Folder.

Likewise, those Friends MUST NOT automatically read Retailer A Folder.

Participation in the same purchase does not create cross-Friend Folder
authority.

------------------------------------------------------------------------

# 8. Same Corporate Group

Multiple commerce services owned by the same corporate group do not
automatically share M-PIN Friend Folder authority.

Corporate ownership ≠ Friend Folder authorization

If services are distinct Friends, their boundaries remain distinct.

------------------------------------------------------------------------

# 9. Owner-Controlled Commerce State

A Commerce Friend Folder may contain Friend-defined Owner-controlled
persistent state such as:

- preferences;
- size or fit information;
- selected delivery preferences;
- wish lists;
- subscription preferences;
- service settings;
- Owner-held receipts;
- Owner-held order information;
- personalization state;
- other Friend-specific continuity data.

These examples are not a mandatory universal schema.

------------------------------------------------------------------------

# 10. Current Payload May Contain Commerce History

Current-State-Only does not prohibit historical commerce content inside
the current payload.

For example, one current Friend payload may contain:

- prior orders;
- old receipts;
- historical wish-list entries;
- previous communications.

That is historical service content inside one Current State.

It is not M-PIN version-history or rollback semantics.

------------------------------------------------------------------------

# 11. Commerce Payload Semantics

The Commerce Friend defines the meaning and service-specific structure
of its payload.

M-PIN defines only the minimum boundary information necessary for
matters such as:

- Friend identity;
- Folder binding;
- authorization;
- integrity;
- applicable envelope metadata.

M-PIN does not require one universal product, order, receipt, or
shopping-preference schema.

The exact `.MPIN` container and serialization format remain deferred.

------------------------------------------------------------------------

# 12. Decision 120 in Commerce

For Commerce:

**Friend responsibility**

- payload semantics;
- service-specific payload composition;
- schema evolution;
- interpretation of commerce objects.

**M-PIN responsibility**

- Friend Folder association;
- authorization;
- isolation;
- minimum envelope requirements;
- integrity;
- persistence boundary.

This follows the v2.0 resolution of Decision 120.

------------------------------------------------------------------------

# 13. Commerce Service Record

A Commerce Service Record is an independent record legitimately
maintained by a commerce service for purposes such as:

- transaction processing;
- payment processing;
- invoices;
- tax;
- refunds;
- fraud prevention;
- accounting;
- delivery;
- disputes;
- security;
- regulatory or legal obligations.

Such records may persist independently from M-PIN Save.

------------------------------------------------------------------------

# 14. Owner State vs Commerce Service Record

Canonical distinction:

Owner-controlled M-PIN Commerce State ≠ Commerce Service Record

For example:

Owner purchases product ↓ merchant creates legitimate transaction record

does not require:

Owner M-PIN SAVE

Likewise:

Owner changes M-PIN Runtime preference ↓ NO SAVE ↓ M-PIN Current State
unchanged

The two persistence systems remain separate.

------------------------------------------------------------------------

# 15. Transaction Is Not Save

Completing a transaction MUST NOT automatically constitute M-PIN Save.

Examples:

- placing an order;
- charging a payment method;
- issuing an invoice;
- shipping a parcel;
- issuing a refund

may create legitimate Commerce Service Records.

They do not inherently mean:

Owner SAVE → M-PIN Commit

------------------------------------------------------------------------

# 16. No Save Does Not Cancel a Transaction

If a purchase is completed but the Owner does not Save M-PIN Runtime
changes:

the purchase does not disappear.

Therefore:

NO M-PIN SAVE ≠ transaction cancellation

M-PIN persistence is not a transaction rollback mechanism.

------------------------------------------------------------------------

# 17. M-PIN Deletion Does Not Delete Transaction Records

Deleting:

- M-PIN commerce state;
- a Commerce Friend Folder;
- an entire M-PIN

does not automatically delete legitimate independent:

- order records;
- invoices;
- payment records;
- tax records;
- refund records;
- delivery records.

External rights or obligations concerning those records remain outside
M-PIN Core.

------------------------------------------------------------------------

# 18. Service Record Retention Does Not Grant Folder Access

A retailer’s need to retain an invoice does not grant permanent access
to the Owner’s Friend Folder.

Likewise, a payment service’s need to retain transaction records does
not grant access to Retailer or Delivery Friend Folders.

Service Record retention ≠ M-PIN Session authority

------------------------------------------------------------------------

# 19. Service Record Anti-Loophole

A Commerce Friend MUST NOT:

1.  synchronize its entire Friend Folder;
2.  permanently duplicate the synchronized state outside M-PIN;
3.  label the duplicate a Commerce Service Record;
4.  use that label to bypass Owner-controlled persistence.

A Service Record requires an independently legitimate service, security,
transaction, contractual, regulatory, or legal basis.

------------------------------------------------------------------------

# 20. Native Commerce Experience

M-PIN does not replace the Friend’s normal commerce experience.

A Retailer Friend may retain its own:

- website;
- application;
- catalog;
- shopping cart;
- checkout;
- account interface;
- customer support;
- recommendation interface.

M-PIN supplies the authorized persistent relationship.

The Friend supplies the service.

------------------------------------------------------------------------

# 21. First Commerce Synchronization

Canonical first synchronization:

Owner ↓ initiates Sync ↓ identifies/opens applicable M-PIN ↓ Owner
authority established ↓ Commerce Friend Identity verified ↓ Friend
Folder resolved ↓ Folder absent ↓ Owner creation approval ↓ Folder
created and bound ↓ Session established ↓ Current/initial state loaded ↓
native Commerce Friend Runtime

The Friend MUST NOT silently create an M-PIN persistent relationship
without applicable Owner approval.

------------------------------------------------------------------------

# 22. Returning Commerce Synchronization

For an existing relationship:

Owner ↓ establishes M-PIN authority ↓ Commerce Friend verified ↓
existing Friend Folder resolved ↓ new Session ↓ Current State loaded ↓
native commerce Runtime

The existing Folder is reused.

------------------------------------------------------------------------

# 23. Commerce Runtime

After loading:

Commerce Friend Folder Current State A ↓ Load ↓ Commerce Runtime ↓
shopping interaction ↓ Runtime State B

Runtime State B does not automatically become M-PIN Current State B.

------------------------------------------------------------------------

# 24. Owner Save

Canonical Commerce persistence:

Current State A ↓ Load ↓ Commerce Runtime State B ↓ Owner SAVE ↓
Validation ↓ Atomic Commit ↓ Current State B

Owner Save controls M-PIN persistence.

------------------------------------------------------------------------

# 25. Save vs Commit

`SAVE` is the Owner’s persistence intent.

`Commit` is the successful M-PIN persistence transition.

The Friend may communicate the intended state through:

- full state;
- delta;
- transaction;
- chunks;
- another compatible representation.

The semantic result of a successful Save is one valid new Current State.

------------------------------------------------------------------------

# 26. Decision 095 in Commerce

Decision 095 is resolved semantically.

M-PIN v2.0 does not require one transport representation for Commerce
state.

It requires that a successful Owner Save result in:

> **one valid authoritative current Friend Folder state**

without creating mandatory M-PIN version-history semantics.

------------------------------------------------------------------------

# 27. Multiple Saves

An Owner may Save multiple times during one Commerce Session.

Example:

State₀ ↓ Save State₁ ↓ Save State₂

The authoritative M-PIN state is the latest successfully committed
Current State.

Core does not require State₀ and State₁ to remain available as
historical M-PIN versions.

------------------------------------------------------------------------

# 28. Personalization

A Commerce Friend may use its own Friend Folder to restore
Owner-authorized personalization.

Examples may include:

- preferred sizes;
- product preferences;
- delivery preferences;
- display settings;
- wish-list state.

The Friend interprets those semantics.

M-PIN does not become the recommendation engine.

------------------------------------------------------------------------

# 29. No Central Commerce Profile

M-PIN v2.0 does not create one universal Owner shopping profile
automatically visible to every retailer.

The prohibited default model is:

M-PIN ↓ universal shopping profile ↓ all retailers

Instead:

Retailer A ↔ Folder A Retailer B ↔ Folder B Payment ↔ Folder P Delivery
↔ Folder D

------------------------------------------------------------------------

# 30. Recommendation Need Is Not Permission

A retailer’s desire to improve recommendations does not create authority
to read another Friend’s Folder.

For example:

Retailer A wants more context ↓ requests Retailer B Folder

Expected:

DENY

Commercial usefulness does not override isolation.

------------------------------------------------------------------------

# 31. Advertising Is Not M-PIN Authorization

M-PIN access MUST NOT automatically be interpreted as authorization for
unrelated advertising or tracking.

Likewise:

advertising consent ≠ cross-Friend Folder access

Any applicable advertising, tracking, or secondary-use authorization
remains separately governed.

------------------------------------------------------------------------

# 32. Cross-Friend Commerce Need

Commerce frequently requires selected information to move between
services.

Example:

Retailer needs delivery information for Delivery Friend

or:

Retailer needs payment confirmation from Payment Friend

This need does not justify direct Friend Folder access.

------------------------------------------------------------------------

# 33. Owner-Mediated Disclosure Candidate

Healthcare and Commerce independently expose the same architectural
need:

selected information may need to move between Friend relationships
without sharing entire Friend Folders.

A candidate future mechanism is:

**Owner-Mediated Disclosure**

Conceptually:

Source Friend relationship ↓ selected data ↓ Owner authorization ↓
Disclosure ↓ Recipient Friend

This remains deferred from the frozen v2.0 Core.

------------------------------------------------------------------------

# 34. Disclosure Is Not Folder Sharing

A future Disclosure mechanism MUST preserve:

Disclosure ≠ recipient receives source Folder access

The recipient receives only selected authorized information.

The source Friend Folder remains isolated.

------------------------------------------------------------------------

# 35. Candidate Disclosure Object

A future generic Disclosure object may include concepts such as:

``` text
disclosure_id
owner_id
source_friend
recipient_friend
selected_data
purpose
authorization
validity
integrity
This list is illustrative.
It is not a frozen v2.0 schema.
```

# 36. Disclosure Scope

A future Disclosure may potentially be scoped as: one-time;
Session-bound; transaction-bound; time-limited; valid until revoked. The
exact mechanism is deferred.

# 37. Disclosure Does Not Transfer Ownership

Selected data disclosure does not automatically: transfer the source
Friend Folder; change Friend binding; make the recipient Owner; merge
two Friend Folders. Disclosure is a transfer mechanism, not a Folder
ownership mechanism.

# 38. Recipient Persistence

If a future Disclosure mechanism provides selected data to a recipient
Friend, that data does not automatically become recipient M-PIN
Persistent State. If it is to persist in the recipient Friend Folder,
the recipient relationship remains subject to its own applicable M-PIN
Save rules.

# 39. Payment Friend

A payment service may participate as a separate Friend. Example: M-PIN
├── Retailer Folder └── Payment Folder The Retailer Friend MUST NOT
automatically read the Payment Friend Folder. The Payment Friend MUST
NOT automatically read the Retailer Folder.

# 40. Payment Authorization Is Separate

M-PIN Owner Authority is not automatically payment authorization.
Therefore: M-PIN authentication ≠ payment authentication and: Owner SAVE
≠ authorize payment Payment authorization remains governed by the
payment service and applicable systems.

# 41. Raw Payment Credentials

M-PIN Core does not require storage of raw payment credentials in a
Friend Folder. A payment implementation may use: tokens;
provider-managed credentials; external authorization; other secure
payment mechanisms. Exact payment architecture is outside v2.0.

# 42. Payment Confirmation

A retailer may need confirmation that payment succeeded. That does not
require Retailer Friend access to the entire Payment Friend Folder.
Selected transaction results may be communicated through existing
payment infrastructure or a future authorized interoperability
mechanism.

# 43. Delivery Friend

A delivery service may be a separate Friend. Example: M-PIN ├── Retailer
Folder └── Delivery Folder The Retailer does not automatically receive
Delivery Folder access. The Delivery Friend does not automatically
receive the Retailer Folder.

# 44. Delivery Information

A delivery workflow may require selected information such as: recipient
information; delivery destination; delivery instructions. The need for
that information does not authorize access to all Owner data or the
entire Retailer Friend Folder.

# 45. Delivery Runtime Data

A Delivery Friend may temporarily use selected delivery information in
Runtime. Temporary Runtime use does not automatically create permanent
M-PIN history. Persistent M-PIN state follows the applicable Save model.
Legitimate delivery Service Records remain separately permitted.

# 46. Physical Retail

M-PIN may also be used in physical retail environments. Example: Owner ↓
M-PIN ↓ Retail Store Friend ↓ in-store Runtime The Core model does not
depend on commerce occurring through a web browser.

# 47. Physical Presence Is Not Authority

Entering a store or approaching a terminal does not automatically
establish M-PIN Owner Authority. Presence ≠ authentication Likewise,
possession of a store loyalty card does not automatically establish
M-PIN ownership unless an explicit compatible mechanism does so.

# 48. Shared Retail Terminals

Shared retail Devices may include: kiosks; fitting-room terminals;
checkout terminals; rental Devices; retail robots. One Owner’s M-PIN
Session MUST NOT transfer usable M-PIN authority to the next customer.

# 49. Residual Data

Commerce implementations SHOULD minimize residual: M-PIN plaintext;
Session credentials; delivery information; personalization data; Friend
Folder cache on shared or public commerce Devices after Session
termination.

# 50. Commerce AI

A Commerce AI may be a Friend separate from the Retailer. Example: M-PIN
├── Commerce AI Folder └── Retailer Folder The AI MUST NOT automatically
receive the Retailer Friend Folder. AI Profile requirements also apply.

# 51. AI Shopping Assistant

An AI shopping assistant may recommend products using information within
its own authorized relationship. If information from another Friend is
required, that need does not create direct Folder authority. A future
Disclosure mechanism may address selected transfer.

# 52. Commerce Robot

A retail robot may act as a Device hosting multiple Friends. Example:
Retail Robot ├── Interaction Friend ├── Retailer Friend ├── Payment
Friend └── Delivery Friend Physical co-location does not collapse Friend
Folder isolation. Robotics Profile requirements also apply.

# 53. Profile Composition

Commerce MAY compose with: AI Profile; Robotics Profile; Healthcare
Profile. Composition adds requirements. It does not weaken Core.

# 54. Healthcare Commerce Example

A pharmacy transaction may involve: Healthcare Friend Payment Friend
Delivery Friend Commerce Friend Each Friend retains its own Folder
relationship. Medical need and commercial need do not automatically
create a shared Folder.

# 55. Returns

A product return may create or modify legitimate Commerce Service
Records. A return is not an M-PIN rollback. Example: Order completed ↓
product returned ↓ merchant records return/refund does not mean: restore
old M-PIN version

# 56. Refunds

A refund may be processed independently of M-PIN Save. Payment and
merchant records may reflect the refund. Owner-controlled M-PIN state
changes only according to the applicable persistence process.

# 57. Warranty

Warranty records may be legitimate Commerce Service Records. Owner-held
warranty information may also exist in the applicable Friend Folder. The
two may coexist without becoming the same persistence system.

# 58. Subscription

A Subscription Friend may maintain legitimate service records
concerning: subscription status; billing; contractual period;
cancellation; required accounting. Owner-controlled preferences may
separately exist in the Friend Folder.

# 59. Subscription Cancellation Is Not Folder Deletion

Canceling a subscription does not automatically delete: the Friend
Folder; the M-PIN; legitimate Service Records. Likewise, deleting the
Friend Folder does not automatically cancel a contractual subscription.
These actions are distinct.

# 60. Commerce Friend Identity

A Commerce Friend must have sufficiently stable and verifiable identity
for Folder binding. Mutable labels such as: “Store” “Payment” “Delivery”
are insufficient by themselves as security identity. Exact credential
mechanisms remain deferred.

# 61. Merchant Rebranding

A retailer may change its name, application, or infrastructure without
necessarily becoming a new Friend. If legitimate Friend continuity
remains: same Friend ↓ same Friend Folder may continue. A display-name
change alone MUST NOT enable Folder theft.

# 62. Merchant Acquisition

If Company A acquires Retailer B: other Company A services do not
automatically gain Retailer B’s Friend Folder authority. Corporate
acquisition does not collapse Friend boundaries.

# 63. Marketplace Boundary

A marketplace may itself be a Friend while individual sellers operate
through the marketplace’s native service architecture. M-PIN v2.0 does
not require every marketplace seller to become a separate Friend. If an
implementation models a seller as an independent Friend, Core
requirements apply to that Friend. The exact marketplace seller boundary
remains implementation-specific.

# 64. Data Minimization

Commerce Friends SHOULD receive only the information required for their
authorized relationship or operation. For example, a delivery service
needing a delivery destination does not thereby require: shopping
history; unrelated payment data; AI conversation history; healthcare
data.

# 65. Identity Minimization

A Commerce Friend SHOULD avoid requesting broader identity information
than necessary for the applicable transaction or service. M-PIN is not a
universal government identity system.

# 66. Age or Eligibility Verification

Some commerce services may require age, eligibility, membership, or
jurisdiction checks. M-PIN Owner authentication does not automatically
satisfy those requirements. A separate applicable verification mechanism
may be required.

# 67. Secondary Use

Authorization to use M-PIN state for a Commerce Friend Runtime does not
automatically authorize unrelated: advertising; tracking; resale of
data; model training; cross-service profiling. Any such use requires its
own applicable basis.

# 68. No Automatic Cross-Service Profile

A Provider, retailer group, or commerce platform MUST NOT treat M-PIN
Friend Folder isolation as permission to silently construct one
universal cross-Friend Owner profile from synchronized payloads. Friend
Folder authority remains scoped.

# 69. Commerce Security Threats

Commerce deployments SHOULD account for threats including: fake merchant
identity; fake payment request; Friend Identity spoofing; unauthorized
delivery-address access; cross-store profiling; replayed authorization;
stolen Session context; compromised shared terminal; malicious Friend;
malicious Provider; compromised Storage.

# 70. Fake Merchant

A malicious service MUST NOT obtain a legitimate Retailer Friend Folder
merely by presenting the same display name as the real retailer. Friend
Identity verification and binding remain required.

# 71. Payment Request Integrity

A Friend’s request for payment does not itself establish payment
authorization. Payment systems must independently validate the
applicable transaction and authorization. M-PIN does not replace
payment-security protocols.

# 72. Replay Protection

Commerce Sessions and applicable authorization artifacts MUST follow
Core replay-resistance requirements. A previously valid M-PIN
authorization MUST NOT become unrestricted reusable authority. Exact
token formats remain deferred.

# 73. Public Terminal Threat

If a commerce terminal is compromised, M-PIN cannot guarantee secrecy of
plaintext legitimately exposed inside the compromised Runtime
environment. Implementations should minimize exposed data. The
compromise MUST NOT automatically authorize unrelated Friend Folders.

# 74. Malicious Commerce Friend

A malicious Friend may misuse plaintext legitimately received from its
own Friend Folder. M-PIN cannot retroactively erase knowledge already
disclosed to an authorized malicious Friend. It can still preserve:
other Folder isolation; future Session boundaries; future Save
authority; revocation boundaries.

# 75. Malicious Provider

Provider administrative authority MUST NOT be treated as Owner
Authority. However, if the implementation gives the Provider access to
decryption keys or plaintext, v2.0 does not claim confidentiality from
that Provider. The exact key architecture remains deferred.

# 76. Device Portability

The Owner may change Device without inherently changing the Commerce
Friend relationship. Example: Device A ↓ M-PIN X ↓ Retailer Folder A
later: Device B ↓ same M-PIN X ↓ same Retailer Folder A where valid
continuity is established.

# 77. Provider Portability

M-PIN Provider migration SHOULD preserve valid Commerce Friend Folder
relationships and Current State. Provider migration does not make the
new Provider the merchant or Owner.

# 78. Merchant Change Is Not Provider Migration

Changing from Retailer A to Retailer B is a Friend change. It is not
M-PIN Provider migration. Retailer B does not automatically inherit
Retailer A’s Friend Folder.

# 79. No Automatic Semantic Commerce Migration

M-PIN does not automatically translate: Retailer A payload ↓ Retailer B
payload The Friends may have different semantics and structures. A
future explicit interoperability mechanism may support selected transfer
without violating Folder isolation.

# 80. Recovery

Commerce recovery follows Core. Authority Recovery ≠ Data Recovery and:
M-PIN recovery ≠ transaction rollback

# 81. Stale Recovered State

A recovered Backup may contain commerce information older than the
merchant’s current Service Records. For example: recovered M-PIN
payload: order status = shipped merchant record: order status =
delivered M-PIN MUST NOT automatically overwrite the merchant’s
independent transaction record.

# 82. Backup Is Not Transaction Authority

Possession of an old M-PIN Backup does not authorize: refund; payment;
cancellation; delivery redirection; account takeover. Those operations
require their own applicable authority.

# 83. Friend Failure

If a retailer disappears, the Owner may retain its Friend Folder.
Another retailer does not automatically gain that Folder. Owner-held
historical content may remain in the Current State even if the original
service no longer operates.

# 84. Provider Failure

If the M-PIN Provider fails, valid M-PIN state may be recovered or
migrated where sufficient recovery material exists. This is independent
of whether the retailer remains operational.

# 85. Commerce Mandatory Requirements

A Commerce implementation claiming M-PIN v2.0 Commerce Profile
conformance MUST satisfy: \### COM-001 — Core Conformance The
implementation MUST satisfy all applicable M-PIN v2.0 Core requirements.
\### COM-002 — Owner / Customer Distinction The implementation MUST NOT
assume that M-PIN Owner status automatically satisfies every Customer,
payment, contractual, identity, or legal authorization requirement. \###
COM-003 — Commerce Friend Isolation Distinct Commerce Friends MUST NOT
automatically access each other’s Friend Folders. \### COM-004 — Service
Record Separation Owner-controlled Commerce State MUST remain
distinguishable from legitimate Commerce Service Records. \### COM-005 —
No Service Record Loophole Commerce Service Records MUST NOT be used as
a blanket mechanism to duplicate complete synchronized Friend Folder
state. \### COM-006 — Owner-Controlled Persistence Commerce Runtime
changes become M-PIN Persistent State only through the applicable Owner
Save process. \### COM-007 — Transaction Separation Purchase, payment,
refund, delivery, or other commerce events MUST NOT automatically
constitute M-PIN Save. \### COM-008 — Payment Separation M-PIN Owner
Authority or Save MUST NOT automatically constitute payment
authorization. \### COM-009 — No Direct Cross-Friend Folder Access
Selected cross-service data need MUST NOT be implemented as unrestricted
access to another Friend’s Folder. \### COM-010 — Recovery Separation
M-PIN recovery MUST NOT be represented as transaction rollback or
modification of independent Commerce Service Records.

# 86. Recommended Commerce Properties

A Commerce implementation SHOULD additionally satisfy: \### COM-011 —
Data Minimization Commerce Friends SHOULD receive only information
necessary for their authorized purpose. \### COM-012 — Shared Device
Hygiene Shared commerce Devices SHOULD minimize residual M-PIN plaintext
and credentials after Session termination. \### COM-013 — Identity
Minimization Commerce Friends SHOULD avoid requesting unnecessary
identity attributes. \### COM-014 — Purpose-Bounded Transfer Any future
selected cross-Friend transfer SHOULD remain limited to authorized
information and purpose. \### COM-015 — Personalization Transparency
Implementations SHOULD avoid implying that access to one Friend Folder
authorizes universal cross-service personalization.

# 87. Commerce Conformance Tests

The following tests supplement the Core suite.

# 88. COM-TEST-001 — Retailer Isolation

## Precondition

Retailer A ↔ Folder A Retailer B ↔ Folder B \## Action Retailer A
requests Folder B. \## Expected DENY

# 89. COM-TEST-002 — Payment Isolation

## Precondition

Retailer Folder and Payment Folder exist. \## Action Retailer requests
Payment Folder. \## Expected DENY

# 90. COM-TEST-003 — Delivery Isolation

## Precondition

Retailer Folder and Delivery Folder exist. \## Action Delivery Friend
requests Retailer Folder under ordinary Delivery authority. \## Expected
DENY

# 91. COM-TEST-004 — Purchase Without Save

## Precondition

M-PIN Current State = A. \## Action Owner completes a valid purchase.
Commerce Runtime changes. Owner does not perform M-PIN Save. Session
terminates. \## Expected M-PIN Current State remains A. Legitimate
merchant transaction records may persist.

# 92. COM-TEST-005 — Save Without Payment Meaning

## Action

Owner performs M-PIN Save during Commerce Session. \## Expected M-PIN
Current State may be committed. The Save alone does not authorize or
execute payment.

# 93. COM-TEST-006 — Refund

## Action

Merchant issues legitimate refund. \## Expected Merchant/payment Service
Records may change. The event does not constitute M-PIN rollback.

# 94. COM-TEST-007 — M-PIN Deletion

## Action

Owner deletes Commerce Friend Folder. \## Expected Independent
legitimate transaction, tax, payment, or refund records are not
automatically deleted.

# 95. COM-TEST-008 — Cross-Friend Data Need

## Action

Retailer requires selected delivery information. \## Expected The
Retailer is not granted unrestricted Delivery Friend Folder access.
Selected data must use an independently authorized mechanism.

# 96. COM-TEST-009 — Provider Migration

## Precondition

M-PIN X under Provider P1 contains Retailer Folder A. \## Action Owner
validly migrates M-PIN X to Provider P2. \## Expected Retailer A ↔
Folder A relationship remains where migration succeeds. Provider P2 does
not become Owner.

# 97. COM-TEST-010 — Merchant Change

## Precondition

Retailer A ↔ Folder A. \## Action Owner begins using Retailer B. \##
Expected Retailer B does not automatically inherit Folder A.

# 98. COM-TEST-011 — Historical Commerce Content

## Precondition

one current Retailer payload contains prior order history. \## Action
M-PIN loads the Current State. \## Expected The payload is not invalid
merely because it contains historical commerce content. This does not
create M-PIN version-history semantics.

# 99. COM-TEST-012 — Shared Retail Terminal

## Precondition

Owner A ends a Session on shared commerce Device. \## Action Owner B
uses the same Device. \## Expected Owner B cannot obtain Owner A’s
usable M-PIN Session or Friend Folder authority.

# 100. Commerce Non-Goals

This Profile does not define: universal product schema; universal order
schema; universal receipt schema; universal payment protocol;
card-processing standard; banking authorization; tax rules; refund law;
delivery protocol; marketplace seller model; advertising-consent
framework; universal commerce identity; universal loyalty system;
automatic cross-retailer profile; automatic semantic migration between
merchants.

# 101. Deferred Commerce Mechanisms

The following remain outside the frozen v2.0 Commerce Profile: generic
Disclosure schema payment authorization integration delivery
authorization schema merchant trust registry marketplace seller identity
model commerce provenance schema cross-retailer semantic mapping
age/eligibility credential integration commerce-specific freshness
mechanism transaction-bound Disclosure token These may be standardized
later if Core boundaries remain intact.

# 102. Commerce Profile Invariants

The Commerce Profile is governed by these invariants: \## Owner and
Customer are distinct architectural concepts. \## Customer account is
not M-PIN Identity. \## One Commerce Friend has one Friend Folder. \## A
transaction does not erase Friend Folder isolation. \## Owner-controlled
Commerce State is not the merchant’s transaction ledger. \## Purchase is
not M-PIN Save. \## Payment authorization is not M-PIN Save. \## No Save
does not cancel a completed transaction. \## M-PIN deletion does not
automatically delete legitimate transaction records. \## Service Record
retention does not grant permanent Friend Folder authority. \## A
retailer does not automatically read Payment or Delivery Friend Folders.
\## Advertising or personalization need does not create cross-Friend
authority. \## Current-State-Only does not prohibit historical business
content inside the current payload. \## M-PIN recovery is not
transaction rollback. \## A new merchant does not automatically inherit
another merchant’s Friend Folder. \## Provider migration does not change
who the Owner is.

# 103. Canonical Commerce Architecture

                              OWNER
                                │
                                ▼
                              M-PIN
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼
    Retailer Folder       Payment Folder       Delivery Folder
          │                     │                     │
          ▼                     ▼                     ▼
    Retailer Friend       Payment Friend       Delivery Friend
          │                     │                     │
          ▼                     ▼                     ▼
    Native Retail          Payment Runtime      Delivery Runtime
       Runtime

Separately:

Retailer / Payment / Delivery services │ ▼ legitimate Service Records No
transaction requires these Friend Folders to become one shared Folder.

# 104. Commerce Persistence Model

Commerce Friend Folder Current State₀ │ ▼ Load │ ▼ Commerce Friend
Runtime │ ├── browse ├── personalize ├── select └── interact │ ▼ Runtime
State′ │ Owner SAVE │ ▼ Validation │ ▼ Atomic Commit │ ▼ Commerce Friend
Folder Current State₁ A transaction may independently occur: Commerce
Runtime │ ▼ purchase / payment / delivery │ ▼ Commerce Service Record
The two paths are not identical.

# 105. Cross-Friend Commerce Model

The forbidden default is: Retailer │ ├── reads Payment Folder ├── reads
Delivery Folder └── reads other Retailer Folders The Core model remains:
Retailer ↔ Retailer Folder Payment ↔ Payment Folder Delivery ↔ Delivery
Folder If selected transfer is later standardized: Source Friend │
selected information │ Owner authorization ▼ Disclosure │ ▼ Recipient
Friend The source Folder remains isolated.

# 106. Cross-Profile Finding

Healthcare and Commerce independently produce the same interoperability
problem: A Friend may legitimately need selected information associated
with another Friend without needing or receiving access to the other
Friend’s entire Folder. This validates the architectural usefulness of a
future Owner-Mediated Disclosure primitive. However, the finding does
not reopen v2.0 Core. For v2.0: \## Owner-Mediated Disclosure V2-NEW +
Cross-Profile Finding + Candidate Interoperability Primitive + DEFERRED
FROM CORE There is no Core 13.

# 107. Commerce Profile Thesis

M-PIN does not attempt to become the store. It does not become: the
payment network; the merchant ledger; the delivery network; the tax
system; the advertising platform. Those services continue to operate
independently. Instead, M-PIN establishes a persistent Owner-controlled
boundary around the Owner’s relationship with each compatible Friend.
The retailer may retain legitimate transaction records. The payment
service may retain legitimate payment records. The delivery service may
retain legitimate delivery records. But those facts do not require the
Owner’s entire persistent commerce state to become a shared
service-owned profile. The architecture therefore separates: the
transaction that happened from: the Owner state that persists through
M-PIN and separates: selected information needed by another service
from: access to another Friend’s entire Friend Folder Therefore: The
merchant may own its transaction record. The Owner may own the
persistent M-PIN relationship. Neither requires the other to disappear.

## M-PIN v2.0 — Profile 04 / Commerce

## Status: FROZEN
