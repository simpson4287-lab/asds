# Retrospective IEC 61010 Uplift
Date (UTC): 2026-07-03 09:22
Conversation ID: 6a477f4c-c814-83ed-b0b5-2d651264c9ec
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-008.json

[M1] ME (2026-07-03 09:22):
I have a test system used for characterising image senses for the purposes of heavy iron on radiation, although it could just as easily be adapted to other forms of radiation with extension of propagation cables. The system is mature now and our latest offering is a result of 10 to 15 years of continuous ramp up in the areas of radiation testing. 

The system has a full and comprehensive data pack, although it could be slightly restructured for better hierarchy in terms of detail. The next generation test system will come along in due course where requirements will be captured. How to take the current offering to the next level although the form factor will largely stay the same the functionality will be major enhanced architecture. I don’t feel this in any way will make any changes to safety And its compliance to the likes of IEC 61010.

So what I’m planning to do is to retrospectively 61010 that system. I won’t necessarily carry out the physical updates but I certainly want to uplift the data pack and full technical construction file to a standard that is referenced to the six 1010 as compliant (not necessarily officially)

The test system is a 19 inch rackmount trolley about 1 m high fed with by a single 230 V AC mains. It then develops very low DC levels in the order of 12 V propagate signal IO down to meter cables to a PCB mounted on a support fixture that is then Exposed in the beam line.

So what I need to do is develop a extremely through and concise action plan as to how to go about this retrospectively. By doing this, I will know exactly the process that needs to be followed when I do the next level system.

What are your early thoughts on this and summarise the top level activities that are key to achieving the target goal?

[M2] AI (2026-07-03 09:22):
I’ll treat this as a “retrospective design assurance / technical file uplift” rather than a formal product certification exercise. The key distinction will be: prove the mature system is controlled, documented, risk-assessed, and tested against IEC 61010 principles without overstating official compliance.

[M3] AI (2026-07-03 09:22):
A useful first framing is to define the “equipment boundary” very explicitly: rack trolley, mains inlet, internal PSUs, control electronics, cabling, DUT fixture/interface, and what sits outside the system at the radiation facility. That boundary will prevent IEC 61010, EMC, facility interlocks, and radiation safety from getting blurred together.

[M4] AI (2026-07-03 09:22):
Assuming “heavy iron” means **heavy-ion radiation**, your idea is sound: treat this as a **retrospective IEC 61010-aligned technical construction file uplift**, not as a claim that the system is formally certified unless you actually run the formal assessment/test route.

IEC 61010-1 is the right centre of gravity because it covers electrical equipment for **test/measurement, control, and laboratory use**. citeturn217051search2 For your system, I would also check whether **IEC 61010-2-030** applies to the external measuring/test circuits going down the propagation cables to the DUT fixture, because that part covers measuring circuits connected to devices or circuits outside the equipment itself. citeturn625629search6 If there is PLC-style/control equipment architecture, **IEC 61010-2-201** may also be relevant for the control-equipment side. citeturn625629search1 EMC should probably sit alongside this under **IEC 61326-1**, which covers EMC requirements for electrical equipment for measurement, control and laboratory use. citeturn217051search12

The important wording is:

> **“Designed, reviewed and documented against the applicable requirements of IEC/BS EN 61010-1, with supporting gap assessment and verification evidence.”**

I would avoid simply saying **“IEC 61010 compliant”** unless you have done the full applicable assessment, testing, evidence review, and sign-off route. For UK/GB placing-on-market scenarios, the electrical safety regulations require technical documentation and conformity assessment, and technical documentation/declaration records are expected to be retained for 10 years. citeturn217051search3turn217051search10

## Early judgement

This sounds like a good candidate for retrospective 61010 alignment because the electrical hazard profile is relatively bounded:

Single 230 V AC input → enclosed rack/trolley → internal conversion to low-voltage DC → signal/control propagation → exposed DUT/interface PCB at beam line.

The highest-value work is probably not physical redesign at first. It is:

**define the safety boundary, freeze the design baseline, map IEC 61010 requirements to existing evidence, identify gaps, then create a controlled technical construction file that future systems can inherit.**

Also, keep radiation safety separate. IEC 61010 can address the electrical/lab-equipment safety of the test system, but the ionising radiation work itself sits under facility radiation controls, local rules, and radiation risk assessment. In the UK, HSE guidance for IRR17 says radiation employers must assess radiation risks before new ionising-radiation activities, including exposure levels and accident situations. citeturn371739search7

## Target evidence chain

The whole exercise should build this traceable chain:

**Intended use → equipment boundary → applicable standards → hazard/risk assessment → design controls → verification evidence → residual risk → user/service documentation → internal compliance statement → change-control process.**

That chain is more important than just producing a thicker data pack.

## Top-level activities

### 1. Define the compliance scope

Write a short **compliance strategy document** first. This should define:

- Intended use: image sensor characterisation during heavy-ion/radiation exposure.
- Users: trained engineers/operators, not general public.
- Environment: lab/radiation test facility, indoor controlled use.
- Equipment boundary: 19-inch rack trolley, mains input, PSUs, control electronics, signal I/O, propagation cables, DUT support fixture/interface PCB.
- Exclusions: radiation source/facility interlocks unless your system interfaces to them.
- Claim level: “IEC 61010-aligned internal technical file” versus “formally certified product”.

This avoids the common trap of trying to make the whole radiation facility part of the product safety file.

### 2. Freeze the current design baseline

Before assessing anything, capture exactly what “the current system” is.

Minimum baseline pack:

- System block diagram.
- Rack layout and internal photos.
- Wiring diagrams.
- Mains distribution diagram.
- Protective earth/bonding diagram.
- PSU list and datasheets.
- Cable schedule.
- Connector schedule.
- PCB assemblies and revision levels.
- BOM / critical safety component list.
- Firmware/software revision list.
- External DUT fixture/interface definition.
- Known variants and build differences.

This is where mature systems often have weakness: the system works, but the build knowledge lives in engineers’ heads.

### 3. Produce an IEC 61010 applicability matrix

Create a clause-by-clause **61010 applicability/gap matrix**.

For each requirement, classify it as:

- Applicable.
- Not applicable, with justification.
- Applicable and satisfied, with evidence reference.
- Applicable but evidence missing.
- Applicable and design gap exists.

This becomes the backbone of the retrospective work. It should reference drawings, photos, calculations, datasheets, inspection records, and test reports.

### 4. Perform a structured hazard/risk assessment

Do not make this just an electrical checklist. Use a proper system hazard review.

Key hazards for your system:

- Electric shock from 230 V AC mains.
- Loss of protective earth.
- Inadequate bonding between rack panels, trolley frame, doors, and exposed metalwork.
- Fire from PSU faults, cable shorts, overloaded outputs, or incorrect fusing.
- Stored energy in capacitors.
- Incorrect cable connection to the beamline/DUT.
- Output short-circuit or backfeed from external equipment.
- Mechanical instability of the trolley.
- Pinch, crush, sharp-edge, and rack-access hazards.
- Thermal hazards from enclosed PSUs/electronics.
- EMC causing malfunction or false test states.
- Software/FPGA fault causing unsafe output state.
- Beamline interface failure, including damaged long propagation cables.
- Maintenance/service access while energised.
- Misuse: wrong mains lead, wrong fuse, wrong connector, exposed DUT touched while powered.

For each hazard, capture:

**cause → hazardous situation → existing control → verification evidence → residual risk → required action.**

### 5. Review the electrical safety architecture

This is probably the technical heart of the 61010 uplift.

Check and document:

- Mains inlet rating.
- Fuse type, breaking capacity, location, and coordination.
- Switch/disconnect method.
- Protective earth bonding path.
- Earth bond resistance evidence.
- Separation between mains and SELV/low-voltage circuits.
- Creepage/clearance review.
- PSU safety approvals.
- Enclosure/fire containment.
- Cable strain relief.
- Gland/connector ratings.
- Internal wire ratings and routing.
- Earthing philosophy for signal shields/screens.
- Accessible conductive parts.
- Accessible voltage/current/energy limits.
- Output protection on propagated lines.
- Protection against shorted propagation cables.
- Protection against incorrect external connections.
- Labelling of hazardous areas and service-only access.

Your system may only produce low DC levels at the DUT, but the rack still contains mains-derived supplies, so the safety case must prove that the low-voltage side remains acceptably isolated and energy-limited under normal and single-fault conditions.

### 6. Define normal-condition and single-fault verification

This is where you turn “we believe it is safe” into evidence.

Likely verification activities:

- Protective earth continuity test.
- Insulation resistance / dielectric withstand where appropriate.
- Leakage/touch current assessment.
- Functional check of mains isolation/switching.
- Fuse/protection review.
- Output short-circuit testing.
- Cable fault testing: open, short, miswire where credible.
- PSU overvoltage/overcurrent behaviour review.
- Thermal soak test under worst-case load.
- Fan/ventilation blockage assessment if applicable.
- Trolley stability/mechanical inspection.
- Sharp edge/accessibility inspection.
- Labelling inspection.
- Emergency shutdown behaviour.
- Software/FPGA safe-state behaviour.
- Power loss and power restoration behaviour.

For a retrospective exercise, you may separate these into:

**Evidence already available**, **inspection-only evidence**, **bench verification required**, and **formal external lab testing required if certification is ever pursued**.

### 7. Build a proper technical construction file structure

I would restructure the data pack into a controlled TCF with this hierarchy:

1. **System overview**
   - Intended use.
   - Operating environment.
   - System boundary.
   - High-level architecture.

2. **Compliance strategy**
   - Applicable standards.
   - Assumptions.
   - Exclusions.
   - Claim wording.

3. **Requirements and traceability**
   - User/system requirements.
   - Safety requirements.
   - 61010 applicability matrix.
   - Verification matrix.

4. **Design definition**
   - Drawings.
   - Schematics.
   - Wiring.
   - BOM.
   - Cable schedules.
   - Rack layout.
   - Mechanical drawings.
   - PCB/interface details.

5. **Risk and safety file**
   - Hazard log.
   - Risk assessment.
   - Single-fault analysis.
   - Safety-critical component list.
   - Residual risk summary.

6. **Verification evidence**
   - Electrical safety tests.
   - EMC evidence/test plan.
   - Functional safety checks.
   - Inspection records.
   - Calibration records.
   - Environmental/thermal checks.

7. **User and service documentation**
   - Operator manual.
   - Installation guide.
   - Maintenance procedure.
   - Beamline setup procedure.
   - Warnings and labels.
   - Emergency shutdown instructions.

8. **Manufacture and configuration control**
   - Build procedure.
   - Inspection checklist.
   - Release checklist.
   - Serial/revision control.
   - Change-control process.

9. **Compliance summary**
   - Gap closure report.
   - Internal declaration / engineering statement.
   - Open issues.
   - Limits of claim.

### 8. Create a gap-action register

Every finding should become an action with an owner, severity, evidence requirement, and closure state.

Example fields:

- Gap ID.
- IEC clause / internal requirement.
- Description.
- Risk level.
- Existing evidence.
- Required action.
- Action type: documentation, inspection, test, design change.
- Owner.
- Closure evidence.
- Residual risk acceptance.

This gives you a clean management route without implying every gap means hardware must be changed.

### 9. Separate present-system uplift from next-generation requirements

This is very important.

For the mature/current system, the goal is:

**Document, justify, inspect, verify, and control.**

For the next-generation system, the goal is:

**Specify safety requirements from day one.**

So every retrospective gap should be tagged as either:

- Must fix now.
- Must document now.
- Acceptable with justification.
- Next-generation design requirement.
- Requires external compliance advice/testing before commercial release.

This will turn the retrospective exercise into a requirements-capture engine for the future system.

## The key deliverables I would aim for

By the end, you want these core documents:

1. **IEC 61010 Retrospective Compliance Strategy**
2. **System Boundary and Intended Use Definition**
3. **Design Baseline Pack**
4. **IEC 61010 Applicability / Gap Matrix**
5. **System Hazard and Risk Assessment**
6. **Electrical Safety Architecture Review**
7. **Single-Fault Analysis**
8. **Verification and Test Plan**
9. **Verification Evidence Pack**
10. **Updated Operator and Service Manual**
11. **Technical Construction File Index**
12. **Internal Compliance Statement**
13. **Next-Generation Safety Requirements Register**

## My strongest early recommendation

Do not start by editing the whole data pack. Start with three control documents:

1. **System Boundary Statement**  
2. **IEC 61010 Applicability Matrix**  
3. **Hazard/Risk Register**

Those three will tell you what the rest of the file needs to contain. Once they are solid, the data pack restructuring becomes much easier and far more defensible.

[M5] ME (2026-07-03 09:31):
Expand further as much as possible to a manual level to steer through process

[M6] AI (2026-07-03 09:32):
I’ll turn this into a working procedure you can actually follow: phases, document outputs, review gates, checklists, and example wording. I’ll keep the claim conservative so it supports an internal technical file without accidentally implying formal third-party certification.

[M7] AI (2026-07-03 09:32):
I’ve pulled in the wider architecture you’ve described before: PXI/LabVIEW/FPGA logging, event flags, shutter state, fluence count pulses, bias-current monitoring, long harnesses, and the in-beam DUT/interface PCB. I’ll write this so it can become the process blueprint for both the current rack and the next-generation version.

[M8] AI (2026-07-03 09:32):
Below is a **manual-level process** you can use to steer the retrospective IEC 61010 uplift. I’ll use “heavy-ion” for the radiation context.

The right way to frame this is:

> **Retrospective safety and technical-file uplift of a mature 230 V AC-fed rackmount radiation image-sensor test system, reviewed against applicable IEC 61010 principles, with identified evidence, gaps, residual risks, and future-generation design requirements.**

IEC 61010-1 is appropriate because it covers electrical equipment for **test and measurement, industrial process-control, and laboratory use**. citeturn435608search0 IEC 61010-2-030 is worth screening because it covers test/measurement circuits connected to external devices or circuits outside the equipment itself, which maps onto your propagated signal/bias/DUT interface side. citeturn435608search10 EMC should sit beside the safety file, typically using IEC 61326-1 for measurement, control and laboratory equipment EMC requirements. citeturn435608search4 In a UK/GB context, technical documentation and conformity-assessment expectations are also relevant where equipment is placed on the market. citeturn435608search5turn435608search12

---

# Retrospective IEC 61010 Uplift Manual  
## For mature 19-inch rackmount radiation image-sensor characterisation system

## 0. Purpose of the exercise

The purpose is not simply to “tidy the data pack”.

The purpose is to produce a defensible engineering safety file showing that the current system has been:

1. **Defined**
2. **Bounded**
3. **Risk-assessed**
4. **Reviewed against IEC 61010 principles**
5. **Verified where necessary**
6. **Controlled under configuration management**
7. **Given a clear residual-risk position**
8. **Used as the safety baseline for the next-generation system**

The output should be a **Technical Construction File**, or TCF, that could support an internal engineering statement such as:

> “The system has been retrospectively reviewed and documented against the applicable principles and requirements of IEC/BS EN 61010-1, with additional consideration of applicable particular standards, including external test/measurement circuits where relevant. This review does not constitute third-party certification unless separately assessed by an accredited body.”

That wording matters. It is strong, useful, and honest.

---

# 1. Define the claim level

Before touching drawings or test records, decide what claim you are actually making.

## 1.1 Claim levels

Use a ladder like this:

| Claim level | Meaning | Recommended for you? |
|---|---|---|
| **Safety reviewed** | Internal review against safety principles only | Too weak |
| **IEC 61010-aligned** | Technical file structured around IEC 61010 requirements | Good starting point |
| **Reviewed against applicable IEC 61010 requirements** | Clause-by-clause gap review completed | Strong target |
| **Designed to meet IEC 61010** | Design evidence supports compliance, but no external certification | Good for internal/product literature with caution |
| **IEC 61010 compliant** | Full evidence and sign-off supports compliance claim | Use carefully |
| **Certified to IEC 61010** | Third-party certification/test house evidence exists | Only if actually done |

## 1.2 Recommended target claim

For the current mature system, I would aim for:

> **Internally assessed and technically documented against the applicable requirements of IEC 61010-1, with supporting gap assessment, risk assessment, and verification evidence.**

For the next-generation system:

> **Safety requirements captured at concept stage and designed to meet the applicable IEC 61010 family requirements from the outset.**

---

# 2. Establish the equipment boundary

This is the first formal document.

Call it:

> **SYS-SAF-001 — Equipment Boundary and Intended Use Statement**

## 2.1 Boundary definition

Define what is inside and outside the equipment.

### Inside the system boundary

Likely included:

- 19-inch rackmount trolley, approximately 1 m high.
- Single 230 V AC mains input.
- Mains inlet, switchgear, fusing, filters, distribution.
- Internal AC/DC PSUs.
- Internal low-voltage DC rails.
- Control electronics.
- PXI/LabVIEW/FPGA elements if included in the delivered rack.
- Bias-generation circuitry.
- Monitoring circuitry.
- Image sensor interface electronics.
- Signal I/O propagation electronics.
- Cable assemblies supplied with the system.
- Support fixture electronics.
- DUT/interface PCB mounted near or in the beamline.
- Operator-accessible controls and indicators.
- Service-accessible internal areas.
- Software/firmware required for operation.

### Outside the system boundary

Likely excluded, unless directly supplied or controlled by you:

- Radiation beam source.
- Facility beamline safety interlocks.
- Facility emergency stops.
- Facility dosimetry equipment.
- Local radiation shielding.
- Host building electrical installation.
- External customer equipment not supplied with the system.
- DUT image sensor itself, unless supplied as part of a configured test article.
- Radiation safety case, except where your system interfaces with it.

## 2.2 Boundary drawing

Create a single-page diagram showing:

```text
230 V AC mains
   |
   v
Rack trolley
   |-- mains inlet / switch / fuse / PE
   |-- AC/DC PSUs
   |-- control electronics
   |-- PXI / FPGA / LabVIEW logging
   |-- bias supplies
   |-- shutter / fluence / event monitoring
   |-- image acquisition / sensor control
   |
   v
Propagation cables, approx. several metres to 15 m or more depending setup
   |
   v
In-beam or near-beam support fixture / DUT PCB
   |
   v
Image sensor under radiation exposure
```

## 2.3 Key boundary questions

Answer these explicitly:

1. Is the DUT PCB part of the supplied system?
2. Are propagation cables supplied, specified, or facility-provided?
3. Are bias rails energy-limited under fault?
4. Can the DUT or fixture become operator-accessible while powered?
5. Can the beamline side connect to other hazardous equipment?
6. Is the system used only by trained personnel?
7. Is the rack intended to be moved while energised?
8. Are there any service operations performed live?
9. Does the system rely on software to maintain safety?
10. Does the system interface to radiation facility interlocks?

These answers drive the rest of the file.

---

# 3. Define intended use and foreseeable misuse

Call this:

> **SYS-SAF-002 — Intended Use, Operating Environment and Foreseeable Misuse**

## 3.1 Intended use

Example wording:

> The system is intended for laboratory and radiation-facility use by trained technical personnel. It provides controlled low-voltage biasing, signal I/O, image sensor readout/control, event monitoring, and data capture for image sensors or detector assemblies exposed to heavy-ion or other radiation sources. The system is powered from a single 230 V AC mains supply and develops low-voltage DC rails and signal interfaces propagated to a DUT/interface PCB mounted on a support fixture at or near the beamline.

## 3.2 User classes

Define user groups:

| User | Access level | Expected competence |
|---|---:|---|
| Operator | External controls/software only | Trained test engineer |
| Facility operator | Beamline controls only | Radiation facility trained |
| Service engineer | Internal rack access | Electrically competent |
| Design engineer | Full design access | Product/domain specialist |
| Customer/user | Configured operation only | Trained by supplier |

## 3.3 Operating environments

Define:

- Indoor laboratory.
- Controlled radiation facility.
- Dry environment unless otherwise specified.
- Professional/industrial/laboratory EMC environment.
- 230 V AC mains supply.
- No explosive atmosphere.
- No medical use.
- No household/consumer use.
- No outdoor use unless separately assessed.

## 3.4 Foreseeable misuse

Include at least:

- Wrong mains lead used.
- Wrong fuse fitted.
- System operated with panels removed.
- DUT fixture touched while powered.
- Cable connected to wrong socket.
- Propagation cable damaged, crushed, or partially disconnected.
- Beamline cable extended beyond validated length.
- DUT latch-up causes high current draw.
- Shutter/event/fluence lines misinterpreted by software.
- System moved while powered.
- Ventilation blocked.
- Rack overloaded with additional equipment.
- Service performed by unqualified personnel.
- Software run with wrong configuration file.
- Old cable set used with new hardware revision.

---

# 4. Freeze the design baseline

Call this:

> **SYS-CFG-001 — Current System Design Baseline**

This is the “what exactly are we assessing?” document.

## 4.1 Configuration freeze

Assign:

- System name.
- System variant.
- Serial number or configuration ID.
- Build revision.
- Rack revision.
- PCB revisions.
- Cable-set revision.
- Software release.
- FPGA/firmware release.
- LabVIEW application version.
- Configuration file version.
- Applicable DUT fixture version.

Example:

```text
System: Radiation Image Sensor Characterisation Rack
Configuration ID: RISC-RACK-GEN1-RETRO-001
Baseline date: YYYY-MM-DD
Power input: 230 V AC single phase
Output/interface: low-voltage DC bias and signal I/O to remote DUT PCB
Primary use: heavy-ion image sensor characterisation
Assessment type: retrospective IEC 61010 technical file uplift
```

## 4.2 Required baseline artefacts

Create a document index.

| Artefact | Required? | Status |
|---|---:|---|
| System block diagram | Yes |  |
| Rack front/rear photos | Yes |  |
| Internal rack photos | Yes |  |
| Mains wiring diagram | Yes |  |
| Protective earth/bonding diagram | Yes |  |
| PSU list and datasheets | Yes |  |
| Fuse schedule | Yes |  |
| Cable schedule | Yes |  |
| Connector schedule | Yes |  |
| PCB schematics | Yes |  |
| PCB layouts | Desirable |  |
| BOM | Yes |  |
| Safety-critical parts list | Yes |  |
| Software architecture | Yes |  |
| FPGA architecture | If applicable |  |
| LabVIEW state-machine description | If applicable |  |
| Test procedures | Yes |  |
| Calibration procedures | If applicable |  |
| Operator manual | Yes |  |
| Service manual | Yes |  |
| Label schedule | Yes |  |
| Risk assessment | Yes |  |
| Verification records | Yes |  |

## 4.3 Configuration traps to catch

Look for:

- Hand modifications.
- Non-drawing-controlled harness changes.
- PSU substitutions.
- Different fuse values between builds.
- Unrecorded panel bonding.
- Cable-screen termination differences.
- Customer-specific variations.
- Prototype boards still in use.
- Old LabVIEW executable with new hardware.
- Firmware not version-controlled.
- Facility-specific adaptor cables.

Anything that exists physically but not in the data pack becomes a gap.

---

# 5. Build the applicable-standards register

Call this:

> **SYS-COMP-001 — Applicable Standards and Compliance Strategy**

## 5.1 Primary standard set

For your system, screen at least:

| Standard | Why it matters |
|---|---|
| IEC/BS EN 61010-1 | General safety requirements for measurement/control/lab equipment |
| IEC 61010-2-030 | External test/measurement circuits connected outside equipment |
| IEC 61010-2-201 | Possible relevance if equipment behaves as industrial control equipment |
| IEC 61326-1 | EMC for measurement/control/lab equipment |
| Low Voltage / Electrical Equipment Safety Regulations | Market/compliance context |
| Machinery/mechanical standards | Only if mechanical hazards become significant |
| Facility radiation rules | Interface only, not product electrical safety |

## 5.2 Standard applicability decision

For each standard, write a formal decision.

Example:

| Standard | Decision | Reason |
|---|---|---|
| IEC 61010-1 | Applicable | System is electrical test/control/lab equipment powered from 230 V AC |
| IEC 61010-2-030 | Screen as applicable | System has external DUT/interface circuits connected via propagation cables |
| IEC 61326-1 | Applicable as EMC framework | System is measurement/control/lab equipment with signal acquisition and control functions |
| Radiation-specific safety standards | Interface only | Radiation source and shielding are facility-controlled, not supplied system boundary |

---

# 6. Create the IEC 61010 applicability matrix

Call this:

> **SYS-COMP-002 — IEC 61010 Applicability and Gap Matrix**

This becomes your core working tool.

## 6.1 Matrix fields

Use columns like:

| Field | Purpose |
|---|---|
| Clause / topic | The IEC 61010 requirement area |
| Applicability | Applicable / Not applicable / Partially applicable |
| Justification | Why it applies or does not |
| Existing design control | What the system already has |
| Evidence reference | Drawing, test report, datasheet, photo, calculation |
| Gap type | None / documentation / test / design |
| Risk level | Low / medium / high |
| Required action | What must be done |
| Owner | Responsible person |
| Closure evidence | How the gap is closed |
| Status | Open / in progress / closed / accepted |

## 6.2 Example entries

| Topic | Applicability | Existing control | Gap | Action |
|---|---|---|---|---|
| Mains input protection | Applicable | Fused IEC inlet / internal distribution | Fuse rationale missing | Create fuse and protection schedule |
| Protective earth continuity | Applicable | Rack bonded to PE | No formal test record | Perform PE continuity test and record |
| Mains/SELV separation | Applicable | Approved AC/DC PSUs | Internal wiring evidence incomplete | Review creepage/clearance and routing photos |
| Output energy limiting | Applicable | Low-voltage DC rails | Fault-current evidence missing | Test or calculate short-circuit limits |
| Long cable fault | Applicable | Multi-metre propagation cables | Miswire/short analysis missing | Add cable fault analysis |
| DUT latch-up | Applicable to use case | Bias/current monitoring | Shutdown thresholds unclear | Define current-limit/shutdown behaviour |
| Software safe state | Applicable if software controls outputs | LabVIEW/FPGA control | Safety dependency unclear | Define hardware vs software safety functions |
| Markings and warnings | Applicable | Some labels present | Label schedule missing | Create label schedule and inspection record |
| Service access | Applicable | Rack panels removable | Live service rules unclear | Add service procedure and warnings |
| EMC immunity | Applicable | Mature system history | Formal EMC evidence unclear | Create EMC rationale/test plan |

---

# 7. Create the hazard and risk assessment

Call this:

> **SYS-RISK-001 — System Hazard Analysis and Risk Register**

This should be independent of the clause matrix. The clause matrix asks “what does the standard require?” The hazard analysis asks “what can hurt someone or cause unsafe operation?”

## 7.1 Risk method

Use a simple method:

| Severity | Meaning |
|---|---|
| S1 | Minor inconvenience or no injury |
| S2 | Minor injury or reversible harm |
| S3 | Serious injury, electric shock, burn, fire risk |
| S4 | Fatality or multiple serious injuries |

| Probability | Meaning |
|---|---|
| P1 | Very unlikely |
| P2 | Credible but uncommon |
| P3 | Reasonably foreseeable |
| P4 | Likely during lifecycle |

Then classify:

```text
Risk = Severity x Probability
```

You do not need an overcomplicated risk model. You need consistency.

## 7.2 Hazard categories

### Electrical shock

- Contact with 230 V AC inside rack.
- Damaged mains inlet or cable.
- Incorrect protective earth connection.
- Metal rack panel not bonded.
- Service access while energised.
- Breakdown of PSU isolation.
- External cable bringing hazardous voltage back into system.
- Incorrect connection to facility equipment.

### Fire and thermal

- PSU fault.
- Cable short.
- Incorrect fuse.
- Overloaded low-voltage output.
- DUT latch-up.
- Tantalum/electrolytic capacitor failure.
- Ventilation blocked.
- Fan failure.
- Rack operated in high ambient environment.
- Unrated cable used in long propagation harness.

### Energy and output hazards

- Low voltage but high available current.
- Shorted bias rail.
- Bias rail overvoltage.
- Reverse polarity at DUT.
- Incorrect connector mating.
- Backfeed from external bench supply.
- Long cable fault causing overheating.
- Stored charge after power-down.

### Mechanical

- Trolley instability.
- Rack tipping while being moved.
- Heavy equipment mounted too high.
- Sharp internal sheet-metal edges.
- Cable trip hazards.
- Fixture collapse or movement at beamline.
- Inadequate strain relief.
- Pinch points in support fixture.

### Functional / control

- Software state-machine error.
- FPGA output stuck active.
- Loss of communication to PXI/controller.
- Power restored into unsafe state.
- Test starts with wrong configuration.
- Shutter state logged incorrectly.
- Fluence count misinterpreted.
- Event timestamp not aligned to exposure.
- Current event flag missed.
- Operator believes output is off when still active.

### Radiation-context interface

Keep this carefully separated:

- System used in radiation environment.
- In-beam DUT PCB may become activated or contaminated depending facility rules.
- Cable access may be restricted during beam operation.
- Radiation damage may cause DUT latch-up or short.
- Facility interlocks are not part of your system unless directly connected.
- Your system must not defeat, bypass, or obscure facility radiation controls.

## 7.3 Example hazard register entry

| Field | Example |
|---|---|
| Hazard ID | H-EL-001 |
| Hazard | Electric shock from exposed mains inside rack |
| Cause | Rack panel removed while energised |
| Hazardous situation | Service engineer contacts live mains terminal |
| Existing controls | Enclosed mains wiring, PE bonding, warning labels |
| Severity | S4 |
| Probability before controls | P2 |
| Existing evidence | Rack photos, wiring diagram, PSU datasheets |
| Gap | Service procedure does not prohibit live access |
| Additional control | Add service isolation procedure and internal warning label |
| Verification | Service manual review; label inspection; PE continuity test |
| Residual risk | Acceptable for trained service personnel only |
| Status | Open / closed |

---

# 8. Perform the electrical safety architecture review

Call this:

> **SYS-SAF-003 — Electrical Safety Architecture Review**

This is probably the most important technical document.

## 8.1 Mains input review

Check:

- Mains inlet type and rating.
- Voltage and frequency rating.
- Fuse location.
- Fuse type.
- Fuse current rating.
- Fuse breaking capacity.
- Single-pole vs double-pole switching.
- Whether neutral/live polarity assumptions matter.
- Mains switch accessibility.
- Emergency disconnection method.
- Strain relief.
- Cable retention.
- Internal mains cable rating.
- Insulation temperature rating.
- Segregation from SELV wiring.
- Mains filter leakage current implications.

Evidence required:

- Datasheet for inlet/filter/switch.
- Wiring diagram.
- Fuse schedule.
- Internal photographs.
- Inspection record.
- Test record.

## 8.2 Protective earth and bonding review

This is crucial for a 19-inch rack/trolley.

Check:

- PE from inlet to chassis.
- Bonding to rack frame.
- Bonding to removable panels.
- Bonding to doors.
- Bonding to slide rails if conductive and accessible.
- Bonding to PSU chassis.
- Bonding to metal connector shells where required.
- Bonding continuity through painted/anodised surfaces.
- Use of serrated washers/star washers where necessary.
- Dedicated PE fasteners.
- Whether any PE fastener is shared with mechanical-only fixings.
- Cable screen terminations.
- Earth loops versus safety earth distinction.

Evidence required:

- PE/bonding drawing.
- Bonding point photos.
- Torque/fastener notes.
- PE continuity test.
- Build inspection checklist.

## 8.3 Internal power distribution

Check:

- AC distribution protection.
- DC rail protection.
- PSU approvals.
- PSU derating.
- Rail current limits.
- Wire gauge against maximum fault current.
- Fusing of branch circuits.
- Protection of harnesses leaving the rack.
- Accessibility of live terminals.
- Terminal block ratings.
- Ferrules/crimps.
- Cable management.
- Separation between mains and low-voltage circuits.

Create a **power tree**:

```text
230 V AC input
   |
   |-- Fuse / switch / filter
   |
   |-- PSU 1: +12 V
   |      |-- control electronics
   |      |-- fan / indicators
   |
   |-- PSU 2: +/- rails if applicable
   |      |-- analogue bias/control
   |
   |-- PSU 3: logic rail if applicable
          |-- PXI/interface electronics
```

For each rail define:

| Rail | Nominal voltage | Max current | Protection | Loads | Accessible? | Fault response |
|---|---:|---:|---|---|---|---|

## 8.4 Isolation and separation

Document:

- Where mains exists.
- Where isolated low voltage starts.
- PSU isolation boundary.
- Clearance/creepage confidence.
- Physical separation in rack.
- Cable routing.
- Connector separation.
- Barriers or covers.
- Whether any low-voltage output can become hazardous under single fault.

For retrospective work, you may not need to re-layout anything, but you do need evidence.

## 8.5 Accessible circuits

Classify all operator-accessible connections:

| Connector | Location | Signal type | Voltage | Current capability | User accessible? | Protection |
|---|---|---|---:|---:|---|---|

Include:

- Bias outputs.
- Trigger lines.
- Shutter lines.
- Fluence/dose count inputs.
- Event flag lines.
- LVDS/image data.
- Control I/O.
- External interlock lines if any.
- Ethernet/USB/Camera Link/CoaXPress if applicable.
- Service ports.

For each connector ask:

1. Can an operator touch it?
2. Can it be connected incorrectly?
3. Can it be connected to hazardous external equipment?
4. Can it overheat if shorted?
5. Is it labelled?
6. Is the mating cable keyed?
7. Is the cable safety-rated?
8. Is there strain relief?
9. Is shield termination intentional?
10. Is the safe state defined if disconnected?

## 8.6 DUT fixture and in-beam PCB

This is a special section.

The DUT side is probably low voltage, but it is externally located and exposed to abnormal conditions.

Check:

- Maximum voltage at fixture.
- Maximum available current.
- Current limiting.
- Bias shutdown threshold.
- Latch-up response.
- Short-to-shield behaviour.
- Short-to-adjacent-pin behaviour.
- Cable disconnection under power.
- Reverse connection risk.
- Connector keying.
- Exposed conductive surfaces.
- Touch accessibility during setup.
- Beamline access restrictions.
- Fixture earthing/bonding.
- Whether the fixture can float.
- Whether the cable screen is bonded at one end or both.
- Whether facility ground differences can create currents.
- Whether extension cables change safety assumptions.

For your system specifically, include radiation-induced events:

- Single-event latch-up.
- Transient current spike.
- Bias droop.
- Bias overcurrent.
- Sensor or board short after radiation damage.
- Data corruption causing false state reporting.

That does not mean IEC 61010 covers radiation physics directly. It means the electrical safety file should consider credible electrical consequences of testing irradiated electronics.

---

# 9. Produce a single-fault analysis

Call this:

> **SYS-SAF-004 — Normal Condition and Single-Fault Analysis**

The question is:

> Under credible single faults, does the system remain safe, or does a protective device operate before a hazardous condition persists?

## 9.1 Faults to assess

### Mains and power faults

- Live conductor short to chassis.
- Neutral open.
- Protective earth open.
- PSU primary-secondary fault.
- PSU output overvoltage.
- PSU output short.
- Fan failure.
- Fuse bypass/wrong fuse.
- Mains switch failure.
- Internal AC wire detached.

### DC output faults

- Bias output short to 0 V.
- Bias output short to adjacent bias.
- Bias output short to chassis/screen.
- Bias output open circuit.
- Bias output stuck high.
- Current-limit failure.
- DUT latch-up.
- Cable crushed.
- Cable disconnected under power.
- Cable misconnected.

### Control/data faults

- FPGA output stuck active.
- LabVIEW process crash.
- PXI controller reboot.
- RAM buffer overflow.
- Timestamp counter reset.
- Event trigger stuck high.
- Event trigger stuck low.
- Fluence count input stuck.
- Shutter status incorrect.
- Watchdog failure.
- Configuration file mismatch.

### Mechanical faults

- Rack wheel lock failure.
- Rack tipped over threshold.
- Cable strain relief failure.
- Fixture mounting loosens.
- Door/panel removed.

## 9.2 Single-fault analysis format

| Fault ID | Fault | Detection | Protection | Result | Safe? | Evidence |
|---|---|---|---|---|---|---|
| SF-001 | +12 V bias cable short to 0 V | PSU current limit / monitor flag | Current limit and shutdown | Output collapses, no overheating | TBD | Test required |
| SF-002 | FPGA trigger output stuck high | Software state check | Hardware output enable required | No unintended beam control if not connected to facility | Yes/TBD | Design review |
| SF-003 | PE bond to door open | None during use | Door not carrying hazardous live parts | Acceptable if no mains on door | TBD | Inspection/test |
| SF-004 | Fan blocked | Temperature rise | Thermal shutdown/derating | No fire hazard | TBD | Thermal test |

## 9.3 Important principle

Avoid relying on software as the only safety control.

Software can be used for monitoring, indication, logging, graceful shutdown, and test sequencing. But for fundamental electrical safety, prefer:

- Fuses.
- Current limiting.
- Isolation.
- Creepage/clearance.
- Protective earth.
- Mechanical barriers.
- Keyed connectors.
- Hardware interlocks.
- Watchdogs.
- Fail-safe default states.

---

# 10. Verification and test plan

Call this:

> **SYS-VER-001 — Retrospective Safety Verification Plan**

Split into four evidence classes.

## 10.1 Evidence classes

| Evidence class | Meaning |
|---|---|
| **Design review** | Evidence from drawings, schematics, datasheets, calculations |
| **Inspection** | Physical check of actual built system |
| **Bench test** | Test on the system or representative assembly |
| **External test** | Formal test-house assessment if required |

## 10.2 Minimum retrospective tests

For your system, I would expect at least:

### Electrical safety

- Protective earth continuity.
- Visual inspection of mains wiring.
- Fuse verification.
- Mains isolation review.
- Accessible voltage review.
- Accessible energy/current review.
- Internal wiring rating review.
- Output short-circuit test.
- Cable fault test.
- Power-up/power-down safe-state test.
- Power loss/recovery test.
- Leakage/touch-current assessment where applicable.
- Insulation/withstand testing where appropriate and safe for the equipment.

### Thermal

- Worst-case operating load.
- Enclosed rack operating condition.
- Fan operation check.
- Blocked vent consideration.
- PSU temperature margins.
- Cable temperature during fault-limited output.
- DUT latch-up/high-current condition.

### Mechanical

- Rack stability inspection.
- Wheel/castor/brake inspection.
- Panel security.
- Cable strain relief.
- Fixture stability.
- Sharp-edge inspection.
- Lifting/moving warnings.

### Functional safety behaviour

- Emergency stop or power-disconnect behaviour.
- Bias outputs off at startup unless deliberately enabled.
- Outputs off after software crash.
- Outputs off or known state after FPGA reset.
- No automatic unsafe restart after power recovery.
- Watchdog behaviour.
- Incorrect configuration detection.
- Event logging failure indication.

### Radiation-test-specific functional checks

- Bias current event flag captured.
- Shutter status captured.
- Fluence/dose count captured.
- Timestamp alignment checked.
- Event acknowledgement behaviour defined.
- Data buffer overflow behaviour defined.
- Loss of communication behaviour defined.
- DUT latch-up detection and response tested or simulated.

## 10.3 Test record format

Each test should have:

```text
Test ID:
Test title:
System configuration:
Hardware revision:
Software revision:
Operator:
Date:
Test equipment used:
Calibration status:
Preconditions:
Method:
Acceptance criteria:
Results:
Pass/fail:
Deviations:
Photos/data attached:
Reviewer:
```

## 10.4 Example test: output short-circuit

```text
Test ID: VER-DC-004
Title: Bias output short-circuit withstand test

Purpose:
To verify that a short circuit on a propagated low-voltage bias output does not create a hazardous condition, overheating, uncontrolled output, or damage that compromises safety.

Preconditions:
System configured with representative cable length and DUT/interface load removed or replaced with test fixture.

Method:
1. Enable relevant bias output under normal operating conditions.
2. Apply controlled short at remote fixture connector.
3. Observe current limit, output voltage, software indication, and recovery behaviour.
4. Maintain condition for defined duration or until protective action occurs.
5. Inspect cable, connector, PSU, and output driver after test.

Acceptance criteria:
- No accessible hazardous voltage.
- No smoke, fire, insulation damage, or excessive heating.
- Current limited by defined protective means.
- Operator indication/logging occurs if required.
- System recovers safely or requires deliberate reset.
```

## 10.5 Example test: power restoration

```text
Test ID: VER-FUNC-006
Title: Power interruption and restoration safe-state test

Purpose:
To verify that the system does not resume biasing, triggering, or test execution in an unsafe or unintended state after loss and restoration of mains power.

Method:
1. Configure system in an active test state.
2. Interrupt mains supply using normal disconnect method.
3. Restore mains supply.
4. Observe state of bias outputs, trigger outputs, shutter/event lines, software state, and logs.

Acceptance criteria:
- Outputs remain off or in a defined safe state.
- Test sequence does not automatically resume unless explicitly designed and justified.
- Operator is informed of interrupted run.
- Event/logging state is clear and not misleading.
```

---

# 11. Software, FPGA and logging safety review

Call this:

> **SYS-SW-001 — Control Software and Firmware Safety Review**

Your next-generation work has a strong event/timestamping angle, but even the current system should define what software does and does not do for safety.

## 11.1 Software boundary

Document:

- LabVIEW application role.
- PXI controller role.
- FPGA role.
- Hardware timebase role.
- RAM/circular-buffer role.
- Data logging role.
- Operator GUI role.
- Configuration-file role.
- Any watchdogs.
- Any remote-control functions.

## 11.2 Software safety classification

For each function, classify:

| Function | Safety relevance | Comment |
|---|---|---|
| Bias enable | Safety relevant | Can energise DUT/interface |
| Bias current monitoring | Safety relevant | Can detect latch-up/overcurrent |
| Event timestamping | Data integrity / test validity | Usually not direct electrical safety |
| Shutter status logging | Test validity / facility correlation | Could become safety relevant if linked to beam controls |
| Fluence count logging | Test validity | Not usually electrical safety |
| FPGA output control | Potentially safety relevant | Depends what outputs drive |
| GUI indication | Safety supporting | Should not be only safety barrier |
| Emergency shutdown | Safety critical if implemented | Prefer hardware-level shutdown |

## 11.3 Safe-state requirements

Define safe state clearly:

```text
The defined safe state shall be:
- Bias outputs disabled or current-limited to safe level.
- Trigger outputs inactive unless explicitly required otherwise.
- DUT/interface outputs placed in known inactive state.
- Test sequencing stopped.
- Operator notified of fault or interrupted state.
- Restart requires deliberate operator action.
```

## 11.4 Software failure modes

Assess:

- Application crash.
- PXI reboot.
- FPGA reset.
- Loss of comms.
- Buffer overflow.
- Disk full.
- Timebase lost.
- Event counter wraparound.
- Wrong sensor configuration loaded.
- Wrong cable length/delay compensation.
- Wrong current-threshold profile.
- LabVIEW front panel frozen.
- GUI shows stale status.
- Operator acknowledges event late.

## 11.5 Logging integrity

For your use case, logging is part of scientific validity and incident reconstruction.

Define:

- What is timestamped in hardware.
- What is timestamped in software.
- Timestamp resolution.
- Clock source.
- Run start reference.
- Event window definition.
- Pre-event/post-event buffer behaviour.
- Event acknowledgement behaviour.
- Whether data is written from RAM after event capture.
- What happens if PC/software asks for record after buffer wrap.
- How shutter, fluence, bias current and image data are correlated.

For next generation, this becomes a requirements set:

| Requirement | Example |
|---|---|
| Timebase | System shall use a common hardware timebase for event correlation |
| Event trigger | System shall capture pre/post-event data around a defined event t0 |
| Circular buffer | System shall maintain configurable pre-event history |
| Bias events | System shall timestamp current threshold events |
| Shutter state | System shall timestamp shutter open/closed transitions |
| Fluence pulses | System shall count and timestamp/aggregate fluence pulses |
| Data integrity | System shall indicate buffer overflow or missed events |
| Operator acknowledgement | System shall distinguish event occurrence time from acknowledgement time |

---

# 12. EMC and signal-integrity review

Call this:

> **SYS-EMC-001 — EMC and Signal Integrity Strategy**

This should sit beside the IEC 61010 file. EMC is not the same thing as electrical safety, but EMC faults can create unsafe or invalid behaviour.

## 12.1 EMC questions

Ask:

1. Is the system intended for industrial/lab use?
2. Are long cables connected to the DUT fixture?
3. Are cables routed near facility equipment?
4. Are there fast digital edges, LVDS, Camera Link, trigger lines, or PXI timing lines?
5. Could EMC upset cause outputs to enable?
6. Could EMC upset cause false event flags?
7. Could EMC upset corrupt image data only, without safety impact?
8. Are cable shields bonded consistently?
9. Are there filters on external interfaces?
10. Are there ESD controls at user-accessible connectors?

## 12.2 EMC evidence options

For retrospective uplift:

- Document cable shielding and grounding philosophy.
- Review enclosure continuity.
- Review external connector filtering.
- Review ESD exposure points.
- Check CE/UKCA status of bought-in PSUs/PXI modules.
- Capture operating experience from previous radiation campaigns.
- Define EMC test plan for next generation.
- Decide whether formal EMC testing is required for the current product claim.

## 12.3 Long propagation cable review

Because your system propagates signals/bias to a DUT fixture, create a specific cable document:

> **SYS-CAB-001 — Propagation Cable Safety and Integrity Review**

Include:

- Cable type.
- Length.
- Shielding.
- Twisted pairs.
- Ground/screen termination.
- Connector pinout.
- Maximum voltage.
- Maximum current.
- Fault current.
- Insulation rating.
- Bend radius.
- Strain relief.
- Beamline routing constraints.
- Extension-cable limits.
- Approved cable list.
- Do-not-use cable list.
- Labelling method.

---

# 13. Mechanical and rack/trolley review

Call this:

> **SYS-MECH-001 — Rack, Trolley and Mechanical Safety Review**

## 13.1 Rack checklist

Check:

- Rack height and centre of gravity.
- Heavy equipment mounted low.
- Castors rated.
- Brakes fitted and functional.
- Handles fitted if moved.
- No sharp edges.
- Covers secured.
- Panels require tool access if protecting hazardous areas.
- Ventilation not blocked.
- Cable exit points protected.
- Cable strain relief fitted.
- Rack cannot easily tip during normal use.
- Transport configuration defined.
- Maximum additional payload defined.
- Warning against moving while connected to beamline cables.

## 13.2 Fixture checklist

Check:

- DUT support fixture stability.
- Beamline mounting method.
- Cable strain relief at fixture.
- No exposed sharp pins.
- No accidental short risk.
- Insulating standoffs suitable.
- Exposed conductive parts bonded or justified as floating.
- Labelling visible during setup.
- Safe handling after irradiation covered by facility rules.

---

# 14. Labelling and markings

Call this:

> **SYS-LAB-001 — Marking and Warning Label Schedule**

## 14.1 Required label categories

Create labels for:

- Equipment name/model.
- Serial number.
- Manufacturer/supplier/internal owner.
- Rated input voltage.
- Rated frequency.
- Rated power/current.
- Fuse rating.
- Protective earth symbol.
- Mains disconnect instruction.
- Service access warning.
- Hazardous voltage warning inside rack.
- Low-voltage output connector labels.
- DUT/interface connector labels.
- Cable labels.
- “Trained personnel only” warning.
- Ventilation warning.
- Weight/movement warning if applicable.
- “Do not connect/disconnect under beamline operation” if applicable.
- “Use approved cable set only” if applicable.

## 14.2 Label schedule format

| Label ID | Text/symbol | Location | Size | Material | Drawing/photo ref |
|---|---|---|---|---|---|
| LAB-001 | Rated input label | Rear panel | TBD | Durable | Photo |
| LAB-002 | Fuse rating | Near inlet | TBD | Durable | Photo |
| LAB-003 | Hazardous voltage | Internal mains cover | TBD | Durable | Photo |
| LAB-004 | DUT bias output | Rear connector | TBD | Durable | Photo |

---

# 15. User manual and service manual uplift

You need both. Do not mix them.

## 15.1 Operator manual

Call this:

> **SYS-MAN-001 — Operator Manual**

Contents:

1. System overview.
2. Intended use.
3. User competence.
4. System boundary.
5. Major hazards.
6. Setup instructions.
7. Cable connection procedure.
8. DUT fixture connection procedure.
9. Pre-use inspection.
10. Power-on procedure.
11. Software startup.
12. Test configuration.
13. Bias enable procedure.
14. Radiation run procedure.
15. Event monitoring.
16. Fault indications.
17. Safe shutdown.
18. Emergency disconnection.
19. Cleaning.
20. Storage.
21. Approved accessories.
22. Prohibited use.
23. Troubleshooting.
24. Contact/service instructions.

## 15.2 Service manual

Call this:

> **SYS-MAN-002 — Service and Maintenance Manual**

Contents:

1. Service competence requirements.
2. Isolation procedure.
3. Stored-energy warning.
4. Rack access procedure.
5. Mains inspection.
6. PE bonding inspection.
7. Fuse replacement.
8. PSU replacement.
9. Cable inspection.
10. Fan/filter maintenance.
11. Firmware/software update.
12. Calibration/verification.
13. Post-service safety test.
14. Service record template.
15. Configuration-control rules.

## 15.3 Pre-use checklist

Example:

```text
Before use, the operator shall confirm:

[ ] Rack is physically stable.
[ ] Ventilation paths are clear.
[ ] Mains cable is undamaged.
[ ] Correct approved cable set is fitted.
[ ] DUT fixture is mechanically secure.
[ ] No exposed damaged conductors are visible.
[ ] Correct DUT configuration is loaded.
[ ] Bias outputs are off before connection.
[ ] Beamline/facility permission is in place.
[ ] Shutter/fluence/event inputs are connected as required.
[ ] Data logging path is available.
[ ] Emergency disconnect method is known.
```

## 15.4 Shutdown checklist

```text
[ ] Stop test sequence.
[ ] Disable bias outputs.
[ ] Confirm outputs off in software and/or hardware indicators.
[ ] Save run data.
[ ] Record abnormal events.
[ ] Power down rack if required.
[ ] Disconnect DUT/interface only when safe.
[ ] Follow facility rules for beamline access.
```

---

# 16. Build the Technical Construction File

Call this:

> **TCF-INDEX-001 — Technical Construction File Index**

Recommended structure:

```text
00_Admin
01_System_Overview
02_Intended_Use_and_Boundary
03_Applicable_Standards
04_Requirements
05_Design_Baseline
06_Risk_Assessment
07_Electrical_Safety
08_Single_Fault_Analysis
09_Software_and_Firmware
10_EMC_and_Signal_Integrity
11_Mechanical_Safety
12_Verification_and_Test
13_User_Service_Documentation
14_Manufacture_and_Configuration_Control
15_Gap_Register
16_Compliance_Summary
17_Next_Generation_Requirements
```

## 16.1 Document numbering

Use a clean numbering system:

| Prefix | Meaning |
|---|---|
| SYS-SAF | Safety documents |
| SYS-RISK | Risk assessment |
| SYS-COMP | Compliance documents |
| SYS-CFG | Configuration baseline |
| SYS-VER | Verification/test |
| SYS-SW | Software/firmware |
| SYS-EMC | EMC |
| SYS-CAB | Cable/interface |
| SYS-MECH | Mechanical |
| SYS-MAN | Manuals |
| SYS-GAP | Gap register |
| TCF | Technical file index/release |

## 16.2 TCF release rule

The file is not “released” until:

- Design baseline is frozen.
- Applicability matrix reviewed.
- Hazard register reviewed.
- Major safety gaps closed or formally accepted.
- Verification evidence attached.
- Manuals updated.
- Compliance summary written.
- Design authority signs off.
- Independent reviewer signs off if possible.

---

# 17. Gap register

Call this:

> **SYS-GAP-001 — Retrospective IEC 61010 Gap Register**

This is the action engine.

## 17.1 Gap types

| Gap type | Meaning | Example |
|---|---|---|
| Documentation gap | System is likely okay, but evidence missing | No PE bonding drawing |
| Verification gap | Needs test or inspection | No output short-circuit test |
| Design gap | Existing design may be inadequate | Unfused cable leaving rack |
| Process gap | Build/service process weak | No post-service safety test |
| Claim gap | Marketing/manual wording too strong | Says “certified” without evidence |

## 17.2 Gap register fields

| Field | Description |
|---|---|
| Gap ID | Unique identifier |
| Source | Risk assessment, 61010 matrix, test failure |
| Description | What is missing/wrong |
| Affected area | Mains, DC, cable, software, mechanical, manual |
| Risk | Low/medium/high |
| Required closure | Document/test/design change |
| Owner | Person/team |
| Due date | Target |
| Closure evidence | Report, photo, drawing, test |
| Residual risk | Accept/reject |
| Status | Open/closed |

## 17.3 Example gap entries

| Gap ID | Description | Type | Action |
|---|---|---|---|
| GAP-001 | No formal equipment boundary statement | Documentation | Create SYS-SAF-001 |
| GAP-002 | PE bonding path not shown on drawing | Documentation | Create bonding diagram |
| GAP-003 | No formal PE continuity record | Verification | Perform and record PE test |
| GAP-004 | External cable short-circuit behaviour undocumented | Verification | Test or calculate cable fault condition |
| GAP-005 | DUT latch-up response not specified | Design/process | Define threshold and shutdown action |
| GAP-006 | Service manual lacks isolation procedure | Documentation | Add service isolation section |
| GAP-007 | Software safe state not formally defined | Documentation/design | Add safe-state requirements |
| GAP-008 | Cable extension limits undefined | Process/design | Define approved cable lengths/configurations |
| GAP-009 | Label schedule missing | Documentation | Create marking schedule |
| GAP-010 | EMC evidence not structured | Documentation/test | Create EMC strategy |

---

# 18. Compliance review gates

Use gates to control the process.

## Gate 0 — Initiation

Entry criteria:

- Scope agreed.
- Claim level agreed.
- Responsible engineer assigned.
- Standards identified.

Exit criteria:

- Compliance strategy started.
- TCF structure created.
- Review team identified.

## Gate 1 — Design baseline freeze

Exit criteria:

- System configuration defined.
- Drawings gathered.
- Photos taken.
- BOM/cable schedule available.
- Software/firmware versions captured.
- Known variants listed.

## Gate 2 — Hazard review

Exit criteria:

- Hazard register created.
- Electrical, mechanical, thermal, software and cable hazards reviewed.
- Initial risk ranking completed.
- Obvious high-risk items escalated.

## Gate 3 — IEC 61010 gap assessment

Exit criteria:

- Applicability matrix complete.
- Evidence linked.
- Gaps classified.
- Required verification identified.

## Gate 4 — Verification

Exit criteria:

- Safety tests complete.
- Inspection records complete.
- Failures resolved or accepted.
- Test deviations recorded.
- Manuals updated from findings.

## Gate 5 — TCF release

Exit criteria:

- Compliance summary written.
- Residual risks accepted.
- Next-generation requirements extracted.
- Internal sign-off complete.
- Document pack controlled.

---

# 19. Specific focus areas for your system

For your rack, I would pay special attention to these.

## 19.1 Single 230 V AC input

Key questions:

- Is the mains inlet correctly rated?
- Is the fuse correct and documented?
- Is there one clear means of isolation?
- Is internal mains wiring segregated?
- Are all accessible metal parts bonded?
- Are removable rack panels bonded or not required to be?
- Are mains terminals finger-safe or covered?
- Is the mains earth path robust through the trolley?

## 19.2 Low-voltage DC generation

Key questions:

- Are all DC rails derived from approved isolated PSUs?
- Are outputs current limited?
- Are branch circuits protected?
- Can a low-voltage cable overheat under fault?
- Is overvoltage credible?
- What happens if a PSU fails high?
- Are tantalum/electrolytic capacitors correctly derated?
- Is inrush controlled?
- Are rail monitors safety-relevant or diagnostic only?

## 19.3 Propagation cables to beamline fixture

Key questions:

- Are cables part of the safety system?
- What is the maximum approved cable length?
- Are cable screens safety-bonded, EMC-bonded, or both?
- What happens under cable crush?
- What happens under wrong connector mating?
- What happens under partial insertion?
- What happens under extension cable use?
- Are cables labelled by function and revision?
- Is cable radiation suitability part of the design file?

## 19.4 DUT/interface PCB

Key questions:

- Is it touch-safe during setup?
- Are bias rails exposed?
- Is there a current limit per rail?
- Can radiation-induced latch-up cause overheating?
- Can the PCB carbonise or fail short?
- Does a failed DUT damage the rack?
- Is the support fixture insulating, grounded, or mixed?
- Is the fixture cleaned/handled under facility rules after exposure?

## 19.5 PXI/LabVIEW/FPGA subsystem

Key questions:

- Does it control anything safety-relevant?
- What happens if software crashes?
- What happens if FPGA resets?
- What is the hardware default output state?
- Does data logging failure stop the test or just flag invalid data?
- Are timestamps for test validity only, or used for protective action?
- Is circular-buffer behaviour defined?
- Is event t0 clearly defined?
- Are pre/post-event windows defined?
- Is acknowledgement time separate from event time?

---

# 20. Next-generation requirement extraction

Every retrospective gap should become a requirement candidate.

Call this:

> **SYS-NG-REQ-001 — Next-Generation Safety and Compliance Requirements Register**

## 20.1 Example next-generation requirements

| ID | Requirement |
|---|---|
| NG-SAF-001 | The system shall define the equipment safety boundary at concept design stage. |
| NG-SAF-002 | The system shall use a documented protective-earth bonding scheme for all accessible conductive parts. |
| NG-SAF-003 | All low-voltage outputs leaving the rack shall be current-limited or otherwise protected against cable faults. |
| NG-SAF-004 | The system shall define a safe state for power-up, power-down, software crash, FPGA reset, and communication loss. |
| NG-SAF-005 | The system shall prevent automatic re-energisation of DUT bias after unexpected power interruption unless explicitly justified. |
| NG-SAF-006 | All external cables shall have defined maximum length, pinout, rating, shielding, and approved part number. |
| NG-SAF-007 | DUT latch-up/high-current conditions shall be detected and placed into a defined response state. |
| NG-SAF-008 | Operator-accessible connectors shall be keyed, labelled, and assessed for misconnection. |
| NG-SAF-009 | Safety-relevant functions shall not rely solely on non-safety-rated software. |
| NG-SAF-010 | The TCF shall be created during design, not retrospectively after build. |

## 20.2 Metadata/timestamping requirements

From your previous direction, include:

| ID | Requirement |
|---|---|
| NG-DATA-001 | The system shall use a common hardware timebase for event correlation. |
| NG-DATA-002 | The system shall timestamp bias-current threshold events. |
| NG-DATA-003 | The system shall timestamp shutter open/closed transitions. |
| NG-DATA-004 | The system shall count fluence pulses and correlate them to run time. |
| NG-DATA-005 | The system shall distinguish event occurrence time from operator acknowledgement time. |
| NG-DATA-006 | The system shall provide configurable pre-event and post-event capture windows. |
| NG-DATA-007 | The system shall define buffer overflow behaviour and flag invalid/missing data. |
| NG-DATA-008 | The system shall record hardware, software, firmware and configuration versions for each run. |

---

# 21. Final compliance summary

Call this:

> **SYS-COMP-003 — Retrospective IEC 61010 Compliance Summary**

This is the final management-facing document.

## 21.1 Recommended structure

1. System description.
2. Assessment scope.
3. Standards considered.
4. Equipment boundary.
5. Intended use.
6. Summary of risk assessment.
7. Summary of electrical safety review.
8. Summary of software/control review.
9. Summary of EMC strategy.
10. Verification evidence summary.
11. Open gaps.
12. Residual risks.
13. Restrictions/conditions of use.
14. Compliance statement.
15. Next-generation recommendations.
16. Approvals.

## 21.2 Example final wording

Use something like:

> The current radiation image-sensor characterisation rack has been retrospectively reviewed against the applicable requirements and principles of IEC 61010-1 for electrical equipment for measurement, control and laboratory use. Particular attention has been given to the 230 V AC mains input, protective earthing, internal power distribution, low-voltage output circuits, propagated DUT/interface cabling, operator access, service access, software-controlled operating states, and credible single-fault conditions.
>
> The review identified documentation, verification and design-control actions, which have been captured in the gap register. Where evidence is available, it has been indexed into the Technical Construction File. Where evidence is incomplete, additional inspection, test, design review or risk acceptance is required.
>
> This review supports an internal engineering position of IEC 61010-aligned design assurance. It does not constitute formal third-party certification unless separately assessed by an accredited body.

---

# 22. Practical execution order

Do it in this order.

## Week/process block 1 — Set the frame

1. Create TCF folder structure.
2. Write equipment boundary statement.
3. Write intended-use statement.
4. Define claim level.
5. Create document register.
6. Freeze design baseline.
7. Photograph the system comprehensively.

## Week/process block 2 — Build the evidence map

1. Gather drawings.
2. Gather BOMs.
3. Gather PSU datasheets.
4. Gather cable drawings.
5. Gather software/firmware versions.
6. Create power tree.
7. Create connector schedule.
8. Create safety-critical parts list.

## Week/process block 3 — Risk and gap review

1. Run hazard workshop.
2. Populate hazard register.
3. Populate IEC 61010 applicability matrix.
4. Identify documentation gaps.
5. Identify verification gaps.
6. Identify possible design gaps.
7. Prioritise high-risk actions.

## Week/process block 4 — Verification

1. Perform PE continuity checks.
2. Perform visual wiring inspection.
3. Verify fuses and ratings.
4. Test output short-circuit behaviour.
5. Test power loss/recovery behaviour.
6. Test software/FPGA safe states.
7. Perform thermal/load checks.
8. Record all evidence.

## Week/process block 5 — Manual and process uplift

1. Rewrite operator manual.
2. Write service manual.
3. Create pre-use checklist.
4. Create post-service checklist.
5. Create label schedule.
6. Update cable-use instructions.
7. Define approved configurations.

## Week/process block 6 — Close and release

1. Close gap register.
2. Accept residual risks.
3. Write compliance summary.
4. Extract next-generation requirements.
5. Hold final design/safety review.
6. Release TCF baseline.

---

# 23. The core documents to create first

Start with these five. They will steer everything else.

1. **SYS-SAF-001 — Equipment Boundary and Intended Use**
2. **SYS-CFG-001 — Current System Design Baseline**
3. **SYS-RISK-001 — Hazard Analysis and Risk Register**
4. **SYS-COMP-002 — IEC 61010 Applicability and Gap Matrix**
5. **SYS-VER-001 — Retrospective Safety Verification Plan**

Once those exist, the rest becomes evidence collection and closure.

---

# 24. My recommended top-level action plan

## Phase A — Definition

Define exactly what the system is, what it does, where it is used, who uses it, and what is inside/outside the safety boundary.

## Phase B — Baseline

Freeze one representative configuration and collect all design evidence against that configuration.

## Phase C — Hazard review

Perform a structured hazard review covering electrical, fire, thermal, mechanical, software/control, cable, DUT, and beamline-interface hazards.

## Phase D — IEC 61010 mapping

Create a clause/topic applicability matrix against IEC 61010-1, with screening of 61010-2-030 for external DUT/test circuits.

## Phase E — Verification

Turn all assumptions into evidence: inspection, calculation, bench test, or formal external test where needed.

## Phase F — Documentation uplift

Restructure the data pack into a controlled Technical Construction File with manuals, labels, drawings, test records, and risk evidence.

## Phase G — Gap closure

Close documentation gaps, verification gaps, and design gaps separately. Do not treat all gaps as hardware problems.

## Phase H — Internal statement

Issue a careful internal compliance summary that says what has been reviewed, what evidence exists, what remains open, and what claim is justified.

## Phase I — Next-generation capture

Convert every retrospective weakness into a clean requirement for the next architecture.

---

The strongest move is to **not start by rewriting everything**. Start by creating the **boundary statement, design baseline, hazard register, and IEC 61010 gap matrix**. Those documents become the steering wheel for the entire uplift.

[M9] ME (2026-07-04 11:18):
Are you able to generate an SVG diagram for a document tree?

[M10] AI (2026-07-04 11:17):
Yes. I can generate a clean, editable **SVG document-tree diagram** based on the Technical Construction File hierarchy above, suitable for inserting into Word, PowerPoint, Visio, or a controlled engineering document.

It could show:

- **Technical Construction File** as the root.
- Main folders such as System Overview, Standards, Risk Assessment, Electrical Safety, Verification, Manuals, and Compliance Summary.
- Key documents beneath each folder.
- Document identifiers such as `SYS-SAF-001`.
- Optional status indicators for existing, missing, draft, or complete documents.
- A landscape or portrait layout with either a classic hierarchy tree or a folder-style structure.

A sensible first version would use the `00_Admin` to `17_Next_Generation_Requirements` hierarchy from the manual, with the principal controlled documents shown below each branch.

[M11] ME (2026-07-04 11:21):
yes

[M12] AI (2026-07-04 11:20):
I’m building a landscape SVG that mirrors the full `00_Admin` to `17_Next_Generation_Requirements` structure, with grouped branches and document identifiers so it can drop straight into the technical file.

[M13] AI (2026-07-04 11:20):
The first export hit a tooling error rather than a diagram issue. I’m regenerating it directly as a standards-friendly SVG file, with a PNG preview alongside it.

[M14] AI (2026-07-04 11:21):
Completed the full Technical Construction File document tree.

[Download the editable SVG](sandbox:/mnt/data/IEC_61010_TCF_Document_Tree.svg)

[View/download the PNG preview](sandbox:/mnt/data/IEC_61010_TCF_Document_Tree_Preview.png)

The SVG includes all folders from `00_Admin` through `17_Next_Generation_Requirements`, grouped into:

- Governance and system definition
- Safety assurance and verification
- Release, operation and future requirements

[M15] ME (2026-07-06 20:29):
Produce an FMEA template that will work well with the standard

[M16] AI (2026-07-06 20:29):
For an IEC 61010 project, I would actually recommend **not using a traditional automotive AIAG FMEA**. It tends to become overly manufacturing-focused and doesn't map particularly well to laboratory and test equipment.

Instead, I would build what I call a **Safety Design FMEA (SDFMEA)**. It combines:

- IEC 61010 hazard thinking
- Functional FMEA
- System FMEA
- Single Fault Condition analysis
- Verification traceability

into a single document.

This then becomes one of the principal documents within the Technical Construction File.

---

# Document Header

**Document No:** SYS-RISK-002

**Title:** Safety Design Failure Mode and Effects Analysis (SDFMEA)

| Item | Value |
|---------|----------|
| System | Radiation Image Sensor Test System |
| Assembly | Complete Test System |
| Revision | |
| Date | |
| Prepared by | |
| Reviewed by | |
| Approved by | |
| Applicable Standards | IEC 61010-1, IEC 61010-2-030, IEC 61326 |
| Configuration Baseline | |

---

# Section 1 — Item Under Review

| Field | Description |
|------------|----------------|
| Assembly |
| Subsystem |
| Drawing Number |
| PCB Revision |
| Software Revision |
| Firmware Revision |
| Cable Set |
| Function |
| Safety Classification |

---

# Section 2 — Functional Description

Describe exactly what the item is intended to do.

Example

> Provides isolated +12 V sensor bias to the DUT through the propagation cable whilst monitoring current consumption and overcurrent events.

---

# Section 3 — Functional Requirements

| Req ID | Requirement |
|-----------|----------------|
| SAF-001 | Output shall never exceed 12.5 V |
| SAF-002 | Output current shall be limited to 500 mA |
| SAF-003 | Output shall switch OFF during emergency stop |
| SAF-004 | Reverse polarity shall not damage equipment |

---

# Section 4 — FMEA

This is the heart of the document.

| ID | Function | Failure Mode | Failure Cause | Local Effect | System Effect | Safety Effect | Detection Method | Existing Controls | Severity | Occurrence | Detection | Risk | Verification | Residual Risk | Action Required | Owner | Status |

This is considerably more useful than the normal AIAG layout.

---

## Example

|ID|Function|Failure Mode|Cause|System Effect|Safety Effect|
|---|---|---|---|---|---|
|F001|Generate Bias|Bias too high|Regulator failure|Sensor damage|Possible overheating|
|F002|Generate Bias|Bias OFF|Fuse open|Test aborts|Safe|
|F003|Generate Bias|Bias oscillates|Poor compensation|Image corruption|No direct safety issue|
|F004|Current Monitor|Fails Low|ADC failure|Latch-up missed|Potential overheating|
|F005|Current Monitor|Fails High|Calibration error|False shutdown|Safe but nuisance|

---

# Section 5 — Safety Analysis

This section does not exist in conventional FMEA but should.

| Hazard ID | Hazard | Failure Modes Contributing | Existing Mitigation | Additional Mitigation |
|----------------|----------------|-----------------------|---------------------|---------------------|

Example

|H-001|Electric shock|F021,F022|Double insulation|None|
|H-004|Fire|F001,F007|Current limiting|Thermal fuse|

---

# Section 6 — IEC 61010 Mapping

This is extremely useful.

| IEC Clause | Requirement | Failure Modes |
|----------------|----------------------|----------------|
|Protection against electric shock|PE failure|F021,F022|
|Mechanical hazards|Rack instability|F090|
|Temperature|Fan failure|F042|
|Fire|Overcurrent|F001|

This gives traceability directly into the standard.

---

# Section 7 — Single Fault Condition Review

One of the major concepts within IEC61010.

| Fault | Expected Behaviour | Actual Behaviour | Acceptable |
|-------------|----------------------|--------------------|-------------|

Examples

Loss of PE

Loss of mains

PSU overvoltage

Fan stopped

Cable short

Cable open circuit

Cable crushed

FPGA halted

Software crash

Power interruption

Power restored

Sensor latch-up

Current monitor failed

Emergency stop operated

---

# Section 8 — Verification Evidence

| Test | Procedure | Result | Report |
|-----------|----------------|-------------|------------|

Examples

Earth continuity

Short circuit

Power cycling

Dielectric

Temperature rise

Cable fault

Overcurrent

Safe startup

Safe shutdown

---

# Section 9 — Residual Risk Assessment

| Hazard | Remaining Risk | Justification | Acceptable |
|----------------|----------------|----------------|---------------|

---

# Section 10 — Improvement Register

Instead of having actions hidden inside the FMEA, keep them here.

| Action ID | Origin | Description | Priority | Status |
|----------------|--------------|----------------|------------|-------------|

---

# Severity Scale

| Score | Meaning |
|---------|-------------|
|1|No effect|
|2|Cosmetic|
|3|Minor inconvenience|
|4|Reduced performance|
|5|Test interrupted|
|6|Equipment damage|
|7|Potential overheating|
|8|Fire possible|
|9|Electric shock possible|
|10|Serious injury or fatality|

---

# Occurrence Scale

| Score | Meaning |
|---------|-------------|
|1|Extremely unlikely|
|2|Remote|
|3|Low|
|4|Occasional|
|5|Moderate|
|6|Known issue|
|7|Likely|
|8|Frequent|
|9|Very frequent|
|10|Almost certain|

---

# Detection Scale

| Score | Meaning |
|---------|-------------|
|1|Automatically prevented|
|2|Automatically detected|
|3|Hardware monitor|
|4|Software monitor|
|5|Operator warning|
|6|Routine inspection|
|7|Manual testing|
|8|Customer likely to find|
|9|Very difficult|
|10|Undetectable|

---

# Risk Priority

Rather than relying solely on the traditional **Risk Priority Number (RPN = Severity × Occurrence × Detection)**, which is increasingly discouraged as the only decision metric, I recommend using both:

- **Risk Level** (Critical / High / Medium / Low), based on engineering judgement and IEC 61010 safety impact.
- **RPN** as a supporting prioritisation metric.

For example:

| RPN | Typical Action |
|------:|----------------|
| 1–40 | Accept or monitor |
| 41–100 | Review and improve where practical |
| 101–200 | Corrective action required |
| >200 | Unacceptable until mitigated |

## Why this works well for IEC 61010

This structure integrates the elements that IEC 61010 expects you to demonstrate across the technical file:

- **Function** → what the subsystem is intended to do.
- **Failure mode** → what can go wrong.
- **Hazard** → how that failure could create a hazardous situation.
- **Protective measure** → how the design prevents or limits the hazard.
- **Verification** → objective evidence that the protective measure works.
- **Residual risk** → what remains after all design controls are applied.
- **Traceability** → direct links to applicable IEC 61010 clauses and your verification reports.

For your radiation test system, this template will work particularly well because it naturally accommodates both **electrical safety** (mains input, protective earthing, power distribution, isolation, propagation cables) and **mission-specific functional failures** (sensor bias, latch-up detection, shutter status, fluence counting, timestamping, FPGA control, and long-cable interfaces) within a single, controlled engineering document. It also becomes reusable for the next-generation platform, allowing most of the structure to be retained while only the subsystem analyses need updating.

[M17] ME (2026-07-06 20:34):
Do the same for a safety document

[M18] AI (2026-07-06 20:34):
For IEC 61010, I would make the **Safety Case** the highest-level engineering document in the Technical Construction File. Everything else (FMEA, risk assessment, verification, manuals, etc.) feeds into it.

Rather than a simple "Safety Document", I recommend producing a **System Safety Case** that demonstrates, with evidence, why the equipment is safe for its intended use.

Think of it as the document that answers one question:

> **"Why should someone believe this equipment is safe?"**

Everything else simply provides evidence for that argument.

---

# Document Header

**Document Number:** SYS-SAF-000

**Title:** System Safety Case

| Field | Value |
|---------|----------|
| System | Radiation Image Sensor Characterisation System |
| Configuration | |
| Revision | |
| Prepared by | |
| Reviewed by | |
| Approved by | |
| Date | |
| Standards | IEC 61010-1, IEC 61010-2-030, IEC 61326 |
| Status | Draft / Released |

---

# Revision History

| Rev | Date | Description | Author |
|------|------|------------|----------|

---

# Contents

1. Purpose
2. Scope
3. Applicable Standards
4. Safety Philosophy
5. System Description
6. Equipment Boundary
7. Intended Use
8. Reasonably Foreseeable Misuse
9. Operating Environment
10. Safety Objectives
11. Hazard Identification
12. Risk Assessment
13. Safety Functions
14. Protective Measures
15. Single Fault Analysis
16. Verification Strategy
17. Residual Risk
18. Operational Safety
19. Maintenance Safety
20. Compliance Assessment
21. Open Items
22. Conclusions

---

# 1 Purpose

Describe why this document exists.

Example

> This document presents the safety case for the Radiation Image Sensor Characterisation System and demonstrates that the system has been designed, assessed, verified and documented against the applicable requirements of IEC 61010 for laboratory and test equipment.

---

# 2 Scope

Exactly define the equipment.

Include

- Rack
- Power entry
- Power supplies
- PXI
- FPGA
- LabVIEW software
- Cabling
- Beamline interface
- DUT fixture
- Support equipment

Also define what is NOT included.

---

# 3 Applicable Standards

Table

| Standard | Purpose | Applicable |
|------------|-------------|---------------|
| IEC 61010-1 | General Safety | Yes |
| IEC 61010-2-030 | Measuring Circuits | Yes |
| IEC 61326 | EMC | Yes |

---

# 4 Safety Philosophy

One of the most important sections.

State the engineering philosophy.

For example

The system shall be safe by design through

- Isolation
- Protective earthing
- Current limiting
- Energy limitation
- Mechanical protection
- Hardware protection
- Fail-safe operation
- Controlled software
- Verification
- Risk reduction

Avoid dependence on procedural controls wherever practical.

---

# 5 System Description

High-level description.

Include

Purpose

Architecture

Subsystems

Power flow

Signal flow

Operator interface

Beamline interface

---

# 6 Equipment Boundary

This should include a large figure.

Define

Inside boundary

Outside boundary

User interfaces

Electrical interfaces

Mechanical interfaces

Facility interfaces

---

# 7 Intended Use

Professional laboratory equipment.

Heavy ion image sensor characterisation.

Trained personnel only.

Indoor use.

Controlled environment.

---

# 8 Foreseeable Misuse

Examples

Wrong mains voltage

Damaged cable

Wrong connector

Moving rack while powered

Incorrect fuse

Connecting external supplies

Incorrect software configuration

Operating with covers removed

Blocked ventilation

Damaged DUT

Extension cable

---

# 9 Operating Environment

Electrical

Mechanical

Temperature

Humidity

EMC

Radiation facility

Storage

Transport

---

# 10 Safety Objectives

Instead of hazards first, define objectives.

Example

SO-001

Prevent electric shock.

SO-002

Prevent fire.

SO-003

Prevent excessive temperatures.

SO-004

Prevent hazardous output energy.

SO-005

Maintain protective earthing.

SO-006

Prevent unsafe restart.

SO-007

Prevent unsafe maintenance.

SO-008

Prevent cable hazards.

SO-009

Prevent mechanical instability.

SO-010

Protect DUT from abnormal outputs.

---

# 11 Hazard Identification

This should become a master hazard log.

| Hazard ID | Hazard | Cause | Severity | Initial Risk |

Categories

Electrical

Thermal

Mechanical

Software

Power

EMC

Cable

Radiation Interface

Human Factors

Maintenance

Transportation

---

# 12 Risk Assessment

Reference

SYS-RISK-001

Summarise

High risks

Medium risks

Residual risks

Accepted risks

---

# 13 Safety Functions

A really important section.

List every safety function.

| ID | Safety Function | Implemented By |
|---------|---------------------|--------------------|

Examples

SF001

Protective earth

SF002

Current limiting

SF003

Fuse protection

SF004

Power isolation

SF005

Output shutdown

SF006

Temperature protection

SF007

Emergency shutdown

SF008

Cable protection

SF009

Operator warning

SF010

Software watchdog

---

# 14 Protective Measures

Organise according to hierarchy.

## Inherently Safe Design

Isolation

SELV

Current limiting

Component derating

Mechanical layout

## Protective Measures

Fuses

Earth

Barriers

Enclosure

Labels

Interlocks

Watchdogs

## Information for Use

Manual

Warnings

Labels

Training

Maintenance

---

# 15 Single Fault Analysis

One chapter for each fault.

Example

Loss of Earth

Expected behaviour

Observed behaviour

Verification

Conclusion

Repeat for

PSU failure

Fuse failure

Cable short

Cable open

Power loss

Power restoration

Software crash

FPGA halt

Current monitor failure

Cooling failure

---

# 16 Verification Strategy

Reference every verification document.

Inspection

Electrical tests

Thermal

Mechanical

Software

Functional

Safety

EMC

Each should have

Procedure

Acceptance Criteria

Report

Result

---

# 17 Evidence Matrix

This is something many safety files miss.

| Safety Requirement | Evidence |
|-------------------------|----------------|

Example

Protective Earthing

Earth continuity report

Cable protection

Cable fault test

Output safety

Short circuit report

Software startup

Verification report

Thermal safety

Temperature report

Every safety claim should point to objective evidence.

---

# 18 Operational Safety

Operator responsibilities.

Pre-use inspection.

Startup.

Shutdown.

Emergency.

Fault reporting.

Safe handling of DUT.

---

# 19 Maintenance Safety

Isolation procedure.

Stored energy.

Fuse replacement.

PSU replacement.

Inspection intervals.

Post maintenance testing.

Configuration control.

---

# 20 Compliance Assessment

Instead of saying

"It complies"

Summarise

Applicable clauses

Evidence

Gaps

Open items

Justifications

Future improvements

---

# 21 Open Items

This is extremely useful.

| ID | Description | Risk | Planned Closure |

---

# 22 Conclusions

Management summary.

Should answer

Is the system safe?

Is residual risk acceptable?

Are outstanding actions acceptable?

Can the equipment be released?

---

# Appendix A

Equipment photographs.

---

# Appendix B

Architecture drawings.

---

# Appendix C

Power tree.

---

# Appendix D

Protective Earth diagram.

---

# Appendix E

Cable schedule.

---

# Appendix F

Connector schedule.

---

# Appendix G

Software architecture.

---

# Appendix H

Verification reports.

---

# Appendix I

Risk Register.

---

# Appendix J

FMEA.

---

# Appendix K

IEC 61010 Clause Matrix.

---

# Appendix L

Safety Requirements Traceability Matrix.

---

# Safety Argument Structure

To make the document particularly robust, I recommend organising it around a clear **claim–argument–evidence** structure. Every major section should answer three questions:

| Claim | Argument | Evidence |
|--------|----------|----------|
| The system is electrically safe. | Protective earthing, isolation, current limiting, enclosure design, and fault protection prevent hazardous accessible energy. | Earth continuity test, insulation review, PSU approvals, wiring inspection, short-circuit tests. |
| The system is safe under single-fault conditions. | Credible electrical, mechanical, and control faults have been analysed and mitigated. | Single-fault analysis, FMEA, verification reports. |
| Residual risks are acceptable. | Remaining risks have been reduced as far as reasonably practicable and are communicated to users where necessary. | Risk register, operator manual, warning labels, maintenance procedures. |

This transforms the document from a collection of safety information into a **structured engineering safety case**, where every assertion is supported by traceable evidence. It also scales naturally to your next-generation platform, allowing new hardware and software to inherit the same safety argument while updating only the supporting evidence.

[M19] ME (2026-07-06 20:37):
Now for an ICD

[M20] AI (2026-07-06 20:37):
For your system, the **Interface Control Document (ICD)** should be one of the most important documents in the Technical Construction File. In a complex radiation test system, the majority of integration problems occur at interfaces rather than within individual subsystems. A well-written ICD becomes the single source of truth for electrical, mechanical, software, and operational interfaces.

Rather than creating separate ICDs for every interface, I recommend a **Master Interface Control Document** with interface-specific appendices. This approach is common in aerospace and defence projects and fits well with a mature IEC 61010 technical file.

---

# Document Header

**Document Number:** SYS-ICD-001

**Title:** Master Interface Control Document

| Field | Value |
|--------|-------|
| System | Radiation Image Sensor Characterisation System |
| Document Number | SYS-ICD-001 |
| Revision | |
| Configuration Baseline | |
| Prepared by | |
| Reviewed by | |
| Approved by | |
| Date | |
| Related Standards | IEC 61010-1, IEC 61326 |

---

# Revision History

| Rev | Date | Description | Author |

---

# Contents

1. Purpose
2. Scope
3. Interface Philosophy
4. System Interface Overview
5. Interface Register
6. Mechanical Interfaces
7. Electrical Interfaces
8. Signal Interfaces
9. Timing Interfaces
10. Software Interfaces
11. Data Interfaces
12. Communication Interfaces
13. Safety Interfaces
14. Human Interfaces
15. Environmental Interfaces
16. Verification Requirements
17. Interface Change Control
18. Appendices

---

# 1 Purpose

Define the purpose of the document.

Example:

> This document defines every external and internal interface within the Radiation Image Sensor Characterisation System to ensure compatibility, safety, maintainability and controlled configuration throughout the equipment lifecycle.

---

# 2 Scope

Clearly state what is included.

Include:

- Rack
- PXI chassis
- FPGA
- Host PC
- DUT interface PCB
- Beamline fixture
- Propagation cable
- Power supplies
- Operator controls
- Emergency stop
- Facility interfaces

Exclude:

- Customer DUT internals
- Beamline equipment
- Radiation source

---

# 3 Interface Philosophy

Describe the engineering rules.

Examples:

- Every interface shall have one owner.
- Every connector shall be uniquely identified.
- Every signal shall have one defined source.
- Every cable shall have a controlled drawing.
- Every interface shall be electrically compatible.
- Safety functions shall not rely on undocumented interfaces.
- All interface changes require configuration control.

---

# 4 System Interface Overview

Provide a high-level block diagram.

Example:

```text
230 Vac
   │
Power Entry
   │
Power Supplies
   │
PXI Controller
   │
FPGA
   │
Interface PCB
   │
Propagation Cable
   │
Fixture PCB
   │
Image Sensor
```

This section should also include:

- Power flow
- Data flow
- Timing flow
- Safety-related signals

---

# 5 Interface Register

The master index.

| Interface ID | Name | Type | Source | Destination | Drawing |
|--------------|------|------|--------|-------------|---------|

Example:

| IF-001 | Mains Input | Electrical | Facility | Rack | DWG-101 |
| IF-002 | Ethernet | Data | PC | PXI | DWG-210 |
| IF-003 | Trigger | Digital | FPGA | DUT | DWG-350 |

---

# 6 Mechanical Interfaces

For each mechanical interface:

| Item | Description |
|------|-------------|
| Interface ID | |
| Assembly | |
| Drawing | |
| Mounting Method | |
| Fasteners | |
| Materials | |
| Torque Values | |
| Alignment Requirements | |
| Clearance Requirements | |
| Weight Limits | |
| Service Access | |

---

# 7 Electrical Interfaces

One section for every electrical interface.

| Parameter | Value |
|-----------|-------|
| Interface ID | |
| Connector | |
| Pin Count | |
| Pinout | |
| Voltage | |
| Current | |
| Maximum Power | |
| Isolation | |
| Protective Earth | |
| Fuse | |
| Cable Length | |
| Cable Type | |
| Shielding | |

---

# 8 Signal Interfaces

For every signal.

| Signal | Description |
|---------|-------------|
| Signal Name | |
| Source | |
| Destination | |
| Direction | |
| Voltage Levels | |
| Logic Family | |
| Rise/Fall Time | |
| Maximum Frequency | |
| Timing Accuracy | |
| Propagation Delay | |
| Loading | |
| Termination | |
| Fail State | |

For your system, include:

- Trigger outputs
- Exposure shutter
- Latch-up flags
- Current monitor signals
- Dose counter
- Timestamp trigger
- Safety interlocks
- Emergency stop inputs

---

# 9 Timing Interfaces

A dedicated chapter for timing is valuable because your system relies on precise synchronisation.

| Parameter | Requirement |
|-----------|-------------|
| Clock Frequency | |
| Clock Source | |
| Jitter | |
| Phase Error | |
| Synchronisation Method | |
| Trigger Latency | |
| Timestamp Resolution | |
| Pulse Width | |
| Maximum Drift | |

Include timing diagrams where appropriate.

---

# 10 Software Interfaces

Describe:

- Host PC software
- FPGA firmware
- Driver APIs
- Configuration files
- State machines
- Error reporting
- Event logging

For each interface:

| Interface | Description |
|-----------|-------------|
| API | |
| Protocol | |
| Commands | |
| Responses | |
| Error Codes | |
| Timeout | |

---

# 11 Data Interfaces

Define every logged parameter.

| Parameter | Units | Resolution | Update Rate | Source |
|-----------|-------|------------|-------------|--------|

For example:

- Sensor bias voltage
- Bias current
- Latch-up count
- Temperature
- Shutter status
- Dose count
- FPGA status
- Timestamp
- Fault flags

---

# 12 Communication Interfaces

For each communications link:

| Parameter | Value |
|-----------|-------|
| Protocol | |
| Speed | |
| Connector | |
| Cable | |
| Packet Structure | |
| Error Detection | |
| Retry Mechanism | |
| Timeout | |

Examples:

- Ethernet
- USB
- PXI backplane
- SPI
- I²C
- UART

---

# 13 Safety Interfaces

These deserve a dedicated section because they are critical to the IEC 61010 safety case.

For each safety-related interface:

| Parameter | Description |
|-----------|-------------|
| Safety Function | |
| Interface ID | |
| Hazard Controlled | |
| Safe State | |
| Failure Response | |
| Verification Reference | |

Examples:

- Protective earth
- Emergency stop
- Mains isolation
- Power inhibit
- Over-current shutdown
- Fan failure indication
- Door interlock (if applicable)

---

# 14 Human Interfaces

Document all operator interactions.

Include:

- Switches
- Push-buttons
- Indicator LEDs
- Displays
- Labels
- Software controls
- Audible alarms

For each item:

| Item | Requirement |
|------|-------------|
| Identifier | |
| Function | |
| Normal State | |
| Fault Indication | |
| Safety Relevance | |

---

# 15 Environmental Interfaces

Capture the operating environment and facility dependencies.

Include:

- Mains supply
- Ambient temperature
- Humidity
- Cooling airflow
- Laboratory earth
- Radiation beamline
- Network connection
- Floor loading
- Transport constraints

---

# 16 Verification Requirements

Every interface should have a verification method.

| Interface | Inspection | Test | Analysis | Demonstration | Acceptance Criteria |
|-----------|------------|------|----------|---------------|---------------------|

---

# 17 Interface Change Control

Document how interface changes are managed.

For every change:

| Change ID | Interface | Reason | Impact Assessment | Approval | Implemented |
|-----------|-----------|--------|-------------------|----------|-------------|

This ensures changes are traceable and assessed for impacts on safety, functionality, and compatibility.

---

# Appendix A – Connector Register

A complete list of all connectors, keyed to drawings and cable assemblies.

---

# Appendix B – Cable Schedule

Cable identifiers, lengths, shielding, routing, and part numbers.

---

# Appendix C – Pin Assignment Tables

Detailed pinouts for every connector.

---

# Appendix D – Signal Dictionary

Definitions of every signal, including naming conventions, electrical characteristics, and functional descriptions.

---

# Appendix E – Timing Diagrams

Clock, trigger, acquisition, and synchronisation diagrams.

---

# Appendix F – Communication Protocols

Packet structures, command sets, message formats, and error handling.

---

# Appendix G – Interface Verification Matrix

Cross-reference every interface to its verification evidence and related requirements.

---

## Why this structure suits your system

Given the complexity of your radiation test platform—with long propagation cables, PXI hardware, FPGA control, precision timing, DUT interface boards, beamline integration, and extensive metadata logging—the ICD becomes more than a connector document. It becomes the definitive integration specification.

When used alongside your **System Requirements Specification**, **System Architecture Document**, **Safety Case**, **FMEA**, and **Verification & Validation Plan**, this ICD provides complete traceability from system requirements, through interface design, to verification evidence and configuration control. It will also serve as the baseline against which the next-generation architecture can evolve while preserving compatibility and maintaining compliance with your overall IEC 61010 technical construction file.

[M21] ME (2026-07-06 20:41):
Now architecture

[M22] AI (2026-07-06 20:41):
For your project, the **System Architecture Description (SAD)** should be the cornerstone of the Technical Construction File. If someone new joined the project and was given only one technical document to understand how the system works, this should be it.

Unlike the ICD, which defines **how components connect**, the Architecture Document explains **why the system is partitioned as it is, how information and energy flow, and how the design satisfies the system requirements and safety objectives**.

I would treat this as a Level 1 design document that sits directly below the System Requirements Specification and above the detailed hardware, software, FPGA, and interface designs.

---

# Document Header

**Document Number:** SYS-ARCH-001

**Title:** System Architecture Description

| Field | Value |
|--------|-------|
| System | Radiation Image Sensor Characterisation System |
| Document Number | SYS-ARCH-001 |
| Revision | |
| Configuration Baseline | |
| Prepared by | |
| Reviewed by | |
| Approved by | |
| Applicable Standards | IEC 61010-1, IEC 61326 |
| Related Documents | System Requirements, Safety Case, ICD, Verification Plan |

---

# Revision History

| Rev | Date | Description | Author |

---

# Contents

1. Purpose
2. Scope
3. Architectural Principles
4. System Context
5. Operational Concept
6. Functional Architecture
7. Physical Architecture
8. Electrical Architecture
9. Software Architecture
10. FPGA Architecture
11. Data Architecture
12. Timing Architecture
13. Communications Architecture
14. Safety Architecture
15. Reliability and Fault Management
16. Maintainability and Configuration
17. Performance Budget
18. Requirements Traceability
19. Future Growth Strategy
20. Conclusions
21. Appendices

---

# 1 Purpose

State the role of the document.

Example:

> This document defines the logical, physical and functional architecture of the Radiation Image Sensor Characterisation System. It provides the design rationale for the partitioning of the system, identifies all major subsystems and interfaces, and demonstrates how the architecture satisfies the system requirements and safety objectives.

---

# 2 Scope

Describe the architectural boundary.

Include:

- 19-inch trolley
- Mains input
- Power conversion
- PXI chassis
- FPGA
- Controller
- Interface electronics
- Propagation cables
- DUT fixture
- Software
- Data acquisition
- Event logging

Exclude:

- Facility infrastructure
- Radiation source
- Customer image sensor internals

---

# 3 Architectural Principles

Define the engineering philosophy that shaped the system.

Typical principles:

- Modular architecture.
- Functional separation of hardware, firmware, and software.
- Single-purpose subsystems.
- Minimise coupling between modules.
- Controlled interfaces (refer to ICD).
- Safe-by-design (IEC 61010).
- Deterministic timing.
- High observability and diagnostics.
- Configuration-controlled components.
- Scalability for future expansion.

These principles provide a benchmark against which future design changes can be assessed.

---

# 4 System Context

Show the system's relationship to the outside world.

Identify:

- Operator
- Laboratory mains supply
- Radiation facility
- DUT
- External network
- Data storage
- Calibration equipment

A context diagram should clearly distinguish external entities from the system boundary.

---

# 5 Operational Concept

Describe how the system is used throughout its lifecycle.

Typical sequence:

1. Installation.
2. Power-up.
3. Self-test.
4. Configuration.
5. Sensor installation.
6. Bias application.
7. Beam exposure.
8. Event acquisition.
9. Data logging.
10. Safe shutdown.
11. Maintenance.

Highlight operational states and transitions.

---

# 6 Functional Architecture

Partition the system into major functions rather than physical components.

Typical functions:

- Power management.
- Sensor bias generation.
- Current monitoring.
- Trigger generation.
- Timing synchronisation.
- Radiation event acquisition.
- Metadata collection.
- Data logging.
- Fault detection.
- Safety management.
- User interface.

For each function, describe:

| Function | Inputs | Outputs | Dependencies | Safety Relevance |

---

# 7 Physical Architecture

Describe the physical implementation.

Typical hierarchy:

- Equipment
  - Rack
    - Power entry module
    - DC power supplies
    - PXI chassis
    - Controller
    - FPGA card
    - Interface modules
  - Propagation cable assembly
  - Fixture electronics
  - DUT

Include photographs and exploded views where useful.

---

# 8 Electrical Architecture

Provide a complete electrical overview.

Include:

- Mains distribution.
- Protective earthing.
- Power tree.
- DC rails.
- Isolation boundaries.
- Energy-limited circuits.
- Fuse allocation.
- Grounding philosophy.
- Shielding strategy.

A power-distribution diagram is essential.

---

# 9 Software Architecture

Describe:

- Host application.
- State machines.
- Configuration management.
- Logging.
- User interface.
- Error handling.
- Configuration files.
- Startup sequence.
- Shutdown sequence.

Illustrate module interactions and data ownership.

---

# 10 FPGA Architecture

Given your use of FPGA technology, dedicate a full chapter to firmware.

Suggested functional blocks:

- Trigger controller.
- Clock generation.
- Event timestamp engine.
- Sensor interface.
- Current monitor interface.
- DMA engine.
- Metadata assembler.
- Fault monitor.
- Watchdog.
- Register interface.

For each block:

| Block | Purpose | Inputs | Outputs | Timing Requirements |

---

# 11 Data Architecture

Describe the lifecycle of data.

Capture:

- Acquisition.
- Buffering.
- Timestamping.
- Metadata attachment.
- Storage.
- Export.

Define data ownership and retention.

Include a data-flow diagram.

---

# 12 Timing Architecture

For your application, timing is a primary architectural concern.

Document:

- Master clock source.
- Clock distribution.
- Synchronisation.
- Trigger generation.
- Event timestamping.
- Latency budgets.
- Jitter budgets.
- Clock-domain crossings.

Provide timing diagrams and latency allocations.

---

# 13 Communications Architecture

Document all communication paths.

Examples:

- PXI backplane.
- PCIe.
- Ethernet.
- SPI.
- I²C.
- UART.
- FPGA register interface.

For each path:

| Link | Protocol | Bandwidth | Latency | Error Handling |

---

# 14 Safety Architecture

Explain how the architecture supports safety objectives.

Include:

- Protective earthing.
- Isolation boundaries.
- Current limiting.
- Fault detection.
- Safe startup.
- Safe shutdown.
- Emergency stop.
- Software watchdog.
- Hardware interlocks.
- Fail-safe defaults.

Cross-reference the Safety Case and FMEA.

---

# 15 Reliability and Fault Management

Describe how the architecture detects and responds to faults.

Cover:

- Hardware diagnostics.
- Firmware monitoring.
- Software exception handling.
- Fault logging.
- Operator notifications.
- Recovery mechanisms.
- Safe-state transitions.

Include a fault-propagation diagram if possible.

---

# 16 Maintainability and Configuration

Describe how the architecture supports maintenance.

Include:

- Modular replacement.
- Firmware updates.
- Software version control.
- Calibration strategy.
- Configuration management.
- Document traceability.

---

# 17 Performance Budget

Allocate measurable performance targets across the architecture.

Example table:

| Parameter | Requirement | Allocation | Verification |
|-----------|-------------|------------|--------------|
| Sensor bias accuracy | ±0.5% | PSU + calibration | Electrical test |
| Timestamp resolution | ≤100 ns | FPGA timing engine | Functional test |
| Trigger latency | ≤1 µs | FPGA path | Oscilloscope measurement |
| Data throughput | ≥X MB/s | PXI DMA | Performance test |
| Availability | >99% | System design | Endurance testing |

---

# 18 Requirements Traceability

Link architectural elements back to system requirements.

| Requirement ID | Architectural Element | Verification Reference |

This ensures every significant architectural decision can be justified against a documented requirement.

---

# 19 Future Growth Strategy

One of the strengths of your programme is its long-term evolution. Capture that explicitly.

Potential growth areas:

- Additional radiation modalities.
- Higher-speed timestamping.
- Increased channel count.
- Fibre-optic propagation links.
- Distributed acquisition nodes.
- Higher bandwidth data capture.
- Enhanced FPGA processing.
- Automated test sequencing.
- Cybersecurity improvements for networked operation.

Document the architectural decisions that already support these future enhancements and identify areas where redesign would be required.

---

# 20 Conclusions

Summarise:

- The architecture satisfies the functional and safety requirements.
- Major design decisions are justified.
- Interfaces are controlled through the ICD.
- Safety is addressed through dedicated architectural features.
- Verification activities provide objective evidence of performance.

---

# Appendices

**Appendix A:** System context diagram.

**Appendix B:** Functional decomposition.

**Appendix C:** Physical block diagrams.

**Appendix D:** Electrical power tree.

**Appendix E:** Data-flow diagrams.

**Appendix F:** Timing diagrams.

**Appendix G:** State-machine diagrams.

**Appendix H:** Communication architecture.

**Appendix I:** Safety architecture.

**Appendix J:** Performance budgets.

**Appendix K:** Requirements traceability matrix.

---

## Recommended architectural views

To elevate this document to the standard expected in aerospace, defence, or high-integrity laboratory equipment projects, don't rely on a single block diagram. Instead, present the architecture through multiple complementary views, each answering a different engineering question:

| View | Answers the Question |
|------|-----------------------|
| **System Context View** | What external systems interact with the test system? |
| **Functional View** | What functions does the system perform? |
| **Logical View** | How are functions partitioned into subsystems? |
| **Physical View** | Where are those subsystems physically located? |
| **Electrical View** | How is power distributed and protected? |
| **Data View** | How does information flow from the DUT to storage? |
| **Timing View** | How are clocks, triggers, and timestamps coordinated? |
| **Safety View** | How are hazards prevented, detected, and controlled? |
| **Deployment View** | How are software, FPGA firmware, and hardware allocated? |

Taken together, these views form a comprehensive architectural description that supports not only design understanding but also your **IEC 61010 Safety Case**, **FMEA**, **ICD**, **Verification & Validation Plan**, and ultimately the entire Technical Construction File.
