# Schematic PCB Sync Issue
Date (UTC): 2026-02-25 16:46
Conversation ID: 699f2740-c3f8-838f-90a1-f3400c4ce7e6
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-02-25 16:46):
[image]
How is this resolved?
[attached file: IMG_CFF8786C-8D45-4E21-961B-E5A452DFB890.jpeg]

[M2] AI (2026-02-25 16:46):
That warning means **your schematic and PCB documents are out of sync** (Altium thinks the schematic “logical” data doesn’t match the PCB “physical” data), and you’re trying to **save a Reuse Block** while that mismatch exists.

To resolve it, you need to get the project back to a clean **Schematic ↔ PCB synchronization state**, then save the block.

## The practical fix (do this in order)

### 1) Make sure you’re editing the *right* pair of documents
- Open the **PCB** that belongs to the same project as the schematic you’re editing.
- If you have multiple PCBs (or copied projects), it’s easy to have the schematic linked to PCB-A while you’ve got PCB-B open.

### 2) Compile the project (flush annotation/parameters/ERC changes)
- **Project → Compile PCB Project**
- Fix any obvious compile errors first (missing libraries, bad parameters, etc.). Warnings are usually fine, errors can break sync.

### 3) Push schematic → PCB (most common)
If your schematic is the “source of truth” (usual case):
- **Design → Update PCB Document**
- In the ECO dialog:
  - Review changes
  - **Validate**
  - **Execute**
- Then save the PCB.

This usually clears the warning immediately.

### 4) Or pull PCB → schematic (if the PCB is the source of truth)
If you did footprint swaps / refdes changes / component edits on the PCB and want to keep them:
- **Design → Import Changes From PCB**
- Then save schematic + PCB.

### 5) Re-try saving the Reuse Block
Once you’ve done one of the above and both docs are saved, the Reuse Block save should no longer complain.

---

## If it *still* complains (common causes)

### A) You’ve got “Pending ECO” changes not executed
Sometimes people open the ECO dialog but don’t execute it.
- Repeat **Design → Update PCB Document**
- Ensure **Execute** is actually run (not just “Validate”).

### B) “Unique ID” / component identity issues (copy/paste / duplicate sheets)
If you’ve copied circuitry between projects/sheets, Altium can get confused about component identity.
Try:
- **Tools → Reset Component Unique IDs** (in schematic)
- Compile again
- Then **Update PCB** again

### C) The Reuse Block includes PCB primitives or references that don’t match
If your Reuse Block includes things that exist only on one side (special rooms, classes, variants, etc.), it can trip validation.
- Make sure the block content is fully defined in schematic (components/nets/params) and that PCB is updated from it.

---

## What to click when you’re in a hurry
If you’re confident the schematic is correct and you just want the warning gone:

1. **Project → Compile**
2. **Design → Update PCB Document**
3. **Execute ECO**
4. Save PCB
5. Save schematic
6. Save the Reuse Block

---

If you tell me **which direction you’ve been editing** (mostly schematic, or mostly PCB) and whether you’re using a **.PrjPcb with a single PCB** or multiple, I can point you at the exact “correct” direction (Update PCB vs Import Changes) and the one or two menu items most likely to fix your case.

[M3] ME (2026-02-25 21:22):
[image]
Hi how do I get these p assigned and pulled through to schematic 
[attached file: IMG_1593FD95-D1ED-4E84-8817-E882B68DDE78.jpeg]

[M4] AI (2026-02-25 21:27):
You’ve got a bunch of parts sitting with the **designator “P?”** (i.e. *un-annotated*), plus at least one **duplicate designator** situation. The fix is: **annotate the schematic**, then **push the changes to the PCB** via ECO so everything “pulls through”.

Here’s the clean way to do it in Altium.

---

## 1) Assign proper designators on the schematic (Annotate)
In the schematic editor:

1. **Tools → Annotation → Annotate Schematics…**
2. In the dialog:
   - Choose **Annotate entire project** (if this is a multi-sheet design)
   - Click **Reset All** (this clears existing conflicting/partial annotation *in the plan*, not necessarily on the sheets yet)
   - Click **Update Changes List**
   - Then **Accept Changes (Create ECO)** / **Execute** (wording varies by version)

This will convert **P? → P1, P2, …** (and similarly for R?, C?, IC?, etc.) *on the schematic*.

### If you specifically want connectors to be “J” not “P”
That’s controlled by the **component’s default designator** in the library:
- Open the component properties (on schematic) → check **Designator**
- Or edit the library symbol default designator (e.g. `J?` instead of `P?`), then update placed components.

But first: get rid of the `?` state.

---

## 2) Push those designators into the PCB (so it “pulls through”)
Once annotated:

1. **Design → Update PCB Document…**
2. In the ECO dialog:
   - Make sure you see actions like **Update Component Designators**
   - **Validate**
   - **Execute**
3. Save PCB + schematic.

That’s the “pulled through” bit: schematic is master, PCB gets updated.

---

## 3) Fix the *Duplicate Component Designators* error (shown in your messages)
That error means **two different components currently share the same designator** (or you have conflicting annotation between sheets).

Quick fix:
- Run **Annotate Schematics** as above, but make sure it’s set to **entire project**, not “current sheet only”.
- If you have repeated circuitry on multiple sheets:
  - Use **Tools → Annotation → Annotate Schematics…**
  - Ensure it uses a consistent scheme across sheets (not restarting from 1 per sheet unless that’s intended).

---

## 4) Fix the *Duplicate Net Names Wire NetP?_1* errors (also shown)
That’s separate, but it will bite you during sync.

This happens when you have multiple unnamed nets that Altium auto-names and they collide, often due to:
- copy/paste blocks
- weird net label placement
- repeated sheets without proper harness/ports/net labels

To locate and resolve fast:
- In the **Messages** panel, **double-click** each “Duplicate Net Names…” entry → it should jump to the offending wire.
- Either:
  - Give those nets **explicit net labels**, or
  - Ensure they are truly the *same intended net* (then connect appropriately), or
  - Make the labels unique.

---

## 5) About those “Duplicate pins in component …” warnings
Those are usually **library symbol issues** (two pins with same number) or a multi-part component defined oddly. It won’t directly stop annotation, but it’s worth fixing in the library later.

---

### The 30-second “just make P? go away” route
1. **Tools → Annotation → Annotate Schematics… → Annotate entire project → Update Changes List → Accept/Execute**
2. **Design → Update PCB Document → Execute ECO**

---

If you tell me one detail, I can be more exact: are these **connectors** that you *want* to be **P1/P2** (or do you want **J1/J2**)? And is this a **single-sheet** schematic or multi-sheet hierarchy?

[M5] ME (2026-02-26 12:14):
[image]
Why are these lot pulling through in who update. Comoilenis clean 
[attached file: IMG_77FC7F22-EE7D-4A45-AA95-82D5F08C730B.jpeg]

[M6] AI (2026-02-26 12:14):
What you’re seeing there (P17, P18, … on a column of “targets”) is **not the ECO “pulling parts through”**. It’s Altium showing **compiled connector/port primitives** (off-sheet connectors / ports / harness entries) that have a **default designator of `P?`**, so after compilation/annotation they become **P17…P24**.

So: **compile being clean doesn’t stop them appearing** — they’re *valid objects* in the compiled netlist. They’ll keep “pulling through” on Update PCB because Altium considers them *real components / connection primitives* that belong in the design.

### The usual reasons this happens

#### 1) They’re actually **connectors**, not just “labels”
If those red chevrons are placed as **Off-Sheet Connectors** (or a library “connector symbol”), Altium treats them as components and they get designators.

**Fix**
- Replace them with the primitive you actually intend:
  - If you want *pure connectivity across sheets*: use **Ports** + **Sheet Entries** (hierarchical), or **Net Labels** (flat).
  - If you want a definable interface object: use a proper connector component (Jx) and keep it.

#### 2) You’ve got **Net Labels duplicated as physical “objects”**
If you copied a block, it’s easy to end up with multiple off-sheet connectors that are meant to be *text labels* but are actually *connectivity objects*.

**Check**
- Click one of the chevrons → open **Properties** panel.
- Look at **Object Type**:
  - “Off Sheet Connector” / “Port” / “Harness Entry” = connectivity primitive (expected)
  - “Component” = library symbol (will definitely get a designator + footprint)
  - “Net Label” = just a label (no designator)

#### 3) The project is set up as **multi-channel / repeated blocks**, and they’re being indexed
Your tooltip shows: `CB1_FAST_CLOCK_2_N (Net Name/Physical Name)` which screams **compiled physical naming** (channel prefixing). That’s normal in a hierarchical/multi-channel design, and it can cause lots of “similar looking” ports/connectors to exist in the compiled view.

That still shouldn’t create *components* unless those objects are component-type.

---

## Why they appear in “Update PCB” even though compile is clean
Because ECO compares **compiled schematic netlist** vs PCB.
If the compiled netlist contains these objects as components/connectors, ECO will keep trying to sync them.

Clean compile just means “no rules broken”, not “nothing to change”.

---

## How to stop them “pulling through” (pick the matching case)

### Case A — They are Off-Sheet Connectors / Ports (you want them, but not as P17 etc.)
They shouldn’t normally have designators. If they do, it’s likely you’re not looking at ports; you’re looking at **connector components**.

✅ Confirm by Properties → Object Type.

If they are components and you just want different prefix:
- Edit the symbol default designator from `P?` to `X?`/`J?` etc (library change), then re-annotate.

### Case B — They are connector components but you *don’t* want them as components
- Delete them and use **Ports / Net Labels** instead.
- Recompile.
- **Design → Update PCB** and you’ll see ECO removing those components.

### Case C — They are “real” connectors, but you don’t want footprints on PCB for them
(Example: logical interface markers)
- Give them a footprint of **No Footprint** / **Not Fitted** style (depends on your libraries/workflow), or set them to **Exclude from PCB** if you’re using managed components / component properties that support it.
- Otherwise Altium will keep insisting they exist on the PCB.

---

## The 20-second diagnostic that will answer it definitively
1. Click one of the chevrons.
2. Look in **Properties** for **Object Type** and whether it has:
   - **Designator**
   - **Footprint / Models**
3. Tell me what Object Type says (Port / Off-Sheet Connector / Component).

With just that one line, I can tell you exactly why they’re being treated as “things to update” and the cleanest fix for your design style.
