# CDR Report Rewrite
Date (UTC): 2026-03-06 09:50
Conversation ID: 69aaa37d-9140-8384-b818-a5a867142c8c
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-06 09:50):
See attached a previous development document that got a bit clunky. Rewrite with structure and narrative to support design report and evidence capture for a Cdr report .
[attached file: OK.docx]

[M2] AI (2026-03-06 09:51):
I reviewed your document and the core issue is clear: it contains **good technical thinking**, but it reads like a **running engineering notebook** rather than a **design report suitable for CDR evidence**.  

For a **Critical Design Review (CDR)** the reviewers typically expect three things:

1. **Clear requirement traceability**
2. **Engineering rationale for design decisions**
3. **Evidence that the design satisfies the requirement**

So the rewrite should follow a **Requirement → Interpretation → Design Implementation → Verification** structure.

Below is a **clean rewritten structure and narrative** you can use as the basis of your CDR design report. I have condensed and organised the technical reasoning from your document into a form suitable for formal review. The content is derived from the uploaded development notes. fileciteturn0file0

---

# CCD Test Camera Headboard  
## Design Description and Requirement Compliance Report (CDR)

---

# 1. Introduction

This document describes the electrical and mechanical design of the CCD test camera headboard developed to support characterisation and operational testing of the CCD381 and CCD385 devices.

The headboard provides the following key functions:

- Generation of programmable CCD clock waveforms
- Generation of CCD bias voltages
- CCD video output conditioning and gain control
- Integration with the Rameses control environment
- Test access and measurement capability for device characterisation

The design has been developed to satisfy the electrical, mechanical and operational requirements defined within the system interface documentation and programme test plan.

This report provides a structured response to those requirements and describes the design decisions taken to meet them.

---

# 2. Device Compatibility

## Requirement

The camera must support **CCD381 and CCD385 devices** in both:

- TEC package (2×18 pins)
- Characterisation package (4×10 pins)

Pin assignments differ between packages.

## Design Implementation

The headboard architecture separates:

- **Electrical interface**
- **Mechanical package interface**

The primary headboard supports the **TEC package configuration**, while compatibility with the characterisation package is provided through a **passive interposer adapter board**.

This approach provides several advantages:

- Maintains optimal routing and signal integrity on the primary headboard
- Avoids dual connector footprints and routing compromises
- Allows independent revision of package adapters

A **pin-mapping matrix** is maintained defining the correspondence between:

- Functional signal
- TEC package pin
- Characterisation package pin

This mapping forms the configuration reference for both hardware and software.

## Verification

Compatibility is verified through:

- Mechanical fit checks against device interface drawings
- Electrical continuity validation through the adapter
- Functional device operation in both configurations

---

# 3. Mechanical Mounting and Thermal Interface

## Requirement

The CCD mounting arrangement shall:

- Provide adequate **thermal contact to the cold finger**
- Provide reliable **electrical connection to the headboard**
- Avoid obstruction of the **illumination path**

## Design Implementation

The device is mounted using a **spring-loaded perimeter clamp assembly** that:

- Maintains consistent clamping force
- Ensures good thermal coupling
- Avoids mechanical stress on the package

A **thin thermal interface layer** is used between the device and cold finger to reduce thermal resistance while accommodating surface tolerances.

The clamp geometry is designed to maintain a **clear optical aperture above the CCD active area**, preventing obstruction of illumination during optical testing.

## Verification

Thermal performance is validated by:

- Temperature stabilisation testing
- Thermal gradient measurement across the mounting interface

Mechanical clearance is verified through CAD modelling and physical fit testing.

---

# 4. Obsolescence Management

## Requirement

Components selected early in the design shall undergo **obsolescence review**, and results reported at PDR.

## Design Implementation

An **obsolescence review process** was implemented covering all critical components including:

- Clock driver ICs
- DACs and ADCs
- LVDS receivers
- FPGA devices
- High-voltage regulators
- Interface connectors

Each component was evaluated for:

- Lifecycle status
- Supplier availability
- Alternative sources
- Replacement strategy

Results are documented in an **Obsolescence Review Table** including risk categorisation and mitigation actions.

## Verification

Obsolescence review documentation forms part of the **PDR evidence package**.

---

# 5. Video Output Chain Gain

## Requirement

The camera output chain shall support selectable gain between:

**Gain ×1 to Gain ×24**

The lowest gain setting must support measurement of signals exceeding **400,000 electrons** without saturation.

## Design Implementation

The video chain uses a **two-stage gain architecture**:

### Stage 1 – Low noise input stage
Provides unity or low gain with minimal noise contribution.

### Stage 2 – Programmable gain stage
Selectable gain settings provide the required amplification range.

The ×1 path is implemented as a **true unity gain configuration**, ensuring maximum signal headroom for full-well measurements.

Higher gains are used for:

- dark current measurements
- read noise analysis

## Verification

Performance is validated through:

- Full-well signal testing
- Noise floor measurements
- Gain linearity verification across gain settings

---

# 6. AC Coupling and Baseline Stability

## Requirement

The AC coupling network in the video chain must support both:

- **50 kHz**
- **375 kHz**

readout rates without introducing settling errors exceeding the CCD read noise.

Provision shall exist for **adjustment of the RC time constant**.

## Design Implementation

The AC coupling network forms a **high-pass filter** designed with a time constant significantly longer than the pixel period.

Adjustment capability is provided through **parallel capacitor footprints**, allowing the effective coupling capacitance to be tuned during system testing.

This approach provides:

- predictable behaviour
- minimal noise impact
- simple implementation

## Verification

Baseline stability is verified by:

- analysing overscan regions
- measuring baseline drift during readout
- comparing performance across readout speeds

---

# 7. Image Acquisition via Rameses

## Requirement

Image acquisition shall be performed using a **scope card connected to Rameses**, allowing viewing and sampling of overscan signals.

## Design Implementation

The headboard provides a dedicated **video output interface** compatible with the scope card acquisition system.

Supporting signals are also provided:

- pixel clock
- line synchronisation
- frame synchronisation

These signals allow the Rameses image viewer module to reconstruct the CCD output stream including overscan regions.

## Verification

Verification is performed by capturing CCD data through the scope card and reconstructing the image in the Rameses viewer.

---

# 8. Clock Voltage Groups

## Requirement

Clock high and low voltages must be grouped according to CCD functional blocks.

Groups include:

- Image clocks
- Memory clocks
- Buffer storage clocks
- Register clocks
- Reset clocks
- Dump gate
- DC reset

## Design Implementation

Each clock group is driven by a **pair of programmable voltage rails**:

- VH(group)
- VL(group)

These rails are generated using DAC-controlled regulators and distributed to the clock driver circuits.

Grouping simplifies voltage control and reflects the electrical organisation of the CCD.

## Verification

Each group rail is measured and confirmed to operate independently and within specification.

---

# 9. Clock Voltage Control

## Clock High Levels

**Range:** +5 V to +15 V  
**Accuracy:** ±0.1 V

Each clock high rail is generated using:

- DAC controlled reference
- closed-loop regulator
- precision feedback network

Rail voltages are monitored using ADC readback to allow calibration within Rameses.

---

## Clock Low Levels

**Range:** −2 V to +2 V  
**Accuracy:** ±0.1 V

Low voltage rails are generated using **bipolar output stages** referenced to a negative supply rail.

Readback and calibration ensure accurate voltage control.

---

# 10. Clock Slew Rate Control

## Requirement

Clock rise and fall times shall be adjustable between:

**3 ns – 150 ns (10–90%)**

## Design Implementation

Slew control is implemented by adjusting the **input edge rate of the clock driver** using selectable series resistors controlled through an analog multiplexer.

This approach avoids switching elements in the high-voltage clock path while providing adjustable edge speeds.

Control parameters are configurable through the Rameses software interface.

## Verification

Rise and fall times are measured at representative clock outputs using oscilloscope measurements.

---

# 11. Clock Sequencer

## Requirement

Clock frequencies required include:

- Image clocks up to **24 MHz**
- Memory clocks up to **4 MHz**
- Buffer clocks up to **1 MHz**
- Register clocks up to **375 kHz**

The sequencer must support **7 ns timing resolution**.

## Design Implementation

Clock generation is implemented using an **FPGA based sequencer** operating with a high-frequency timing base.

This architecture enables:

- programmable waveform sequences
- variable clock frequencies
- precise phase relationships between clocks

Single-pulse signals such as dump gate triggers are generated using timed events within the sequencer.

## Verification

Clock timing and phase relationships are validated using oscilloscope measurements and FPGA simulation.

---

# 12. Bias Voltage Generation

The following bias rails are generated:

| Bias | Range |
|-----|------|
| SS | 0 – 12 V |
| RD | 0 – 25 V |
| OD | 0 – 35 V |
| DD | 0 – 30 V |
| DDM | 0 – 30 V |
| OG | −2 – 10 V |

All bias voltages are DAC controlled and regulated to within **±0.1 V accuracy**.

OG is implemented as a bipolar rail requiring a negative supply.

## Verification

Bias voltages are verified using multimeter measurements and system readback through ADC monitoring.

---

# 13. External Bias Injection

## Requirement

External supplies for **RD, OD and SS** shall be possible.

## Design Implementation

Auxiliary Molex connectors allow external supplies to be injected.

Selection between internal and external bias sources is achieved using **link jumpers**, preventing back-driving of internal regulators.

This capability allows noise investigations and alternative supply configurations during testing.

---

# 14. Power-Up Safe State

## Requirement

At initial power-up all biases and clocks shall be **0 V ±0.1 V**.

## Design Implementation

A hardware **SAFE ENABLE** signal holds:

- bias regulators disabled
- clock drivers disabled

until system configuration is complete.

Pull-down networks ensure all clock control signals default to a safe state.

## Verification

Power-up testing confirms all outputs remain within ±0.1 V before system enable.

---

# 15. Test Access

Test access points are provided for:

- all bias rails
- clock rails
- video output
- representative clock signals

These include both:

- DMM measurement points
- oscilloscope access connectors

This ensures the system can be debugged and validated during testing.

---

# 16. Characterisation Test Capability

The headboard design supports the following device tests:

- output impedance
- inter-electrode capacitance
- electrode-substrate capacitance
- output amplifier bandwidth

Isolation links and measurement access points allow the CCD to be connected to external instrumentation where required.

Where direct measurement from the headboard is impractical, dedicated **breakout fixtures** are used.

---

# 17. Conclusion

The headboard design implements a flexible and configurable CCD control system capable of supporting both operational testing and detailed device characterisation.

The architecture provides:

- programmable clock generation
- precision bias control
- flexible gain video processing
- robust measurement access
- integration with Rameses acquisition tools

The design approach ensures compatibility with both CCD381 and CCD385 devices and supports the full range of programme testing activities.

---

If you'd like, I can also help you with **two things that would significantly strengthen your CDR package**:

1. Turn this into a **proper CDR document format (with requirement trace table)**  
2. Create a **Requirement → Design → Verification matrix** reviewers love (it massively improves review outcomes).

[M3] ME (2026-03-06 10:04):
Both 

[M4] AI (2026-03-06 10:15):
Done — I created both, based on your uploaded baseline notes. fileciteturn1file0

- [CDR design report (.docx)](sandbox:/mnt/data/ccd_headboard_cdr_design_report.docx)
- [Requirement-evidence trace matrix (.xlsx)](sandbox:/mnt/data/ccd_headboard_cdr_trace_matrix.xlsx)

If you want, I can also produce a **clean client-facing PDF set** from these next.

[M5] ME (2026-03-06 10:57):
The word report above has expired 

[M6] AI (2026-03-06 11:01):
Here’s a fresh link to the Word report:

[CCD headboard CDR design report (.docx)](sandbox:/mnt/data/ccd_headboard_cdr_design_report.docx)

The trace matrix is still here as well:

[CCD headboard CDR trace matrix (.xlsx)](sandbox:/mnt/data/ccd_headboard_cdr_trace_matrix.xlsx)

[M7] ME (2026-03-06 15:29):
Now rewrite the report with this structure 

1.     INTRODUCTION.. 1
1.1 Purpose of the Document. 2
1.2        Scope. 2
1.3        Applicable Documents. 2
1.4        Requirement Traceability Approach. 2
0      REF. 2
Table of Contents. 3
2.         SYSTEM OVERVIEW... 7
2.1        Test Camera Architecture. 7
2.1.2      Block diagram: detector → headboard → clocks/bias → output → digitiser. 8
2.1.3      Identify where CCD381 and CCD385 diverge and converge. 8
2.2        Supported Detector Variants. 8
2.2.1      CCD381 and CCD385 summary. 9
2.2.2      Matrix vs LIDAR mode distinctions. 9
2.2.3      Package and pinout commonality / differences. 9
3.         MECHANICAL AND PACKAGE INTERFACE. 9
3.1        Characterisation Package Interface. 9
3.1.1      Mechanical interface per AD10 / AD11. 9
3.1.2      Electrical interface overview.. 9
3.2        Device Mounting and Clamping. 9
3.2.1      Clamp concept. 10
3.2.2      Contact strategy. 10
3.2.3      Heritage from CCD47‑20. 10
3.2.4      Optical clearance discussion. 10
3.3        Headboard Storage and Handling. 10
3.3.1      ESD protection. 10
3.3.2      Physical protection. 10
3.3.3      Multi‑headboard accommodation. 10
4.         ELECTRONICS ARCHITECTURE. 10
4.1        Headboard Overview.. 10
4.1.1      Functional partitioning: 11
4.2        Obsolescence Considerations. 11
4.2.1      Summary of component lifecycle checks. 12
4.2.2      Risks and mitigations. 12
5.         OUTPUT CHAIN DESIGN.. 12
5.1        Gain Architecture. 12
5.1.1      Gain stages. 12
5.1.2      Gain range. 12
5.1.3      Full‑well accommodation. 12
5.2        AC Coupling and RC Time Constants. 13
5.2.1      RC calculations. 13
5.2.2      50 kHz and 375 kHz justification. 13
5.2.3      Adjustment mechanisms (design provision). 13
5.3        Output Monitoring and Image Capture. 13
5.3.1      Scope card / Rameses integration. 14
5.3.2      OS sampling strategy. 14
6.         CLOCK GENERATION AND SEQUENCING.. 14
6.1 Clock Grouping Strategy. 14
6.1.1      Image, Memory, Buffer, Register, Reset, Dump Gate groupings. 14
6.2        Clock Voltage Generation. 14
6.2.1      High and low voltage ranges. 15
6.2.2      Accuracy expectations. 15
6.2.3      Rameses control 15
6.3        SLEW RATE CONTROL. 15
6.3.1      Hardware mechanism.. 15
6.3.2      User control path. 15
6.4        CLOCK FREQUENCY CAPABILITY. 15
6.4.1      Image, Memory, Buffer, Register, Reset clocks. 16
6.4.2      24 MHz LIDAR mode justification. 16
6.4.3      Sequencer tick capability. 16
7.         BIAS GENERATION.. 16
7.1        Bias Architecture Overview.. 16
7.1.1      System Interface. 17
SS, RD, OD, DD, DDM, OG.. 17
Range and accuracy targets. 17
7.2        Bias Commoning Strategy. 17
OGA/RDA/ODA treatment. 17
Documentation of implementation choice. 17
7.3        Auxiliary Bias Inputs. 17
External bias injection points. 17
Connector locations. 17
7.4        Power‑On / Power‑Off Behaviour. 17
Zero‑bias strategy. 18
Protection rationale. 18
8.         TEST ACCESS AND MEASUREMENT SUPPORT. 18
8.1        Test Points. 18
8.1.2      Multimeter access. 18
8.1.3      Oscilloscope access. 18
8.2        Non‑Standard EO Tests. 18
8.2.1      Output impedance. 19
8.2.2      Inter‑capacitance. 19
8.2.3      Amplifier bandwidth. 19
8.2.4      Breakout strategy (if required). 19
8.3        Automated Measurement Support. 19
8.3.1      Rationale for automation. 19
8.3.2      Scope card / scripting approach. 19
9.         NOISE AND PERFORMANCE CONSIDERATIONS. 19
9.1        Noise Measurement Approach. 20
9.1.1      Bandwidth assumptions. 20
9.1.2      CDS assumptions. 20
9.1.3      Primary and auxiliary outputs. 20
10.        THERMAL DESIGN.. 20
10.1      Temperature Sensing. 20
10.1.1        PT1000 implementation. 20
10.1.2        Die monitoring without powering. 20
10.2      TEMPERATURE UNCERTAINTY. 21
10.2.1        Error budget. 21
10.2.1        Heritage and tolerances. 21
10.3      TEMPERATURE CONTROL CAPABILITY. 21
10.3.1        −70 °C to +25 °C strategy. 21
10.3.2        TEC linkage. 21
11.        PROGRAMMABLE PINOUT AND TIMING.. 21
11.1      Pinout Flexibility. 21
11.1.1        CCD381 vs CCD385 differences. 22
11.1.2        Hardware accommodation. 22
11.2      Timing File Adaptation. 22
11.2.1        Sequencer configuration strategy. 22
12.        POWER DISSIPATION MEASUREMENT. 22
12.1.1        Static and dynamic measurement concepts. 22
12.1.2        Design features enabling measurement. 22
13.        VERIFICATION STRATEGY SUMMARY. 23
13.1       Design evidence → this document. 23
13.2       Test evidence → Verification Plan / Test Reports. 23
Appendix A — Requirements Traceability Table (REQ No. + Derived Description + Closure Sections). 24

[M8] AI (2026-03-06 15:39):
Done — I rewrote the report to your requested section ladder and carried across the additional thermal/PT1000, programmable pinout, timing-file adaptation, and power-dissipation material from your uploaded notes. fileciteturn2file2 fileciteturn2file11 fileciteturn2file9

[Download the restructured Word report](sandbox:/mnt/data/ccd_headboard_cdr_design_report_restructured.docx)

I rendered and checked the layout after rebuilding it. The appendix traceability table, cover page, and main section flow are all in place.

[M9] ME (2026-03-06 15:40):
Now rewrite the report with this structure 

1.     INTRODUCTION.. 1
1.1 Purpose of the Document. 2
1.2        Scope. 2
1.3        Applicable Documents. 2
1.4        Requirement Traceability Approach. 2
0      REF. 2
Table of Contents. 3
2.         SYSTEM OVERVIEW... 7
2.1        Test Camera Architecture. 7
2.1.2      Block diagram: detector → headboard → clocks/bias → output → digitiser. 8
2.1.3      Identify where CCD381 and CCD385 diverge and converge. 8
2.2        Supported Detector Variants. 8
2.2.1      CCD381 and CCD385 summary. 9
2.2.2      Matrix vs LIDAR mode distinctions. 9
2.2.3      Package and pinout commonality / differences. 9
3.         MECHANICAL AND PACKAGE INTERFACE. 9
3.1        Characterisation Package Interface. 9
3.1.1      Mechanical interface per AD10 / AD11. 9
3.1.2      Electrical interface overview.. 9
3.2        Device Mounting and Clamping. 9
3.2.1      Clamp concept. 10
3.2.2      Contact strategy. 10
3.2.3      Heritage from CCD47‑20. 10
3.2.4      Optical clearance discussion. 10
3.3        Headboard Storage and Handling. 10
3.3.1      ESD protection. 10
3.3.2      Physical protection. 10
3.3.3      Multi‑headboard accommodation. 10
4.         ELECTRONICS ARCHITECTURE. 10
4.1        Headboard Overview.. 10
4.1.1      Functional partitioning: 11
4.2        Obsolescence Considerations. 11
4.2.1      Summary of component lifecycle checks. 12
4.2.2      Risks and mitigations. 12
5.         OUTPUT CHAIN DESIGN.. 12
5.1        Gain Architecture. 12
5.1.1      Gain stages. 12
5.1.2      Gain range. 12
5.1.3      Full‑well accommodation. 12
5.2        AC Coupling and RC Time Constants. 13
5.2.1      RC calculations. 13
5.2.2      50 kHz and 375 kHz justification. 13
5.2.3      Adjustment mechanisms (design provision). 13
5.3        Output Monitoring and Image Capture. 13
5.3.1      Scope card / Rameses integration. 14
5.3.2      OS sampling strategy. 14
6.         CLOCK GENERATION AND SEQUENCING.. 14
6.1 Clock Grouping Strategy. 14
6.1.1      Image, Memory, Buffer, Register, Reset, Dump Gate groupings. 14
6.2        Clock Voltage Generation. 14
6.2.1      High and low voltage ranges. 15
6.2.2      Accuracy expectations. 15
6.2.3      Rameses control 15
6.3        SLEW RATE CONTROL. 15
6.3.1      Hardware mechanism.. 15
6.3.2      User control path. 15
6.4        CLOCK FREQUENCY CAPABILITY. 15
6.4.1      Image, Memory, Buffer, Register, Reset clocks. 16
6.4.2      24 MHz LIDAR mode justification. 16
6.4.3      Sequencer tick capability. 16
7.         BIAS GENERATION.. 16
7.1        Bias Architecture Overview.. 16
7.1.1      System Interface. 17
SS, RD, OD, DD, DDM, OG.. 17
Range and accuracy targets. 17
7.2        Bias Commoning Strategy. 17
OGA/RDA/ODA treatment. 17
Documentation of implementation choice. 17
7.3        Auxiliary Bias Inputs. 17
External bias injection points. 17
Connector locations. 17
7.4        Power‑On / Power‑Off Behaviour. 17
Zero‑bias strategy. 18
Protection rationale. 18
8.         TEST ACCESS AND MEASUREMENT SUPPORT. 18
8.1        Test Points. 18
8.1.2      Multimeter access. 18
8.1.3      Oscilloscope access. 18
8.2        Non‑Standard EO Tests. 18
8.2.1      Output impedance. 19
8.2.2      Inter‑capacitance. 19
8.2.3      Amplifier bandwidth. 19
8.2.4      Breakout strategy (if required). 19
8.3        Automated Measurement Support. 19
8.3.1      Rationale for automation. 19
8.3.2      Scope card / scripting approach. 19
9.         NOISE AND PERFORMANCE CONSIDERATIONS. 19
9.1        Noise Measurement Approach. 20
9.1.1      Bandwidth assumptions. 20
9.1.2      CDS assumptions. 20
9.1.3      Primary and auxiliary outputs. 20
10.        THERMAL DESIGN.. 20
10.1      Temperature Sensing. 20
10.1.1        PT1000 implementation. 20
10.1.2        Die monitoring without powering. 20
10.2      TEMPERATURE UNCERTAINTY. 21
10.2.1        Error budget. 21
10.2.1        Heritage and tolerances. 21
10.3      TEMPERATURE CONTROL CAPABILITY. 21
10.3.1        −70 °C to +25 °C strategy. 21
10.3.2        TEC linkage. 21
11.        PROGRAMMABLE PINOUT AND TIMING.. 21
11.1      Pinout Flexibility. 21
11.1.1        CCD381 vs CCD385 differences. 22
11.1.2        Hardware accommodation. 22
11.2      Timing File Adaptation. 22
11.2.1        Sequencer configuration strategy. 22
12.        POWER DISSIPATION MEASUREMENT. 22
12.1.1        Static and dynamic measurement concepts. 22
12.1.2        Design features enabling measurement. 22
13.        VERIFICATION STRATEGY SUMMARY. 23
13.1       Design evidence → this document. 23
13.2       Test evidence → Verification Plan / Test Reports. 23
Appendix A — Requirements Traceability Table (REQ No. + Derived Description + Closure Sections). 24

[M10] AI (2026-03-06 15:52):
Done — I rebuilt it to that section structure and saved a fresh copy here:

[Download the rewritten Word report](sandbox:/mnt/data/ccd_headboard_cdr_design_report_restructured_v2.docx)

I also checked the rendered layout after rebuilding. The document now follows your requested ladder through system overview, mechanical interface, electronics architecture, output chain, clocks, biases, test support, thermal, programmable pinout/timing, power dissipation, verification summary, and Appendix A traceability.

[M11] ME (2026-03-06 16:05):
Now rewrite the report with this structure 

1.     INTRODUCTION.. 1
1.1 Purpose of the Document. 2
1.2        Scope. 2
1.3        Applicable Documents. 2
1.4        Requirement Traceability Approach. 2
0      REF. 2
Table of Contents. 3
2.         SYSTEM OVERVIEW... 7
2.1        Test Camera Architecture. 7
2.1.2      Block diagram: detector → headboard → clocks/bias → output → digitiser. 8
2.1.3      Identify where CCD381 and CCD385 diverge and converge. 8
2.2        Supported Detector Variants. 8
2.2.1      CCD381 and CCD385 summary. 9
2.2.2      Matrix vs LIDAR mode distinctions. 9
2.2.3      Package and pinout commonality / differences. 9
3.         MECHANICAL AND PACKAGE INTERFACE. 9
3.1        Characterisation Package Interface. 9
3.1.1      Mechanical interface per AD10 / AD11. 9
3.1.2      Electrical interface overview.. 9
3.2        Device Mounting and Clamping. 9
3.2.1      Clamp concept. 10
3.2.2      Contact strategy. 10
3.2.3      Heritage from CCD47‑20. 10
3.2.4      Optical clearance discussion. 10
3.3        Headboard Storage and Handling. 10
3.3.1      ESD protection. 10
3.3.2      Physical protection. 10
3.3.3      Multi‑headboard accommodation. 10
4.         ELECTRONICS ARCHITECTURE. 10
4.1        Headboard Overview.. 10
4.1.1      Functional partitioning: 11
4.2        Obsolescence Considerations. 11
4.2.1      Summary of component lifecycle checks. 12
4.2.2      Risks and mitigations. 12
5.         OUTPUT CHAIN DESIGN.. 12
5.1        Gain Architecture. 12
5.1.1      Gain stages. 12
5.1.2      Gain range. 12
5.1.3      Full‑well accommodation. 12
5.2        AC Coupling and RC Time Constants. 13
5.2.1      RC calculations. 13
5.2.2      50 kHz and 375 kHz justification. 13
5.2.3      Adjustment mechanisms (design provision). 13
5.3        Output Monitoring and Image Capture. 13
5.3.1      Scope card / Rameses integration. 14
5.3.2      OS sampling strategy. 14
6.         CLOCK GENERATION AND SEQUENCING.. 14
6.1 Clock Grouping Strategy. 14
6.1.1      Image, Memory, Buffer, Register, Reset, Dump Gate groupings. 14
6.2        Clock Voltage Generation. 14
6.2.1      High and low voltage ranges. 15
6.2.2      Accuracy expectations. 15
6.2.3      Rameses control 15
6.3        SLEW RATE CONTROL. 15
6.3.1      Hardware mechanism.. 15
6.3.2      User control path. 15
6.4        CLOCK FREQUENCY CAPABILITY. 15
6.4.1      Image, Memory, Buffer, Register, Reset clocks. 16
6.4.2      24 MHz LIDAR mode justification. 16
6.4.3      Sequencer tick capability. 16
7.         BIAS GENERATION.. 16
7.1        Bias Architecture Overview.. 16
7.1.1      System Interface. 17
SS, RD, OD, DD, DDM, OG.. 17
Range and accuracy targets. 17
7.2        Bias Commoning Strategy. 17
OGA/RDA/ODA treatment. 17
Documentation of implementation choice. 17
7.3        Auxiliary Bias Inputs. 17
External bias injection points. 17
Connector locations. 17
7.4        Power‑On / Power‑Off Behaviour. 17
Zero‑bias strategy. 18
Protection rationale. 18
8.         TEST ACCESS AND MEASUREMENT SUPPORT. 18
8.1        Test Points. 18
8.1.2      Multimeter access. 18
8.1.3      Oscilloscope access. 18
8.2        Non‑Standard EO Tests. 18
8.2.1      Output impedance. 19
8.2.2      Inter‑capacitance. 19
8.2.3      Amplifier bandwidth. 19
8.2.4      Breakout strategy (if required). 19
8.3        Automated Measurement Support. 19
8.3.1      Rationale for automation. 19
8.3.2      Scope card / scripting approach. 19
9.         NOISE AND PERFORMANCE CONSIDERATIONS. 19
9.1        Noise Measurement Approach. 20
9.1.1      Bandwidth assumptions. 20
9.1.2      CDS assumptions. 20
9.1.3      Primary and auxiliary outputs. 20
10.        THERMAL DESIGN.. 20
10.1      Temperature Sensing. 20
10.1.1        PT1000 implementation. 20
10.1.2        Die monitoring without powering. 20
10.2      TEMPERATURE UNCERTAINTY. 21
10.2.1        Error budget. 21
10.2.1        Heritage and tolerances. 21
10.3      TEMPERATURE CONTROL CAPABILITY. 21
10.3.1        −70 °C to +25 °C strategy. 21
10.3.2        TEC linkage. 21
11.        PROGRAMMABLE PINOUT AND TIMING.. 21
11.1      Pinout Flexibility. 21
11.1.1        CCD381 vs CCD385 differences. 22
11.1.2        Hardware accommodation. 22
11.2      Timing File Adaptation. 22
11.2.1        Sequencer configuration strategy. 22
12.        POWER DISSIPATION MEASUREMENT. 22
12.1.1        Static and dynamic measurement concepts. 22
12.1.2        Design features enabling measurement. 22
13.        VERIFICATION STRATEGY SUMMARY. 23
13.1       Design evidence → this document. 23
13.2       Test evidence → Verification Plan / Test Reports. 23
Appendix A — Requirements Traceability Table (REQ No. + Derived Description + Closure Sections). 24

[M12] ME (2026-03-06 16:11):
Rewrite this report using this structure :

Now rewrite the report with this structure 

1.     INTRODUCTION.. 1
1.1 Purpose of the Document. 2
1.2        Scope. 2
1.3        Applicable Documents. 2
1.4        Requirement Traceability Approach. 2
0      REF. 2
Table of Contents. 3
2.         SYSTEM OVERVIEW... 7
2.1        Test Camera Architecture. 7
2.1.2      Block diagram: detector → headboard → clocks/bias → output → digitiser. 8
2.1.3      Identify where CCD381 and CCD385 diverge and converge. 8
2.2        Supported Detector Variants. 8
2.2.1      CCD381 and CCD385 summary. 9
2.2.2      Matrix vs LIDAR mode distinctions. 9
2.2.3      Package and pinout commonality / differences. 9
3.         MECHANICAL AND PACKAGE INTERFACE. 9
3.1        Characterisation Package Interface. 9
3.1.1      Mechanical interface per AD10 / AD11. 9
3.1.2      Electrical interface overview.. 9
3.2        Device Mounting and Clamping. 9
3.2.1      Clamp concept. 10
3.2.2      Contact strategy. 10
3.2.3      Heritage from CCD47‑20. 10
3.2.4      Optical clearance discussion. 10
3.3        Headboard Storage and Handling. 10
3.3.1      ESD protection. 10
3.3.2      Physical protection. 10
3.3.3      Multi‑headboard accommodation. 10
4.         ELECTRONICS ARCHITECTURE. 10
4.1        Headboard Overview.. 10
4.1.1      Functional partitioning: 11
4.2        Obsolescence Considerations. 11
4.2.1      Summary of component lifecycle checks. 12
4.2.2      Risks and mitigations. 12
5.         OUTPUT CHAIN DESIGN.. 12
5.1        Gain Architecture. 12
5.1.1      Gain stages. 12
5.1.2      Gain range. 12
5.1.3      Full‑well accommodation. 12
5.2        AC Coupling and RC Time Constants. 13
5.2.1      RC calculations. 13
5.2.2      50 kHz and 375 kHz justification. 13
5.2.3      Adjustment mechanisms (design provision). 13
5.3        Output Monitoring and Image Capture. 13
5.3.1      Scope card / Rameses integration. 14
5.3.2      OS sampling strategy. 14
6.         CLOCK GENERATION AND SEQUENCING.. 14
6.1 Clock Grouping Strategy. 14
6.1.1      Image, Memory, Buffer, Register, Reset, Dump Gate groupings. 14
6.2        Clock Voltage Generation. 14
6.2.1      High and low voltage ranges. 15
6.2.2      Accuracy expectations. 15
6.2.3      Rameses control 15
6.3        SLEW RATE CONTROL. 15
6.3.1      Hardware mechanism.. 15
6.3.2      User control path. 15
6.4        CLOCK FREQUENCY CAPABILITY. 15
6.4.1      Image, Memory, Buffer, Register, Reset clocks. 16
6.4.2      24 MHz LIDAR mode justification. 16
6.4.3      Sequencer tick capability. 16
7.         BIAS GENERATION.. 16
7.1        Bias Architecture Overview.. 16
7.1.1      System Interface. 17
SS, RD, OD, DD, DDM, OG.. 17
Range and accuracy targets. 17
7.2        Bias Commoning Strategy. 17
OGA/RDA/ODA treatment. 17
Documentation of implementation choice. 17
7.3        Auxiliary Bias Inputs. 17
External bias injection points. 17
Connector locations. 17
7.4        Power‑On / Power‑Off Behaviour. 17
Zero‑bias strategy. 18
Protection rationale. 18
8.         TEST ACCESS AND MEASUREMENT SUPPORT. 18
8.1        Test Points. 18
8.1.2      Multimeter access. 18
8.1.3      Oscilloscope access. 18
8.2        Non‑Standard EO Tests. 18
8.2.1      Output impedance. 19
8.2.2      Inter‑capacitance. 19
8.2.3      Amplifier bandwidth. 19
8.2.4      Breakout strategy (if required). 19
8.3        Automated Measurement Support. 19
8.3.1      Rationale for automation. 19
8.3.2      Scope card / scripting approach. 19
9.         NOISE AND PERFORMANCE CONSIDERATIONS. 19
9.1        Noise Measurement Approach. 20
9.1.1      Bandwidth assumptions. 20
9.1.2      CDS assumptions. 20
9.1.3      Primary and auxiliary outputs. 20
10.        THERMAL DESIGN.. 20
10.1      Temperature Sensing. 20
10.1.1        PT1000 implementation. 20
10.1.2        Die monitoring without powering. 20
10.2      TEMPERATURE UNCERTAINTY. 21
10.2.1        Error budget. 21
10.2.1        Heritage and tolerances. 21
10.3      TEMPERATURE CONTROL CAPABILITY. 21
10.3.1        −70 °C to +25 °C strategy. 21
10.3.2        TEC linkage. 21
11.        PROGRAMMABLE PINOUT AND TIMING.. 21
11.1      Pinout Flexibility. 21
11.1.1        CCD381 vs CCD385 differences. 22
11.1.2        Hardware accommodation. 22
11.2      Timing File Adaptation. 22
11.2.1        Sequencer configuration strategy. 22
12.        POWER DISSIPATION MEASUREMENT. 22
12.1.1        Static and dynamic measurement concepts. 22
12.1.2        Design features enabling measurement. 22
13.        VERIFICATION STRATEGY SUMMARY. 23
13.1       Design evidence → this document. 23
13.2       Test evidence → Verification Plan / Test Reports. 23
Appendix A — Requirements Traceability Table (REQ No. + Derived Description + Closure Sections). 24
[attached file: ccd_headboard_cdr_design_report.docx]

[M13] ME (2026-03-06 16:17):
You can write the document here 

[M14] AI (2026-03-06 16:22):
Absolutely — below is a rewritten version of the report using your requested structure, with the existing design narrative reorganised into a more formal CDR-style document. The content is based on your uploaded draft plus the supporting requirement-response material you developed around package support, clocks, biases, output chain, thermal sensing, automated measurement, and verification logic. fileciteturn4file5 fileciteturn4file8

---

# CCD TEST CAMERA HEADBOARD  
## CDR DESIGN REPORT

---

## 1. INTRODUCTION

The CCD test camera headboard is intended to provide the electrical, mechanical and measurement interface required to support evaluation of CCD381 and CCD385 detector devices across development, characterisation and verification activities. The design must combine programmable clocks, programmable biases, output signal conditioning, detector mounting, thermal monitoring and structured test access in a form suitable for repeated laboratory use and formal programme review. fileciteturn4file8

### 1.1 Purpose of the Document

This document records the design intent, architectural choices and requirement-driven implementation approach for the CCD test camera headboard. Its purpose is to support Critical Design Review by presenting a coherent engineering narrative that links system requirements to proposed hardware responses and to the verification evidence expected to close them. fileciteturn4file8turn4file5

### 1.2 Scope

The report covers the headboard concept and its supporting interfaces, including detector compatibility, package accommodation, clamping and thermal interface, programmable clocks and biases, output chain design, test access, automation support, thermal sensing, timing flexibility and verification strategy. It is written as a design narrative rather than a test report, and therefore points forward to controlled evidence items such as pin-mapping tables, rail tables, test-point schedules and verification data packs. fileciteturn4file8turn4file5

### 1.3 Applicable Documents

Applicable documents include the package and interface definitions for CCD381 and CCD385 devices, including TEC and characterisation package interface drawings, the CCD interface and operation information, programme requirements, lessons learned references, and the developing verification and evidence matrix associated with this headboard design. The requirement responses also reference AD10, AD11 and AD13 for package interface definition and dimensional control. fileciteturn4file11

### 1.4 Requirement Traceability Approach

Requirement traceability is handled by expressing each major design area in three linked layers: requirement interpretation, design response, and evidence/verification path. This report therefore acts as the design-evidence narrative, while detailed closure is expected through supporting artefacts such as the requirement trace matrix, controlled interface tables, obsolescence checks, gain tables, bias tables, test access maps and verification results. fileciteturn4file5turn4file8

## 0. REF.

Reference control for this report should identify the working issue, baseline requirements source, linked trace matrix, linked verification plan and any associated package/interposer drawings or fixture definitions. This section is intended as the controlled reference anchor for the final issue. fileciteturn4file5

## Table of Contents

The table of contents should be generated from the heading structure of this document and locked only at controlled issue release. The structure below is written to match the requested review format. 

---

## 2. SYSTEM OVERVIEW

The headboard sits between the detector package and the external control and measurement environment. It provides programmable clock and bias distribution, analog output conditioning, thermal monitoring and test access while remaining compatible with multiple detector/package variants. The overall design philosophy is to preserve a clean primary signal path and introduce flexibility through controlled options, interposers, links or breakout fixtures where needed. fileciteturn4file8turn4file10

### 2.1 Test Camera Architecture

The test camera architecture is based on a detector-specific headboard supported by external sequencing, bias control, capture hardware and Rameses-based supervision. The headboard performs the immediate detector interface role and is therefore the point where detector package differences, clock rail implementation, bias routing, video extraction and testability considerations must be reconciled. fileciteturn4file8

#### 2.1.2 Block diagram: detector → headboard → clocks/bias → output → digitiser

At system level the detector is mounted onto the headboard through either the TEC interface or a characterisation-package interposer path. The headboard routes programmable clock rails and detector biases to the device, conditions the analog output, and presents that output to a measurement or digitisation chain such as the scope card used with Rameses. Timing markers and control signals allow waveform reconstruction, overscan analysis and automated measurement. fileciteturn4file7turn4file8

#### 2.1.3 Identify where CCD381 and CCD385 diverge and converge

The CCD381 and CCD385 converge at the level of needing the same broad class of infrastructure: programmable clocks, programmable biases, video output capture, temperature monitoring and package support. They diverge in timing modes, frequency requirements, package/pinout variants and operating modes such as matrix versus LiDAR operation. The headboard architecture therefore treats shared infrastructure as common while keeping pin mapping, timing configuration and package adaptation as controlled variant layers. fileciteturn4file11turn4file8

### 2.2 Supported Detector Variants

The design supports CCD381 and CCD385 detectors in both TEC and characterisation package forms. Compatibility is not assumed from direct footprint similarity; instead, a controlled mapping strategy is required to preserve electrical correctness and mechanical fit. fileciteturn4file10turn4file11

#### 2.2.1 CCD381 and CCD385 summary

Both detector families require programmable clocking, programmable biasing and robust output observation. The headboard is intended to support test and characterisation across these devices rather than serve as a narrowly optimised single-device carrier. This drives the need for flexible sequencing, configurable bias sets and explicit interface documentation. fileciteturn4file8

#### 2.2.2 Matrix vs LIDAR mode distinctions

Matrix and LiDAR modes place different timing demands on the sequencing architecture. In particular, the image clocking requirements include lower-rate operation for matrix modes and higher-rate operation such as 24 MHz in LiDAR mode, which pushes the sequencer timing resolution and phase control requirements. These distinctions are handled within the common sequencing architecture rather than by separate hardware families. fileciteturn4file8

#### 2.2.3 Package and pinout commonality / differences

The key package difference is between the TEC package and the characterisation package, which use different physical pin arrangements and require explicit remapping. The recommended approach is one primary headboard with a passive interposer or adapter for the characterisation package, governed by a formal pin-mapping matrix covering functional nets, package pins and notes on grounds, reserved nodes and commoned signals. fileciteturn4file10turn4file11

---

## 3. MECHANICAL AND PACKAGE INTERFACE

The mechanical interface must simultaneously satisfy package accommodation, electrical contact quality, thermal contact to the cold finger and optical access. These requirements are coupled, so the mounting concept is treated as a system function rather than an isolated fixture detail. fileciteturn4file10

### 3.1 Characterisation Package Interface

The characterisation package is treated as a supported variant through a controlled adaptation strategy rather than by compromising the main headboard layout with dual direct footprints. This preserves routing quality for clocks and video while retaining compatibility. fileciteturn4file10turn4file11

#### 3.1.1 Mechanical interface per AD10 / AD11

Mechanical implementation for the characterisation package should follow the applicable interface drawings and retain controlled alignment, keepout and stack-height definition. The interposer or adaptor concept should be tied directly to those drawings and controlled as a formal part of the package interface solution. fileciteturn4file11

#### 3.1.2 Electrical interface overview

Electrically, the characterisation package path should behave as a remapped extension of the primary detector interface. Fast clocks and video paths require short routing, continuous reference return, controlled grounding and avoidance of unnecessary stubs. This is one of the reasons the interposer route is preferred over a dual-footprint main board. fileciteturn4file11

### 3.2 Device Mounting and Clamping

The mounting and clamp arrangement must produce repeatable thermal pressure, reliable electrical registration and unobstructed illumination. The preferred concept is a perimeter clamping approach with controlled spring force. fileciteturn4file10

#### 3.2.1 Clamp concept

A perimeter clamp using controlled spring loading provides a repeatable and reviewable mounting concept. It reduces local package stress, supports consistent thermal contact and avoids a central obstruction above the active optical area. fileciteturn4file10

#### 3.2.2 Contact strategy

Contact strategy is based on positive alignment and repeatable compression rather than relying on uncontrolled pressure. Electrical contact, thermal transfer and mechanical location should all be deliberate design functions, not secondary consequences of assembly force. A thin thermal interface layer is recommended to improve heat transfer while accommodating minor surface variation. fileciteturn4file10

#### 3.2.3 Heritage from CCD47-20

The design rationale allows heritage-style thinking where proven clamp and cold-finger practices from earlier detector systems can reduce risk, provided those practices are captured explicitly rather than assumed implicitly. Where heritage is claimed, the report should identify what is inherited and what is modified for CCD381/CCD385 package and optical constraints. This follows the same overall philosophy already established in the working design narrative: preserve what is proven, but document it clearly. fileciteturn4file8turn4file10

#### 3.2.4 Optical clearance discussion

Optical clearance must be maintained by keeping clamp features and support hardware outside the illumination path. The mechanical evidence for this should include clear optical keepout views and fit checks showing that mounting, cable strain relief and package adaptation do not obstruct the active region. fileciteturn4file10

### 3.3 Headboard Storage and Handling

The development material also identifies the need for safe storage and handling where multiple headboards or fixtures are required. This is a practical but important part of repeatable lab use and design protection. fileciteturn4file8

#### 3.3.1 ESD protection

Where multiple boards are required, ESD-safe storage should be provided using proper shielding packaging and controlled handling arrangements. This supports both device protection and orderly configuration control. fileciteturn4file8

#### 3.3.2 Physical protection

Physical protection should prevent connector damage, bent pins, contamination and board handling damage. The design narrative already points toward labelled, dedicated storage rather than informal bench storage. fileciteturn4file8

#### 3.3.3 Multi-headboard accommodation

If programme execution requires multiple headboards, breakout fixtures or special metrology boards, the storage and handling solution should treat them as a controlled set, with clear identity, revision state and protection arrangement. fileciteturn4file8

---

## 4. ELECTRONICS ARCHITECTURE

The headboard electronics are partitioned into three broad functions: clock generation and shaping, bias generation and high-voltage rail handling, and video/output chain processing. This partitioning was explicitly identified in the development material as the cleanest way to avoid design overload and to support structured review. fileciteturn4file0turn4file3

### 4.1 Headboard Overview

The headboard is not a simple carrier PCB; it is a mixed-signal detector interface containing multiple voltage domains, selectable behaviour and test-oriented features. The architecture therefore favours disciplined partitioning, controllability and reviewable configuration rather than ad hoc integration. fileciteturn4file3

#### 4.1.1 Functional partitioning:

The functional partitioning is: clock generation and shaping; bias generation and high-voltage rails; video and analog front end; test access; and monitoring. This decomposition provides a practical framework for both design review and verification planning. fileciteturn4file0turn4file3

### 4.2 Obsolescence Considerations

Early-selected parts that are hard to replace later in the design cycle require lifecycle assessment and formal reporting by PDR. This applies especially to clock drivers, DACs, ADCs, FPGA devices, regulators, specialised switches, connectors and any niche high-voltage components. fileciteturn4file10

#### 4.2.1 Summary of component lifecycle checks

Lifecycle checks should identify whether key components are active, constrained, ageing, or at risk of obsolescence, and whether credible alternates or second-source options exist. The output should be a controlled obsolescence review artefact rather than a loose note set. fileciteturn4file10

#### 4.2.2 Risks and mitigations

Mitigations include alternate component identification, avoidance of fragile single-source choices where practical, and explicit acknowledgement of parts that are early-locked because of mechanical or high-voltage constraints. The evidence expected is the obsolescence report itself plus supporting supply-chain or manufacturer data. fileciteturn4file10

---

## 5. OUTPUT CHAIN DESIGN

The output chain must support both high-headroom operation for full-well work and higher-gain operation for low-signal measurements such as noise and dark current. It must also preserve overscan integrity and allow automated waveform analysis. fileciteturn4file10turn4file7

### 5.1 Gain Architecture

The working design narrative recommends a staged analog chain rather than forcing the full gain span into a single amplifier stage. This is the cleanest way to preserve headroom, bandwidth and noise performance. fileciteturn4file10

#### 5.1.1 Gain stages

A low-noise front-end stage should feed a programmable gain stage. This staged approach allows x1 operation to remain clean while still enabling higher gain settings without extreme resistor ratios or unnecessary noise penalty. fileciteturn4file10

#### 5.1.2 Gain range

The output chain is intended to support gain settings from x1 to x24, with selectable operating points chosen to support the required measurement modes. fileciteturn4file10

#### 5.1.3 Full-well accommodation

The x1 path should be a true unity or near-unity path to preserve full-well headroom and demonstrate that signals above 400,000 electrons can be measured without clipping. Verification should include gain calibration, linearity checks and full-well headroom confirmation. fileciteturn4file10

### 5.2 AC Coupling and RC Time Constants

The AC coupling network is a major design sensitivity because it directly affects baseline wander, overscan integrity and settling error at both 50 kHz and 375 kHz readout. The requirement logic captured in the development notes treats this as a controlled high-pass behaviour problem with explicit provision for tuning. fileciteturn4file10

#### 5.2.1 RC calculations

The design intent is to choose an RC time constant long enough that coupling-induced droop and settling error remain insignificant relative to the readout noise over the sampling interval. The requirement-response material emphasises that this is not a minor implementation detail but a governing output-chain design choice. fileciteturn4file10

#### 5.2.2 50 kHz and 375 kHz justification

The design must work across both 50 kHz and 375 kHz operation, which means the AC coupling behaviour must be justified against both pixel periods and against the sampling windows used for reference and signal evaluation. Verification should include overscan-based baseline analysis and settling assessment at both rates. fileciteturn4file10

#### 5.2.3 Adjustment mechanisms (design provision)

The recommended practical mechanism is provision for adjustable capacitance or equivalent tuning by controlled component population, rather than leaving the RC network fixed and hoping for compatibility across all modes. The narrative specifically supports provision for parallel capacitance options or other controlled design adjustments. fileciteturn4file10

### 5.3 Output Monitoring and Image Capture

The system is intended to support not just analog signal transport but structured output observation, including waveform analysis and image reconstruction. This ties directly into the scope-card and Rameses approach. fileciteturn4file7

#### 5.3.1 Scope card / Rameses integration

A dedicated output path compatible with the scope card and Rameses is the preferred architecture for capture and analysis. This output path should be deterministic, documented and suitable for repeated acquisition rather than dependent on manual probing. fileciteturn4file7

#### 5.3.2 OS sampling strategy

Overscan is explicitly valued in the working material because it helps expose settling issues and dark-signal behaviour. The design should therefore preserve overscan in the acquired data path and ensure timing markers or configuration models exist so Rameses can interpret the waveform structure correctly. fileciteturn4file7

---

## 6. CLOCK GENERATION AND SEQUENCING

Clocking is one of the central functions of the headboard architecture. The design must support grouped clock rails, programmable voltage levels, adjustable slew rates and variable timing capability across multiple operating modes. fileciteturn4file0turn4file8

### 6.1 Clock Grouping Strategy

The clocking strategy groups related detector clocks so that common high and low rails can be generated and controlled per function rather than per single line, reducing complexity while maintaining configurability. fileciteturn4file8

#### 6.1.1 Image, Memory, Buffer, Register, Reset, Dump Gate groupings

The design logic distinguishes image, memory, buffer storage, register, reset and gate-related clocks as separate groupings. This grouping philosophy underpins the rail-generation approach and should be captured in a controlled table mapping clock functions to high/low rail pairs and Rameses control objects. fileciteturn4file8

### 6.2 Clock Voltage Generation

Clock high and low rails are intended to be programmable and software-controlled, with the implementation based on DAC-controlled rail generation and regulated output stages. The emphasis in the requirement responses is on controlled, readback-capable rail generation rather than open-loop approximation. fileciteturn4file8

#### 6.2.1 High and low voltage ranges

Clock-high and clock-low ranges must cover the required detector operating envelope, including positive high rails and low rails that may extend slightly negative. The underlying design intent is to handle these as explicit rail-generation problems rather than by informal level-shifting workarounds. fileciteturn4file8

#### 6.2.2 Accuracy expectations

Accuracy expectations are stated at the rail level and should be satisfied through closed-loop regulation, precision feedback networks and, ideally, readback/calibration. The design narrative repeatedly points toward robust control and verification rather than assuming nominal values are enough. fileciteturn4file8

#### 6.2.3 Rameses control

Rameses should act as the user-level control interface for clock rail setting and monitoring, with controlled mapping between user commands and hardware rails. This provides the traceable control path required for repeatable testing and automated configuration. fileciteturn4file8

### 6.3 SLEW RATE CONTROL

Slew-rate control is needed because waveform quality, settling and measurement fidelity are affected by edge speed, and different device modes may prefer different rise/fall behaviour. fileciteturn4file8

#### 6.3.1 Hardware mechanism

The preferred hardware approach is to control slew through the driver input or equivalent controlled shaping mechanism rather than by making the detector-facing high-voltage nodes themselves complicated or noisy. This is consistent with the overall philosophy of preserving the core signal path. fileciteturn4file8

#### 6.3.2 User control path

The user-facing control path should be presented through Rameses as a finite and calibrated set of selectable slew modes, rather than as a vague analog trim. This supports repeatability and traceability. fileciteturn4file8

### 6.4 CLOCK FREQUENCY CAPABILITY

Clock frequency capability must span lower-rate operating modes and higher-rate image clocking, including 24 MHz LiDAR mode. The requirement response material treats this as a sequencer architecture problem, not merely a driver bandwidth problem. fileciteturn4file8

#### 6.4.1 Image, Memory, Buffer, Register, Reset clocks

Different clock groups have different maximum frequency requirements, so the architecture should support grouped timing generation from a common timing engine with mode-specific configuration rather than separate unsynchronised sources. fileciteturn4file8

#### 6.4.2 24 MHz LIDAR mode justification

The 24 MHz LiDAR mode requirement drives the need for sufficiently fine timing granularity and deterministic sequence generation, especially where multiple phase relationships must be maintained. This is one of the clearest arguments for a proper FPGA-based sequencing architecture. fileciteturn4file8

#### 6.4.3 Sequencer tick capability

The requirement responses conclude that the sequencer needs a tick capability on the order of several nanoseconds to support the faster multi-phase timing. The architecture therefore favours a high-rate, synchronous timing engine rather than software-timed or loosely coordinated outputs. fileciteturn4file8

---

## 7. BIAS GENERATION

Bias generation is a primary headboard function and includes both normal detector biases and the flexibility to accommodate commoned nets and externally injected low-noise sources where needed. fileciteturn4file8

### 7.1 Bias Architecture Overview

The headboard should provide regulated, programmable bias outputs for the required detector nodes and should treat these as controlled analog rails with proper setting, monitoring and verification. The narrative specifically covers SS, RD, OD, DD, DDM and OG as key system-interface biases. fileciteturn4file8

#### 7.1.1 System Interface

The system interface for biases should define each bias function, its nominal range and its control/measurement path. This should be captured in a controlled bias configuration table that sits alongside the narrative design report. fileciteturn4file5turn4file8

**SS, RD, OD, DD, DDM, OG**  
These are the core named detector bias functions discussed in the working requirements and design notes. fileciteturn4file8

**Range and accuracy targets**  
The design intent is that each bias rail should be programmable over its required operating range with sufficiently accurate setting and readback to support formal testing. The working narrative recommends closed-loop generation plus readback/calibration where practical. fileciteturn4file8

### 7.2 Bias Commoning Strategy

Some bias variants may be commoned where permitted by the requirements and package mapping. This should be an explicit implementation choice, not an accidental consequence of routing. fileciteturn4file8

**OGA/RDA/ODA treatment**  
Treatment of OGA, RDA and ODA relative to OG, RD and OD should be captured clearly in the implementation documentation, with any commoning reflected in both the electrical schematic and the interface mapping. fileciteturn4file8

**Documentation of implementation choice**  
The report should state whether these nodes are implemented as commoned or independent and reference the controlling artefact that defines that decision. fileciteturn4file8

### 7.3 Auxiliary Bias Inputs

The requirements and design notes identify the need for auxiliary external bias injection for certain rails where external low-noise sources may be beneficial, particularly during investigations or repeated measurement work. fileciteturn4file8

**External bias injection points**  
External injection points should be provided for selected biases such as RD, OD and SS, with a safe and low-noise method of selecting internal versus external sourcing. fileciteturn4file8

**Connector locations**  
These injection points should be brought to deliberate connectors located near the relevant analog distribution region and documented in the test access and system interface material. fileciteturn4file8

### 7.4 Power-On / Power-Off Behaviour

Power-up and power-down behaviour are treated as safety-critical detector interface requirements. The design notes explicitly call for hardware-based safe-state control. fileciteturn4file5

**Zero-bias strategy**  
Biases and clock outputs should default to a forced-safe or disabled condition at initial power-up, using deterministic enable logic, defined pulls and safe DAC/sequencer startup states. This is a hardware behaviour requirement, not something to leave to software timing alone. fileciteturn4file5

**Protection rationale**  
The rationale is to prevent unintended detector stress, accidental out-of-range drive or ambiguous startup behaviour before the system has been deliberately configured. Verification should therefore include power-up tests performed before normal software initialisation. fileciteturn4file5

---

## 8. TEST ACCESS AND MEASUREMENT SUPPORT

A major strength of the headboard concept is that it is not only intended to drive the detector but also to support meaningful debug, characterisation and repeated waveform analysis. Test access therefore forms part of the architecture, not an afterthought. fileciteturn4file5turn4file13

### 8.1 Test Points

The development material recommends a deliberate test access map including DMM-friendly points for DC rails and controlled waveform access for clocks and video. fileciteturn4file5

#### 8.1.2 Multimeter access

All key DC rails should have labelled multimeter access points with local references, allowing repeatable checking of detector biases and rail states without improvised probing. fileciteturn4file5

#### 8.1.3 Oscilloscope access

Representative clocks and the video path should be observable through suitable waveform access points, ideally including controlled monitor taps or coax-based measurement nodes where direct probing would risk disturbing the circuit. fileciteturn4file5

### 8.2 Non-Standard EO Tests

The programme includes special tests such as output impedance, inter-electrode capacitance, capacitance to substrate and output amplifier bandwidth. The design notes are clear that the headboard should enable these tests without necessarily becoming a precision metrology fixture itself. fileciteturn4file13

#### 8.2.1 Output impedance

The headboard should provide access and disconnect features that make output-impedance measurement possible, with the expectation that dedicated fixtures or controlled injection arrangements may be used for the actual metrology. fileciteturn4file13

#### 8.2.2 Inter-capacitance

Inter-electrode capacitance measurement requires the ability to isolate electrodes from their normal drivers and expose them to guarded measurement paths. The design recommendation is to support this through isolation links and breakout strategies. fileciteturn4file13

#### 8.2.3 Amplifier bandwidth

Output amplifier bandwidth should be assessable either directly through the provided video access path or through a dedicated measurement configuration that avoids corrupting the normal operating chain. fileciteturn4file13

#### 8.2.4 Breakout strategy (if required)

The recommended split is clear: keep the primary headboard optimised for normal operation, but include the links, disconnects and access points that allow dedicated breakout or metrology fixtures to perform intrusive measurements when required. fileciteturn4file13

### 8.3 Automated Measurement Support

The design also supports automated waveform analysis rather than relying on repeated manual scope interpretation across multiple devices. This is strongly aligned with the Rameses plus scope-card concept already identified in the development material. fileciteturn4file7

#### 8.3.1 Rationale for automation

Automation is preferred because multiple waveform attributes must be measured repeatedly across many devices, including reference level, reset feedthrough, offset level, settling times and pulse durations. Manual capture would be slow and less repeatable. fileciteturn4file7

#### 8.3.2 Scope card / scripting approach

The preferred implementation is an analysis-grade acquisition path into the scope card, combined with deterministic timing markers and Rameses-based scripting so that waveform regions can be identified, metrics extracted and results stored consistently per device and per mode. fileciteturn4file7

---

## 9. NOISE AND PERFORMANCE CONSIDERATIONS

Noise and measurement integrity influence the design across the video chain, biasing strategy, waveform capture path and test methodology. The output chain, coupling behaviour and auxiliary bias options are all justified partly by noise performance requirements. fileciteturn4file8turn4file7

### 9.1 Noise Measurement Approach

Noise measurement should be treated as a defined system method, not just a by-product of general acquisition. The design notes explicitly tie noise work to gain selection, overscan capture and waveform analysis structure. fileciteturn4file10turn4file7

#### 9.1.1 Bandwidth assumptions

Any quoted noise result should identify the analog bandwidth and measurement path used, because front-end gain, capture bandwidth and filtering materially affect the result. The staged gain architecture and controlled output path are intended to make this measurable and repeatable. fileciteturn4file10

#### 9.1.2 CDS assumptions

Where correlated double sampling assumptions or equivalent waveform segmentation are used, those assumptions should be reflected in the capture model and analysis scripts so that results remain consistent between devices and modes. The waveform automation notes already point toward this kind of formalised region-based measurement. fileciteturn4file7

#### 9.1.3 Primary and auxiliary outputs

If both primary and auxiliary outputs are available, the report should distinguish their intended use and measurement role. This avoids ambiguity when interpreting noise, settling and feedthrough behaviour. The same principle already appears in the design narrative through the emphasis on defined measurement paths instead of ad hoc probing. fileciteturn4file5turn4file7

---

## 10. THERMAL DESIGN

Thermal design is not limited to cold-finger contact; it also includes temperature sensing, uncertainty estimation and the ability to monitor the detector state even when the die itself is not powered. The PT1000 requirement and associated uncertainty discussion are therefore central to the report. fileciteturn4file4turn4file12

### 10.1 Temperature Sensing

The working material explicitly recommends a PT1000-based die or die-proximate temperature monitor with an always-available readout path. fileciteturn4file4turn4file12

#### 10.1.1 PT1000 implementation

The recommended implementation is a PT1000 driven by a precision low-current source, preferably around 100 µA, with 4-wire sensing where feasible, feeding an instrumentation and ADC chain that can also integrate naturally with the wider system monitoring architecture. This keeps self-heating low while allowing fine resolution. fileciteturn4file4turn4file12

#### 10.1.2 Die monitoring without powering

The temperature readout must remain operational without powering the CCD die itself, which implies an always-available analog measurement domain independent of the detector bias rails. Placement is critical: the PT1000 must be thermally bonded close to the die or cold-finger interface, not left on a warm headboard region. fileciteturn4file4turn4file12

### 10.2 TEMPERATURE UNCERTAINTY

The design report must not merely state that temperature is measured; it must estimate the uncertainty of that measurement and distinguish electrical measurement uncertainty from die-to-sensor thermal uncertainty. fileciteturn4file2turn4file9

#### 10.2.1 Error budget

The recommended uncertainty budget includes PT1000 class tolerance, lead resistance where applicable, excitation current accuracy, ADC/reference error, amplifier error, self-heating and thermal gradient between the sensor location and the actual die. This is exactly the structure already set out in the requirement-response material. fileciteturn4file9turn4file12

#### 10.2.1 Heritage and tolerances

Heritage and tolerance arguments can be used, but they must be backed by the actual measurement chain assumptions: RTD class, 2-wire versus 4-wire routing, calibration strategy and estimated thermal delta between sensor and die. The narrative specifically warns against confusing ambient or board temperature with true die temperature. fileciteturn4file9turn4file12

### 10.3 TEMPERATURE CONTROL CAPABILITY

The headboard must support operation in a controlled thermal environment rather than acting as a temperature controller in isolation. It therefore needs to interface cleanly with the cold finger, TEC-related infrastructure and measurement system. fileciteturn4file10turn4file12

#### 10.3.1 −70 °C to +25 °C strategy

The thermal monitoring architecture has been discussed against an operating span down to approximately −70 °C and up to +25 °C. That range drives the PT1000 resistance span, lead-error sensitivity and the need for low self-heating excitation. fileciteturn4file4turn4file12

#### 10.3.2 TEC linkage

Temperature monitoring should be logged alongside the broader operating state, potentially including TEC current and cold-finger temperature, so that detector behaviour can be correlated with thermal conditions during acquisition and verification. fileciteturn4file4turn4file12

---

## 11. PROGRAMMABLE PINOUT AND TIMING

Because the headboard must support multiple package variants and multiple timing modes, flexibility in pin mapping and timing definition is a core design feature rather than a convenience. fileciteturn4file10turn4file11

### 11.1 Pinout Flexibility

Pinout flexibility is provided through controlled adaptation rather than by making the primary headboard ambiguous or over-routed. fileciteturn4file10turn4file11

#### 11.1.1 CCD381 vs CCD385 differences

CCD381 and CCD385 differences should be captured explicitly in the pin-mapping and timing configuration artefacts. These differences are not a reason to fragment the architecture, but they are a reason to maintain strict interface control. fileciteturn4file11

#### 11.1.2 Hardware accommodation

Hardware accommodation is achieved through the main-board plus interposer strategy, together with controlled rail grouping, configurable timing and explicit documentation of commoned or variant-specific nodes. fileciteturn4file10turn4file11

### 11.2 Timing File Adaptation

Timing adaptation should be implemented as a sequencer configuration problem rather than as repeated hardware redesign. The notes already point strongly toward a high-rate programmable timing engine with mode-specific configuration. fileciteturn4file8

#### 11.2.1 Sequencer configuration strategy

The recommended strategy is to retain common sequencing hardware and support device/mode differences through configuration files, timing tables or microcoded sequence definitions. This keeps the hardware stable while allowing CCD381, CCD385, matrix and LiDAR differences to be absorbed by controlled timing data. fileciteturn4file8

---

## 12. POWER DISSIPATION MEASUREMENT

Power dissipation measurement is one of the sample-test themes identified in the design material, and it should be treated as a supported measurement mode rather than an afterthought. fileciteturn4file8

#### 12.1.1 Static and dynamic measurement concepts

Static and dynamic dissipation measurement require access to the relevant supply and bias paths in a way that supports current or voltage-drop observation without disrupting normal operation. The report should identify whether this is handled directly on the headboard or via breakout support. fileciteturn4file8

#### 12.1.2 Design features enabling measurement

Design features that enable measurement may include insertion points, current-sense options, isolation links or fixture paths. As with the more specialised EO tests, the core principle is to keep the normal headboard clean while exposing the right hooks for controlled metrology. fileciteturn4file13

---

## 13. VERIFICATION STRATEGY SUMMARY

The design narrative is only one half of closure. The other half is the deliberate set of evidence items and tests that prove the design decisions have been implemented and that they satisfy the governing requirements. fileciteturn4file5turn4file8

### 13.1 Design evidence → this document

This report provides the design-side evidence narrative: what the system is intended to do, why the architecture has been chosen, and which design artefacts are expected to exist. It should be read alongside the traceability table, interface definitions, rail tables, pin maps, test access schedules, obsolescence review and fixture definitions. fileciteturn4file5

### 13.2 Test evidence → Verification Plan / Test Reports

Formal closure should come from verification planning and test evidence, including mechanical fit confirmation, continuity checks, clock and bias setpoint checks, gain verification, overscan/settling capture, waveform automation results, thermal monitoring validation, power-up safety checks and any dedicated metrology fixture results. fileciteturn4file5turn4file13

---

# Appendix A — Requirements Traceability Table  
## (REQ No. + Derived Description + Closure Sections)

A controlled appendix should list each requirement number, a derived short description, the section(s) of this report that address the requirement, and the linked evidence item or verification route. The existing design narrative already points to the appropriate closure artefacts, including the package pin-mapping matrix, clock rail table, bias configuration table, video gain table, power-up safety note, test access map, characterisation test enablement matrix and obsolescence review. fileciteturn4file5

---

If you want, I can now turn this into a **cleaner final issue version** with tighter wording, a more formal engineering tone, and a compact **Appendix A traceability table written out in full here as well**.

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] AI (2026-03-06 16:17):
Absolutely — below is a **rewritten report body** using your requested structure, with the content reorganised into a more formal CDR narrative and aligned to the technical intent already present in your uploaded report and development notes. fileciteturn4file0 fileciteturn4file5

---

# CCD Test Camera Headboard  
## CDR Design Report and Evidence Narrative

---

## 1. INTRODUCTION

### 1.1 Purpose of the Document
This document provides the design narrative for the CCD Test Camera Headboard at Critical Design Review. Its purpose is to describe the intended architecture, explain the principal design decisions, and show how the design addresses the applicable programme requirements. It is written to support both engineering review and evidence capture, so that design intent, requirement interpretation and expected verification paths are recorded in a single controlled narrative. fileciteturn4file0

### 1.2 Scope
The scope of this document covers the headboard assembly and its immediate interfaces to the detector, the control electronics, the thermal system and the acquisition chain. It addresses mechanical interface, package accommodation, clock generation, bias generation, output chain design, measurement access, thermal sensing, programmable timing accommodation and power measurement support. It does not replace the detailed verification plan, schematics, mechanical drawings or software implementation notes, but is intended to sit alongside those artefacts as the principal design description for review. fileciteturn4file5

### 1.3 Applicable Documents
Applicable documents include the detector interface drawings and control documents for the CCD381 and CCD385 devices, including the characterisation package references AD10 and AD11, the TEC package references, the interface control documentation, the programme test plan, and the associated requirement and evidence matrix. This report also draws on the earlier working development notes that were subsequently restructured into formal requirement responses. fileciteturn4file0

### 1.4 Requirement Traceability Approach
The report has been structured so that each major requirement area is expressed through four linked ideas: requirement interpretation, design response, implementation intent, and evidence pathway. Where a requirement is best satisfied through controlled fixture support rather than direct headboard implementation, that distinction is made explicitly. This document therefore acts as the design-evidence narrative, while the detailed requirement-by-requirement closure is expected to be maintained in the separate traceability matrix. fileciteturn4file9

## 0. REF.
This document should be read in conjunction with the controlled requirement traceability table, applicable detector interface drawings, thermal and mechanical definitions, schematic set, and future verification records. The intention is that no claim in this report stands alone; each is either grounded in design implementation or linked to a defined verification activity. fileciteturn4file9

## Table of Contents
*To be generated automatically in the controlled document issue.*

---

## 2. SYSTEM OVERVIEW

### 2.1 Test Camera Architecture
The CCD Test Camera architecture is centred on a programmable headboard that interfaces the detector to the external control and acquisition electronics. The headboard receives timing and configuration control from the system electronics, generates the required detector clocks and biases, conditions the output video signal, and exposes measurement and debug access sufficient for both normal operation and specialised characterisation. The design philosophy favours controllability, traceability and test access, while avoiding unnecessary compromise in the primary signal path. fileciteturn4file0

### 2.1.2 Block diagram: detector → headboard → clocks/bias → output → digitiser
At system level, the signal and control chain is:

**Detector → Headboard interface → Clock and bias generation → Detector output chain → Scope card / digitiser → Rameses**

The detector is mounted to the headboard and cold-finger arrangement. The headboard provides the applied clocks and biases required for the active detector mode. The detector output is then routed through the defined analogue output chain to the acquisition hardware, with synchronisation and timing signals exported as needed to support image reconstruction and overscan analysis in Rameses. fileciteturn4file0turn4file5

### 2.1.3 Identify where CCD381 and CCD385 diverge and converge
The two detector families converge in the need for a common control philosophy: programmable clocks, programmable biases, output signal conditioning, thermal control and structured measurement access. They diverge in pin assignment, package presentation, and operating mode emphasis, particularly where CCD381 includes LiDAR-oriented clocking requirements at the high-speed end and where the timing interpretation differs across operational modes. The architecture therefore uses common electrical building blocks but preserves flexibility in physical accommodation and timing configuration. fileciteturn4file0turn4file13

### 2.2 Supported Detector Variants
The headboard is intended to support both CCD381 and CCD385 devices, including both TEC and characterisation package forms. The preferred implementation is a primary headboard arrangement aligned to the principal package approach, with controlled accommodation for package variation through interposer or adapter strategy where required. fileciteturn4file5

### 2.2.1 CCD381 and CCD385 summary
CCD381 and CCD385 are both back-illuminated detector variants requiring a controlled set of detector clocks and biases, but they do not present identical interface assignments or timing expectations. The headboard must therefore be sufficiently configurable to support both families without requiring a complete architectural redesign between variants. fileciteturn4file0

### 2.2.2 Matrix vs LIDAR mode distinctions
The system must support lower-frequency matrix operation as well as the higher-speed image clocking associated with CCD381 LiDAR mode. This distinction particularly affects the sequencing architecture, required timing resolution, and confidence that the clock path can support 24 MHz image operation with adequate phase placement and edge control. fileciteturn4file0

### 2.2.3 Package and pinout commonality / differences
Package and pinout differences are treated as controlled interface variations rather than as ad hoc implementation details. Commonality exists at functional-net level, but not at direct package pin level. The design therefore relies on a pin-mapping abstraction and, where appropriate, physical adaptation rather than assuming a single direct shared footprint. fileciteturn4file5

---

## 3. MECHANICAL AND PACKAGE INTERFACE

### 3.1 Characterisation Package Interface
The characterisation package interface is treated as a supported configuration, not as a one-off exception. The design intent is that the electrical and mechanical treatment of the package is documented and repeatable, with the interface governed by the applicable drawings and the corresponding pin mapping. fileciteturn4file5

### 3.1.1 Mechanical interface per AD10 / AD11
Mechanical implementation for the characterisation package is driven from the referenced interface drawings. The headboard or interposer arrangement must preserve the required pin engagement, package support, and physical alignment while avoiding distortion or local stress. CAD fit checks and package-interface definition are expected evidence items. fileciteturn4file5

### 3.1.2 Electrical interface overview
Electrically, the characterisation package interface is governed by a functional-net mapping between detector requirements and headboard signals. This avoids treating the package as a simple connector variant and instead defines it as a controlled interface conversion from package pins to the common signal set used by the headboard architecture. fileciteturn4file0

### 3.2 Device Mounting and Clamping
The mounted detector must maintain thermal contact, electrical contact and optical access simultaneously. The preferred concept is a perimeter clamp arrangement with controlled spring force, selected because it supports repeatable pressure, reduces local package stress and preserves the optical aperture. fileciteturn4file5

### 3.2.1 Clamp concept
A spring-controlled perimeter clamp is the preferred solution. This provides repeatable contact pressure and supports a defined thermal interface to the cold finger while avoiding obscuration of the illuminated detector area. fileciteturn4file5

### 3.2.2 Contact strategy
The contact strategy separates the thermal path, the electrical interface, and the optical keepout. A thin thermal interface layer is used between the detector and cold finger, while the electrical connection is maintained through the package-to-headboard interface. The assembly is intended to avoid reliance on uncontrolled pressure-only electrical contact. fileciteturn4file5

### 3.2.3 Heritage from CCD47-20
The mounting philosophy may draw on proven heritage concepts where similar detector mounting needed to maintain thermal coupling, electrical reliability and optical clearance together. Any such heritage should be explicitly referenced in the controlled design package as justification for clamp geometry, contact pressure approach and optical keepout discipline.

### 3.2.4 Optical clearance discussion
The optical clearance requirement is addressed by keeping the clamping structure at the package perimeter and preserving the central illuminated path. This should be evidenced through layout or CAD views showing the keepout and confirming that the mounting concept does not introduce obscuration or shadowing into the intended optical path. fileciteturn4file5

### 3.3 Headboard Storage and Handling
Where multiple headboards or detector interface variants are required, the handling solution must protect against ESD and physical damage. This is not merely a logistics issue but part of the controlled implementation needed to support repeatable lab use. fileciteturn4file0

### 3.3.1 ESD protection
Storage should use shielding-grade ESD packaging rather than simple antistatic bags, with controlled handling instructions and appropriate labelling for detector-facing assemblies. fileciteturn4file0

### 3.3.2 Physical protection
The physical protection strategy should prevent damage to connectors, package interfaces and exposed test access features. Rigid support, foam restraint or slot-based storage is preferred over loose bag-only storage. fileciteturn4file0

### 3.3.3 Multi-headboard accommodation
If separate headboards, interposers, or test fixtures are used, the storage arrangement should preserve revision identity, test status and physical segregation. This supports both ESD control and configuration control. fileciteturn4file0

---

## 4. ELECTRONICS ARCHITECTURE

### 4.1 Headboard Overview
The headboard provides the electrical interface between detector and support electronics. Its principal functions are programmable clock generation, programmable bias generation, detector output conditioning, integration with Rameses, and provision of test and debug access. The architecture is intentionally partitioned so that normal detector operation is preserved while still allowing intrusive or non-standard measurements through controlled access methods. fileciteturn4file0

### 4.1.1 Functional partitioning
The design is logically partitioned into detector interface, clock path, bias path, video/output chain, thermal monitoring and test access. This partitioning supports both design clarity and requirement traceability, while also making it easier to separate normal operation from special test modes. fileciteturn4file5

### 4.2 Obsolescence Considerations
Obsolescence is treated as a design control activity for early-locked components, particularly those difficult to replace once layout and interface definitions are fixed. The expectation is that clock drivers, DACs, ADCs, regulators, FPGA/CPLD devices and key connectors are reviewed early and tracked through PDR and CDR as applicable. fileciteturn4file5

### 4.2.1 Summary of component lifecycle checks
Lifecycle checks should classify each early-selected component by availability and replacement risk, with a clear indication of whether the part is active, at risk, or requiring an alternate strategy. The review should be maintained as a controlled design artefact, not as an informal procurement note. fileciteturn4file5

### 4.2.2 Risks and mitigations
Mitigations include identifying alternates, avoiding avoidable single-source dependencies, preserving layout flexibility where sensible, and documenting any component choices that would drive disproportionate redesign effort if supply status changed. fileciteturn4file5

---

## 5. OUTPUT CHAIN DESIGN

### 5.1 Gain Architecture
The output chain must support a wide gain range while still allowing full-well measurement at the lowest gain and low-noise dark-current or read-noise analysis at the highest gain. The design intent is therefore a structured gain architecture rather than a single compromised stage. fileciteturn4file0

### 5.1.1 Gain stages
The preferred implementation is a low-noise front end followed by a programmable gain element or equivalent multi-stage arrangement. This permits a robust low-gain path while still supporting high-gain operation for sensitive measurements. fileciteturn4file0

### 5.1.2 Gain range
The required operating range spans approximately x1 to x24. The x1 mode is needed for full-well tests and the high-gain mode for noise and dark-current tests. The gain structure should therefore be intentional, documented and measurable, rather than inferred from component values alone. fileciteturn4file0

### 5.1.3 Full-well accommodation
The lowest gain path must provide sufficient headroom to accommodate a detector signal corresponding to greater than 400,000 electrons without clipping or compressing the output chain. This drives the need for a true low-gain or unity-like path rather than a nominal x1 setting that still sacrifices headroom. fileciteturn4file0

### 5.2 AC Coupling and RC Time Constants
The AC-coupled output chain must not introduce settling or baseline errors that materially affect measurements at the target readout rates. The requirement is therefore not simply to AC couple the signal, but to choose and justify the RC time constant and provide practical tuning provision. fileciteturn4file0

### 5.2.1 RC calculations
The RC design should be based on the actual pixel-rate operating windows and the need to keep droop or baseline shift sufficiently small relative to read noise and overscan interpretation. The chosen values should be traceable to this behaviour and not left as arbitrary nominal selections. fileciteturn4file0

### 5.2.2 50 kHz and 375 kHz justification
Both 50 kHz and 375 kHz operation must be considered explicitly, since the acceptable settling behaviour differs across those regimes. The design rationale should show that the selected or tunable RC network is compatible with both readout cases. fileciteturn4file0

### 5.2.3 Adjustment mechanisms (design provision)
Adjustment is best supported through controlled component options such as parallel capacitor footprints or equivalent stuffing flexibility. This preserves a low-noise implementation while still allowing empirical tuning if the actual detector and front-end behaviour require refinement. fileciteturn4file0

### 5.3 Output Monitoring and Image Capture
The output chain must support not only analogue fidelity but also practical image capture and waveform interpretation in the wider system. This is especially important where overscan analysis has already proven useful for diagnosing settling and dark-signal behaviour. fileciteturn4file0

### 5.3.1 Scope card / Rameses integration
The preferred acquisition methodology is to use the scope card in conjunction with Rameses, with the headboard providing a defined video output path and the relevant timing references needed to reconstruct the image and associated overscan regions. This output must therefore be treated as a deliberate interface, not as an improvised measurement point. fileciteturn4file0turn4file3

### 5.3.2 OS sampling strategy
Overscan sampling should remain visible and interpretable in the image viewer path, with sufficient timing determinism that pedestal levels, settling behaviour and high-dark anomalies can be assessed consistently. The report should make clear that the design preserves OS observability as an intentional feature, not as an accidental by-product. fileciteturn4file0turn4file3

---

## 6. CLOCK GENERATION AND SEQUENCING

### 6.1 Clock Grouping Strategy
Clock voltages are grouped by detector function rather than individually per electrode wherever appropriate. This reduces unnecessary complexity while preserving the configurability required by the detector architecture. fileciteturn4file0

### 6.1.1 Image, Memory, Buffer, Register, Reset, Dump Gate groupings
The headboard should maintain distinct group treatment for the image clocks, memory clocks, buffer-storage clocks, register clocks, reset-related clocks and pulse-type functions such as dump gate and DC reset. This grouping forms the basis for both rail generation and sequencing configuration. fileciteturn4file0

### 6.2 Clock Voltage Generation
Clock high and low levels are generated as controlled rails rather than as incidental by-products of the driver outputs. This supports software-settable operation, repeatability and verification. fileciteturn4file0

### 6.2.1 High and low voltage ranges
High rails are required over approximately +5 V to +15 V, and low rails over approximately –2 V to +2 V, depending on group. The design therefore requires both unipolar and bipolar rail-generation capability. fileciteturn4file0

### 6.2.2 Accuracy expectations
The target rail accuracy is on the order of ±0.1 V. The architecture should therefore be based on DAC-controlled closed-loop generation, with readback and calibration strongly preferred where confidence at temperature and under load is needed. fileciteturn4file0

### 6.2.3 Rameses control
The rails are intended to be set and monitored through Rameses so that detector configuration becomes part of a controlled operating state rather than a manual bench-only adjustment. The software interface should therefore expose intended setpoint control and, where available, readback. fileciteturn4file0

### 6.3 SLEW RATE CONTROL
The clock edge rate must be adjustable across a wide practical range, which is a performance and signal-integrity control requirement rather than merely a convenience feature. fileciteturn4file0

### 6.3.1 Hardware mechanism
The preferred mechanism is to influence slew at the low-voltage driver-control side, for example through selectable series resistive shaping or equivalent pre-driver control, rather than by adding complexity directly into the high-voltage switched path. This gives a more robust and scalable implementation. fileciteturn4file0

### 6.3.2 User control path
User-level selection of slew mode should be exposed through the control environment as a bounded set of defined operating options, rather than as an uncontrolled analogue trim. The measured relationship between setting and achieved edge rate should be recorded as part of verification. fileciteturn4file0

### 6.4 CLOCK FREQUENCY CAPABILITY
The sequencing architecture must support both relatively slow register/reset operation and the much faster image-clock case, including the LiDAR-related image clock requirement. fileciteturn4file0

### 6.4.1 Image, Memory, Buffer, Register, Reset clocks
The design must accommodate the required operating ranges for image, memory, buffer, register and reset functions. This is fundamentally a sequencer and timing-resolution problem rather than only a driver-speed issue. fileciteturn4file0

### 6.4.2 24 MHz LIDAR mode justification
The 24 MHz image clock requirement, particularly in multi-phase operation, justifies a sequencer architecture with sufficiently fine time quantisation to place edges deterministically. This is one of the principal reasons a simple low-rate divider-only approach is not sufficient. fileciteturn4file0

### 6.4.3 Sequencer tick capability
The timing engine should operate from a sufficiently high internal timebase to realise the required edge placement granularity. The development notes identify the need for roughly 7 ns tick capability as a defensible basis for the high-speed image sequence. fileciteturn4file0

---

## 7. BIAS GENERATION

### 7.1 Bias Architecture Overview
The headboard must provide the required detector bias lines with controlled range, accuracy and monitoring potential. These include SS, RD, OD, DD, DDM and OG, with both unipolar and bipolar bias behaviour required across the set. fileciteturn4file0

### 7.1.1 System Interface
The system bias interface comprises the programmable generation and delivery of SS, RD, OD, DD, DDM and OG to the detector. Each bias should be treated as a controlled output with traceable setpoint intent and defined measurement support. fileciteturn4file0

**SS, RD, OD, DD, DDM, OG**  
These are the principal detector bias lines required by the interface definition. OG is particularly important because it introduces bipolar generation requirements while other rails drive higher positive-voltage ranges. fileciteturn4file0

**Range and accuracy targets**  
The architecture is expected to support the required ranges and deliver approximately ±0.1 V accuracy at the point of application, preferably with readback-enabled confidence rather than purely open-loop control. fileciteturn4file0

### 7.2 Bias Commoning Strategy
Some related detector bias nodes may be treated as commoned where the detector interface and test intent permit that simplification. This should be an intentional documented choice, not an implicit shortcut. fileciteturn4file0

**OGA/RDA/ODA treatment**  
The notes indicate that OGA, RDA and ODA may be commoned respectively with OG, RD and OD. If this is the chosen implementation, it should be stated clearly in both the design report and the bias configuration table. fileciteturn4file0

**Documentation of implementation choice**  
Whether the commoning is hardwired, link-selectable or treated as a test configuration should be recorded explicitly so that the implementation remains reviewable and traceable. fileciteturn4file0

### 7.3 Auxiliary Bias Inputs
The design should support external injection of selected bias rails where previous test experience has shown benefit, particularly for noise investigations. fileciteturn4file0

**External bias injection points**  
External input support is required for rails such as RD, OD and SS so that cleaner or alternative supplies can be applied without redesigning the headboard. The preferred implementation is through deliberate auxiliary connectors and controlled source selection. fileciteturn4file0

**Connector locations**  
The auxiliary bias connector should be located so that external-supply routing is practical while still preserving good analogue grounding and minimising unnecessary disturbance to the local distribution path. fileciteturn4file0

### 7.4 Power-On / Power-Off Behaviour
Safe-state behaviour at power-up and power-down is an architectural requirement and should be implemented in hardware, not assumed from software sequencing alone. fileciteturn4file9

**Zero-bias strategy**  
At initial power-on, all clocks and biases are intended to remain at or near zero until the system is explicitly configured and enabled. This implies global enable control, defined DAC defaults, and deterministic pull conditions in the sequencing and driver path. fileciteturn4file9

**Protection rationale**  
This approach protects the detector from unintended bias application or clock activity during bring-up, brownout or partial configuration states, and should be demonstrated by direct power-up measurement before normal software control is applied. fileciteturn4file9

---

## 8. TEST ACCESS AND MEASUREMENT SUPPORT

### 8.1 Test Points
Measurement access is treated as a design feature, not as an afterthought. The hardware should provide deliberate access for both DC and waveform measurement. fileciteturn4file9turn4file14

### 8.1.2 Multimeter access
All key DC rails should have labelled DMM-friendly access points with nearby reference grounds. The access should be physically usable in a lab setting and should not rely on unstable probe placement onto small or ambiguous pads. fileciteturn4file14

### 8.1.3 Oscilloscope access
Representative clocks and the video chain should have controlled scope access, preferably through coax launches or attenuated monitor taps where direct probing would risk disturbing the operating node. The measurement path should be part of the design map and not improvised during test. fileciteturn4file9turn4file14

### 8.2 Non-Standard EO Tests
The headboard must support a number of non-standard electrical-optical support tests either directly or through dedicated fixtures. The design should therefore distinguish between “headboard supports access” and “headboard itself performs the metrology.” fileciteturn4file8

### 8.2.1 Output impedance
Output impedance measurement is best supported by providing an injection or access point that allows the detector output node to be characterised without conflating the result with the entire downstream chain. This may require a disconnect option or defined measurement fixture. fileciteturn4file8

### 8.2.2 Inter-capacitance
Inter-electrode capacitance measurements require the ability to isolate detector electrodes from the normal driver network so that the measurement reflects the detector rather than the supporting circuitry. Links, resistive isolation points or fixture support are therefore expected. fileciteturn4file8

### 8.2.3 Amplifier bandwidth
Output amplifier bandwidth should be measurable through a controlled output access path, ideally with known load conditions and, where necessary, the ability to de-embed the downstream front end. fileciteturn4file8

### 8.2.4 Breakout strategy (if required)
Where intrusive measurement would unduly compromise the main headboard, breakout fixtures or metrology-specific adapters are the preferred solution. This preserves the main design while still satisfying the characterisation requirement. fileciteturn4file8turn4file9

### 8.3 Automated Measurement Support
The wider system already points toward semi-automated or automated acquisition and analysis. The headboard should support that approach by exposing deterministic access points and timing references. fileciteturn4file3

### 8.3.1 Rationale for automation
Automation improves repeatability, throughput and evidence capture, especially where multiple settling, pedestal or overscan-related metrics must be extracted over repeated runs. fileciteturn4file3

### 8.3.2 Scope card / scripting approach
The preferred route is the use of the scope card and Rameses as the primary automated measurement path, supported by deterministic timing markers and a stable output tap. Manual scope checks remain useful as cross-checks for algorithm confidence. fileciteturn4file3

---

## 9. NOISE AND PERFORMANCE CONSIDERATIONS

### 9.1 Noise Measurement Approach
Noise performance should be considered at architecture level rather than only at final test stage. This includes gain selection, bandwidth control, output-chain fidelity, clock integrity, bias cleanliness, and the relationship between the primary signal path and any auxiliary monitoring outputs. fileciteturn4file0

### 9.1.1 Bandwidth assumptions
Noise interpretation depends on the effective bandwidth of the measurement path. The report should therefore make explicit the assumed bandwidth associated with the selected gain mode, analogue chain configuration and measurement route.

### 9.1.2 CDS assumptions
Where correlated double sampling or equivalent timing-based signal extraction is assumed by the acquisition chain or later analysis, that should be stated clearly. Otherwise there is a risk that read-noise claims are conflated with broader front-end behaviour.

### 9.1.3 Primary and auxiliary outputs
If both a main output and auxiliary or monitor outputs exist, the design report should distinguish their intended roles. Auxiliary taps may be suitable for measurement and debug without being treated as performance-equivalent to the primary science path.

---

## 10. THERMAL DESIGN

### 10.1 Temperature Sensing
Thermal performance is not limited to physical cooling; it also requires reliable measurement of the detector temperature in a form suitable for control, logging and evidence capture. The development notes strongly support implementation of a PT1000-based sensing path associated with the detector or cold-finger assembly, remaining operational even when the detector itself is unpowered. fileciteturn4file2turn4file6

### 10.1.1 PT1000 implementation
The preferred implementation is a PT1000 measured using a precision low-current excitation, nominally around 100 µA, with 4-wire sensing where feasible. The measurement chain should use a precision current source, suitable amplifier stage and ADC, with the resulting temperature logged in Rameses. This same precision monitoring architecture may also support bias monitoring functions. fileciteturn4file2turn4file6

### 10.1.2 Die monitoring without powering
The temperature monitoring path should remain operational when the detector itself is not biased or clocked. This ensures thermal state can be observed during idle, precondition, and controlled power-up phases and supports the requirement to monitor die-related temperature without requiring the detector to be electrically active. fileciteturn4file2turn4file6

### 10.2 TEMPERATURE UNCERTAINTY
The report should explicitly estimate the uncertainty associated with reported temperature, not merely provide measured values. The notes identify both electrical uncertainty and die-to-sensor thermal uncertainty as relevant contributors. fileciteturn4file1turn4file7turn4file10

### 10.2.1 Error budget
The uncertainty budget should include RTD interchangeability, lead resistance where relevant, excitation current tolerance and drift, ADC/reference/amplifier contribution, self-heating, and die-to-sensor thermal gradient. The notes identify PT1000 slope and typical contributor magnitudes as the practical basis for such a budget. fileciteturn4file1turn4file7turn4file10

### 10.2.1 Heritage and tolerances
Class A versus Class B RTD selection, 2-wire versus 4-wire measurement, and whether single-point or two-point calibration is used materially affect the credible uncertainty statement. The report should therefore state the chosen implementation explicitly and avoid generic temperature claims detached from the actual sensing chain. fileciteturn4file1turn4file11

### 10.3 TEMPERATURE CONTROL CAPABILITY
The thermal design must not only measure temperature but support control over the required operating range for the detector package where TEC cooling is used. The notes identify –70 °C to +25 °C and ±0.5 °C control accuracy as the relevant performance intent for the peltier package case. fileciteturn4file11turn4file12turn4file13

### 10.3.1 −70 °C to +25 °C strategy
A credible strategy is based on accurate PT1000 measurement, low-drift analogue readout, calibrated interpretation and a suitable control loop, with thermal margin justified against hot-side boundary conditions. The notes point toward a slow, stable control philosophy rather than an aggressive electrically noisy implementation. fileciteturn4file11turn4file12

### 10.3.2 TEC linkage
The detector TEC and its drive method should be treated as part of the system thermal control architecture. The notes specifically warn against noisy drive methods that could compromise detector performance, and recommend a more stable closed-loop control path with continuous logging and validation across soak conditions. fileciteturn4file12turn4file13

---

## 11. PROGRAMMABLE PINOUT AND TIMING

### 11.1 Pinout Flexibility
The programme requirement for programmable pinout is interpreted not as a mechanical request but as a logical-routing and timing-abstraction requirement. The hardware should therefore avoid locking the detector family to a fixed semantic assignment inside the sequencing chain where practical. fileciteturn4file13

### 11.1.1 CCD381 vs CCD385 differences
CCD381 and CCD385 may require different logical assignment of clock or control functions even where the broader architecture remains common. This means the timing system must support remapping at configuration level rather than assuming one immutable detector identity in hardware. fileciteturn4file13

### 11.1.2 Hardware accommodation
Hardware accommodation may be achieved through a structured routing abstraction between sequencer outputs, driver channels and detector pins, with the final mapping governed by configuration data and documentation. If that path is hardwired without abstraction, the programmability claim becomes weak. fileciteturn4file13

### 11.2 Timing File Adaptation
Timing-file adaptation is the software and control-system complement to the programmable pinout strategy. The sequencing architecture should support the use of detector-specific timing definitions without needing a different hardware concept for each detector family. fileciteturn4file13

### 11.2.1 Sequencer configuration strategy
The preferred strategy is to keep the sequencing engine generic and detector-agnostic at core level, with detector-specific behaviour expressed in controlled timing files or equivalent configuration artefacts. This preserves reuse while still allowing functional divergence between CCD381 and CCD385 modes. fileciteturn4file13

---

## 12. POWER DISSIPATION MEASUREMENT

### 12.1.1 Static and dynamic measurement concepts
The system must support measurement of both static and dynamic detector power. The notes identify the use of voltage drop across series load or shunt resistors as the practical and already-proven method. Static power corresponds to quiescent bias conditions, whereas dynamic power includes the incremental demand associated with active clocking or readout. fileciteturn4file3

### 12.1.2 Design features enabling measurement
To enable this, the design should incorporate defined current-measurement points on the relevant rails, ideally through low-value series shunts with controlled sense access. The measurement arrangement should support both slow DMM-based static power assessment and, where needed, time-varying observation of dynamic current or power envelopes. fileciteturn4file3

---

## 13. VERIFICATION STRATEGY SUMMARY

### 13.1 Design evidence → this document
This document provides the structured design argument for the headboard concept. It captures design intent, requirement interpretation and implementation philosophy across the major requirement themes, and is intended to be used as the narrative backbone for CDR. fileciteturn4file0turn4file9

### 13.2 Test evidence → Verification Plan / Test Reports
Closure of the design claims requires complementary evidence in the form of pin-mapping tables, rail setpoint sweeps, gain verification, power-up safety tests, thermal validation, timing captures, special-test enablement records, and final verification reports. This report therefore does not claim closure by prose alone; it defines what the design is intended to do and where evidence is expected to come from. fileciteturn4file9

---

## Appendix A — Requirements Traceability Table  
**(REQ No. + Derived Description + Closure Sections)**

The traceability appendix should list each governing requirement, its derived engineering interpretation, the section or sections in this report that address the design response, and the downstream evidence source expected to close verification. The uploaded report already identifies the need for supporting artefacts such as the package pin-mapping matrix, clock rail table, bias configuration table, gain table, power-up safety note, test access map, characterisation test enablement matrix and obsolescence review. Those artefacts should be referenced directly from this appendix. fileciteturn4file9

---

If you want, I can now turn this into a **tighter final issue version** with:
**formal engineering wording, no commentary tone, and a compact Appendix A traceability table written directly in chat.**
