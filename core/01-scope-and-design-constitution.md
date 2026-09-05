# M-PIN v2.0

## Core 01 — Scope & Design Constitution

**Status:** FROZEN **Version:** 2.0 **Document Type:** Normative Core
Specification

------------------------------------------------------------------------

# 1. Purpose

This document defines the scope, constitutional boundaries, and design
discipline of M-PIN v2.0.

It establishes what M-PIN is, what the Core is responsible for, what
remains outside the Core, and the rules that all subsequent M-PIN v2
Core documents and Profiles MUST preserve.

This document does not define a particular implementation.

------------------------------------------------------------------------

# 2. M-PIN Definition

M-PIN is an Owner-centered architecture for persistent data ownership
and service-independent digital continuity.

Under M-PIN:

- the Owner retains authority over Owner-controlled persistent data;
- a Friend provides its own service;
- a Friend continues to control its own Runtime, UX, internal
  implementation, and service semantics;
- a Friend interacts only with the M-PIN data area authorized for that
  Friend;
- Runtime activity does not automatically become M-PIN Persistent State;
- persistent change is governed by the Owner-controlled persistence
  model.

The architectural relationship is:

``` text
                         OWNER
                           │
                    Owner Authority
                           │
                           ▼
                         M-PIN
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
Friend Folder A      Friend Folder B      Friend Folder C
       │                   │                   │
       ▼                   ▼                   ▼
    Friend A            Friend B            Friend C
       │                   │                   │
    Runtime             Runtime             Runtime
       │                   │                   │
   Native UX           Native UX           Native UX
```

# 3. Core Thesis

## M-PIN separates service execution from persistent data ownership.

A Friend may execute a service. That fact alone does not make the Friend
the architectural Owner of the Owner-controlled persistent M-PIN state.

# 4. Owner Sovereignty

The Owner is the central authority of M-PIN. The architecture MUST NOT
redefine any of the following as the Owner merely because they provide
infrastructure or service execution: Friend Friend Account Device
Storage M-PIN Service Provider M-PIN MUST preserve the distinction
between service authority and Owner authority.

# 5. Friend

A Friend is an external service principal that may interact with M-PIN
under Owner-authorized conditions. A Friend MAY represent services in
different industries, including but not limited to: AI robotics
healthcare commerce transportation future digital or physical services
The Core MUST NOT assume that a Friend is an AI service.

# 6. Friend Sovereignty

A Friend remains responsible for its own: service Runtime native UX
internal implementation internal algorithms business policies service
semantics product evolution M-PIN MUST NOT become the general operating
authority of the Friend. M-PIN governs the boundary through which the
Friend interacts with Owner-controlled persistent state.

# 7. Friend Folder

A Friend Folder is the Owner-owned persistent M-PIN data area associated
with one specific Friend. The canonical relationship is: \## One Friend,
One Friend Folder. A Friend Folder is not merely a visual folder or UI
convention. It represents a structural association and access boundary
between a Friend and the Owner-controlled persistent state associated
with that Friend.

# 8. Friend Folder Isolation

The presence of multiple Friend Folders within one M-PIN MUST NOT imply
common Friend visibility. Conceptually: M-PIN

├── Friend A Folder ← Friend A ├── Friend B Folder ← Friend B └── Friend
C Folder ← Friend C Friend A MUST NOT receive default access to Friend B
Folder. Common Owner-controlled storage does not mean common Friend
access.

# 9. Domain Terminology

M-PIN v2.0 does not define a separate Core entity named Domain in
addition to Friend Folder. Historical M-PIN v1 material may contain
Domain terminology. Where that terminology refers to a Friend-specific
persistent data area, v2 uses the normative term: \## Friend Folder
Historical wording remains part of v1 provenance and MUST NOT be
silently rewritten.

# 10. Native Friend Experience

M-PIN does not replace the Friend’s workspace. A conforming Friend
remains free to use its existing: application interface service workflow
Runtime interaction model M-PIN synchronization SHOULD integrate with
the Friend without requiring the Owner to use a universal replacement
interface for the Friend service.

# 11. Runtime and Persistence

M-PIN distinguishes temporary Runtime State from Persistent State.
Persistent State ↓ LOAD Runtime State ↓ Friend processing A Runtime
change MUST NOT automatically be treated as an M-PIN Persistent State
change. The persistence boundary is defined separately from the Friend’s
Runtime behavior.

# 12. Owner-Controlled Persistence

The canonical persistence model is: Persistent State A ↓ LOAD Runtime
State A ↓ WORK Runtime State B ↓ OWNER SAVE Commit ↓ Persistent State B
Without Owner Save: Persistent State A ↓ LOAD Runtime State ↓ WORK
Runtime State B ↓ NO SAVE Session End ↓ Persistent State A remains
Therefore: \## Runtime Change ≠ Persistent Change is a Core invariant.

# 13. Current State

M-PIN Core represents the current committed Persistent State. The Core
does not require: version history; automatic historical snapshots;
rollback history; time travel; perpetual state archives. This rule does
not prohibit protected backups of the current state. It also does not
prohibit a Friend’s current payload from containing historical service
content where that content is part of the Friend’s current service
state. For example, a current Friend state may contain a current
conversation list, order history, or healthcare document set. M-PIN
state history and historical content inside current Friend state are
different concepts.

# 14. Synchronization

M-PIN interaction with a Friend occurs through a Synchronization
Session. The canonical invariant is: \## One M-PIN, One Active Friend,
One Synchronization Session. The detailed Session lifecycle is defined
by Core 08.

# 15. First Friend Synchronization

When a Friend synchronizes with an M-PIN for the first time: Owner
initiates synchronization ↓ M-PIN authentication ↓ Friend identity
verification ↓ Friend Folder lookup ↓ Folder not found ↓ Owner approval
↓ Friend Folder creation ↓ Synchronization Session A missing Friend
Folder MUST NOT be created without the required Owner authorization.

# 16. Returning Synchronization

If the Friend Folder already exists, a subsequent authorized
Synchronization Session uses that existing Folder. Conceptually:
Existing Friend Folder ↓ Current committed state ↓ Friend Runtime The
Friend uses the synchronized state through its own Runtime and native
service experience.

# 17. Zero Requirement

M-PIN defines behavioral requirements rather than mandating one
implementation technology. The Core MUST NOT require every Friend to use
one particular: SDK API programming language Runtime database operating
system cloud provider user interface A conforming implementation MUST
satisfy the required M-PIN behavior regardless of internal
implementation choice.

# 18. M-PIN Standard and Service Provider

M-PIN v2 distinguishes: M-PIN Standard ≠ M-PIN Service Provider An M-PIN
Service Provider is an optional implementation or deployment role. A
Provider MAY provide functions such as: hosting; storage; authentication
infrastructure; recovery infrastructure; synchronization infrastructure;
migration support. The Provider MUST NOT become the Owner merely by
providing those functions.

# 19. Provider Independence

The M-PIN Core MUST NOT require permanent architectural dependence on
one named M-PIN Service Provider. A conforming architecture MAY support:
Provider-hosted deployment; Owner-managed local deployment;
Owner-controlled cloud storage; removable storage; other conforming
deployment models. The detailed portability requirements are defined in
Core 11.

# 20. Device Independence

M-PIN identity and continuity MUST NOT inherently depend on one physical
Device. Conceptually: Device A ↓ same M-PIN

Device B ↓ same M-PIN Changing a Device does not by itself create a new
Owner or a new M-PIN.

# 21. Core Neutrality

The M-PIN Core MUST remain industry-neutral. The Core MUST NOT contain
healthcare-specific, commerce-specific, robotics-specific, or
AI-specific business logic merely because a Profile needs it. The
governing design test is: \## The Core should not need to know the
industry.

# 22. Core and Profiles

M-PIN v2 uses two architectural layers: M-PIN CORE │ ├── universal
ownership boundary ├── identity ├── Friend / Friend Folder ├──
permission ├── Session ├── Runtime / Persistence ├── security ├──
portability └── conformance

PROFILES │ └── domain-specific requirements A Profile MAY add
requirements necessary for a particular environment. A Profile MUST NOT
weaken a Core requirement.

# 23. v2.0 Validation Profiles

M-PIN v2.0 contains four validation Profiles: AI Robotics Healthcare
Commerce These Profiles validate the same Core. They do not define four
different M-PIN architectures.

# 24. Profile Composition

A single real-world environment MAY involve more than one Profile. For
example, a healthcare robot containing an AI service may involve: M-PIN
Core + Robotics Profile + Healthcare Profile + AI Profile Profile
composition MUST preserve Core isolation and Owner authority.

# 25. Service Records

M-PIN distinguishes Owner-controlled M-PIN Persistent State from records
independently maintained by a Friend for legitimate service,
institutional, operational, security, or legal purposes.
Owner-controlled M-PIN State ≠ Friend Service Record A Service Record
MUST NOT be treated as permission to copy unrelated or excessive M-PIN
state. M-PIN does not automatically replace a Friend’s independent
recordkeeping obligations.

# 26. Security Scope

M-PIN security is concerned primarily with preserving: Owner authority;
authentication boundaries; Friend identity; Friend Folder isolation;
authorization; Session validity; persistent-state integrity; Save
authority; portability and recovery authority. Detailed security
requirements are defined in Core 10.

# 27. Security Non-Goal

M-PIN does not claim complete control over a malicious Friend after that
Friend has legitimately received authorized plaintext for processing. A
fully compromised authorized Runtime may be capable of copying
information made available to it. M-PIN MUST therefore minimize and
enforce the authorized boundary rather than claim impossible control
over all internal Friend behavior.

# 28. Portability

M-PIN aims to preserve Owner continuity when: Device changes; Storage
changes; Location changes; M-PIN Service Provider changes. Portability
MUST NOT inherently require creation of a new Owner identity or
replacement M-PIN identity.

# 29. Recovery

Recovery aims to restore legitimate Owner authority to the same M-PIN
where possible. The Core distinguishes: Authority Recovery ≠ Data
Recovery Recovery of authority cannot recreate data that no longer
exists in any recoverable form.

# 30. Conformance

M-PIN compatibility is defined by observable required behavior.
Conformance MUST NOT depend solely on whether an implementation uses a
particular technology branded as M-PIN. Independent implementations may
differ internally while remaining conformant if they preserve the
normative Core behavior. Detailed requirements are defined in Core 12.

# 31. Interoperability Boundary

Friend Folder Isolation is the v2.0 Core baseline. A Friend MUST NOT
receive direct access to another Friend’s Folder merely because
information exchange between services would be useful. Healthcare and
Commerce Profile validation identified a possible future
interoperability primitive based on Owner-authorized selected
disclosure. That mechanism is recorded as: Owner-Mediated Disclosure
V2-NEW CANDIDATE DEFERRED FROM v2.0 CORE Its exact protocol is not part
of the frozen v2.0 Core. Any future interoperability mechanism MUST
preserve Friend Folder Isolation unless a later version explicitly
changes the architecture.

# 32. Design Non-Goals

M-PIN Core does not define: AI model architecture; robot control
systems; clinical systems; payment networks; merchant systems;
transportation systems; universal business logic; universal Friend UI;
universal Friend database format. M-PIN is not intended to replace those
systems.

# 33. Implementation Non-Goals

M-PIN v2.0 Architecture does not freeze a particular: .MPIN
binary/container representation; serialization format; cryptographic
algorithm suite; key hierarchy; Session token representation; network
transport; Provider discovery mechanism; recovery algorithm; heartbeat
interval; Disclosure schema. Those choices are deferred unless a
normative Core requirement specifically constrains their behavior.

# 34. Design Discipline

M-PIN v2 follows a finite specification discipline. Once a requirement
is LOCKED or FROZEN, it MUST NOT be reopened merely because: the same
question is rephrased; a new example appears; another industry is
considered; a different implementation preference is proposed. A frozen
requirement SHOULD be reconsidered only when there is evidence of: an
actual internal contradiction; a security defect; implementation
impossibility; material conformance ambiguity.

# 35. Historical Integrity

M-PIN v1 remains the historical design baseline. v2 MUST NOT silently
rewrite v1 Decisions to make later v2 concepts appear older than they
are. Later formalizations MUST be classified according to their actual
provenance.

# 36. External Reference Rule

External technologies, products, or standards MAY be used for comparison
or engineering analysis. Their similarity to M-PIN does not
automatically make them: part of M-PIN provenance; a source of v1
architecture; evidence of derivation; evidence of copying. Such claims
require independent evidence.

# 37. Constitutional Invariants

The following invariants govern all M-PIN v2 Core documents and
Profiles. \### C-01 — Owner Centrality The architecture MUST remain
centered on the Owner. \### C-02 — Persistent Ownership Boundary
Owner-controlled M-PIN Persistent State MUST remain under Owner
authority. \### C-03 — Friend Sovereignty M-PIN MUST NOT assume control
over Friend internal operation. \### C-04 — Friend Folder Isolation A
Friend MUST NOT receive default access to another Friend’s Friend
Folder. \### C-05 — Explicit Persistence Runtime change MUST NOT
automatically become M-PIN Persistent State. \### C-06 — Native Friend
Experience M-PIN MUST NOT require replacement of the Friend’s native
service experience. \### C-07 — Zero Requirement Conformance MUST NOT
depend on one mandatory internal implementation technology. \### C-08 —
Core Neutrality Core MUST remain independent of industry-specific
business logic. \### C-09 — Device Independence M-PIN continuity MUST
NOT inherently depend on one Device. \### C-10 — Provider Independence
The Standard MUST NOT inherently depend on one permanent Provider. \###
C-11 — Session Boundary M-PIN access MUST occur through bounded
synchronization authority. \### C-12 — Verifiable Conformance Required
security and ownership boundaries MUST be testable through observable
behavior.

# 38. v2.0 Core Boundary

The M-PIN v2.0 Core consists of: 01 Scope & Design Constitution 02 Core
Principles 03 Terminology 04 Core Architecture 05 Owner & Identity 06
Friend & Friend Folder Model 07 Permission Model 08 Session Protocol 09
Runtime & Persistence 10 Security & Threat Model 11 Portability &
Recovery 12 Conformance Specification No additional Core document is
required for v2.0 completion.

# 39. Version Boundary

M-PIN v2.0 is frozen at this architectural boundary. Future changes are
classified as: compatible clarification ↓ v2.1

architectural redesign ↓ v3 A new implementation technique or industry
example does not by itself constitute architectural redesign.

# 40. Constitutional Thesis

The M-PIN v2 Constitution can be reduced to five statements: \## The
Owner is the center. \## The Friend provides the service without
becoming the Owner of M-PIN persistent state. \## One Friend is
associated with one isolated Friend Folder. \## Runtime activity becomes
M-PIN Persistent State only through the Owner-controlled persistence
boundary. \## The Core remains neutral to Friend, Device, industry, and
Provider implementation.

## M-PIN v2.0 — Core 01 / Scope & Design Constitution

## Status: FROZEN
