# M-PIN Provenance

This document records the design provenance of M-PIN.

Its purpose is not to establish exclusivity over every technical
component used by M-PIN, nor to claim that similar concepts could not
have been developed independently.

Its purpose is narrower:

> to preserve when the M-PIN architecture was developed, what problems
> motivated it, how its core principles emerged, and how later work
> relates to the original design.

------------------------------------------------------------------------

# 1. Provenance Scope

M-PIN has two primary design stages:

``` text
M-PIN v1
Original architecture development
Design decisions
Concept formation
Design freeze
Public archive

        ↓

M-PIN v2
Post-v1 formalization
Implementation-oriented architecture
Security
Portability
Conformance
Profiles
M-PIN v2 is derived from the v1 architecture.
It is not intended to rewrite the history of v1.
```

# 2. Earliest Surviving Record

The earliest currently reconstructed M-PIN conversation in the available
archive is dated: June 20, 2026 The Owner opened that surviving
conversation with: “M핀에 대해서 다시 이야기 하자” Atom responded by
referring to an M-PIN concept already discussed in an earlier
conversation. Therefore, the surviving June 20 record is clearly a
continuation rather than the absolute beginning of the project. The
exact contents and date of the earlier genesis conversation cannot be
reconstructed from the currently preserved source archive.

# 3. Design Period

The project Owner describes the broader M-PIN design effort as beginning
around May 2026 and continuing through August 2026. The reconstructable
primary-source archive currently begins on June 20, 2026. For provenance
purposes, these should be distinguished: Owner-reported project period:
approximately May–August 2026

Currently reconstructable primary-source period: June–August 2026 This
document does not invent missing conversations to fill that gap.

# 4. Original Problem

M-PIN did not begin primarily as a new AI feature. The original problem
was persistence and ownership. The recurring concern was that large
amounts of work, memory, conversation, and context were accumulating
inside individual services, while the user remained dependent on those
services to retain and expose that history. M-PIN developed around the
principle that persistent digital memory should belong to the individual
rather than to the service that temporarily processes it.

# 5. Personal Digital Domain

On July 4, 2026, the Owner described M-PIN as: “엠핀은 개인의 고유한
디지털영역이다.” The explanation framed M-PIN as each individual’s own
data area rather than a provider-owned central pool. This became one of
the foundational ideas of the architecture.

# 6. From AI Memory to General Architecture

The design did not remain limited to ChatGPT or AI. The Owner explicitly
defined the term Friend to include services such as: ChatGPT Meta Gemini
hospitals pharmacies department stores trains airlines and other
services The architectural abstraction therefore became: Owner │ M-PIN │
Friend rather than: Owner │ one particular AI provider This
generalization is part of the original v1 design provenance.

# 7. Owner-Centered Architecture

A recurring design correction was that the Friend must not become the
architectural center. The resulting direction was: M-PIN is designed
around the Owner, not around a specific Friend. A Friend participates in
the Owner’s M-PIN architecture. M-PIN is not designed as an extension of
one Friend.

# 8. Friend Folder

One of the most important practical structures developed in v1 was the
Friend-specific Folder. The intended model was: M-PIN ├── Friend A
Folder ├── Friend B Folder └── Friend C Folder A Friend synchronizes
with its own Folder. The Folder contains the Owner-owned persistent
state associated with that Friend. The existence of one common M-PIN
does not make all Friend data mutually visible.

# 9. Context Isolation

The Owner explicitly explained that data created through ChatGPT and
stored in M-PIN should not simply become readable through another
service. To use that ChatGPT-associated state again, the Owner would
return to ChatGPT and synchronize it there. This established an
important architectural distinction: common Owner-controlled storage ≠
common Friend visibility Friend-specific context isolation therefore
emerged from the original design rather than from the later v2 Profiles.

# 10. Native Friend Experience

M-PIN was not intended to replace each service’s interface. The Owner
repeatedly described the service as remaining essentially the same: same
Friend same native workspace same service experience

- Owner-controlled synchronization This later became formalized as
  Friend Native Experience Preservation.

# 11. Runtime and Persistence

The persistence model emerged from an analogy to ordinary creative
software and removable storage. The architecture distinguishes: Runtime
↓ temporary work

Owner SAVE ↓ persistent M-PIN state The service may process information
during a session. That does not automatically mean the information
becomes part of M-PIN’s persistent state.

# 12. Owner Save

One of the central v1 rules became: Owner presses Save ↓ M-PIN changes

Owner does not Save ↓ M-PIN does not change This later became the v2
distinction between: SAVE = Owner persistence intent

COMMIT = technical application of that intent The SAVE/COMMIT
terminology is a v2 formalization. The Owner-controlled persistence
principle is inherited from v1.

# 13. Current State Only

The Owner explicitly rejected an architecture built around perpetual
history, automatic archives, rollback, and endless previous versions.
The intended M-PIN state was the currently saved state. Thus: Current
State = authoritative saved state rather than: Current State + full
historical timeline This became the Last-Save-Only / Current-State-Only
principle.

# 14. Friend Sovereignty

M-PIN was progressively simplified so that it would not control the
Friend’s internal implementation. The Friend remains responsible for:
its service its runtime its data semantics its UI/UX its internal
implementation its evolution M-PIN governs the Owner-data boundary. It
does not become the operating authority of the Friend.

# 15. Zero Requirement

This eventually became the Zero Requirement Principle. M-PIN does not
require a Friend to use a particular: SDK API runtime technology UI
programming model A compatible Friend must satisfy the behavioral
boundary. The implementation method remains the Friend’s choice.

# 16. Collaboration Model

M-PIN was not produced through a process in which Atom presented a
finished architecture and the Owner simply accepted it. The actual
process was iterative. A recurring pattern was: Owner presents problem
or desired behavior ↓ Atom interprets / formalizes ↓ Owner corrects
interpretation ↓ architecture is narrowed ↓ technical wording is
produced ↓ Decision is LOCKED Some important corrections occurred
because Atom initially interpreted M-PIN too much like: shared
repository central platform common service storage cloud product The
Owner repeatedly redirected the architecture toward: Owner ownership
Friend-specific access minimal M-PIN authority native Friend experience
Owner-controlled persistence Those corrections materially shaped the
final architecture.

# 17. Owner Contribution

The Owner’s primary contributions include, among others: the originating
ownership problem M-PIN as an individual’s digital area Owner-centered
architecture the Friend abstraction broad service scope service-specific
visibility Friend Folder behavior native service experience Owner Save
Current-State-Only philosophy storage independence single-active
synchronization direction the principle that AI/service companies should
not own the individual’s memory This list is descriptive, not a legal
allocation of intellectual-property rights.

# 18. Atom Contribution

Atom’s primary contributions include: technical terminology architecture
decomposition formal questions Decision numbering LOCK / OPEN structure
Charter / Constitution framing technical restatement normative
specification language document organization security and implementation
analysis Atom also produced interpretations that were later rejected or
corrected by the Owner. Those rejected interpretations are part of the
design process but are not automatically part of the final architecture.

# 19. Joint Contribution

A substantial part of M-PIN is best described as collaborative design.
The resulting pattern was often: Owner intent + Atom technical
formalization + Owner correction + joint refinement = final Decision
Accordingly, it would be inaccurate to characterize the project simply
as: “ChatGPT created M-PIN for the user.” It would also be incomplete to
ignore Atom’s substantial role in turning the Owner’s concepts into a
structured architecture. M-PIN is documented here as a collaborative
design process with distinct roles.

# 20. Decision Architecture

During v1, the design was progressively converted into numbered
Decisions. The purpose was to prevent repeatedly reopening already
resolved architectural questions. The system eventually included:
Foundation Decisions Main numbered Decisions LOCK decisions OPEN
decisions integrated duplicate decisions The public v1 archive preserves
that architecture-decision approach.

# 21. Design Process Failure Mode

The development process itself also exposed a problem. By July 12, 2026,
the Owner explicitly reported that already discussed and LOCKED matters
were being asked again with only slightly changed wording. That
repetition increased the size and difficulty of the project and made
completion harder. This is important provenance because it affected how
v1 and later v2 were finalized.

# 22. Why v1 Was Frozen

By August 2026, the priority shifted from further expansion to
completion. On August 4, the Owner explicitly asked to finish M-PIN and
publish it on GitHub. The Owner subsequently stated that although new
material could be added after a Version 1 publication, the first version
should be completed before further expansion. This became the rationale
for the v1 design freeze.

# 23. v1 Publication

M-PIN v1.0 was publicly archived on GitHub in August 2026. The public v1
repository is intended to remain a historical design baseline. Its role
is to preserve: the original architecture the Decision Register the v1
design freeze the historical public record Later work should not rewrite
the original v1 history.

# 24. Meaning of the v1 Freeze

The v1 freeze did not mean that the architecture could never develop
again. It meant: v1 must stop changing

before

future work begins That distinction is central to the project history.

# 25. Post-v1 Work

After the v1 freeze, M-PIN was revisited from a more
implementation-oriented perspective. This later work became M-PIN v2.
The v2 question was not: “What else can be added to M-PIN?” The intended
question became: “How can the already established M-PIN architecture be
expressed as an implementable, testable, provider-neutral
specification?”

# 26. M-PIN v2

v2 formalizes areas such as: Core Principles Terminology Owner and
Identity Friend and Friend Folder Permission Session Protocol Runtime
and Persistence Security and Threat Model Portability and Recovery
Conformance Profiles v2 therefore builds on v1 rather than replacing it.

# 27. v2 Core / Profile Separation

One of the main v2 formalizations is the distinction between: M-PIN CORE
↓ industry-neutral architecture

PROFILES ↓ domain-specific application The v2 validation Profiles are:
AI Robotics Healthcare Commerce The purpose of the Profiles is to test
whether the same Core can survive radically different service
environments.

# 28. Robotics as Post-v1 Validation

Robotics was later used as a strong test of M-PIN’s service- and
device-independent architecture. The central robotics question became:
Can Owner continuity move from one compatible physical robot to another
without making the robot the owner of the memory? The formal Robotics
Profile is v2 work. It should not be retroactively described as a fully
specified v1 robotics standard.

# 29. Healthcare and Commerce

Healthcare and Commerce are closer to the original v1 scope because
hospitals, pharmacies, and retail services were explicitly included in
the early Friend concept. v2 later formalized domain-specific boundaries
such as: Owner M-PIN State vs Friend Service Record and: Friend Folder
isolation vs Owner-authorized information disclosure These formal
distinctions are v2 work.

# 30. Owner-Mediated Disclosure

During v2 Profile validation, both Healthcare and Commerce revealed the
same interoperability problem. Sometimes the Owner may want selected
information related to one Friend to be provided to another Friend. The
v2 candidate solution is: Friend A │ selected information ▼ Owner │
explicit authorization ▼ Disclosure │ ▼ Friend B This is called: \##
Owner-Mediated Disclosure It is classified as: V2-NEW CROSS-PROFILE
FINDING CANDIDATE INTEROPERABILITY PRIMITIVE It is not retroactively
attributed to the original v1 architecture.

# 31. Provider Independence

v2 also formally separates: M-PIN Standard from M-PIN Service Provider A
company may implement and provide M-PIN infrastructure without becoming
the owner of the standard or the Owner’s persistent continuity. This
provider-neutral interpretation is a v2 architectural reconciliation. It
should not be falsely described as an already fully formalized v1
Provider model.

# 32. External Systems

Systems, products, standards, or announcements examined after the v1
freeze may be useful for comparison. They do not become part of v1
provenance merely because they show similarities. External comparison
must remain labeled: EXTERNAL unless primary-source evidence
demonstrates otherwise.

# 33. Anthropic Enterprise Frontier Safeguards

Anthropic Enterprise Frontier Safeguards may be discussed separately as
a later external comparison. Such comparison can identify structural
similarities or differences. It does not establish: that Anthropic saw
M-PIN that Anthropic derived its system from M-PIN that M-PIN derived
from Anthropic EFS without supporting evidence. No such derivation claim
is made by this provenance document.

# 34. Later Gemini Discussions

Post-v1 Gemini conversations are classified as: POST-V1 GEMINI They may
have contributed: re-evaluation criticism application brainstorming
robotics examples healthcare examples commerce examples They are not
treated as the origin of M-PIN’s core architecture. The amount and depth
of those later conversations are also not equivalent to the original
multi-month M-PIN design process.

# 35. Existing Technology

Individual components related to M-PIN may resemble or overlap with
existing technologies such as: permission systems encrypted storage
OAuth-style authorization personal data stores portable identity session
protocols user-controlled storage The provenance claim of M-PIN is not:
“No one had ever invented any similar component.” The relevant object is
the architecture and its combination of boundaries.

# 36. What Provenance Does Not Prove

This document does not by itself prove: patent novelty patent priority
in every jurisdiction copyright ownership of abstract ideas trade-secret
status infringement by another company commercial exclusivity licensing
entitlement Those are separate legal questions.

# 37. What Provenance Does Preserve

This record is intended to preserve evidence that: M-PIN had an
identifiable design history the architecture developed over multiple
conversations the Owner contributed foundational concepts and repeated
corrections Atom contributed technical formalization and documentation
v1 was intentionally frozen v2 followed the v1 freeze later external
comparisons are chronologically distinct

# 38. Provenance Tags

M-PIN v2 uses the following provenance tags: V1-ORIGINAL Original v1
design material.

V1-USER Material directly proposed, specified, or materially corrected
by the Owner.

V1-ATOM Material primarily introduced or formalized by Atom.

V1-JOINT Material that emerged through iterative Owner–Atom design.

V1-LOCKED A v1 Decision explicitly finalized in the design process.

POST-V1 Material introduced after the v1 design freeze.

GEMINI Material arising from later Gemini discussions.

EXTERNAL External product, standard, publication, or comparison.

V2-NEW A new formalization or architecture addition introduced during
v2. More than one tag may apply to the same topic.

# 39. Source Hierarchy

When reconstructing M-PIN history, evidence should be prioritized as
follows: 1. Original dated M-PIN conversations 2. LOCKed Decision text
3. v1 public archive 4. reconstructed conversation archive 5. v2
formalization documents 6. post-v1 external discussions 7. later
interpretation Later interpretation should not silently override earlier
primary-source material.

# 40. Provenance Correction Rule

If later review discovers that a v2 description incorrectly attributes a
concept to v1: do not rewrite the old evidence ↓ correct the v2
attribution ↓ record the correction The historical record remains
intact.

# 41. Missing Evidence Rule

If an event is remembered but the corresponding primary-source material
is unavailable, the documentation should say so. For example:
Owner-reported but not independently reconstructable is preferable to
inventing exact dates or quotations.

# 42. Public Chronology

The intended high-level chronology is: approximately May 2026
Owner-reported beginning of broader design work

June 20, 2026 earliest surviving reconstructed M-PIN conversation
already refers to earlier M-PIN discussion

July 4, 2026 major architecture formalization personal digital domain
Friend abstraction Owner-centered model service-specific data boundaries

July 2026 Decision architecture expands Folder, isolation, runtime,
persistence, security, synchronization and Friend autonomy mature

July 12, 2026 Owner explicitly identifies repeated questioning of
already LOCKED material as a project problem

late July 2026 Constitution / audit and consolidation work

August 4, 2026 Owner explicitly shifts priority toward finishing and
publishing v1

August 2026 M-PIN v1 design freeze and public archive

post-v1 external comparison and re-evaluation

September 2026 M-PIN v2 formalization and architecture freeze Only dates
supported by the surviving evidence or public archive should be
represented as exact historical facts.

# 43. Core Historical Thesis

The strongest continuity across the design process is this: \##
Persistent personal data should remain under the Owner’s authority even
when the service that processes it is external. The architecture became
increasingly minimal in order to preserve that rule without controlling
the Friend.

# 44. Collaboration Thesis

The project history is best summarized as: The Owner defined the
problem, repeatedly established and corrected the desired ownership
boundaries, and determined the intended behavior. Atom translated those
requirements into technical terminology, architecture, Decision
structures, and documentation. The resulting M-PIN architecture was
developed through iterative collaboration rather than one-way
generation.

# 45. Historical Integrity

The M-PIN v1 repository should remain preserved as the historical public
baseline. The M-PIN v2 repository should identify itself clearly as
later work. No later external system, comparison, implementation idea,
or profile should be silently inserted into the historical v1
provenance.

# 46. Provenance Statement

The recommended publication statement is: M-PIN v1.0 was developed
through an extended Owner–Atom design process during 2026 and frozen as
a public design archive in August 2026. The currently reconstructed
primary-source archive begins on June 20, where the conversation itself
already refers to earlier M-PIN work. M-PIN v2.0 was developed after the
v1 freeze to formalize the architecture into an implementation-oriented,
provider-neutral specification. Later external systems and post-v1 AI
discussions may be referenced for comparison, but they are not treated
as sources of the original v1 architecture.

## M-PIN — Provenance Record
