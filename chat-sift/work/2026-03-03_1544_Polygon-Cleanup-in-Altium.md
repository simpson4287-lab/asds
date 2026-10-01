# Polygon Cleanup in Altium
Date (UTC): 2026-03-03 15:44
Conversation ID: 69a701d4-d1ec-838a-84ee-149b7d76877d
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-03 15:44):
[image]
When taking over this hod, is ok to just delete all the polygons to clean things up
[attached file: IMG_0C98E8DE-DC1F-4E0C-96B4-EDA97A6CC82B.jpeg]

[M2] AI (2026-03-03 15:44):
You *can* delete them, but as a “clean-up” move it’s usually the fastest way to accidentally break the board.

Polygons in Altium are often doing **real electrical work**, not just visual tidying:

- **Power distribution / planes** (especially inner layers like your W11/W12 entries): deleting can disconnect power nets or change IR drop.
- **Return paths / EMC control**: removing a “ground guard” / reference pour can wreck high-speed return current routing, crosstalk, emissions.
- **Thermal relief behaviour**: polygons carry the connect style (direct/relief), spoke width, etc. Deleting/recreating can silently change solderability.
- **Shielding / guard rings**: your screenshot shows nets like `RD_GUARD_0` — those are very likely intentional.

### Safer “takeover” workflow (what I’d do instead)
1. **Commit/save a restore point** (or copy the PCB file) so you can revert cleanly.
2. In **Polygon Pour Manager**:
   - **Shelve all** polygons (instead of deleting) to see what routing looks like without them.
   - Then **Repour All** and run **DRC** to check if they were masking problems (clearances, shorting, dead copper, etc.).
3. **Interrogate a few key polygons** (double-click / properties):
   - Net assignment (GND, supplies, guard nets)
   - Layer
   - Pour mode / priority / pour order
   - Connect style + thermal settings
   - “Pour over same net polygons only”, dead copper removal, etc.
4. If the issue is “messy/duplicated polygons”:
   - **Rename** them consistently (GND_W12_Main, GND_W12_Guard, etc.).
   - **Delete only true junk**: e.g., tiny stray polygons on “No Net”, duplicates that overlap with same purpose, or legacy experiments—*after* you’ve proven they aren’t referenced by rules/intent.
5. After any cleanup: regenerate outputs and sanity check (**power nets continuity**, **plane connectivity**, impedance/reference layers, etc.).

### When deleting *is* reasonable
- Polygons are clearly **temporary**, **No Net**, or obviously accidental.
- You’re planning a **full re-authoring of the plane strategy** and you’ve confirmed what nets/layers must exist.
- You have a known-good reference (old gerbers / released outputs) to compare against.

If you tell me what the board is (high-speed sensor? mixed-signal?) and which nets those inner pours are meant to be (GND, RD_GUARD_0, supplies), I can suggest a “minimum-risk” consolidation plan (including the exact settings to standardise on).

[M3] ME (2026-03-03 15:52):
[image]
How do I shape this to the circle 
[attached file: IMG_BE276218-D951-49AC-904D-BA310E2FFBEC.jpeg]

[M4] AI (2026-03-03 15:52):
You’ve basically got a polygon/region boundary that’s currently “freehand”, and you want its edge to become a true circular arc that matches (or is concentric with) that dotted clearance circle.

In Altium, do it like this (quick + clean):

### Option A — Reshape the polygon using **Arc** segments (most common)
1. **Select the polygon** (click its outline so the vertices show).
2. Go to **Tools → Polygon Pours → Polygon Actions → Modify Polygon**  
   (or right-click the polygon edge → **Polygon Actions**).
3. Choose **Modify Vertices** / **Edit Polygon** (wording varies by version).
4. While editing:
   - **Delete** the straight segments that should become the circle (select the vertices/edges and remove them).
   - **Add an arc** segment:
     - Use **Place → Arc** while in vertex edit (or the context menu: **Convert Segment → Arc** if available).
     - Snap the arc endpoints to your remaining vertices.
5. Set arc as **tangent** / adjust by dragging the arc handles until it matches the circle.

**Tip:** Turn on snapping: `Shift+E` for snap options; set **Snap to Center** / **Snap to Objects**.

---

### Option B — Make it *exact* by drawing a circle first, then “copy shape” into the polygon
This is the most deterministic way if you want a perfect circle.

1. **Place a Circle** (or Arc) on the *same layer* as the polygon outline:
   - **Place → Arc → Full Circle** (or Place → Circle if you have it)
   - Make it the exact diameter you want (type in properties).
2. Select the circle/arc.
3. Use **Tools → Convert → Create Region from Selected Primitives** (or “Convert to Region”).
4. Now you have a **Region** that is a perfect circle.
5. Use that region to define copper instead of fighting polygon vertices:
   - Either keep it as a Region (often fine),
   - Or use it as a **Polygon Cutout** / **Combine/Subtract** depending on what you’re trying to achieve.

---

### Option C — If you’re trying to “hug” the clearance circle around a pad/via array
Often you don’t actually want to hand-shape anything—just let rules do it.

- In the polygon properties:
  - Enable **Remove Necks** / **Remove Islands** as needed
  - Check **Arc Approximation** (smaller = rounder edge, but more vertices)
  - Ensure clearance rules are correct
- Then **Repour**.

This won’t make a *perfect* circle boundary, but it will follow the rule-driven keepouts.

---

### One key question (so I don’t steer you wrong)
Do you want the copper to be:
- **a circular pour area** (copper disk/ring), **or**
- a **circular cutout/anti-pad** (keep copper out inside the circle)?

If you tell me which of those two it is, I’ll give you the exact clicks for the best method (Region vs polygon outline vs polygon cutout).

[M5] ME (2026-03-03 15:53):
The connector was there but popped out on eco 

[M6] AI (2026-03-03 15:53):
Yep — that’s a classic ECO symptom: the PCB thinks the connector is **not meant to exist** (or not meant to exist *there*), so on sync it gets **deleted or swapped**.

Here are the main causes, in the order I’d check them, and the quickest way to recover without making the file worse.

## Why it “pops out” on ECO
### 1) The connector is **not in the schematic** (or not compiled)
- If it was manually placed on the PCB only, the next ECO will remove it.
- Or it *is* on the schematic but sits in a **disabled variant**, **uncompiled sheet**, or behind a compile problem.

**Check:** In schematic, compile (Project → Compile) and confirm the connector appears in the **Navigator / Components panel**.

### 2) It’s on the schematic but has **wrong footprint link**
- If the schematic component links to a different footprint (or “no footprint”), ECO will replace/remove the PCB instance.

**Check:** Schematic component properties → **Models → PCB Footprint**.

### 3) Duplicate designators / multi-channel reuse block confusion
- If you’ve got reuse blocks, channels, or designators in brackets, Altium can decide your PCB component is a “duplicate” and delete one.

**Check:** Project → **Error/Warning panel** after compile for duplicate designators / channel conflicts.

### 4) Unique ID mismatch (the “same refdes but not the same component”)
- Copy/paste, library swaps, or snippet/reuse workflows can create a connector with the same designator but a different **Unique ID**, so ECO treats it as “remove old, add new”.

**Check:** Compare the connector’s Unique ID (SCH vs PCB) if you’re deep in this situation; otherwise, the fix below usually resolves it.

---

## Fastest safe recovery path
### Step A — Find out what ECO is trying to do
1. **Design → Update PCB Document**
2. In the ECO dialog, look for an operation like:
   - *Remove Component J?*
   - *Replace Component…*
   - *Add Component…*
3. **Don’t execute yet.** This tells you whether it’s a “remove” vs “replace” scenario.

### Step B — Make the schematic authoritative again
- Ensure the connector exists in the schematic **in the active variant** and has the **correct footprint**.

Then:
1. Re-compile.
2. Run **Design → Update PCB** again.

### Step C — If it still wants to delete it
You have two good options:

**Option 1 (cleanest): accept ECO, then place it correctly**
- Let it delete/add the “official” connector from schematic.
- Then use **Rooms / placement / move** to put it back where you need.

**Option 2 (surgical): match the PCB component to the schematic component**
- If the PCB one is correct physically, you want the schematic to “become” that one.
- The usual practical way: **relink footprint** and ensure same designator, then update PCB and let it “replace” rather than delete.

---

## Quick sanity checks that catch 80% of these
- Is the connector **inside a reuse block** that you copied in but didn’t properly “instantiate”?
- Is it in a sheet that’s **not included in compile**?
- Did you **rename/annotate** and now there are two of the same designator?
- Is it in a **variant** as “Not Fitted”?

---

If you can tell me what the connector designator is (e.g., J1 / P3), and what the ECO dialog line actually says (remove vs replace vs add), I can tell you the exact minimal-click fix for your case.

[M7] ME (2026-03-03 15:54):
I’ve sorted that’s I just need to reposition it by snapping on those arcs 

[M8] AI (2026-03-03 15:54):
Nice — then you’re in the “place it *exactly* on a circle” game. In Altium the cleanest way is to **use the arc/circle centre as the reference**, then rotate/drag with snapping enabled.

## Best method (exact): move by **reference point** + snap to the arc
1. Turn on the right snaps:
   - Press **Shift+E** (Snap Options)
   - Enable **Snap to Objects**
   - Set a sensible **Snap Grid** (e.g. 0.1mm or 0.05mm while doing this)

2. **Make sure the arcs are real objects** (not just clearance display):
   - If those dashed circles are *clearance boundaries* (rule display), you **can’t snap** to them.
   - If they’re actual **arc primitives** (on a mech layer / keepout / etc.), you *can* snap.

3. Select the connector, then do:
   - **Edit → Move → Move** (or just M, M)
   - Before clicking to place, hit **Space** to rotate as needed.
   - Watch for the snap cues (cursor changes / highlight). Place it so its datum point lands on the arc.

## If you need “snap the connector’s *hole centre* onto the arc”
This is the usual requirement (mounting holes / circular pattern).

1. Select the connector.
2. Press **M, R** (Move → Move Reference) or use right-click **Move → Move Reference** (naming varies)
3. Click the point you want as the “grab point” (e.g., pad/hole centre on the connector).
4. Now move it and **snap that reference point** to the arc.

That avoids the annoyance of Altium grabbing the component origin when you really want pad-centre.

## If those dashed arcs are *not snappable* (very likely)
In your photo they look like **clearance / DRC display**, not actual geometry. If so:

### Create a real snappable circle in 10 seconds
- **Place → Arc → Full Circle** (or Place → Circle) on a **mechanical layer** (or keepout if appropriate).
- Set the exact radius/diameter to match what you need.
- Now you can snap to that circle perfectly and then delete/hide the mech layer later.

## Bonus: making a circular pattern
If you’ve got multiple connectors/features around that circle:
- **Edit → Move → Arrange → Move/Rotate** (or **Tools → Component Placement → Arrange in Circle** depending on version)
- Or copy then **Paste Special** with rotation increments.

If you tell me one thing: are those dashed rings coming from **“Show Clearance Boundaries” / DRC”** or are they actual arcs on a mech layer?  
If you’re not sure, click one: if you can select it as an object, it’s snappable; if not, we’ll do the quick “mech-layer circle” trick.

[M9] ME (2026-03-03 16:21):
Some of this is relevant and some redundant, it’s hard to clean. Want to just delete it all but where does that leave me 

[M10] ME (2026-03-03 16:21):
[image]
[attached file: IMG_7EAB2281-7A2B-41FA-AFE2-906A0EC35DDA.jpeg]

[M11] AI (2026-03-03 16:21):
I get the urge, but if you “delete it all” you’re very likely to delete **real constraints** (keepouts/courtyards/mechanical outlines) along with the visual noise. That can leave you with a board that *looks* clean but is now **unsafe to modify** (parts can overlap, copper can encroach, assembly/mech data gets lost).

From your screenshot there are **three different kinds of “mess”** that often get mixed up:

1) **Ratsnest / connection lines** (thin straight lines everywhere)  
2) **Clearance / courtyard / keepout style rings** (dashed arcs around pads/features)  
3) **Actual drawn primitives** (tracks/arcs/regions on mech layers or keepout layers)

### First: make it *quiet* without deleting anything
Do these in order; each is reversible:

**A) Turn off the ratsnest**
- Press **N** then **S** (Net Connections → Hide)  
  (Or View Configuration → “Connections” / “Ratsnest” off)

**B) Turn off clearance/courtyard-style overlays**
- Open **View Configuration** (press **L**)
- In View Options / PCB View Options, toggle off things like:
  - **Clearance Boundaries**
  - **Component Clearance**
  - **Component Courtyard**
  - **Rooms** (if they’re showing outlines)
  - Any “Display…” options that add dashed halos

**C) Exit any special editing mode**
On your left panel it looks like you’re in a mode like **Hotspot Snap / arc tuning**.
- Hit **Esc** a couple of times to fully exit interactive tools.

This usually gets you from “Christmas tree” to “workable” in 30 seconds **without destroying design intent**.

---

## If you still want to delete: do it surgically
Only delete stuff once you’ve proven it’s *real geometry* (selectable objects), and you know what layer it’s on.

### Step 1 — Identify what it is (critical)
Click one of the dashed arcs and look at the **Properties** panel:
- **Object type** (Arc? Track? Region? Keepout? Room? Component clearance display?)
- **Layer** (Top Overlay? Mechanical 13? Keepout? etc.)
- **Net** (No Net / GND / etc.)

If it’s **not selectable**, it’s just a display overlay → **don’t delete**, just hide the display option.

### Step 2 — If it *is* selectable, delete by layer/type, not by eye
Use the PCB Filter (Panels → PCB Filter), for example:
- Delete only **No Net** primitives on a specific mechanical layer:
  - `IsArc AND OnLayer('Mechanical 13') AND Net = 'No Net'`
- Or only keepout objects:
  - `IsKeepout`

Then you can **Select** → verify → delete.

---

## Where does “delete it all” leave you?
Usually in one (or more) of these states:

- **Assembly/mechanical outputs broken** (courtyards/outlines were on mech layers)
- **Copper can violate spacing** (keepouts removed)
- **Placement can overlap** (component clearance/courtyard intent removed)
- **High-speed behaviour degrades** if you accidentally delete guard/ground structures (polygons/regions)

So: you *can* end up with a board that passes a quick DRC but is no longer mechanically/EMC robust.

---

### The practical compromise I recommend
1) **Hide overlays** first (ratsnest + clearance/courtyard display).  
2) Then delete only:
   - genuinely redundant **No Net** geometry
   - junk on the wrong layer
   - duplicate/mechanical clutter you’ve confirmed is not used for outputs

If you tell me **one thing**—when you click a dashed arc, does it actually select as an object, and what **layer** does Properties show?—I’ll tell you exactly whether it’s “just display” (hide it) or “real geometry” (filter + delete safely).

[M12] ME (2026-03-03 16:24):
[image]
[attached file: IMG_0D0CEE6F-DF94-42E4-B92B-EE57D8FDC00E.jpeg]

[M13] AI (2026-03-03 16:24):
Yep — that screenshot is exactly the “half real, half display” mess that makes people want to nuke it.

Here’s the practical way to get to a **clean, controllable** state without deleting something important.

## What you’re looking at in that image
- The **thick red** shapes are real copper (tracks / fills).
- The **green** bits are likely a different net / layer / selection highlight.
- The **dashed red outlines** are *either*:
  1) **real primitives** (keepouts / courtyard / mech outlines / regions), **or**
  2) **display overlays** (clearance boundaries / component clearance / DRC visualisation).

The difference matters because **(2) can’t be “cleaned” by deleting** — you must turn it off in View Config.

---

## Step 1: Prove whether the dashed stuff is real or just display
Click one dashed outline:
- If it **selects** (vertices show, Properties says Arc/Track/Region/Keepout etc.) → it’s **real geometry**.
- If it **won’t select** → it’s **display overlay**.

Do this once and you’ll know which path you’re on.

---

## Path A — If it’s DISPLAY overlay (most common)
Open **View Configuration** (`L`) and turn off these (names vary slightly by version):

- **Clearance Boundaries**
- **Component Clearance**
- **Courtyard**
- **DRC Violations display / Online DRC markers** (if enabled)
- **Rooms** (if you see room outlines)

Also (if you want it super calm):
- Press **N, S** to hide **connection lines / ratsnest** (those straight “spider” lines).

This gets you a clean canvas **without deleting anything**.

---

## Path B — If it’s REAL geometry (selectable), delete safely
Don’t delete by hand. Delete by **layer + object type**, so you don’t wipe genuine assembly/mechanical intent.

### 1) Identify the layer that contains the junk
When you click a dashed outline, look in **Properties → Layer** (often a Mechanical layer, or Keepout).

### 2) Use PCB Filter to select only that junk
Panels → **PCB Filter**, then use something like:

- If it’s arcs/lines on a mech layer:
  - `((IsArc) OR (IsTrack)) AND OnLayer('Mechanical 13')`
- If it’s keepouts:
  - `IsKeepout`

Click **Select**, visually confirm, then delete.

### 3) Don’t delete these unless you *intend to re-author outputs*
- **Courtyard / Assembly outlines**
- **Board shape / cutouts**
- **Keepouts around connectors or HV areas**
- **Mechanical alignment circles / drill templates**

Those are often exactly the dashed circles people think are “mess”.

---

## If your goal is ONLY “snap the connector to those arcs”
Don’t rely on clearance/DRC visuals. Create a **real snappable construction circle**:

1. Put a circle on a mechanical layer: **Place → Arc → Full Circle**
2. Set it to the exact diameter/radius you want
3. Snap the connector using **Move Reference** (grab pad centre) and snap to that circle
4. Hide that mech layer later

That gives you precision without wrestling with whatever those dashed rings represent.

---

## “If I delete it all, where does that leave me?”
Usually: the board still *routes*, but you’ve lost the **mechanical truth** (assembly data, keepouts, courtyards), and you won’t notice until fabrication/assembly review or the next ECO causes something to overlap. It’s recoverable, but it becomes a rework job.

---

If you do one quick test for me (purely for targeting): **does a dashed ring select as an object?**  
- If *no*: I’ll tell you exactly which View Config toggles to kill it in one go.  
- If *yes*: I’ll give you the exact PCB Filter expression to wipe only the junk layer(s) and keep the important mech intent.

[M14] ME (2026-03-03 17:13):
[image]
How do I back annotate these test point changes 
[attached file: IMG_7B18CC68-06FC-49F2-BC25-65BB8C631413.jpeg]

[M15] AI (2026-03-03 17:13):
Back-annotating “test point changes” depends on **what kind of change you made on the PCB**:

- **Moved/rotated the testpoint footprint only** → that’s a *PCB placement* change (can be pushed back to schematic if the schematic has that footprint/comp and you use the right process).
- **Changed which net the testpoint is on / renamed it / swapped it / added/removed a TP** → that’s *connectivity* (schematic should be the authority; you normally update the schematic first, not back-annotate from PCB).

From your screenshot it looks like **TP designators / testpoint components near pads** (TP26 etc.) and you’re editing on PCB.

### If you changed placement/designators and want SCH to match
Do this:

1. **PCB editor → Design → Update Schematics…**  
   (In some versions: *Design → Import Changes from PCB…* / *Update Schematics*.)
2. In the dialog, enable:
   - **Component parameter changes** (if you edited Comment/Value/parameters)
   - **Component designator changes** (if you renumbered TPs)
   - **Component placements** (if you want X/Y/Rotation pushed back — only relevant if you use those in SCH or Draftsman outputs)
3. **Validate the ECO list** (make sure it’s not trying to do something insane like delete a load of parts).
4. **Execute Changes**.
5. In SCH: **Project → Compile** and check the TP designators and any TP tables.

### If you changed nets / connectivity on the PCB (TP moved to another net)
Don’t back-annotate that. Do this instead:

1. In **schematic**, move the test point symbol connection to the correct net (or update the Net Label).
2. Then: **Design → Update PCB Document** to push that connectivity to the PCB.
3. Repour polygons and run DRC.

Altium will often *let* you create weird connectivity on PCB, but the next ECO can “undo” it if schematic doesn’t agree.

---

## The reliable workflow for Test Points specifically
If you’re using Altium’s testpoint system (rather than hand-placed TP footprints):

1. **Tools → Testpoint Manager**
2. Confirm each TP is:
   - Associated to the correct **net**
   - Has the right **style/footprint**
3. Then use **Design → Update PCB** (or **Update Schematics** depending which direction you’re making authoritative)

If you placed/edited TP footprints manually, you’re outside the manager — still fine, just be consistent about schematic authority.

---

## Quick check: what exactly changed?
Tell me which of these you did, and I’ll give you the exact minimal-click path:

1) “I **moved** TP26/TP25 footprints on PCB”  
2) “I **renumbered** the TPs”  
3) “I **changed which net** a TP is on”  
4) “I **added/removed** test point components”

(You can answer with just the number.)

[M16] ME (2026-03-03 17:14):
Things got misaligned Ina component link.:9 the schematics symbols are dotted around. As the artwork is fixed I want to keep them in place 

[M17] AI (2026-03-03 17:14):
Got it. In Altium terms: **your PCB placement is the truth**, and you want the schematic to stop “spraying” symbols around when you do *Component Links / ECO*, because the **artwork is fixed**.

There are two separate problems to solve:

1) **Stop schematic symbols moving** (keep them where they are)  
2) **Keep PCB placement fixed** while you repair links/IDs

## 1) Prevent schematic symbols being re-positioned
### A. Turn off schematic “re-annotation / re-arrange” behaviour
In the **schematic editor**:
- **DXP / Preferences → Schematic → Graphical Editing**
  - Disable anything like **“Reposition selected components after annotation”** / **“Auto-position…”** (wording varies)
- Also check **Schematic → General** for options that auto-spread parts.

### B. Stop “Update Schematics” from pushing placement changes
When you do **PCB → Design → Update Schematics…**:
- In the ECO/options, **untick** anything related to:
  - **Component positions**
  - **Component rotations**
  - **Component re-annotation**
  - **Room / class driven placement** (if it’s offering it)

You generally only want:
- **Designator / parameter** updates (if needed)
- **Component links / Unique ID fixes**
Not graphical movement.

**Rule of thumb:** If the ECO list contains lines like *“Move Component …”* in schematic — **don’t execute**.

---

## 2) Keep PCB placement fixed while fixing “component links” mess
The “symbols dotted around” usually happens when Altium thinks they’re **new components**, so it adds them at default locations.

That is almost always due to **Unique ID / linking mismatch**, common with:
- reuse blocks / snippets
- copy-paste between projects
- library swaps
- duplicated designators

### The safe fix: re-establish Unique IDs in schematic (without moving anything)
In the **schematic**:
1. **Project → Compile** (fix any duplicate designators first).
2. **Tools → Reset Component Unique IDs**  
   (or *Tools → Annotation → Reset Unique IDs* depending on version)
3. Save.
4. Then do **Design → Update PCB Document** (SCH → PCB direction).

This forces Altium to treat schematic parts as authoritative identities again, so the PCB components link instead of “remove/add”.

> If your PCB is already correct and you just need the link repaired, this is usually the least destructive approach.

---

## 3) If the PCB is fixed: the “do not touch copper/placement” workflow
Use this exact sequence:

1) **Make a backup / new revision** (so you can revert if ECO goes wild).  
2) In SCH: **compile clean** (no duplicates).  
3) **Reset Unique IDs** in SCH.  
4) **Design → Update PCB Document**  
5) In the ECO:
   - ✅ Accept **component link** / **parameter** changes
   - ❌ Reject anything that **adds/removes components**, or **moves PCB tracks/components**
6) Repour, DRC.

If ECO still proposes add/remove, you’ve still got identity mismatch (designator conflicts or variant/unfitted parts).

---

## 4) Fast triage: the one check that tells you what’s wrong
When you run **Design → Update PCB Document**, look at the ECO list:

- If it says **“Remove component X / Add component X”** → Unique ID mismatch / duplicate designators / variant mismatch.
- If it says **“Move component X”** → you’ve enabled a placement sync you don’t want (disable “positions” updates).

---

If you can tell me what you used when you say **“component link”**:
- **Tools → Component Links…** (manual linking panel), or
- **Design → Update PCB Document** (normal ECO),

…and whether ECO is trying to **add/remove** parts or just **move** them, I’ll give you the exact clicks to lock the schematic graphics while repairing the links.

[M18] ME (2026-03-03 20:23):
[image]
It’s worse than I thought and the components are massively jumbled 
[attached file: IMG_9CD1C854-08DD-4F98-92E4-F8E72400752C.jpeg]

[M19] AI (2026-03-03 20:23):
Oof — that screenshot is the classic “library/ID/variant mismatch → ECO thinks half the design is new → it re-adds components and they land in a pile / random spots”. The good news: **you can recover without moving the PCB artwork** if you treat the PCB as authoritative and fix **identity/linking** systematically.

Below is the “don’t make it worse” recovery runbook.

---

## Ground rules (so the artwork stays fixed)
1) **Do not run** any ECO that proposes:
   - *Remove component…*
   - *Add component…*
   - *Swap component…*
   - *Move component… (PCB)*  
2) Make a **copy of the project** first (new folder or VCS branch). You want a hard rollback.

---

## Step 1 — Work out what actually jumbled
There are two very different “jumbles”:

### A) PCB is fine, but you’re *seeing* lots of outlines/courtyards/keepouts
That’s display clutter. Fix via **View Configuration**.

### B) The PCB actually has components duplicated/stacked/mis-linked
That’s an identity/link problem (Unique IDs/designators/variants).

Your screenshot looks like **B**: lots of courtyards/assembly outlines visible and text overlapped, and likely some components have been re-instantiated.

---

## Step 2 — Immediately stop Altium auto-moving/auto-adding on updates
### In PCB update dialogs:
When you do **Design → Update PCB Document**, in the ECO dialog:
- **Untick** any options that include **component placement** changes.
- If it’s proposing adds/removes, **Cancel**.

### In schematic update dialogs:
Avoid **Update Schematics from PCB** until the links are stable.

---

## Step 3 — Fix the *cause*: Unique IDs / duplicate designators / variants
### 3.1 Compile and clear designator issues
In **schematic**:
- **Project → Compile**
- Open **Messages** panel:
  - Fix **Duplicate designators**
  - Fix **Components not fitted / variants** inconsistencies

If duplicates exist, Altium *will* “remove/add” during ECO.

### 3.2 Reset Unique IDs (this is usually the big one)
In **schematic editor**:
- **Tools → Reset Component Unique IDs**  
  (or “Reset All Unique IDs” depending on version)

This forces a coherent identity model again.

> This does **not** have to move symbols. It’s metadata.

### 3.3 Re-link footprints/models if they’re broken
For any component that says “no footprint” or wrong footprint:
- Component Properties → **Models → PCB Footprint**
- Fix those before any ECO.

---

## Step 4 — Re-establish links without changing PCB placement
Now do: **Design → Update PCB Document**

In the ECO list you want to see mostly:
- “Update parameters”
- “Update footprint link” (careful)
- “Update component links”

You do **not** want:
- Add/remove components
- Move components (PCB)
- Any large-scale replace operations

If you still see add/remove, the usual culprits are:
- Same designator used twice (even across channels)
- Variant state mismatch (fitted vs not fitted)
- Components exist in PCB but not in SCH (or vice versa)
- Mixed libraries created “new” instances

---

## Step 5 — If the PCB already has duplicates/stacked parts
This happens when ECO ran earlier and created new components on top of old.

**How to detect quickly**
- Click a messy area and press **Tab** to cycle selections: if you can cycle through multiple “R23” or multiple bodies in same spot, you’ve got duplicates.
- Use **Panels → PCB** and search a designator (e.g., “R23”) — if it shows multiple instances, that confirms.

**What to do**
- Don’t start deleting randomly.
- First make SCH↔PCB identity consistent (Steps 3–4), then:
  - Run **Tools → Component Links** and check if there are “unmatched components”.
  - You can then delete the *unmatched duplicates* (usually the ones with no schematic partner).

---

## Step 6 — Make the view usable (separate from the real fix)
Right now you’ve got too many mechanical layers visible (Top/Bottom Courtyard, Assembly, 3D body, etc).

Press **L** (View Configuration) and temporarily hide:
- **Top Courtyard / Bottom Courtyard**
- **Top Assembly / Bottom Assembly**
- **3D Body**
- Most **Mechanical** layers (leave only what you need)

This doesn’t fix the underlying issue, but it stops your brain melting while you repair links.

---

## The fastest “tell me what to do next” test
Open **Design → Update PCB Document** and look at the first 5–10 ECO entries:

- If you see **Add/Remove/Replace** → identity mismatch still present.
- If you see only **parameter / link updates** → you’re close; execute carefully.

If you paste (or screenshot) the ECO list, I can tell you exactly which entries are safe to execute and which ones will wreck the fixed artwork.

Also: are you using **reuse blocks / multi-channel** in this design? That massively increases the chance of designator/UniqueID collisions, and changes the safest repair path.

[M20] ME (2026-03-03 20:35):
[image]
Why have I now lost my values on resistors 
[attached file: IMG_86E1AA62-7F2C-48DF-959F-97616DDC99DC.jpeg]

[M21] AI (2026-03-03 20:35):
This usually happens for one of three reasons in Altium, and all three are consistent with the “linking/ECO got messy” situation you’ve been in:

## 1) You’re no longer *displaying* the Value parameter
In the schematic editor, resistors normally show the **Comment** string (often set to `=Value`). If that got changed, the value “disappears” even though the parameter still exists.

**Fix (quick check):**
- Click a resistor → **Properties**
- Look at **Comment**:
  - If it’s blank, or something like `R`, you won’t see 10k/1k5 etc.
  - Set it to **`=Value`** (or whatever convention you use, e.g. `=Resistance`).
- Also check the **eye/visibility** next to the Comment/Value parameter.

**Bulk fix:** Schematic → **Tools → Parameter Manager** (or SCH List panel) → set Comment to `=Value` for all resistors.

---

## 2) The “Value” parameter got overwritten/cleared by a library update / ECO
If you updated from libraries (or did an ECO that “Update parameters from library”), Altium can replace component parameters with the library defaults. If the library resistor has no Value set, you end up with blanks.

**Confirm:**
- Click a resistor → Properties → **Parameters**
- Is there a **Value** parameter at all? Is it empty?

**Fix:**
- If values were meant to be per-instance, **don’t push library parameters** over the top.
- Restore by:
  - Undo / revert to a previous revision if possible, or
  - Refill via **Parameter Manager** (if you’ve got a BOM export / earlier values list).

---

## 3) You’re looking at a “compiled/variant” state where values are hidden
If a variant marks parts as **Not Fitted** or swaps them, annotations/values can appear different (or hidden).

**Check:**
- Project → **Variants**: are you in a specific active variant?
- In the schematic sheet: is there any variant/compile indicator?

---

# Fastest path to get them back (do this now)
1. Pick one resistor that “lost” its value.
2. In **Properties** check:
   - **Comment** = `=Value`?
   - **Parameters**: does **Value** exist and is it populated?
3. Based on what you see:
   - **Value exists but not showing** → it’s display/Comment/visibility. Set `=Value` and enable visibility.
   - **Value is empty** → it was overwritten/cleared; you need to restore values (undo, version revert, or refill via manager).

If you tell me what you see for **one resistor** (Comment field + whether Value parameter is present/blank), I’ll give you the exact clicks for the correct branch and a bulk-fix method.

[M22] ME (2026-03-03 20:39):
I will be but not yet this is the base design I need to get straight first 

[M23] AI (2026-03-03 20:39):
Understood — get the **base design** stable first, then variants later. In that case, treat “lost resistor values” as a **symptom of a linking/library sync event**, and fix it at the schematic metadata level (so it stays fixed).

Here’s the clean, base-design-first way to straighten it.

## 1) Decide what the schematic *should* display for passives
In most flows the resistor symbol displays **Comment**, and Comment is set to **`=Value`**. If that got changed globally (or the library part has Comment blank), your values “vanish” even if the Value parameter is still there.

### Quick single-part check (1 minute)
Click one resistor → **Properties**:
- **Comment**: set to `=Value`
- Ensure the little **visibility (eye)** for the comment/value is ON
- In **Parameters**: confirm there is a **Value** parameter and it’s not empty

That tells you whether you’ve got a *display problem* or a *data wiped* problem.

---

## 2) Bulk-fix for the whole schematic (base design)
### A) If values exist but aren’t showing (most likely)
Use **SCH List** or **Parameter Manager** to force Comment format:

- Open **Panels → SCH List**
- Filter/select all resistors (Type = Resistor, or Designator starts with “R”)
- Edit the **Comment** column → set to **`=Value`**
- Ensure **Comment visibility** is enabled

This restores the on-sheet values without touching PCB.

### B) If Value fields are actually blank (worse case)
Then an ECO/library update has cleared the Value parameters. You need to repopulate them.

Best sources:
- Your **last BOM/CSV export**
- A previous commit/zip/backup of the project
- If none: you’ll have to re-enter them, but you can still do it efficiently via SCH List.

---

## 3) Lock the base design so it doesn’t happen again
Once fixed, avoid these until the base is stable:
- “Update from Libraries” that includes **parameters**
- ECO actions that say **Replace component** or **Update parameters from library**
- Any batch library relinking while Unique IDs/designators are still shaky

If you must relink footprints, do it with **models only**, not parameters.

---

## What I need from you (no rabbit holes)
Open **one resistor** and tell me **two fields** from Properties:

1) **Comment** = ?  
2) **Value parameter** = present + filled, or blank/missing?

With just that, I’ll tell you *exactly* which branch you’re on and the fastest bulk fix for the whole base design.

[M24] ME (2026-03-03 20:40):
[image]
[image]
I’m back to this 
[attached file: IMG_2EBF63F9-5C74-4FEE-ABEE-4FA7EFD58FB8.jpeg]
[attached file: IMG_50612BF8-9411-4185-A7B0-9431C37177A0.jpeg]

[M25] AI (2026-03-03 20:40):
Good — **this state is recoverable**. What I’m seeing now is mostly **visual overload** (lots of mech/courtyard/assembly layers enabled) plus the normal copper. It doesn’t look like the “everything duplicated in a pile” disaster state.

So your next move is: **stabilise the base design by locking down link integrity**, and **make the view sane** so you can work.

---

## 1) Make it readable again (no risk, 30 seconds)
Press **L** (View Configuration) and temporarily **turn OFF**:
- **Top Courtyard / Bottom Courtyard**
- **Top Assembly / Bottom Assembly**
- **3D Body** layers
- Most **Mechanical** layers (leave only the one(s) you actually use for outline/keepouts)
- If you don’t need them right now: **Top/Bottom Paste** too

Leave ON:
- Top/Bottom copper as needed
- Top/Bottom overlay
- Keepout (only if you’re actively placing)

This will instantly remove 80% of the clutter you’re currently seeing.

---

## 2) “Back to this” means: do NOT run any ECO that moves/adds/removes parts
From here, your base-design objective is:

✅ **PCB placement stays fixed**  
✅ **Schematic links match** (no add/remove)  
✅ **Parameters/values stable**

So: **no more Component Links panel tinkering** unless you’re only inspecting.

---

## 3) The correct “base design stabilisation” sequence
Do this exact order:

### Step A — In SCH: compile clean
- **Project → Compile**
- Open **Messages**
- Fix anything like:
  - duplicate designators
  - components with no footprint
  - variant/fitted mismatches (even if you “aren’t using variants yet”, make sure you’re on the base/default variant)

### Step B — Reset Unique IDs in SCH (metadata only, doesn’t move symbols)
- Schematic editor: **Tools → Reset Component Unique IDs** (Reset All)
- Save all

### Step C — Push SCH → PCB but only accept *safe* ECO items
- **Design → Update PCB Document**
- In the ECO list:
  - ✅ allow: parameter updates, link updates
  - ❌ reject/cancel if you see: **Add**, **Remove**, **Swap**, **Move component** (PCB)

If it still proposes Add/Remove, stop: that means identity mismatch remains (usually duplicates, variants, or inconsistent footprints).

---

## 4) If you still have “lost values” risk
Once link integrity is stable, bulk-restore resistor display:
- SCH List / Parameter Manager:
  - set **Comment** to `=Value`
  - ensure **Value parameter** exists and visible

But do this *after* the ID/link work, otherwise the next library sync can wipe it again.

---

## One fast diagnostic that will tell me your next action
Open **Design → Update PCB Document** and look at the first few ECO lines:

- If you see **only** “Update Parameters / Update Component Links” → you’re safe to execute.
- If you see **Add/Remove/Replace** → don’t execute; we need to fix the mismatch first.

If you can screenshot just that ECO list, I’ll tell you exactly which entries are safe to run and which ones will re-break the artwork.

[M26] ME (2026-03-03 20:41):
[image]
Those greens are violations where the ring c on plenty id
[attached file: IMG_9C0573C8-BB53-4811-9B28-6C74C2918CE5.jpeg]

[M27] ME (2026-03-03 20:41):
No it’s because the wrong component is there

[M28] AI (2026-03-03 20:41):
Ah — that’s actually *good news*, because it means you’re not fighting clearances/polygons; you’re fighting **identity**: the PCB has a footprint instance that Altium thinks is a different component (wrong library item / wrong footprint / wrong pin mapping), so the connectivity/DRC goes nuts and you see those green “markers”.

### What those greens usually mean in this situation
When the **wrong component/footprint** is placed, Altium will happily connect nets to pads that **don’t match the schematic pin designations**, so you get:
- **Un-routed / wrong-net** connections
- **Shorts** (pads tied together that shouldn’t be)
- **Clearance violations** because copper is now “legal” to approach the *wrong* pad/net

So the fix is: **make the PCB component match the schematic component**, without moving your fixed artwork.

---

## Minimal-risk fix: correct the footprint/model from the schematic, then ECO
### Step 1 — Identify the culprit component
In PCB:
1. Click one of the pads that has the green markers.
2. Look at **Properties**:
   - Which **Component** is it (designator)?
   - Which **Footprint name** is currently used?
   - Which **net** does the pad think it’s on?

Write down the designator (e.g. R22 / TP14 / etc.).

### Step 2 — In schematic, confirm what it *should* be
Find that same designator in SCH:
- Check the **Library reference / component type**
- Check **Models → PCB Footprint** (what footprint should be)

### Step 3 — Force the correct footprint onto the PCB via ECO (don’t hand-swap on PCB)
Do:
- **Design → Update PCB Document**
In the ECO list, you want an item like:
- **Change/Update Footprint** for that designator

✅ Accept that  
❌ Reject anything that adds/removes/moves lots of other components

Execute, then:
- **Repour polygons**
- Run DRC again

---

## If ECO wants to *remove/add* the component instead of “change footprint”
That means Altium thinks it’s a different identity (Unique ID mismatch), not just a wrong footprint.

Then do this sequence:

1. In **SCH**: **Tools → Reset Component Unique IDs** (for the project)
2. Compile.
3. **Design → Update PCB Document** again.

This often converts “remove/add” into a clean “relink/update footprint”.

---

## If you must swap the component on PCB (last resort)
Only if you cannot get a clean ECO footprint update:
- Right-click the component → **Component Actions → Replace Component**  
  Choose the correct footprint model instance.

But this is riskier because it can create more linking divergence if the schematic still disagrees.

---

## Quick sanity check you can do immediately
Click the “wrong” component and press **Ctrl+H** (Highlight Net) on one pad:
- If the highlighted net is clearly not what the schematic expects (e.g., “REM_ADD_CLK” showing on a pad that should be GND), you’ve confirmed it’s a **footprint/pin mapping mismatch**.

---

If you tell me the **designator** of the wrong part (the one near TP14 / R22 in your screenshot), I’ll tell you the *exact* safest path (footprint update vs replace vs relink) and what to allow/deny in the ECO so you don’t disturb the fixed layout.

[M29] ME (2026-03-03 20:42):
No, the wrong resistors have replaced originals and now it violates 

[M30] AI (2026-03-03 20:42):
Yep — that’s the smoking gun: **a library update / ECO swap replaced resistor instances**, so the PCB now has the *wrong footprint or wrong pad geometry* (or even wrong component class/rules), and you’re seeing DRC violations as a consequence.

What you want is **to get the original resistor footprints/instances back** without moving anything else.

Here’s the safest way to do it.

---

## 1) Confirm what “wrong” means (usually one of these)
On one offending resistor in the PCB, open **Properties** and check:

- **Footprint name** (e.g., `R_0603`, `R_0805`, `R_1206`, etc.)
- **Pad sizes / solder mask expansion** (visibly different)
- **Rule class / component class** (can change clearances)
- **Design Item ID / Library link** (if it changed to a generic resistor template)

Most often it’s simply: **0603 got replaced by 0805**, or a different land pattern with bigger mask/paste.

---

## 2) Recover by making SCH authoritative for footprints (not values)
### Step A — In schematic, set the correct footprint model for the resistor(s)
Pick one designator that’s wrong (say R22):
- SCH: open R22 → **Models → PCB Footprint**
- Set it to the correct original footprint

If many resistors are wrong, do it in bulk:
- **SCH List / Parameter Manager**
- Filter designators `R*`
- Set the footprint model field appropriately (or by subset if some are 0603 and some 0805)

### Step B — Push SCH → PCB and only accept footprint changes
- **Design → Update PCB Document**
In ECO, accept only items like:
- **Change footprint** / **Update footprint model**

Reject anything that:
- Adds/removes components
- Re-annotates designators
- Moves components on PCB

Execute.

This should “snap” the footprints back while keeping placement.

---

## 3) If ECO tries to “remove resistor / add resistor” instead of “change footprint”
That means the swap broke **Unique IDs** and Altium thinks they’re different components.

Fix that first:
1. SCH: **Tools → Reset Component Unique IDs**
2. **Project → Compile**
3. Then **Design → Update PCB Document** again

Often that converts remove/add into clean relink/footprint updates.

---

## 4) If you need a quick way to find all swapped resistors on PCB
- Panels → **PCB**
- Filter by footprint (e.g., show all `R_0805` and see if any shouldn’t be)
- Or sort by **Component Kind / Library Reference / Footprint**

Then you can correct in batches.

---

## 5) Prevent it happening again (once recovered)
Avoid “Update from Libraries” with parameter/model overwrite until stable.
If you must update libraries:
- update **symbols** only, or
- update **models** only (and never “replace existing parameters/models” blindly)

---

### One very targeted question (so I can give you the exact click path)
Were the originals **0603 vs 0805** (footprint size change), or did the **pad numbering/pin mapping** change too?

If you don’t want to check: tell me just **one resistor designator** that is wrong and what footprint it currently shows in PCB Properties, and I’ll tell you the quickest bulk fix path for the whole set.

[M31] ME (2026-03-03 20:44):
Foot prints are correct it’s the designators. I had to manually link and it got messy

[M32] AI (2026-03-03 20:44):
Got it. If the **footprints are correct** and what’s wrong is **which resistor designator is sitting on which footprint/location**, then you’ve effectively got a **scrambled SCH↔PCB component mapping** (Unique IDs / component links), not a footprint problem.

The goal now is: **rebuild the component links so each PCB part at a fixed location is linked to the correct schematic designator**, without moving the PCB.

### Critical principle
**Do not try to “fix” this by re-annotating.**  
You need to **re-link identities** (Unique IDs / component links). Re-annotation will just rename the mess.

---

## The clean recovery path (PCB is authoritative for placement)
### 0) Safety
- Save a copy / new commit first.
- Turn OFF any “Update parameters from libraries” stuff.

### 1) Stop Altium from “helping” (so it won’t move/add parts)
When doing any ECO:
- If you see **Add/Remove/Move components** → **Cancel**.

### 2) Reset schematic Unique IDs (so it’s linkable again)
In **schematic editor**:
- **Tools → Reset Component Unique IDs** (reset all)
- **Project → Compile** (must compile clean—no duplicate designators)

This doesn’t move symbols; it just gives you a consistent identity set.

### 3) Now rebuild the links using **Component Links**
In the **PCB editor**:
- **Project → Component Links…** (or **Design → Component Links…** depending on version)

You’ll see two lists:
- **Schematic Components**
- **PCB Components**
and a mapping table.

#### Best way to relink when designators are scrambled
Use **cross-probing by selection**, not by scrolling lists:

1. In PCB, click the physical resistor at the correct location.
2. In the Component Links dialog, use **Select in PCB / Locate** (or it auto-highlights that PCB entry).
3. In schematic, find the *intended* resistor (by circuit context), click it.
4. In Component Links, pick that schematic component and **Link** it to the selected PCB component.
5. Repeat for the subset that’s wrong.

**Key trick:** Work block-by-block (e.g., do the whole R22–R29 cluster) rather than random single fixes.

### 4) Validate before committing links
In the Component Links window:
- Use **Check / Validate** (or equivalent)
- Ensure each designator maps **1:1** (no duplicates, no unlinked)

Then **Apply / OK**.

### 5) Push link repair through ECO (but only link changes)
- Run **Design → Update PCB Document**
- Accept only **Component link** / **Unique ID** type updates
- Reject anything about placement or add/remove

---

## Fast way to detect what’s scrambled
Pick one wrong-looking resistor on the PCB and:
- Use **Cross Probe** to schematic
  - If it jumps to the wrong resistor symbol, that confirms link scramble.
- Do this for 3–4 resistors: if the mapping is consistently “shifted”, you can repair a whole bank quickly.

---

## If the scramble is widespread: the “nuclear but controlled” option
If manual linking touched a lot of parts and it’s too messy, sometimes it’s faster to:
1) **Remove all component links**
2) Rebuild them cleanly by rule (designator matching + Unique IDs)

But I only recommend that if:
- the schematic designators are correct and stable, and
- the PCB has the correct physical parts placed, and
- you can afford a relink pass.

(We can do this, but it’s easy to make worse if duplicates exist.)

---

## The one thing I need to choose the exact method
In **Component Links**, do the lists show:
- mostly **matched-by-designator** but “some wrong”, **or**
- **lots of “unmatched” / duplicates / many-to-one**?

If it’s “some wrong”, you repair locally (best).  
If it’s “lots unmatched”, you likely need a full relink strategy.

If you can screenshot the **Component Links dialog** (just the mapping table area), I’ll tell you the fastest safe relink plan and what *not* to press.

[M33] ME (2026-03-03 20:55):
As a side note, what was the dual lvds receiver in mssop pack 

[M34] AI (2026-03-03 20:55):
The one I had in mind is **TI / National DS90LV027A** — it’s a **dual LVDS line receiver** and it’s available in an **8-pin MSOP** package (as well as SOIC).  

A couple of other “close” parts people sometimes mean (package varies by ordering code):
- **TI SN65LVDS2** (also a dual LVDS receiver family member; often seen in small-outline variants like VSSOP/MSOP depending on suffix)

If you tell me whether you need **3.3 V only** or **1.8–3.3 V**, and whether you need **failsafe / open-circuit fail-safe**, I can point you to the most appropriate exact ordering code.

[M35] ME (2026-03-03 21:05):
It’s a receiver 

[M36] AI (2026-03-03 21:06):
If what you want is a **dual LVDS line receiver in a really small 8-pin package**, the part that fits that mental slot is:

- **TI DS90LV028A** — **dual LVDS receiver** (packages are **SOIC-8** and **WSON-8**, not MSOP). citeturn1search0

If you *specifically* meant the tiny “MSOP-ish” footprint but were really thinking of **SOT-23-8**, then:

- **Maxim (Analog Devices) MAX9113** — **dual LVDS receiver**, available in **8-pin SOT-23** (also SO-8). citeturn4view0

Small correction to my earlier note: **DS90LV027A** is the **dual driver** companion; the **dual receiver** is **DS90LV028A**. citeturn0search0turn1search0

If you tell me your supply (3.3 V only vs 1.8–3.3 V) and whether you want **internal 100 Ω termination**, I’ll point you at the best exact device/variant.

[M37] ME (2026-03-03 21:06):
What about single receiver then 

[M38] AI (2026-03-03 21:06):
For a **single-channel LVDS receiver**, the two small-package “usual suspects” are:

- **Analog Devices / Maxim MAX9111** — **single LVDS receiver** (the MAX9113 is the dual). citeturn0search0turn0search2  
- **TI DS90LT012AH** — **single LVDS differential line receiver** in a **5-pin SOT-23** (also notable because TI positions it as a high-temperature option). citeturn0search6

If you tell me your **supply voltage** (1.8/2.5/3.3 V) and whether you want **failsafe/term**, I’ll point you at the best-fit exact part + package variant.

[M39] ME (2026-03-03 21:07):
What about an lvds 1:2

[M40] AI (2026-03-03 21:07):
An “LVDS 1:2” usually means **one differential LVDS input replicated to two differential LVDS outputs** (fanout). There are a few solid ways to do it, depending on whether it’s **clock** or **data**:

### Clock-style 1:2 fanout (clean, low skew/jitter)
- **TI CDCLVD2102** — explicitly a **dual 1:2 LVDS fanout clock buffer** (2 inputs → 4 LVDS outputs = two independent 1:2 banks). citeturn3search1  
- **TI LMK1D210x family** — clock distribution buffers; includes **dual 1:2 differential buffer** variants depending on the exact part. citeturn3search3turn1search0  

### Data/logic fanout or “buffer with features”
- **TI DS15MB200** — a **2:1 / 1:2 LVDS mux/buffer** (use it in 1:2 mode), with pre-emphasis aimed at higher-speed links. citeturn3search2  

### If you mean “I just want to split an LVDS pair”
You *can* sometimes do a passive split for short runs, but it’s a signal-integrity gamble (loading, termination, stubs). The proper way is a **true fanout/buffer** like the above.

If you tell me **speed (~Mbps or MHz)** and whether it’s **clock or data**, I’ll point you to the best fit (and the package options) from those families.

[M41] ME (2026-03-04 00:15):
Why aren’t these diodes pulling through? They in the library added

[M42] ME (2026-03-04 00:15):
[image]
So what do I do when I have this connection I’ve corrected but still says violate. Is there a reconnect button?
[attached file: IMG_EB09C838-F2D0-471D-8C3C-B302BD78EED5.jpeg]

[M43] AI (2026-03-04 00:15):
You’ve got two different issues tangled together here:

1) **“Diodes not pulling through”** (SCH→PCB sync / libraries / ECO)  
2) **“I fixed the connection but it still shows a violation”** (DRC not updated, stale objects, wrong-net copper, or polygons not repoured)

I’ll hit (2) first because your screenshot is clearly showing a **constraint violation** banner.

---

# A) “I corrected the connection but it still violates” — what to do
There isn’t a single “reconnect” button, but there *is* a reliable reset sequence:

## 1) Repour polygons (very often the cause)
Your status text shows a lot of “Polygon Shelved…” and you’re working around copper/pours.

Do:
- **Tools → Polygon Pours → Repour All**  
  (or right-click on board → Polygon Actions → Repour All)

Then re-run DRC markers.

## 2) Re-run DRC / clear stale markers
If you’re using **Online DRC**, markers can persist until the engine re-evaluates.

Do one of these:
- **Tools → Design Rule Check… → Run DRC**
- Or if you just want to refresh markers: **Tools → Reset Error Markers** (wording varies; sometimes in the DRC panel)

## 3) Confirm the copper is actually on the correct net
This is the big one when things have been “messy linking”.

- Click the **track/pad** that you believe you fixed  
- Look in **Properties → Net**
- If it says something like `NetC...` or **No Net** when you expected `+3V3D` (etc.), then the “fix” is visually correct but **net ownership** is wrong.

### Fix wrong-net track quickly
- Select the offending track/region → in **Properties**, set **Net** to the correct net (if allowed), or
- Delete and **re-route** from pad to pad so it inherits the correct net.

## 4) If the violation is “Collision” between pad and track
Your on-screen text shows **Collision <10mil between Pad on TopLayer and Track on TopLayer**.
That means your clearance rule still sees them as different nets (or a keepout).

So check:
- Is the **pad net** correct?
- Is the **track net** correct?
- Is there a **keepout / polygon cutout / room rule** there?

If both nets match and it still says collision, 99% it’s either:
- You’re looking at a **different layer object** (e.g., a region/track underneath),
- Or it’s a **polygon cutout/region** causing the marker (your footer shows “Polygon Pour Cutout …”).

### Quick check for hidden/overlapping junk
- Click where the marker is and press **Tab** to cycle through objects under the cursor.
- If it selects a **Region / Polygon Cutout**, that’s your real offender.

---

# B) “Diodes aren’t pulling through” — why and the quickest check
If a diode is “in the library” but won’t appear on the PCB after ECO, common causes:

1) **No PCB footprint model attached** on the schematic symbol  
   - SCH component → Properties → **Models** → must have a **PCB Footprint**
2) **Variant says Not Fitted**
3) **Duplicate designator / Unique ID mismatch** (Altium refuses to instantiate cleanly)
4) You added the part to the library but didn’t **place it in the schematic** (library presence alone doesn’t pull it through)

Fast test:
- In SCH, click the diode → does it show a valid **PCB footprint** in Models?
- Then **Design → Update PCB Document** and see if ECO includes “Add component Dxx”.

---

# Do this exact “reset” sequence right now for your current violation
1) **Tools → Polygon Pours → Repour All**  
2) **Run DRC** (or reset markers)  
3) Click the **track** and **pad** involved → confirm **both are on the same Net**  
4) If still flagged: **Tab-cycle** at the marker and delete/adjust the *actual* offending object (often a region/cutout)

If you tell me what the violation text says in full (it’s partially visible in your overlay: “Collision <10mil between pad… and track…”), and what **Net** the pad/track show in Properties, I can tell you the single most direct fix (net reassignment vs delete/reroute vs remove cutout).

[M44] ME (2026-03-04 01:50):
[image]
Why is my connector not showing the nets ?
[attached file: IMG_F5755067-54E7-43B7-9A96-6B0F1D1BF49F.jpeg]

[M45] AI (2026-03-04 01:50):
If a connector’s pads aren’t “showing the nets” in Altium, it’s almost always one of these (and the fix is quick once you know which):

## 1) The pads are actually **No Net**
This happens when the PCB footprint pads aren’t mapped to the schematic pins correctly (or the component link/Unique IDs got scrambled, which you’ve been dealing with).

**Check**
- Click one pad → **Properties → Net**  
  - If it says **No Net**, the PCB doesn’t think it’s connected to any net.

**Fix**
- Go to schematic and ensure that connector symbol pins are actually wired/net-labelled.
- Then **Design → Update PCB Document** (SCH→PCB).
- If it still stays No Net: it’s a **pin mapping / component link** issue (see #3).

---

## 2) Net names are present but you’re not **displaying** them
Altium can hide net names on pads/vias unless the right display option is on.

**Fix (display)**
- Press **L** (View Configuration)
- Turn on **Net Names** (and/or “Net Labels”), and ensure your **Single Layer Mode** isn’t hiding overlays.
- Also make sure you’re looking at **Top Layer/Overlay** appropriately.

(You can also toggle net name display from the **View Options** / PCB View Options area.)

---

## 3) Pin mapping mismatch: connector is linked, but **pins don’t correspond**
If your schematic connector symbol pin numbers don’t match the footprint pad numbers, then even with a link, pads can stay No Net.

**Check**
- In schematic: open connector → confirm pin numbers (1…N)
- In PCB footprint: open footprint → confirm pad designators match (1…N)

**Fix**
- Correct pin numbering or footprint pad numbers, then update PCB.

---

## 4) You’re looking at a “special object” that doesn’t carry nets (less common)
e.g., mechanical mounting holes inside the connector footprint, shield pads, or tooling holes can be intentionally **No Net**.

**Check**
- If only the big shell pads are No Net but signal pins have nets, that’s normal.

---

## The fastest diagnosis
Click one of the connector’s signal pads and tell me what it says in **Properties → Net**:
- **No Net** → linkage/pin mapping/update problem (#1/#3)
- Shows a net but not visible on screen → display setting (#2)

If you can also tell me whether the **ratsnest** lines go to the connector pins, I can pinpoint it in one step.

[M46] ME (2026-03-04 09:03):
Why has the connector turned green when in the design whereas it’s black as it should be in library 

[M47] ME (2026-03-04 09:03):
[image]
[attached file: IMG_CD262700-FAC4-426E-9E38-788B553E57B0.jpeg]

[M48] AI (2026-03-04 09:03):
Nothing is actually “wrong” with the connector. What you’re seeing is just **Altium’s 3D colour mapping**, not the model changing.

In **3D view**, Altium colours bodies depending on what they are:

- **Copper / board** → green (board material)
- **3D body primitives or STEP models without material** → often shown **green / translucent green**
- **3D models with material definitions** → appear **black / realistic**

So the reason it looks **black in the library but green in the PCB** is usually one of these:

### 1. The PCB is not using the STEP model material
If the STEP model doesn’t contain colour/material info, Altium assigns a default **green component body**.

**Check:**
Select the connector → **Properties → 3D Body**

Look at:
- **Model Type**: STEP / Generic
- **Use component color / material**

### 2. “Component color override” is enabled in the PCB view
Sometimes Altium forces a colour for all component bodies.

Press **L → View Configuration → 3D Settings**

Look for:
- **Component body color**
- **Use model color**

Make sure **Use model color** is enabled.

### 3. The library uses a STEP with colour but the PCB is using a **different 3D body**
If the footprint in the PCB library has a simple **extruded body**, it will render green.  
The library preview may have the **STEP attached**, but the PCB footprint instance might not.

Check:
```
Footprint → Properties → 3D Body
```
and confirm the **STEP file is actually attached**.

---

### Quick test
Select the connector and **press 3 → 2 → 3** (toggle 3D view refresh).  
If it stays green, it’s just the model colour override.

---

### Important reassurance
This **does not affect manufacturing, placement, or exports**.  
It’s purely a **3D viewer rendering preference**.

---

If you want, I can also show you a **really useful Altium trick for connector STEP models** that makes them render perfectly and align automatically with the footprint (saves hours of manual alignment).

[M49] ME (2026-03-04 09:04):
[image]
Ok off board 
[attached file: IMG_C64D3580-451F-4161-A6F6-E65E44087362.jpeg]

[M50] AI (2026-03-04 09:04):
Yep — that’s simply the **3D body offset/rotation** (or a footprint origin mismatch). The PCB is using the STEP/3D body, but its **XYZ placement relative to the pads** is wrong, so it’s floating “off board”.

### Fastest fix (in the PCB footprint library, not in the PCB)
Do this in the **.PcbLib** so every instance is correct:

1. Open the **footprint** in the **PCB Library** (PcbLib).
2. Click the **3D Body** (the STEP model).
3. In **Properties → 3D Body** adjust:
   - **Standoff Height (Z)** → usually set this to **0** first.
   - **X / Y offset** → nudge until it sits over the pads.
   - **Rotation** if needed (90/180/270).
4. Use **View → 3D Layout Mode** inside the footprint editor to visually align.
5. Save the PcbLib.
6. Back in the PCB: **Design → Update PCB** (or right-click component → **Update from Libraries**) so the updated 3D body comes through.

### Two gotchas that cause this exact “off board” look
- The STEP model was made with its origin nowhere near the pins (common).
- The footprint’s **component origin** is not at the mechanical datum the STEP expects.

### Best-practice alignment trick (makes it painless)
In the footprint:
- Place the 3D body, then set its **Reference Point** to a known pad (e.g., pin 1 centre) using “Move 3D Body” with snap (if available), then only small offset tweaks are needed.

### If you only need it “visually ok” for this one board (not ideal)
You *can* fix it at board level:
- Select component → in Properties find **3D Body** entry → edit its offset
…but it won’t propagate and will bite you later.

If you tell me whether this connector is **TH** or **SMT** and whether the model should sit **flush** or with a small **standoff**, I’ll tell you what Z should roughly be (usually 0 for SMT, a couple mm for through-hole housings depending on the datasheet).

[M51] ME (2026-03-04 09:11):
Why can I select multiple designators anymore?

[M52] AI (2026-03-04 09:11):
This is almost always one of these “modes” problems in Altium — something is forcing **single-selection** or you’re in a tool that captures clicks.

## 1) You’re in an interactive command (most common)
If you’re in **Move / Route / Measure / Hotspot Snap / Polygon edit / 3D body edit**, Altium won’t let you multi-select normally.

**Fix:** hit **Esc** 2–3 times until the status bar stops mentioning a command.

---

## 2) “Single Layer Mode” or a selection filter is restricting what you can grab
If you’ve accidentally enabled filtering, multi-selection feels “broken”.

### A) Clear selection filters
- Open **Panels → PCB Filter** (or Properties/PCB panel depending on your layout)
- Make sure there isn’t a filter expression active.
- Click **Clear**.

### B) Check Selection Filter panel
- **Panels → Selection Filter**
- Ensure “Designators” (and the relevant object types) are allowed.

---

## 3) You’re trying to select **designator strings inside components**
There are two different things:
- Selecting **components** (easy, multi-select works)
- Selecting **just the designator text** (can be restricted if designators are “part of component” selection)

**Workaround that always works:**
- Select the **components** instead (box select or shift-click components)
- Then edit designators in bulk via **Properties** / **PCB Inspector**.

---

## 4) You’re in 3D mode
Multi-selecting text/designators is flaky in 3D.

**Fix:** press **2** (2D mode) and try again.

---

## Quick “get me unstuck” sequence (do this in order)
1. Press **Esc, Esc**
2. Press **2** (back to 2D)
3. Press **Shift+C** (clear current selection)
4. Open **Panels → PCB Filter** → **Clear**
5. Try **Shift-click** multiple items or **click-drag** a selection box.

If it still won’t: tell me whether you mean **schematic** or **PCB**, and whether you’re trying to select **component designators (text)** or the **components themselves**.

[M53] ME (2026-03-04 09:14):
How do I come out of remote pc mode easily?

[M54] AI (2026-03-04 09:14):
Depends what you’re using to remote in, but here are the fastest “muscle-memory” exits for the common ones:

### Windows Remote Desktop (mstsc)
- **Ctrl + Alt + End** → sends Ctrl+Alt+Del to the remote PC (then you can sign out / lock etc.)
- To get out of full screen: **Ctrl + Alt + Break** (on some keyboards it’s **Pause/Break**)
- Or hover top of screen → click the **pin/restore** button on the RDP bar

### TeamViewer
- **Ctrl + Alt + Del** via the toolbar
- Close the session: **X** on the top TeamViewer bar (or “Connection → Disconnect”)

### AnyDesk
- Move mouse to reveal top bar → **Disconnect**
- Or **Ctrl + Alt + Shift** (toggles some modes; varies with settings)

### Chrome Remote Desktop
- Open the side panel → **Stop sharing / Disconnect**
- Fullscreen toggle is in the CRD toolbar

### Quick universal fallback
- **Alt + Tab** (switch to the remote client window)
- Then **Alt + F4** (close it) *if you just want to drop the session*

If you tell me which app you’re using (RDP/TeamViewer/AnyDesk/Chrome, etc.) and whether you’re stuck in **full screen**, I’ll give you the exact single shortcut for that setup.

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] AI (2026-03-03 16:21):
I get the urge — but in Altium “delete it all

[A2] AI (2026-03-03 20:41):
Yep — that green “pepper” pattern (little green circles/crosses all over pads/tracks) is **Altium’s DRC violation markers**. It’s not copper, it’s the online/offline DRC overlay shouting “something is breaking a rule here”.

In your screenshot it’s very likely one (or more) of these:

## What the green markers usually mean in this situation
### 1) **Solder mask / paste violations** (most common when you see it all over pads)
- Mask expansion too small/negative
- Mask slivers below minimum
- Paste mask overlap / paste sliver
- Courtyard/assembly not relevant, but *mask* rules are.

### 2) **Clearance violations caused by pours / plane connection style**
- Your “ring” around the pad/testpoint might be a polygon/region/plane necking in too close.
- If you changed polygon priorities / re-poured, you can suddenly create lots of tiny clearance fails around pads.

### 3) **Unrouted net / net tie / short markers** (less likely from the look, but possible)
- If the “ring” is on the wrong net or there’s a tiny overlap, you’ll get loads of markers.

---

## First do this: identify *exactly* what rule is being violated
1. In PCB, open **Panels → PCB Rules and Violations** (or “Messages” depending on your setup).
2. Click one of the green markers (or a pad with the markers).
3. The panel will tell you the violation type, e.g.:
   - *Clearance Constraint*
   - *Solder Mask Expansion*
   - *Minimum Solder Mask Sliver*
   - *Paste Mask Expansion*
   - *Short-Circuit*
   - *Un-Routed Net*

That single step changes this from guesswork to a 2-minute fix.

---

## If you just need to stop the screen going green (without fixing yet)
- Press **L** → View Configuration
- Turn off:
  - **Violations**
  - **Online DRC**
  - (optionally) **Clearance Boundaries**

This only hides it — it doesn’t resolve it — but it makes the board usable while you’re cleaning base design.

---

## The likely “ring on pad/test point” cause + fix
Because you mentioned “ring … on pad / testpoint id”, I’m guessing you’ve got a **round keepout / region / polygon cutout** around a testpoint or via and it’s violating either clearance or mask rules.

### Typical fix patterns
- If it’s a **clearance violation**:
  - Increase the ring diameter / cutout diameter
  - Or adjust polygon pour priority so the correct copper wins
  - Or edit the specific **Clearance Constraint** for that net/class (careful!)

- If it’s a **solder mask sliver**:

