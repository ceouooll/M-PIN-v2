# M-PIN

**Owner-controlled persistent data architecture for service-independent
digital continuity**

M-PIN is an architecture in which the **Owner retains persistent
ownership of their data**, while external services — called **Friends**
— continue to operate through their own runtime, user experience, and
internal implementation.

A Friend may use the Owner-authorized data associated with that Friend
during an active synchronization session.

Persistent changes are committed to M-PIN only according to the
Owner-controlled persistence model.

> **Friend provides the service. Owner owns the data. M-PIN preserves
> the ownership boundary.**

## Reference Implementation

A minimal executable reference for the frozen M-PIN v2 lifecycle is available here:

**[M-PIN Reference Implementation v0.1b Verified](./reference-implementation/)**

- Verified on Windows
- Demo execution: PASS
- Reference Conformance Tests: 9/9 PASS
- Python 3.11+
- No third-party packages required

This Reference Implementation demonstrates the core lifecycle:

`Connect → Load → Runtime → Owner SAVE → Validate → Atomic Commit → Disconnect`

It is not a production M-PIN Hub or a complete security implementation.
------------------------------------------------------------------------

## M-PIN v2.0

M-PIN v2.0 formalizes the architecture first documented in M-PIN v1.0.

v1 primarily preserved the design decisions, principles, and
architecture developed during the original design process.

v2 converts that foundation into a more implementation-oriented
specification covering:

- Owner and identity
- Friend and Friend Folder
- permissions
- synchronization sessions
- runtime and persistence
- security and threat boundaries
- portability and recovery
- behavioral conformance
- cross-domain validation profiles

M-PIN v2 does not replace the historical v1 archive.

The two versions have different roles:

``` text
M-PIN v1
What / Why
Architecture Decisions
Design provenance
Historical baseline

        ↓

M-PIN v2
How
Formal architecture
Protocol behavior
Security boundaries
Conformance
Profiles
```

## Core Idea

Traditional digital services commonly combine two roles: Service +
Persistent User Data M-PIN separates them. OWNER │ Owner Authority │ ▼
M-PIN │ ┌───────────┼───────────┐ │ │ │ Friend Folder A Friend Folder B
Friend Folder C │ │ │ ▼ ▼ ▼ Friend A Friend B Friend C │ │ │ Runtime
Runtime Runtime │ │ │ Native UX Native UX Native UX The Friend remains
responsible for its service. The Owner remains the authority over M-PIN
persistent state.

## Owner

The Owner is the final authority over the Owner-controlled persistent
data stored through M-PIN. The Owner is not equivalent to: a device a
service account a Friend a cloud provider a storage location Changing
those environments does not inherently change the Owner or the M-PIN
identity.

## Friend

A Friend is an external service that interacts with M-PIN to provide a
service to the Owner. A Friend is not limited to AI. Examples may
include: AI service hospital pharmacy retailer robot service
transportation service future digital or physical service M-PIN does not
require every service to become a Friend. A service chooses whether and
how to support M-PIN.

## Friend Folder

Each Friend is associated with its own Owner-owned persistent data area:
\## Friend Folder The basic relationship is: One Friend ↕ One Friend
Folder For example: M-PIN ├── AI Service A Folder ├── Hospital A Folder
├── Retailer A Folder └── Robot Service A Folder A Friend normally
accesses only its own Friend Folder. The existence of multiple Friend
Folders inside one M-PIN does not create a shared data pool.

## First Synchronization

When an Owner synchronizes with a Friend for the first time: Owner opens
Friend ↓ requests synchronization ↓ M-PIN authentication ↓ Friend
identity verification ↓ Friend Folder lookup ↓ Folder not found ↓ Owner
approves creation ↓ Friend Folder created ↓ Synchronization Session If
the Friend Folder already exists, the existing Folder is used.

## Runtime and Persistence

M-PIN separates temporary service execution from persistent state.
Persistent State A ↓ LOAD Runtime State A ↓ WORK Runtime State B ↓ OWNER
SAVE Commit ↓ Persistent State B Without Owner Save: Persistent State A
↓ Runtime State B ↓ NO SAVE ↓ Session ends ↓ Persistent State A remains
Therefore: \## Runtime change is not automatically persistent change.

## Current State

The M-PIN Core represents the Owner’s current committed persistent
state. It is not defined as a historical archive system. Core semantics
do not require: Version History Snapshot History Rollback Time Travel
Automatic historical archive Backup copies may exist, but backup and
historical versioning are different concepts.

## Friend Independence

M-PIN does not replace the Friend’s workspace or user experience. A
Friend continues to control its own: user interface runtime internal
implementation service policies data semantics product evolution M-PIN
does not require a specific: SDK API runtime UI programming language
database cloud operating system Compatibility is based primarily on
observable behavior rather than implementation technology.

## One Active Friend

The v2 Core uses the following synchronization invariant: \## One M-PIN,
One Active Friend, One Synchronization Session. When a synchronization
session ends, the Friend’s M-PIN access authority ends with it. Abnormal
disconnection must not silently commit unsaved runtime state.

## Security

M-PIN v2 defines security around the ownership and access boundary. Core
security principles include: encrypted protected persistent state Owner
authentication Friend identity verification Friend Folder isolation
explicit authorization session revocation integrity verification
fail-closed behavior protection against unauthorized Save separation of
Provider authority from Owner authority M-PIN does not claim that an
authorized but malicious Friend can never copy plaintext that it
legitimately receives during runtime. The purpose of the architecture is
to minimize and enforce the authorized boundary, not to claim impossible
control over a fully compromised authorized runtime.

## Device Independence

M-PIN is not bound to one device. Conceptually: Device A ↓ same M-PIN

Device B ↓ same M-PIN A device change does not inherently create a new
Owner or a new M-PIN identity.

## Provider Independence

M-PIN v2 distinguishes the M-PIN Standard from an M-PIN Service
Provider. M-PIN Standard ≠ one provider A provider may offer creation,
hosting, authentication, recovery, storage, or migration services.
However, the standard itself is not defined around one permanent
provider. A compatible M-PIN may conceptually be implemented through:
Owner-managed local storage Provider A Provider B removable storage
other compatible environments

## Portability

Portability aims to preserve the same M-PIN continuity when the
environment changes. Device changes Storage changes Location changes
Provider changes

        ↓

same Owner same M-PIN identity same persistent continuity Provider
migration is not defined as creating a new M-PIN.

## Recovery

Recovery restores legitimate authority to the same M-PIN where possible.
Recovery ≠ silently creating a replacement identity M-PIN distinguishes:
Authority Recovery vs Data Recovery If all copies of the actual data are
destroyed, authentication recovery alone cannot recreate that data.

## Single Active Continuity

Protected copies or backups may exist. But M-PIN treats one continuity
as the authoritative active state. multiple protected copies MAY exist

one authoritative continuity MUST be maintained A fully offline clone
problem cannot be globally solved without some coordination or trusted
mechanism. M-PIN v2 therefore does not claim an impossible global
cryptographic guarantee for completely disconnected independent clones.

## Service Records

M-PIN distinguishes Owner-controlled persistent state from records that
a Friend independently maintains for legitimate service or institutional
purposes. Examples may include: hospital clinical records merchant
transaction records robot safety records AI billing or security records
Therefore: Owner M-PIN State ≠ Friend Service Record This distinction
does not give a Friend unrestricted authority to copy the Owner’s entire
M-PIN.

## Profiles

M-PIN v2 validates the same Core against four different domains. \## AI
Profile Validates: AI memory continuity Friend-specific AI context
native AI UX preservation agent permission boundaries model evolution
runtime vs Owner-controlled persistence \## Robotics Profile Validates:
continuity across physical robots hardware / Friend separation
shared-device isolation sensor runtime boundaries robot safety
independence multi-vendor deployment \## Healthcare Profile Validates:
Hospital and Pharmacy as independent Friends Owner-held health state
institutional medical records cross-hospital disclosure boundaries
healthcare AI emergency access boundaries \## Commerce Profile
Validates: Retailer, Payment, and Delivery Friends transaction records
vs Owner state personalization minimum disclosure cross-service commerce
interactions payment authorization vs persistence authorization The
purpose of the Profiles is not to create four different M-PIN
architectures. All four use the same Core.

## Owner-Mediated Disclosure

Healthcare and Commerce both reveal the same interoperability need:
sometimes the Owner may want information originating in one Friend
relationship to be provided to another Friend. M-PIN does not solve this
by giving Friend B direct access to Friend A’s Folder. Instead, v2
records a candidate model: Friend A │ selected data ▼ Owner │ explicit
authorization ▼ Disclosure │ ▼ Friend B This is referred to as: \##
Owner-Mediated Disclosure It is a cross-profile v2 finding. The exact
interoperability schema is deferred beyond the frozen v2.0 Core.

## Conformance

M-PIN compatibility is defined by observable behavior rather than one
mandatory implementation. Conformance areas include: Owner authority
Identity Friend Folder isolation Permission Session behavior Runtime /
Persistence separation Security Portability Recovery Example negative
tests include: Friend attempts another Friend Folder Owner Save is
forged terminated session is replayed persistent state is tampered with
two Friends attempt concurrent synchronization Provider migration
creates conflicting active states unauthorized recovery is attempted A
compatible implementation must fail safely when required boundaries
cannot be verified.

## Repository Structure

M-PIN-v2/

README.md

core/ 01-scope-and-design-constitution.md 02-core-principles.md
03-terminology.md 04-core-architecture.md 05-owner-and-identity.md
06-friend-and-friend-folder.md 07-permission-model.md
08-session-protocol.md 09-runtime-and-persistence.md
10-security-and-threat-model.md 11-portability-and-recovery.md
12-conformance-specification.md

profiles/ 01-ai.md 02-robotics.md 03-healthcare.md 04-commerce.md

PROVENANCE.md CHANGELOG.md FREEZE.md LICENSE

## Architecture Status

M-PIN v2.0 Core consists of twelve architecture documents. 01 Scope &
Design Constitution LOCK 02 Core Principles LOCK 03 Terminology LOCK 04
Core Architecture LOCK 05 Owner & Identity LOCK 06 Friend & Friend
Folder LOCK 07 Permission Model LOCK 08 Session Protocol LOCK 09 Runtime
& Persistence LOCK 10 Security & Threat Model LOCK 11 Portability &
Recovery LOCK 12 Conformance Specification LOCK Profiles: AI LOCK
Robotics LOCK Healthcare LOCK Commerce LOCK Deferred implementation
details include: exact .MPIN container format serialization
cryptographic algorithms key hierarchy recovery algorithm transport
protocol session token representation provider discovery strong offline
single-active mechanism Disclosure schema These are intentionally not
required to reopen the v2.0 architecture.

## v2.0 Architecture Freeze

M-PIN v2.0 Core is considered closed. New industries, product ideas, or
implementation techniques do not automatically reopen the Core. Future
changes are classified as: compatible clarification ↓ v2.1

architectural redesign ↓ v3 The v2 Core should be reopened only when an
actual contradiction, security defect, or implementation impossibility
is demonstrated.

## Provenance

M-PIN v1.0 was developed and documented before the v2 work. M-PIN v1.0
Owner-reported broader design period: approximately May–August 2026.

Earliest surviving reconstructed record: June 20, 2026. M-PIN v1.0
public archive: August 20, 2026. M-PIN v2.0 was developed after the v1
design freeze to formalize the architecture into a more
implementation-oriented specification. External systems published or
reviewed after the v1 freeze may be discussed as comparative references,
but they are not part of the v1 design provenance. The original v1
archive should remain unchanged as the historical baseline.

## Project Status

M-PIN v1 Historical design archive

M-PIN v2 Architecture specification Core frozen Profiles frozen

Production implementation Not part of the v2 architecture freeze

## Core Thesis

## M-PIN separates service execution from persistent data ownership.

## Continuity Thesis

## Service may change. Device may change. Provider may change. Owner continuity remains.

## Friend Thesis

M-PIN does not control the Friend. It controls the boundary through
which the Friend accesses Owner-owned persistent state. \## Folder
Thesis \## One Friend, One Friend Folder. \## Persistence Thesis \##
Runtime belongs to the service process. Persistence belongs to the
Owner’s decision.

## M-PIN v2.0 — Architecture Frozen
