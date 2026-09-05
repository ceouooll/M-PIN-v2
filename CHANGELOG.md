# M-PIN Changelog

This file records significant changes between published M-PIN
specification versions.

M-PIN v1.0 remains the historical architecture baseline.

M-PIN v2.0 formalizes that architecture into a more
implementation-oriented specification.

------------------------------------------------------------------------

# \[2.0.0\] — 2026

**Status:** Architecture Frozen

M-PIN v2.0 converts the v1 architecture and Decision Register into a
structured Core specification with behavioral conformance and
cross-domain validation Profiles.

v2.0 does not replace or rewrite v1.0.

------------------------------------------------------------------------

## Added — Formal Core Specification

Introduced twelve Core architecture documents:

``` text
01 — Scope & Design Constitution
02 — Core Principles
03 — Terminology
04 — Core Architecture
05 — Owner & Identity
06 — Friend & Friend Folder Model
07 — Permission Model
08 — Session Protocol
09 — Runtime & Persistence
10 — Security & Threat Model
11 — Portability & Recovery
12 — Conformance Specification
The Core is explicitly industry-neutral.
```

## Added — Core / Profile Separation

Introduced a formal distinction between: M-PIN Core = industry-neutral
architecture

M-PIN Profile = domain-specific application of the unchanged Core This
prevents industry-specific requirements from becoming unnecessary Core
complexity.

## Added — Validation Profiles

Added four v2.0 validation Profiles: AI Robotics Healthcare Commerce The
Profiles validate that materially different service environments can
operate under the same M-PIN Core. No additional Profile is required for
the v2.0 Architecture Freeze.

## Clarified — Owner

Formalized Owner as an architectural authority distinct from: Friend
Friend Account Device Storage M-PIN Service Provider Owner remains the
authority over Owner-controlled M-PIN persistent state.

## Added — Identity Separation

Formalized the distinction between: Owner Identity M-PIN Identity Friend
Identity Friend Account Identity Device Identity Provider Identity M-PIN
Identity is not defined as a particular Friend account, physical device,
or Provider account.

## Clarified — Friend

Preserved the v1 Friend abstraction while formalizing its role. A Friend
remains responsible for its own: service Runtime native UX internal
implementation data semantics business rules evolution M-PIN does not
become the Friend’s operating authority.

## Clarified — Friend Folder

Standardized the v2 Core term: \## Friend Folder A Friend Folder is the
Owner-owned persistent data area associated with a specific Friend. The
canonical relationship is: \## One Friend, One Friend Folder.

## Corrected — Folder / Domain Terminology

During early v2 drafting, Friend-specific storage was temporarily
generalized into a separate Domain abstraction. That interpretation was
rejected. v2.0 restores Friend Folder as the Core entity. Historical v1
uses of Domain remain part of the historical record but do not create a
separate v2 Core entity.

## Clarified — Friend Folder Isolation

Formalized the principle that: common M-PIN ≠ common Friend visibility A
Friend does not receive default access to another Friend’s Folder.

## Clarified — First Synchronization

Formalized the first synchronization behavior: Owner initiates Sync ↓
M-PIN authentication ↓ Friend identity verification ↓ Friend Folder
lookup ↓ Folder absent ↓ Owner approval ↓ Folder creation ↓
Synchronization Session Friend Folder creation remains subject to Owner
approval.

## Clarified — Returning Synchronization

Formalized reuse of an existing Friend Folder during later
synchronization. existing Friend Folder ↓ current saved state ↓ Friend
Runtime

## Clarified — Native Friend Experience

Preserved the v1 rule that M-PIN does not replace the Friend’s workspace
or user experience. The Friend continues to operate through its native
Runtime and UX.

## Added — Formal Session Protocol

Introduced a formal Synchronization Session model. The canonical
invariant is: \## One M-PIN, One Active Friend, One Synchronization
Session. Session lifecycle, authorization, initial read, termination,
and abnormal disconnect behavior are now explicitly modeled.

## Added — Session State Model

Formalized conceptual Session states covering: Idle Authentication
Friend resolution Folder resolution Owner authorization Session open
Initial read Runtime active Save / Commit Termination The exact wire
protocol remains implementation-defined.

## Clarified — Abnormal Disconnect

Preserved and formalized the v1 behavior that abnormal disconnect
terminates M-PIN synchronization authority. Unsaved Runtime State must
not be silently persisted because of disconnection.

## Clarified — Runtime / Persistence Separation

Formalized: \## Runtime Change ≠ Persistent Change Canonical flow:
Persistent State A ↓ LOAD Runtime State A ↓ WORK Runtime State B ↓ OWNER
SAVE Persistent State B Without Save: Runtime State B ↓ Session End ↓
discard relative to M-PIN ↓ Persistent State A remains

## Added — SAVE / COMMIT Distinction

Introduced formal v2 terminology: SAVE = Owner persistence intent

# COMMIT

technical application of the authorized persistence change This is a v2
formalization of the existing Owner-controlled persistence principle.

## Added — Atomic Commit

Added the requirement that a failed persistence operation must not
establish a partially corrupted state as the valid Current State.
Conceptually: A → B

or

A → A rather than: A → partial/corrupted B

## Clarified — Current State Only

Preserved the v1 Last-Save-Only philosophy. M-PIN Core does not require:
version history snapshot history rollback time travel automatic
historical archive This does not prohibit protected backups of the
current state.

## Clarified — Historical Content Inside Current State

v2 distinguishes M-PIN version history from historical service content
contained in a Friend’s current state. For example, a current Friend
payload may legitimately contain: conversation history order history
medical documents receipts if those are part of that Friend’s current
service state. Therefore: No M-PIN version history ≠ Friend payload
cannot contain historical content

## Added — Formal Permission Model

Formalized permission around: Owner authority Friend identity Friend
Folder Session scope persistence authority Friend need or convenience
does not create access authority.

## Clarified — Read and Save Authority

Formalized the separation between: authority to read/load and authority
to persist/save A Friend’s ability to use synchronized state does not
independently grant permanent write authority.

## Added — Formal Security & Threat Model

Introduced explicit analysis of threats including: malicious Friend
compromised Friend malicious or compromised Provider lost device
compromised storage network attacker unauthorized Owner device replay
tampering unauthorized Save

## Added — Security Non-Goal

Explicitly documented that M-PIN cannot guarantee that an authorized
malicious Friend will never copy plaintext legitimately made available
to its Runtime. M-PIN constrains authorization and exposure. It does not
claim control over every internal action of a fully compromised
authorized Friend.

## Clarified — Encryption

Preserved v1 protected-storage requirements while placing them in the
formal Security model. Exact cryptographic algorithms are deferred.

## Added — Fail-Closed Principle

Added a formal requirement to deny access or persistence when required
authority, identity, Session validity, Folder binding, or integrity
cannot be established.

## Added — Provider Model

Introduced a formal distinction between: M-PIN Standard and M-PIN
Service Provider A Provider may implement or host M-PIN infrastructure
without becoming the Owner.

## Added — Provider Independence

Formalized Provider Independence as a v2 architectural principle. M-PIN
Standard is not defined around one mandatory permanent Provider.

## Clarified — Provider Optionality

v2 does not require a permanent centralized Provider for every valid
deployment. Possible deployment environments may include:
provider-hosted Owner-managed local storage Owner-controlled cloud
storage removable storage other conforming environments

## Added — Formal Portability Model

Formalized continuity across changes in: Device Storage Location
Provider Migration should preserve the same M-PIN identity and Owner
continuity rather than silently creating a replacement M-PIN.

## Added — Provider Migration

Defined Provider migration separately from Friend migration. Provider A
→ Provider B does not inherently mean: Friend A → Friend B

## Added — Formal Recovery Model

Introduced the distinction between: Authority Recovery and Data Recovery
Recovery aims to restore legitimate authority to the same M-PIN where
possible. It does not imply that destroyed data can be recreated from
authentication alone.

## Clarified — Backup vs Active Instance

Formalized the distinction between: protected backup copies and
authoritative active continuity Multiple protected copies may exist
without creating multiple legitimate active M-PIN continuities.

## Added — Offline Clone Limitation

Explicitly documented a limitation that v1 did not fully formalize. Two
completely disconnected offline clones cannot be globally guaranteed
never to consider themselves active without some coordination or trusted
mechanism. v2 therefore treats Single Active as a normative continuity
invariant rather than claiming impossible universal offline enforcement.
Strong offline single-active enforcement is deferred.

## Added — Service Record Distinction

Formalized the distinction: Owner-controlled M-PIN State ≠ Friend
Service Record This became especially important during Healthcare and
Commerce validation. Examples of independent Service Records may
include: clinical records transaction records billing records safety
records regulatory records security records

## Added — Service Record Anti-Loophole Boundary

Clarified that independent Service Record obligations do not grant a
Friend permission to copy the Owner’s entire synchronized M-PIN state.

## Profile Changes

## Added — AI Profile

Validated M-PIN against AI services. The AI Profile formalizes
boundaries for: AI memory conversation continuity AI agents model
changes long context multiple AI Friends native AI UX AI remains a
Friend and does not receive privileged M-PIN authority.

## Added — Robotics Profile

Validated M-PIN against physical and embodied systems. Formalized
distinctions including: Robot as Device Robot Service as Friend hardware
manufacturer Robot software AI Friend M-PIN Provider M-PIN preserves
Owner continuity without becoming a robot operating system or physical
safety controller.

## Added — Healthcare Profile

Validated M-PIN against: Hospital Pharmacy Healthcare AI Medical Device
Formalized the distinction between Owner-controlled health state and
institutional healthcare records. M-PIN does not replace an EHR/EMR or
clinical authority.

## Added — Commerce Profile

Validated M-PIN against: Retailer Marketplace Payment Service Delivery
Service physical commerce Formalized the distinction between Owner
Commerce State and Merchant Transaction Records. Also formalized:
Commerce transaction authorization ≠ M-PIN SAVE authorization

## Cross-Profile Findings

## Added — Owner-Mediated Disclosure Candidate

Healthcare and Commerce independently exposed a common interoperability
requirement. Candidate model: Friend A │ selected data ▼ Owner │
explicit authorization ▼ Disclosure │ ▼ Friend B This is classified as:
V2-NEW CROSS-PROFILE FINDING CANDIDATE DEFERRED FROM CORE It does not
create direct cross-Friend Folder access.

## Clarified — Isolation vs Interoperability

v2 formalizes that interoperability does not require shared Folder
authority. Friend Folder Isolation + Owner-authorized selected
disclosure may coexist. The exact Disclosure protocol is deferred.

## v1 Open Decision Disposition

## Decision 095

v2 resolves the architecture-level persistence question as: Owner SAVE ↓
Friend supplies its intended persistent state ↓ M-PIN validates required
authority / structure / integrity ↓ Commit Exact full-state versus delta
encoding is not fixed by the architecture. v2 status: RESOLVED

## Decision 120

v2 resolves the architecture-level responsibility boundary as: Friend
payload semantics = Friend responsibility

minimum M-PIN envelope / identity / integrity requirements = M-PIN
responsibility Exact container and serialization format remain deferred.
v2 status: RESOLVED IN PRINCIPLE

## Conformance

## Added — Behavioral Conformance

Introduced formal conformance based on observable behavior rather than
mandatory implementation technology. Conformance covers: Owner authority
Identity Friend Folder Permission Session Runtime / Persistence Security
Portability Recovery

## Added — Negative Conformance Testing

v2 explicitly tests failure cases such as: cross-Friend Folder access
unauthorized Save Session replay tampered persistent state concurrent
Friend synchronization failed migration unauthorized recovery

## Provenance

## Added — Formal Provenance Classification

Introduced provenance tags: V1-ORIGINAL V1-USER V1-ATOM V1-JOINT
V1-LOCKED POST-V1 GEMINI EXTERNAL V2-NEW This prevents post-v1 concepts
and later external comparisons from being silently attributed to the
original architecture.

## Added — Historical Source Boundary

v2 records that the earliest currently reconstructed source begins on
June 20, 2026 and already refers to prior M-PIN discussion. The broader
approximately May–August 2026 design period is Owner-reported. The
missing earlier conversation is not reconstructed by invention.

## Freeze

## Added — Architecture Freeze Rule

M-PIN v2.0 Core is frozen at twelve Core documents and four validation
Profiles. New industries or implementation ideas do not automatically
reopen the Core. The Core should be reconsidered only when there is
evidence of: actual contradiction security defect implementation
impossibility material conformance ambiguity

## Added — Version Evolution Rule

After v2.0: compatible clarification ↓ v2.1

implementation extension ↓ v2.x / implementation profile

architectural redesign ↓ v3 v2.0 remains preserved as the frozen
historical specification.

## Deferred from v2.0 Architecture

The following remain intentionally unspecified at the architecture
level: exact .MPIN container format serialization format cryptographic
algorithms key hierarchy key rotation key migration recovery algorithm
Friend credential format Session token format heartbeat interval
transport protocol Provider discovery Provider trust mechanism
integrity-proof representation backup freshness mechanism strong offline
single-active enforcement Owner-Mediated Disclosure schema These are
implementation/protocol decisions, not reasons to continue expanding the
frozen architecture.

## \[1.0.0\] — 2026-08-20

Status: Historical Design Freeze M-PIN v1.0 publicly archived the
original architecture and Architecture Decision Register developed
during the initial design period. The v1 repository records the
architecture as a document-based design rather than a production
implementation. Major v1 concepts include: Owner-centered architecture
Friend abstraction Friend-specific persistent areas Friend Folder
synchronization Owner-controlled persistence Current-State-Only Friend
sovereignty native Friend UX preservation selective synchronization
Friend isolation single active synchronization device independence
storage independence Owner data sovereignty Zero Requirement v1 remains
unchanged as the historical baseline for M-PIN v2.

## Version Summary

M-PIN v1.0 2026-08-20 │ │ Historical design baseline │ Architecture
Decision Register │ ▼ M-PIN v2.0 2026 │ │ Formal architecture │ Security
│ Portability │ Recovery │ Conformance │ Four Profiles │ ▼ Architecture
Frozen

## M-PIN — Changelog
