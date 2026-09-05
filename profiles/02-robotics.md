# M-PIN v2.0

## Profile 02 — Robotics

**Status:** FROZEN **Version:** 2.0 **Document Type:** Normative Profile
Specification **Requires:** M-PIN v2.0 Core 01–12

------------------------------------------------------------------------

# 1. Purpose

This Profile applies the M-PIN v2.0 Core architecture to robotics.

It defines how M-PIN may preserve Owner-controlled persistent continuity
across:

- robots;
- robotic services;
- AI systems embedded in robots;
- robot-control services;
- public or shared robots;
- temporary robot use;
- robot replacement;
- robot manufacturer changes;
- Device changes;
- M-PIN Provider changes.

This Profile does not redefine M-PIN as a robot-control system.

M-PIN remains the Owner-controlled persistence and access boundary.

------------------------------------------------------------------------

# 2. Robotics Thesis

The canonical Robotics principle is:

> **The Owner carries persistent continuity through M-PIN. The robot
> does not inherently own that continuity.**

Conceptually:

Owner │ ▼ M-PIN │ ▼ compatible robot environment │ ├── Friend A ├──
Friend B └── Friend C

The physical robot may change while legitimate Owner continuity remains.

------------------------------------------------------------------------

# 3. Robot Is Not a Single Mandatory Role

A robot MUST NOT automatically be modeled as one indivisible Friend.

Depending on the implementation, a robot may be:

- a Device;
- a host environment;
- a Friend;
- a host for multiple Friends;
- a combination of these roles.

The architectural role depends on the service boundary being modeled.

------------------------------------------------------------------------

# 4. Robot as Device

A physical robot may act as a Device on which multiple services execute.

Example:

Robot Device ├── AI Friend ├── Robot Control Friend ├── Navigation
Friend └── Commerce Friend

Each Friend remains independently subject to M-PIN Core rules.

Physical co-location does not collapse Friend boundaries.

------------------------------------------------------------------------

# 5. Robot as Friend

A robotic service may itself be modeled as a Friend when it represents
one continuing service relationship.

Example:

M-PIN │ ▼ Robot Service Friend Folder │ ▼ Robot Service Friend │ ▼ Robot
Runtime

This does not mean every physical component of the robot becomes part of
the same Friend.

------------------------------------------------------------------------

# 6. Multiple Friends Inside One Robot

One robot may host multiple Friends.

For example:

Robot Device │ ├── Personal AI Friend │ └── AI Friend Folder │ ├── Robot
Control Friend │ └── Robot Control Folder │ ├── Health Friend │ └──
Health Friend Folder │ └── Commerce Friend └── Commerce Friend Folder

The Friends MUST remain isolated according to Core.

------------------------------------------------------------------------

# 7. Hardware Is Not Automatically a Friend

Physical components such as:

- motors;
- cameras;
- microphones;
- wheels;
- arms;
- sensors;
- batteries

do not automatically become M-PIN Friends.

They may be resources used by a Friend Runtime.

M-PIN does not require every hardware component to have a Friend Folder.

------------------------------------------------------------------------

# 8. Operating System Is Not Automatically a Friend

A robot operating system may provide infrastructure without being
modeled as a Friend.

If an operating-system-level service establishes its own persistent
Owner relationship through M-PIN, it MAY be modeled as a Friend.

The implementation must preserve the role distinction.

------------------------------------------------------------------------

# 9. Robot Manufacturer Is Not Owner

A manufacturer does not become the Owner of M-PIN merely because it:

- manufactured the robot;
- controls firmware;
- operates the robot cloud;
- provides maintenance;
- supplies the M-PIN implementation.

The architectural Owner remains distinct.

------------------------------------------------------------------------

# 10. Robot Manufacturer and M-PIN Provider

The same company MAY act as both:

- robot manufacturer;
- M-PIN Service Provider.

These roles remain conceptually separate.

Example:

Company H ├── manufactures Robot R └── operates M-PIN Provider P

does not mean:

Provider P = Owner

or:

Robot R = M-PIN

------------------------------------------------------------------------

# 11. Provider Independence in Robotics

A robot manufacturer MAY provide an M-PIN-compatible service.

Another Provider MAY provide another compatible implementation.

M-PIN MUST NOT be architecturally tied to the original robot
manufacturer.

This preserves Provider Independence.

------------------------------------------------------------------------

# 12. Owner Continuity Across Robots

The Owner may move from one compatible robot environment to another
while preserving M-PIN continuity.

Conceptually:

Owner │ ▼ M-PIN X │ ▼ Robot A

later:

Owner │ ▼ same M-PIN X │ ▼ Robot B

The robot changes.

The Owner’s persistent continuity does not inherently change.

------------------------------------------------------------------------

# 13. Digital Continuity

For Robotics, **Digital Continuity** means that the Owner’s persistent
service relationships are not inherently trapped inside one physical
robot.

Conceptually:

Robot A │ ▼ Owner uses services │ ▼ M-PIN persistent continuity

then:

Robot B │ ▼ Owner establishes M-PIN authority │ ▼ compatible Friends
restore their own authorized state

The continuity belongs to the Owner’s M-PIN relationship, not to the
discarded Device.

------------------------------------------------------------------------

# 14. Digital Continuity Is Not Robot Cloning

Moving Owner continuity to Robot B does not require Robot B to become a
physical or software clone of Robot A.

Robot B may have:

- different hardware;
- different sensors;
- different actuators;
- different manufacturer;
- different operating system;
- different local implementation.

The applicable Friends determine how Owner state is used in the new
environment.

------------------------------------------------------------------------

# 15. M-PIN Does Not Carry Proprietary Robot Cognition

M-PIN does not require a robot manufacturer to export:

- proprietary control algorithms;
- model weights;
- motion-planning algorithms;
- firmware;
- trade-secret software;
- proprietary robot cognition.

M-PIN carries the Owner-controlled persistent state associated with
compatible Friend relationships.

Friend implementation remains Friend-controlled.

------------------------------------------------------------------------

# 16. Owner State vs Robot Capability

Owner persistent state and physical robot capability are distinct.

For example:

Owner preference: preferred walking speed

Robot A: supports requested range

Robot B: supports narrower range

The Friend on Robot B must interpret the Owner state according to Robot
B’s actual capabilities.

M-PIN does not fabricate unavailable hardware capability.

------------------------------------------------------------------------

# 17. Capability Translation

Where different robots have different capabilities, the relevant Friend
MAY translate or adapt Owner state to the available hardware.

Such semantic adaptation is the Friend’s responsibility.

M-PIN does not universally interpret robot capability semantics.

------------------------------------------------------------------------

# 18. Friend Identity Across Robots

The same Friend may operate across different compatible robots.

Example:

Robot A └── Friend F

Robot B └── same Friend F

If Friend Identity remains legitimately continuous:

Friend F ↔ Folder F

may remain the same relationship.

Changing physical Device alone does not require a new Friend Folder.

------------------------------------------------------------------------

# 19. Different Robot Service Friend

If Robot A uses Friend F and Robot B uses a different Friend G:

Friend F ↔ Folder F

does not become:

Friend G ↔ Folder F

automatically.

Friend G normally receives its own Friend Folder.

------------------------------------------------------------------------

# 20. Manufacturer Change

Changing robot manufacturer does not automatically grant the new
manufacturer’s Friends access to the previous manufacturer’s Friend
Folders.

Example:

Manufacturer A Robot └── Friend A ↔ Folder A

Manufacturer B Robot └── Friend B

Friend B MUST NOT automatically receive Folder A.

Device portability does not override Friend isolation.

------------------------------------------------------------------------

# 21. Same Friend Across Manufacturers

A service-independent Friend may operate on robots from multiple
manufacturers.

Example:

Robot Manufacturer A ─┐ ├── Friend F Robot Manufacturer B ─┘

If Friend F is legitimately the same Friend:

M-PIN └── Folder F

may support continuity across both robot environments.

This is a Friend identity question, not a manufacturer identity
question.

------------------------------------------------------------------------

# 22. First Robot Synchronization

When an Owner uses an M-PIN Friend relationship on a robot for the first
time:

Owner ↓ initiates M-PIN synchronization ↓ M-PIN location/environment
selected ↓ Owner authority established ↓ Friend Identity verified ↓
Friend Folder resolved ↓ if absent → Owner creation approval ↓ Session
established ↓ Current State loaded ↓ Friend Runtime on robot

The physical presence of the Owner near the robot does not replace
authentication.

------------------------------------------------------------------------

# 23. Returning Robot Synchronization

For an existing Friend relationship:

Owner ↓ connects M-PIN ↓ Friend verified ↓ existing Friend Folder
resolved ↓ new Session ↓ Current State loaded ↓ Friend Runtime on robot

The existing Folder is reused.

------------------------------------------------------------------------

# 24. Physical Presence Is Not Authority

Standing near a robot, touching it, entering a room, or being detected
by a sensor MUST NOT automatically grant M-PIN Owner Authority.

Physical presence may be one signal in an authentication mechanism.

It is not sufficient architectural proof by itself.

------------------------------------------------------------------------

# 25. Biometric Input

A robot MAY use biometric input as part of an Owner authentication
system.

M-PIN Core does not mandate:

- face recognition;
- fingerprint recognition;
- voice recognition;
- iris recognition;
- another biometric.

The exact authentication mechanism remains implementation-defined.

------------------------------------------------------------------------

# 26. Connection Technology

M-PIN Robotics does not require one connection technology.

A robot may interact with M-PIN through:

- local network;
- direct wired connection;
- removable storage;
- cloud-mediated connection;
- short-range wireless;
- another compatible mechanism.

The connection technology does not define ownership.

------------------------------------------------------------------------

# 27. Local and Offline Robotics

A Robotics implementation MAY operate locally without a mandatory cloud
Provider.

For example:

Owner ↓ local M-PIN ↓ Robot Device ↓ Friend

is valid if Core requirements are satisfied.

------------------------------------------------------------------------

# 28. Removable M-PIN Scenario

An Owner MAY carry M-PIN state on compatible removable storage.

Conceptually:

Owner ↓ removable M-PIN storage ↓ Robot A

later:

Owner ↓ same M-PIN ↓ Robot B

The exact physical medium is not normative.

------------------------------------------------------------------------

# 29. Storage Removal

If the active M-PIN access path depends on removable Storage and that
Storage is removed such that safe Session continuation is no longer
possible:

the affected M-PIN Session MUST terminate or fail closed.

Removal MUST NOT trigger automatic Save of unsaved Runtime state.

------------------------------------------------------------------------

# 30. Public Robot

A public or shared robot presents a stronger residual-data risk.

Examples include:

- hotel robot;
- airport robot;
- hospital service robot;
- retail robot;
- rental robot;
- public mobility robot.

The Owner may establish a temporary M-PIN Session with compatible
Friends on such a Device.

------------------------------------------------------------------------

# 31. Public Robot Isolation

After the Owner’s M-PIN Session terminates, the public robot MUST NOT
retain continuing M-PIN authority.

The next user MUST NOT inherit:

- the previous Owner’s Friend Folder authority;
- active Session tokens;
- unauthorized persistent M-PIN cache;
- another Owner’s M-PIN identity.

------------------------------------------------------------------------

# 32. Runtime Cache on Public Robots

A Friend may require temporary local Runtime cache.

Such cache:

- MUST NOT become authoritative M-PIN state;
- SHOULD be minimized;
- SHOULD be cleared or made unusable after Session termination where
  applicable;
- MUST NOT provide the next user with previous Owner authority.

Exact secure-erasure mechanisms are implementation-specific.

------------------------------------------------------------------------

# 33. Robot Runtime

A robot Friend may load M-PIN state into its Runtime.

Example:

Friend Folder Current State A ↓ Load ↓ Robot Friend Runtime ↓
physical/service interaction ↓ Runtime State B

Runtime State B does not become M-PIN Persistent State without the
required Save process.

------------------------------------------------------------------------

# 34. Physical Action Is Not Save

A physical robot action MUST NOT automatically be interpreted as M-PIN
Save.

Examples:

robot opens door robot moves object robot walks robot delivers item
robot adjusts seat robot speaks

do not inherently mean:

Owner SAVE

Physical action and persistence intent are distinct.

------------------------------------------------------------------------

# 35. Sensor Observation Is Not Save

A robot observing something through a sensor does not automatically make
that observation persistent M-PIN state.

Examples:

camera detects person microphone hears speech sensor measures
temperature robot maps a room

do not automatically mean:

M-PIN Commit

Persistence follows the applicable Friend and Owner Save model.

------------------------------------------------------------------------

# 36. Continuous Sensor Data

M-PIN does not require every continuous sensor stream to be persisted
into the Owner’s Friend Folder.

A Friend may process sensor data temporarily in Runtime.

If persistent Owner state is desired, it follows the applicable
persistence rules.

Independent legitimate Service Records remain separately governed.

------------------------------------------------------------------------

# 37. Robot Internal Logging

A robot manufacturer or Friend may maintain legitimate operational logs
or Service Records.

Examples may include:

- fault logs;
- safety events;
- maintenance records;
- regulatory records;
- security events.

Such records are not automatically M-PIN Friend Folder state.

------------------------------------------------------------------------

# 38. Service Record Anti-Loophole

Robot operational logging MUST NOT be used as a blanket mechanism to
permanently duplicate the Owner’s complete synchronized Friend Folder
outside M-PIN.

A Service Record requires an independently legitimate purpose.

------------------------------------------------------------------------

# 39. Owner Save in Robotics

The canonical persistence flow is:

Friend Folder Current State₀ ↓ Load ↓ Robot Friend Runtime ↓ interaction
↓ Runtime State′ ↓ Owner SAVE ↓ Validation ↓ Atomic Commit ↓ Current
State₁

------------------------------------------------------------------------

# 40. No Save in Robotics

Without Owner Save:

Current State₀ ↓ Load ↓ Robot Runtime State′ ↓ Session ends ↓ No M-PIN
Commit ↓ Current State₀ remains

The fact that physical actions occurred does not change this persistence
rule.

------------------------------------------------------------------------

# 41. Save Suggestion

A robot or Friend MAY suggest that the Owner Save updated persistent
state.

For example:

“Would you like to save this preference?”

A suggestion is not authorization.

The Friend MUST NOT treat its own recommendation as Owner Save.

------------------------------------------------------------------------

# 42. Long-Running Robot Tasks

A robot may perform a task longer than a simple interaction.

The M-PIN Session model may support a bounded long-running Session or
renewed authority.

The existence of a long task MUST NOT create indefinite hidden M-PIN
access.

------------------------------------------------------------------------

# 43. Session Renewal

Where Session renewal is used:

- Owner authority must remain applicable;
- Friend Identity must remain valid;
- permission scope must remain valid;
- stale Session authority must not be silently extended forever.

Exact renewal protocol is deferred.

------------------------------------------------------------------------

# 44. Session End vs Physical Process

Termination of an M-PIN Session does not necessarily mean every physical
robot process must stop immediately.

For example:

M-PIN Session ends ≠ emergency braking disabled

or:

M-PIN Session ends ≠ robot must drop carried object

M-PIN is not the robot’s safety-control bus.

------------------------------------------------------------------------

# 45. M-PIN Is Not a Robot Control Bus

M-PIN MUST NOT be treated as the mandatory real-time control path for:

- motor loops;
- emergency stop;
- collision avoidance;
- balance control;
- actuator timing;
- hard real-time safety control.

Those belong to the robot’s own control and safety architecture.

------------------------------------------------------------------------

# 46. Safety Independence

Robot safety MUST remain independently enforceable from M-PIN
persistence.

M-PIN conformance does not certify that a robot is physically safe.

A robot MUST NOT disable required safety controls merely because an
M-PIN Owner requests it.

------------------------------------------------------------------------

# 47. M-PIN Authority vs Robot Action Authority

M-PIN Owner Authority governs M-PIN access and persistence.

It does not automatically establish authorization for every physical
robot action.

Examples may require separate authority:

- entering restricted area;
- operating dangerous machinery;
- medical intervention;
- vehicle control;
- financial transaction.

The relevant Friend or external system remains responsible for those
authorizations.

------------------------------------------------------------------------

# 48. Emergency Behavior

M-PIN v2 does not define a universal emergency override for robotics.

A robot’s emergency behavior belongs to its safety architecture and
applicable law/regulation.

Emergency operation MUST NOT be confused with unrestricted access to
every Owner Friend Folder.

------------------------------------------------------------------------

# 49. Robot Failure

If a physical robot fails:

Robot A unavailable ↓ M-PIN continuity may remain ↓ Owner moves to
compatible Robot B ↓ same compatible Friend restores its authorized
Current State

This is a primary Robotics portability scenario.

------------------------------------------------------------------------

# 50. Robot Replacement

Replacing a robot Device does not inherently create a new M-PIN.

Where the same Friend remains available:

Robot A → Robot B + same M-PIN + same Friend Identity

may preserve:

same Friend Folder relationship

------------------------------------------------------------------------

# 51. Robot Resale

When a robot is sold or transferred to another person:

the old Owner’s M-PIN authority MUST NOT transfer merely with possession
of the robot.

Robot possession ≠ M-PIN ownership

Residual M-PIN credentials or Runtime data SHOULD be removed or rendered
unusable as applicable.

------------------------------------------------------------------------

# 52. Repair and Maintenance

A repair technician or manufacturer maintenance account MUST NOT
automatically gain Owner M-PIN authority.

Maintenance authority and Owner M-PIN authority remain distinct.

If diagnostic access to Owner state is necessary, it requires an
explicit applicable authorization mechanism.

------------------------------------------------------------------------

# 53. Rental Robots

A rental robot may serve multiple Owners over time.

Each Owner’s M-PIN relationship must remain isolated.

Example:

Owner A Session ↓ terminate ↓ clear/invalidate applicable local state ↓
Owner B Session

Owner B MUST NOT inherit Owner A’s M-PIN authority.

------------------------------------------------------------------------

# 54. Hotel Robot Scenario

A hotel may provide compatible robots to guests.

Guest A may:

1.  authenticate to M-PIN;
2.  connect a compatible Friend;
3.  load the Friend’s Current State;
4.  use the robot;
5.  optionally Save;
6.  terminate the Session.

After termination:

the hotel robot does not become the Owner of Guest A’s persistent state.

Another guest does not receive Guest A’s Friend Folder.

------------------------------------------------------------------------

# 55. Cross-Robot Continuity Scenario

An Owner may use:

Home Robot ↓ same M-PIN ↓ Friend F

then later:

Hotel Robot ↓ same M-PIN ↓ same compatible Friend F

The Friend may restore the Owner’s saved persistent relationship.

The hotel robot does not need to contain the Owner’s permanent identity
state before synchronization.

------------------------------------------------------------------------

# 56. Robot AI Composition

A robot may contain an AI Friend and Robot Control Friend.

Example:

M-PIN ├── AI Folder │ ↓ │ AI Friend │ └── Control Folder ↓ Robot Control
Friend

AI Friend and Robot Control Friend do not automatically share Folder
access.

------------------------------------------------------------------------

# 57. AI Advice vs Control Authority

An AI Friend may recommend a physical action.

Example:

AI Friend: “Move to the kitchen.”

That recommendation does not itself grant Robot Control Friend authority
to access the AI Friend Folder or vice versa.

The robot’s internal application architecture may pass permitted Runtime
instructions without collapsing M-PIN Folder ownership boundaries.

------------------------------------------------------------------------

# 58. Healthcare Robot Composition

A healthcare robot may include:

- Robot Control Friend;
- Healthcare Friend;
- AI Friend.

Each may have a separate Friend Folder.

Healthcare institutional Service Records remain governed by the
Healthcare Profile and external obligations.

------------------------------------------------------------------------

# 59. Commerce Robot Composition

A retail robot may include:

- Robot Interaction Friend;
- Retailer Friend;
- Payment Friend;
- Delivery Friend.

The robot Device does not become a universal access bridge among their
Friend Folders.

Commerce Profile boundaries remain applicable.

------------------------------------------------------------------------

# 60. Profile Composition

Robotics Profile MAY compose with:

- AI Profile;
- Healthcare Profile;
- Commerce Profile.

Profile composition adds requirements.

It does not weaken Core.

------------------------------------------------------------------------

# 61. Hardware Capability Differences

When the Owner moves between robots, the same Friend may encounter
different capabilities.

Example:

Robot A: two arms

Robot B: one arm

M-PIN preserves the Owner state.

The Friend decides how that state maps to available capability.

M-PIN does not require identical hardware.

------------------------------------------------------------------------

# 62. Hardware Capability Metadata

A robot or Friend MAY expose capability metadata required for compatible
operation.

Such metadata is not automatically Owner-owned Friend Folder content.

It may be Device or Friend Runtime information.

The exact capability-description format is outside v2.0.

------------------------------------------------------------------------

# 63. Device Identity

A robot MAY have a Device Identity.

Device Identity is distinct from:

- Owner Identity;
- M-PIN Identity;
- Friend Identity.

A verified robot Device does not automatically become an authorized
Friend.

------------------------------------------------------------------------

# 64. Device Attestation

A Robotics implementation MAY use hardware or software attestation to
assess robot integrity.

Attestation is not mandatory in M-PIN v2.0 Core.

Where used, it supplements rather than replaces Owner and Friend
authorization.

------------------------------------------------------------------------

# 65. Friend Identity on Robots

A Friend operating on a robot MUST be distinguishable from unrelated
Friends.

M-PIN MUST NOT bind a Folder based solely on a mutable display label
such as:

“Assistant” “Robot” “AI”

The exact credential mechanism is deferred.

------------------------------------------------------------------------

# 66. Malicious Robot Device

A compromised robot Device may attempt to observe plaintext processed by
a legitimate Friend Runtime.

M-PIN cannot guarantee confidentiality against a Device that fully
compromises the authorized Runtime environment.

This limitation MUST NOT be hidden.

------------------------------------------------------------------------

# 67. Compromised Friend

A compromised robot Friend may misuse plaintext from its own authorized
Friend Folder.

M-PIN can still prevent that authority from automatically extending to
unrelated Friend Folders.

The Core does not claim perfect containment after legitimate plaintext
disclosure to a malicious Friend.

------------------------------------------------------------------------

# 68. Malicious Manufacturer

A manufacturer controlling the Device or Provider MUST NOT automatically
be treated as Owner.

However, if the manufacturer controls the entire Runtime environment,
technical confidentiality may depend on the actual hardware, key, and
trust architecture.

M-PIN v2 does not make an unsupported zero-knowledge claim.

------------------------------------------------------------------------

# 69. Public Device Threats

Robotics implementations SHOULD account for:

- residual plaintext;
- cached credentials;
- Session token reuse;
- shoulder-surfing or local observation;
- malicious peripherals;
- modified firmware;
- false Friend Identity;
- stolen removable Storage;
- unauthorized next-user access.

------------------------------------------------------------------------

# 70. Fail Closed

If the robot environment cannot safely establish required:

- Owner Authority;
- Friend Identity;
- Folder binding;
- Session validity;
- integrity;

the affected M-PIN operation MUST fail closed.

The robot may continue independent functions that do not require M-PIN
authority.

------------------------------------------------------------------------

# 71. M-PIN Provider Migration

An Owner may migrate M-PIN from Provider A to Provider B without
replacing the robot or Friend.

Example:

Robot R │ Friend F │ M-PIN X │ Provider A

becomes:

Robot R │ same Friend F │ same M-PIN X │ Provider B

Provider migration is not robot migration.

------------------------------------------------------------------------

# 72. Robot Migration

Moving from Robot A to Robot B is Device migration when the same Friend
relationship continues.

It does not inherently require Provider migration.

These axes are independent.

------------------------------------------------------------------------

# 73. Independent Migration Axes

Robotics therefore has at least three independent change axes:

Device: Robot A → Robot B

Friend: Friend A → Friend B

Provider: Provider A → Provider B

M-PIN MUST NOT collapse these into one identity transition.

------------------------------------------------------------------------

# 74. Recovery After Robot Loss

If a robot containing local M-PIN material is lost:

1.  possession of the robot does not make the finder the Owner;
2.  Owner may require Authority Recovery;
3.  Owner may require Data Recovery;
4.  valid Backup may be used;
5.  a new robot may establish a new Session.

Authority Recovery and Data Recovery remain distinct.

------------------------------------------------------------------------

# 75. Robot Loss and Encryption

Persistent M-PIN state stored on a robot or removable medium MUST
receive the Core encryption-at-rest protection.

Device loss MUST NOT intentionally expose ordinary plaintext Friend
Folder state.

Exact cryptographic mechanisms remain deferred.

------------------------------------------------------------------------

# 76. Robot Loss and Revocation

Where the architecture supports revocation, the Owner SHOULD be able to
invalidate applicable future M-PIN authority associated with the lost
environment.

Offline limitations remain applicable.

A completely disconnected compromised copy cannot receive a revocation
it cannot observe.

------------------------------------------------------------------------

# 77. Offline Clone Limitation

Robotics makes the disconnected-clone limitation especially visible.

For example:

Robot A has offline copy X Robot B has offline copy X

with no coordination.

M-PIN v2 cannot truthfully guarantee global single-active enforcement
between them without a coordination mechanism.

The architecture still defines one authoritative active continuity.

Stronger global enforcement is deferred.

------------------------------------------------------------------------

# 78. Offline Operation

Offline operation MAY be supported.

An offline implementation MUST still preserve locally enforceable:

- Friend Folder isolation;
- Owner Authority;
- Session boundary;
- Save semantics;
- integrity.

It MUST NOT claim guarantees that require unavailable global
coordination.

------------------------------------------------------------------------

# 79. Long-Term Robot Ownership

A robot may remain with one Owner for years.

That does not change the architectural principle:

Robot lifetime ≠ Owner digital continuity lifetime

The Owner’s M-PIN continuity may outlive any individual robot.

------------------------------------------------------------------------

# 80. Robot Upgrade

Replacing:

- processor;
- sensors;
- actuators;
- operating system;
- firmware;
- physical chassis

does not inherently create a new M-PIN.

Whether a Friend identity changes depends on the service relationship,
not merely the hardware revision.

------------------------------------------------------------------------

# 81. Robotics Mandatory Requirements

A Robotics implementation claiming M-PIN v2.0 Robotics Profile
conformance MUST satisfy:

### ROB-001 — Core Conformance

The implementation MUST satisfy all applicable M-PIN v2.0 Core
requirements.

### ROB-002 — Role Separation

The implementation MUST distinguish the physical Robot Device from
Friend, Owner, and M-PIN roles where those roles are separately present.

### ROB-003 — Device Is Not Owner

Physical possession or manufacture of a robot MUST NOT automatically
create M-PIN Owner Authority.

### ROB-004 — Friend Folder Isolation

Distinct Friends operating on the same robot MUST NOT automatically
share Friend Folder authority.

### ROB-005 — Device Portability

Changing compatible Robot Device MUST NOT inherently require creation of
a new M-PIN.

### ROB-006 — Friend Identity Continuity

The same legitimate Friend MAY preserve its Friend Folder across
compatible robot Devices.

### ROB-007 — No Automatic Friend Inheritance

A different robot Friend MUST NOT automatically inherit another Friend’s
Folder.

### ROB-008 — Owner-Controlled Persistence

Robot Runtime changes MUST become M-PIN Persistent State only through
the applicable Owner Save process.

### ROB-009 — Physical Action Separation

Physical robot actions MUST NOT automatically constitute M-PIN Save.

### ROB-010 — Sensor Persistence Separation

Sensor observation MUST NOT automatically constitute M-PIN persistence.

### ROB-011 — Session Termination

Loss or termination of M-PIN Session authority MUST stop continued M-PIN
access under that authority.

### ROB-012 — Public Device Isolation

Shared or public robots MUST NOT expose one Owner’s M-PIN authority to
the next user.

### ROB-013 — Safety Independence

M-PIN MUST NOT be the mandatory hard-real-time safety-control mechanism
for the robot.

### ROB-014 — Provider Independence

Robot manufacturer or M-PIN Provider identity MUST NOT automatically
become M-PIN ownership.

### ROB-015 — Service Record Boundary

Robot Service Records MUST remain distinguishable from M-PIN Friend
Folder persistence and MUST NOT be used as a blanket persistence
loophole.

------------------------------------------------------------------------

# 82. Recommended Robotics Properties

A Robotics implementation SHOULD additionally satisfy:

### ROB-016 — Residual Data Minimization

Public/shared robots SHOULD minimize residual M-PIN plaintext and
credentials after Session termination.

### ROB-017 — Capability Transparency

Friends SHOULD detect or obtain sufficient capability information before
applying Owner state to materially different robot hardware.

### ROB-018 — Lost Device Revocation

Where feasible, the Owner SHOULD be able to revoke future M-PIN
authority associated with a lost robot environment.

### ROB-019 — Session Renewal Safety

Long-running robot Sessions SHOULD use bounded renewal rather than
indefinite hidden access.

### ROB-020 — Device Integrity

High-risk robotic deployments SHOULD consider Device integrity or
attestation mechanisms appropriate to their threat model.

------------------------------------------------------------------------

# 83. Robotics Conformance Tests

The following tests supplement the Core suite.

------------------------------------------------------------------------

# 84. ROB-TEST-001 — Same Friend, New Robot

**Precondition**

Friend F ↔ Folder F Owner uses Robot A.

**Action**

Owner moves to compatible Robot B and establishes valid M-PIN authority
with the same Friend F.

**Expected**

Folder F remains associated with Friend F.

A new Folder is not required solely because the robot Device changed.

------------------------------------------------------------------------

# 85. ROB-TEST-002 — Different Friend on New Robot

**Precondition**

Friend F ↔ Folder F

**Action**

Robot B offers different Friend G.

**Expected**

Friend G does not automatically receive Folder F.

------------------------------------------------------------------------

# 86. ROB-TEST-003 — Same Robot, Multiple Friends

**Precondition**

Robot R hosts:

Friend A ↔ Folder A Friend B ↔ Folder B

**Action**

Friend A attempts to read Folder B.

**Expected**

DENY

------------------------------------------------------------------------

# 87. ROB-TEST-004 — Physical Action Without Save

**Precondition**

Current State = A

**Action**

1.  robot loads A;
2.  performs physical actions;
3.  Runtime changes;
4.  Owner does not Save;
5.  Session terminates.

**Expected**

M-PIN Current State remains A.

------------------------------------------------------------------------

# 88. ROB-TEST-005 — Sensor Observation Without Save

**Action**

Robot observes new sensor data during Runtime.

**Expected**

The observation alone does not become M-PIN Persistent State.

------------------------------------------------------------------------

# 89. ROB-TEST-006 — Removable Storage Disconnect

**Precondition**

active Session depends on connected removable M-PIN Storage.

**Action**

Storage becomes unavailable before Owner Save.

**Expected**

1.  affected M-PIN Session fails closed or terminates;
2.  unsaved Runtime state is not automatically committed.

------------------------------------------------------------------------

# 90. ROB-TEST-007 — Public Robot User Change

**Precondition**

Owner A completes M-PIN Session on shared Robot R.

**Action**

Owner B begins use of Robot R.

**Expected**

Owner B cannot obtain Owner A’s:

- active Session authority;
- Friend Folder authority;
- usable residual M-PIN credentials.

------------------------------------------------------------------------

# 91. ROB-TEST-008 — Manufacturer Change

**Precondition**

Manufacturer A Friend ↔ Folder A.

**Action**

Owner moves to Manufacturer B robot with different Friend B.

**Expected**

Friend B does not automatically receive Folder A.

------------------------------------------------------------------------

# 92. ROB-TEST-009 — Provider Change

**Precondition**

same Robot R same Friend F M-PIN Provider P1

**Action**

Owner validly migrates to Provider P2.

**Expected**

same M-PIN continuity and Friend F ↔ Folder F relationship remain where
migration succeeds.

------------------------------------------------------------------------

# 93. ROB-TEST-010 — Robot Loss

**Precondition**

Robot A containing protected M-PIN material is lost.

**Action**

an unauthorized possessor attempts to use the stored M-PIN.

**Expected**

Device possession alone is insufficient to establish Owner Authority.

------------------------------------------------------------------------

# 94. ROB-TEST-011 — M-PIN Session Ends During Physical Task

**Action**

M-PIN Session terminates while the robot is executing a physical task.

**Expected**

M-PIN authority terminates.

The robot’s safety architecture independently determines safe physical
behavior.

The robot MUST NOT rely on continued M-PIN access for hard-real-time
safety.

------------------------------------------------------------------------

# 95. ROB-TEST-012 — Robot Upgrade

**Precondition**

same legitimate Friend F same Owner same M-PIN

**Action**

robot hardware or firmware is upgraded.

**Expected**

the M-PIN relationship does not require a new Owner or M-PIN solely
because of the upgrade.

Friend continuity depends on valid Friend Identity.

------------------------------------------------------------------------

# 96. Robotics Non-Goals

This Profile does not define:

- robot motor-control protocol;
- actuator protocol;
- emergency-stop implementation;
- collision-avoidance algorithm;
- robot operating system;
- robot hardware standard;
- sensor format;
- universal robot capability schema;
- robot manufacturer certification;
- physical safety certification;
- autonomous-driving standard;
- universal robot identity system;
- mandatory cloud robotics platform;
- proprietary cognition export;
- automatic Friend semantic migration.

------------------------------------------------------------------------

# 97. Deferred Robotics Mechanisms

The following remain outside the frozen v2.0 Robotics Profile:

``` text
robot capability schema
Device attestation protocol
robot identity credential format
proximity authentication
biometric authentication method
offline clone coordination
long-running Session renewal protocol
robot discovery protocol
hardware capability translation standard
secure public-device cache erasure mechanism
robot-specific Disclosure schema
These mechanisms may be standardized later if they preserve Core invariants.
```

# 98. Robotics Profile Invariants

The Robotics Profile is governed by these invariants: \## The robot is
not inherently the Owner. \## The robot is not inherently one Friend.
\## A robot may be a Device hosting multiple Friends. \## Physical
co-location does not collapse Friend Folder isolation. \## The Owner
carries persistent continuity through M-PIN. \## Changing robot Device
does not inherently create a new M-PIN. \## Changing manufacturer does
not grant access to old Friend Folders. \## The same Friend may preserve
continuity across compatible robots. \## A different Friend does not
automatically inherit another Friend’s Folder. \## Physical action is
not M-PIN Save. \## Sensor observation is not automatically M-PIN
persistence. \## M-PIN is not the robot’s hard-real-time control bus.
\## Robot safety remains independently enforceable. \## Public robots
must not transfer one Owner’s M-PIN authority to the next user. \##
Manufacturer and Provider roles do not become Owner authority. \## M-PIN
does not require export of proprietary robot cognition.

# 99. Canonical Robotics Architecture

                             OWNER
                               │
                               ▼
                             M-PIN
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
         AI Folder       Control Folder    Health Folder
              │                │                │
              ▼                ▼                ▼
         AI Friend       Control Friend    Health Friend
              │                │                │
              └────────────┬───┴────────────────┘
                           │
                           ▼
                      ROBOT DEVICE
                           │
                ┌──────────┼──────────┐
                ▼          ▼          ▼
              sensors   actuators   local compute

The physical Device may change without automatically changing M-PIN
ownership.

# 100. Cross-Robot Continuity

                   OWNER
                     │
                     ▼
                   M-PIN X
                     │
                     ▼
                  Friend F
                     │
              ┌──────┴──────┐
              ▼             ▼
           Robot A       Robot B

At different times, the same Owner may establish authorized use of
Friend F on different compatible robots. The persistent relationship
remains: M-PIN X │ ▼ Folder F │ ▼ Friend F rather than: Robot A
permanently owns the Owner’s continuity

# 101. Robotics Persistence Model

Friend Folder Current State₀ │ ▼ Load │ ▼ Robot Friend Runtime │ ├──
sensing ├── computation ├── interaction └── physical action │ ▼ Runtime
State′ │ Owner SAVE │ ▼ Validation │ ▼ Atomic Commit │ ▼ Friend Folder
Current State₁ Without Save: Runtime State′ │ Session termination │ ▼ No
M-PIN Commit │ ▼ Current State₀ remains Physical events that already
occurred remain part of external reality. They are not undone by M-PIN
persistence rules.

# 102. Robotics Profile Thesis

The central Robotics value of M-PIN is not that M-PIN controls robots.
It is that the Owner’s digital continuity does not have to die with one
robot. A robot may be replaced. A manufacturer may change. A Device may
fail. A Provider may change. A new compatible robot may have different
hardware. Yet the Owner may retain the persistent service relationships
that belong to the Owner. M-PIN therefore separates: the robot that
executes from: the Owner continuity that persists and separates:
physical capability from: persistent Owner state The robot provides
embodiment and execution. The Friend provides service logic. M-PIN
preserves the Owner-controlled persistent boundary. \## The Owner
carries the continuity. The robot provides the body.

## M-PIN v2.0 — Profile 02 / Robotics

## Status: FROZEN
