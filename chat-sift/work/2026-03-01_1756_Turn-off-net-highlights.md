# Turn off net highlights
Date (UTC): 2026-03-01 17:56
Conversation ID: 69a47dd0-e604-8386-b8d9-1f3313b2488a
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-01 17:56):
How do I turn off bet highlights in altium 

[M2] AI (2026-03-01 17:56):
In Altium, the “net highlights” are almost always one of these modes. Try them in this order (fastest first):

### 1) Clear the active highlight
- Press **Shift + C** (Clear Filter / Clear Highlight)
- Or click in empty space and press **Esc** a couple of times

### 2) If you used “highlight net” (the thick coloured overlay)
- Press **Shift + H** (toggle **Highlight Net** off)
- Or go **View → Highlight Net** and disable it

### 3) If it’s actually a filter (everything else is dimmed)
- Open **Panels → Filter**  
- Click **Clear** (or **Reset**), and make sure **Enable Filter** is off  
- Also press **Shift + C** again afterwards (it clears a surprising amount)

### 4) If it’s cross-probing / selection highlight from schematic
- In PCB: **Tools → Cross Select Mode** → turn it off (or set to a less aggressive mode)
- Also check **Panels → PCB** / **Properties**: if you’ve got a “Mask” or selection filter applied, clear it

If you tell me what it looks like (e.g., *single net goes neon*, or *everything else goes dark*, or *rats nest highlights*), I’ll point you to the exact toggle for that specific highlight mode.

[M3] ME (2026-03-01 17:57):
[image]
I’m trying to change colours of wires but it keeps presenting this 
[attached file: IMG_16045C2D-F470-41AC-B28E-F812899B3C52.jpeg]

[M4] AI (2026-03-01 17:57):
That pop-up is Altium telling you: **you’re trying to assign Net Colours, but “Show Net Color Override” is currently OFF**, so you wouldn’t see the result.

### If your goal is to *see* the wire colours you’re assigning
Click **Yes** on that dialog (it simply turns the display on).

Then, to make it “stick” (and stop nagging):

1. Press **L** (View Configuration)
2. Go to **Schematic → Net Color Override**
3. Tick **Show Net Color Override** (wording may be *Show net colour override*)

Now any net colour you set will actually show on the wires.

---

### How to actually set the wire/net colour (schematic)
Pick whichever matches how you’re working:

**A) Per net (recommended)**
1. Click the **wire/net** (or its **net label**)
2. Open **Properties** panel
3. Find **Net / Net Color / Color Override** (name varies slightly by version)
4. Choose the colour

**B) Using the panel**
1. Open **Panels → SCH → Nets** (or just **SCH** panel)
2. Select the net from the list
3. Set its colour / override there

---

### If you *don’t* want net-colour overrides at all (turn off)
- Press **L** → **Schematic → Net Color Override** → untick **Show…**
- Or just press **Shift+C** to clear highlighting/filtering if you were only “highlighting” nets.

---

If you tell me: are you in **schematic editor** (SchDoc) or **PCB editor** (PcbDoc) when doing it, and are you trying to colour **all wires of a named net** or just a *single segment*, I’ll point you to the exact control (Altium treats those differently).

[M5] ME (2026-03-01 17:58):
I’m just trying to change the wires colours after an import. Nothing g to do with highlights 

[M6] AI (2026-03-01 17:58):
Got you — this **isn’t “highlight” mode**. It’s Altium’s **Net Color Override** system: wire colours are driven by the **net**, not by the individual wire segments (unless you literally draw graphic lines, which you don’t want).

So after an import, if you want to recolour the schematic wiring, you do it via **net colours**, and you must enable the display toggle once.

### Do this (once) so colours actually show
1. Press **L** (View Configuration)
2. **Schematic → Net Color Override**
3. Tick **Show Net Color Override**

That’s exactly what that pop-up is trying to turn on. If you click **Yes** once, it’s the same effect.

### Then set colours properly
**Option A (fast, for lots of nets):**
1. Open **Panels → SCH**
2. Switch the SCH panel mode to **Nets**
3. Select one or multiple nets → set **Color / Net Color Override** (in the panel/properties)

**Option B (per net):**
1. Click a **net label** (or a wire that belongs to that net)
2. In **Properties**, set **Net Color / Color Override**

### Important gotcha after import
If the import created lots of **unnamed nets** (no net labels), Altium may treat many wires as separate nets, so recolouring feels impossible/pointless.
- In the SCH panel, check if you’ve got a ton of nets like **NetCxx / N$xx** etc.
- If yes, you’ll want to **apply net labels / net naming** (or run the importer’s “name nets” step) so colours map to meaningful nets.

If you upload a zoomed screenshot of one of the wires and its label (or confirm whether nets are named sensibly), I’ll tell you the quickest way to bulk-colour them without clicking 500 times.

[M7] ME (2026-03-01 18:02):
It was fine in all other shears. I filter wires. Select them all and change colours. Now it just fixated on net highlights 

[M8] AI (2026-03-01 18:02):
Yep — what’s changed is you’re no longer editing the **wire object’s colour**, you’re tripping the **net-colour / net-highlight** mechanism. That’s why it keeps dragging you into “Net Color Override / highlighting”.

Two clean ways out, depending on what you actually want:

## A) You want “old-school”: change **wire primitive** colours (not net colours)
1. **Esc** a couple of times (make sure you’re not in any net highlight command).
2. Select your wires (filter-select like you’re doing).
3. Open **Properties** panel.
4. In the selection properties, set **Color** (this is the *wire primitive* colour).
5. Crucial: make sure you are **NOT** changing anything called **Net Color**, **Net Color Override**, or **Net Highlight**.

If your Properties panel is only showing “Net …” fields when wires are selected, it means you’ve actually selected a **Net** (logical object) not the wire primitives.

### Force selection to be wire primitives
- Bottom-right: set selection filter to **Wires** (or open **Panels → Selection Filter** and tick **Wires** only).
- Then box-select again.

## B) You actually don’t care about primitive colour — you want net-based colouring, but without the nag
Then accept it and make it stable:
- Press **L** → **Schematic → Net Color Override** → tick **Show Net Color Override**
- Now changing net colours won’t pop that dialog and it won’t feel like “highlighting”; it will just be the net’s display colour.

## Why it “was fine on other sheets”
Common causes:
- Those other sheets have **Show Net Color Override OFF** and you were only changing **primitive wire colours**.
- This sheet (after import) has lots of wires belonging to **named nets** and Altium is prioritising net colour behaviour (or you’re selecting net labels/junctions rather than wires).

### Quick test (10 seconds)
Click **one** wire segment.
- If Properties title says **Wire** and you see **Color** → you’re in mode A.
- If Properties shows **Net** / **Net Color Override** → you’re in net mode.

If you want, tell me what the Properties panel header says when you click a wire on the “bad” sheet (e.g., *Wire*, *Net*, *Net Label*). That one word will determine the exact fix.

[M9] ME (2026-03-01 18:12):
[image]
It does t even let me say no its so frustrating 
[attached file: IMG_F273BB4D-E5DC-4CBF-BCEC-14376479B9C0.jpeg]

[M10] AI (2026-03-01 18:12):
Yeah I can see why that’s doing your head in — that dialog only appears when Altium thinks you’re trying to set **Net Color Override** (net-based colouring). If you’re just trying to recolour **wire primitives** after an import, you need to get out of the “net colour” pathway entirely.

Here are the fastest ways to regain control.

## 1) First: kill the pop-up even if it won’t click
While that dialog is up, try **keyboard** dismissal:

- **Esc** (often closes it)
- If not: **Tab** until the **No** button is selected, then **Enter**
- Or try **Alt + N** (sometimes “No” is the accelerator)
- Worst case: **Alt + F4** closes the dialog window

Once it’s gone, do the next bit so it stops coming back.

## 2) Stop Altium from going into “Net Color Override” when you change colour
What’s happening: your selection (via filter) is likely grabbing **nets / net labels / connections**, not the **wire primitives**. So when you change colour, Altium interprets it as “set net colour” → prompts you.

### Force selection to *wires only*
1. Open **Panels → Selection Filter**
2. Tick **Wires** (and optionally **Bus**)  
3. Untick **Net Labels**, **Junctions**, **Ports**, **Power Ports**, **Text**, etc.
4. Now do your filter/box select again.

Then, in the **Properties** panel, you should see the object type as **Wire**, and a plain **Color** field. Changing that will **not** trigger net-colour prompts.

## 3) Quick sanity check (this tells us instantly what’s being selected)
Click a single “wire” on that sheet and look at the **Properties** panel header:
- If it says **Wire** → you can change **Color** and you’re fine.
- If it says **Net / Net Label / Connection** → that’s why the pop-up keeps forcing itself.

## 4) Practical workaround if you’re blocked right now
If you *cannot* get it to stop prompting, do this once:
1. Click **Yes** (enables the net-colour display)
2. Immediately press **L** (View Configuration) → **Schematic → Net Color Override**
3. Turn it **back off** after you’ve finished whatever Altium is forcing.

But the real fix is #2: **select wire primitives, not nets**.

If you tell me what the Properties panel header says when you click one of those “wires” on the problem sheet (one word: Wire vs Net vs Net Label), I’ll give you the exact click-path for your case.

[M11] ME (2026-03-01 18:12):
It won’t let me, I ave ti say yes 

[M12] AI (2026-03-01 18:12):
Understood — if it’s forcing you, just **say Yes once**. That isn’t “highlight mode”; it’s simply enabling the *display* of net colour overrides so Altium can show what it’s about to change.

Then do this to get back to “change wire colour without net nonsense”:

## 1) Accept it once (Yes), then immediately disable net-colour override again
- Press **L** (View Configuration)
- **Schematic → Net Color Override**
- **Untick** **Show Net Color Override**

That stops the “net colour” mechanism being visually applied.

## 2) Make sure you’re editing **Wire** primitives (not the Net object)
This is the real issue: your selection is grabbing nets.

- Open **Panels → Selection Filter**
- Tick **Wires** (and **Buses** if needed)
- Untick **Net Labels**, **Junctions**, **Ports**, **Power Ports**, etc.
- Now reselect the wires and change **Color** in **Properties** (it should say **Wire** at the top)

## 3) If you want it to stop ever prompting again (nuclear option)
Disable net colour overrides entirely in preferences:
- **DXP → Preferences**
- **Schematic → Graphical Editing** (or **Schematic → General**, depends on version)
- Look for an option like **Net Color Override** / **Enable Net Color Override** / **Prompt to enable Net Color Override**
- Turn that off

(Altium’s wording varies between versions, but it’s in Schematic preferences.)

### Why “No” is effectively ignored
Because the action you triggered **requires** net-colour override to be visible; Altium is basically saying “I can’t show you the result unless I turn it on.”

If you can, tell me exactly how you’re changing the colour (Properties panel “Color” field? right-click menu? SCH panel nets list?). That determines the cleanest way to get you back to per-wire colouring.

[M13] ME (2026-03-01 18:14):
[image]
O just come sup with that 
[attached file: IMG_824FB51D-AB85-4000-9CAC-B6B33CA849C0.jpeg]

[M14] AI (2026-03-01 18:14):
That black vertical **“1…10”** popup is Altium’s **selection list** (it appears when there are **multiple objects under the cursor** and Altium wants you to choose which one you mean — wire vs net label vs junction vs port vs something stacked).

It’s strongly consistent with what’s been happening: you think you’re clicking a wire, but you’re actually landing on a *different* object (often a net / net label / connection), which then drags you into the Net Color Override prompt.

### Get rid of it (right now)
- Press **Esc** to cancel it.
- Or just click the actual item you want from the list (usually **1** is the topmost under cursor).

### Stop it happening / force “wire only”
Do this once and your life gets easier:

1. **Panels → Selection Filter**
2. **Tick only**: **Wires** (and **Buses** if you use buses)
3. **Untick**: **Net Labels**, **Junctions**, **Ports**, **Power Ports**, **Text**, **Components**, etc.

Now when you box-select or click, Altium won’t keep offering 10 candidate objects — it’ll just grab wires.

### One quick check (to confirm we’ve fixed it)
After setting the Selection Filter, click one of those cyan wires:
- The **Properties** panel header should say **Wire**.
- You should see a plain **Color** field.
If it says **Net** or **Net Label**, you’re still not selecting wires.

**Single question:** when that 1–10 list pops up, if you hit **1** does it select the wire, or does it select a label/connection? (You’ll see it in the Properties header.)

[M15] ME (2026-03-01 18:19):
It’s just constantly coming up. Highlight this, highlight that 

[M16] AI (2026-03-01 18:19):
Yep — you’re stuck in a “selection ambiguity + net interaction” loop. The quickest way out is to **force Altium to only be allowed to pick wires**, and to **clear any active highlight/filter**.

Do these in order:

## 1) Hard stop all highlight / filter modes
- Press **Shift + C** (clears filters/highlights)
- Then press **Esc** twice

## 2) Force Altium to stop offering “1–10” choices
Open **Panels → Selection Filter** and do a “wire-only” mode:

- ✅ **Wires**
- (optional) ✅ **Buses**
- ❌ everything else (Net Labels, Ports, Power Ports, Junctions, Components, Text, etc.)

Now click a wire: it should select instantly, no pop-up.

## 3) Make sure you’re not in a net command
If you’ve right-clicked anything like **Net Actions / Highlight Net / Color Net**, you’ll keep getting net prompts.
After step 2, click **blank space** and hit **Esc** once more.

## 4) Now change the colour the way you expect
With wires selected, in **Properties** you want the object type to be **Wire** and the field to be **Color** (not “Net Color Override”).

---

### One question (so I can lock the diagnosis):
When you click a cyan wire *right now*, what does the **Properties** panel title say at the top — **Wire** or **Net / Net Label**?

[M17] ME (2026-03-01 18:20):
[image]
This?
[attached file: IMG_6F7A8472-BF3B-4D51-81D7-F46F61AB3752.jpeg]

[M18] AI (2026-03-01 18:20):
Yes — **that panel is exactly part of the problem.** You’ve got the **SCH Filter** panel open, and it’s set to **Mask out** / **Deselect** etc. That will make Altium feel like it’s *constantly highlighting / masking / popping selection lists*.

Do this sequence:

## 1) Turn the filter OFF (stop the masking/highlighting)
In that **SCH Filter** panel:
- Untick **Mask out**
- Untick **Deselect**
- Untick **Zoom** (optional)
- Then click the little **X** (top-right of that panel) to close it

Then press:
- **Shift + C** (clears any remaining mask/filter)
- **Esc** once

## 2) Stop the “1–10” selection pop-up permanently (wire-only selection)
Open **Panels → Selection Filter** (different panel from SCH Filter)
- Tick **Wires** only (and Bus if needed)
- Untick the rest

Now when you click/box select, it won’t keep asking “which object?”

## 3) Now change wire colours without net nonsense
Box-select the wires → **Properties** should say **Wire** → change **Color**.

If it still throws the Net Color Override prompt, it means you’re still selecting a **Net / Net Label** somewhere in the selection — the wire-only Selection Filter will prevent that.

**One quick check:** in your screenshot, I can see the dropdown at the top of the SCH Filter panel. What does it currently say — “**Objects passing the filter**” actions? If you tell me whether **Mask out** was ticked, I can tell you why it got into this state.

[M19] ME (2026-03-01 18:22):
It’s still doing it 

[M20] AI (2026-03-01 18:22):
Alright — then we’ll do the “hard reset” that clears *everything* that can cause this (SCH Filter masking, net highlight, and selection ambiguity) and then force wire-only editing.

Do these steps exactly, in order:

## 1) Clear *all* masks/highlights/filters
1. Click **blank space** on the schematic.
2. Press **Esc** twice.
3. Press **Shift + C**.
4. Go **View → Clear Filter** (if you see it).

(That combination usually nukes stuck masks that survive one clear.)

## 2) Close the SCH Filter panel completely
- If **SCH Filter** is open: untick **Mask out** and **Deselect**, then close the panel (**X**).
- Also check **Panels** menu: if **SCH Filter** is ticked, untick it.

## 3) Turn OFF “net selection / net highlighting” behaviour
This is the bit that often gets latched after imports.

Go: **DXP → Preferences → Schematic → Graphical Editing**
- Find and **disable** options like:
  - **Click selects net** / **Prefer net objects** / **Net highlighting on selection** (wording varies)
  - Anything that makes clicking a wire act on the *net* rather than the *wire*

(You’re looking for “net” and “highlight” in that preference page.)

## 4) Force “wire primitives only” selection (this stops the 1–10 list)
Open **Panels → Selection Filter** and set:
- ✅ **Wires**
- (optional) ✅ **Buses**
- ❌ everything else

Now box-select your wires again.

## 5) Verify what you’re actually selecting (this tells us what’s still wrong)
Click one of the “wires” and look at the **Properties** panel header:
- If it says **Wire** → change **Color** and you’re done.
- If it says **Net** or **Net Label** → you are *still not selecting wires* (some preference or filter is forcing net selection).

**Single question:** when you click a wire *right now*, what does the Properties panel title say — **Wire** or **Net/Net Label**?

[M21] ME (2026-03-01 20:42):
How do I change the visual grid 

[M22] AI (2026-03-01 20:42):
Sure — in Altium there are *two* “grids” to think about: the **visible grid (dots/lines)** and the **snap grid** (what your cursor actually snaps to). Usually you want to change both.

### 1) Change the **visible grid** (what you see)
In the Schematic editor:
1. Press **L** (View Configuration)
2. Go to **Schematic → Grids** (or just **Grids**)
3. Adjust:
   - **Grid Style**: *Dots / Lines / None*
   - **Grid Color**
   - **Grid Spacing** (the displayed spacing)

### 2) Change the **snap grid** (what you place on)
Still in schematic:
- Press **G** to cycle snap grid presets (quick way)
- Or go **View → Grids → Snap Grid** and set the value you want

(You can also set it in the document options depending on your setup.)

### 3) If you’re actually in the **PCB editor**
- Press **G** to cycle the snap grid
- Press **Ctrl + G** to directly set the grid value (common shortcut)
- For visible grid: **L** → **View Configuration → Grids**

One question so I point you to the exact menu: are you changing the grid on the **schematic (SchDoc)** or the **PCB (PcbDoc)**?

[M23] ME (2026-03-01 20:47):
What grid should I work on 

[M24] AI (2026-03-01 20:47):
It depends what you’re doing (schematic vs PCB), but there are “safe defaults” that keep Altium happy and keep you aligned to libraries.

## Schematic (SchDoc)
**Use an imperial snap grid for placement and wiring.**

- **Primary snap grid:** **10 mil**
- **Finer snap grid (temporary):** **5 mil** (sometimes **1 mil** for awkward symbols)
- **Electrical grid:** keep it aligned with your snap (typically **10 mil**)

Why: most Altium symbols/pins are built on a 10-mil lattice, and off-grid pins are what cause weird selection/connection pain after imports.

**Habit:** stay on **10 mil** for normal work, drop to **5 mil** briefly, then go back.

## PCB (PcbDoc)
**Use metric for modern footprints (mm) OR imperial (mil) if your library is mil-based — but be consistent.**

A solid “doesn’t fight you” setup for mixed work:
- **Placement grid:** **0.1 mm** (or **5 mil** if imperial)
- **Routing grid:** **0.05 mm** (or **2.5 mil**)
- **Fine adjust (temporary):** **0.025 mm** (or **1 mil**)

For connectors / BGAs you often need the finer one; for big parts stick to the coarser.

## The rule that matters most
**Match the grid to your libraries**:
- If your imported symbols/footprints were created on **10 mil**, stay there.
- If your PCB library is **0.1 mm**, stick with that.

### One question (so I don’t steer you wrong):
Are you asking about grid for **schematic wiring** or **PCB placement/routing**? (Just “schematic” or “PCB”.)

[M25] ME (2026-03-01 20:48):
This is schematic 

[M26] AI (2026-03-01 20:48):
For **schematic**, keep it simple and consistent:

### Recommended schematic grids
- **Snap grid (main): 10 mil**
- **Snap grid (temporary fine): 5 mil** (drop to this only when you *have* to)
- **Electrical grid: 10 mil**

That combo keeps pins/wires aligned and avoids the “off-grid import” weirdness.

### Quick way to work
- Press **G** to cycle snap grids (set it so one of the steps is **10 mil** and another is **5 mil**).
- If you need to set it explicitly: **View → Grids → Snap Grid → 10mil** (and same menu for 5mil).
- Electrical grid is in **Document Options** (often **Design → Document Options**) → set **Electrical Grid = 10mil**.

One tiny check: when you click a wire endpoint/pin, does it “grab” nicely, or do you see tiny gaps / miss-clicks? If it’s the latter, you’ve likely got symbols/pins off the 10 mil lattice and we can realign them.

[M27] ME (2026-03-01 20:49):
I keep getting problems with off grid even when I’ve aligned it

[M28] AI (2026-03-01 20:49):
Yeah — that happens a lot after imports, because **your grid can be “right” but the objects aren’t actually on it** (pins, wire vertices, junctions, net labels can sit at weird fractional coords).

Let’s isolate *where* the off-grid is coming from, then fix it cleanly.

### The key idea
In schematics there are **two grids** that matter:
- **Snap grid** (your cursor snap)
- **Electrical grid** (what Altium uses for “connections are valid”)

Even if you align visually, if a **pin** is off-grid by 1 mil (or worse), wires can look connected but aren’t “electrically” clean.

### Quick fix workflow (doesn’t require re-drawing everything)
1) Set **Snap grid = 1 mil** (temporarily)  
2) Set **Electrical grid = 10 mil** (leave it here)  
3) For the problem area: **nudge** the offending item onto the electrical lattice:
   - grab the **wire vertex** or **junction**, move it away and back so it re-snaps
   - same for **net labels** sitting on the wire
4) Return **Snap grid to 10 mil** for normal work

This works because 1 mil lets you “pick up” imported junk that isn’t landing on 10 mil increments.

### Better: find the real culprit (usually pins)
If it’s the **symbol pins** that are off-grid, you’ll chase this forever until you fix the library symbol. In that case the right solution is to open the symbol in the library, put pins back on a 10 mil lattice, then update the schematic.

**One question (so I don’t send you down the wrong path):**  
When you say “off grid”, is it a **compiler/ERC message** (like “off-grid object”) or are you noticing it because **wires won’t properly connect / you get little gaps** when wiring?

[M29] ME (2026-03-01 20:50):
I’m going to have to align it all again, and I don’t want to have to do it again. What settings shall I use for all designs. We work in though for grids 25 or 50

[M30] AI (2026-03-01 20:50):
I hear you. The way to avoid “doing it twice” is: pick a **single company default** (snap + electrical) that matches how your symbols are built, and only ever deviate temporarily.

If your place uses **25/50 thou**, here’s the clean, repeatable setup I’d standardise on for schematics:

## Company-standard schematic grid settings (thou)
### Defaults (use 95% of the time)
- **Snap grid:** **25 mil**
- **Electrical grid:** **25 mil**
- **Visible grid:** **25 mil** (dots)

### When you need more resolution (temporary)
- **Snap grid:** **5 mil** (or **1 mil** for “salvage/import surgery”)
- **Electrical grid stays:** **25 mil**

**Why keep electrical at 25 mil?**  
It enforces that real connection points (pins, wire ends, junctions) land on a consistent lattice, which is what stops latent off-grid grief later. You can still *draw* with a finer snap, but you “land” on 25 mil.

## The one non-negotiable rule
**Symbols must have pins on the electrical grid.**  
If imported symbols have pins on 10 mil but you set electrical to 25 mil, you’ll get endless off-grid flags. So the “right” company standard is whichever matches your symbol library lattice.

### Pick 25 or 50?
- If your library symbols are dense (ICs, lots of pins close): **25 mil** is the better default.
- **50 mil** is fine for big block diagrams, but it’s too coarse for many real symbols and tends to force awkward pin spacing.

So: I’d standardise on **25 mil**.

## Make it “sticky” for every new schematic
In **Preferences / Document Options**, set the defaults, then save as your company **template** so new sheets inherit it.

**Single question:** are your existing “good” schematics (the ones that don’t complain) built on **25 mil pin spacing** or **50 mil pin spacing**? (Just answer “25” or “50”.) That tells us which electrical grid will stop the off-grid messages across *all* designs.

[M31] ME (2026-03-01 20:51):
[image]
So what do I do here 
[attached file: IMG_4B313BC6-BA36-4A0C-95EC-D0B638B66746.jpeg]

[M32] AI (2026-03-01 20:51):
Perfect — you’re in exactly the right place (**Preferences → Schematic → Grids**). This page sets your *global schematic grid presets*.

For a solid “never redo it” setup in **thou**, do this:

## What to set here (recommended company default)
### 1) Imperial presets
Set the **top row** as your main working grid:

- **Snap Grid:** ✅ **25 mil**
- **Snap Distance:** ✅ **25 mil**
- **Visible Grid:** ✅ **25 mil**

Then keep the other two as “zoom levels”:
- **50 mil**: ✅ for all three (handy for big block moves)
- **100 mil**: ✅ for all three (rarely needed, but fine)

That’s it on this screen — press **OK**.

## Then set the one that actually matters for “off-grid” errors
This screen does **not** set the **Electrical Grid**. That’s the key setting that drives “off grid” complaints.

Do this next (same schematic document open):
1. Go to **Design → Document Options** (in the schematic)
2. Set **Electrical Grid = 25 mil**

Now you’ve got: snap=25, visible=25, electrical=25 — consistent.

## Practical workflow (so you don’t get trapped again)
- Work normally on **25 mil**
- If you need to “rescue” imported junk: temporarily drop **snap** to **5 mil or 1 mil**, BUT keep **electrical** at **25 mil**, and then snap endpoints back onto the lattice.

### One check (single question)
Do your symbols’ **pin pitch** look like **100 mil between pins** (typical DIP-style) or tighter? If you’ve got lots of tight pin symbols, 25 mil electrical is still fine — but it tells us whether your library is actually built for 25 mil or something else.

[M33] ME (2026-03-01 20:53):
[image]
Can’t see it
[attached file: IMG_47536F1C-8EC3-47A4-8F5D-CA06779120E6.jpeg]

[M34] AI (2026-03-01 20:53):
You’re looking in the right general area, but **in your Altium version that setting isn’t under “Design”** (hence why you can’t see *Document Options* there).

Do this instead (schematic open):

## Find Document Options (schematic)
### Option 1 (most reliable)
- Press **F1**, then type **Document Options** in the help/search bar (it will jump you to the command/menu path).

### Option 2 (common in AD 26)
- Go **Tools → Document Options** (some installs put it here)
- Or **Project → Document Options** (less common)

### Option 3 (panel-based)
- Open **Panels → Properties**
- Click **blank space** on the schematic sheet (so nothing is selected)
- In Properties you should see **Document Options** / **General / Grids** for the sheet, including **Electrical Grid**

## If you just want the electrical grid value (the one that stops off-grid errors)
Once you’re in Document Options / sheet properties:
- Set **Electrical Grid = 25 mil** (to match your snap grid standard)

---

### One quick question (so I can direct you to the exact place in *your* UI)
When you click **blank sheet**, what does the **Properties** panel title say? (e.g., “**Sheet**”, “**SCH Document**”, etc.)

[M35] ME (2026-03-01 20:55):
[image]
Here?
[attached file: IMG_5F239229-F863-47E6-90A1-D18091DBAB57.jpeg]

[M36] AI (2026-03-01 20:55):
Yep — you’re in the right **Preferences** window, but you’re on **Schematic → General**. The **Electrical Grid** isn’t on that page.

### Do this (one step)
On the left tree, click:

**Schematic → Grids**

(You’ve already found it once — it’s just a couple of items below “General”.)

### What you need to set
There are **two** things to set, in two places:

## A) Global defaults (Preferences → Schematic → Grids)
Set your presets like you showed:
- **25 mil** for Snap / Snap Distance / Visible
(keep 50 and 100 as secondary presets)

This affects *how new docs behave* and your grid cycling.

## B) Per-sheet Electrical Grid (this stops off-grid errors)
This is **NOT** in Preferences. It’s per schematic sheet:

1. Close Preferences for a moment.
2. Go back to the schematic sheet.
3. Click **blank space** on the sheet (so nothing is selected).
4. Open the **Properties** panel (Panels → Properties).
5. In Properties for the **SCH Document / Sheet**, find **Electrical Grid** and set it to:
   - **25 mil**

That’s the setting that makes Altium stop moaning even if you’re “aligned”.

---

### One quick check (so we don’t miss the UI detail)
When you click blank space on the schematic, does the **Properties** panel show **“SCH Document”** (or “Sheet”)? If you don’t see Properties at all, tell me and I’ll give you the exact menu path to bring it up.

[M37] ME (2026-03-01 20:56):
[image]
[attached file: IMG_69096968-888D-4F79-8D42-30B1C440A64F.jpeg]

[M38] AI (2026-03-01 20:56):
Yes — **this is the right panel** (Properties → **Document Options**). And I can see the core issue straight away:

You’re currently in **mm** units with **1mm / 0.4mm** grids — that’s *guaranteed* to create off-grid pain if your imported symbols were built in thou.

Do this right here:

## Set your “never redo it” schematic defaults (thou)
1) Under **Units**, click **mils** (not mm).

2) Then set:
- **Visible Grid:** **25mil**
- **Snap Grid:** ✅ **25mil**
- **Snap Distance:** **25mil**

3) Keep ✅ **Snap to Electrical Object Hotspots** ON (good).

## Now set the missing piece: Electrical Grid
In this same **Document Options** panel, scroll a bit (it’s often just below the grid fields) and find **Electrical Grid**.
- Set **Electrical Grid = 25mil**

That’s the one that stops Altium flagging connections as off-grid.

### If you can’t see “Electrical Grid” anywhere
Use the **Search** box at the top of the Properties panel and type: **electrical**  
It will jump you to it.

---

### One small but important note
This change is **per sheet**, so once you fix this sheet, do the same on the other imported sheets (or we can make a template standard after).

**Do this next and tell me what you see:** after switching to **mils**, do your wires/pins suddenly “line up” more naturally, or do some still sit between grid dots?

[M39] ME (2026-03-01 20:57):
[image]
[attached file: IMG_B7C7DA4E-5DC5-4EE4-B514-6E0AF5BAA572.jpeg]

[M40] AI (2026-03-01 20:57):
Nice — you’ve now got the **visual + snap** grid set correctly to **25 mil** in that sheet. 👍

What’s missing (and what actually stops the “off grid” errors) is the **Electrical Grid** setting — it’s *not visible in your screenshot*, but it’s on this same “Document Options” context.

## Do this next (on the same Properties panel)
1. In the **Search** box at the top of the Properties panel, type: **electrical**
2. Set **Electrical Grid** to **25mil**

That’s the “no more re-align later” setting.

### If “electrical” search shows nothing
You might be editing **Sheet options** rather than **SCH Document options**.
Do this:
1. Click **blank area** of the schematic sheet again (so nothing is selected)
2. At the very top of Properties, make sure it says **Document Options** (not a specific object)
3. Search **electrical** again

## After you set it
Press **Shift + C** once to clear any previous masks/highlights, then try wiring/dragging a couple of junctions — they should land cleanly.

**One question:** when you type **electrical** in that search box, do you get an **Electrical Grid** field, yes or no?

[M41] ME (2026-03-01 20:58):
[image]
It comes up but it’s just toggle to 
[attached file: IMG_B48A97E6-2D77-42E2-AB91-2CE0F342392B.jpeg]

[M42] AI (2026-03-01 20:58):
Right — that search box you’re using there is the **global command search**, so it’s only finding **“Toggle Electrical Grid”** (Shift+E). That just shows/hides the electrical grid display — it doesn’t set the electrical grid value.

You need to set the **Electrical Grid value** in the **Properties panel** (Document Options), not in command search.

## Do this (works in your exact UI)
1) Click **blank space** on the schematic (so “Nothing selected” stays at the bottom).
2) In the **Properties** panel, click in its **Search** field (inside the Properties panel, not the top global one).
3) Type: **Electrical**

You should see **Electrical Grid** appear. Set it to **25mil**.

### If you can’t find the Properties-panel search
In your earlier screenshot, it’s the small **Search** box just under the “Document Options / Components (and 11 more)” row.

## Alternative (no searching)
In **Properties → Document Options**, scroll down a bit. In many AD26 builds, **Electrical Grid** is under a “Grids” or “General” subsection and can be off-screen until you scroll.

## Quick sanity check
- **Shift + E** = only turns the electrical grid **display** on/off.
- **Electrical Grid = 25mil** = fixes the off-grid connection rules.

**One question:** in the Properties panel, do you see a little funnel/filter icon (blue) next to the object selector? If it’s filtering what fields show, it can hide Electrical Grid — we can turn that filter off.

[M43] ME (2026-03-01 20:59):
[image]
[attached file: IMG_93001637-92AD-4913-9207-CF9DACC113F4.jpeg]

[M44] AI (2026-03-01 20:59):
Got it — this screenshot is the smoking gun.

You’ve got the **funnel filter** (top-right of Properties) turned **ON**, so the Properties panel is only showing a reduced set of fields. That’s why you can’t see **Electrical Grid** — it’s being filtered out.

## Do this (10 seconds)
1) Click the **funnel icon** (top right, the blue one) to **turn the filter off**.  
   - If it opens a small menu, choose **Clear / Reset / Show All** (wording varies).

2) Now clear the search box (delete “elec”) and scroll, or search again for **grid** or **electrical**.

You should then see **Electrical Grid** as an editable value.

### If you still don’t see it
At the top left of the Properties panel, click the drop-down that currently says:
**“Components (and 11 more)”**
and set it to **Document Options / Sheet / SCH Document** (i.e., the document itself, not components).

Then search **electrical** again.

---

**Single next action:** click that funnel and tell me if it turns grey/off and more fields appear.

[M45] ME (2026-03-01 21:00):
[image]
[attached file: IMG_70295BFC-A942-4280-B7ED-672E92E55135.jpeg]

[M46] AI (2026-03-01 21:00):
Ok — the funnel is now **grey** (so filter is off). Good.

What you’re seeing now is simply because the **search term is filtering the fields** to only ones containing “elec”, and the only match in Document Options is **“Snap to Electrical Object Hotspots”**.

So: **clear the search box** and the rest of the grid fields will come back.

## Do this
1) Delete `elec` from the Properties search field (make it blank).
2) Scroll the **Document Options** list and look for **Grids** / **Electrical Grid**.

### If you still can’t find it
Use the search box again but type **grid** (not “elec”):
- You should then see **Snap Grid**, **Visible Grid**, **Snap Distance**, and (crucially) **Electrical Grid** if it exists in this context.

### If “Electrical Grid” genuinely doesn’t exist in your build
Some Altium setups don’t expose “Electrical Grid” as a separate value; instead they use:
- snap-to-hotspots + snap grid as the enforcement mechanism, and the “off grid” warnings come from **Compiler settings**.

In that case the “fix” is:
- keep **Snap Grid = 25mil**, **Snap Distance = 25mil**, **Snap to Electrical Object Hotspots = ON**
- and turn off (or relax) the off-grid violation check in **Project → Project Options → Error Reporting** (look for “Off grid” / “Electrical grid” warnings).

**Single question:** when you clear the search and type **grid**, do you see an **Electrical Grid** field, or only Snap/Visible/Snap Distance?

[M47] ME (2026-03-01 21:01):
[image]
Shall I select this 
[attached file: IMG_CD8BE5D5-3DBC-44E8-BBDC-33521A2D34AE.jpeg]

[M48] AI (2026-03-01 21:01):
Yes — **tick that** ✅

**Snap to Electrical Object Hotspots** is exactly what you want ON, especially right after an import. It forces wire ends, pins, junctions, ports, etc. to “land” on valid connection points even if the underlying geometry is a bit messy.

So for your “never align again” baseline on schematics:

- Units: **mils**
- Visible Grid: **25mil**
- Snap Grid: **25mil**
- Snap Distance: **25mil**
- ✅ **Snap to Electrical Object Hotspots**: **ON**

That combination is the best practical guardrail in AD26 when the explicit “Electrical Grid” field isn’t exposed.

### One more thing (very important)
This setting helps new edits snap correctly, but it **won’t automatically fix** existing off-grid vertices. For the imported sheet, do a quick “re-seat” in the worst area:
- Grab a wire end/junction, move it a tiny bit, then put it back — it will re-snap to the hotspot.

If you want a fast check: after turning it on, try placing a new wire onto a pin—does it “magnet” nicely onto the pin centre?

[M49] ME (2026-03-01 21:18):
[image]
How do I change the colour of the designator in the part 
[attached file: IMG_90F15CB1-5AC0-4B44-8BCD-E4416D743763.jpeg]

[M50] AI (2026-03-01 21:19):
You’ve got two different “layers” you can change here, depending on whether you want it **just on this sheet** or **for every instance of that symbol**.

## Option 1 — Change just this instance (fast)
1) Click the **designator text** itself (e.g., click “C136” or “R223” until the Properties panel shows **Designator** / **Text**).
2) In the **Properties** panel, set **Color** (or disable “Use default” then set Color).

If clicking keeps grabbing the component instead of the text:
- Use **Tab** to cycle the selection under the cursor until **Designator** is selected, or
- Temporarily set **Selection Filter → Texts ON** (and maybe Components off) to make it easy to click the text.

## Option 2 — Change it for all parts of that type (library-level)
This is the “do it once forever” way:
1) Open the component in the **SCHLIB** (symbol library).
2) Click the **Designator** text object.
3) Set its **Color** in Properties.
4) **Save library** and **Update** / **Refresh** the schematic from libraries.

This will update every placed instance that uses that library symbol (unless overridden locally).

---

### Important note (from your screenshot)
Your **Properties panel Units** on the right shows **mm** again — that means you’re not currently on the document options you set earlier (or you’re on a different sheet / selection context). Doesn’t block color changes, but worth keeping consistent.

**One question:** do you want the designator colour change **only for a few parts on this schematic**, or **as a global standard** across the whole project/library?

[M51] ME (2026-03-01 21:19):
[image]
Designator doesn’t show in part 
[attached file: IMG_3CF62C07-37CF-49D5-89FF-E65ADFE2E7CC.jpeg]

[M52] AI (2026-03-01 21:20):
Right — you’re in the **SCHLIB editor** (good), but you’ve selected the **component** object, not the **Designator text object**, and it looks like this symbol **doesn’t currently have a Designator string placed** (or it’s hidden).

Here’s how to fix it cleanly.

## 1) Check if the Designator is just hidden
In the SCHLIB editor:
- Click **View → Document Options** (or in the right Properties panel, look for “Show/Hide…” options)
- Make sure **Designators are visible** (sometimes it’s “Show Component Designators”).

If that doesn’t reveal it, it’s probably not placed.

## 2) Place the Designator string onto the symbol (library-level fix)
You want to place the special text string, not normal text.

1. Go to **Place → Text String → Special String**
2. Choose **.Designator** (or **Designator**) from the list
3. Click to place it where you want on the symbol

Now you’ll see something like `C?` appear.

## 3) Change its colour (and other formatting)
1. Click the newly placed `C?` text
2. In **Properties**, set **Color** (and font/size if needed)

## 4) Push it back into the schematic
- **Save** the SCHLIB
- In the schematic, run **Tools → Update From Libraries** (or whatever update flow you use)

---

### One thing to watch (common gotcha)
If you placed **normal text** “C?” instead of the **special string**, it won’t update to C136/C137 etc. So make sure it’s the **Special String = Designator**.

**Single question:** when you go to **Place**, do you see **Special String** in the menu? If not, I’ll give you the exact AD26 menu path (it moves slightly depending on workspace).

[M53] ME (2026-03-01 21:21):
[image]
[image]
Can’t see it 
[attached file: IMG_2CA13C95-BDE1-4F5C-917D-AB72E75BD89F.jpeg]
[attached file: IMG_0350C4F8-669E-4D2E-864E-30206C2D5A3E.jpeg]

[M54] AI (2026-03-01 21:21):
You’re in the **right dropdown**, but you’re looking at the **sheet template special strings** (that’s why you see things like `=Drawn_By`, `=Project_Name`, etc.). That list is for title blocks, not components.

For a component designator you need the **special string for a component**, which in Altium is:

- `=Designator`
(or sometimes `=Comment` / `=Value` etc.)

It won’t be in that title-block list if you’re placing a *generic* special string.

### Do this instead (library symbol, SCHLIB)
1) Make sure you’re editing the **symbol** (SCHLIB), not the sheet template.
2) Go **Place → Text String** (or **Place → Text**) and choose **Special String**.
3) In the dropdown, **type** (literally type into the field) `=Designator` and press **Enter**.
4) Click to place it on the symbol.

Altium will accept special strings even if they’re not shown in the list.

### If you want the “official” way with the correct dialog
There’s also a command specifically for component fields:
- **Place → Designator** (sometimes it’s called **Place → Designator/Comment** in SCHLIB)

That places the correct dynamic designator object, which you can then colour.

### Then change colour
Click the placed `C?` / `R?` text → **Properties → Color**.

**Single question:** are you editing an **SCHLIB symbol** (like your capacitor symbol), or are you accidentally editing the **A2 schematic template** (title block)? The strings you’re seeing look very template-ish, so I want to steer you to the right “Place” menu.

[M55] ME (2026-03-01 21:36):
[image]
Why can’t I move the value?
[attached file: IMG_F85E5BF3-2E31-46C8-9E67-1D7ADAEE6735.jpeg]

[M56] AI (2026-03-01 21:36):
You *can* move it — but right now you’re almost certainly selecting the **component body** (or the whole component), not the **value text object**. In Altium, the value is a separate “parameter text” primitive, and it can also be **locked** or **set to follow the component**.

Do this in this order:

## 1) Make sure you’re grabbing the VALUE text, not the part
- Hover over the **“4k87”** text
- Press **Tab** a few times until the selection cycles to **Value / Parameter** (you’ll see the highlight change and the Properties panel title change)
- Then **click-drag** or use **Move** (M, M)

If the “1–10” selection list appears, pick the one that says **Text / Parameter** (not Component).

## 2) Check if the text is locked
With the value text selected, look in **Properties** for:
- **Locked** (or a padlock icon) → **untick** it.

## 3) If it snaps back, it’s set to “autoposition / follow component”
Still with the value text selected, in Properties look for something like:
- **Autoposition** (Top/Bottom/Left/Right)  
Set it to **Manual** (or disable autoposition), then move it.

## 4) If you’re editing in the SCHLIB vs the schematic
- In a **SCHLIB**, the value/designator can be configured as “hidden” or “default position.” You can still move it, but make sure you’re selecting the **parameter text** primitive.

### One-question diagnostic
When you click the “4k87” text, what does the **Properties panel header** say: **Component**, **Text**, or **Parameter**?

[M57] ME (2026-03-01 21:39):
[image]
Def won’t let me select it. Can select designator.
[attached file: IMG_0223FC42-A5D1-4239-ABC8-5F1C8AB5B4A3.jpeg]

[M58] AI (2026-03-01 21:39):
Got it — in that screenshot the **value “100n” is not the normal selectable “Comment”/Value text**. It’s almost certainly coming from a **Parameter Set / blanket / harness/variant text / or a “locked” text primitive** that’s sitting on top of/linked to the component — which is why you can grab the designator but the value won’t highlight.

Let’s nail it with the quickest test/fix.

## Step 1: Force-pick what’s under the cursor (no guessing)
Hover your mouse directly over **“100n”** and press **Tab** repeatedly.

- If a selection list pops up, pick the item that says **Text** / **Parameter** (not Component/Wire).
- If it *never* offers “Text/Parameter” for the 100n, it’s not a normal text object.

## Step 2: Check your Selection Filter (this is the common cause)
Open **Panels → Selection Filter** and make sure **Texts** and **Parameters** are enabled.

If you’ve been toggling filters earlier, it’s very easy to have **Texts** disabled, which makes value text unselectable.

## Step 3: If it’s still unselectable, it’s probably “Comment” autoposition
In Altium the component’s **Comment** can be set to autoposition, and then it won’t move like free text unless you switch it to manual.

Do this:
1. Click the **component body** for C187 (not the text).
2. In **Properties**, find **Comment** display settings (often under “Parameters”/“Graphical”).
3. Look for **Autoposition** (Top/Bottom/Left/Right).  
   Set it to **Manual**.
4. Now try selecting/moving “100n” again.

## Step 4: If it’s a Parameter Set (most likely in imported sheets)
Sometimes imports place a **Parameter Set** that “prints” the value and it’s not the component comment.

Quick check:
- Click near the “100n” but not on the component.
- If Properties shows **Parameter Set**, delete it (or hide it), and then use the real component Comment.

---

### One question (single, decisive):
When you hover over **100n** and press **Tab**, what object type does Altium say you’re selecting (Text / Parameter Set / Component / nothing)?

[M59] ME (2026-03-01 21:42):
[image]
Howndoninstol the default to yellow in the designator 
[attached file: IMG_7E087989-7AC2-49EA-9DC2-906A7ACB93C8.jpeg]

[M60] AI (2026-03-01 21:42):
You’re asking for a **global default**: *all designators (R?, C?, U?) show in yellow by default*.

In Altium schematic, that’s controlled by the **system color for the Designator text (and/or Parameter text)** — not by the net/highlight stuff. Set it once in **Preferences**, and it applies across schematics.

## Set designator default colour (global)
1) **DXP → Preferences**
2) Go to **Schematic → Colors** (sometimes under **Schematic → Graphical Editing → Colors** depending on install)
3) Find the item for:
   - **Component Designators** (or just **Designator**)
4) Set that colour to **Yellow**
5) Also set **Component Comments** (if you want values like 100n to follow a default colour too)
6) Click **Apply / OK**

That sets the **default**, so newly placed and normally formatted designators will come in yellow.

## If some designators stay black/blue after this
Those instances are **overridden locally** (common after import).
To reset them back to the default:
- Select the component(s)
- In **Properties**, for the Designator text, look for **Use System Color** / **Use Default** and turn it **ON** (or clear the local colour override).

### The one thing I need from you (single question)
In your Preferences tree on the left, do you see a **“Schematic → Colors”** entry? (Yes/No). If not, I’ll give the exact alternate path in AD 26.3.0.

[M61] ME (2026-03-01 21:46):
[image]
[attached file: IMG_EFFEDA91-3211-4B72-8DF6-9178DCB71AC2.jpeg]

[M62] AI (2026-03-01 21:46):
Yep — you’re in **Schematic → Graphical Editing**, but this page only controls **selection colours / cursor / special-strings display**. It won’t set the default **designator text colour**.

What you want is the **Schematic Colors** page.

## Do this (from the same Preferences window)
1) In the left tree, scroll a bit and click:
**Schematic → Colors**  
(if you don’t see “Colors”, look under **Schematic → General** or a “System Colors” style entry — it’s usually near Graphical Editing / Grids.)

2) In **Colors**, set:
- **Component Designators** = **Yellow**
(Optional) also set:
- **Component Comments** = whatever you want for values (often white/cyan)

3) Click **Apply** then **OK**.

## If some designators stay non-yellow after you set this
That means those designators have a **local override** from the import.
Fix one as a test:
- Click the designator text (e.g., “R146”)
- In Properties, enable **Use System Color / Use Default** (wording varies)

Once that’s confirmed, you can batch-fix by selecting all components and clearing local colours.

**One question:** in your left tree under *Schematic*, do you see an item literally called **Colors** (yes/no)?

[M63] ME (2026-03-01 21:47):
[image]
How do I change the fit of the value 
[attached file: IMG_D4DB44C6-F7E9-4BA5-AE26-5467486812B1.jpeg]

[M64] AI (2026-03-01 21:48):
You’re editing the **SCHLIB symbol** and you’ve selected the **component**, so you’re only seeing the *data* for Designator/Comment — not the **text formatting** for how the value is drawn.

To change the **font/size (“fit”)** of the value you must select the **Comment text primitive** (the bit that actually prints on the symbol).

## Do this
1) In the SCHLIB editor, **turn on Comment visibility** if needed:
- Press **L** (View Configuration) → make sure **Comments** are shown.

2) Now **click the comment text** on the symbol (it will usually show as `=Comment` or something like `R?` / `C?` / value placeholder).
- If you can’t click it, hover and press **Tab** until it selects **Text / Comment**.

3) With that text selected, in **Properties** set:
- **Font** (typeface)
- **Height** (text size)
- **Width / stroke** (if available)
- **Justification** (left/centre/right)
- **Autoposition** → set to **Manual** if it keeps snapping back

That’s the “fit” control.

### If there is *no comment text on the symbol*
Some imported symbols don’t include it. In that case:
- **Place → Text String → Special String → `=Comment`**
- Place it, then format it as above.

**Single question:** on the symbol drawing, do you actually see a `=Comment` (or any value placeholder) anywhere, or is it missing entirely?

[M65] ME (2026-03-01 21:51):
[image]
Every time I reload it it goes back to yellow 
[attached file: IMG_693A710E-5450-48A6-A3CE-7155A1E8A2F7.jpeg]

[M66] AI (2026-03-01 21:51):
That behaviour is *exactly* what you get when the designator colour is coming from the **library/system default**, and your manual change was only a **local override**. When you “reload/update from libraries”, Altium reapplies the library’s formatting → back to yellow.

So you’ve got two choices:

## Option A (recommended): change it “properly” in the SCHLIB so it stays
You need to set the designator/parameter text colour **inside the symbol**, then update.

1) Open the part in the **SCHLIB**
2) Click the **Designator text** (the actual text object, e.g. `R?`, not the component)
3) In **Properties**, set **Color** to what you want  
   - If there’s a tick like **Use System Color / Use Default**, turn it **OFF** so the library stores the colour.
4) Save SCHLIB
5) Update schematic from libraries

Now reloads won’t change it.

## Option B: keep the library yellow, but stop updates overwriting your local tweak
When you run **Update From Libraries**, Altium has an option that controls whether it pushes **graphics** (including designator/comment formatting).

- In the **Update From Libraries** dialog, look for options like:
  - **Update graphical parameters**
  - **Update symbol graphics**
  - **Update parameters / designator/comment positions**
  
Disable the one that updates **graphics/graphical** so it doesn’t reapply the library’s colours/positions.

(Names vary, but it’s the “graphical” one.)

---

### The fast diagnostic (one question)
When you select the designator text on the schematic, do you see an option like **“Use System Color”** (ticked) in Properties?  
- If **yes** → that’s why it snaps back. Turn that off in the **library** (Option A) or stop graphical updates (Option B).

[M67] ME (2026-03-01 21:52):
The designator text doesn’t show in the part 

[M68] AI (2026-03-01 21:52):
Got you — if the **designator text primitive isn’t present in the SCHLIB symbol**, then Altium is generating the yellow designators from the **component’s default/parameter display**, and every library update will keep reasserting that behaviour. You need to **add a real Designator text object** to the symbol (once), then you can format it and it will stay.

Here’s the clean way to do it in AD26 SCHLIB:

## Add a real Designator to the symbol (SCHLIB)
1) Open the symbol in the **SCHLIB**.
2) Go to **Place → Designator**  
   - If you don’t see that menu item: use **Place → Text String** (or **Text**) → **Special String**.
3) In the special string field, **type** exactly:
   - `=Designator`
   (don’t rely on the dropdown list; it won’t always show it)
4) Click to place it on the symbol.

You should now see `R?` / `C?` on the library symbol.

## Set the colour (and “fit”)
1) Click the `R?` / `C?` text you just placed
2) In **Properties** set:
- **Color** (your desired default)
- Font/height if needed
- Autoposition: **Manual** (if it keeps snapping)

## Save + push to schematic
- Save SCHLIB
- Update schematic from libraries

### One important detail
If the symbol currently shows **no designator at all**, check that you’re not in a view mode hiding it:
- Press **L** → ensure **Special Strings** are displayed.

**Single question:** in your SCHLIB editor, do you have a **Place** menu at the top (File/Edit/View/Place…)? If yes, click **Place** and tell me whether you see **Designator** in that list.

[M69] ME (2026-03-01 21:54):
[image]
[attached file: IMG_18C760F4-1CB0-4456-BA98-69AE6127E914.jpeg]

[M70] AI (2026-03-01 21:55):
Yes — **this is the exact place** to set the *default colour* for Designators (and Comments/Values) so they appear in the SCHLIB/schematic without you manually placing text.

Do this:

## Set default designator colour (global)
1) In that list, click **Designator**
2) On the right, change the **Color** swatch to the colour you want (e.g. **yellow**)
3) Tick **Permanent**
4) Click **OK**

## Also set the default value/comment colour
Altium usually treats the displayed “value” as the **Comment** field:
1) Click **Comment** in the primitive list
2) Set the **Color** you want for values
3) Tick **Permanent**
4) **OK**

### What this does (so you know what to expect)
- Newly placed parts will use these colours.
- If a library update keeps forcing yellow, it’s because the designator/comment is using **default/system colours** — this sets those defaults.

**Single question:** do you want *values* to be yellow as well, or keep **designators yellow** and **values white/cyan**?

[M71] ME (2026-03-01 21:55):
So it must be locked in the part 

[M72] AI (2026-03-01 21:55):
Not necessarily “locked” — what you’re seeing is usually **one of two things**:

### 1) It’s using **system/default colours**
If the designator/comment text in the symbol is set to **Use System Color / Default**, then every library reload will snap back to whatever the defaults are (like yellow). That’s *not* locked; it’s just “inherits defaults”.

**How to tell/fix (SCHLIB):**
- Select the **Designator** (or **Comment**) text object *in the symbol*  
- In **Properties**, look for **Use System Color / Use Default**  
  - If it’s ON → turn it OFF, then set your colour manually.

### 2) The text primitive is actually **locked**
Less common, but possible after import.
- Select the text primitive (Designator/Comment) and check **Locked** in Properties. Turn it off.

### What you should do next (quick, decisive)
Since you already found **Preferences → Schematic → Defaults**, you’ve set the *global* behaviour. Now to confirm whether the part itself is overriding:

1) Open the symbol in **SCHLIB**
2) Try to **select the Designator text** (`R?`) or **Comment** (`=Comment`)
   - If you can’t see them, turn on special strings (View config) or place them.
3) When selected, check if **Use System Color** is enabled.

**Single question:** in the SCHLIB for one of these parts, can you actually see `R?` or `=Comment` on the symbol drawing (yes/no)?

[M73] ME (2026-03-01 21:57):
[image]
But it won’t show me in the part 
[attached file: IMG_1EB20D5F-EEC0-4293-B910-2B53FA7E433B.jpeg]

[M74] AI (2026-03-01 21:57):
I see what’s happening: in your **SCHLIB** the “4k87” you’re looking at is being drawn as the **component’s Comment parameter display**, but you **don’t have separate selectable text objects (Designator/Comment primitives) placed on the symbol** — so you can’t click/format them “in the part”.

In other words: you’re editing the *component*, not the *text primitives*, because they don’t exist (or they’re hidden).

### Fix (do it once per symbol template)
You need to **place** the two special strings onto the symbol:

## 1) Place the Designator + Comment onto the SCHLIB symbol
In the SCHLIB editor:

1. **Place → Text String → Special String**
2. In the entry box, **type** `=Designator` → place it near the symbol body
3. Repeat: **Place → Text String → Special String**
4. Type `=Comment` → place it where you want the value

Now you’ll see `R?` and the value placeholder (driven by Comment) as real, selectable text.

## 2) Make them selectable + set colour/font
- Click the placed `R?` text → **Properties → Color / Font / Size**
- Click the placed `=Comment` text → **Properties → Color / Font / Size**
- If you want them to ignore global defaults, turn off **Use system/default color** (if present)

## 3) If you *still* can’t see them after placing
Press **L** (View Configuration) and ensure **Special Strings** are enabled/visible.

---

### Quick sanity check from your screenshot
Your Properties panel is on **Component**, which confirms you haven’t selected a text primitive yet. After you place `=Designator`, clicking it should change the Properties header to **Text**.

**Do you see “Place” on the top menu in the SCHLIB editor right now?** If yes, go to it — do you have **Text String** available?

[M75] ME (2026-03-01 21:58):
[image]
What text?
[attached file: IMG_A1C5D654-AE45-4578-BEAB-58A17C17A2EC.jpeg]

[M76] AI (2026-03-01 21:58):
That’s **not** the component symbol text — you’ve selected a **sheet/template special string text** (things like `=Drawn_By`, `=Checked_By`, etc.). That’s why the dropdown only shows title-block fields.

You need to be editing the **SCHLIB symbol**, and place **component special strings** (`=Designator`, `=Comment`) onto the symbol.

## Do this to get the right “text”
### 1) Switch to the SCHLIB tab
At the top you should have a tab like **…Updated.SCHLIB**. Click that so you’re definitely in the **library editor**, not the sheet.

### 2) Select the symbol (not the title block)
Click the resistor/cap symbol body in the SCHLIB editor window (you should see the component box, pins, etc.).

### 3) Place the correct special string
Use:
- **Place → Text String → Special String**
Then **type** (don’t look for it in the list):
- `=Designator`  (for R?, C?, U?)
and place it.
Repeat with:
- `=Comment` (for the value)

If you don’t see “Special String” in the Place menu:
- Use the top **Search** bar and run the command **“Special String”** (this time it’s fine) and it will start the placement tool.

### 4) Confirm you’ve got the right thing
When you click the placed `R?` text, the Properties panel should show something like **Text** with content `=Designator` (not `=Drawn_By` etc.).

**Single check:** are you currently on a **SchDoc sheet** (title block visible), or on the **.SCHLIB** tab?

[M77] ME (2026-03-02 08:01):
[image]
I can’t turn off the numbers of these pins??
[attached file: IMG_D7799F4A-3747-49D2-90A1-7F50D3A71B99.jpeg]

[M78] AI (2026-03-02 08:02):
Those big **1** and **2** aren’t “pin numbers you can’t turn off” — they’re the **Pin Designators display** in the SCHLIB editor, and you’ve got **Show Pin Designators** enabled (you even had that ticked earlier in your Preferences screenshot).

### Turn them off (global)
1) **DXP → Preferences**
2) **Schematic → Graphical Editing**
3) Untick **Show Pin Designators**
4) **Apply / OK**

### Or turn them off just for viewing (quick toggle)
In the SCHLIB editor:
- Press **L** (View Configuration) and look for a checkbox like **Show Pin Designators** / **Pin Designators** and untick.

If it still shows after unticking, you’re probably editing a **Pin** object and it’s in a display mode — but 99% of the time it’s that **Show Pin Designators** preference.

**One check:** after you untick it, do the “1” and “2” disappear immediately in the SCHLIB view?

[M79] ME (2026-03-02 08:03):
They are still there. I want to see designators in ic some turning them off is t good 

[M80] AI (2026-03-02 08:04):
Got it — you want **IC pin numbers visible**, but you *don’t* want these huge “1 / 2” on simple 2-pin parts (res/cap). So don’t use the global toggle; instead change the **pin objects in this symbol**.

Those big numbers are coming from the **Pin’s “Designator” text size/style** (in the SCHLIB). You can make them tiny or hide them **per pin**, while still leaving IC pin designators on globally.

## Fix it per symbol (recommended)
### 1) Select the pins in the SCHLIB
- Click pin “1”
- Shift-click pin “2” (or box-select both)

### 2) Edit pin display settings
In the **Properties** panel (it should say **Pin**):
- Find **Designator** / **Show Designator** (wording varies)
  - Either **untick Show Designator** (per pin), **or**
  - Set the **Designator text size** to something small (e.g. 50–60 mil equivalent, whatever matches your library)
- Also check **Name** if it’s showing (not relevant here)

### 3) Save + update
- Save the SCHLIB
- Update schematic from libraries

### Quick “why it didn’t go away”
The **Preferences → Show Pin Designators** affects whether Altium displays them at all, but in SCHLIB some pins can still show because the symbol has them configured very prominently (and/or you’re in a mode showing pin info).

---

### One question (single, so we hit the exact control):
When you click on the “1” number itself, does the **Properties** panel header change to **Pin**? If yes, you’re in the right place — tell me if you can see a checkbox like **Show Designator**.

[M81] ME (2026-03-02 08:11):
[image]
[image]
On this part I can easily turn them on and off. But it f I copy it over to the problem part, I can no longer toggle them and they are locked on. It’s very tried reading then from scratch and still unable to hide the numbers 
[attached file: IMG_37041284-0F28-485D-8D64-3825197B7762.jpeg]
[attached file: IMG_FB2D1D12-F4D5-4ADD-A919-77773CFA0F52.jpeg]

[M82] AI (2026-03-02 08:11):
Yep — that difference (works on one symbol, “locked on” on the imported/problem symbol) almost always means the *numbers you’re seeing are not coming from the same mechanism*.

On the “good” symbol, the **pin designators are being drawn by the pin object** (so you can toggle/format them in Pin properties).

On the “problem” symbol, those big “1 / 2” are usually **plain Text primitives** that were imported (or generated) and happen to sit at the pin ends — so they *look* like pin numbers, but they’re just text, and the pin’s own designator display toggle doesn’t affect them.

### Do this to prove it (and fix it)
#### 1) Click the “1” itself and watch the Properties header
- If Properties says **Pin** → it’s real pin designator.
- If Properties says **Text** → it’s fake/imported text.

You only need to check **one** of the numbers.

#### 2) If it’s **Text** (most likely)
- Delete those text objects (select “1”, Delete; select “2”, Delete).
- Then decide what you want:
  - If you *never* want pin numbers on passives: leave them off (don’t enable pin designators globally).
  - If you want optional display: use the real pin display (next step).

#### 3) Recreate using real pins (so the toggle works)
On the problem symbol:
1. Select a pin (Properties shows **Pin**).
2. Make sure it has **Designator = 1** / **2** etc.
3. Then the show/hide is controlled by:
   - your **Show Pin Designators** preference, **and/or**
   - the pin’s own display settings (font/size under **Font Settings → Designator**).

#### 4) If it’s real pins but still “stuck on”
Then it’s usually because the **SCHLIB is set to always show designators for pins** via Defaults:
- **DXP → Preferences → Schematic → Defaults → Pin**
- Look for a setting that forces **Pin Designator visibility** (or designator font size = huge) and make it sane.

---

### One single question (decisive)
When you click directly on the big **“1”** on the *problem* symbol, does the Properties panel title say **Text** or **Pin**?

[M83] ME (2026-03-02 08:12):
[image]
I can’t, but it’s def part of the pin 
[attached file: IMG_DA6E82DD-AE0C-4E34-80DA-20172D5984C1.jpeg]

[M84] AI (2026-03-02 08:12):
Yep — that tells us a lot: if you **can’t select the “1” as Text**, and it behaves like it’s part of the pin, then it *is* the pin designator — but it’s being shown by the **SCHLIB editor view**, not by a per-pin toggle you can easily hit on that symbol.

In AD26, there are **two different “pin number” displays** in SCHLIB:

1) **Pin Designator display** (what you want ON for ICs)  
2) **Pin “hotspot markers / pin end labels” view** that can be forced on in the SCHLIB view/config.

Let’s fix it **per symbol** so passives don’t show huge numbers, while ICs still do.

## The real fix: make the pin designator font tiny for this symbol’s pins
You’re already in the **Pin** properties (good).

1) Click **Pin 1** (or the pin end)
2) In Properties (right), scroll to **Font Settings → Designator**
3) Tick **Custom Settings**
4) Set the font size small (start with **6** or **8**)  
   - That will make the “1” and “2” unobtrusive (effectively “off” visually)
5) Repeat for **Pin 2** (or multi-select both pins first in the pins list and apply once)

This keeps global “Show pin designators” enabled for ICs, but makes passives quiet.

### If you want them truly hidden (not just small)
In the same **Pin → Font Settings → Designator** area, look for either:
- **Visible** / **Show Designator** checkbox, or
- A **colour** selector (set it to match background), or
- A “**No symbol**” / “**Inside/Outside**” display option tied to designator (some libs expose it differently)

But **font size** is the most reliable lever across versions.

## One extra gotcha: you may be editing *only one pin*
To do both at once:
- In the **Pins list** (right panel where it shows Pin 1 / Pin 2), click Pin 1 then **Shift-click** Pin 2, then change **Designator font** once.

---

### Single check (so I don’t mislead you)
In your Pin Properties panel, do you see **Font Settings → Designator → Custom Settings** like in your earlier screenshot? If yes, set it small and you’re done. If no, tell me what the lowest section title you can see is (“Symbols”, “Font Settings”, etc.) and I’ll route you to it.

[M85] ME (2026-03-02 08:14):
[image]
I think it’s because it’s saying it’s part of part 1 of the symbol 
[attached file: IMG_90882011-2C4B-40AF-906F-C2D407E00756.jpeg]

[M86] AI (2026-03-02 08:14):
You’re very close, but **“Part 1” isn’t the cause**. The reason you’re seeing **0, 3, 4** etc is: those are **pin designators on extra pins that exist in the symbol**, not “ghost text”.

So the fix is to clean the symbol so the *resistor* only has pins **1 and 2**, and/or make the extra pins **hidden/invisible**.

Here’s the fastest way to do that properly:

## 1) Confirm: you have extra pins in the SCHLIB symbol
In your screenshot you’re on **Component** properties. Click the **Pins** tab (top of the Properties panel, next to General).  
You should see a list of pins — I’m expecting **Pin 1, Pin 2, Pin 0, Pin 3, Pin 4** etc.

## 2) Delete the unwanted pins (recommended)
In that **Pins list**:
1. Select the unwanted ones (e.g. **Pin 0, Pin 3, Pin 4**)
2. Press **Delete**
3. Leave only **Pin 1** and **Pin 2**

This is the cleanest fix because you’ll never fight it again.

## 3) If you can’t delete them (rare, but possible)
Then hide them:
1. Click one of the unwanted pins in the list (e.g. Pin 3)
2. In the Pin properties, look for **Visible** / **Hidden** / **Show** (sometimes a small “eye” style control)
3. Turn it off
4. Repeat for Pin 0/4/etc

## 4) Save + update
Save the SCHLIB, then update the schematic from libraries.

---

### Why copying from a “good” symbol doesn’t help
If you copy pins/text across but the destination symbol still contains those extra pins, the SCHLIB view will keep showing their designators.

**Single question:** when you click the **Pins** tab, how many pins does it list for this resistor symbol?

[M87] ME (2026-03-02 08:19):
[image]
[attached file: IMG_3F6DCAD3-F63D-4BC0-8F23-CF6DF37ED66D.jpeg]

[M88] AI (2026-03-02 08:19):
Great — that proves it: the symbol **only has Pin 1 and Pin 2**. So the extra “0 / 3 / 4” you saw earlier were from a *different symbol* or a different object type — but for this problem case the “1” and “2” are definitely the **pin designators**.

So why can’t you “toggle them off” on this symbol?

Because in the SCHLIB editor, pin designators are controlled by **either**:
- the **global “Show Pin Designators” preference** (you said turning it off globally is no good), **or**
- the **pin’s own font/display settings** (per pin), which is what we’ll use.

## Do this: make them effectively “off” for passives by shrinking them
1) Click **Pin 1** in that Pins list.
2) Now click the little **wrench / edit** button at the bottom right of that pins list (or just click the pin on the canvas) so Properties switches to **Pin**.
3) Scroll to **Font Settings → Designator**.
4) Tick **Custom Settings**.
5) Set the font size small (try **6**).  
6) Repeat for **Pin 2** (or multi-select both pins first and apply once).

Now ICs can still show pin numbers (they’ll have sensible font sizes), but resistors/caps won’t have giant numbers even when pin designators are globally enabled.

### If you want them totally hidden (not just small)
Some builds expose a per-pin visibility flag:
- In **Pin** properties, look for **Show Designator** / **Visible** next to designator. If present, untick it for Pin 1 & Pin 2.

---

### One quick question (so I can direct you to the exact button you have)
When you click **Pin 1** in the list, does the Properties header change from **Component** to **Pin** automatically, or does it stay on Component?

[M89] ME (2026-03-02 09:21):
Is there a big table view of the library I can use to edit?

[M90] AI (2026-03-02 09:21):
Yes — in Altium you can edit library content in a spreadsheet-style way, but it depends **what you want to edit**.

## 1) Components + parameters (Design Item ID, Value/Comment, MPN, etc.)
Use the **SCH List** panel (it’s the closest to “big table”):

1. Open your SCHLIB (or SchDoc)
2. **Panels → SCH List**
3. Set the list to show **Components**
4. You can **sort/filter**, and bulk-edit parameter cells (esp. if you enable in-place editing)

This is great for tidying imported parameters quickly.

## 2) Pins (pin numbers, names, electrical type) in a table
For symbols, use the **Pins tab** in the **Properties** panel as your “table”:
- Select the component in SCHLIB
- Go **Properties → Pins**
- That list is your editable table for pin Designator/Name/etc. (bulk select rows)

Not a full spreadsheet UI, but it’s the official bulk pin editor.

## 3) Footprints / PCB libraries
For PCBLIB there’s a more “table” feel via:
- **PCB Library panel** (components list)
- And you can use **SCH List** / reports for pads aren’t usually table-edited like parameters.

---

### Quick aim check (one question)
Do you want a table to edit **component parameters** (values, IDs, MPNs), or a table to edit **pin properties** (numbers/names/types)?

[M91] ME (2026-03-02 09:23):
I want to view manufacturer info etc 

[M92] AI (2026-03-02 09:23):
Yep — for manufacturer / supplier fields the best “big table” views are:

## Option A: **SCH List** panel (fastest, spreadsheet-ish)
1) Open the **schematic** (SchDoc) that has the parts placed (best), or open the SCHLIB if you must.
2) **Panels → SCH List**
3) Set the list to **Components**
4) Right-click the column header area → **Choose Columns…**
5) Tick the fields you care about (typical ones):
- **Manufacturer**
- **Manufacturer Part Number (MPN)**
- **Supplier / Supplier Part Number**
- **Description**
- Any custom params your library uses

Now you can sort/filter and spot missing data quickly.

> Why schematic is better: SCH List shows the *real placed parts + all parameters*, including ones coming from managed content or DB links.

## Option B: **Components panel** (if you’re on Concord Pro / managed content)
If your parts are coming from Concord/365:
1) **Panels → Components**
2) Use the filters/search
3) Switch to a list view and add columns (where available)

Good for browsing managed components, less nice for bulk checking a design.

## Option C: Generate a report (if you want an export)
From the schematic/project:
- **Reports → Bill of Materials**
- Configure columns to include Manufacturer/MPN/etc
- Export to Excel/CSV

That’s the ultimate “big table” for audit/cleanup.

### One question
Are your parts **managed** (Concord/365) or **local libraries**? (Just “managed” or “local”.) This changes whether the manufacturer info lives in the component item, or as plain schematic parameters.

[M93] ME (2026-03-02 09:26):
I need to tidy up the library and add all missing attributes. Trying to find the quickest way for this 

[M94] AI (2026-03-02 09:26):
Fastest way is to **work from a BOM-style table**, fill the gaps in bulk, then push the cleaned parameters back into the library (or into managed components). Don’t try to click parts one-by-one.

## Step 1: Make a “gap finder” table from the schematic (quickest)
1) Open a schematic that contains *all/most* of the parts you care about.
2) **Reports → Bill of Materials**
3) In the BOM setup, include these columns (minimum viable set):
- **Design Item ID / Library Ref**
- **Comment (Value)**
- **Description**
- **Manufacturer**
- **Manufacturer Part Number (MPN)**
- **Supplier 1 + Supplier Part No** (if you use it)
- **Footprint**
4) Export to **CSV/Excel**.

Now you’ve got a single sheet where blanks jump out.

## Step 2: Fill missing attributes in bulk (one pass)
In Excel:
- Filter each column for blanks (Manufacturer blank, MPN blank, etc.)
- Fill/standardise naming (e.g., “Yageo” vs “Yageo Corp.”)
- Keep a consistent parameter naming scheme (exact spelling matters).

## Step 3: Push back efficiently (depends on library type)
### If you’re using **local SCHLIB** parts with parameters
Use the **SCH List** panel as your “bulk editor”:
1) Open the **SCHLIB**
2) **Panels → SCH List**
3) Filter to the parts you’re editing
4) Bulk-add parameters:
   - Select multiple rows → add parameter column → paste values down

(Where it won’t let you true-spreadsheet edit, you can still do a lot faster than opening each component.)

### If you’re using **managed components (Concord/365)**
Best practice is:
- Edit the component’s **Parameters** in the managed item (Components panel / Explorer)
- Then **release** a new revision.
(Doing it locally in a SCHLIB won’t stick if the source of truth is managed.)

---

## The real accelerator: decide the “mandatory attribute set”
For most teams a good default is:
- Manufacturer, MPN
- Description
- Value/Comment (normalised)
- Package/Footprint name
- Voltage/Power/Tolerance (where relevant)
- Lifecycle / RoHS (if you track it)
- Supplier + Supplier PN (optional, but great)

### One question (so I give you the exact fastest workflow):
Are these parts coming from **local libraries** (SCHLIB/DBLib) or **managed Concord/365 components**?

[M95] ME (2026-03-02 09:38):
[image]
Ok, I’ve derived the bom. Now export to csv?
[attached file: IMG_3486052C-D122-4E27-9959-9F3780F60696.jpeg]

[M96] AI (2026-03-02 09:38):
Yep — from that **BOM.BomDoc** view you can export.

### Export BOM to CSV (AD26)
1) In the BOM document, go **File → Export → CSV**  
   (sometimes it’s **File → Save As…** and you choose **CSV**)
2) Pick location + filename → **Save**

### If you don’t see “Export CSV” in File
Use the BOM panel itself:
- Right-click anywhere in the BOM table → look for **Export / Save As / Export to CSV**
- Or use **Reports → Bill of Materials** from the main project and choose **CSV** as the output.

### Quick sanity before you export
Hit **Columns** (right panel) and make sure you’ve included the fields you need (e.g. Manufacturer, MPN, Supplier PN, Description). Then export.

**One question:** do you want the CSV grouped (like your current “Group by” view), or **one line per placed component** (ungrouped)?

[M97] ME (2026-03-02 09:46):
[image]
Can’t I change it in the bin?
[attached file: IMG_1BEFBFD4-D11A-4576-8CA4-9B2DE8B8523A.jpeg]

[M98] AI (2026-03-02 09:46):
You *can* change things in the **BOM** view, but it depends what you mean by “change it”:

### What you **can** do in that BOM.BomDoc
- Add **Manufacturer Part** solutions (MPN, manufacturer) per line item (that **Add Solution** button at the bottom).
- Choose a preferred supplier / part.
- It’s basically a **supply-chain assignment tool**.

That will help you get a clean BOM, but it **doesn’t automatically write those attributes back into your SCHLIB symbols** unless you’re using managed components / a workflow that links “solutions” back to the component item.

### What you **can’t reliably do** there (for local libs)
- Bulk-edit your *library parameters* (Manufacturer, MPN, etc.) in the SCHLIB directly from the BOM doc.
- The BOM is derived data; it’s not the source-of-truth editor for local libraries.

## Fastest workflow (given what you’re doing)
### A) Use BOM doc to identify gaps + assign MPNs quickly
1) In BOM.BomDoc, click an item with the red warning
2) Click **Add Solution → Manufacturer Part**
3) Add the MPN/manufacturer for that line

### B) Then push those back into the library (source of truth)
- If you’re **local SCHLIB**: open the part and add parameters there (or use SCH List panel for batch).
- If you’re **managed (Concord/365)**: add the manufacturer part to the managed component and release a revision.

### The tell in your screenshot
Your “Name” column showing `=Value` for many rows suggests lots of parts don’t have clean Value/Comment parameters yet — that’s better fixed at schematic/library level, not only in BOM.

**Single question:** are these components **managed** (Concord/365 components), or are they **local SCHLIB parts**? That decides whether edits in this BOM tool can be promoted back automatically.

[M99] ME (2026-03-02 09:53):
So what’s the quickest way to change a load of bom oarameters

[M100] AI (2026-03-02 09:53):
Quickest depends on where your “source of truth” is. For **local SCHLIB / schematic parameters** (what your screenshots look like), the fastest is:

## Fastest bulk-edit method: **SCH List panel + paste from Excel**
### 1) Work in the **schematic (SchDoc)**, not the BOM doc
1. Open the SchDoc that contains the parts.
2. **Panels → SCH List**
3. Set mode to **Components**.
4. Filter down to what you’re fixing (e.g., all caps, all resistors, or items where MPN is blank).

### 2) Add the columns you need
In SCH List:
- Right-click header → **Choose Columns / Select Columns**
- Add: **Manufacturer**, **MPN**, **SupplierPN**, **Description**, etc.

### 3) Fill in Excel, paste back in one hit
1. Copy the SCH List rows into Excel (or export BOM to CSV, edit there).
2. Fill missing cells using filters.
3. Copy the completed column(s) back and **paste** into the SCH List column (Altium will paste down rows).

This is the “100 parts in 5 minutes” approach.

## If you need it to update the **library**, not just this design
After fixing in the schematic:
- Use **Tools → Update Components From Schematic** / **Update Libraries** workflow (depends on your setup), or
- Open the SCHLIB and do the same SCH List trick there if supported (less pleasant than schematic, but works).

## Managed (Concord/365) exception
If the parts are managed: fastest is to fix manufacturer parts in **Components/Explorer** and release revisions (BOM tool helps assign, but the managed item is the truth).

**One question:** do you need the changes to apply to **this project only**, or do you need them to become the **library standard** for future projects?

[M101] ME (2026-03-02 09:58):
[image]
It doesn’t show the value 
[attached file: IMG_2F08D1D3-CE5F-42F2-A12B-0D0D622D61E5.jpeg]

[M102] AI (2026-03-02 09:58):
You’re *in the right tool* (SCH List), but you’re currently showing mostly **component meta-columns**. The “Value” you care about is the component’s **Comment** (or a parameter called **Value**), and you need to add that column.

### Do this in SCH List
1) **Right-click the column headers** (top row) → **Choose Columns…** (or *Select Columns…*)
2) In the list, enable:
- **Comment** (this is typically the schematic “value”)
- and/or **Value** (if your library uses a parameter literally named Value)
- **Manufacturer**
- **Manufacturer Part Number** (or MPN)
- any supplier fields you use
3) OK.

Now you’ll see the value column.

### Why yours looks blank / “=Value”
I can already see lots of entries where **Comment** is literally `=Value` — that means the component comment is a **special string** pointing at a parameter called Value, but that parameter isn’t populated (or not present), so it can’t resolve.

Two ways to fix that, depending on what you want as your standard:

- **If you want Comment to just be the value** (e.g. “100n”, “4k7”): change Comment from `=Value` to the actual text (bulk edit).
- **If you want Comment to reference a Value parameter**: then you must add/populate a **Value** parameter for each component.

### Quick next step (single action)
Add the **Comment** column first and tell me: does it show real values, or does it show `=Value` everywhere?

[M103] ME (2026-03-02 10:02):
Can concord pro 364 help with this?

[M104] AI (2026-03-02 10:02):
Yes — **Concord Pro / Altium 365 can help a lot**, *if* you move your parts to **managed components** and make the managed component the **single source of truth** for parameters + manufacturer parts.

What it helps with (practically):

## What Concord/365 is good at
- **Manufacturer Parts (“solutions”) live with the component**  
  You add MPN + manufacturer once, and every design using that managed component inherits it.
- **Parameter governance**  
  You can define required parameters (Manufacturer, MPN, Description, Lifecycle, etc.) and keep them consistent.
- **Avoids “local override drift”**  
  No more one schematic having `=Value` weirdness while another doesn’t — because the component definition is central.
- **Supply chain checks**  
  Missing manufacturer part warnings are exactly what you’re seeing in BomDoc — managed components make it natural to fix at the source.

## What it won’t magically do
- It won’t auto-invent missing MPNs. You still have to populate them (but you’ll do it **once per component**, not once per project).

## The quickest Concord/365 workflow for your cleanup
1) Use your **BOM.BomDoc** as the to-do list: red warnings = missing manufacturer parts.
2) For each unique component (not each designator), add **Manufacturer Part** once (MPN + manufacturer).
3) Release/update the managed component so the whole library is fixed.

If your current parts are **local SCHLIB** only, the step is:
- **Migrate/convert** them to managed components (batch possible), then do the cleanup there.

### One question (so I give you the right “next clicks”)
Are your parts **already** managed components (from Concord/365), or are they still **local SCHLIB components** that you place from files?

[M105] ME (2026-03-02 16:46):
Why do people use j ref as connector. We used to use pl and sk. Which I think is good as you know what it is better

[M106] AI (2026-03-02 16:46):
People use **J** (and **P**) mostly because it’s a **widely adopted convention** in generic electronics CAD libraries/BOM tooling:

- **J** = “jack/connector” (catch-all for any connector: headers, D-subs, board-to-board, sockets, etc.)
- **P** = “plug” (sometimes used for cable-side or male)
- Many Altium/IPC-style libraries default to **J** so you don’t have to decide “is this a plug, socket, header, testpoint, etc.” every time.

Why teams still like **PL/SK** (your way)
- It’s semantically rich: you instantly know **plug vs socket**.
- Helpful for harnesses/cable assemblies and for humans scanning a schematic.

Why some teams avoid PL/SK
- Ambiguity with **board-to-board** where “plug/socket” isn’t obvious or flips depending on the mating part.
- Mixed ecosystems: suppliers call things “receptacle/header/plug/socket” inconsistently.
- Library reuse: a generic “CONN_2x10” symbol used in many contexts doesn’t want a gender baked into the prefix.

A solid compromise many teams use:
- **J** for *any connector on the PCB* (board connector)
- Put **gender/role in parameters**: `Gender=Plug/Socket`, `Mating=...`, `ConnectorType=Header/Receptacle`, `Mount=TH/SMT`, etc.
- Or keep **PL/SK** but enforce a rule: *SK = PCB receptacle, PL = cable plug* (or vice versa) so it’s consistent.

If you tell me your typical cases (e.g., board-to-board mezzanine, cable harness, test sockets), I can suggest a prefix rule-set that stays consistent and doesn’t cause ECO renumber pain.

[M107] ME (2026-03-02 16:48):
Usually wire to board 

[M108] AI (2026-03-02 16:48):
For **wire-to-board**, your instinct is right: **PL/SK can be genuinely useful** because the mating roles are clearer than on board-to-board.

A clean, low-ambiguity convention many teams use is:

## Recommended wire-to-board naming
### On the PCB (the connector mounted to the board)
- **J** *or* **SK** (pick one and standardise)
  - **SK** works well if you want “board receptacle/socket” to be obvious.

### On the cable/harness side (if you document it)
- **PL** (plug)

So you’d have:
- PCB: **SK1** (or **J1**)  
- Harness: **PL1** (mates with SK1)

## Why some teams still use J on PCB even for wire-to-board
Because the PCB has *a connector*, full stop — and the “plug/socket” depends on mating hardware and vendor wording. They push “male/female” into:
- a **Gender** parameter
- a **MatingConnector** parameter
- a **Harness ref** (e.g., HARN1/PL1)

## If you want maximum clarity without fights
Use **J** for all board connectors *but* add a required parameter set:
- `Role = BoardConn`
- `Mate = PLxx`
- `Gender = Receptacle/PinHeader`
- `WireSide = Yes/No`

That gives you PL/SK clarity in the data model, while keeping the schematic prefix simple.

**Single question:** do you ever put the *harness/cable* in Altium as a separate schematic (or is it only the PCB schematic)?

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] ME (2026-03-01 21:54):
How do I change it globally 

[A2] AI (2026-03-01 21:54):
If you want it **global** (i.e., every designator in every schematic comes out the way you want, and stays that way), you need to set it at the **library + default formatting** level, not by tweaking instances.

There are two “global” knobs—pick the one that matches what you mean:

## Global across all designs that use your libraries (recommended)
### 1) Fix it in the SCHLIB templates
For each symbol style (R/C/U etc.), ensure the symbol actually *contains*:
- a `=Designator` special string
- a `=Comment` (value) special string (optional)

Then set the colour/size on those text objects in the **SCHLIB** and save.

Now every time you place or update from libraries, it will be consistent.

**Fastest way if you have loads of symbols:**
- Open one “good” resistor symbol that looks right
- Copy the `=Designator` text object
- Paste it into the other resistor symbols (repeat per family)

(Yes, it’s annoying once, but it’s the only way that survives updates reliably.)

## Global just for how Altium *displays* designators (system default)
This changes the default “system colour” used when text is set to **Use System Color**:

1) **DXP → Preferences**
2) Go to **Schematic → Colors** (or **Schematic → System Colors** depending on your install)
3) Set **Component Designators** = **Yellow** (or whatever)
4) Apply/OK

This affects display, but **won’t help** if the designator string doesn’t exist in the symbol and you want per-symbol formatting to persist.

---

### Which “global” do you mean?
Just answer with one word:
- **Display** (same colour everywhere, regardless of library content), or
- **Library** (b

[A3] ME (2026-03-01 21:55):
[image]
It’s already in what I want it to be 
[attached file: IMG_42899B12-1379-4C68-A723-3503CD945756.jpeg]

[A4] AI (2026-03-01 21:55):
Yep — this screenshot shows your **Designator default is already
