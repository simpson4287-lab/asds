# Library Checklist Examples
Date (UTC): 2026-01-16 03:06
Conversation ID: 6969ab28-453c-832b-8af7-a85f7f8553f2
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-004.json

[M1] ME (2026-01-16 03:06):
For my library checklist I want to get screenshot if the part definition. Would you have some examples?

[M2] AI (2026-01-16 03:06):
Yes — and this is one of those quietly powerful habits that separates *“library seems fine”* from *“library is defensible under audit.”*  
A screenshot isn’t decoration; it’s a **frozen truth claim**. It says *this is what the part meant at the moment I released it.*

Below are **good, concrete examples** of what a “part definition screenshot” should look like, and why each earns its keep.

---

## 1. Schematic Symbol — the *semantic* truth

image_group{"query":["Altium Designer schematic symbol IC","schematic symbol pin names datasheet match","Altium schematic symbol power pins"]}

This screenshot answers one question only:  
**“Does this symbol mean what the datasheet says it means?”**

Include:
- Full symbol visible (no cropped pins)
- Pin numbers and pin names legible
- Power, ground, NC, EP clearly shown
- Any pin grouping or functional blocks visible

Why it matters:  
If a pin is wrong here, everything downstream is fiction. This is the *linguistic definition* of the component.

---

## 2. Footprint (Top View) — the *geometric* truth

image_group{"query":["Altium PCB footprint QFN","PCB footprint pin 1 indicator","Altium footprint courtyard silkscreen"]}

This screenshot answers:  
**“If I place this, will copper meet silicon in the right places?”**

Include:
- Top view of the footprint
- Pin-1 marker clearly visible
- Pad numbers readable
- Courtyard / outline visible if present

Why it matters:  
Most catastrophic library failures live here. This captures orientation, numbering, and physical intent in one frame.

---

## 3. Footprint vs Datasheet Overlay — the *correspondence* proof

image_group{"query":["QFN datasheet footprint comparison","PCB footprint vs datasheet pinout","datasheet land pattern QFN"]}

This screenshot answers:  
**“Did I actually check, or did I assume?”**

Include:
- Datasheet pinout or land pattern
- Footprint visible side-by-side or overlaid
- Matching pin numbers called out visually

Why it matters:  
This is the audit-grade evidence. You are showing that the footprint was *derived*, not guessed.

---

## 4. Component Parameters / Metadata — the *identity* truth

image_group{"query":["Altium component parameters panel","Altium component properties MPN","Altium library parameters footprint link"]}

This screenshot answers:  
**“What exact thing is this supposed to represent?”**

Include:
- Manufacturer name
- Exact MPN (package-specific)
- Package / footprint link
- Datasheet link (visible and correct)

Why it matters:  
Without this, a perfect symbol and footprint can still map to the wrong physical part. Identity drift is subtle and deadly.

---

## 5. 3D Model (Optional but Gold-Standard) — the *sanity* check

image_group{"query":["Altium 3D PCB component view","PCB 3D model QFN","Altium STEP model alignment"]}

This screenshot answers:  
**“Does this exist in the same universe as the PCB?”**

Include:
- 3D view of the part on the board or in isolation
- Body aligned with pads
- Orientation sensible

Why it matters:  
3D catches mistakes that logic and geometry both miss — flipped parts, mirrored footprints, absurd body sizes.

---

## How this fits your **single-pass checklist**

For each released library part, you attach:
- 1–2 symbol screenshots
- 1 footprint screenshot
- 1 datasheet comparison screenshot


[M3] ME (2026-01-16 03:07):
Altium designer 

[M4] AI (2026-01-16 03:07):
Right — **Altium Designer–specific**, no abstraction, no theory fluff. This is about *what you actually screenshot* inside Altium so your library part has a paper trail that would survive a grumpy design review or a future-you interrogation.

Below is a **clean, minimal screenshot set** that works beautifully with your single-pass checklist mindset.

---

## 1. Schematic Symbol (SCHLIB) — logical definition

image_group{"query":["Altium Designer schematic library symbol editor","Altium SCHLIB pin properties","Altium schematic symbol IC pins"]}

**Where in Altium**
- Open the **SCHLIB**
- Open the component
- Zoom so the *entire symbol* is visible

**What must be visible**
- All pins (no scrolling required)
- Pin numbers + pin names readable
- Power / GND / NC pins visible (not hidden)
- Any functional grouping (A/B channels, banks, etc.)

**Why this screenshot exists**
This is the **semantic contract**.  
If a pin is wrong here, the PCB can be perfect and still wrong.

Filename suggestion:  
`MPN_SCHLIB_symbol_v1.png`

---

## 2. Footprint (PCBLIB) — copper reality

image_group{"query":["Altium Designer PCB footprint editor","Altium PCBLIB footprint top view","Altium footprint pin 1 marker"]}

**Where in Altium**
- Open the **PCBLIB**
- Select the footprint
- View in **2D Layout Mode**
- Top view

**What must be visible**
- Pads with numbers readable
- Pin-1 indicator
- Component outline / courtyard (if used)
- Pad shapes clearly visible

**Why this screenshot exists**
This is where most expensive mistakes are born.  
It proves pad numbering, orientation, and intent.

Filename suggestion:  
`MPN_PCBLIB_footprint_top.png`

---

## 3. Footprint ↔ Datasheet Check — correspondence proof

image_group{"query":["QFN datasheet pinout","Altium footprint vs datasheet comparison","datasheet land pattern QFN"]}

**Where in Altium**
Two good options:
- Split screen: Altium footprint + PDF datasheet
- Or annotate the datasheet externally and screenshot both

**What must be visible**
- Datasheet pinout or land pattern
- Matching pad numbers / orientation
- Clear visual alignment (even if informal)

**Why this screenshot exists**
This proves you *checked*, not assumed.  
This is your audit-grade evidence.

Filename suggestion:  
`MPN_footprint_vs_datasheet.png`

---

## 4. Component Parameters (Properties panel) — identity lock

image_group{"query":["Altium component parameters panel","Altium component properties manufacturer part number","Altium library parameters datasheet link"]}

**Where in Altium**
- In SCHLIB or Component view
- Open **Properties / Parameters**

**What must be visible**
- Manufacturer
- Exact MPN (package-specific)
- Footprint name linked
- Datasheet URL

**Why this screenshot exists**
Perfect symbols mapped to the *wrong* MPN are silent killers.  
This locks identity to geometry.

Filename suggestion:  
`MPN_parameters_identity.png`

---

## 5. 3D View (PCBLIB) — sanity check (optional but excellent)

image_group{"query":["Altium Designer 3D PCB view component","Altium STEP model alignment","Altium 3D component view"]}

**Where in Altium**
- PCBLIB
- Switch to **3D Layout Mode**

**What must be visible**
- Body aligned to pads
- Correct orientation
- Reasonable body size

**Why this screenshot exists**
This catches mirrored parts, flipped pin-1s, and absurd scale errors that logic misses.

Filename suggestion:  
`MPN_3D_alignment.png`

---

## Minimal rule set (this fits your checklist style)

For each released part:
- 1 screenshot = symbol
- 1 screenshot = footprint
- 1 screenshot = datasheet comparison
- 1 screenshot = parameters  
(3D is bonus, not mandatory)

If **any screenshot looks ambiguous**, the part isn’t released. No drama — just physics.

If you want, next step is to:
- define a **standard folder structure**, or  
- compress this into a **single “Library Evidence” Excel row** with screenshot links.

[M5] ME (2026-01-16 03:07):
I need some really clear and obvious snaps. Symbol showing parameters, footprint showing parameters, 3d body and parameters 

[M6] AI (2026-01-16 03:07):
Perfect — that narrows it nicely. What you’re asking for is **not** “a nice view”, it’s **forensic screenshots**: one glance, no interpretation, no hunting. The reviewer should be able to say *“yes, that’s the part”* in under three seconds.

Below is a **very literal, Altium-specific capture recipe** for each snap. Think of these as *identity cards*, not illustrations.

---

## 1. SCHLIB — Symbol **with parameters visible**

image_group{"query":["Altium Designer SCHLIB symbol properties panel","Altium schematic library component parameters","Altium schematic symbol with parameters visible"]}

**Altium setup**
- Open **SCHLIB**
- Select the component (not a pin)
- Open **Properties panel**
- Dock Properties on the **right**
- Zoom symbol to fill ~70% of screen

**What must be in frame**
- Entire symbol
- Properties panel showing:
  - Manufacturer
  - MPN
  - Description
  - Footprint link
  - Datasheet link
- Component name visible at top

**This screenshot proves**
> “This logical symbol claims to represent *this exact real-world part*.”

**Common failure to avoid**
- Properties panel cropped
- Scrolling parameters out of view
- Showing only generic fields

**Filename**
`MPN_SCHLIB_symbol+params.png`

---

## 2. PCBLIB — Footprint **with parameters visible**

image_group{"query":["Altium PCBLIB footprint properties panel","Altium footprint editor with properties","Altium PCB footprint parameters visible"]}

**Altium setup**
- Open **PCBLIB**
- Select the footprint
- 2D Layout Mode (top view)
- Properties panel visible

**What must be in frame**
- Footprint pads fully visible
- Pin numbers readable
- Pin-1 marker
- Properties panel showing:
  - Footprint name
  - Component height
  - Courtyard / clearance rules (if used)
  - Linked 3D body count

**This screenshot proves**
> “This geometry is intentional, named, and dimensioned.”

**Common failure to avoid**
- Footprint shown without identity
- No indication which package variant this is

**Filename**
`MPN_PCBLIB_footprint+params.png`

---

## 3. PCBLIB — 3D Body **with parameters visible**

image_group{"query":["Altium 3D body properties panel","Altium PCB 3D view component properties","Altium STEP model properties"]}

**Altium setup**
- PCBLIB
- Switch to **3D Layout Mode**
- Click the **3D Body**
- Properties panel visible

**What must be in frame**
- 3D body clearly visible
- Pads visible underneath
- Properties panel showing:
  - STEP model name
  - Rotation values
  - Offset values
  - Body height
  - Association to footprint

**This screenshot proves**
> “The 3D model is aligned, scaled, and intentionally placed.”

**Common failure to avoid**
- Pretty 3D shot with no metadata
- Model floating or half-cut

**Filename**
`MPN_3Dbody+params.png`

---

## The **golden rule** (important)

Every screenshot must answer **two questions at once**:

1. *What am I looking at?*  
2. *What part does this claim to be?*

If either answer requires scrolling, clicking, or guessing — the snap fails.

---

## Recommended capture layout (works well on reviews)

- Altium full screen
- Symbol / footprint on **left**
- Properties panel on **right**
- No floating dialogs
- No zoomed-in fragments

This creates a repeatable visual language across your entire library.

---

If you want, next we can:
- define **exact parameter names** you mandate (Manufacturer vs Mfr vs MFG)
- or create a **one-page “Library Evidence Standard”** you can literally pin above your desk

[M7] ME (2026-01-16 03:08):
Example of a soic-8

[M8] AI (2026-01-16 03:08):
Good choice. **SOIC-8** is perfect because everyone *thinks* they know it — which is exactly why clear evidence screenshots matter.

Below is a **concrete, visual example set** of what “really clear and obvious” looks like in **Altium Designer**, using an SOIC-8 as the reference. These are not decorative; they’re *identity snapshots*.

---

## 1. SCHLIB — SOIC-8 symbol **with parameters visible**

image_group{"query":["Altium SCHLIB SOIC-8 symbol properties panel","Altium schematic symbol SOIC-8 with parameters","Altium Designer schematic library SOIC-8"]}

**What this snap must show (no exceptions)**  
- Full 8-pin symbol on screen  
- Pin numbers **and** pin names readable  
- Properties panel visible showing:
  - Manufacturer
  - MPN (e.g. `OPA2134UA`, `LM358DR`, etc.)
  - Description
  - Footprint link (`SOIC-8_3.9mm`)
  - Datasheet URL

**Why this matters**  
This locks the *logical meaning* of the part to a real device.  
An SOIC-8 symbol without parameters is just eight lies in a trench coat.

---

## 2. PCBLIB — SOIC-8 footprint **with parameters visible**

image_group{"query":["Altium PCBLIB SOIC-8 footprint properties","Altium footprint SOIC-8 pin 1 marker","Altium Designer PCB footprint SOIC-8"]}

**What this snap must show**
- Entire SOIC-8 footprint (top view)
- All pads visible and numbered 1–8
- Clear pin-1 marker (dot, chamfer, or silk)
- Properties panel showing:
  - Footprint name (`SOIC-8_3.9x4.9mm_P1.27`)
  - Component height
  - Courtyard / clearance info (if defined)
  - Linked 3D bodies count

**Why this matters**  
SOIC-8 comes in *multiple widths*.  
This screenshot proves you didn’t accidentally build a narrow-body fantasy for a wide-body reality.

---

## 3. PCBLIB — SOIC-8 3D body **with parameters visible**

image_group{"query":["Altium SOIC-8 3D body properties panel","Altium PCB 3D view SOIC-8 STEP","Altium Designer SOIC-8 3D alignment"]}

**What this snap must show**
- 3D body clearly visible
- Pads visible underneath
- Correct pin-1 orientation
- Properties panel showing:
  - STEP model name
  - Rotation (X/Y/Z)
  - Offset (X/Y/Z)
  - Body height

**Why this matters**  
This catches the classic horrors:
- mirrored bodies  
- rotated pin-1  
- packages floating 0.5 mm above the board like ghosts  

3D is the lie detector.

---

## The “three-second test”

Hand these three images to another engineer.

If they can’t answer **all three** instantly:
- *What exact part is this?*
- *What exact package is this?*
- *Is pin-1 unambiguous?*

…then the snaps aren’t good enough yet.

---

## Canonical filenames (recommended)

- `MPN_SOIC8_SCHLIB_symbol+params.png`
- `MPN_SOIC8_PCBLIB_footprint+params.png`
- `MPN_SOIC8_3Dbody+params.png`

Order matters. Consistency breeds trust.

---

If you want next, we can:
- define a **parameter whitelist** that must be visible in every snap  
- or build a **one-row Excel template** where each cell links to these three images  

That’s how libraries stop being folklore and start being infrastructure.

[M9] ME (2026-01-16 03:10):
Maybe a better example? How about just a resistor 

[M10] AI (2026-01-16 03:10):
Excellent choice. A **resistor** is even better than SOIC-8 because there is nowhere to hide. If this is clear, *everything* else will be.

Below is a **clean, unmistakable Altium Designer example** for a single resistor (say **10 kΩ, 0603, 1%**) showing exactly what your screenshots should look like.

Think of this as the **baseline specimen** for your whole library.

---

## 1. SCHLIB — Resistor symbol **with parameters visible**

image_group{"query":["Altium SCHLIB resistor symbol properties panel","Altium schematic resistor parameters","Altium Designer schematic library resistor"]}

**Altium setup**
- Open **SCHLIB**
- Select the resistor component (not a pin)
- Properties panel docked on the **right**
- Symbol centred, filling most of the left side

**What must be visible in one shot**
- Entire resistor symbol
- Designator (R?)
- Value field visible (`10k`)
- Properties panel showing clearly:
  - Comment / Value = `10k`
  - Tolerance = `1%`
  - Power rating = `0.1W`
  - Package = `0603`
  - Footprint link = `RES_0603`
  - Datasheet / family reference (if used)

**What this proves**
> “This logical thing claims to be a **10 kΩ 0603 resistor**, not ‘some resistor’.”

If the value or package isn’t visible here, the snap fails.

---

## 2. PCBLIB — Resistor footprint **with parameters visible**

image_group{"query":["Altium PCBLIB 0603 resistor footprint properties","Altium footprint resistor 0603","Altium Designer PCB library resistor footprint"]}

**Altium setup**
- Open **PCBLIB**
- Select footprint `RES_0603`
- 2D Layout Mode (top view)
- Properties panel visible

**What must be visible**
- Both pads fully visible
- Pad numbers readable (1 and 2)
- Courtyard / outline visible (if you use one)
- Properties panel showing:
  - Footprint name = `RES_0603`
  - Pad dimensions
  - Component height
  - Solder mask / paste settings (summary view)

**What this proves**
> “This footprint is intentionally a **0603** and not a scaled accident.”

This is where silent errors usually live: wrong pad length, wrong gap, wrong height.

---

## 3. PCBLIB — 3D body **with parameters visible**

image_group{"query":["Altium resistor 0603 3D body properties","Altium PCB 3D view resistor","Altium Designer 3D body resistor properties"]}

**Altium setup**
- Same PCBLIB
- Switch to **3D Layout Mode**
- Click the **3D body**
- Properties panel visible

**What must be visible**
- 3D resistor body on pads
- Pads visible underneath
- Correct orientation (centred, not floating)
- Properties panel showing:
  - Body type (Extruded / STEP)
  - Length / width / height
  - Z offset = sane (≈0)
  - Rotation = sane (0/0/0)

**What this proves**
> “This part occupies physical space realistically.”

If the body floats, sinks, or clips, your library is lying to MCAD and assembly.

---

## Why the resistor is the *perfect* standard

A resistor snapshot should let someone answer instantly:
- What value is it?
- What size is it?
- What footprint will be placed?
- Does the physical body make sense?

If they can’t do that in **three seconds**, the screenshot is not clear enough.

---

## Gold-standard consistency rule

Every part — resistor, op-amp, FPGA — follows the **same three snaps**:
1. Symbol + parameters  
2. Footprint + parameters  
3. 3D body + parameters  

Same layout. Same zoom. Same framing.  
After five parts, reviewers stop thinking and just *trust* the library.

---

If you want, the next natural step is:
- a **parameter whitelist** for pass/fail, or  
- a **one-row Excel checklist** where each cell links to these three images  

That’s how this turns from “good practice” into a system that never regresses.

[M11] ME (2026-01-16 03:11):
So I’ve got a checklist I just need to know what the best screen shots are as a minimum 

[M12] AI (2026-01-16 03:11):
Good — then let’s collapse this to the **irreducible minimum**.  
Not “nice to have”, not “belt and braces”. Just the **fewest screenshots that still prove the part is real, correct, and intentional**.

If you capture **only these**, your checklist is defensible.

---

## The minimum viable screenshot set (Altium Designer)

### Screenshot 1 — **Symbol + parameters (SCHLIB)**

image_group{"query":["Altium SCHLIB component with properties panel","Altium schematic library symbol parameters","Altium Designer schematic symbol properties"]}

**This must show, in one frame**
- Entire symbol
- Designator + value/comment
- Properties panel with:
  - Component name
  - Manufacturer
  - MPN (or family for passives)
  - Footprint link
  - Datasheet link (or family reference)

**What this single image proves**
> The *logical definition* and the *claimed identity* are aligned.

If a pin or value is wrong, it is visible here.

---

### Screenshot 2 — **Footprint + parameters (PCBLIB, 2D)**

image_group{"query":["Altium PCBLIB footprint with properties panel","Altium PCB footprint properties","Altium Designer PCB library footprint top view"]}

**This must show**
- Entire footprint (top view)
- Pad numbers readable
- Pin-1 marker (if applicable)
- Properties panel with:
  - Footprint name
  - Package dimensions / height
  - Courtyard / clearance info (if used)

**What this proves**
> The copper geometry is intentional and matches the package definition.

This is where most “looks fine” failures actually live.

---

### Screenshot 3 — **3D body + parameters (PCBLIB, 3D)**

image_group{"query":["Altium 3D body properties panel","Altium PCB 3D component properties","Altium Designer 3D layout mode component"]}

**This must show**
- 3D body sitting on pads
- Pads visible underneath
- Properties panel with:
  - Body type / STEP name
  - Rotation values
  - Offset values
  - Body height

**What this proves**
> The physical representation is aligned, scaled, and sane.

This catches mirrored parts, floating bodies, and wrong heights.

---

## That’s it. Three screenshots.

Anything beyond this is **bonus**, not required for release.

---

## The pass/fail rule (very important)

A screenshot is **invalid** if:
- You need to scroll to see key parameters
- The Properties panel is cropped
- Identity (what part is this?) isn’t obvious in under 3 seconds

If any of the three fails → the part fails the checklist.

No judgement. No heroics. Just don’t release it yet.

---

## Why this minimum works

These three images together prove:
- **Meaning** (symbol)
- **Geometry** (footprint)
- **Physical reality** (3D)

That triangle is sufficient for:
- Design review
- Manufacturing handover
- Future-you sanity checks

---

If you want next, we can:
- compress this into **one checklist row per part**, or  
- define a **standard capture resolution + naming scheme** so every screenshot looks identical  

That’s how this becomes frictionless instead of overhead.

[M13] ME (2026-01-16 06:40):
[image]
Here is the criteria, can you make up an example? Part number (MPN) correct and unambiguous	Select	
Package variant explicitly identified	Select	
Datasheet linked and correct revision	Select	
Schematic Symbol		
Pin count matches datasheet	Select	
Pin names and functions match datasheet	Select	
Pin numbers exactly correct	Select	
Power and ground pins complete	Select	
NC / DNU pins clearly identified	Select	
Special pins represented correctly	Select	
Footprint		
Package type and body size correct	Select	
Land pattern dimensions verified	Select	
Pin pitch and numbering orientation correct	Select	
Pin-1 indicator correct and obvious	Select	
Courtyard / assembly outline present	Select	
Thermal pad present and sized correctly	Select	
Symbol ↔ Footprint Mapping		
All pins map correctly symbol → footprint	Select	
No swapped, mirrored, or rotated pin assignments	Select	
Power pins land on correct pads	Select	
NC / DNU pins not accidentally bonded	Select	
Differential / paired pins mapped correctly	Select	
Parametrics & Metadata		
Voltage / power / tolerance fields populated	Select	
Approved alternates noted	Select	
Lifecycle status known	Select	
Internal library revision assigned	Select	
Imaging / Test-Electronics Sanity		
Absolute max ratings compatible with system rails	Select	
Sensitive pins identified	Select	
Known vendor errata checked	Select	
No violation of test-system assumptions	Select	
Release Check		
Reviewed by second pass	Select	
Notes recorded if anything is non-obvious	Select	
[attached file: d60c8af6-aed5-4e39-a521-eda96c8fdd96.png]

[M14] AI (2026-01-16 06:40):
Perfect — this is already a *very* solid checklist. What you’re asking for now is an **example row that shows how it gets used in real life**, so the intent of each “Select” is unambiguous.

I’ll do this as a **worked example** for a simple, boring, defensible part:

> **Example part:**  
> **Resistor, 10 kΩ, 1%, 0603**  
> **MPN:** Yageo **RC0603FR-0710KL**

I’ll keep it concise but concrete, exactly as it would appear when someone has actually done the checks.

---

## Example — completed checklist (single part)

### Identity & Scope
- **Part number (MPN) correct and unambiguous** → **Yes**  
  *RC0603FR-0710KL matches manufacturer datasheet*
- **Package variant explicitly identified** → **Yes**  
  *0603 (1608 metric)*
- **Datasheet linked and correct revision** → **Yes**  
  *Yageo datasheet rev. 2023-06*

---

### Schematic Symbol
- **Pin count matches datasheet** → **Yes**  
  *2 terminals*
- **Pin names and functions match datasheet** → **Yes**  
  *Terminal 1 / Terminal 2*
- **Pin numbers exactly correct** → **Yes**  
  *1 ↔ 2*
- **Power and ground pins complete** → **N/A**  
- **NC / DNU pins clearly identified** → **N/A**
- **Special pins represented correctly** → **N/A**

---

### Footprint
- **Package type and body size correct** → **Yes**  
  *0603 nominal body*
- **Land pattern dimensions verified** → **Yes**  
  *Compared against IPC-7351 + Yageo recommended*
- **Pin pitch and numbering orientation correct** → **Yes**
- **Pin-1 indicator correct and obvious** → **Yes**  
  *Pad-1 silk / assembly marker*
- **Courtyard / assembly outline present** → **Yes**
- **Thermal pad present and sized correctly** → **N/A**

---

### Symbol ↔ Footprint Mapping
- **All pins map correctly symbol → footprint** → **Yes**
- **No swapped, mirrored, or rotated pin assignments** → **Yes**
- **Power pins land on correct pads** → **N/A**
- **NC / DNU pins not accidentally bonded** → **N/A**
- **Differential / paired pins mapped correctly** → **N/A**

---

### Parametrics & Metadata
- **Voltage / power / tolerance fields populated** → **Yes**  
  *50 V, 0.1 W, ±1 %*
- **Approved alternates noted** → **Yes**  
  *Panasonic ERJ-3EKF1002V*
- **Lifecycle status known** → **Yes**  
  *Active*
- **Internal library revision assigned** → **Yes**  
  *LIB-R-0603-v1.2*

---

### Imaging / Test-Electronics Sanity
- **Absolute max ratings compatible with system rails** → **Yes**  
  *≤ 24 V systems*
- **Sensitive pins identified** → **N/A**
- **Known vendor errata checked** → **N/A**
- **No violation of test-system assumptions** → **Yes**

---

### Release Check
- **Reviewed by second pass** → **Yes**  
  *Initials + date*
- **Notes recorded if anything is non-obvious** → **Yes**  
  *“0603 footprint aligned to IPC-7351 nominal”*

---

## Why this example matters

Notice a few important things:

- **N/A is used aggressively**  
  This keeps the checklist honest and fast.
- **Every “Yes” is defensible**  
  Each one corresponds to something you could point at: a screenshot, a datasheet page, or a property field.
- **This scales**  
  The exact same checklist works for:
  - an op-amp  
  - an ADC  
  - an FPGA  
  - a CCD sensor  

Only the number of N/A rows changes.

---

## How this ties back to screenshots (cleanly)

This entire checklist can be satisfied with **three minimum screenshots**:
1. Symbol + parameters  
2. Footprint + parameters  
3. 3D body + parameters  

The checklist tells you *what to verify*.  
The screenshots prove *that you actually did*.

If you want, next we can:
- convert this into a **filled Excel example row** (with dropdowns),
- or mark **which checklist rows are satisfied by which screenshot**, so nothing is redundant.

This is already very close to “library as infrastructure,” not folklore.

[M15] ME (2026-01-16 06:41):
Can you do it in a table for mat fr me to drop in?

[M16] AI (2026-01-16 06:41):
Absolutely. Below is a **clean, paste-ready table** that mirrors your checklist exactly, but with the **example selections filled in**. You can drop this straight into **Excel or Word** and keep or overwrite the “Example evidence / notes” column as you see fit.

This example uses the same **10 kΩ, 0603 resistor** so it stays simple and unambiguous.

---

### Library Part Checklist — Worked Example

| Section | Check Item | Result | Example evidence / notes |
|---|---|---|---|
| **Identity & Scope** | Part number (MPN) correct and unambiguous | Yes | RC0603FR-0710KL (Yageo) |
|  | Package variant explicitly identified | Yes | 0603 (1608 metric) |
|  | Datasheet linked and correct revision | Yes | Yageo datasheet rev. 2023-06 |
| **Schematic Symbol** | Pin count matches datasheet | Yes | 2 terminals |
|  | Pin names and functions match datasheet | Yes | Terminal 1 / Terminal 2 |
|  | Pin numbers exactly correct | Yes | Pins 1–2 |
|  | Power and ground pins complete | N/A | Passive component |
|  | NC / DNU pins clearly identified | N/A | None |
|  | Special pins represented correctly | N/A | None |
| **Footprint** | Package type and body size correct | Yes | 0603 nominal |
|  | Land pattern dimensions verified | Yes | IPC-7351 + datasheet |
|  | Pin pitch and numbering orientation correct | Yes | 1 ↔ 2 |
|  | Pin-1 indicator correct and obvious | Yes | Pad-1 assembly mark |
|  | Courtyard / assembly outline present | Yes | Courtyard layer present |
|  | Thermal pad present and sized correctly | N/A | Not applicable |
| **Symbol ↔ Footprint Mapping** | All pins map correctly symbol → footprint | Yes | 1→1, 2→2 |
|  | No swapped, mirrored, or rotated pin assignments | Yes | Visual check |
|  | Power pins land on correct pads | N/A | Not applicable |
|  | NC / DNU pins not accidentally bonded | N/A | Not applicable |
|  | Differential / paired pins mapped correctly | N/A | Not applicable |
| **Parametrics & Metadata** | Voltage / power / tolerance fields populated | Yes | 50 V, 0.1 W, ±1 % |
|  | Approved alternates noted | Yes | Panasonic ERJ-3EKF1002V |
|  | Lifecycle status known | Yes | Active |
|  | Internal library revision assigned | Yes | LIB-R-0603-v1.2 |
| **Imaging / Test-Electronics Sanity** | Absolute max ratings compatible with system rails | Yes | ≤ 24 V systems |
|  | Sensitive pins identified | N/A | Passive component |
|  | Known vendor errata checked | N/A | None published |
|  | No violation of test-system assumptions | Yes | Generic passive |
| **Release Check** | Reviewed by second pass | Yes | Initials + date |
|  | Notes recorded if anything is non-obvious | Yes | IPC-7351 nominal used |

---

### Notes on using this table (brief but important)

- This is **one part, one table**.  
- “Result” should be a **dropdown** in Excel (Yes / No / N/A).
- The last column can:
  - stay free-text, or  
  - link to your **three evidence screenshots**.

If you want next, I can:
- give you **exact Excel dropdown definitions**, or  
- mark which **screenshot satisfies which rows**, so reviewers know exactly where to look.

This is already very clean engineering hygiene.

[M17] ME (2026-01-16 06:43):
[image]
All pins map correctly symbol → footprint	1→1, 2→2
No swapped, mirrored, or rotated pin assignments	Visual check
Power pins land on correct pads	
NC / DNU pins not accidentally bonded	
Differential / paired pins mapped correctly	
[attached file: 72c121f6-51de-4373-ba19-2ac63047173d.png]

[M18] AI (2026-01-16 06:43):
Good — this is exactly the right level of pedantry. What you’re really asking is:

> *What should go in the **notes/evidence** column for these rows so they’re not hand-wavy?*

Below is a **tight, copy-pasteable fill** for those five rows, written in the same factual tone as your checklist. This works for both **passives** and **ICs**, with N/A used deliberately.

You can drop this straight into Excel.

---

### Symbol ↔ Footprint Mapping — example entries

| Check Item | Example entry (Notes / Evidence) |
|---|---|
| All pins map correctly symbol → footprint | Symbol pins map 1→1, 2→2 (verified against footprint pad numbering) |
| No swapped, mirrored, or rotated pin assignments | Orientation and numbering verified by visual comparison of SCHLIB symbol and PCBLIB footprint |
| Power pins land on correct pads | N/A — no dedicated power pins (passive component) |
| NC / DNU pins not accidentally bonded | N/A — no NC/DNU pins present |
| Differential / paired pins mapped correctly | N/A — no differential or paired pins |

---

### Why this wording works

- **Explicit but brief**  
  It states *what was checked* and *how*, without inventing ceremony.
- **N/A is intentional**  
  Reviewers can see immediately that this was considered, not forgotten.
- **Scales to complex parts**  
  For an IC, those N/A lines become specific mappings instead of prose.

---

### For comparison: how this would look on an IC

Just so you can see the contrast, here’s how the same rows would look for (say) an ADC:

- *All pins map correctly symbol → footprint*  
  `All 48 pins mapped 1:1; verified against datasheet pinout table`
- *Differential / paired pins mapped correctly*  
  `AIN_P/N pairs mapped to adjacent pads as per datasheet Figure 23`

Same structure. Same tone. No ambiguity.

---

If you want next, we can:
- define a **controlled vocabulary** for this notes column, or  
- mark **which screenshot** proves each of these rows so reviewers don’t argue about “visual check”.

You’re very close to a checklist that actually enforces correctness instead of just recording optimism.
