# Certification Comparison 61010 FCC
Date (UTC): 2026-05-20 17:26
Conversation ID: 6a0deea4-36bc-83eb-bc46-5557edc8a4fb
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-05-20 17:26):
Compare the certification route between 61010 and fcc

[M2] AI (2026-05-20 17:26):
The two routes are related, but they solve fundamentally different problems and are governed very differently.

- entity["organization","IEC","International Electrotechnical Commission"] / entity["organization","UL","Underwriters Laboratories"] / entity["organization","TÜV Rheinland","TÜV Rheinland Group"] style safety certification:
  - “Will this equipment injure someone, catch fire, arc, overheat, expose mains, or fail dangerously?”
  - That is the world of entity["standard","IEC 61010","Safety requirements for electrical equipment for measurement, control, and laboratory use"].

- entity["organization","Federal Communications Commission","United States"] compliance:
  - “Does this equipment emit too much RF noise or become upset by RF?”
  - That is the world of FCC Part 15 EMC/EMI compliance.

They often happen together on a product, but they are not substitutes for each other.

---

# High-level comparison

| Area | IEC 61010 | FCC |
|---|---|---|
| Purpose | Electrical safety | Electromagnetic emissions |
| Main concern | Shock, fire, energy hazards | Radio interference |
| Region | International basis | United States |
| Typical standards | IEC 61010-1, -2 variants | FCC Part 15 |
| Applies to | Lab, measurement, industrial equipment | Digital electronics with clocks/RF |
| Testing style | Construction + fault analysis + physical tests | EMC chamber measurements |
| Certification route | Often CB/TÜV/UL/NRTL | Supplier Declaration or FCC authorization |
| Focus on mains? | Very heavily | Not necessarily |
| Can low-voltage DC gear still need it? | Sometimes yes | Usually yes if digital electronics present |

---

# IEC 61010 route (Safety)

For your kind of equipment — measurement systems, PXI-integrated instrumentation, detector electronics, evaluation racks — 61010 is the relevant safety family.

Typical path:

## 1. Define product category

You first determine:
- Laboratory equipment?
- Measurement/control equipment?
- OEM subsystem?
- Professional-use evaluation platform?
- Installed system vs standalone product?

This matters enormously because:
- Intended use
- User access
- Operator skill level
- Installation assumptions
all influence the hazard assessment.

For your “B2B evaluation rack powered from approved SELV lab supplies” concept, this framing is strategically important.

---

## 2. Identify applicable standards

Usually:
- entity["standard","IEC 61010-1","General safety requirements for electrical equipment for measurement, control, and laboratory use"]
- Possibly:
  - 61010-2-030 (test circuits)
  - 61010-2-081 (automatic lab equipment)
  - 61010-2-201 (control equipment)

Then supporting standards:
- EMC
- RoHS
- CE directives
- Machinery exclusions/inclusions
- LVD applicability

---

## 3. Perform hazard-based design review

This is the big difference from FCC.

61010 is deeply construction-oriented.

You assess:
- Creepage/clearance
- Insulation coordination
- SELV boundaries
- Fault conditions
- Thermal rise
- Fire enclosure
- Fuse coordination
- Earthing
- Connector accessibility
- Stored energy
- Mechanical hazards
- Operator misuse
- Single-fault conditions

This becomes:
- Risk analysis
- Safety case
- Technical file

---

## 4. Lab testing

Testing can include:
- Hi-pot/dielectric withstand
- Earth bond
- Leakage current
- Temperature rise
- Abnormal operation
- Flammability
- Stability/mechanical tests
- Mains transient testing

This is much more invasive than FCC.

The lab may demand:
- Schematics
- BOMs
- PCB layouts
- safety-critical component evidence
- transformer certs
- fuse datasheets
- enclosure materials
- spacing evidence

---

## 5. Certification / declaration

Depending on route:
- Self-declared CE basis
- CB Scheme
- UL/NRTL listing
- TÜV certification

A lot of professional B2B gear is technically “self declared” but built around tested evidence.

Large customers often expect:
- CB report
- NRTL marks
- or equivalent evidence

especially in institutional/lab environments.

---

# FCC route (EMC/EMI)

FCC is usually much narrower and faster.

For most digital products:
- FCC Part 15 Subpart B
- Unintentional radiator

Applies because:
- clocks
- processors
- LVDS
- Ethernet
- switchers
- FPGA activity
all radiate RF.

---

## Typical FCC path

## 1. Determine device class

Usually:
- Class A:
  - Industrial/commercial/lab
  - Easier limits
- Class B:
  - Residential
  - Harder limits

Your equipment would almost certainly target Class A.

That helps enormously.

---

## 2. Pre-compliance EMC work

You try to avoid:
- Radiated emissions failures
- Conducted emissions failures

This becomes layout/cabling/filtering work:
- shielding
- grounding
- cable terminations
- common-mode control
- enclosure seams
- filter strategy

---

## 3. EMC chamber testing

Typical tests:
- Radiated emissions
- Conducted emissions

Possibly immunity too depending on region/market.

Unlike 61010:
- the lab usually does not deeply inspect your schematics for safety construction.
- they care about RF behaviour.

---

## 4. Supplier Declaration / authorization

For many lab/industrial devices:
- formal FCC certification is not like Wi-Fi certification.
- often Supplier’s Declaration of Conformity is enough.

Intentional transmitters are different:
- Wi-Fi
- Bluetooth
- radios
need stricter authorization.

---

# The practical difference in effort

For a custom instrument:

## FCC pain:
- failing emissions at 200 MHz
- noisy DC/DC converters
- cable radiation
- enclosure seams
- grounding strategy

## 61010 pain:
- proving no hazardous fault exists
- insulation systems
- thermal/fire containment
- accessible energy
- mains segregation
- documentation burden
- safety-critical component traceability

61010 is usually the more architecturally invasive requirement.

FCC is often more iterative/debug-oriented.

---

# Why your “approved external PSU” idea matters

This is exactly why many engineering/evaluation systems:
- externalize mains handling
- use certified lab PSUs
- keep internal rails SELV
- avoid direct AC input

because it dramatically reduces:
- insulation complexity
- fire analysis
- mains spacing burden
- touch hazard scope

That does not automatically eliminate 61010 concerns, but it can radically simplify them.

A low-voltage DC-powered professional subsystem can sometimes sit in a much more manageable compliance position than a fully integrated mains-powered commercial instrument.

---

# Rough real-world comparison

| Aspect | 61010 | FCC |
|---|---|---|
| Engineering impact | Very high | Moderate |
| PCB/layout influence | Medium | Very high |
| Mechanical influence | Very high | Medium |
| Documentation burden | Very high | Moderate |
| Lab time | Longer | Shorter |
| Iteration risk | Moderate | High |
| Cost risk | High | Moderate |
| Often solved by external PSU? | Yes, partially | Not much |

---

# In your specific architecture

Your proposed approach:
- approved external PSU/mainframe
- SELV DC distribution
- professional/B2B evaluation positioning
- rack integration
- no exposed mains handling
- modular PXI/lab instrumentation ecosystem

is actually very aligned with how many advanced lab systems reduce the certification burden.

It does not mean:
“no compliance needed.”

But it can mean:
- dramatically narrower hazard scope,
- clearer intended-use arguments,
- and more defensible technical-file positioning.

[M3] ME (2026-05-20 17:28):
So both are needed for selling to us lab

[M4] AI (2026-05-20 17:28):
Yes — in practice, for a professional lab instrument sold into the entity["country","United States","United States"] market, you normally end up needing both safety and EMC compliance evidence, but the formality and route can vary significantly depending on how the product is positioned.

A simplified view is:

| Requirement | Why it matters |
|---|---|
| entity["standard","IEC 61010","Safety requirements for electrical equipment for measurement, control, and laboratory use"] / NRTL safety | “Is it safe to operate?” |
| entity["organization","Federal Communications Commission","United States"] Part 15 | “Does it create unacceptable RF interference?” |

For a lab customer, procurement, EHS, facilities, or system integration teams often expect evidence for both.

---

# The subtle but important distinction

## FCC is effectively mandatory in the US

If the device contains:
- digital logic,
- clocks,
- FPGA activity,
- Ethernet,
- switchers,
- processors,
- LVDS,
etc,

then FCC emissions compliance is usually legally required before marketing/selling in the US.

Even many quiet industrial devices still fall under Part 15 as “unintentional radiators.”

---

# 61010 is more about market acceptance + liability + institutional policy

This is where nuance appears.

Strictly speaking, not every OEM subsystem absolutely requires formal 61010 certification by law in every scenario.

However:

- universities,
- national labs,
- aerospace customers,
- semiconductor fabs,
- defence integrators,
- industrial R&D labs

often will not deploy equipment lacking recognizable safety evidence.

They may require:
- NRTL listing
- UL mark
- TÜV certification
- CB report
- or documented conformity to 61010

even if not explicitly mandated federally.

So commercially, it becomes “effectively required.”

---

# Typical real-world combinations

## Fully commercial bench instrument

Example:
- oscilloscope
- PSU
- spectrum analyzer

Usually has:
- FCC
- UL/TÜV/NRTL
- IEC 61010
- CE/EMC
- RoHS

Fully formal route.

---

## OEM module / detector electronics / engineering platform

May instead use:
- FCC Class A
- engineering-use labeling
- professional-use restrictions
- external certified PSU
- partial 61010 assessment
- system integrator responsibility split

This is closer to the territory you keep describing.

---

# Your strategy is actually common in advanced instrumentation

Your repeated ideas:
- external certified PSU/mainframe
- SELV-only internal electronics
- professional B2B positioning
- evaluation/development framing
- no direct mains exposure
- modular rack ecosystem

are exactly the sort of architectural decisions companies use to:
- narrow the compliance boundary,
- reduce certification cost,
- reduce safety scope,
- and avoid becoming a “consumer appliance.”

That does not eliminate obligations, but it changes the argument from:

> “We built a standalone mains laboratory appliance”

to:

> “We provide a professional low-voltage subsystem intended for integration and operation within approved laboratory infrastructure.”

That distinction matters a lot.

---

# FCC vs 61010 from a customer perception angle

A customer may never even ask about FCC explicitly because they assume it exists.

But they often WILL ask:
- “Is it UL listed?”
- “Does it comply with 61010?”
- “Can it enter our lab?”
- “Can EHS approve it?”
- “What mains voltages are exposed?”
- “Is it SELV internally?”
- “What happens under fault?”

Especially in aerospace, semiconductor, and radiation-test environments.

---

# Important nuance for your rack concept

If your rack contains:
- a certified entity["company","Keysight Technologies","Keysight Technologies"] PSU/mainframe,
- certified PXI chassis,
- approved AC infrastructure,

and your own electronics are low-voltage internal modules,

then your custom hardware may plausibly sit closer to:
- OEM subsystem,
- measurement accessory,
- engineering development equipment,

rather than:
- standalone mains appliance.

That can materially reduce compliance complexity.

But:
- you still need engineering discipline,
- EMC still matters,
- documentation still matters,
- and product claims must match reality.

---

# The trap many startups fall into

They assume:
> “Low voltage means no compliance.”

That is usually false.

Even a 12 V FPGA system can:
- radiate badly,
- overheat,
- burn cables,
- fail dangerously,
- damage connected infrastructure.

So:
- FCC still appears,
- EMC still appears,
- and safety expectations still appear.

The trick is reducing scope intelligently — not pretending the scope disappears.
