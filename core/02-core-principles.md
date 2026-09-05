# M-PIN v2.0

## Core 02 — Core Principles

**Status:** FROZEN **Version:** 2.0 **Document Type:** Normative Core
Specification

------------------------------------------------------------------------

# 1. Purpose

This document defines the normative principles of M-PIN v2.0.

These principles constrain all other Core documents, Profiles,
conforming Friend implementations, and M-PIN Service Provider
implementations.

The principles describe required architectural behavior.

They do not mandate one internal implementation technology.

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and
**MAY** are used normatively.

------------------------------------------------------------------------

# 2. Principle Set

M-PIN v2.0 defines fifteen Core Principles:

``` text
P-01  Owner Centrality
P-02  Owner Data Sovereignty
P-03  Friend Sovereignty
P-04  One Friend, One Friend Folder
P-05  Friend Folder Isolation
P-06  Explicit Owner Authority
P-07  Runtime / Persistence Separation
P-08  Owner-Controlled Persistence
P-09  Current-State-Only
P-10  Native Friend Experience
P-11  Zero Requirement
P-12  Bounded Synchronization
P-13  Device Independence
P-14  Provider Independence
P-15  Core Neutrality
These principles MUST be interpreted together.
No individual principle may be used to invalidate another Core principle.
```

### P-01 — Owner Centrality

## The Owner is the center of M-PIN.

M-PIN MUST be designed around the Owner rather than around a specific
Friend, Device, Storage location, or M-PIN Service Provider.
Conceptually: Friend A ─┐ Friend B ─┼──► M-PIN ◄── Owner Authority
Friend C ─┘ The architecture MUST NOT invert this relationship into:
Friend │ └── owns or governs Owner’s M-PIN A Friend participates in the
Owner’s M-PIN architecture. The Owner does not become a subordinate data
tenant of the Friend merely because the Friend provides a service.

### P-02 — Owner Data Sovereignty

## Owner-controlled M-PIN Persistent State remains under Owner authority.

A Friend MAY process Owner-authorized data while providing its service.
A Provider MAY store or transport protected M-PIN state. Neither role
alone transfers M-PIN ownership authority. The architecture MUST
distinguish: processing authority storage capability service authority
administrative capability from: Owner authority This principle concerns
M-PIN Owner-controlled state. It does not assert that every record
independently created or legally maintained by a Friend is an
Owner-controlled M-PIN record.

### P-03 — Friend Sovereignty

## M-PIN controls the ownership boundary, not the Friend’s internal service.

A Friend remains responsible for its own: Runtime; UX; algorithms;
service logic; internal architecture; data semantics; business policy;
product evolution. M-PIN MUST NOT require control over Friend internals
merely to preserve Owner data sovereignty. A Friend MAY evolve
independently as long as its M-PIN-visible behavior remains conformant.

### P-04 — One Friend, One Friend Folder

## One Friend is associated with one Friend Folder within an M-PIN.

The Friend Folder is the persistent M-PIN data area associated with that
Friend. Conceptually: Friend A ↕ Friend Folder A The association MUST be
stable enough for M-PIN to resolve the correct Friend Folder during
later Synchronization Sessions. A Friend MUST NOT arbitrarily bind
itself to another Friend’s Folder. Friend identity and Folder binding
requirements are defined in later Core documents.

### P-05 — Friend Folder Isolation

## A Friend’s Folder is not a shared data pool for other Friends.

Conceptually: M-PIN

├── Friend Folder A ← Friend A ├── Friend Folder B ← Friend B └── Friend
Folder C ← Friend C The default relationship MUST be: Friend A → Friend
Folder A Friend A ✕ Friend Folder B Friend A ✕ Friend Folder C A common
M-PIN container, storage location, Device, or Provider MUST NOT imply
common Friend visibility. Friend Folder Isolation is an access and
visibility boundary, not merely a file-organization convention. A future
interoperability mechanism MUST NOT silently convert Friend Folder
Isolation into universal cross-Friend Folder access.

### P-06 — Explicit Owner Authority

## Service need does not create M-PIN authority.

A Friend wanting, needing, or benefiting from data does not itself
authorize access. Required M-PIN actions MUST occur under valid Owner
authority as specified by the relevant protocol. This includes, where
applicable: initial authorization; Friend Folder creation;
Synchronization Session establishment; persistence authorization;
recovery; migration. The architecture MUST distinguish: Friend request ≠
Owner authorization and: authentication ≠ authorization

### P-07 — Runtime / Persistence Separation

## Runtime State and M-PIN Persistent State are different states.

A Friend may create, transform, infer, or temporarily hold data during
Runtime. That Runtime activity MUST NOT automatically modify the
authoritative M-PIN Persistent State. Conceptually: Persistent State ↓
LOAD Runtime State ↓ WORK Runtime State’ At this point: Runtime State’ ≠
new M-PIN Persistent State until the persistence requirements are
satisfied.

### P-08 — Owner-Controlled Persistence

## Persistence into M-PIN follows Owner persistence intent.

The canonical flow is: Persistent State A ↓ LOAD Runtime State A ↓ WORK
Runtime State B ↓ OWNER SAVE Commit ↓ Persistent State B Without Owner
Save: Persistent State A ↓ LOAD Runtime State ↓ WORK Runtime State B ↓
NO SAVE ↓ Session End ↓ Persistent State A remains A Friend MUST NOT
silently convert ordinary Runtime activity into an M-PIN Commit. SAVE
represents Owner persistence intent. COMMIT represents the technical
application of that authorized persistence change.

### P-09 — Current-State-Only

## M-PIN Core preserves the current committed state, not an automatic M-PIN state history.

M-PIN Core does not require: historical versions; automatic snapshots;
rollback; time travel; perpetual state archives. A new valid Commit
establishes the new authoritative current M-PIN state for the relevant
persistence scope. Protected backup copies MAY exist. Backups MUST NOT
automatically be interpreted as user-visible version history. This
principle does not prohibit historical service content from existing
inside the Friend’s current payload. For example: current AI Friend
payload may contain conversation history

current Commerce Friend payload may contain order history

current Healthcare Friend payload may contain documents from earlier
care The distinction is: historical content inside current state ≠
historical versions of M-PIN state

### P-10 — Native Friend Experience

## M-PIN does not replace the Friend’s service experience.

A Friend SHOULD continue to present its service through its own native
UX and Runtime. M-PIN MUST NOT require every Friend to move its service
into a universal M-PIN workspace. Conceptually: M-PIN │ Synchronization
▼ Friend Runtime │ ▼ Friend Native UX The Owner may therefore use M-PIN
continuity without abandoning the normal Friend service experience.

### P-11 — Zero Requirement

## M-PIN standardizes required behavior without requiring one internal implementation method.

The Core MUST NOT require every Friend to adopt one specific: SDK; API;
programming language; database; operating system; Runtime; cloud
platform; user interface. Two implementations MAY be internally
different and still be conformant. Conformance depends on required
observable behavior. Zero Requirement does not mean “no requirements.”
It means: \## no unnecessary requirement on how the Friend internally
achieves the required M-PIN behavior.

### P-12 — Bounded Synchronization

## M-PIN access occurs through a bounded Synchronization Session.

The v2.0 synchronization invariant is: \## One M-PIN, One Active Friend,
One Synchronization Session. A Session MUST have a defined authorization
and termination boundary. A terminated Session MUST NOT remain a hidden
permanent M-PIN access channel. Abnormal disconnection MUST NOT silently
cause unsaved Runtime State to become Persistent State. The detailed
state machine is defined in Core 08.

### P-13 — Device Independence

## M-PIN continuity is not inherently tied to one physical Device.

Conceptually: Device A │ ▼ M-PIN ▲ │ Device B Changing a Device MUST NOT
inherently require creation of: a new Owner; a new M-PIN identity; a new
Friend Folder set. Device authentication or migration procedures MAY
differ between implementations. The architectural continuity principle
remains unchanged.

### P-14 — Provider Independence

## M-PIN Standard is not one M-PIN Service Provider.

Conceptually: M-PIN Standard │ ┌─────────┼─────────┐ │ │ │ Local
Provider A Provider B A Provider MAY supply infrastructure. The Provider
MUST NOT become the architectural Owner merely because it hosts or
administers that infrastructure. The Core MUST NOT require permanent
dependence on one named Provider. A conforming portability model SHOULD
permit movement between compatible environments without silently
creating a new M-PIN identity. Provider Independence does not mean that
every implementation must support every migration mechanism. The
normative portability requirements are defined in Core 11.

### P-15 — Core Neutrality

## The M-PIN Core does not need to know the industry.

The same Core MUST be capable of describing materially different Friend
environments without embedding their business logic into the Core. For
example: AI Robotics Healthcare Commerce use the same fundamental M-PIN
architecture. Industry-specific requirements belong in Profiles where
possible. A Profile MAY strengthen requirements for its environment. A
Profile MUST NOT weaken the Core.

# 3. Principle Interaction

The fifteen principles form one architecture. For example, P-02 Owner
Data Sovereignty MUST NOT be interpreted to violate P-03 Friend
Sovereignty. Therefore M-PIN does not obtain Owner sovereignty by taking
control of the Friend’s entire internal service. Similarly, P-05 Friend
Folder Isolation MUST NOT be interpreted to prohibit every future form
of authorized interoperability. It prohibits unauthorized direct
cross-Friend Folder access. Any interoperability mechanism must preserve
the relevant Owner authority and isolation boundaries.

# 4. Ownership and Service Independence

The combined effect of P-01, P-02, and P-03 is: Owner owns / authorizes
Owner-controlled persistent M-PIN state

Friend controls service execution

M-PIN preserves the boundary This is a separation of responsibilities.
It is not a requirement that M-PIN take over the Friend.

# 5. Isolation and Interoperability

P-04 and P-05 establish the v2.0 default: One Friend ↓ One Friend Folder
not: All Friends ↓ Shared universal data pool Healthcare and Commerce
validation later identified a possible Owner-Mediated Disclosure
mechanism. For v2.0 it remains: CANDIDATE DEFERRED FROM CORE Therefore
no conforming Core implementation is required to support cross-Friend
Disclosure merely to satisfy Core 02.

# 6. Persistence and Friend Internal Behavior

P-07 and P-08 govern M-PIN persistence. They do not require a Friend to
eliminate every internal autosave, cache, transaction record, or
operational record from its own service. The relevant distinction is:
Friend internal/service behavior vs M-PIN Persistent State A Friend’s
own operational behavior does not automatically constitute an M-PIN
Commit. Likewise, an M-PIN Save does not automatically determine whether
an independent legal or transactional Friend action occurred.

# 7. Service Records

Some Friends legitimately maintain independent Service Records. Examples
may include: clinical records; transaction records; billing records;
regulatory records; safety records; security records. Therefore:
Owner-controlled M-PIN State ≠ Friend Service Record This distinction
MUST NOT be used as a loophole to copy unrelated M-PIN state.

# 8. Security Interpretation

The Principles do not claim that M-PIN can control all behavior inside
an authorized malicious Runtime. When plaintext has legitimately been
disclosed to a Friend for processing, a fully compromised Friend may be
technically capable of copying that plaintext. M-PIN therefore MUST
focus on: correct authorization; minimum required exposure; Friend
Folder isolation; Session boundaries; integrity; persistence authority;
recovery authority. The Core MUST NOT make security claims that its
architecture cannot technically enforce.

# 9. Storage Independence

M-PIN persistent state MAY be held through different compatible storage
environments. Examples include: local Device storage Owner-controlled
cloud storage removable storage Provider-hosted storage The storage
location does not by itself become the Owner. Storage independence MUST
preserve the other Core Principles.

# 10. Backup and Active Continuity

P-13 and P-14 permit continuity across devices and environments. This
does not imply unrestricted simultaneous active clones. Protected backup
copies MAY exist. The architecture nevertheless maintains the logical
requirement of one authoritative active continuity. Fully disconnected
offline clones create an enforcement limitation that may require
implementation-specific coordination. M-PIN v2.0 does not claim a
universal solution to that distributed-systems problem.

# 11. Principle Precedence

No Profile, Provider policy, Friend convenience, or implementation
choice MAY override these Core Principles while claiming full M-PIN v2.0
Core conformance. Where two requirements appear to conflict,
implementations MUST interpret them in a way that preserves the
constitutional invariants defined in Core 01. If no such interpretation
is possible, the conflict MUST be treated as a specification issue
rather than silently weakening a Core principle.

# 12. Conformance Implication

The Principles are not merely aspirational statements. Core 12 converts
them into observable conformance requirements and tests. For example:
P-05 Friend Folder Isolation ↓ attempt unauthorized Folder access ↓
access MUST fail and: P-08 Owner-Controlled Persistence ↓ modify Runtime
without Owner Save ↓ terminate Session ↓ Persistent State MUST remain
unchanged The implementation technology may differ. The required
behavior may not.

# 13. Principle Stability

The fifteen principles are FROZEN for M-PIN v2.0. A new example,
industry, Friend type, Device, or Provider MUST first be evaluated
against the existing principles. It MUST NOT automatically create a new
Core Principle. A principle SHOULD be reconsidered only if an actual:
contradiction; security defect; implementation impossibility; material
conformance ambiguity is demonstrated.

# 14. Canonical Summary

P-01 Owner Centrality Owner is the architectural center.

P-02 Owner Data Sovereignty Owner-controlled persistent M-PIN state
remains under Owner authority.

P-03 Friend Sovereignty Friend controls its service and internals.

P-04 One Friend, One Friend Folder Each Friend has its associated
persistent area.

P-05 Friend Folder Isolation One Friend does not receive default access
to another Friend’s Folder.

P-06 Explicit Owner Authority Service need does not create permission.

P-07 Runtime / Persistence Separation Runtime change is not persistent
change.

P-08 Owner-Controlled Persistence M-PIN persistence follows Owner Save.

P-09 Current-State-Only M-PIN Core preserves current committed state,
not automatic M-PIN version history.

P-10 Native Friend Experience M-PIN does not replace Friend UX.

P-11 Zero Requirement Required behavior, not one implementation
technology.

P-12 Bounded Synchronization One M-PIN, One Active Friend, One
Synchronization Session.

P-13 Device Independence Owner continuity is not tied to one Device.

P-14 Provider Independence M-PIN Standard is not one Provider.

P-15 Core Neutrality Core remains independent of industry.

# 15. Core Principle Thesis

The fifteen principles can be reduced to one architectural relationship:
Owner │ │ authority over persistence ▼ M-PIN │ │ bounded, isolated
synchronization ▼ Friend │ │ independent service execution ▼ Runtime /
Native UX The Friend remains free to provide the service. The Owner
remains authoritative over Owner-controlled M-PIN persistence. M-PIN
preserves the boundary between them.

## M-PIN v2.0 — Core 02 / Core Principles

## Status: FROZEN
