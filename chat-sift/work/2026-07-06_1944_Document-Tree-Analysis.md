# Document Tree Analysis
Date (UTC): 2026-07-06 19:44
Conversation ID: 6a4c057a-ec00-83eb-90e9-66883aba2da7
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-008.json

[M1] ME (2026-07-06 19:44):
Hold this : Having reviewed all eight files, the core finding is that the pack contains four generations of the same thinking with four competing document trees and numbering schemes: A (the Rev A manual, most refined — 24-doc register, three architecture rules, gap-closure methodology), B (clause-level numbers and acceptance values plus the SEC/DOC xlsx tree), C (the deepest execution library — SYS-xxx numbering, gates, checklists, worked test formats), and D (the raw chat log behind the 18-branch tree). Two housekeeping discoveries worth flagging: the four "docx" files are actually plain text, and UKAEACCFECP2512.PDF is actually a ZIP of page images of the UKAEA JET optical-fibre paper — domain context only, not a compliance input. The spec sets precedence (this spec → A → C → B → D), and Section 11 is a reconciliation matrix proving every item from every tree has a canonical home, with seven recorded conflicts and their resolutions (e.g. EMC out per A, B's "Declaration of Conformity" retired for a Statement of Compliance, boundary/intended-use docs merged per A's anti-proliferation rule).
How the output is demonstrated — resolving your design-vs-safety instruction: completeness is proven by three layers. The Master Document List carries every canonical document with an evidence state (E1 verified through E5 must-create), so absences appear as recorded lines rather than silence. The safety and cross-reference layer (compliance matrix, hazard register, single-fault analysis, safety requirements, verification matrix, Safety Document) is Class F — authored full and thorough, every clause and every hazard, placeholders permitted only in evidence fields, never in analysis. The design data is Class D — one Design Data Update Register listing concrete updates required per existing schematic, drawing, PCB, FPGA and LabVIEW document, with an explicit ban on redrawing. A strict fabrication ban applies throughout: no invented measurements, ratings or clause text, ever.
Sizing. Nine phases (0–8) mapped onto A's eight activities, B's five phases and C's gates A–I, producing ~31 controlled register entries (20 full-author, 8 delta-managed, 3+ reference) plus 8–15 new bench-test records. Envelope: 25–43 engineer-day equivalents, of which roughly two-thirds is documentation/analysis executable by an agent from the data pack alone, and one-third is human-dependent (photo survey, bench tests, gate sign-offs, residual-risk acceptances). The critical path is the Phase 4 clause matrix (~100+ assessable requirements), then Phase 5 test scheduling around beam-campaign access.
Validating questions (full table with defaults and risk-if-wrong is Section 10; each has a default so a future agent can proceed unblocked):
Blocking (Gate 0): Q1 — confirm the claim level is C's wording ("internally assessed and documented against applicable requirements of IEC 61010-1... not third-party certification")? Q2 — which edition of 61010-1 is licensed, and are 2-030/2-201 being procured for screening? Q3 — which serial/build is the frozen baseline, and do variants sit inside the claim? Q4 — boundary rulings: DUT PCB and supplied cable sets in, DUT sensor out? Q5 — hardware modification confirmed excluded as a closure route, and who owns escalation of un-closable findings? Q6 — adopt the hybrid numbering (A's register + C's SYS-xxx), and assign the blank system designation from A's title block?
Shaping (by Gate 1): Q7 — when is physical access available for photos and the bench tests, and who is the competent person? Q8 — what historical evidence exists (PAT, earth-bond, insulation, PSU certs) and where's the archive? Q9 — who signs as design authority, and is an independent reviewer available? Q10 — confirm OVC II / PD2 and B's environmental profile? Q11 — confirm EMC stays out of scope with only a two-page position stub? Q12 — does monitors-armed hard-wire into facility interlocks or is it internal gating only (this one materially changes the boundary if wrong)?
Confirmatory (by Gate 3): Q13 — UKAEA paper is context only? Q14 — adopt B's numbers (0.1 Ω, 3.0/6.3 mm, 10°, 150 N, V-0) as provisional acceptance criteria pending clause confirmation? Q15 — any beam-campaign or safety-committee deadline that should pull the schedule? Q16 — resolve the cable-length discrepancy (~25 m in A vs "up to 15 m+" in C) and the extension-cable policy.
The strategic sequencing note carried through from C stands: don't start by rewriting everything — the five steering documents (boundary, baseline, hazard register, clause matrix, verification plan) control the whole job, and the Gen-2 extraction in Phase 8 is where the retrospective effort pays forward. If you can answer even just Q1–Q6, I can fold them into a Rev B of the spec now.

[M2] AI (2026-07-06 19:44):
Held.

This reads as a strong executive synthesis of the retrospective IEC 61010 programme and captures the key decisions, assumptions and execution strategy. The main elements are:

- **Source hierarchy established:** Four generations (A–D) reconciled with explicit precedence:
  1. This specification
  2. A (Rev A manual)
  3. C (SYS execution library)
  4. B (clause/SEC-DOC tree)
  5. D (raw chat archive)

- **Reconciliation complete:** Seven document-tree conflicts resolved, with Section 11 providing traceability so every historical document has a canonical destination.

- **Evidence philosophy defined:**
  - Master Document List with evidence states E1–E5.
  - Safety documentation treated as complete engineering analysis (Class F).
  - Design documentation treated as delta updates only (Class D).
  - Explicit prohibition on inventing dimensions, ratings or compliance evidence.

- **Programme sizing:**
  - Nine phases (0–8).
  - Approximately 31 controlled documents.
  - 8–15 new verification records.
  - Approximately 25–43 engineer-days.
  - Around two-thirds documentation/analysis and one-third physical verification.

- **Critical path identified:**
  1. IEC 61010 clause assessment matrix.
  2. Physical verification and beam-time dependent testing.

- **Decision register structured as questions:**
  - Gate 0 (Q1–Q6): compliance claim, edition, baseline, boundary, modification policy, numbering.
  - Gate 1 (Q7–Q12): evidence, authority, environment, EMC scope, facility interfaces.
  - Gate 3 (Q13–Q16): contextual documents, provisional criteria, programme dates, cable policy.

- **Strategic principle preserved:**
  Begin with the steering documents (boundary, baseline, hazards, clause matrix and verification plan), not wholesale document rewriting. This keeps the programme controlled and enables the Gen-2 system to inherit a mature compliance framework.

Overall, this is suitable as the executive summary or opening synopsis of the retrospective IEC 61010 specification. It clearly communicates scope, methodology, assumptions, deliverables, and decision gates while remaining aligned with your intention of achieving a thoroughly documented, internally assessed system rather than claiming formal third-party certification.

[M3] ME (2026-07-06 19:45):
Hold this : 
[attached file: Pasted markdown.md]

[M4] AI (2026-07-06 19:45):
Held as the controlling **Rev A job specification** for the retrospective IEC 61010 survey and TCF uplift. fileciteturn0file0L1-L5

[M5] ME (2026-07-06 19:47):
The attached is the combined effort across multiple platforms. I need this to be completely restructured as a full manual that supports the above job specification. Write the response here as structured as possible
[attached file: 61010 All.docx]

[M6] AI (2026-07-06 19:47):
I’m consolidating the combined 100-page source into one controlled execution manual aligned to the Job Specification, removing duplicated trees, conflicting numbering, and provisional claims. I’ll preserve useful procedures, templates, gates, checklists, and acceptance logic while making the specification the governing authority.

[M7] AI (2026-07-06 19:48):
The source contains four overlapping manuals rather than one coherent procedure. The new structure will therefore separate: governing rules, phase-by-phase work instructions, document-specific authoring instructions, evidence/gap controls, review gates, and reusable templates—while retaining the system-specific electrical, mechanical, cabling, FPGA/LabVIEW, and beamline checks.

[M8] AI (2026-07-06 19:48):
Below is the restructured **master execution manual**. It treats `JOB-SPEC-61010-001` as the controlling specification and converts the combined 100-page source into a single operational procedure, retaining its detailed checklists, test formats, risk methods, software analysis, cabling review and Generation-2 requirements while removing duplicated document trees and conflicting instructions. fileciteturn2file2 fileciteturn2file0

:::writing{variant="document" id="68431"}
# RETROSPECTIVE IEC 61010 COMPLIANCE UPLIFT  
## EXECUTION AND TECHNICAL CONSTRUCTION FILE MANUAL

**Heavy-Ion Radiation Test System — Image Sensor Characterisation Rig, Generation 1**

| Field | Value |
|---|---|
| Manual ID | MAN-61010-001 |
| Revision | A — Draft for review |
| Date | 6 July 2026 |
| System designation | `[ASSIGN — Q6]` |
| Controlling job specification | JOB-SPEC-61010-001 |
| Applicable system | Generation-1 heavy-ion radiation image-sensor characterisation system |
| Process owner | `[ASSIGN]` |
| Design authority | `[ASSIGN — default: Paul]` |
| Independent reviewer | `[ASSIGN]` |
| Document status | Controlled draft |
| Supersedes | The combined A/B/C/D working manuals and competing document-tree instructions |
| Classification | Internal engineering process document |

---

# DOCUMENT APPROVAL

| Role | Name | Signature | Date |
|---|---|---|---|
| Author/process owner |  |  |  |
| Design authority |  |  |  |
| Independent safety reviewer |  |  |  |
| Configuration/document control |  |  |  |

---

# REVISION HISTORY

| Revision | Date | Description | Author | Approval |
|---|---|---|---|---|
| A | 6 July 2026 | Initial consolidated execution manual supporting JOB-SPEC-61010-001 |  |  |

---

# CONTENTS

1. Purpose  
2. Scope  
3. Governing principles and source precedence  
4. Intended compliance position  
5. System summary  
6. Definitions and abbreviations  
7. Organisation, responsibilities and competence  
8. Technical Construction File architecture  
9. Document classes and evidence states  
10. Programme lifecycle and review gates  
11. Phase 0 — Initiation and framing  
12. Phase 1 — Boundary, intended use and classification  
13. Phase 2 — Configuration freeze and evidence harvest  
14. Phase 3 — Hazard analysis and safety requirements  
15. Phase 4 — Clause mapping and gap assessment  
16. Phase 5 — Evidence formalisation and verification  
17. Phase 6 — Gap closure, manuals and operational controls  
18. Phase 7 — TCF assembly, Safety Document and release  
19. Phase 8 — Generation-2 requirements extraction  
20. Document-specific production instructions  
21. Electrical safety assessment procedure  
22. Propagation cable and DUT-interface assessment  
23. Mechanical and trolley safety assessment  
24. Software, FPGA, LabVIEW and logging assessment  
25. Verification and test management  
26. Gap, concession and residual-risk management  
27. Traceability and cross-reference control  
28. Document control and configuration management  
29. Quality assurance and prohibited practices  
30. Project planning and execution priorities  
31. Completion criteria  
Appendix A — Canonical document register  
Appendix B — TCF folder structure  
Appendix C — Mandatory templates  
Appendix D — Review-gate checklists  
Appendix E — System-specific survey checklists  
Appendix F — Validation-question register  
Appendix G — Approved compliance wording  
Appendix H — Generation-2 seed requirements  

---

# 1. PURPOSE

## 1.1 Purpose of this manual

This manual defines how to execute the retrospective IEC 61010 compliance survey and Technical Construction File uplift required by JOB-SPEC-61010-001.

The job specification defines:

- the required outputs;
- the canonical document set;
- the governing evidence rules;
- the phased programme;
- the compliance claim constraints;
- the definition of completion.

This manual defines:

- how each phase shall be performed;
- how the engineering data pack shall be surveyed;
- how evidence shall be assessed and classified;
- how safety analyses shall be authored;
- how design-data updates shall be controlled without redrawing the existing design;
- how gaps shall be raised, closed or escalated;
- how verification shall be planned and recorded;
- how the TCF shall be reviewed, released and maintained;
- how findings shall be converted into Generation-2 requirements.

## 1.2 Nature of the exercise

This is a **retrospective conformity survey and technical-file uplift**.

It is not:

- a redesign programme;
- a hardware modification programme;
- a third-party certification exercise;
- a CE-marking exercise;
- a UKCA-marking exercise;
- a substitute for a licensed copy of the applicable standards;
- an instruction to invent missing technical evidence;
- a radiation-facility safety case.

## 1.3 Strategic objective

The work shall achieve two connected objectives:

1. Establish a defensible internal engineering position for the mature Generation-1 system.
2. Extract a reusable compliance-by-design framework for the Generation-2 system.

The retrospective work is therefore both an assurance activity and a requirements-capture activity.

---

# 2. SCOPE

## 2.1 System within scope

Unless changed by an approved boundary decision, the assessed system comprises:

- the mobile 19-inch rackmount trolley;
- the single 230 V AC mains input;
- mains inlet, switching, filtering, fusing and distribution;
- protective-earth connections and chassis bonding;
- internal AC/DC power supplies;
- low-voltage power distribution;
- bias generation and monitoring;
- signal-conditioning and propagation electronics;
- PXI, FPGA and LabVIEW elements required for system operation;
- safety-relevant firmware and software;
- controls, indicators and operator interfaces;
- supplied cable assemblies;
- the five signal classes:
  - bias and sense;
  - differential;
  - LVDS;
  - RF coaxial;
  - clock;
- the DUT support fixture;
- the interface PCB at or near the beamline;
- supplied accessories necessary for the defined configuration;
- operator and service documentation;
- labels and markings;
- configuration files required for safe and correct operation.

## 2.2 Normally excluded

Unless an interface or contractual requirement brings them into scope, the following are excluded:

- the radiation source;
- radiation shielding;
- facility dosimetry;
- facility emergency stops;
- facility beamline safety systems;
- host-building electrical installation;
- external customer equipment not supplied as part of the system;
- the DUT sensor itself;
- the facility radiation safety case;
- EMC testing under the IEC 61326 series;
- functional-safety certification under IEC 61508;
- market-access declarations or conformity marking.

## 2.3 Interface rule

An excluded system may still create an in-scope interface.

For each excluded item, the assessment shall determine:

1. What connection exists?
2. What signal, energy or information crosses the boundary?
3. Which party owns the interface?
4. Can failure outside the boundary create an in-scope electrical, thermal, mechanical or control hazard?
5. Does the Generation-1 equipment rely on the external system to remain safe?
6. Is the reliance contractual, procedural, physical or software-based?
7. Is the reliance documented in an ICD?

## 2.4 Hardware-modification constraint

Physical modification is excluded as a planned closure route.

Where an identified design condition cannot be justified by:

- verification;
- engineering analysis; or
- formal residual-risk acceptance,

the item shall be escalated as a significant finding.

It shall not be silently marked compliant.

---

# 3. GOVERNING PRINCIPLES AND SOURCE PRECEDENCE

## 3.1 Precedence

Where instructions conflict, apply the following order:

1. JOB-SPEC-61010-001.
2. This manual.
3. The controlling Rev A process manual.
4. The detailed execution library.
5. The master compliance blueprint and SEC/DOC tree.
6. The raw working discussion and 18-branch tree.
7. Uncontrolled working notes.

## 3.2 Three architecture rules

### Rule 1 — Group by ownership and change rate

Documents shall be separated where they have different:

- owners;
- approval routes;
- technical disciplines;
- revision cycles;
- evidence lifecycles.

Documents shall not be split merely because a topic has several subtopics.

Example: the five propagation signal classes belong in one Cabling ICD because they share the same physical boundary and ownership.

### Rule 2 — Reference rather than duplicate

Schematics, drawings, PCB packages, BOMs, FPGA design descriptions and LabVIEW design descriptions shall remain in their engineering homes.

Safety documents shall cite them by:

- document number;
- title;
- revision;
- applicable sheet, section or item.

Safety documents shall not copy whole design descriptions into new documents.

### Rule 3 — Keep FMEA and hazard assessment distinct

The FMEA is:

- bottom-up;
- failure-mode driven;
- detailed;
- relatively fast-changing.

The hazard register is:

- top-down;
- harm driven;
- controlled at a slower cadence;
- the basis of safety requirements and residual-risk acceptance.

Only safety-significant FMEA findings shall flow into the hazard register.

The hazard register shall not become a duplicate FMEA.

## 3.3 Steering-document principle

The work shall not begin by rewriting every document.

The following steering documents shall be established first:

1. SYS-SAF-001 — Equipment Boundary and Intended Use Statement.
2. SYS-CFG-001 — Current System Design Baseline.
3. SYS-RISK-001 — Hazard-Based Risk Assessment and Register.
4. SYS-COMP-002 — IEC 61010 Applicability and Gap Matrix.
5. SYS-VER-001 — Retrospective Safety Verification Plan and V&V Matrix.

These documents control all subsequent evidence collection and closure activity.

---

# 4. INTENDED COMPLIANCE POSITION

## 4.1 Default claim

Subject to formal confirmation at Gate 0, the approved claim is:

> The system has been retrospectively reviewed and documented against the applicable principles and requirements of IEC/BS EN 61010-1, with additional consideration of applicable particular standards, including external test and measurement circuits where relevant. This review does not constitute third-party certification unless separately assessed by an accredited body.

## 4.2 Permitted descriptions

The following descriptions may be used where supported by the evidence:

- reviewed against applicable IEC 61010 requirements;
- gap-assessed against IEC 61010;
- documented using an IEC 61010-referenced technical-assurance framework;
- safety rationale aligned with applicable IEC 61010 principles;
- internally assessed and technically documented;
- supported by risk, design-review and verification evidence.

## 4.3 Prohibited descriptions

Unless a separate formal conformity route supports them, the following shall not be used:

- certified;
- IEC 61010 certified;
- certified compliant;
- independently certified;
- fully compliant without qualification;
- CE declaration of conformity;
- UKCA declaration of conformity;
- approved by a test house;
- formally qualified to IEC 61010.

## 4.4 Clause references and numeric criteria

Exact clause references, test conditions and acceptance limits shall be taken from the licensed edition held by the organisation.

Until confirmed, provisional criteria shall be marked:

`[PROVISIONAL — CONFIRM AGAINST LICENSED STANDARD]`

This rule applies particularly to:

- protective-earth resistance;
- clearance;
- creepage;
- mechanical tilt;
- applied force;
- flammability classification;
- environmental limits;
- access-probe requirements;
- dielectric and insulation test levels;
- leakage or touch-current limits.

---

# 5. SYSTEM SUMMARY

The system is a mature heavy-ion radiation test system used for image-sensor characterisation and adaptable to other radiation forms through approved propagation arrangements.

The established system description is:

- mobile 19-inch rackmount trolley;
- approximately 1 m high;
- single 230 V AC supply;
- internally derived low-voltage DC supplies, typically of the order of 12 V;
- long cable runs between the rack and the beamline fixture;
- five signal classes;
- interface PCB on a support fixture exposed at or near the beamline;
- FPGA fault-supervision and event-capture functions;
- LabVIEW supervisory control;
- bias-current monitoring;
- split hardened/recoverable response to Single Event Latch-up;
- configurable dual-threshold fault detection;
- monitors-armed gating before beam-on;
- FPGA-latched sub-second event timing supplementing slower supervisory polling.

These features are not assumed to prove compliance. They are candidate controls requiring evidence, analysis and traceability.

---

# 6. DEFINITIONS AND ABBREVIATIONS

| Term | Definition |
|---|---|
| Baseline | The uniquely identified hardware, software, firmware, cabling and fixture configuration being assessed |
| Class D | Existing design data managed through a delta/update register |
| Class F | Fully authored safety, compliance, risk or cross-reference document |
| Class R | Reference material indexed but not re-authored |
| Closure evidence | Evidence demonstrating that a gap has been resolved |
| Compliance Matrix | Clause-by-clause applicability and evidence matrix |
| Concession | Formal acceptance of a known deviation or evidence limitation |
| DDR | Design Data Update Register |
| DUT | Device under test |
| E-state | Evidence-availability and review status |
| FMEA | Failure Modes and Effects Analysis |
| Gap | Missing, incomplete, unsuitable or conflicting evidence, control or process |
| Hazard | Potential source of harm |
| HUMAN-ACTION | Activity requiring physical access, competence, judgement or approval that shall not be simulated by an agent |
| ICD | Interface Control Document |
| MDL | Master Document List |
| MET | Main Earthing Terminal |
| PE | Protective Earth |
| Residual risk | Risk remaining after recognised controls have been considered |
| SEL | Single Event Latch-up |
| TCF | Technical Construction File |
| Verification | Confirmation through review, inspection, test, calculation or other objective evidence |
| V&V Matrix | Requirements-to-verification traceability matrix |

---

# 7. ORGANISATION, RESPONSIBILITIES AND COMPETENCE

## 7.1 Required roles

| Role | Primary responsibility |
|---|---|
| Process owner | Controls the programme and this manual |
| Design authority | Owns technical decisions, escalations and final engineering acceptance |
| Compliance lead | Owns standards register, clause matrix and assurance strategy |
| Configuration manager | Freezes the baseline and controls document status |
| Electrical reviewer | Reviews mains, PE, power distribution, isolation and accessible circuits |
| Mechanical reviewer | Reviews trolley, enclosure, fixture, stability and handling |
| Software/firmware reviewer | Reviews FPGA, LabVIEW, safe states, configuration and logging |
| Verification lead | Owns verification planning, methods, equipment and reports |
| Competent test engineer | Performs physical electrical and functional tests |
| Independent reviewer | Challenges completeness, reasoning and residual-risk decisions |
| Document controller | Releases and archives approved records |
| Facility representative | Confirms beamline boundaries, access restrictions and interface ownership |

One person may hold more than one role, but each responsibility shall remain explicit.

## 7.2 Competence requirements

Work shall be assigned according to competence.

Examples:

- live or mains-adjacent work: electrically competent person;
- PE, insulation or touch-current tests: competent test engineer using suitable calibrated equipment;
- risk acceptance: authorised design authority;
- facility interface decisions: facility representative or interface owner;
- software safety analysis: engineer familiar with the actual FPGA/LabVIEW implementation;
- configuration freeze: engineer able to identify hardware, firmware, application and cable revisions.

## 7.3 Agent-permitted work

An AI or documentation agent may:

- inventory files;
- classify documents;
- build registers;
- draft complete safety documents from supplied evidence;
- identify missing evidence;
- prepare test procedures;
- prepare gap entries;
- create traceability;
- compare revisions;
- populate placeholders;
- draft review records.

An agent shall not:

- claim to have inspected hardware;
- invent measurements;
- invent approval marks;
- infer unseen circuit ratings as facts;
- simulate signatures;
- accept residual risk;
- claim to have reviewed licensed standard text unless it was supplied;
- record a physical test as completed without the actual record.

---

# 8. TECHNICAL CONSTRUCTION FILE ARCHITECTURE

## 8.1 Top-level branches

The TCF shall contain the following controlled branches:

1. Governance and administration.
2. Boundary and baseline.
3. Interfaces.
4. Design definition.
5. Assurance and safety.
6. Verification and test.
7. Operations.
8. Generation-2 forward path.

## 8.2 Navigation hierarchy

The navigation order shall be:

1. TCF-INDEX-001 — Master Document List.
2. SYS-COMP-002 — Compliance Matrix.
3. SYS-SAF-010 — Safety Document.
4. Supporting risk, design, verification and operational evidence.

## 8.3 Evidence architecture

The TCF demonstrates completeness through three layers.

### Layer 1 — Inventory completeness

TCF-INDEX-001 records:

- every required document;
- revision;
- status;
- owner;
- class;
- location;
- E-state;
- approval status.

Missing documents remain visible as E4 or E5 entries.

### Layer 2 — Safety and compliance traceability

SYS-COMP-002 and SYS-VER-001 demonstrate:

`Clause → hazard → safety requirement → design control → evidence → verification → conclusion`

### Layer 3 — Design-data realism

SYS-DDR-001 records the required update to each existing design document.

The design is not redrawn solely for the TCF.

---

# 9. DOCUMENT CLASSES AND EVIDENCE STATES

## 9.1 Document classes

### Class F — Full author

Class F documents shall contain complete engineering analysis.

Evidence placeholders are permitted, but analytical placeholders are not.

A hazard row may state that a test record is missing. It may not omit:

- the hazard;
- the initiating cause;
- the hazardous situation;
- severity;
- controls;
- residual-risk logic.

### Class D — Delta managed

Class D documents already exist in the engineering data pack.

The TCF action is to record:

- current document and revision;
- required safety-related additions;
- missing attributes;
- cross-references to add;
- revision action;
- owner;
- priority;
- status.

A delta entry shall be specific.

Unacceptable:

> Review the schematic.

Acceptable:

> Add a complete mains-input chain showing inlet, switch, filtering, fuse type and rating, PE termination and segregation boundary; add drawing reference to SYS-SAF-003 Section 5.

### Class R — Reference

Class R material shall be indexed with:

- title;
- source;
- revision or issue;
- date;
- role;
- validity;
- relationship to the baseline.

Examples:

- manufacturer datasheets;
- agency certificates;
- calibration certificates;
- facility procedures;
- historical test records;
- contextual research papers.

## 9.2 Evidence states

| Code | State | Required treatment |
|---|---|---|
| E1 | Available — Verified | Reviewed and cited by document number and revision |
| E2 | Available — Unverified | Located but not yet assessed; temporary state |
| E3 | Partial | Some evidence exists, but a defined supplement or delta is required |
| E4 | Missing — Recoverable | Archive search or straightforward regeneration is expected |
| E5 | Missing — Create | New analysis, document, inspection or test is required |
| E6 | Not applicable | Applicability decision and rationale recorded |

E2 shall not remain at Gate 3.

## 9.3 Evidence placeholder

Use the following exact construction:

`[EVIDENCE REQUIRED — description of evidence — proposed source/test — GAP-xxx]`

Example:

`[EVIDENCE REQUIRED — protective-earth continuity measurement between mains plug earth and removable rack door — VER-EL-001 — GAP-003]`

---

# 10. PROGRAMME LIFECYCLE AND REVIEW GATES

## 10.1 Phases

| Phase | Title | Principal output |
|---|---|---|
| 0 | Initiation and framing | Approved strategy, claim and document-control framework |
| 1 | Boundary and classification | Signed boundary and intended-use definition |
| 2 | Baseline and evidence harvest | Frozen configuration and complete evidence inventory |
| 3 | Hazard and requirements analysis | Hazard register, FMEA and safety requirements |
| 4 | Clause mapping | Complete compliance matrix and classified gaps |
| 5 | Evidence formalisation and verification | Technical reviews and test records |
| 6 | Closure and operational uplift | Closed gaps, manuals and labels |
| 7 | TCF assembly and release | Safety Document, Statement and controlled release |
| 8 | Generation-2 extraction | Next-generation requirements and checklist |

## 10.2 Gates

| Gate | Decision |
|---|---|
| Gate 0 | Is the programme correctly framed and authorised? |
| Gate 1 | Is the assessed configuration fully defined and evidenced? |
| Gate 2 | Have hazards and safety requirements been comprehensively identified? |
| Gate 3 | Is the standards assessment complete and are all gaps classified? |
| Gate 4 | Is the required verification complete or formally dispositioned? |
| Gate 5 | Is the TCF suitable for controlled release? |

## 10.3 Gate records

Every gate record shall contain:

- date;
- attendees;
- inputs reviewed;
- findings;
- open actions;
- deviations;
- approval decision;
- conditions of approval;
- signatures.

A gate may be:

- approved;
- approved with actions;
- held;
- rejected.

---

# 11. PHASE 0 — INITIATION AND FRAMING

## 11.1 Objective

Establish the authorised scope, claim, standards set, ownership and control framework before detailed assessment begins.

## 11.2 Required inputs

- JOB-SPEC-61010-001;
- this manual;
- available system description;
- known data-pack index;
- answers or defaults for Q1–Q6;
- applicable organisational procedures.

## 11.3 Procedure

### Step 1 — Assign identity

Assign:

- system designation;
- TCF identifier;
- assessed-unit identifier;
- process owner;
- design authority;
- document controller.

### Step 2 — Confirm the claim

Record the approved wording in SYS-COMP-001.

Record prohibited wording.

### Step 3 — Establish the standards register

Record:

- exact edition;
- amendments;
- licence status;
- applicability decision;
- rationale;
- relationship to the system.

At minimum screen:

- IEC/BS EN 61010-1;
- IEC 61010-2-030;
- IEC 61010-2-201;
- IEC 61326 family as a separate EMC stream;
- organisational electrical-safety rules;
- facility interface rules.

### Step 4 — Confirm exclusions

Record:

- physical modification excluded;
- EMC testing excluded unless separately authorised;
- radiation-source safety excluded;
- third-party certification excluded;
- market marking excluded.

### Step 5 — Create the TCF skeleton

Create the folder structure in Appendix B.

Open:

- TCF-INDEX-001;
- DECISIONS.md;
- SYS-GAP-001;
- review-gate register.

### Step 6 — Record unresolved decisions

Unanswered Q1–Q6 shall be entered in DECISIONS.md with:

- default used;
- reason;
- risk if incorrect;
- decision owner;
- date by which confirmation is required.

## 11.4 Gate 0 exit criteria

Gate 0 may close only when:

- the claim is fixed or defaulted;
- the system and assessment have identifiers;
- the standards strategy is opened;
- the process owner and design authority are named;
- the document architecture is created;
- the boundary work is authorised;
- unresolved assumptions are visible.

---

# 12. PHASE 1 — BOUNDARY, INTENDED USE AND CLASSIFICATION

## 12.1 Objective

Define exactly what equipment is being assessed, how it is used and which external systems it depends upon.

## 12.2 Principal outputs

- SYS-SAF-001;
- classification block in SYS-COMP-001;
- boundary diagram;
- initial foreseeable-misuse register.

## 12.3 Boundary-development procedure

### Step 1 — Describe the system

Include:

- purpose;
- principal functions;
- supply;
- internal power architecture;
- signal classes;
- operating modes;
- beamline connection;
- control architecture;
- user access;
- service access.

### Step 2 — Define physical boundary

List all hardware inside and outside.

Do not use vague phrases such as “associated equipment”.

Name each category.

### Step 3 — Define functional boundary

For each function determine:

- where it begins;
- where it ends;
- what hardware performs it;
- whether it is safety-relevant;
- whether it relies on software;
- whether it relies on facility infrastructure.

### Step 4 — Define energy boundary

Identify all energy entering, leaving or stored in the system:

- 230 V AC;
- low-voltage DC;
- fault current;
- stored electrical energy;
- mechanical energy from movement;
- thermal energy;
- external backfeed;
- signals from third-party equipment.

### Step 5 — Define user boundary

Record user classes:

| User | Access | Minimum competence |
|---|---|---|
| Operator | External controls and software | Trained test engineer |
| Facility operator | Facility controls | Facility-authorised |
| Service engineer | Internal rack access | Electrically competent |
| Design engineer | Full design/configuration access | Discipline specialist |
| Configured user | Approved setup only | Trained for defined configuration |

### Step 6 — Define intended use

The intended-use statement shall include:

- test purpose;
- permitted DUT types;
- approved environment;
- approved cable sets;
- approved fixture;
- required user competence;
- permitted operating modes;
- restrictions during beam operation;
- restrictions on movement;
- restrictions on service access;
- restrictions on configuration changes.

### Step 7 — Define foreseeable misuse

The analysis shall consider at least:

- wrong mains lead;
- wrong fuse;
- operation with panels removed;
- live internal service;
- wrong cable connected;
- partial connector insertion;
- cable crushed or severed;
- unapproved cable extension;
- wrong cable revision;
- DUT connected while outputs are enabled;
- exposed fixture touched while powered;
- DUT latch-up;
- backfeed from external equipment;
- blocked ventilation;
- failed fan;
- rack moved while energised;
- rack moved while connected to beamline cables;
- excessive payload;
- wrong software configuration;
- stale status shown by the GUI;
- operator acknowledgement confused with event occurrence;
- facility interlock assumptions misunderstood.

### Step 8 — Answer boundary questions

Record explicit answers to:

1. Is the interface PCB supplied?
2. Are the propagation cables supplied?
3. Are the bias outputs energy-limited?
4. Can the fixture be touched while powered?
5. Can hazardous external equipment connect to the fixture?
6. Are only trained personnel permitted?
7. May the rack be moved while energised?
8. Is live service permitted?
9. Does software maintain any safety function?
10. Does the equipment connect to facility interlocks?

### Step 9 — Produce the boundary diagram

The diagram shall show:

- mains source;
- rack boundary;
- PE;
- internal supplies;
- control electronics;
- bias and protection;
- FPGA/LabVIEW boundary;
- propagation cable boundary;
- fixture/interface PCB;
- DUT boundary;
- facility boundary;
- signal and energy directions;
- ownership of each boundary.

## 12.4 Classification

Record, subject to confirmation against the licensed standard:

- indoor use;
- equipment mobility;
- intended environment;
- altitude;
- ambient temperature;
- humidity;
- pollution degree;
- overvoltage category;
- operator-access classification;
- service-access classification;
- wet-location exclusion;
- explosive-atmosphere exclusion;
- medical-use exclusion.

## 12.5 Phase 1 completion

The boundary shall be signed before detailed hazard analysis is finalised.

A later boundary change shall trigger formal impact assessment.

---

# 13. PHASE 2 — CONFIGURATION FREEZE AND EVIDENCE HARVEST

## 13.1 Objective

Define exactly which physical and digital configuration is being assessed and map every incoming file to a canonical location.

## 13.2 Principal outputs

- SYS-CFG-001;
- populated TCF-INDEX-001;
- SYS-DDR-001;
- initial SYS-CMP-001;
- SYS-CAL-001;
- photo-survey record;
- initial orphan-file register.

## 13.3 Baseline identification

Record:

- system name;
- configuration ID;
- serial number;
- rack revision;
- chassis configuration;
- instrument/module list;
- PCB revisions;
- fixture revision;
- cable-set revision;
- PSU models;
- fuse types and ratings;
- FPGA build;
- firmware release;
- LabVIEW version;
- executable version;
- configuration-file revision;
- operating-system image where relevant;
- external accessories;
- facility adaptor cables.

## 13.4 Physical survey

The physical survey is a `HUMAN-ACTION`.

Capture:

- front view;
- rear view;
- both sides;
- top and base where accessible;
- open-rack internal views;
- mains inlet and disconnect;
- fuse locations;
- mains distribution;
- PSU labels;
- MET;
- PE conductors;
- panel and door bonds;
- rack rails;
- cable segregation;
- ventilation;
- fan arrangement;
- connector panels;
- label locations;
- strain relief;
- fixture;
- fixture PCB;
- exposed conductors;
- cable routes;
- castors and brakes;
- structural fixings;
- hand modifications.

Each photo shall have:

- unique identifier;
- date;
- system configuration;
- view description;
- photographer;
- relationship to evidence or gap.

## 13.5 Configuration-trap sweep

Search specifically for:

- undocumented wire links;
- hand modifications;
- unused but energised wiring;
- substituted PSU;
- substituted fuse;
- different fuse values between units;
- unrecorded bonding straps;
- bonding through paint;
- missing star washers;
- changed connector pinouts;
- modified harnesses;
- prototype PCBs;
- obsolete software executables;
- mismatched FPGA and software versions;
- uncontrolled configuration files;
- customer-specific adaptations;
- facility-specific cable extensions.

Every unexplained physical difference shall become:

- a baseline note;
- a DDR item;
- a gap; or
- a variant exclusion.

## 13.6 File-by-file evidence harvest

For each source file:

1. Identify file type.
2. Identify actual format.
3. Record title and revision.
4. Record apparent owner.
5. Assign canonical home.
6. Assign Class F, D or R.
7. Assign E-state.
8. Identify duplicates.
9. Identify superseded versions.
10. Record whether it applies to the frozen baseline.
11. Record required action.
12. Record access or corruption issues.

No incoming item shall remain unmapped.

## 13.7 Orphan handling

An orphan is a file that:

- has no clear owner;
- has no clear system relationship;
- has conflicting identity;
- is unreadable;
- is duplicated without revision control.

Orphans shall be recorded in TCF-INDEX-001 until dispositioned as:

- applicable;
- superseded;
- reference only;
- unrelated;
- corrupt;
- duplicate;
- archive-only.

## 13.8 Design Data Update Register

SYS-DDR-001 shall contain:

| Field | Requirement |
|---|---|
| DDR ID | Unique row number |
| Existing document | Number and title |
| Current revision | As found |
| Discipline owner | Electrical/mechanical/software/etc. |
| Baseline applicability | Yes/no/partial |
| Missing safety view | Exact missing attribute |
| Required update | Concrete revision instruction |
| Cross-reference | Document requiring the evidence |
| Priority | High/medium/low |
| Owner | Named person or function |
| Status | Open/in progress/complete/deferred |
| Completion evidence | Revised document or approved disposition |

## 13.9 Gate 1 exit criteria

- assessed configuration uniquely identified;
- variants listed;
- source files inventoried;
- physical survey complete or formally planned;
- design documents mapped;
- E-states assigned;
- uncontrolled differences raised as gaps;
- software and firmware versions captured;
- cable-set baseline captured.

---

# 14. PHASE 3 — HAZARD ANALYSIS AND SAFETY REQUIREMENTS

## 14.1 Objective

Identify what can cause harm, evaluate the existing controls and convert the safety needs into explicit requirements.

## 14.2 Principal outputs

- SYS-RISK-001;
- SYS-RISK-002;
- SYS-REQ-002;
- populated SYS-GAP-001;
- Gate 2 review record.

## 14.3 Risk method

Use a consistent severity and probability model.

### Severity

| Rating | Meaning |
|---|---|
| S1 | No injury or minor inconvenience |
| S2 | Minor or reversible injury |
| S3 | Serious injury, significant burn, electric shock or localised fire |
| S4 | Fatality or multiple serious injuries |

### Probability

| Rating | Meaning |
|---|---|
| P1 | Very unlikely |
| P2 | Credible but uncommon |
| P3 | Reasonably foreseeable |
| P4 | Likely during the lifecycle |

The organisation may apply its own risk matrix, but the selected method shall be defined before scoring begins.

## 14.4 Hazard families

### Electrical shock

Consider:

- accessible mains;
- damaged mains cable;
- failed inlet;
- failed insulation;
- incorrect PE;
- unbonded panel;
- detached live conductor;
- exposed mains terminal;
- live service;
- PSU primary-to-secondary failure;
- hazardous backfeed;
- facility ground potential difference.

### Fire and thermal

Consider:

- incorrect fuse;
- PSU fault;
- overloaded branch;
- cable short;
- cable crush;
- failed current limit;
- DUT latch-up;
- shorted capacitor;
- failed fan;
- obstructed vent;
- excessive ambient temperature;
- inadequate conductor rating;
- high-resistance connection;
- repeated fault cycling.

### Output energy

Consider:

- high available current at low voltage;
- bias overvoltage;
- bias short;
- reverse polarity;
- stored charge;
- adjacent-pin short;
- short to screen;
- external-supply backfeed;
- cable heating;
- component rupture.

### Mechanical

Consider:

- trolley overturning;
- castor failure;
- brake failure;
- centre of gravity;
- drawer extension;
- movement over thresholds;
- excessive payload;
- unsecured panel;
- dropped component;
- sharp edge;
- pinch point;
- cable trip;
- fixture movement;
- fixture collapse;
- inadequate strain relief.

### Functional and control

Consider:

- wrong configuration;
- FPGA output stuck active;
- FPGA reset;
- LabVIEW crash;
- controller reboot;
- loss of communication;
- stale GUI status;
- loss of watchdog;
- unintended restart;
- incorrect bias threshold;
- event not detected;
- shutter status incorrect;
- fluence data incorrect;
- timestamp reset;
- buffer overflow;
- operator assumes output is off.

### Radiation-context electrical consequences

Consider:

- Single Event Latch-up;
- transient current demand;
- bias droop;
- shorted DUT;
- damaged interface PCB;
- erroneous state reporting;
- restricted access during a fault;
- delayed disconnection because of beamline controls;
- activated or contaminated hardware handled contrary to facility rules.

Radiation physics and personnel radiation protection remain facility-controlled unless explicitly included.

## 14.5 Hazard register format

Each hazard entry shall contain:

- hazard ID;
- hazard title;
- initiating cause;
- foreseeable sequence;
- hazardous situation;
- person or asset exposed;
- potential harm;
- initial severity;
- initial probability;
- existing inherent controls;
- existing protective controls;
- procedural controls;
- evidence;
- control dependency;
- single-fault vulnerability;
- required additional control;
- safety requirement;
- verification method;
- residual severity;
- residual probability;
- residual-risk decision;
- status;
- owner.

## 14.6 Protective Measures Register

Annex A of SYS-RISK-001 shall list each protective measure and classify it as:

- inherent by design;
- component-based protection;
- mechanical protection;
- monitoring/detection;
- procedural control;
- information for safety.

For each measure record:

- hazards controlled;
- evidence;
- dependency;
- failure mode;
- single-point nature;
- associated safety requirement;
- verification.

## 14.7 FMEA procedure

SYS-RISK-002 shall cover, at minimum:

- mains inlet and distribution;
- PE system;
- PSUs;
- DC rails;
- bias channels;
- monitoring;
- propagation cables;
- connectors;
- DUT interface;
- FPGA;
- LabVIEW;
- configuration files;
- event buffer;
- ventilation;
- trolley and fixture.

For each failure mode record:

- item;
- function;
- failure;
- cause;
- local effect;
- system effect;
- safety effect;
- detection;
- protection;
- evidence;
- action;
- relationship to hazard register.

## 14.8 Safety requirements

Each material hazard control shall become a requirement in SYS-REQ-002.

Requirement format:

`SYS-SAF-REQ-xxx — The system shall...`

Each requirement shall include:

- unique ID;
- requirement text;
- rationale;
- source hazard;
- source clause/topic;
- applicability;
- acceptance criteria;
- verification method;
- evidence;
- owner;
- status.

Requirements shall cover:

- mains protection;
- PE;
- insulation;
- accessible parts;
- output-energy limits;
- fault handling;
- cable protection;
- connector control;
- safe states;
- startup;
- shutdown;
- recovery;
- movement;
- stability;
- ventilation;
- labelling;
- instructions;
- service;
- configuration control.

## 14.9 Gate 2 exit criteria

- all hazard families reviewed;
- no blank analytical rows;
- obvious high-risk findings escalated;
- safety-significant FMEA findings linked;
- safety requirements traceable to hazards;
- evidence gaps entered in SYS-GAP-001;
- risk method approved.

---

# 15. PHASE 4 — CLAUSE MAPPING AND GAP ASSESSMENT

## 15.1 Objective

Assess every applicable requirement of the confirmed IEC 61010 standard set against the frozen configuration.

## 15.2 Principal outputs

- completed SYS-COMP-002;
- completed standards register;
- completed component ledger;
- classified gap register;
- verified or corrected provisional criteria.

## 15.3 Matrix creation

The matrix shall be created from the licensed standard, not from remembered clause numbers or internet summaries.

Use one row per assessable requirement or logically indivisible requirement group.

## 15.4 Required matrix fields

| Field | Content |
|---|---|
| Matrix row | Unique ID |
| Standard | Standard and edition |
| Clause | Confirmed clause reference |
| Requirement topic | Concise description |
| Applicability | Applicable/partial/not applicable |
| Applicability rationale | Specific reasoning |
| Hazard links | Hazard IDs |
| Safety-requirement links | Requirement IDs |
| Existing control | Current design or process |
| Evidence | Document number and revision |
| Evidence state | E1–E6 |
| Assessment status | Defined status vocabulary |
| Gap ID | Where applicable |
| Required action | Specific closure |
| Verification | Review/inspection/test/calculation |
| Owner | Responsible role |
| Closure evidence | Final evidence |
| Reviewer conclusion | Reasoned statement |
| Status | Open/closed/accepted |

## 15.5 Permitted assessment statuses

Use only:

- compliant by design;
- compliant by evidence;
- compliant by documented rationale;
- partially compliant;
- not evidenced;
- not applicable.

Do not use “pass” without identifying the evidence basis.

## 15.6 Applicability decisions

A not-applicable decision shall state why the requirement does not apply to:

- the product type;
- the boundary;
- the installation;
- the energy level;
- the user-access category;
- the operating mode;
- the environmental classification.

“Not relevant” is not an adequate rationale.

## 15.7 Particular-standard screening

### IEC 61010-2-030

Determine whether the propagated bias/sense or other external connections meet the applicable definition of testing or measuring circuits connected to external circuits.

Record:

- circuits assessed;
- external connection;
- maximum normal voltage;
- credible external voltage;
- source impedance;
- protection;
- access;
- applicability conclusion;
- effect on the matrix.

### IEC 61010-2-201

Record whether the PXI/FPGA/LabVIEW architecture is:

- in scope;
- analogous only;
- awareness only;
- excluded with rationale.

Do not silently expand the claim.

## 15.8 Component ledger

SYS-CMP-001 shall include safety-significant components in the mains or hazardous-energy path.

Record:

- reference;
- function;
- manufacturer;
- part number;
- rating;
- application stress;
- approval marks;
- applicable certificate;
- conditions of acceptability;
- baseline location;
- evidence location;
- substitution control.

Candidate categories:

- mains inlet;
- filters;
- switches;
- fuses;
- circuit breakers;
- terminal blocks;
- internal mains wiring;
- AC/DC PSUs;
- insulation barriers;
- protective covers;
- PE hardware;
- connectors carrying material energy;
- safety-critical cable assemblies.

An approval mark shall not be treated as evidence of correct application without checking:

- rating;
- temperature;
- installation;
- isolation class;
- fuse requirements;
- mounting;
- conditions of acceptability.

## 15.9 Gap classification

Every deficient matrix row shall be classified as:

- documentation;
- verification;
- design;
- process;
- claim.

Several types may apply, but one shall be marked primary.

## 15.10 Gate 3 exit criteria

- every clause assessed;
- every not-applicable decision justified;
- all clause references confirmed;
- E2 evidence resolved;
- evidence links use number and revision;
- gaps classified;
- verification needs identified;
- provisional numeric criteria confirmed, corrected or retained with explicit status.

---

# 16. PHASE 5 — EVIDENCE FORMALISATION AND VERIFICATION

## 16.1 Objective

Produce the detailed technical analyses and objective evidence required to support the matrix and risk controls.

## 16.2 Required technical reviews

The phase shall produce:

- SYS-SAF-003;
- SYS-SAF-004;
- SYS-MECH-001;
- SYS-SW-001;
- SYS-EMC-001;
- completed ICD uplifts;
- SYS-VER-001;
- required SYS-VER-1xx reports.

## 16.3 Evidence hierarchy

Use the strongest proportionate evidence available:

1. direct review of controlled design information;
2. inspection of the baseline hardware;
3. non-destructive bench test;
4. engineering calculation;
5. historical evidence validated against the baseline;
6. supplier certification;
7. operating history as supplementary evidence;
8. residual-risk acceptance.

Operating history alone shall not prove a safety requirement where direct evidence is reasonably available.

## 16.4 Design-review evidence

A design review shall identify:

- source documents;
- revisions;
- reviewer;
- date;
- questions considered;
- assumptions;
- calculation method;
- findings;
- conclusion;
- open gaps.

## 16.5 Inspection evidence

An inspection record shall identify:

- exact unit;
- date;
- inspector;
- access condition;
- photographs;
- checklist;
- deviations;
- conclusion;
- raised gaps.

## 16.6 Test evidence

Each test shall follow Section 25.

All physical tests are `HUMAN-ACTION`.

## 16.7 Deferred testing

A test may be deferred only when the record states:

- why it cannot be performed;
- risk of not performing it;
- interim evidence;
- planned date or trigger;
- owner;
- effect on the compliance claim;
- required approval.

Deferred tests remain open gaps unless a different closure route is formally accepted.

## 16.8 Gate 4 exit criteria

- planned reviews completed;
- planned inspections completed;
- tests complete or dispositioned;
- failures entered as gaps;
- test deviations assessed;
- manuals updated with relevant findings;
- technical reviews linked to the matrix;
- no result fabricated or inferred.

---

# 17. PHASE 6 — GAP CLOSURE, MANUALS AND OPERATIONAL CONTROLS

## 17.1 Objective

Close all identified gaps through permitted routes and ensure the operational documentation reflects the assessed safety position.

## 17.2 Closure order

Use this order of preference:

1. bench verification;
2. engineering analysis;
3. residual-risk acceptance.

## 17.3 Documentation closure

A documentation gap closes when:

- the required controlled document or delta is complete;
- it has been reviewed;
- references resolve;
- revision is recorded;
- the corresponding matrix and gap rows are updated.

## 17.4 Verification closure

A verification gap closes when:

- the test or inspection is complete;
- equipment and calibration are recorded;
- acceptance criteria were defined before conclusion;
- result and deviations are recorded;
- reviewer approves the report;
- traceability is updated.

## 17.5 Engineering-analysis closure

An analysis shall contain:

- issue;
- evidence;
- assumptions;
- method;
- worst-case conditions;
- margins;
- uncertainty;
- conclusion;
- reviewer approval.

## 17.6 Residual-risk closure

Residual-risk acceptance shall contain:

- hazard;
- gap;
- reason stronger closure was unavailable or disproportionate;
- current controls;
- affected users and modes;
- restrictions;
- residual risk;
- review date or trigger;
- approving authority;
- Generation-2 action.

Generic statements such as “system has operated for years without incident” are insufficient on their own.

## 17.7 Operational-document uplift

Complete:

- SYS-MAN-001;
- SYS-MAN-002;
- SYS-LAB-001.

The manuals shall match:

- the frozen baseline;
- approved cable sets;
- approved fixture;
- actual software;
- defined safe states;
- restrictions and residual risks.

## 17.8 Phase 6 exit criteria

- no gap lacks a closure route;
- no unclosable design gap is silently accepted;
- residual-risk decisions are signed;
- manuals and labels reflect findings;
- Generation-2 actions are tagged;
- claim wording remains within the approved level.

---

# 18. PHASE 7 — TCF ASSEMBLY, SAFETY DOCUMENT AND RELEASE

## 18.1 Objective

Assemble the final controlled TCF and issue the apex Safety Document and internal Statement of Compliance.

## 18.2 Safety Document structure

SYS-SAF-010 shall contain:

1. Introduction and scope.
2. Applicable standards and classification.
3. System description.
4. Hazard-based risk assessment conclusions.
5. Protection-architecture summary.
6. Compliance Matrix as Annex A.
7. Mechanical and enclosure findings.
8. Residual-risk and concession log.
9. Statement of Compliance.
10. Referenced documents.
11. Revision history.

## 18.3 Safety Document rules

The Safety Document shall:

- be readable independently;
- state the assessed configuration;
- state the exact claim;
- describe the boundary;
- summarise rather than duplicate evidence;
- cite documents by number and revision;
- identify open limitations;
- identify conditions of use;
- contain signed residual-risk decisions;
- distinguish current evidence from future Generation-2 actions.

## 18.4 Compliance summary

SYS-COMP-003 shall be management-facing and contain:

- system identity;
- scope;
- standards;
- claim level;
- boundary;
- risk summary;
- electrical review summary;
- mechanical review summary;
- software review summary;
- verification summary;
- open items;
- residual risks;
- restrictions;
- Statement of Compliance;
- approvals.

## 18.5 TCF release checks

Before release:

- TCF-INDEX-001 shall be complete;
- all document links shall resolve;
- all revisions shall match citations;
- all mandatory approvals shall be present;
- superseded documents shall be clearly marked;
- open gaps shall be visible;
- residual risks shall be approved;
- exact baseline shall be named;
- no E2 items shall remain;
- no uncontrolled “final” files shall exist outside the released baseline.

## 18.6 Gate 5 decision

Gate 5 approval confirms that the TCF supports the stated internal assurance position.

It does not create third-party certification.

---

# 19. PHASE 8 — GENERATION-2 REQUIREMENTS EXTRACTION

## 19.1 Objective

Convert every material retrospective finding into a prospective requirement or design-review action.

## 19.2 Sources

Extract requirements from:

- hazards;
- FMEA;
- compliance gaps;
- verification failures;
- residual risks;
- manual restrictions;
- configuration traps;
- obsolete design controls;
- evidence weaknesses;
- software/logging limitations;
- cable and fixture limitations.

## 19.3 Requirement categories

Each Generation-2 requirement shall be tagged:

- mandatory;
- recommended;
- legacy carryover;
- evidence/process;
- data integrity;
- interface;
- verification;
- architecture.

## 19.4 Review-gate mapping

Map requirements to:

- System Requirements Review;
- Preliminary Design Review;
- Critical Design Review;
- first-use release.

## 19.5 Generation-2 principle

The Generation-2 Safety Document shall emerge from normal design reviews.

It shall not be reconstructed after design completion.

---

# 20. DOCUMENT-SPECIFIC PRODUCTION INSTRUCTIONS

## 20.1 TCF-INDEX-001 — Master Document List

Shall include:

- document number;
- title;
- class;
- revision;
- status;
- owner;
- approver;
- baseline applicability;
- E-state;
- physical/electronic location;
- supersession;
- gap relationship;
- notes.

Open first and close last.

## 20.2 SYS-COMP-001 — Standards and Compliance Strategy

Shall include:

- assessment purpose;
- claim;
- standards and editions;
- applicability decisions;
- exclusions;
- classification;
- environment;
- market-status context;
- review authorities;
- change-control rule.

## 20.3 SYS-SAF-001 — Boundary and Intended Use

Shall contain:

- system description;
- inside/outside lists;
- boundary diagram;
- user classes;
- intended use;
- environments;
- operating modes;
- access types;
- foreseeable misuse;
- interface dependencies;
- boundary decisions.

## 20.4 SYS-CFG-001 — Baseline

Shall contain:

- unique configuration;
- revision table;
- hardware list;
- software/firmware list;
- cable and fixture list;
- source artefact index;
- photograph index;
- variant statement;
- configuration traps;
- unresolved differences.

## 20.5 SYS-DDR-001 — Design Data Update Register

Shall be the sole controlling list of required design-document changes.

It shall not direct unnecessary redraw.

## 20.6 SYS-RISK-001 — Hazard Register

Shall be complete across all identified hazard categories.

Evidence may be missing. Analysis may not be missing.

## 20.7 SYS-RISK-002 — FMEA

Shall be one living register covering safety-significant failure modes.

## 20.8 SYS-REQ-002 — Safety Requirements

Shall provide bidirectional traceability with:

- hazards;
- clauses;
- design controls;
- verification.

## 20.9 SYS-SAF-003 — Electrical Safety Architecture Review

Shall include:

1. Mains architecture.
2. Disconnect and protection.
3. PE and bonding.
4. Internal distribution.
5. PSU and isolation evidence.
6. Power tree.
7. accessible-circuit schedule.
8. branch protection.
9. cable-output energy.
10. fixture electrical safety.
11. abnormal conditions.
12. evidence and gaps.

## 20.10 SYS-SAF-004 — Normal and Single-Fault Analysis

Shall assess credible faults in:

- mains;
- PE;
- power supplies;
- outputs;
- cables;
- connectors;
- controls;
- software;
- ventilation;
- mechanical structure.

## 20.11 SYS-MECH-001 — Mechanical Review

Shall cover:

- stability;
- movement;
- payload;
- castors;
- brakes;
- handles;
- enclosure;
- panels;
- sharp edges;
- fixture;
- cable loads;
- transport restrictions.

## 20.12 SYS-SW-001 — Software and Firmware Safety Review

Shall cover:

- functional boundary;
- safety classification;
- safe state;
- failure modes;
- startup;
- reset;
- communication loss;
- wrong configuration;
- stale indication;
- timebase;
- circular buffer;
- event correlation;
- acknowledgement timing;
- overflow behaviour.

## 20.13 SYS-CMP-001 — Component Ledger

Shall identify every safety-significant component and demonstrate correct application.

## 20.14 SYS-EMC-001 — Position Statement

Unless scope changes, limit this document to:

- EMC is a separate stream;
- cable-screen and bonding decisions overlapping safety;
- bought-in equipment status;
- known operating-history observations;
- Generation-2 EMC action.

No present-system EMC compliance claim shall be inferred.

## 20.15 SYS-VER-001 — Verification Plan

Shall map:

- requirement;
- hazard;
- matrix row;
- verification method;
- configuration;
- acceptance criteria;
- report;
- conclusion.

## 20.16 SYS-MAN-001 — Operator Manual

Shall include:

1. System overview.
2. Intended use.
3. User competence.
4. Boundary.
5. Hazards.
6. Approved configuration.
7. Setup.
8. Cable connection.
9. Fixture connection.
10. Pre-use check.
11. Power-up.
12. Software startup.
13. Test configuration.
14. Bias enabling.
15. Beam-run procedure.
16. Monitoring.
17. Faults.
18. Safe shutdown.
19. Emergency disconnection.
20. Cleaning.
21. Storage.
22. Accessories.
23. Prohibited use.
24. Support and service.

## 20.17 SYS-MAN-002 — Service Manual

Shall include:

- competence;
- isolation;
- stored energy;
- access;
- mains inspection;
- PE inspection;
- fuse replacement;
- PSU replacement;
- cable inspection;
- fan/filter maintenance;
- firmware/software updates;
- post-service tests;
- service records;
- configuration control.

## 20.18 SYS-LAB-001 — Label Schedule

Shall identify:

- text or symbol;
- purpose;
- location;
- size;
- material;
- durability;
- drawing;
- photograph;
- inspection status.

## 20.19 SYS-GAP-001 — Gap Register

Shall remain live from Phase 3 to release and thereafter for controlled open actions.

## 20.20 SYS-NG-REQ-001 and SYS-NG-001

Shall convert findings into prospective requirements and review checklists.

---

# 21. ELECTRICAL SAFETY ASSESSMENT PROCEDURE

## 21.1 Mains input

Review:

- inlet type and rating;
- rated voltage and frequency;
- fuse location;
- fuse rating;
- fuse type;
- breaking capacity;
- switching arrangement;
- live/neutral assumptions;
- disconnect accessibility;
- strain relief;
- cable retention;
- internal conductor rating;
- terminal protection;
- segregation;
- filter leakage implications;
- emergency disconnection.

## 21.2 Protective earth

Review:

- PE conductor from inlet;
- MET;
- rack frame;
- removable panels;
- doors;
- rack rails;
- PSU chassis;
- connector shells;
- bonding through coatings;
- washers and fasteners;
- dedicated PE fasteners;
- loosened-fastener risk;
- safety-earth versus screen-earth functions.

Record the complete PE path graphically.

## 21.3 Internal distribution

For each rail record:

| Rail | Nominal value | Maximum available current | Protection | Loads | Accessible | Fault response |
|---|---:|---:|---|---|---|---|

Review:

- branch protection;
- conductor rating;
- terminal rating;
- ferrules and crimps;
- cable routing;
- derating;
- short-circuit behaviour;
- overvoltage behaviour;
- PSU failure-high behaviour;
- inrush;
- stored energy.

## 21.4 Isolation

Identify:

- where mains ends;
- where isolated secondary begins;
- PSU isolation claim;
- applicable certificate;
- conditions of acceptability;
- physical segregation;
- barriers;
- clearance and creepage;
- accessible low-voltage outputs;
- potential external backfeed.

## 21.5 Accessible circuits

Create a schedule containing:

| Connector | Location | Signal | Voltage | Available current | Access | Protection | Safe state |
|---|---|---|---:|---:|---|---|---|

For each connection answer:

1. Can it be touched?
2. Can it be misconnected?
3. Can it be partially inserted?
4. Can hazardous external energy be introduced?
5. Can it overheat under short circuit?
6. Is it labelled?
7. Is it keyed?
8. Is the cable controlled?
9. Is screen termination intentional?
10. Is disconnection behaviour defined?

## 21.6 Single faults

At minimum assess:

- live-to-chassis short;
- PE open;
- neutral open;
- detached mains conductor;
- fuse bypass;
- wrong fuse;
- failed mains switch;
- PSU primary-secondary fault;
- PSU output overvoltage;
- PSU output short;
- DC branch short;
- bias stuck active;
- current-limit failure;
- cable short;
- cable crush;
- adjacent-pin short;
- reverse connection;
- external backfeed;
- fan failure;
- blocked vent.

## 21.7 Software-control limitation

Software shall not be assumed to provide the sole control against fundamental electric shock, fire or hazardous energy.

Prefer:

- isolation;
- PE;
- fusing;
- current limiting;
- physical segregation;
- barriers;
- keyed connectors;
- hardware enables;
- watchdogs;
- fail-safe defaults.

---

# 22. PROPAGATION CABLE AND DUT-INTERFACE ASSESSMENT

## 22.1 Cabling ICD

SYS-ICD-002 shall cover all five signal classes in one controlled document.

The interconnect schedule shall be an annex.

## 22.2 Required cable data

For every cable or approved set record:

- identifier;
- revision;
- function;
- signal class;
- cable type;
- conductor details;
- length;
- maximum approved length;
- extension policy;
- connector;
- pinout;
- keying;
- shielding;
- screen termination;
- voltage;
- current;
- fault current;
- insulation rating;
- bend radius;
- strain relief;
- route;
- radiation suitability where required;
- approved applications;
- prohibited applications.

## 22.3 Cable-fault assessment

Assess:

- open conductor;
- shorted conductor;
- short to screen;
- adjacent-pin short;
- connector reversal;
- partial insertion;
- crushed cable;
- severed cable;
- damaged insulation;
- unapproved extension;
- wrong revision;
- cross-connection;
- ground-potential difference;
- cable disconnected under power.

## 22.4 Fixture assessment

Record:

- maximum voltage;
- maximum current;
- current limiting;
- exposed conductors;
- touch access;
- connector protection;
- fixture bonding or floating rationale;
- mechanical security;
- strain relief;
- permitted setup condition;
- permitted beamline access;
- handling after exposure;
- DUT-failure effects;
- radiation-induced short or latch-up response.

## 22.5 Cable-length control

The approved maximum shall be the longest validated baseline set unless a separate analysis or test establishes a greater value.

Extensions shall be prohibited until validated.

---

# 23. MECHANICAL AND TROLLEY SAFETY ASSESSMENT

## 23.1 Trolley review

Review:

- total mass;
- mass distribution;
- centre of gravity;
- high-mounted equipment;
- drawer extension;
- castor rating;
- castor attachment;
- brake effectiveness;
- handle provision;
- thresholds and uneven floors;
- maximum payload;
- transport configuration;
- cable connection during movement;
- panel security;
- rack-mount fasteners;
- ventilation openings;
- sharp edges;
- pinch points.

## 23.2 Stability verification

Mechanical acceptance criteria shall be confirmed against the licensed standard.

Where provisional criteria are used, mark them accordingly.

Test or analyse:

- adverse tilt;
- horizontal push;
- fully loaded state;
- least favourable castor orientation;
- unlocked and locked conditions as relevant;
- extended drawers or modules;
- additional fixture or cable loads.

## 23.3 Fixture mechanics

Review:

- beamline mounting;
- locking;
- strain relief;
- loose parts;
- sharp pins;
- standoff materials;
- insulating parts;
- conductive exposed parts;
- accidental contact;
- service access;
- post-exposure handling.

## 23.4 Movement restriction

Unless specifically justified:

> The trolley shall not be moved while connected to beamline propagation cables.

This restriction shall appear in:

- risk register;
- safety requirement;
- operator manual;
- label schedule;
- verification checklist.

---

# 24. SOFTWARE, FPGA, LABVIEW AND LOGGING ASSESSMENT

## 24.1 Functional inventory

Document:

- LabVIEW role;
- PXI controller role;
- FPGA role;
- hardware timebase;
- trigger processing;
- bias enable;
- bias monitoring;
- current-threshold logic;
- dwell timers;
- SEL response;
- monitors-armed gating;
- shutter input;
- fluence input;
- circular buffer;
- event record;
- GUI;
- configuration files;
- watchdogs;
- remote control.

## 24.2 Safety classification

Classify each function as:

- safety relevant;
- safety supporting;
- test-validity relevant;
- diagnostic;
- convenience only.

## 24.3 Defined safe state

The default safe-state requirement is:

- bias outputs disabled or limited to a defined safe value;
- triggers inactive unless explicitly justified;
- fixture outputs in a known state;
- test sequence stopped;
- operator notified;
- restart requiring deliberate action;
- logs showing the interruption clearly.

Any deviation shall be justified.

## 24.4 Failure modes

Assess:

- LabVIEW crash;
- frozen GUI;
- stale status;
- PXI reboot;
- FPGA reset;
- FPGA output stuck;
- communication loss;
- watchdog loss;
- disk full;
- buffer overflow;
- counter wrap;
- lost timebase;
- wrong configuration;
- wrong cable-delay parameter;
- wrong threshold profile;
- late acknowledgement;
- power interruption;
- power restoration.

## 24.5 Logging integrity

Document:

- hardware timestamps;
- software timestamps;
- clock source;
- resolution;
- run start;
- definition of `t0`;
- event window;
- pre-event history;
- post-event capture;
- buffer depth;
- buffer wrap;
- write-record timing;
- occurrence time;
- acknowledgement time;
- shutter correlation;
- fluence correlation;
- bias-event correlation;
- image-data correlation;
- invalid-data flagging.

## 24.6 Safety versus scientific validity

A loss of logging may invalidate the experiment without making the equipment electrically unsafe.

The review shall distinguish:

- personnel/equipment safety consequences;
- DUT-protection consequences;
- scientific-validity consequences;
- incident-reconstruction consequences.

---

# 25. VERIFICATION AND TEST MANAGEMENT

## 25.1 Verification methods

Use:

- design review;
- inspection;
- calculation;
- bench test;
- historical evidence;
- external assessment.

## 25.2 Minimum verification considerations

### Electrical

- PE continuity;
- mains wiring inspection;
- fuse verification;
- isolation review;
- accessible voltage;
- accessible current or energy;
- internal wiring rating;
- output short circuit;
- cable fault;
- power-up safe state;
- power-down safe state;
- power-loss recovery;
- leakage or touch current where applicable;
- insulation or withstand where appropriate and safe.

### Thermal

- representative maximum load;
- enclosed operation;
- fan operation;
- blocked-vent scenario;
- PSU margin;
- cable heating under fault;
- DUT latch-up condition.

### Mechanical

- stability;
- castors;
- brakes;
- panels;
- strain relief;
- fixture;
- sharp edges;
- movement warnings.

### Functional

- outputs at startup;
- outputs after software crash;
- outputs after FPGA reset;
- communication loss;
- watchdog;
- wrong configuration;
- interrupted-run indication;
- no unintended automatic restart.

### Radiation-test functions

- bias-current event capture;
- shutter-state capture;
- fluence count;
- timestamp alignment;
- event acknowledgement;
- buffer overflow;
- communication loss;
- SEL detection and response.

## 25.3 Test record

Every test report shall contain:

- test ID;
- title;
- purpose;
- requirement links;
- hazard links;
- matrix links;
- configuration;
- hardware revision;
- software revision;
- operator;
- date;
- equipment;
- calibration status;
- preconditions;
- method;
- acceptance criteria;
- raw results;
- conclusion;
- deviations;
- photographs;
- reviewer;
- approval.

## 25.4 Acceptance criteria

Acceptance criteria shall be defined before results are interpreted.

They may be based on:

- confirmed standard limits;
- controlled system requirements;
- supplier ratings;
- approved engineering limits;
- explicit risk controls.

## 25.5 Failed tests

A failed test shall:

- remain recorded;
- create or update a gap;
- trigger risk review;
- trigger impact review;
- not be deleted or replaced by an undocumented retest.

A retest shall reference the original failure.

## 25.6 Example: output short-circuit test

**Test ID:** VER-DC-004  
**Purpose:** Verify that a shorted propagated output does not create hazardous voltage, fire, insulation damage or uncontrolled heating.

Minimum observations:

- fault current;
- output voltage;
- protective action;
- time to action;
- cable temperature;
- connector condition;
- PSU condition;
- indication;
- logging;
- recovery;
- reset requirement.

## 25.7 Example: power interruption and restoration

**Test ID:** VER-FUNC-006  
**Purpose:** Verify that the system does not resume biasing or test execution in an unintended state after power restoration.

Observe:

- bias outputs;
- trigger outputs;
- fixture outputs;
- FPGA state;
- LabVIEW state;
- active run;
- operator indication;
- event record;
- restart behaviour.

---

# 26. GAP, CONCESSION AND RESIDUAL-RISK MANAGEMENT

## 26.1 Gap types

| Type | Meaning |
|---|---|
| Documentation | Control may exist but evidence is missing or inadequate |
| Verification | Objective confirmation is absent |
| Design | Existing design may not provide an adequate control |
| Process | Build, service, operation or change control is weak |
| Claim | Wording exceeds the evidence |

## 26.2 Gap-register fields

- gap ID;
- source;
- description;
- affected area;
- type;
- hazard;
- clause;
- risk;
- existing control;
- required closure;
- proposed route;
- owner;
- due date;
- HUMAN-ACTION status;
- NEXT-GEN tag;
- closure evidence;
- residual risk;
- approval;
- status.

## 26.3 Gap status

Use:

- open;
- assigned;
- in progress;
- awaiting human action;
- awaiting evidence;
- ready for review;
- closed;
- accepted residual risk;
- escalated;
- transferred to Generation 2.

## 26.4 Significant finding

A finding is significant where:

- credible serious harm remains;
- a fundamental protective measure is absent;
- compliance cannot be supported without hardware change;
- the stated boundary is invalid;
- the actual baseline cannot be identified;
- safety relies unknowingly on software or facility action;
- test evidence contradicts the design claim;
- configuration drift prevents a representative claim.

Significant findings require design-authority review.

## 26.5 Concession control

A concession shall not be used to avoid completing reasonably achievable verification.

It shall have:

- defined scope;
- affected serial/configuration;
- justification;
- restrictions;
- expiry or review trigger;
- approver;
- Generation-2 disposition.

---

# 27. TRACEABILITY AND CROSS-REFERENCE CONTROL

## 27.1 Required traceability

The following links shall exist:

`Hazard ↔ safety requirement ↔ clause ↔ design evidence ↔ verification ↔ gap ↔ conclusion`

## 27.2 Citation format

Evidence citations shall include:

- document number;
- revision;
- section/sheet;
- item or figure where useful.

Example:

`SYS-DD-006 Rev C, Section 4.3, Figure 7`

## 27.3 Broken-reference review

Before each gate:

- export the document register;
- check cited revisions;
- identify obsolete links;
- verify gap IDs;
- verify requirement IDs;
- verify matrix rows;
- verify test-report references.

## 27.4 No duplicate conclusions

A safety conclusion shall have one authoritative home.

Other documents shall reference it.

---

# 28. DOCUMENT CONTROL AND CONFIGURATION MANAGEMENT

## 28.1 Required metadata

Every controlled document shall contain:

- title;
- number;
- system;
- revision;
- status;
- author;
- owner;
- approver;
- date;
- baseline applicability;
- revision history.

## 28.2 Status vocabulary

Use:

- draft;
- in review;
- approved;
- released;
- superseded;
- withdrawn;
- archive reference.

## 28.3 File naming

Recommended format:

`<Document-ID>_<Short-Title>_Rev-<Revision>.<extension>`

Example:

`SYS-SAF-003_Electrical-Safety-Architecture-Review_Rev-A.docx`

## 28.4 Working files

Working material shall be kept separate from released evidence.

Do not place uncontrolled drafts in the released TCF folder.

## 28.5 Baseline changes

A change after Gate 1 shall trigger assessment of:

- boundary;
- hazard register;
- FMEA;
- safety requirements;
- clause matrix;
- verification;
- manuals;
- Statement of Compliance.

## 28.6 Decision log

DECISIONS.md shall record:

- decision ID;
- date;
- issue;
- options;
- decision;
- rationale;
- evidence;
- approver;
- affected documents;
- review trigger.

---

# 29. QUALITY ASSURANCE AND PROHIBITED PRACTICES

## 29.1 Fabrication ban

Do not invent:

- values;
- test results;
- dates;
- signatures;
- serial numbers;
- revisions;
- part numbers;
- certification;
- clause text;
- photographs;
- ratings;
- dimensions.

## 29.2 Analytical completeness

Class F documents shall not contain placeholders for:

- hazard description;
- applicability logic;
- analysis method;
- risk reasoning;
- required action;
- conclusion basis.

## 29.3 Design-data control

Do not redraw or rewrite mature design data without a specific approved need.

Use the DDR.

## 29.4 Numeric assumptions

Do not convert provisional values into requirements without confirming their basis.

## 29.5 Historical evidence

Historical evidence shall be checked for:

- matching configuration;
- matching serial number;
- matching revision;
- suitable method;
- calibration validity;
- acceptance criteria;
- completeness;
- continued relevance.

## 29.6 Operating history

Operating history may support confidence but shall not replace required direct evidence without an approved rationale.

## 29.7 Review quality

Reviewers shall challenge:

- unsupported claims;
- incomplete boundaries;
- unjustified not-applicable decisions;
- hidden dependence on procedures;
- hidden dependence on software;
- generic residual-risk statements;
- ambiguous revisions;
- unverified supplier claims.

---

# 30. PROJECT PLANNING AND EXECUTION PRIORITIES

## 30.1 Indicative effort

The programme is expected to require approximately 25–43 engineer-day equivalents, depending on:

- configuration drift;
- data-pack quality;
- standards screening;
- archive quality;
- test access;
- number of variants;
- number of significant findings.

## 30.2 Human-dependent work

Likely human work includes:

- photo survey;
- physical configuration inspection;
- PE test;
- cable-fault tests;
- output-short tests;
- thermal tests;
- stability checks;
- gate reviews;
- residual-risk approvals.

## 30.3 Critical path

The likely critical path is:

1. boundary and baseline;
2. hazard analysis;
3. clause matrix;
4. test definition;
5. physical access;
6. verification;
7. gap closure;
8. final Safety Document.

## 30.4 Priority rule

Prioritise work in this order:

1. potentially high-risk design findings;
2. scope and baseline uncertainty;
3. missing safety controls;
4. missing verification;
5. missing safety documentation;
6. operational manual and label gaps;
7. formatting and presentational improvements.

## 30.5 Stop conditions

Pause and escalate if:

- the physical baseline cannot be identified;
- dangerous voltage is found outside the expected boundary;
- PE integrity is doubtful;
- an unfused/high-energy external cable is found;
- software is the only protection against a serious hazard;
- the facility interlock boundary differs materially from the assumption;
- evidence indicates a credible unsafe single fault;
- the proposed claim exceeds available evidence.

---

# 31. COMPLETION CRITERIA

The programme is complete only when:

1. Every canonical document has an owner, status, revision and E-state.
2. Every applicable clause has an assessment.
3. Every not-applicable clause has a rationale.
4. Every hazard has been analysed.
5. Every safety requirement traces to a hazard and verification.
6. Every gap has a recorded disposition.
7. Every residual risk is authorised.
8. Every Class D document has a concrete DDR disposition.
9. Every physical test has a genuine record.
10. The assessed configuration is frozen.
11. The operator and service manuals match the baseline.
12. The label schedule is complete.
13. The Safety Document is approved.
14. The Statement of Compliance uses approved wording.
15. Generation-2 requirements have been extracted.
16. Gate 5 has formally approved release.

---

# APPENDIX A — CANONICAL DOCUMENT REGISTER

## A.1 Governance

| ID | Title | Class |
|---|---|---|
| TCF-INDEX-001 | Master Document List / TCF Index | F |
| SYS-COMP-001 | Applicable Standards Register and Compliance Strategy | F |
| SYS-COMP-002 | IEC 61010 Applicability and Gap Matrix | F |
| SYS-COMP-003 | Compliance Summary and Statement of Compliance | F |
| SYS-REQ-001 | System Requirements / Specification | D |
| SYS-DES-001 | Architecture / Design Description | D |

## A.2 Boundary and baseline

| ID | Title | Class |
|---|---|---|
| SYS-SAF-001 | Equipment Boundary and Intended Use Statement | F |
| SYS-CFG-001 | Current System Design Baseline | F |

## A.3 Interfaces

| ID | Title | Class |
|---|---|---|
| SYS-ICD-001 | Facility Interface ICD | D/F-lite |
| SYS-ICD-002 | Cabling ICD | D/F |
| SYS-ICD-003 | DUT Fixture ICD | D/F-lite |

## A.4 Design definition

| ID | Title | Class |
|---|---|---|
| SYS-DDR-001 | Design Data Update Register | F register |
| SYS-DD-001 | Electrical Schematics and Calculations | D |
| SYS-DD-002 | Assembly and Fabrication Drawings | D |
| SYS-DD-003 | PCB Design Package | D |
| SYS-DD-004 | FPGA Design Description | D |
| SYS-DD-005 | LabVIEW Design Description | D |
| SYS-DD-006 | Protection Architecture Description | D |
| SYS-DD-007 | Bill of Materials | D |

## A.5 Assurance and safety

| ID | Title | Class |
|---|---|---|
| SYS-RISK-001 | Hazard-Based Risk Assessment and Register | F |
| SYS-RISK-002 | FMEA Register | F |
| SYS-REQ-002 | Safety Requirement Specification | F |
| SYS-SAF-003 | Electrical Safety Architecture Review | F |
| SYS-SAF-004 | Normal and Single-Fault Analysis | F |
| SYS-MECH-001 | Mechanical and Trolley Safety Review | F |
| SYS-SW-001 | Software and Firmware Safety Review | F |
| SYS-CMP-001 | Safety-Critical Component Ledger | F/R |
| SYS-EMC-001 | EMC and Signal-Integrity Position Statement | F-stub |
| SYS-GAP-001 | Gap and Residual-Risk Register | F |
| SYS-SAF-010 | Safety Document | F |

## A.6 Verification and test

| ID | Title | Class |
|---|---|---|
| SYS-VER-001 | Retrospective Safety Verification Plan and V&V Matrix | F |
| SYS-VER-1xx | Individual Test Reports | F/R |
| SYS-CAL-001 | Calibration Records Index | R |

## A.7 Operations

| ID | Title | Class |
|---|---|---|
| SYS-MAN-001 | Operator and Safety Manual | F |
| SYS-MAN-002 | Service and Maintenance Manual | F |
| SYS-LAB-001 | Labelling and Marking Schedule | F |

## A.8 Generation 2

| ID | Title | Class |
|---|---|---|
| SYS-NG-REQ-001 | Next-Generation Safety and Compliance Requirements | F |
| SYS-NG-001 | Generation-2 Compliance-by-Design Checklist | F |

---

# APPENDIX B — TCF FOLDER STRUCTURE

```text
00_Admin
01_System_Overview
02_Boundary_and_Intended_Use
03_Applicable_Standards
04_Requirements
05_Configuration_Baseline
06_Design_Definition
07_Interfaces
08_Risk_and_FMEA
09_Electrical_Safety
10_Single_Fault
11_Software_and_Firmware
12_Mechanical_Safety
13_Verification_and_Test
14_Operations_and_Service
15_Labelling
16_Component_Evidence
17_Gaps_and_Concessions
18_Safety_Document
19_Compliance_Summary
20_Generation_2
99_Archive_and_Superseded
```

---

# APPENDIX C — MANDATORY TEMPLATES

## C.1 Hazard-register row

| Field | Entry |
|---|---|
| Hazard ID |  |
| Hazard |  |
| Cause |  |
| Foreseeable sequence |  |
| Hazardous situation |  |
| Harm |  |
| Initial severity/probability |  |
| Existing controls |  |
| Evidence |  |
| Gap |  |
| Safety requirement |  |
| Verification |  |
| Residual risk |  |
| Approval/status |  |

## C.2 Single-fault row

| Fault ID | Fault | Detection | Protection | Result | Safe? | Evidence | Gap |
|---|---|---|---|---|---|---|---|

## C.3 Compliance-matrix row

| Row | Standard/clause | Topic | Applicability | Rationale | Hazard | Requirement | Control | Evidence | E-state | Status | Gap | Verification | Conclusion |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## C.4 Gap-register row

| Gap ID | Source | Description | Type | Risk | Closure | HUMAN-ACTION | NEXT-GEN | Owner | Evidence | Approval | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|

## C.5 Test record

```text
Test ID:
Title:
Purpose:
System configuration:
Hardware revision:
Software/firmware revision:
Requirements:
Hazards:
Matrix rows:
Operator:
Date:
Test equipment:
Calibration status:
Preconditions:
Method:
Acceptance criteria:
Results:
Deviations:
Conclusion:
Photos/data:
Reviewer:
Approval:
```

## C.6 Residual-risk acceptance

```text
Acceptance ID:
Related gap:
Related hazard:
Affected configuration:
Unresolved condition:
Reason stronger closure is not practicable:
Existing controls:
Restrictions and instructions:
Residual severity/probability:
Review or expiry trigger:
Generation-2 action:
Prepared by:
Reviewed by:
Approved by:
Date:
```

## C.7 Gate record

```text
Gate:
Date:
Chair:
Attendees:
Inputs reviewed:
Key findings:
Open actions:
Deviations:
Decision:
Conditions:
Approvals:
```

---

# APPENDIX D — REVIEW-GATE CHECKLISTS

## D.1 Gate 0

- claim approved;
- editions identified;
- scope exclusions recorded;
- process owner appointed;
- design authority appointed;
- identifiers assigned;
- TCF structure created;
- questions Q1–Q6 resolved or defaulted.

## D.2 Gate 1

- baseline frozen;
- variants recorded;
- hardware revisions captured;
- software/firmware captured;
- cable set captured;
- photo survey complete;
- artefact inventory complete;
- DDR populated;
- uncontrolled changes raised.

## D.3 Gate 2

- hazard categories complete;
- FMEA safety rows complete;
- requirements generated;
- high risks escalated;
- protective measures recorded;
- gaps opened.

## D.4 Gate 3

- clause matrix complete;
- standard editions confirmed;
- applicability rationales complete;
- E2 cleared;
- component ledger complete;
- provisional limits addressed;
- verification plan complete.

## D.5 Gate 4

- technical reviews complete;
- inspections complete;
- tests complete or dispositioned;
- failures recorded;
- deviations assessed;
- manuals updated;
- closure evidence linked.

## D.6 Gate 5

- Safety Document approved;
- compliance summary approved;
- all gaps dispositioned;
- residual risks signed;
- MDL complete;
- citations verified;
- baseline released;
- Generation-2 requirements extracted.

---

# APPENDIX E — SYSTEM-SPECIFIC SURVEY CHECKLISTS

## E.1 Mains and PE

- inlet identified;
- rating visible;
- disconnect identified;
- fuse identified;
- fuse schedule available;
- breaking capacity evidenced;
- PE inlet path visible;
- MET identified;
- panels assessed;
- door bonds assessed;
- paint penetration assessed;
- fasteners assessed;
- mains terminals protected;
- mains/SELV segregation evidenced.

## E.2 Low-voltage outputs

- every rail listed;
- maximum current known;
- current limiting known;
- branch protection known;
- output short assessed;
- overvoltage assessed;
- accessible energy assessed;
- fixture current assessed;
- stored energy assessed.

## E.3 Propagation cables

- all five signal classes included;
- approved length known;
- extension policy known;
- pinouts controlled;
- cable revisions controlled;
- shielding recorded;
- screen termination recorded;
- insulation rating recorded;
- short and crush behaviour assessed;
- labels present;
- strain relief present.

## E.4 Trolley and fixture

- mass known;
- centre of gravity considered;
- castors rated;
- brakes functional;
- handles suitable;
- panels secure;
- sharp edges absent or controlled;
- movement restriction documented;
- fixture secure;
- fixture access controlled.

## E.5 FPGA/LabVIEW

- versions captured;
- safe state defined;
- startup state known;
- reset state known;
- communication-loss state known;
- watchdog known;
- thresholds controlled;
- configuration controlled;
- buffer overflow defined;
- `t0` defined;
- event and acknowledgement separated;
- invalid data flagged.

---

# APPENDIX F — VALIDATION-QUESTION REGISTER

## F.1 Gate 0 questions

1. Confirm claim level.
2. Confirm licensed standard editions.
3. Confirm assessed physical unit and variants.
4. Confirm DUT PCB, cable and sensor boundary.
5. Confirm hardware modification exclusion and escalation authority.
6. Confirm numbering, designation and file format.

## F.2 Gate 1 questions

7. Confirm physical access and competent test personnel.
8. Confirm historical safety evidence and archive location.
9. Confirm design authority and independent reviewer.
10. Confirm installation classification and environment.
11. Confirm EMC position-statement-only approach.
12. Confirm whether monitors-armed interacts with facility safety systems.

## F.3 Gate 3 questions

13. Confirm the UKAEA material is contextual only.
14. Confirm treatment of provisional numeric criteria.
15. Confirm programme deadlines.
16. Confirm maximum approved cable length and extension policy.

Each answer shall be recorded in DECISIONS.md.

---

# APPENDIX G — APPROVED COMPLIANCE WORDING

## G.1 Approved statement

> The system has been retrospectively reviewed and documented against the applicable principles and requirements of IEC/BS EN 61010-1, with additional consideration of applicable particular standards, including external test and measurement circuits where relevant. This review does not constitute third-party certification unless separately assessed by an accredited body.

## G.2 Required qualification

The statement shall identify:

- assessed configuration;
- applicable standards and editions;
- exclusions;
- residual risks;
- restrictions;
- approval date.

---

# APPENDIX H — GENERATION-2 SEED REQUIREMENTS

The following are initial requirements only. Numeric values shall remain provisional until confirmed.

| ID | Requirement |
|---|---|
| NG-SAF-001 | The equipment safety boundary shall be defined at concept stage. |
| NG-SAF-002 | All accessible conductive parts requiring PE shall have a documented bonding scheme. |
| NG-SAF-003 | Every low-voltage output leaving the rack shall be protected against credible cable faults. |
| NG-SAF-004 | Safe states shall be defined for startup, shutdown, power loss, software crash, FPGA reset and communication loss. |
| NG-SAF-005 | DUT bias shall not automatically re-energise after unexpected interruption unless explicitly justified. |
| NG-SAF-006 | External cables shall have controlled length, pinout, rating, shielding and part identity. |
| NG-SAF-007 | DUT latch-up and abnormal current shall be detected and handled by a defined response. |
| NG-SAF-008 | Fundamental electrical safety shall not depend solely on software. |
| NG-SAF-009 | The design shall use approved isolated power-conversion modules rather than an uncontrolled custom mains stage. |
| NG-SAF-010 | Compliance evidence shall be planned and reviewed at SRR, PDR, CDR and first-use release. |
| NG-DATA-001 | A common hardware timebase shall support event correlation. |
| NG-DATA-002 | Bias-current threshold events shall be timestamped. |
| NG-DATA-003 | Shutter transitions shall be timestamped. |
| NG-DATA-004 | Fluence pulses shall be counted and correlated to run time. |
| NG-DATA-005 | Event occurrence time shall be distinct from acknowledgement time. |
| NG-DATA-006 | Configurable pre-event and post-event windows shall be provided. |
| NG-DATA-007 | Buffer overflow and missing data shall be positively indicated. |
| NG-DATA-008 | Hardware, firmware and software versions shall be stored with each run record. |

---

# END OF MANUAL
:::

This version establishes the manual-level structure and working rules without duplicating the Job Specification. The next refinement would normally be to split its appendices into the controlled spreadsheet templates and individual document skeletons named in the canonical register.

[M9] ME (2026-07-06 20:14):
Risk_

[M10] AI (2026-07-06 20:14):
Held.

From what you've provided, plus the consolidated material in **61010 All.docx**, I think the current document has reached the point where it should stop being treated as a collection of ideas and instead become an **engineering manual**. The content is already there, but it exists as multiple generations layered together (A, B, C and D), resulting in repeated guidance, conflicting numbering, and several different document trees. That is also reflected in the uploaded manual, which currently contains overlapping "Section A", "Section B", "Section C" material and repeated topics. fileciteturn3file17L1-L33 fileciteturn3file13L1-L27

## I would completely restructure it

Rather than a 100-page guidance document, it should become something closer to an engineering standard or design manual.

The hierarchy would become:

```
IEC 61010 Retrospective Compliance Uplift Manual
Revision B

Volume 1
Management Manual
-------------------
1. Purpose
2. Scope
3. Normative References
4. Definitions
5. Compliance Philosophy
6. Claim Level
7. Document Architecture
8. Process Overview
9. Gates
10. Deliverables
11. Reconciliation Matrix
12. Validation Questions

Volume 2
Execution Manual
----------------
Phase 0
Phase 1
...
Phase 8

Volume 3
Document Specifications
-----------------------
One chapter per controlled document

SYS-SAF-001
SYS-CFG-001
SYS-RISK-001
SYS-RISK-002
SYS-REQ-002
...

Volume 4
Engineering Guidance
--------------------
Electrical safety
Mechanical safety
Software
FPGA
Interfaces
Cable systems
Verification

Volume 5
Appendices
-----------
Templates
Registers
Checklists
Examples
Decision trees
Cross-reference tables
```

---

## Every chapter should follow exactly the same pattern

Instead of narrative prose, every document specification should become almost procedural.

Example

```
SYS-RISK-001
Hazard Analysis and Risk Register

Purpose

Owner

Inputs

Outputs

Dependencies

Applicable IEC clauses

Applicable Part 2 standards

Relationship to other documents

Mandatory contents

Required tables

Acceptance criteria

Evidence classes

Review frequency

Approval authority

Revision rules

Typical mistakes

Completion checklist

References
```

Every one of the thirty-plus documents should look identical.

That makes the manual usable rather than readable.

---

## The manual should become procedural

Instead of saying

> "Create a hazard register..."

it becomes

```
Step 3.1

Create SYS-RISK-001.

Minimum contents:

•
Electrical hazards

•
Mechanical hazards

•
Thermal hazards

•
Fire hazards

•
Functional hazards

Evidence required:

E1
E2
E3
E4
E5

Output:

Completed document ready for Gate 2.
```

An engineer can literally work down the manual.

---

## Gates become the backbone

Rather than discussing phases repeatedly, everything revolves around gates.

```
Gate 0
Definition

Inputs

Mandatory documents

Acceptance criteria

Outputs

Approvals

Exit conditions

Deliverables
```

repeat for

```
Gate 1
Gate 2
...
Gate 8
```

Every document states which gate creates it.

---

## The document tree should disappear from the narrative

Instead it becomes Appendix A.

The manual should simply reference

```
See Appendix A
Master Document Tree
```

The actual tree becomes graphical.

---

## Every controlled document gets a one-page specification

Rather than discussing documents throughout the manual, dedicate one specification page to each.

Example

```
SYS-SAF-003

Electrical Safety Architecture Review

Purpose

This document demonstrates...

Inputs

Electrical schematics
Power tree
Cable schedule

Outputs

Electrical safety evidence

Owner

Electrical Design Authority

Created

Phase 5

Updated

As required

Evidence

Inspection
Analysis
Calculation
Bench test

Referenced by

Safety Document
Compliance Matrix

Mandatory sections

1

2

3

4

...

Completion checklist
```

That eventually becomes your internal document standard.

---

## Separate process from engineering

Currently they're mixed.

Instead:

Process Manual

> what to do

Engineering Manual

> how to do it

Document Specification

> what each document contains

Templates

> where to write it

That removes duplication.

---

## Risk should become its own manual chapter

Rather than being embedded, I'd elevate it.

```
Chapter 9

Risk Management

9.1 Philosophy

9.2 Method

9.3 Severity

9.4 Probability

9.5 Risk Matrix

9.6 Hazard Categories

9.7 Existing Controls

9.8 Additional Controls

9.9 Verification

9.10 Residual Risk

9.11 Acceptance

9.12 Traceability

9.13 Relationship to FMEA

9.14 Relationship to Compliance Matrix
```

Everything about risk lives there.

---

## The biggest improvement

At the moment the document is approximately

```
40%

guidance

30%

ideas

20%

examples

10%

actual specification
```

I would invert that.

```
75%

specification

15%

procedure

5%

guidance

5%

examples
```

That makes it read like an internal engineering standard rather than a transcript of how the standard was developed.

---

## My recommendation

Based on everything you've produced so far, I would stop thinking of this as **"61010 All.docx"** and instead treat it as **Revision 0 source material**.

The next revision should be a completely rewritten manual—not an edit—that uses all the reconciled content, your precedence rules (Spec → A → C → B → D), the unified document register, the gate structure, and the evidence model as its foundation. The result would likely be in the **180–300 page** range, but with far less repetition and a much stronger engineering workflow. It would function as a repeatable process manual that another engineer—or another AI agent—could execute end to end with minimal ambiguity.
