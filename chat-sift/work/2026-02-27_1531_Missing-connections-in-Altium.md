# Missing connections in Altium
Date (UTC): 2026-02-27 15:31
Conversation ID: 69a1b89f-48ec-838c-a07e-775be47dfd1c
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-02-27 15:31):
[image]
How do I get up the missing connections when routing 
[attached file: IMG_85EE4F17-6C8A-410F-AD45-3BDBD9CA7C51.jpeg]

[M2] AI (2026-02-27 15:31):
In Altium, the “missing connections” you want while routing are the **ratsnest / connection lines**. They’re almost certainly just **hidden** in your view (your screenshot shows zero connection lines at all).

### Fastest way to bring them back
1. **PCB editor → `View` → `Connections` → `Show All`**  
   (If you previously hid them, this restores them globally.)

### If they’re still not showing
2. Press **`L`** (View Configuration) → make sure **`Connections / Connection Lines (Ratsnest)`** is **enabled** (and not set to “None/Off”).

### If only *some* nets look “missing”
3. Clear any filtering that can suppress connections:
- Press **`Shift + C`** (Clear filter)
- If you’ve used net highlighting, press **`Shift + H`** (clear highlights) if needed.

### During interactive routing
4. If you want to see what’s left *as you route*:
- Route normally, and use the **PCB panel → Nets**:
  - Select a net → **Right-click → Show Net** / **Highlight** to force its remaining connections to display clearly.

If you tell me your exact Altium version (looks like 23.x) and whether this happens **only while Interactive Routing** or **all the time**, I’ll give you the exact checkbox/menu path for that build.

[M3] ME (2026-02-27 15:32):
Ahh, they aren’t there as I prevented them when doing an eco update. I was finding that it was tearing up a lot of tracks. I’ll eco again and report back when it wants to do 

[M4] AI (2026-02-27 15:32):
Got you — that’s a classic side-effect of doing an ECO where Altium is effectively “re-binding” the PCB to the schematic and offering to re-apply a bunch of changes. Two key points:

1) **Ratsnest visibility** (missing connections) is *usually* just display/filtering.  
2) **Tracks getting torn up** is almost always because the ECO is trying to **remove/re-add components**, **swap footprints**, or **recreate nets** (net identity changes), which forces Altium to treat existing copper as “not belonging” (or belonging to old nets).

Here’s how to ECO again without it nuking your routing.

## Before you run the ECO
### A) Make sure you’re not accidentally “recreating” the PCB
- In the PCB editor: **Project » Project Options » Class Generation** (sanity check, optional)
- More importantly: check if your change flow is **Schematic → PCB** (ECO) or you’ve got a **snippet/reuse block** situation that can cause net/UID churn.

### B) Save your current PCB state (so you can compare)
- **File → Save Copy As** (quick safety net).

## Run ECO, but *declaw* the destructive actions
1. From schematic: **Design » Update PCB Document…**
2. In the **Engineering Change Order** list, expand the changes and look for these “danger” items:
   - **Remove Component / Add Component**
   - **Change Footprint**
   - **Remove Net / Add Net / Update Net**
   - **Component Unique ID changes**
   - **Remove/Re-add rooms / classes** (less destructive but can be noisy)

3. **Uncheck / disable** anything that implies “remove and re-add” unless you genuinely intend it.

### The big rule
If the ECO is proposing **Remove + Add** for parts that already exist on the PCB, *that’s exactly* when you see routing tear-ups.

## If you only want “missing connections” back
You do **not** need an ECO just to see ratsnest.

Do this instead:
- PCB editor → **View → Connections → Show All**
- Press **L** (View Configuration) → ensure **Connections** are enabled
- **Shift+C** clear any filter

That brings back missing connection lines without touching copper.

## If your ECO is *still* trying to rip up routing
That usually means one of these is happening:

### 1) Footprints changed (even if “same”)
Altium sees it as a new component instance → old copper no longer matches.

### 2) Net identity changed (netlist churn)
Common with reuse blocks / copy-paste / re-annotation workflows.
Copper is still there, but it’s now “wrong net” relative to the new netlist.

### 3) Component Unique IDs changed
If UIDs regenerate, Altium can’t correlate PCB parts to schematic parts.

## What I want you to report back with
When you re-run the ECO, tell me the **top 5–10 ECO actions** it proposes (literally the list items like “Remove Component X”, “Add Net Y”, “Update Component Parameters”, etc.).  
From that list I can tell you *exactly* which tick boxes to leave on/off to get connectivity restored while preserving routing.

If you can, grab a screenshot of the ECO dialog (the proposed changes list).

[M5] ME (2026-02-27 15:47):
[image]
Best way to align the size of legend ?
[attached file: IMG_CB81FD51-843C-4D52-86C0-8B7F0A7B3C26.jpeg]

[M6] AI (2026-02-27 15:47):
You’ve basically got two different problems mixed together: **(1) make overlay text a consistent size**, and **(2) make it *look* consistent (same stroke/weight, same “visual height”)**. In Altium the clean way is to standardise the **Text Style** and then batch-apply it.

## Best practice (do this once per board)
### 1) Decide your house “overlay font spec”
Typical starting points (you’ll tune to your fab/process):
- **Designators:** 1.0–1.2 mm height, 0.15–0.20 mm stroke
- **Component values:** same or slightly smaller
- **Connector IDs / big labels:** 1.5–2.0 mm height, 0.20–0.25 mm stroke

(If you’re tight on space, go smaller, but avoid stroke < 0.12 mm unless you *know* the fab can hold it.)

### 2) Set the defaults so new text comes in “right”
PCB editor:
- **Preferences → PCB Editor → Defaults**
  - Find **Text** (and also **Component Designator / Component Comment** defaults)
  - Set **Height** and **Stroke Width** (and font if you use TrueType)

This stops the problem coming back.

---

## Align / normalise what you already have (fastest)
### Option A — Batch edit via Properties + PCB Filter (most controllable)
1. Open **Panels → PCB Filter**
2. Filter what you want, e.g. **Top Overlay designators**:
   - For designators (special strings):  
     `IsDesignator AND OnLayer('Top Overlay')`
   - For any free text on overlay:  
     `IsText AND OnLayer('Top Overlay')`

3. Click **Apply** → all matching objects highlight
4. Open **Properties** panel and set:
   - **Text Height**
   - **Stroke Width**
   - (Font if needed)
5. It will apply to the whole selection.

That’s the best “do it once, be done” method.

### Option B — Single “template” text then paste formatting
If you just need to quickly match a bunch of random overlay strings:
1. Pick one text object and set it exactly how you want.
2. Copy it.
3. Select other text objects → **Paste Special** / “Paste Attributes” (depending on your shortcut setup)  
Altium is a bit inconsistent here depending on object type, so Option A is usually cleaner.

---

## Important gotcha: Designators in footprints vs designators on the PCB
If those huge labels are coming from the **footprint overlay** (inside the PCBLIB), then changing them on the PCB is fighting the source.

**If you want the change to be permanent across projects:**
- Edit the **PCB Library footprint**
  - Ensure the designator text is a **special string `.Designator`**
  - Set its **height/stroke**
  - Update the PCB from the library

**If you want it only on this PCB:**
- Keep changes local using Option A above.

---

## Make them visually consistent (not just numerically)
Two texts can both be “1.2 mm” but look different if:
- One is **TrueType** and one is **Stroke**
- Stroke widths differ
- “Inverted” / soldermask settings differ

So: try to standardise to **one font type** across overlay (either all Stroke or all a specific TrueType).

---

## Quick suggestion based on your screenshot
Those “P17 / IC2 / J6” labels look like they’re set much larger than everything else and may be footprint text that wasn’t normalised.

Do this:
- Filter: `IsDesignator AND OnLayer('Top Overlay')`
- Set: **Height ~1.2 mm**, **Stroke ~0.15–0.20 mm**
- Then separately filter big reference labels if they’re plain text: `IsText AND OnLayer('Top Overlay')`

If you tell me your fab’s **minimum silkscreen line/space** (or who manufactures), I’ll give you a safe height/stroke pair so it actually prints cleanly.

[M7] ME (2026-02-27 15:52):
Why would it only let me select one at a time as opposed to all?

[M8] AI (2026-02-27 15:52):
That behaviour is almost always because Altium thinks you’re doing **object picking** (cycling through overlapping items) rather than **multi-select**, or because a **filter / selection lock** is in effect.

Here are the usual culprits and the fixes, in the order I’d check them:

## 1) You’re in “cycle through overlapping objects” mode
On dense overlay it’s very common.

**Fix**
- Hold **Shift** while clicking additional items to add them to the selection (classic add-to-selection).
- Or do a **window selection** (click-drag a box) to grab many at once.

**Tip:** If everything overlaps, use:
- **Shift + Click** repeatedly to cycle the candidates under the cursor, *then* add the one you want.

## 2) Selection Filter is restricting what can be selected
If the filter is set to only allow (say) “Components” or “Pads”, you’ll only ever pick one relevant thing at a time.

**Fix**
- Open **Panels → Selection Filter**
- Tick what you actually want selectable (usually **Texts / Strings** and/or **Components**)
- Or hit **Shift + C** to clear filters/highlights and try again.

## 3) “Single-layer mode” / view configuration is confusing what you can grab
Less common, but if you’re effectively isolating a layer or objects, selection can feel “sticky”.

**Fix**
- Press **L** (View Configuration)
- Make sure you haven’t got odd restrictions enabled.
- Toggle **Single Layer Mode** with **Shift + S** until you’re back to normal.

## 4) You’re trying to select **component designators** that are “special strings”
Designators/comments are not generic “Text” objects; they’re component parameters displayed on overlay. You *can* multi-select them, but it’s easiest via the PCB Filter approach.

**Best way (guaranteed multi-select)**
- **Panels → PCB Filter**
- Enter:
  - `IsDesignator AND OnLayer('Top Overlay')`
- Click **Apply**
- Now all designators are selected, and you can edit height/stroke in **Properties** in one hit.

## 5) “Lock Primitives” / locked objects
If some are locked, you’ll only successfully modify the unlocked one you happened to pick.

**Fix**
- Click a text → **Properties** → check **Locked**
- Or filter locked ones and unlock in batch.

---

### The quickest “make them all the same” workflow (no faffing with clicking)
1. **Panels → PCB Filter**
2. Apply one of these:
   - Designators: `IsDesignator AND OnLayer('Top Overlay')`
   - Free text: `IsText AND OnLayer('Top Overlay')`
3. Edit **Text Height** + **Stroke Width** in **Properties**

If you tell me whether you were clicking **component designators** or **random overlay text**, I’ll give you the exact filter expression that matches what you’re trying to bulk-edit.

[M9] ME (2026-02-27 16:23):
Had do i select components in schematic and they select themselves in PCB 

[M10] AI (2026-02-27 16:23):
To “cross-select” from **schematic → PCB** in Altium you need two things: the documents must be **compiled/linked**, and **Cross Select Mode** must be on.

## Do this (schematic → PCB selection)
1. **Compile / validate the project**
   - In the schematic: **Project » Compile** (or **Project » Validate PCB Project**).
2. Turn on cross selection:
   - **Tools » Cross Select Mode** (toggle ON)
3. Now click a component (or drag a box to select several) in the **schematic** → Altium should jump/select them in the **PCB**.

### Useful extras
- **Tools » Cross Probe**: zooms/pans to the selected object in the other editor.
- After selecting in schematic, press **F1**? (depends on key mapping) — but generally **Cross Probe** is the “take me there” tool.

## If it doesn’t work, it’s usually one of these
### A) No live link between sch and pcb
- The PCB isn’t part of the same **.PrjPcb**, or you’re editing an “orphan” PCB.
- Fix: Ensure both SchDoc and PcbDoc are in the same project and re-compile.

### B) Components aren’t matched (UID mismatch)
This is common after copy/paste, reuse blocks/snippets, or library swaps.
- Symptom: cross select/probe does nothing or selects the wrong things.
- Fix: run **Design » Update PCB Document…** (ECO) and ensure component matching is sane (avoid remove/add unless intended).

### C) You’re selecting inside a **reuse block** on the schematic
Selection sometimes behaves oddly depending on how the block was placed.
- Workaround: try selecting the **component(s)** (not the block frame), or open the source sheet and select there.

If you tell me whether you’re using a **multi-channel / reuse block** in this project, I’ll give you the exact “UID repair” path if cross-select still won’t bind.

[M11] ME (2026-02-27 16:35):
[image]
What’s this massive area that appears when I select the mmcx connectors 
[attached file: IMG_9F6B9E6A-9CDE-46AA-916F-401BFF93B113.jpeg]

[M12] AI (2026-02-27 16:35):
That big pale/stripy rectangle is almost certainly **a Room** (Altium “placement room”), not copper.

When you select the MMCX connectors, Altium is also selecting/highlighting the **room they belong to** (often created automatically during **Update PCB / ECO** from schematic classes). If the room got generated with bad extents (or based on a weird footprint bounding box), it can end up **massive** like this.

### How to confirm in 10 seconds
- Open **Panels → PCB**
- In the drop-down (top of the panel) choose **Rooms**
- Click that big rectangle → you should see a room entry highlight (often named after a class/channel).

Or:
- Press **L** (View Configuration) and **toggle Rooms off** to see if it disappears.

### How to get rid of it (common fixes)
**Option A — Remove rooms completely (most common)**
- **Design → Rooms → Remove Rooms** (or “Delete Rooms” depending on version wording)

**Option B — Stop Altium auto-creating them**
- **Project → Project Options → Class Generation**
- Disable **Generate Rooms** (wording varies slightly)
- Then update/compile again.

### If it’s *not* a Room (second most likely)
It can be a **huge courtyard / mechanical / component body primitive** in the MMCX footprint (e.g., a stray rectangle far away), which expands the component’s bounding box.

**Check**
- Select the MMCX → open **Properties** → look at selected primitives, or
- Open the footprint in the **PCBLIB** and look for a misplaced **Region/Track/Fill** on Courtyard/Mechanical layers.

If you tell me whether you’re using **rooms for placement constraints** (sometimes handy) or you just want them gone, I’ll give you the cleanest “keep routing safe” workflow for your project.

[M13] ME (2026-02-27 16:39):
[image]
[attached file: IMG_E6EDA8EB-EFB4-4A76-BDB7-0E549FB76484.jpeg]

[M14] AI (2026-02-27 16:39):
Yep — that screenshot basically confirms it: the big pale rectangle is on **Top Courtyard** (Altium’s status text at the top-left says **Top Courtyard**). So it’s **not copper** and it’s **not a Room** in this case; it’s a **courtyard primitive** (almost certainly a Region/Fill) that’s been created **massively oversized**.

That means one of these is true:

## What it is
### 1) A rogue courtyard shape inside the MMCX footprint
Most likely: in the **PCBLIB** for the MMCX, there’s a **Region/Fill/Track** on *Top Courtyard* that’s miles too big (or has one vertex far away), so selecting/moving the connector drags that whole courtyard “sheet” with it.

### 2) It’s not in the footprint, but on the PCB and linked to the component somehow
Less likely, but possible if you placed a courtyard region manually and it’s now being selected because of selection behaviour.

---

## Fastest fix (clean, permanent)
### A) Open the footprint and delete/resize the bad courtyard
1. In PCB, **right-click the MMCX → Find Similar Objects** (optional, to see all of them).
2. **Right-click → Edit Footprint** (or **Edit in PCB Library** / “Edit Footprint” depending on your setup).
3. In the footprint editor:
   - Set the active layer to **Top Courtyard**
   - Use **Edit → Select → All on Layer** (or just click the big region)
   - Delete the giant Region/Fill (or redraw it properly)
4. Save the library.
5. Back in PCB: **Design → Update PCB Document** (or **Tools → Update From Libraries**) to push the fixed footprint in.

That fixes it for every use of that connector.

---

## Quick “local-only” fix (if you don’t want to touch the library yet)
### B) Hide courtyards so it stops getting in the way
- Press **L** → View Configuration
- Turn off **Courtyard** layers (Top Courtyard / Bottom Courtyard)

This won’t fix the underlying issue, but it removes the visual pain immediately.

---

## If you want to prove it’s *in the footprint* in 5 seconds
- Select the connector, then look in **Properties**: it’ll show primitives on **Top Courtyard** as part of that component.
- Or open **Panels → PCB** and expand the component → you’ll see a **Region** (or Fill) listed under Top Courtyard.

---

## What caused it (so you can avoid repeats)
Common causes:
- Imported footprint (STEP/IDX/IPC wizard) that accidentally dumped a huge rectangle onto Courtyard.
- Copy/paste of a courtyard outline where one vertex got flung to a far coordinate.
- “Generate Courtyard” script/settings gone wrong.

---

If you want, tell me the **MMCX footprint source** (manufacturer lib / Ultra Librarian / SamacSys / IPC wizard / your own) and whether you actually need courtyards for DRC, and I’ll suggest the “right” courtyard rule-of-thumb for MMCX (keepout/courtyard outline) so it behaves properly.

[M15] ME (2026-02-27 18:17):
How do
You find a lost designator

[M16] AI (2026-02-27 18:17):
Here are the fastest, most reliable ways in Altium to locate a “lost” designator (works for both **schematic** and **PCB**).

## PCB: find a missing component/designator
### 1) Jump straight to it
- Press **Ctrl + F** (Find)
- Type the designator, e.g. `R268` or `J4`
- Hit Enter → it should zoom/center and select it

If Ctrl+F is searching *text* only in your setup, use:

### 2) PCB panel (bullet-proof)
- **Panels → PCB**
- Set the dropdown to **Components**
- In the search box, type the designator (e.g. `R268`)
- Click it → Altium selects it and you can **Zoom** (right-click → *Zoom to Selected*)

### 3) Navigator / Jump (if enabled)
- **View → Panels → Navigator**
- Search by designator and “Jump”.

## Schematic: find a component (or its designator text)
### 4) SCH panel
- **Panels → SCH**
- Dropdown: **Components**
- Search for `R268`
- Click → it selects; right-click → **Jump** / **Zoom**

---

## If the *designator text* is what’s “lost” (invisible), not the component
### PCB: designator exists but you can’t see it
1) Turn it back on globally:
- Press **L** (View Configuration)
- Under **View Options**, enable **Component Designators**

2) Check it’s not on the wrong layer:
- Designators should normally be on **Top Overlay** / **Bottom Overlay**
- If it’s on a mechanical layer, it’ll “vanish” when that layer is off.

3) Check it’s not hidden per-component:
- Click the component → **Properties**
- Look for **Hide Designator** / designator visibility options.

### Schematic: designator text hidden
- Click the component → **Properties**
- Ensure **Designator** is set to **Visible**
- Also check **View Configuration** / document display options if you’ve hidden parameter text.

---

## If Altium can’t find the designator at all
That usually means it got **re-annotated** or you’re looking in the wrong document/version.
- Run **Tools → Annotation → Annotate Schematics** and check if it changed.
- Or in PCB panel, sort by comment/value and see what it became.

If you tell me whether the designator is “lost” on **PCB overlay**, **schematic**, or you suspect it’s been **renamed**, I’ll give you the exact quickest path for that case.

[M17] ME (2026-02-27 18:19):
Looks
Like it’s somehow been deleted 

[M18] AI (2026-02-27 18:19):
If it’s genuinely been deleted, you’ve got two separate possibilities:

1) **The component still exists, but only the *designator text* got deleted/hidden** (very common), or  
2) **The whole component instance is gone** (less common).

Here’s how to tell which, and how to recover cleanly.

## A) Check whether the component still exists (most important)
### PCB
- **Panels → PCB → Components**
- In the search box type the designator you expect (e.g. `R268`)
  - If it **appears in the list** → the component is still there; only the designator display is missing/hidden.
  - If it **doesn’t appear** → the component instance is likely gone or renumbered.

### Schematic
- **Panels → SCH → Components**
- Search for the designator.

## B) If the component exists but the designator text is missing
This happens when someone accidentally edits primitives and deletes the `.Designator` string in the footprint or it’s set invisible.

### Fix on PCB (quick)
1. Click the component.
2. **Properties** panel:
   - Look for **Designator** display settings (Visible / Hidden).
   - Turn **Visible** on.

### If it’s missing because the footprint has no `.Designator` string
1. Right-click the component → **Edit Footprint** (in library).
2. Ensure there’s a **Special String** `.Designator` on **Top Overlay** (and Bottom if needed).
3. Save library → **Update PCB from Libraries**.

## C) If the component itself is deleted (schematic and/or PCB)
### Best recovery (authoritative): restore from schematic via ECO
1. In schematic: **Design → Update PCB Document…**
2. In ECO list you should see **Add Component …**
3. Execute ECO → the component comes back (usually in a room / off to the side)

**Important:** before executing, make sure it’s not also proposing destructive remove/add for lots of other parts.

### If it’s deleted only on the PCB but still on schematic
ECO is the right fix.

### If it’s deleted on schematic too
Then you need:
- **Undo** (Ctrl+Z) if it’s recent, or
- Pull it from **VCS/history** / a previous saved version, or
- Re-place the component and re-annotate.

## D) Quick sanity checks (why it “vanished”)
- **View config** hiding designators: press **L** and ensure “Component Designators” enabled.
- It got moved miles away: use PCB panel → Components → sort by X/Y or “Zoom to selected”.
- It got **re-annotated**: search by **Comment/value** in SCH/PCB panels instead of designator.

---

If you tell me **which item** it is (e.g., “R268”) and whether it’s missing from **schematic, PCB, or both**, I’ll tell you the exact shortest recovery path and what to expect in the ECO list.

[M19] ME (2026-02-27 18:23):
Now I’ve mirrored the view 

[M20] AI (2026-02-27 18:23):
Ah — “mirrored view” usually means you’ve either flipped to the **bottom side** (viewing the board from underneath) or you’ve toggled a display option that mirrors text. That absolutely can make you think designators have vanished (you’re now looking at the *other* overlay layer).

## Get back to normal (top-side, not mirrored)
### 1) Flip the board view back
- Press **V** then **B**  
  (View → Flip Board)

That toggles between viewing from top and bottom and is the most common “suddenly mirrored” cause.

### 2) Make sure you’re actually showing the right overlay
If you’re now looking from the bottom:
- You’ll want **Bottom Overlay** visible (not Top Overlay), and vice versa.

Quick check:
- Look at the bottom layer tabs: **Top Overlay / Bottom Overlay**
- Or press **L** (View Configuration) and ensure the correct overlay layer is on.

## If you want text to always read normally
- Press **L** (View Configuration)
- Look for an option like **Mirror/Flip Text** / **Display Text on Bottom as Mirrored** (wording varies by version)
  - Disable it if you want bottom text to read left-to-right while you’re routing/inspecting.

## If the “missing designator” was actually on the other side
Once you flip back (V,B), it often “reappears” because it was on:
- Bottom Overlay, or
- You were looking at the board from the opposite side.

If you tell me whether you meant **the whole board is mirrored** (pads/tracks reversed) or just **text is mirrored**, I’ll point you to the exact checkbox in 26.3.0.

[M21] ME (2026-02-27 18:26):
What decoupling does the adg704 want?

[M22] AI (2026-02-27 18:26):
For **ADG704** (4:1 / 1:4 analog mux), treat it like any small CMOS switch: it wants a **tight local HF bypass** and (optionally) a **small bulk cap** if your rail is noisy or there’s any digital edge-current nearby.

### Recommended decoupling at the device
- **0.1 µF (100 nF) X7R** ceramic **right at VDD–GND**  
  - 0402/0603, shortest loop possible (cap → VDD pin → device → GND via).
- **+ 1.0 µF to 4.7 µF X7R** nearby on the same rail (optional but good practice)  
  - Helps if the rail is fed through a ferrite/trace inductance or shared with fast logic.

### If you’re running dual supply (ADG704 can be single-supply; some variants allow ± rails)
- Put **100 nF from each supply pin to GND** (or to their return), and if there’s a negative rail, add **100 nF from VSS to GND** as well.
- Still add a small bulk cap on the local rail node if the supply path is long.

### Layout notes that matter more than the value
- Put the **100 nF within a few mm** of the pins.
- Give the cap its **own ground via** close to the pad (don’t wander to a distant ground).
- Keep control lines away from sensitive analog nodes; add a **series 22–100 Ω** on digital select lines if you see ringing/EMI (not mandatory, but often helps).

### Any special “charge injection” cap?
Not required for the IC itself. If you’re switching high-impedance analog nodes and seeing glitches, you handle that at the **signal** (e.g., small C to ground at the receiving node, or lower source impedance), not by adding weird caps on VDD.

If you tell me your **VDD (3.3/5 V)** and whether you’re switching **video-ish bandwidth** or slower control signals, I’ll suggest whether the extra 1 µF/4.7 µF is worth placing and any select-line damping values.

[M23] ME (2026-02-27 18:29):
Why can’t i select a room I made

[M24] AI (2026-02-27 18:29):
In Altium, not being able to click-select a **Room** is almost always one of these:

## 1) Rooms are not enabled as selectable objects
**Fix**
- Open **Panels → Selection Filter**
- Make sure **Rooms** is ticked (and not locked out)
- Then try selecting again

## 2) You’re actually clicking a *fill/region* on a mechanical/courtyard layer, not the Room outline
Rooms are their own object type; if your view is busy (courtyard/regions/keepouts), your click will grab something else.

**Fix**
- Press **Tab** while your cursor is over the area to **cycle** through overlapping objects until it highlights **Room**
- Or use the PCB panel method below (most reliable)

## 3) It’s locked
**Fix**
- Use **Panels → PCB** → set dropdown to **Rooms**
- Click your room in the list
- In **Properties**, check **Locked** and untick it

## 4) You’re in a mode that blocks selection (filter/highlight/drag)
**Fix**
- Press **Shift + C** (clear filter)
- Press **Esc** to exit any active command (routing/placing/etc.)

## Bullet-proof method (works even when clicking fails)
1. **View → Panels → PCB**
2. Dropdown: **Rooms**
3. Click the room name → it selects it
4. Right-click → **Zoom** (or just hit `Z` then `A` for zoom all)

If you can share what you mean by “room I made” (manual **Design → Rooms → Define Room** vs auto-generated from ECO), I’ll tell you the exact menu path to edit/move/resize it.

[M25] ME (2026-02-27 18:30):
[image]
[attached file: IMG_05FCC58E-1CDD-468C-A2F6-ED8C6C8D04CC.jpeg]

[M26] AI (2026-02-27 18:30):
From your screenshot you’re in the **PCB Filter / Selection Filter** panel, and **Room isn’t enabled** for selection/highlight — that’s why you can’t click it.

### Fix (based on what I can see)
1. In that panel, in the **Object** list, tick **Room** (same column where “Component” is ticked).  
   - Right now only **Component** is ticked (top row).

2. Then clear any existing filter text so it doesn’t override you:
   - Click in the **Filter** box at the bottom and **delete** the expression (or press **Shift + C** in the PCB editor to clear filters).

3. Now try selecting the room again.

### Bullet-proof way (even if clicking still doesn’t work)
- Open **Panels → PCB**
- Dropdown: **Rooms**
- Click the room in the list → it selects every time.

### If it *still* won’t select after ticking Room
You’re likely clicking through other objects (courtyard/regions).
- Hover over the room boundary and press **Tab** to cycle objects until it says **Room** in the status bar, then click.

If you want, tell me whether you’re trying to select the room to **move/resize** it or to **delete** it — the best workflow differs slightly.

[M27] ME (2026-02-27 18:34):
[image]
I can select it and bring it up but not actually click it 
[attached file: IMG_DEE0A1B6-2349-4999-ABC6-EB679DD67237.jpeg]

[M28] AI (2026-02-27 18:34):
Yep — that’s a really specific (and common) Altium situation:

You **can select the Room from the PCB panel**, so the Room object exists, but you **can’t click it in the workspace** because either:

1) **Rooms are not enabled for interactive selection**, *or*  
2) You’re always clicking a different object sitting “on top” of it (courtyard/region/fill/keepout), *or*  
3) The room outline is **not being displayed**, so you’re clicking blind.

Here’s the quickest way to make it clickable.

## 1) Make Rooms selectable (interactive)
- **Panels → Selection Filter**
- Tick **Room**
- Also tick **Room in “Free”** column if you’re using that matrix (varies by version/panel mode).
- Then press **Shift + C** to clear any filters.

*(In your earlier screenshot, Room wasn’t ticked — so the PCB panel can select it, but mouse-picking in the editor won’t.)*

## 2) Make sure Rooms are actually visible
- Press **L** (View Configuration)
- Ensure **Rooms** (and/or **Room Names / Room Boundaries**) are enabled.
- If you’re in a mode where Rooms are dimmed/hidden, you won’t be able to visually target them.

## 3) If something is “on top”, cycle to the Room
When there’s a big courtyard/region sitting over the same area, clicks will hit that first.
- Hover where the room boundary should be
- Press **Tab** to cycle the selection candidates until the status bar says **Room**
- Then click/drag

## 4) Unlock / edit handles
Once selected from the PCB panel:
- Look in **Properties** for the Room:
  - **Locked** = OFF
  - Then you can **drag the room outline handles** (if boundaries are shown)

## 5) If you just want to move/resize the room without clicking it
Since you can select it via PCB panel:
- Select it in **PCB panel → Rooms**
- Use:
  - **M, M** (Move) or drag
  - **Properties → Boundary** options (depending on room type)

---

### One extra gotcha
If this is an **auto-generated room** from ECO (component class room), Altium sometimes makes it awkward to “grab” because it’s tied to class generation. In that case, the best workflow is:
- Select room in PCB panel → right-click → **Delete Room** (or **Remove Rooms** via menu)
- And disable “Generate Rooms” in **Project Options → Class Generation** if you don’t want them coming back.

If you tell me what you’re trying to do with it (**move it**, **resize it**, or **delete it**), I’ll give you the exact clean steps for that action.

[M29] ME (2026-02-27 18:39):
[image]
[image]
I can right click it and move, I can right click the menu and bring up clsss. I just can’t select it 
[attached file: IMG_8D92C5AD-8DFC-4679-9A21-8B22BB0F9034.jpeg]
[attached file: IMG_14030959-B732-47D7-9AC5-9198EDC3032B.jpeg]

[M30] AI (2026-02-27 18:39):
Got it — and your screenshots explain *exactly* what’s happening:

That big pink rectangle you’re interacting with is **not a Room object**. It’s a **courtyard / region primitive** (status bar says **Top Courtyard**), which is why:

- you can **right-click → move** (you’re moving that primitive),
- you can open **Edit Component Class** (because the components are in a class),
- but you **can’t left-click “select the room”** because there isn’t a selectable Room boundary there (or it’s hidden/disabled and you’re always clicking the courtyard region instead).

So you’re mixing up **Component Class membership** (what you’ve shown in the dialog) with an actual **Room boundary object**.

### Do this to prove it in 30 seconds
1. **Hide Top Courtyard** temporarily:
   - Press **L** → View Configuration → untick **Top Courtyard** (and Bottom Courtyard if needed)
2. Now try clicking where the room boundary should be.
   - If you suddenly can select it → the courtyard region was “on top” and stealing clicks.
   - If you still can’t → you likely don’t have a room object at all, only a class.

### Bullet-proof: select the Room object from the PCB panel
1. **Panels → PCB**
2. Dropdown at top: choose **Rooms**
3. If the list is empty → you **do not have any rooms**, full stop (only component classes).
4. If rooms exist, click one → it will select even if you can’t click it on the canvas.

### If you *do* have a room but can’t click it
Then it’s one of these two:

#### A) Rooms aren’t allowed to be selected by mouse
- **Panels → Selection Filter**
- Tick **Room**
- Then **Shift + C** to clear any filter/highlight state

#### B) Something overlays it (likely courtyard/region/keepout)
- Hover and press **Tab** to cycle until it says **Room** then click.

---

## What you probably actually want
It sounds like you’re trying to create a “placement grouping” for those parts (IC8 + Rs etc.). You can do that either with:

### Option 1 — **Component Class only** (what you’ve got)
Good for rules and selecting members, but **no boundary**.

### Option 2 — **Room** (boundary + auto-placement tool)
If you actually want a boundary:
- **Design → Rooms → Create Room From Selected Components**  
  (wording may be “Define Room” / “Generate Room from Component Class” depending on version)

Then it will appear in **PCB panel → Rooms** and becomes a real selectable object.

---

### One more important note
Your huge pink shape on **Top Courtyard** looks like a **bad courtyard region in the MMCX footprint**, which will keep messing with selection until you fix it in the footprint (delete/resize that oversized courtyard region).

If you answer just this: **In PCB panel → Rooms, do you see any rooms listed?**  
I’ll tell you the exact next click-path (either “you have no rooms” → create one, or “you have rooms but can’t select” → enable + de-overlay).

[M31] ME (2026-02-27 18:42):
[image]
Right, got it. Now I want to copy once room placement to another 
[attached file: IMG_2022FEF8-617A-4A02-A006-13C1FB750117.jpeg]

[M32] AI (2026-02-27 18:42):
Perfect — you’re in exactly the right dialog: **Confirm Channel Format Copy**. That’s Altium’s “copy this room’s placement/format to the other channel room” tool.

Here’s the clean way to use it without accidentally wrecking routing.

## Copy placement from one room to another (safe/default)
1. Make sure the correct rooms are set:
   - **Source Room:** the one you’ve already placed nicely
   - **Destination Room:** the one you want to match (e.g. `RoomDefinition_1`)

2. Tick only what you actually want to copy:
   - ✅ **Copy Component Placement** (this is the main one)
   - ✅ (Optional) **Copy Designator & Comment Formatting** (if you want overlay text moved/rotated the same)
   - ✅ (Optional) **Copy Room Size/Shape** (only if you want the destination room boundary to match too)
   - ⛔ **Copy Routed Nets** (leave OFF unless you truly want it to duplicate routing—this is where “tearing up tracks” pain comes from)

3. **Component matching**
   - Set **Match Components by Channel Offsets** (usually the right choice for multi-channel)
   - If it can’t match, it’ll either do nothing or do something weird—so if you see poor matching later, stop and we’ll fix the channel annotation/matching.

4. **Touching objects options**
   - If you want *only* the components in that channel to move, keep it conservative:
     - Prefer **Fully Enclosed Objects Only**
     - And/or tick **Copy Selected Objects Only** (if you preselected just the parts you want)

5. Click **OK**

## Practical “don’t mess me up” recipe
For your first attempt, use:
- ✅ Copy Component Placement  
- ✅ Copy Designator & Comment Formatting (optional)  
- ⛔ Copy Routed Nets  
- ⛔ Copy All Objects Touching the Room (unless you know why you need it)  
- Selection: **Fully Enclosed Objects Only**

That will clone the placement pattern without copying copper.

## After you click OK — sanity check
- Zoom to the destination room
- Confirm rotations and relative spacing look right
- Then re-run DRC / look for any unexpected moved items outside the room boundary

---

If you tell me whether your channels are genuinely identical (same refdes offset style, e.g. R1→R101) or you’ve got any “odd one off” parts per channel, I’ll suggest the best matching mode so it doesn’t mis-map components.

[M33] ME (2026-02-27 18:44):
[image]
[attached file: IMG_4AE6F0A2-021A-4F31-A9E1-1F96E1D8C2BC.jpeg]

[M34] AI (2026-02-27 18:44):
That dialog means Altium **can’t reliably map the source-room components to the destination-room components using “Channel Offsets”**. If you click **Yes**, it will still copy *something*, but the risk is it copies placement onto the **wrong parts** (or skips some), which is how you end up with a mess.

### What the two error types mean
- **Sequence Errors**: the designator numbering offset pattern isn’t consistent (e.g. R36→R136 works, but then there’s an R39 missing, or it jumps).
- **Failed Offset Matches**: for some source parts it can’t find a corresponding destination part with the expected offset.

## What you should do right now
### 1) Click **No** (recommended)
Unless you’re happy to manually verify every part afterwards.

## Then fix the mapping (pick one approach)

### Option A — Use explicit matching instead of “Channel offsets”
In that Channel Format Copy dialog there’s a drop-down for matching (you were on **Match Components by Channel Offsets**).

Switch to something like:
- **Match by Designator** (if the channels share same designators — rare), or
- **Match by Unique ID / Component GUID** (best if it’s a true multi-channel design that Altium understands), or
- **Match by Name + Comment + Footprint** (works surprisingly well if each room has identical BOM).

Exact wording varies by version, but the key is: **don’t rely on numeric offsets** if your designators aren’t perfectly offset-clean.

### Option B — Make the offsets consistent (best long-term)
If this is a proper repeated channel, you want the channels annotated with a clean offset:
- Channel 1: R1…R50, C1…C20, etc.
- Channel 2: R101…R150, C101…C120, etc. (or +100 offset, consistently)

Then recompile/update so the rooms are genuinely recognized as channels.

### Option C — Copy only the room boundary first (safe) then manually place
If you just want the same “box” area:
- Tick **Copy Room Size/Shape**
- Untick **Copy Component Placement**
This avoids any mapping issues entirely.

## If you *do* click Yes anyway
Do it only if:
- you’re copying a small subset, or
- you can visually verify the destination room afterwards.

Afterwards immediately check:
- do the same footprints land on the same relative locations?
- do polarised parts (diodes, ICs) have the correct rotation?
- are all connectors aligned?

---

### Quick diagnostic question you can answer without digging
Are the designators in each channel **offset by a fixed number** (e.g. R36 in room A corresponds to R136 in room B), or are they **independently annotated** / mixed?  
If you tell me that, I’ll tell you which matching mode is the least painful and how to set up annotation so this tool works flawlessly going forward.

[M35] ME (2026-02-27 18:46):
[image]
Do I need to do something here?
[attached file: IMG_DE72E13F-247F-4297-B251-283E82F8ADC1.jpeg]

[M36] AI (2026-02-27 18:46):
You’re in **Edit Room Definition**. You only need to change things here if the room is **not correctly “bound” to the right set of components**, or if you want Altium to **enforce** the room boundary.

From your screenshot the key line is:

**Where the object matches:** `Component Cla` … `Room Definition2`

That means this room’s membership is being driven by a **query** (likely a component class). If that query is wrong, you’ll get the channel-copy mapping errors you saw.

## What to do (practical checklist)

### 1) Click **Test Queries**
- If the highlighted preview (green/yellow) shows **exactly the components you intend** for that room, you’re good.
- If it shows the wrong set / missing parts / extras → fix the query source (next step).

### 2) Verify the drop-downs in “Where the object matches”
You want the room to match something stable, typically one of:
- **ComponentClass = RoomDefinition1** (or similar)  
- Or a channel-based rule if you truly have multi-channel annotation

Right now it looks like it’s tied to **Room Definition2** while the room name is **RoomDefinition_1** — that mismatch is a red flag.

**Action:** make sure the room’s query points at the *correct* class for that room (RoomDefinition_1 should reference the class for channel/room 1, etc.).

### 3) Don’t lock anything yet (unless you’re enforcing placement)
- Leave **Room Locked** and **Components Locked** **unticked** while you’re still placing/copying.
- If you want Altium to stop you accidentally dragging parts out later, tick **Room Locked** at the end.

### 4) Only use “Keep Objects Inside” if you actually want constraint behaviour
That setting makes it act like a placement constraint. It’s optional.

---

## The bigger picture: why you got “Channel-offset errors”
Those errors usually happen when the tool can’t see two *equivalent* rooms/channels. That’s often because:
- the rooms are not correctly defined by channel/class, **or**
- the designators are not offset cleanly.

So yes — the *one* thing worth doing here is:
✅ **make sure each room’s “Where the object matches” points to the correct component class/channel**, and confirm with **Test Queries**.

If you tell me what your intended mapping is (e.g. RoomDefinition_1 should contain U1, R5, C2, C13… and RoomDefinition_2 contains the same set but different designators), I’ll tell you exactly what the query should be.

[M37] ME (2026-02-27 18:47):
Do I need to room schematic also 

[M38] AI (2026-02-27 18:47):
You **don’t need “rooms” on the schematic** to route or to keep the PCB synced.

You only need schematic “rooms” (really: **channels / repeated blocks**) if you want Altium to understand that parts are **repeated instances** so you can use tools like **Copy Room Formats**, **channel offset matching**, auto-dup placement/routing, etc.

### When you *do* need something on the schematic
If your goal is: **“I placed one channel/room, now copy that placement to the other channel(s)”**, then yes — you need the schematic set up as a **multi-channel / repeated block** design (or at least have stable, repeatable component mapping), otherwise Altium can’t match parts reliably (hence your “channel-offset errors”).

That setup is typically:
- A **sheet symbol** instanced multiple times (channels), or
- A **repeated sub-sheet** with channel annotation/parameters.

### If you’re not doing proper multi-channel
You can still use PCB rooms manually, but Altium will struggle to “intelligently” copy placement between them unless:
- Designators are perfectly offset, *or*
- You match by Unique ID / consistent component mapping.

### Practical recommendation
- **For simple boards:** don’t bother with schematic rooms; just place/rout normally.
- **For repeated circuits:** use proper **multi-channel** in the schematic (sheet symbol repeated), then the PCB room/channel tools work cleanly.

If you tell me which case you’re in:
- **Is your design actually repeated** (same circuit 2+ times), or were you just using rooms as “placement boxes”?  
I’ll point you to the simplest workflow for your situation.

[M39] ME (2026-02-27 18:58):
[image]
Howndoninlocate target block with placement replication. It’s trying to do ic5 block which I’ve already done 
[attached file: IMG_4267AA31-8167-4094-A747-75F1B0EA7230.jpeg]

[M40] AI (2026-02-27 18:58):
You’re in **PCB Layout Replication** and Altium has auto-picked **IC5’s channel/block** as the *source* for replication — you want to (a) **see where the target block is**, and (b) **stop it trying to replicate the one you’ve already done**.

Here’s the clean way.

## 1) Locate / zoom to the Target Block
In that dialog:

1. In the **Target Blocks** list, click **Target Block 1** (or whichever).
2. Make sure the checkboxes at the top-left of the dialog are enabled (they’re usually):
   - ✅ **Select**
   - ✅ **Zoom**
   - ✅ **Clear Existing**
3. Now **single-click** a component inside the target block list (e.g. C12 / C11 / IC5 etc).  
   With **Zoom** enabled, Altium will jump to the physical location on the PCB and highlight that block in the workspace.

If it still doesn’t jump:
- Click the **Preview** pane component view; it often “activates” the block highlight.
- Or temporarily close the dialog and use **Panels → PCB → Components** to zoom to one of the target block designators (e.g. C12).

## 2) Stop it trying to replicate the block you’ve already done
In your screenshot you’ve got **NO ROUTING** and then **Target Block 1** with a checkbox. If it’s trying to do the “already done” one, you have to **remove it from the target set**.

Do one of these:

### Option A (most direct): untick the block
- Untick the checkbox beside **Target Block 1** (or whichever is the “already done” one).
- Then only tick the block(s) you still want replicated.

### Option B: delete the block from the target list
- Right-click **Target Block 1** → look for **Remove Target Block / Delete** (wording varies).
- If that menu isn’t available, use Option A.

### Option C: re-identify blocks so IC5’s channel isn’t treated as the “template”
- Close the dialog
- Run **Design → Rooms → Update Rooms** (or “Recreate Rooms”) if your channel mapping has drifted
- Then restart **PCB Layout Replication** and choose the correct **source** and **targets**.

## 3) Why it’s happening (so you can avoid it)
Replication keys off **channel/block identification** (designators / channel offsets / component matching). If Altium thinks IC5’s block is the canonical “block”, it’ll keep selecting it.

Usually that means:
- your blocks aren’t uniquely identified as channels, or
- the “source” selection didn’t start from the block you intended.

**Pro tip:** start Layout Replication by first selecting a component *in the block you want as the master*, then invoke the command. It tends to pick that as the source.

---

If you tell me the designators of the block you actually want to replicate **from** (e.g. “IC8 block”), I’ll tell you the exact “select this first → run tool → choose these targets” sequence so it locks onto the right one.

[M41] ME (2026-02-27 19:00):
[image]
How do I find my other target blocks 
[attached file: IMG_1EC3D47A-7892-47E8-A254-34907E0B599C.jpeg]

[M42] AI (2026-02-27 19:00):
In **PCB Layout Replication**, the “Target Blocks” list only shows blocks that Altium has successfully identified as **replicable instances** of the source block. If you’re only seeing **Target Block 1**, the other channels aren’t being recognised as targets yet.

### First: expand what’s already there
- Click **Expand All** (top right of the Target Blocks table)
- Or click the little triangle **▸** next to **Target Block 1**

That won’t magically create new blocks, but it confirms what Altium thinks the target is.

---

## How to make the *other* target blocks appear

### 1) You must have multiple “rooms/channels” defined
Layout Replication uses **rooms / channels / component classes** to detect repeated blocks.

Check:
- **Panels → PCB → Rooms**
  - Do you see RoomDefinition_1, _2, _3 etc?
  - If you only have one room, you’ll only ever get one target block.

If you don’t have rooms:
- **Design → Rooms → Create Rooms From Component Classes**
  (or “Generate Rooms” / “Recreate Rooms”, wording varies)

### 2) Your other channels must match the source block membership
If Altium can’t match the component set, it won’t offer the block as a target.

Typical reasons it fails:
- Designators aren’t offset consistently
- One channel has extra/missing parts (even an extra DNI cap)
- Footprints differ (0402 vs 0603 etc.)
- Components aren’t in the same component class/channel

**Quick test:** pick one “missing” block’s key component (e.g. the other ADG704) and see if it exists and is in the same class.

### 3) You might be in a “single-channel / wrong source” situation
A good trick:
1. Cancel the dialog.
2. On the PCB, **click a component in the block you want to use as the SOURCE** (the one you already placed nicely).
3. Then run **Tools → PCB Layout Replication** again.
This often makes Altium choose the right source and then it finds the other targets.

### 4) If it still only finds one target: force it via Component Classes
Make sure each channel is a **Component Class** and rooms are generated from them:
- **Design → Classes… → Component Classes** (confirm there are multiple)
- Then **Design → Rooms → Create Rooms From Component Classes**
- Then retry Layout Replication

---

## Fast “where are my other blocks physically?”
Even if replication won’t list them, you can jump to them:
- **Panels → PCB → Components**
- Search `IC5` / `IC8` / whatever the repeated IC is
- Right-click → **Zoom**

---

### The tell in your screenshot
You’ve got a yellow warning triangle next to **Target Block 1**. That often means Altium sees only one valid target and even that has a mapping issue.

If you tell me how many repeated circuits you expect (2? 4?) and what the “anchor” component is in each (e.g. IC5, IC6, IC7, IC8), I’ll give you the exact sequence to:
1) ensure rooms/classes exist,  
2) make Altium recognise all blocks, and  
3) replicate placement without touching routing.

[M43] ME (2026-02-27 19:03):
[image]
That’s room 2
[attached file: IMG_E5DEBB02-AEA9-4B70-9638-356664717E64.jpeg]

[M44] AI (2026-02-27 19:03):
Nice — that tells us something important:

- You’re editing **RoomDefinition_2** (top left),
- but the **Test Queries Result** popup is reporting **Rule: RoomDefinition_1** and showing **10** objects matched.

That mismatch is one of the reasons Altium isn’t finding “other target blocks” reliably.

## What this means
Your rooms are being driven by **query rules**, and at least one of these is true:

1) The **room rule names** and the **room objects** are out of sync (RoomDefinition_2 is referencing the wrong rule / class), or  
2) You’ve got **multiple room definition rules** and the one with higher priority is catching the objects (so it reports RoomDefinition_1).

Either way: Altium can’t cleanly separate channels/blocks → replication sees only one “valid” target.

---

## What to do next (quick and concrete)

### 1) In this dialog, check the “Where the object matches” line
You want it to be something unambiguous like:
- **Component Class = RoomDefinition2** (for RoomDefinition_2)

In your screenshot it *looks* like that’s what it says — good. But the test result still claims RoomDefinition_1, which screams **rule priority conflict**.

### 2) Fix rule priority / duplication
Go to:
- **Design → Rules…**
- Find the section for **Rooms / Room Definition** (or search for “RoomDefinition”)
- You’ll likely see multiple rules:
  - RoomDefinition_1
  - RoomDefinition_2
  - etc.

Now ensure:
- Each rule’s **query** matches only its class (e.g. `InComponentClass('RoomDefinition2')`)
- The rules don’t overlap
- Priorities are sane (or all non-overlapping so priority doesn’t matter)

### 3) Re-test
Back in RoomDefinition_2 → **Test Queries**
- It should now say **Rule: RoomDefinition_2**
- And match the correct count.

---

## Why this matters for “finding other target blocks”
PCB Layout Replication uses these room/channel separations to identify the repeated blocks. If the rules overlap (Room 1 rule also matches Room 2 parts), it collapses everything into effectively one block, so you only see **Target Block 1**.

---

### Fast shortcut if you want to avoid the whole rules mess
If you don’t actually need Altium’s “room rules” long-term:
- **Design → Rooms → Remove Rooms**
- Then re-create cleanly from classes:
  - **Design → Classes…** confirm your component classes are correct
  - **Design → Rooms → Create Rooms From Component Classes**

That often clears the “RoomDefinition_1 catching everything” problem in one shot.

If you can tell me: **Do you have RoomDefinition_1 / _2 / _3 / _4 rules in Design → Rules**, or did you create rooms manually? I’ll point you at the quickest clean-up path for your exact setup.

[M45] ME (2026-02-27 19:04):
[image]
[attached file: IMG_D1FC6BE8-F242-401A-BC83-6A9962E6C347.jpeg]

[M46] AI (2026-02-27 19:04):
Yep — this view is the *right* one, and it actually shows you’re **mostly OK**:

- **Room name:** `RoomDefinition_2`
- **Where the object matches:** `Component Class = Room Definition2`
- Preview highlights a small set of parts (good)

So you **don’t need to change anything here** *unless* your other rooms don’t each point at a **unique class**. The replication issue (only seeing one target block) usually happens when:

1) **Only one room exists** (or only one room has the correct class binding), or  
2) Multiple rooms exist but **their queries overlap** (room 1 rule matches room 2 parts), or  
3) The repeated blocks aren’t “equivalent” (missing/extra parts per room), so Altium refuses to treat them as additional target blocks.

### What to do next (quick, deterministic)
#### 1) Confirm you actually have multiple rooms
- **Panels → PCB → Rooms**
- You should see: `RoomDefinition_1`, `_2`, `_3`… (however many you expect)

If you only see `_2` (or just one), that explains it: only one target block.

#### 2) Confirm each room maps to its *own* component class
For each room, open this same dialog and check:
- RoomDefinition_1 → ComponentClass = RoomDefinition1  
- RoomDefinition_2 → ComponentClass = RoomDefinition2  
- etc.

#### 3) Ensure each class has the same “shape” of components
Replication wants the same “pattern”:
- same footprints
- same count of parts
- no extras (even an extra DNI cap can break it)

A fast check:
- **Design → Classes… → Component Classes**
- Compare member counts for each RoomDefinition class.

### If you want the “other target blocks” to appear immediately
The most reliable reset is:
1. **Design → Rooms → Remove Rooms**
2. **Design → Rooms → Create Rooms From Component Classes**
3. Re-run **PCB Layout Replication** after selecting a component in the *source* block first.

If you tell me how many blocks you expect (2? 4?) and whether you have `RoomDefinition_3` / `_4` etc, I’ll tell you exactly which of the three failure modes above you’ve hit and the shortest fix.

[M47] ME (2026-02-27 19:05):
Yes, I set up 4, I have 4 blocks 

[M48] AI (2026-02-27 19:05):
Good — if you’ve got **4 rooms/blocks** but Layout Replication only shows **Target Block 1**, then Altium is failing to recognise the other 2–3 as valid replication targets. That’s almost always one of these:

1) the other rooms aren’t actually mapped to **unique component classes** (or overlap),  
2) the blocks aren’t **equivalent** (extra/missing parts, footprint differences), or  
3) the tool is starting from the wrong “source” and collapsing the others.

Here’s the fastest way to diagnose and fix without guesswork.

## 1) Verify all 4 rooms exist and are distinct
- **Panels → PCB → Rooms**
  - You should see 4 entries (RoomDefinition_1…4 or similar).
- Click each room in the list and hit **Zoom**.
  - Confirm each room highlights a different physical cluster.

If any room zooms to the same place as another → your room queries overlap.

## 2) Check each room’s query binding (the big one)
For each room:
- Right-click room (from PCB panel) → **Properties / Edit Room Definition**
- Confirm **Where the object matches** is:
  - RoomDefinition_1 → `ComponentClass = RoomDefinition1`
  - RoomDefinition_2 → `ComponentClass = RoomDefinition2`
  - RoomDefinition_3 → `ComponentClass = RoomDefinition3`
  - RoomDefinition_4 → `ComponentClass = RoomDefinition4`
- Click **Test Queries** and make sure it reports the *same room rule name* (not RoomDefinition_1 for everything).

If Test Queries always references RoomDefinition_1, you’ve got a **rule priority / overlap** problem.

### Quick fix for overlap
- **Design → Rules…**
- Search “RoomDefinition”
- Ensure each rule query is unique, e.g.:
  - `InComponentClass('RoomDefinition1')`
  - `InComponentClass('RoomDefinition2')` etc.
- Make sure none of them are something broad like `All` or `InRoom()`.

## 3) Confirm block equivalence (why only one target)
In **Design → Classes… → Component Classes**
- Compare member counts for RoomDefinition1/2/3/4.
- They should match (same number of parts, same footprints).

If one room has (say) an extra DNI capacitor, replication may refuse it as a “target block”.

## 4) Make Layout Replication pick the right “source” and rediscover targets
Do this exact sequence:

1. **Cancel** the PCB Layout Replication dialog.
2. On the PCB, **click one component inside the block you want as the MASTER** (e.g. IC8 or the ADG704).
3. Run **Tools → PCB Layout Replication** again.
4. In the dialog, look at Target Blocks:
   - you should now see **Target Block 1, 2, 3** (targets exclude the source).

If you still only see one target block, it’s definitely #2 (overlap) or #3 (non-equivalence).

## 5) Nuclear “reset rooms cleanly” (often quickest)
If you suspect the room definitions got messy:
1. **Design → Rooms → Remove Rooms**
2. **Design → Rooms → Create Rooms From Component Classes**
3. Re-run Layout Replication (step 4 above)

This clears hidden/duplicated room rules in one go.

---

### The quickest single check to pinpoint the cause
In **Component Classes**, do RoomDefinition1/2/3/4 all have the **same number of members**?

- **Yes** → it’s almost certainly **room rule overlap/priority**.
- **No** → replication won’t see them as equivalent targets until the member sets match.

If you tell me the member counts you see (e.g. 10/10/10/9) I’ll tell you exactly what to fix next.

[M49] ME (2026-02-27 19:09):
Ok, I’ve deleted the other 2. I just have 2 rooms now

[M50] AI (2026-02-27 19:09):
Nice — that simplifies things a lot. With **2 rooms** you can make replication behave reliably.

Here’s the clean, low-risk sequence to copy placement from Room A → Room B and avoid the offset/mismatch warnings.

## 1) Make sure each room is “owned” by a unique component class
- **Panels → PCB → Rooms**
- Select **RoomDefinition_1** → **Properties / Edit Room Definition**
  - **Where the object matches:** `ComponentClass = RoomDefinition1`
- Do the same for **RoomDefinition_2**
  - `ComponentClass = RoomDefinition2`

(If either room points to the wrong class, fix it now.)

## 2) Ensure the two classes have identical membership
- **Design → Classes… → Component Classes**
- Check RoomDefinition1 and RoomDefinition2 have:
  - same *count* of members
  - same footprints (e.g. both have ADG704, same MMCX footprint, same R/C footprints)

If they differ, Layout Replication will either not list the target or will warn.

## 3) Use PCB Layout Replication the right way
1. On the PCB, click a component **inside the “master” room** (the one you’ve placed nicely).
2. Run **Tools → PCB Layout Replication** (or the menu entry you used to open that dialog).
3. In the dialog, you should see **one Target Block** (the other room).
4. Tick only:
   - ✅ component placement (and designator/comment formatting if you want)
   - ⛔ routing (leave off for now)
5. Click **Replicate**

## 4) If you still get “Channel-offset errors”
That’s because it’s trying to match by designator offsets.

Two ways out:

### Option A (best): use a different matching mode
In the replication/format copy tool, change matching away from **Channel Offsets** to a mode based on:
- **Unique ID / Component GUID**, or
- **Design Item ID + Footprint + Comment**
(wording varies)

### Option B (quick and dirty): accept, but verify
If it’s only a handful of parts and they’re obvious, you *can* continue — but immediately sanity-check:
- IC orientation
- connector orientation
- polarised caps/diodes
- any “odd one-off” parts

## 5) Pro move: after placement is copied, lock the room
Once happy:
- Tick **Room Locked** (and optionally Components Locked) in the room definition so you can’t accidentally drag it apart.

---

If you tell me: are the two rooms **identical circuits** (same parts, just different designators), or are they slightly different (DNI parts / footprint swaps)? That decides whether you should force “GUID matching” or just tidy the classes and channel-offset will work.

[M51] ME (2026-02-27 19:11):
[image]
That’s room 1
[attached file: IMG_9A9E0912-5204-4CBA-A08A-32E15BAD725C.jpeg]

[M52] AI (2026-02-27 19:11):
Great — this screenshot is exactly what we need. Your **Component Class “Room Definition1”** currently contains:

**C23, C24, C28, IC8, J8, R34, R36, R37, R38, R39** (10 members)

So Room 1’s class is clean and finite. The next step is to make sure **Room Definition2** contains the *equivalent* set (same footprints / same function parts), otherwise replication will keep complaining or only find one target.

## What to do next (fast)
### 1) Open **Room Definition2** class and compare
- **Design → Classes… → Component Classes → Room Definition2**
- You want the **same count (10)** and same pattern:
  - 3 capacitors (Cxx)
  - 1 IC (ICx = ADG704)
  - 1 connector (Jx = MMCX)
  - 5 resistors (Rxx)

If Room Definition2 has 9 or 11, or a different footprint/comment, replication will struggle.

### 2) Sanity check: don’t mix IC5/IC8 channels
Right now RoomDefinition1 contains **IC8 / J8**. That’s fine — just ensure RoomDefinition2 contains the *other* instance, e.g. **IC5 / J4** (or whatever your second channel uses). The numbers don’t matter; the *membership shape* does.

### 3) Recreate rooms from classes (optional but often fixes targeting)
Once both classes are correct:
- **Design → Rooms → Remove Rooms**
- **Design → Rooms → Create Rooms From Component Classes**
Now Layout Replication will usually list the other room as the one target block.

### 4) Replicate placement (safe settings)
- Select a component in the **master** room (RoomDefinition1 / IC8 block)
- **Tools → PCB Layout Replication**
- Tick the target block
- ✅ placement, ✅ designator/comment formatting (optional)
- ⛔ routing
- Replicate

---

## One small naming tip
Your class is called **“Room Definition1”** (space) but earlier we saw **RoomDefinition_1** (underscore) in room names. That’s OK, but it can get confusing. If you rename, keep it consistent:
- Class: `RoomDef_1`, `RoomDef_2`
- Room: `RoomDef_1`, `RoomDef_2`

No functional requirement — just reduces human error.

If you post a screenshot of **Room Definition2** members (same dialog), I’ll tell you immediately whether it’s “equivalent enough” for replication and what to add/remove.

[M53] ME (2026-02-27 19:14):
[image]
Yes, that’s looks right 
[attached file: IMG_83E488BA-BC89-44A6-9A3D-E1CC32F040B9.jpeg]

[M54] AI (2026-02-27 19:14):
Yep — that’s a clean match.

**Room Definition2** has **10 members** as well: **C17, C21, C22, IC6, J5, R23, R24, R25, R27, R28**.  
So both classes are the same “shape” (3 caps, 1 IC, 1 connector, 5 resistors). That’s exactly what Altium needs for replication to behave.

Now do this to copy placement from Room 1 → Room 2 reliably:

## 1) Recreate the rooms from the classes (recommended reset)
This avoids any stale/overlapping room rules from earlier:
1. **Design → Rooms → Remove Rooms**
2. **Design → Rooms → Create Rooms From Component Classes**

You should end up with exactly **two rooms**, one for each class.

## 2) Run placement replication from the correct source
1. On the PCB, click a component in **Room Definition1** (e.g. **IC8** or **J8**).
2. Run **Tools → PCB Layout Replication**
3. In the dialog:
   - You should see **one Target Block** (the other room).
   - Tick that target block.
   - Ensure **routing is OFF** (you only want placement right now).
4. Click **Replicate**

## 3) If it still tries “channel offset matching” and warns
Because your designators aren’t a simple +100 offset (IC8 ↔ IC6 etc.), Altium might still moan if it’s in “offset” mode.

Two ways through:
- In the replication dialog, switch matching away from **Channel Offsets** (if there’s a drop-down) to **match by design item/footprint/comment** or **UID**.
- Or proceed and just verify orientation (IC + connector) and that each footprint landed in the right spot.

## 4) Lock afterwards (optional)
When you’re happy:
- Edit room → tick **Room Locked** (and optionally Components Locked).

If you tell me what you’re trying to copy next (just placement vs placement+designator formatting vs routing too), I’ll give you the exact checkbox set so it doesn’t touch your existing tracks.

[M55] ME (2026-02-27 19:16):
[image]
Can’t see remove 
[attached file: IMG_5FA6C675-834E-46C8-8E77-D3468CD991DC.jpeg]

[M56] AI (2026-02-27 19:16):
Yep — in your screenshot you’re in **Design → Rooms**, and Altium 26.x often **doesn’t show “Remove Rooms” in that submenu**. It’s not you — it’s just buried elsewhere / context-sensitive.

Here are the reliable ways to remove rooms.

## Method 1 (fastest): delete them from the PCB panel
1. **Panels → PCB**
2. Dropdown (top of panel) → **Rooms**
3. Click a room (RoomDefinition_1 / _2)
4. Press **Delete**
   - or right-click → **Delete**

That removes the actual room objects from the PCB.

## Method 2: delete rooms with a filter (bulk)
1. Open **Panels → PCB Filter**
2. In the Filter box type:
   - `IsRoom`
3. Click **Select**
4. Press **Delete**

## Method 3: remove all rooms via the Rooms menu (if present elsewhere)
Sometimes it’s under:
- **Tools → Component Placement → Rooms** (varies), or
- **Design → Rooms → Delete Rooms** (wording differs)

But honestly, Method 1 is the one I’d use every time.

---

### After deleting, recreate cleanly from your two component classes
Once rooms are deleted:
- **Design → Rooms → Create Rooms from selected components** (or from classes)
OR (better for you since you already made classes):
- **Design → Rooms → Create… from selected components** won’t use classes,
so instead do this:
1. Select all members of **Room Definition1** class (PCB panel → Component Classes → right-click → Select Members)
2. **Design → Rooms → Create Rectangular Room from selected components**
3. Repeat for Room Definition2

That yields two clean room objects with no legacy rule overlap.

If you want, tell me what you see in **PCB panel → Rooms** right now (names/count). I’ll tell you the quickest “delete → recreate → replicate” flow for your exact state.

[M57] ME (2026-02-27 19:20):
Done that, recreated them and still nothing 

[M58] AI (2026-02-27 19:20):
Alright — if you’ve **deleted rooms**, **recreated them**, and **PCB Layout Replication still shows “nothing” / no usable target**, then one of these is true:

1) the new rooms are **pure geometry** (manual rooms) and **not “definition rooms”** tied to your component classes, so Altium can’t treat them as replicated blocks, **or**
2) you’re using the wrong tool for what you want (Layout Replication vs Room Format Copy).

Given your screenshots, you actually want **Room Format Copy** (placement clone), not Layout Replication.

## Use the right tool: Copy Room Formats (works with 2 rooms)
This is the menu item you *do* have (in your screenshot):

**Design → Rooms → Copy Room Formats**

### Correct sequence (no ambiguity)
1. **Click inside the source room** (the one you’ve placed how you want).
2. Go **Design → Rooms → Copy Room Formats**
3. In the dialog:
   - **Source Room** = your good one
   - **Destination Room** = the other one
   - Tick:
     - ✅ **Copy Component Placement**
     - ✅ (optional) **Copy Designator & Comment Formatting**
     - ⛔ **Copy Routed Nets** (leave OFF unless you want copper duplicated)
   - Set containment to **Fully Enclosed Objects Only**
4. **OK**

This method does *not* rely on “channel-offset matching” the same way Layout Replication does, and it’s the most reliable for “two identical rooms”.

---

## If Copy Room Formats still can’t see the destination room
Then your rooms are not “real” definition rooms (i.e., not bound to a query/class).

### Make the rooms definition-driven (critical)
For **each** room:
1. Select the room (PCB panel → Rooms)
2. Open **Properties / Edit Room Definition**
3. Under **Where the object matches**, set:
   - Room 1 → `ComponentClass = 'Room Definition1'`
   - Room 2 → `ComponentClass = 'Room Definition2'`
4. Hit **Test Queries**
   - It must highlight the correct 10 components.

If you created rooms using “Create Rectangular Room from selected components”, they often start as “manual” and won’t behave like class-driven rooms until you set this.

---

## One more gotcha that blocks both tools
If the rooms overlap (even slightly), Altium can get confused about ownership/matching.

Quick check:
- Press **L** → turn on room boundaries/names
- Ensure the two room rectangles **do not overlap** at all.

---

### Practical recommendation for you, right now
Use **Copy Room Formats** (not PCB Layout Replication) and keep it to **placement only**. That should get you moving.

If you tell me what “still nothing” means exactly (e.g., **destination room dropdown empty**, or **it copies but nothing moves**, or **it throws offset errors**), I can pinpoint the single setting that’s wrong — but the steps above are the most common fix path in 26.x.

[M59] ME (2026-02-27 19:22):
[image]
That’s room 1
[attached file: IMG_D3C0EC63-6A13-4D82-AF5F-E503C7895334.jpeg]

[M60] AI (2026-02-27 19:22):
This screenshot is the smoking gun: your **Room object is called `RoomDefinition` (no “_1”)**, but its rule binding is **ComponentClass = `Room Definition1`**.

That’s fine in principle — **the room name doesn’t have to match the class** — but it *does* mean if you “recreated rooms” manually you may now have:

- **two rooms with near-identical names** (hard to pick in the Copy Room Formats dialog), or
- a room that’s correctly bound to the class, but the *other* room is **not** (or both are bound to the same class), so the copy tool has “nothing” to map to.

Let’s make this deterministic.

## 1) Verify Room 2 is bound to Room Definition2
Do the same dialog for the other room and confirm:
- **Where the object matches:** `ComponentClass = Room Definition2`

If it accidentally says Room Definition1 for both rooms, Copy Room Formats will behave like “nothing”.

## 2) Give the rooms distinct names (this helps the copy dialog)
In each room’s **Name** field:
- Rename this one to: `RoomDefinition_1`
- Rename the other to: `RoomDefinition_2`

Click **OK** after each.

This doesn’t change membership; it just makes the **Source Room / Destination Room** dropdowns unambiguous.

## 3) Now use Copy Room Formats (placement only)
- **Design → Rooms → Copy Room Formats**
- Set:
  - **Source Room:** `RoomDefinition_1`
  - **Destination Room:** `RoomDefinition_2`
- Tick:
  - ✅ Copy Component Placement
  - ✅ (optional) Copy Designator & Comment Formatting
  - ⛔ Copy Routed Nets
- Set: **Fully Enclosed Objects Only**
- OK

## 4) If it still “does nothing”
Two common blockers:

### A) Components are locked
In that room dialog, ensure **Components Locked** is **unchecked** for the destination room.

### B) The destination room already has components placed but not “owned”
Click **Test Queries** on both rooms:
- It should highlight **exactly** the 10 components of each class.
If room 2 highlights the wrong set (or none), then the room isn’t actually bound correctly.

---

### Quick sanity check you can do immediately
Open **Panels → PCB → Rooms**:
- Do you see **two rooms** and are their names distinct?
If they’re both just “RoomDefinition”, that alone can make the copy dialog look like it has “nothing” obvious to choose.

If you show me the **Room 2** dialog (same screen) I can tell you in one glance whether it’s bound correctly or accidentally pointing at the wrong class.

[M61] ME (2026-02-27 19:24):
[image]
[image]
[attached file: IMG_060EE0EE-45C0-43A9-ADD5-74D6D7CE89AB.jpeg]
[attached file: IMG_60797D69-9E1E-4731-A2F5-0161909025AA.jpeg]

[M62] AI (2026-02-27 19:24):
Brilliant — **these two screenshots confirm the room definitions are now correct**:

- **RoomDefinition1** → `ComponentClass = Room Definition1`
- **RoomDefinition2** → `ComponentClass = Room Definition2`
- Neither room/components are locked.

So if you’re still seeing “nothing” when trying to copy/replicate, it’s now down to **how you’re invoking the copy**, or a **matching setting** (Altium still trying to do channel-offset mapping).

## Do this exact “can’t fail” copy
### 1) Make sure you start from the source room
- Close these dialogs.
- Click a component inside **RoomDefinition1** (source/master).

### 2) Use the tool that matches what you want
Go: **Design → Rooms → Copy Room Formats**

### 3) In the dialog set these options
- **Source Room:** RoomDefinition1  
- **Destination Room:** RoomDefinition2  
- Tick:
  - ✅ **Copy Component Placement**
  - ✅ (optional) **Copy Designator & Comment Formatting**
  - ⛔ **Copy Routed Nets**
  - ✅ **Copy Selected Objects Only** (IMPORTANT)
- Then before clicking OK:
  - **Pre-select the exact components you want copied** (see step 4)

### 4) Pre-select the components (this avoids mapping/offset issues)
This is the trick that dodges “channel offset” entirely:

1. **Panels → PCB → Component Classes**
2. Select **Room Definition1** → right-click → **Select Members**
3. Now run **Copy Room Formats** and keep **Copy Selected Objects Only** ticked.

Now Altium is copying **those exact selected components’ placement** into the destination room instead of trying to infer offsets.

## If it still doesn’t move anything
Two common blockers:

### A) The destination components are already placed and Altium refuses to move them because of interactive placement rules
Try:
- Temporarily turn off **component “push” / collision avoidance** (or just move the destination room contents out of the way first).
- Easiest: select all members of **Room Definition2** class and **move them aside** (so you can see the copy clearly).

### B) You’re on the wrong “copy mode”
If you see any “Match components by channel offsets” options in the dialog, set it to **match by Design Item ID / Comment / Footprint** (anything *not* offsets).

## Sanity check that the tool is actually seeing both rooms
In **Copy Room Formats** dialog, do you see both rooms listed in Source/Destination dropdowns?  
- If **yes** → the above selection-based method will work.  
- If **no** → you’re not using *Copy Room Formats* (or you’re in PCB Layout Replication instead).

If you show me the **Copy Room Formats** dialog screen (the one with Source/Destination and checkboxes), I can tell you exactly which box is stopping it.

[M63] ME (2026-02-27 19:45):
[image]
What do these brackets mean?
[attached file: IMG_73556C96-FA7D-499D-A6CB-BE3430754864.jpeg]

[M64] AI (2026-02-27 19:45):
Those **brackets with a number** are simply the **document instance count** in your workspace/project group.

- `PCB.PcbDoc (1)` = you currently have **one PCB document** with that name loaded in the workspace.
- `Schematic.SchDoc (2)` = there are **two schematic sheets** open/loaded (or two documents with that base name).
- `CS_SCH_Lib.SCHLIB (2)` = you’ve got **two SCHLIB documents** in the workspace (often because the same library is open twice, or you have two similarly-named SCHLIBs and Altium is grouping them by base name).

It’s **not** a revision number and **not** an error by itself.

### Why you might see “(2)” unexpectedly
Common causes:
- You opened the same file twice (e.g., one from the project, one from a different folder / Free Documents).
- You have **two different files with the same name** in different paths.
- You have one in **Free Documents** and one in **Source Documents**.

### Quick way to confirm
Right-click the item → **Open / Properties** (or **Explore** / **Open Containing Folder**) and check the full path. If there are two, they’ll point to different locations.

If you want, send a wider shot showing the two `CS_SCH_Lib.SCHLIB` entries expanded (or right-click menu), and I’ll tell you which one is the “real” one tied to your project.
