# Requirements Validation for Reused Hardware
Date (UTC): 2026-02-02 16:23
Conversation ID: 6980cf52-2a48-8397-a168-257f5d0c2e14
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-005.json

[M1] ME (2026-02-02 16:23):
If a project reuses an article of hardware from a previously validated project. How are the requirements for the new project validated best. Referencing the previous verified criteria?

[M2] AI (2026-02-02 16:23):
When a new project reuses previously validated hardware, the *correct* approach is **requirements reuse with explicit re-validation by equivalence**, not blind inheritance. The goal is to *prove* that the prior verification remains valid in the new context.

Below is a **best-practice, systems-engineering compliant method** that is widely accepted in regulated and safety-critical environments.

---

## 1. Establish Reuse Intent and Boundaries

Formally declare the hardware as **“Reused Item”** in the new project.

Define:
- Exact **part number / revision**
- **Firmware / configuration state**
- **Manufacturing process equivalence**
- **Operational environment** (electrical, thermal, mechanical, EMC, radiation, etc.)

> If *any* of these differ, reuse becomes **partial**, not full.

---

## 2. Perform Requirements Mapping (Old → New)

Create a **Requirements Equivalence Matrix**.

For each new-project requirement:
- Identify whether it:
  - **Matches** an existing requirement
  - Is **more stringent**
  - Is **less stringent**
  - Is **new / uncovered**

Example:

| New Req ID | Old Req ID | Status | Action |
|-----------|----------|--------|-------|
| SYS-045 | HW-012 | Identical | Reuse verification |
| SYS-046 | HW-014 | More stringent | Delta test |
| SYS-051 | — | New | Full verification |

This matrix becomes a **formal artifact**.

---

## 3. Verification by Equivalence (Primary Mechanism)

For requirements that are *identical*:

### Acceptable evidence:
- Prior **verification reports**
- Test procedures + **pass results**
- Analysis reports
- Environmental qualification records

### Mandatory justification:
A short **Equivalence Statement**, e.g.:

> “Requirement SYS-045 is satisfied by prior verification HW-012 as the hardware, configuration, operating limits, and environmental conditions are unchanged between Project A and Project B.”

This is **not optional**—auditors expect it.

---

## 4. Delta Analysis (Critical Step)

Perform a **delta analysis** between projects:

### Assess changes in:
- Supply voltages / power budgets
- Timing / bandwidth / loading
- Interfaces (LVDS length, impedance, protocol use)
- Thermal envelope
- Duty cycle / lifetime
- Safety or regulatory context

Classify each delta:
- **No impact**
- **Analysis sufficient**
- **Targeted re-test required**
- **Full re-verification required**

Document this explicitly.

---

## 5. Targeted Re-Verification (When Needed)

Only re-verify what changed.

Examples:
- Longer cable → signal-integrity analysis + eye diagram
- Higher duty cycle → thermal analysis + soak test
- Different EMC class → partial EMC scan

This keeps reuse **efficient but defensible**.

---

## 6. Traceability in the New Project

In the new project:
- Requirements trace to:
  - **Reused verification evidence**, or
  - **New delta verification**

Example trace:
```
SYS-045 → HW-012 → VR-A-034 (reused)
SYS-046 → DT-B-007 (delta test)
```

Never leave a requirement traced only to “previous project” without an artifact.

---

## 7. Formal Reuse Declaration (Strongly Recommended)

Add a **Reuse Justification Section** to the verification plan or compliance matrix:

- List reused items
- Define reuse scope
- State assumptions
- Identify deltas and mitigations

This is often what saves projects during audits.

---

## 8. What *Not* to Do (Common Failures)

❌ Copy requirements and mark them “verified”  
❌ Reference a previous project without equivalence justification  
❌ Ignore environmental or usage changes  
❌ Assume validation “transfers automatically”

These are frequent causes of non-conformances.

---

## Canonical Summary (One-Sentence Rule)

> **Previous verification can be reused only when equivalence is demonstrated, deltas are analysed, and traceable justification exists in the new project.**

---

If you want, I can:
- Provide a **Requirements Equivalence Matrix template**
- Draft a **Reuse Justification section** suitable for design reviews
- Align this to **ECSS / ISO 15288 / DO-254 / IEC 61508** style expectations
- Tailor it specifically to **electronics modules / FPGA / sensor-chain reuse**

Say which framework you want to align to.

[M3] ME (2026-02-02 16:30):
So if a project is only 5% different to a previous project. Is it best to do a delta design document or another complete duplicate document with a delta section 

[M4] AI (2026-02-02 16:30):
**Short answer:**  
For a project that is ~5% different, the **best practice is a *delta design document*** that formally references a **frozen baseline**, *not* a full duplicate design document with a delta section.

Below is the rationale and a defensible structure.

---

## Recommended Approach (Industry-Best Practice)

### **Primary artifact**
**Delta Design & Verification Impact Document**  
referencing a **Baseline Design Package** from the previous project.

This is the model used in aerospace, defence, medical, and high-integrity electronics because it:
- Preserves configuration control
- Avoids divergence and document rot
- Keeps audits clean and fast
- Makes intent explicit: *“we changed very little, and here is exactly what”*

---

## Why NOT Duplicate the Full Design Document

Duplicating a 95%-identical document introduces real risk:

- ❌ Two “authoritative” descriptions of the same hardware  
- ❌ Silent drift in future updates  
- ❌ Reviewers miss changes buried in copied text  
- ❌ Traceability becomes ambiguous (“which document governs?”)

Auditors and senior reviewers generally *dislike* this model.

---

## Canonical Structure (What Works Best)

### 1. **Baseline Reference (Frozen)**
Explicitly identify the reused design:

- Project name / identifier
- Document IDs (requirements, design, verification)
- Hardware revision
- Firmware version
- Configuration checksum (if applicable)

Example:
> “This project reuses the hardware design defined in Project A, Design Document DD-A-001 Rev C, unchanged except where explicitly stated in this delta document.”

This makes the old documentation **normative**.

---

### 2. **Delta Design Document (Primary New Document)**

This document contains *only* what changed and the impact of those changes.

**Mandatory sections:**

#### 2.1 Scope of Reuse
- Reused subsystems
- Explicit exclusions
- Assumptions

#### 2.2 Change Summary Table
| Area | Change | Reason | Impact |
|----|------|------|------|
| Power | +0.3 V rail | New sensor | Thermal review |
| Firmware | Timing tweak | Interface change | SI analysis |

#### 2.3 Detailed Deltas
- Schematics (only changed pages)
- BOM changes
- Firmware diffs
- Mechanical drawings (if any)

#### 2.4 Requirements Impact
Mapping of:
- Unchanged → reused verification
- Changed → delta verification
- New → full verification

#### 2.5 Verification Impact Statement
- Reused evidence
- New tests
- Analyses performed
- Tests explicitly *not* repeated (with justification)

---

### 3. **Traceability Statement**
Explicitly state how traceability is handled:

> “Requirements not listed in Section X inherit verification evidence from Project A. Requirements listed herein are verified by delta activities defined in Section Y.”

This is extremely important in regulated environments.

---

## When a Full Duplicate Document *Is* Justified

A full re-issue may be acceptable **only if** one of the following is true:

- Regulatory body explicitly requires a standalone pack
- The original documentation quality is poor or inconsistent
- The organisation lacks configuration control discipline
- The product will diverge significantly in future revisions

Even then, best practice is:
> **Full document + embedded references to original verification evidence**, not re-verification.

---

## Decision Rule (Use This Internally)

| Change Level | Best Artifact |
|------------|--------------|
| 0–10% | **Delta design document** |
| 10–30% | Delta + partial re-issued sections |
| 30–60% | New design document referencing reused blocks |
| >60% | New project documentation |

At **5%**, delta-only is the cleanest and safest approach.

---

## One-Line Executive Justification

> “A delta design document preserves a single authoritative baseline while providing explicit, auditable justification for all changes and their verification impact.”

---

If you want, I can:
- Provide a **Delta Design Document template**
- Provide wording that satisfies **ISO 15288 / ECSS / DO-254 reviewers**
- Help you write a **reuse policy** you can apply across projects
- Tailor this to **electronics / FPGA / sensor-chain reuse**

Say which framework you’re working under.

[M5] ME (2026-02-02 16:33):
Provide 

[M6] AI (2026-02-02 16:33):
Below is a **ready-to-use Delta Design & Verification Impact Document template**, suitable for electronics / FPGA / hardware reuse projects and acceptable under ISO 15288 / ECSS / DO-254 style reviews.

---

# Delta Design & Verification Impact Document  
*(For Reused Hardware Projects)*

---

## 1. Document Control

| Item | Value |
|----|----|
| Project | \<New Project Name\> |
| Document ID | DD-DELTA-XXX |
| Revision | A |
| Date | \<dd-mm-yyyy\> |
| Author | \<Name\> |
| Baseline Project | \<Previous Project Name\> |
| Baseline Doc(s) | \<DD-A-001 Rev C, VR-A-004 Rev B, etc.\> |

---

## 2. Purpose and Scope

This document defines and justifies all design, requirements, and verification differences between the **Baseline Project** and the **New Project**.

All design elements, requirements, and verification evidence **not explicitly listed in this document** are inherited unchanged from the baseline documentation.

---

## 3. Baseline Reference (Frozen)

The following baseline artifacts are **normative** for this project:

- Design Description: \<ID, Rev\>
- Requirements Specification: \<ID, Rev\>
- Verification Reports: \<ID, Rev\>
- Hardware Revision: \<PN / Rev\>
- Firmware Version / Hash: \<if applicable\>

**Assumption:** Baseline hardware, firmware, manufacturing process, and operating limits are unchanged except where stated herein.

---

## 4. Scope of Reuse

### 4.1 Fully Reused (No Change)
- \<Subsystem A\>
- \<Subsystem B\>

### 4.2 Modified (Delta Applies)
- \<Subsystem C\>
- \<Interface D\>

### 4.3 Explicitly Excluded
- \<Anything not reused\>

---

## 5. Change Summary (High-Level)

| Area | Change | Reason | Impact |
|----|----|----|----|
| Power | +0.3 V rail | New load | Thermal & margin review |
| FPGA | Timing tweak | Interface delta | SI analysis |
| BOM | Alt regulator | Availability | No functional impact |

---

## 6. Detailed Design Deltas

### 6.1 Electrical
- Schematic pages changed: \<IDs\>
- Net changes: \<summary\>
- Load / margin impact: \<summary\>

### 6.2 Firmware / FPGA
- Modified modules: \<names\>
- Behavioural change: \<summary\>
- Configuration impact: \<summary\>

### 6.3 Mechanical / Thermal (if applicable)
- Enclosure changes: \<none / describe\>
- Thermal delta: \<summary\>

---

## 7. Requirements Impact Assessment

### 7.1 Requirements Mapping

| New Req ID | Baseline Req ID | Status | Verification Method |
|----|----|----|----|
| SYS-001 | HW-001 | Identical | Reuse evidence |
| SYS-014 | HW-009 | Modified | Delta test |
| SYS-021 | — | New | Full verification |

### 7.2 Equivalence Statement (Reusable Text)

> “Requirements marked *Identical* are satisfied by prior verification evidence from the Baseline Project. Hardware design, configuration, operating conditions, and environment remain unchanged with respect to these requirements.”

---

## 8. Verification Impact Analysis

### 8.1 Reused Verification Evidence
- VR-A-012 (Power margins)
- VR-A-019 (Thermal soak)
- VR-A-027 (Functional test)

### 8.2 Delta Verification Activities

| Test ID | Purpose | Type | Status |
|----|----|----|----|
| DT-001 | Power margin check | Analysis | Complete |
| DT-002 | SI eye diagram | Test | Planned |

### 8.3 Tests Not Repeated (Justified)

| Test | Reason |
|----|----|
| EMC scan | No electrical or layout change |
| Vibration | Mechanical unchanged |

---

## 9. Risk and Assumptions

### 9.1 Assumptions
- Manufacturing process unchanged
- Operating envelope unchanged
- Supplier equivalence confirmed

### 9.2 Residual Risks
- \<Risk\> – mitigated by \<action\>

---

## 10. Compliance Statement

> “This project is compliant with all applicable requirements. All deviations from the baseline design have been identified, assessed, and verified as documented herein.”

---

## 11. Approval

| Role | Name | Signature | Date |
|----|----|----|----|
| Engineering |  |  |  |
| Verification |  |  |  |
| Quality |  |  |  |

---

## Practical Rule to Apply Internally

> **If it isn’t in the delta document, it didn’t change—and its verification is reused.**

---

If you want next:
- A **Requirements Equivalence Matrix (Excel-ready)**
- A **Verification Reuse Justification** one-page addendum
- A **policy wording** you can reuse across all future projects
- A version tailored specifically to **FPGA / sensor-chain / PoE hardware**

State which you want.
