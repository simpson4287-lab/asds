# Altium Logo Usage Rules
Date (UTC): 2026-04-20 14:09
Conversation ID: 69e6338f-2570-83eb-bc0d-1ec612e9971f
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-20 14:09):
Can I use altium logo on a design checklist? Sort of a capability marking

[M2] AI (2026-04-20 14:09):
I’m checking Altium’s current brand/trademark guidance rather than guessing, because logo-use rules are exactly the kind of thing that can change.

[M3] AI (2026-04-20 14:09):
Probably **not without permission**.

I could not find a public Altium page that grants general permission to use the **Altium logo** as a capability badge on your own checklist, while Altium’s site makes clear that its content and branding are protected by trademark laws, and its trademark notices state that trademark rights remain with Altium. citeturn259956search0turn259956search2turn259956search15

So for a design checklist, the safer position is:

- **Do not use the Altium logo** as a “capability marking” or endorsement-style badge.
- **Do use plain text** such as:
  - “Created using Altium Designer”
  - “Altium Designer workflow”
  - “Compatible with Altium Designer deliverables”
- Better still, add a disclaimer like:
  - “Altium and Altium Designer are trademarks of Altium. This checklist is an independent internal document and is not endorsed by Altium.”

That keeps you in descriptive territory rather than looking like official branding or certification. Altium’s documentation does show that the software can place logos/graphics in designs, but that is a **technical capability**, not permission to use Altium’s own trademarks on your materials. citeturn259956search3turn259956search6

Best practical answer: **text reference yes, logo badge no, unless you have written brand-use permission from Altium**. If you want, I’ll draft a few safe “capability marking” wordings that look professional without crossing the line.

[M4] ME (2026-04-20 14:21):
On my review sheet I want to add some comments to gates. When the mouse hovers over it displays them. I want it to be a good print as to what the outcomes of stage stage are. What we ware checking, why it’s important. This is for engineering use so it doesn’t want to be dumb but it wants to be light enough to really be through provoking etc 

The stages are

requirements
 library
Schematic
Placement
Interface alignment both mech and electrical (we’ve been burnt)
Layout / routing
Datapack 

Can you compile the summary for review



[M5] AI (2026-04-20 14:21):
Yes. A good approach is to make each hover note read like a **mini review intent statement** rather than a checklist item. For engineering use, I would keep each one to three parts:

**What this gate is confirming**  
**Why it matters**  
**What failure looks like if missed**

That gives enough weight without turning it into a wall of text.

Below is a polished set you can drop into hover comments.

---

## Requirements

**Purpose**  
Confirms the design intent is defined clearly enough to drive implementation and review. Checks that functional, electrical, mechanical, environmental, interface, and verification requirements are captured, bounded, and internally consistent.

**Why it matters**  
Weak or ambiguous requirements do not stay abstract for long; they propagate into wrong part choices, unsuitable interfaces, missing test coverage, and late-stage redesign. This gate is where avoidable downstream churn is either prevented or silently authorised.

**Review focus**  
Check that requirements are specific, testable, traceable, and prioritised. Confirm assumptions, constraints, operating modes, external dependencies, and acceptance criteria are explicit.

---

## Library

**Purpose**  
Confirms that symbols, footprints, models, parameters, lifecyle states, and supply-chain data are correct, complete, and suitable for release use.

**Why it matters**  
Library errors are deceptively expensive because they appear authoritative and then replicate quickly through the design. A single bad pin mapping, pad pattern, MPN, voltage rating, or package assumption can invalidate otherwise sound engineering.

**Review focus**  
Check symbol-to-footprint consistency, pin mapping, electrical types, polarity/orientation, manufacturer part linkage, key parameters, approved status, and any special assembly or inspection notes.

---

## Schematic

**Purpose**  
Confirms the circuit architecture is technically sound and that the schematic communicates intent clearly enough for implementation, review, debug, and future maintenance.

**Why it matters**  
The schematic is the primary statement of electrical intent. If the design is only “functionally there” but lacks clarity, rationale, or discipline, errors become harder to detect and much harder to diagnose once embodied in layout or hardware.

**Review focus**  
Check topology, biasing, protection, margins, control philosophy, interface treatment, power integrity provisions, net naming, design partitioning, and whether the schematic tells the truth about how the design is meant to behave.

---

## Placement

**Purpose**  
Confirms the physical arrangement of parts supports electrical performance, manufacturability, serviceability, thermal behaviour, and mechanical integration.

**Why it matters**  
Good placement is where much of the board quality is decided before routing begins. Poor placement forces compromise into routing, return paths, noise behaviour, assembly access, connector usability, and thermal performance.

**Review focus**  
Check functional grouping, critical path proximity, connector orientation, keepouts, mechanical clearances, thermal spread, access for probing/rework, and whether the placement reflects how the circuit actually needs to operate.

---

## Interface Alignment — Mechanical and Electrical

**Purpose**  
Confirms that all interfaces to the wider assembly are aligned in both geometry and behaviour: connector positions, mounting features, stack heights, pinouts, signal definitions, voltage domains, timing assumptions, and grounding strategy.

**Why it matters**  
This is a classic high-cost failure point because each side can be internally correct yet mutually incompatible. Mechanical and electrical misalignment often escapes until integration, where the penalty becomes delay, rework, credibility loss, and sometimes hardware damage.

**Review focus**  
Check mating-part assumptions, pin numbering conventions, orientation, datum strategy, tolerances, cable/loom realities, interface control documentation, voltage compatibility, sequencing, and fault consequences of incorrect connection.

---

## Layout / Routing

**Purpose**  
Confirms that the PCB implementation preserves the design intent through controlled routing, return path discipline, power distribution, isolation, and manufacturable detail.

**Why it matters**  
A correct schematic can still become a poor product if the board implementation introduces coupling, impedance problems, ground disruption, crosstalk, thermal concentration, or assembly risk. This gate checks whether the realised hardware still deserves trust.

**Review focus**  
Check current paths, return paths, layer usage, decoupling implementation, controlled impedance where relevant, sensitive-node treatment, creepage/clearance, noise segregation, shielding/guarding if required, via strategy, and manufacturability.

---

## Datapack

**Purpose**  
Confirms the released design is supported by a coherent, accurate, and usable data set for manufacture, assembly, inspection, test, integration, and future change control.

**Why it matters**  
A technically good design can still fail organisationally if the release package is incomplete, inconsistent, or ambiguous. The datapack is what turns design effort into repeatable execution and controlled product knowledge.

**Review focus**  
Check drawings, fabrication data, assembly data, BoM integrity, revision consistency, approved deviations, interface documents, test notes, programming data, special build instructions, and whether another competent team could build and support the item without tribal knowledge.

---

## Shorter hover versions

If your hover popup needs to be tighter, use these:

**Requirements**  
Are the requirements clear, testable, traceable, and sufficient to constrain the design properly? This gate prevents ambiguity from becoming rework.

**Library**  
Are the parts truly correct in symbol, footprint, parameters, and lifecycle status? Library errors replicate quickly and undermine the whole design.

**Schematic**  
Does the circuit make technical sense, and does the schematic communicate intent clearly? This is the core expression of electrical design quality.

**Placement**  
Are components positioned to support performance, manufacture, thermal behaviour, and integration? Poor placement creates avoidable downstream compromise.

**Interface Alignment**  
Do the electrical and mechanical interfaces genuinely match the wider system? Internal correctness is not enough if mating assumptions are wrong.

**Layout / Routing**  
Has the board implementation preserved design intent in real physical form? Routing quality determines whether the circuit behaves as designed.

**Datapack**  
Is the release package complete, consistent, and usable by others? A design is not truly ready until it can be built, checked, and supported from the data.

---

## A slightly sharper engineering tone

If you want them a bit more thought-provoking and less passive, this style works well:

**Requirements**  
Have we defined the problem tightly enough that the design cannot drift into assumption-led interpretation?

**Library**  
Are we building from trusted parts data, or are we allowing hidden errors to enter under the guise of library authority?

**Schematic**  
Does the design merely connect, or does it show clear, defensible engineering intent?

**Placement**  
Have we arranged the board around function and physics, or are we leaving routing to compensate for weak placement decisions?

**Interface Alignment**  
Are we certain this design matches the real system at the points that matter most: fit, pinout, polarity, voltage, timing, and grounding?

**Layout / Routing**  
Has the physical implementation protected the circuit’s integrity, or introduced avoidable risk through geometry and return-path neglect?

**Datapack**  
Could another competent team build, inspect, integrate, and support this design without needing verbal explanation?

---

My recommendation would be:
- use the **shorter hover versions** for the live sheet
- keep the **full versions** in a side legend or review guidance tab

I can also turn this into:
1. **single-line tooltip text**
2. **medium-length hover text**
3. **formal gate criteria wording**

so it matches however your review sheet is laid out.

[M6] ME (2026-04-20 15:27):
Can you compress images in a workbook globally

[M7] AI (2026-04-20 15:27):
Yes, usually.

In **Excel**, you can compress images across the workbook like this:

1. Click any picture in the workbook.
2. Go to **Picture Format**.
3. Choose **Compress Pictures**.
4. **Untick** “Apply only to this picture” if you want it workbook-wide.
5. Pick the resolution you want.
6. Confirm.

A few important points:

- This only affects **inserted pictures**, not shapes or charts rendered as vector objects.
- It generally applies to the images embedded in that file, not linked external images in the same way.
- Compression is often **lossy**, so save a copy first if image clarity matters.
- If “Apply only to this picture” is greyed out or behaviour seems inconsistent, it can depend on the image type and Excel version.

If your goal is mainly **file size reduction**, also check:
- **File > Info** for media/file options
- image cropping, because Excel can keep hidden cropped areas unless deleted
- saving as a new workbook after compression

If you want, I can also give you the cleanest settings for **engineering review packs** so screenshots stay readable without bloating the workbook.

[M8] ME (2026-04-20 15:30):
[image]
I think it’s that… if I select lower??
[attached file: IMG_4D5BE849-7EE0-402E-932F-9AC5AFCA18CA.jpeg]

[M9] AI (2026-04-20 15:30):
Yes — **that setting is the global/default image compression target for the workbook selected in that dropdown**.

From your screenshot, you’re in the right place:

**File → Options → Advanced → Image Size and Quality**

What to do:

- Make sure **“Do not compress images in file”** is **unticked**
- Set **Default resolution** lower than 220 ppi if you want more compression

Typical choices:

- **150 ppi** → good compromise for review sheets, screenshots, embedded evidence, and normal printing
- **96 ppi** → strongest size reduction, but can make text in screenshots look a bit soft or fuzzy
- **220 ppi** → fairly safe quality, but not much reduction
- **330 ppi / High fidelity** → little or no useful compression

A couple of important caveats:

1. That setting mainly controls how Excel handles image compression for that file going forward.  
   It does **not always aggressively recompress every existing image already embedded** just from changing the dropdown.

2. To force stronger reduction on existing images, the usual method is:
   - click one picture
   - **Picture Format → Compress Pictures**
   - untick **Apply only to this picture**
   - choose **150 ppi** or **96 ppi**
   - tick **Delete cropped areas of pictures** if appropriate

For your kind of workbook:
- use **150 ppi** first
- save as a **new copy**
- check a few screenshots at 100% zoom
- only go to **96 ppi** if file size is still too large

For engineering screenshots with small text, **150 ppi is usually the sensible floor**. 96 can start to make captured schematics, CAD screenshots, and tables a bit annoying to read.
