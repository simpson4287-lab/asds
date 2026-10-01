# Net rename in Altium
Date (UTC): 2026-03-05 18:54
Conversation ID: 69a9d12e-449c-8385-8fa0-914dafb54847
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-05 18:53):
[image]
Mice changed this net name in schematic but not coming through to PCB should be 1v8
[attached file: IMG_4D9A0F4B-59B0-4BB1-87CA-45779C202B82.jpeg]

[M2] AI (2026-03-05 18:54):
Yep — in Altium a net rename **only reaches the PCB via a compiled project + an ECO**. If you’ve just edited a label/port with the mouse, it’s easy to end up with a *visual* rename that doesn’t actually drive the netlist update (or the PCB is preserving the old name).

Here’s the quickest “make it obey” sequence, plus the common gotchas.

## 1) Confirm the schematic net is *really* 1V8
On the schematic:
- Click the **wire** that should be 1V8 (not the text).
- Panels → **Properties** (or hover) and check the **Net** name shown there.
  - If it still shows `+3V3D`, your label/port isn’t actually connected (off-grid, tiny gap, label on wrong segment, etc.).
- If you renamed a **Power Port**, make sure you changed the **Power Port name**, not just a text string.

Then:
- **Project → Compile PCB Project** (fix any compile warnings related to nets).

## 2) Push the rename into PCB via ECO
From the schematic:
- **Design → Update PCB Document…**
- In the **Engineering Change Order (ECO)** window:
  - You should see something like **Change Net Name** / **Remove Net +3V3D** / **Add Net 1V8** / **Reassign primitives**.
- **Execute Changes**.

If the ECO does **not** include a net rename, Altium still thinks the schematic netlist hasn’t changed → go back to step 1 (it’s usually a connectivity/label issue).

## 3) If ECO runs but the pad still shows +3V3D (your screenshot)
That usually means one of these:

### A) The pad is actually connected to +3V3D somewhere on the PCB
In PCB:
- Ctrl+click the `+3V3D` net name (or use **Highlight Net**) and see what lights up.
- Look for:
  - A **polygon pour** assigned to +3V3D touching that pad
  - A **power plane / split plane region** assigned to +3V3D
  - A **net tie** or accidental short/track

If it’s an **internal plane**, you must change the **plane region net assignment** (ECO should do it, but only if the netlist update is correct and the region isn’t locked).

### B) “Preserve existing net names” / PCB-side rename protection
If someone renamed nets in PCB earlier:
- PCB: **Design → Netlist Options** (or in the ECO/options area depending on version)
- Look for anything like **Preserve existing net names** / **Do not update net names** and disable it, then re-run **Update PCB**.

### C) Primitives locked / coming from a reused snippet block weirdness
If you’re deep in reuse blocks / multi-channel merges (which you are):
- Check the pad/region isn’t **Locked** (Properties panel).
- Re-run **Update PCB**.
- If the project is behaving “stale”, do:
  - **Project → Compile**
  - **Project → Validate PCB Project**
  - Then **Design → Update PCB**

## 4) Fast sanity test
In PCB, open **Panels → PCB → Nets**:
- Do you see **1V8** listed?
- Does **+3V3D** still exist?
  - If both exist, you likely have two separate nets and something is still driving +3V3D (plane/polygon/short).
  - If only +3V3D exists, the schematic rename didn’t actually take.

---

If you tell me **whether 1V8 appears in the PCB Nets list** and whether this pad is on an **internal plane layer** or just normal signal layers, I can tell you which branch above is the real cause in about one step.

[M3] ME (2026-03-05 18:56):
Compiler says net name alteeady exists 

[M4] AI (2026-03-05 18:57):
That compiler message is actually useful: it means **Altium already has a net called `1V8` somewhere in the compiled design**, and your rename is trying to create **another** `1V8` net (i.e., it thinks it’s a *different* connectivity island than the existing `1V8`).

So the question becomes: **do you want these two islands to be the same net, or not?**

## What’s really happening
In Altium, net names are global in the compiled project. If you rename `+3V3D` → `1V8` on *one* island, but there’s already a `1V8` net elsewhere that Altium considers *not connected* to this island, the compiler throws “net name already exists” because it can’t have two separate nets with the same name.

This is nearly always caused by one of:
- You already have a **Power Port** named `1V8` elsewhere.
- There’s a **Net Label** / **Port** named `1V8` elsewhere.
- You’ve got **two different net identifiers** (Net Label vs Power Port vs Port) and they aren’t actually joining how you think (sheet symbols / harness / off-grid / wrong port I/O type / not wired).

## Step 1 — Find where `1V8` already exists (fast)
On the schematic editor:

1) **Panels → Navigator**
2) Set filter to **Nets**
3) Search `1V8`
4) Click each result and jump to it.

Alternative:
- **Panels → PCB / SCH → Messages** sometimes gives clickable references.
- **Edit → Find Text** for `1V8` (good for labels/ports/power ports).

You’re looking for *what object* defines it:
- **Power Port** named `1V8` (global)
- **Net Label** `1V8` (local to that sheet but global once compiled if connected via ports etc)
- **Port** `1V8` going through sheet symbols

## Step 2 — Decide what you want

### Case A: It SHOULD be the same 1V8 rail everywhere
Then you need to **make Altium see it as one connectivity**:

- Prefer using **Power Ports** for rails like 1V8 (cleanest):
  - Place a **Power Port** named `1V8` on this net *and remove/rename the old label*.
- Or if you’re using hierarchical ports:
  - Ensure the net is carried through properly:
    - Port name matches Sheet Symbol entry exactly
    - Port direction set sensibly (Passive is safest)
    - No off-grid gaps: wire endpoints actually touch ports/labels

Then:
- **Project → Compile**
- **Design → Update PCB Document**
- ECO should show reassigning primitives from `+3V3D` to `1V8`.

### Case B: It should NOT join the existing 1V8 (it’s a different local rail)
Then you must give it a unique name:
- `1V8_A`, `1V8_LOCAL`, `1V8D`, `1V8_IO`, etc.

(Altium won’t allow two separate nets both called `1V8`.)

## Step 3 — Common gotcha that causes “duplicate 1V8” even when you think it’s one net
**You changed visible text, not the net identifier.**

Example:
- A text string “1V8” near the wire ≠ a Net Label/Power Port that defines the net.
- Or the Net Label is sitting *near* the wire but not actually attached (microscopic gap / off grid).

Do this check:
- Click the **wire**, open **Properties**, confirm the **Net** field shows the intended name.

---

## Quick diagnostic (one question, no screenshots needed)
When you search `1V8` in **Navigator → Nets**, do you get:
1) **One result** (single net instance), or  
2) **Multiple results** across sheets?

If you tell me which, I’ll tell you the exact fix path (power-port merge vs hierarchy connectivity issue vs rename-unique).

[M5] ME (2026-03-05 20:04):
[image]
Can you view older versions of Reid win altium 
[attached file: IMG_F20D6DFC-015E-4D94-B7F1-EE5B8C05B148.jpeg]

[M6] AI (2026-03-05 20:04):
Yes — but it depends what you mean by “older versions”. In Altium there are **three** common places versions can live:

## 1) If the PCB/SCH is under version control (Git/SVN) or Altium 365
This is the clean “proper” way.

### Altium 365 (Workspace / managed project)
- **View → Panels → Storage Manager** (or **Explorer** panel depending on setup)
- Find your **project** → you should see **Versions / History / Revisions**
- You can open an older revision (read-only) and compare.

### Git/SVN (external VCS)
- Use your Git client (or SVN) to checkout an old commit / tag.
- Open that project folder in Altium.
- Altium itself won’t magically browse Git history unless you’re using the VCS integration — the history is in the repo.

If you tell me whether you’re on Altium 365 or local Git/SVN, I can point you to the exact panel/menu in your build.

## 2) If it’s **not** in version control: Altium’s *Local History*
Altium keeps automatic backups (“Local History”) of each file.

Try this:
- In the editor, click the tab for the file (e.g. `*.PcbDoc` or `*.SchDoc`)
- **File → History → Local History…** (wording varies slightly by version)
- You’ll get a list of timestamped snapshots you can open/restore.

Also check your disk folder:
- Altium creates `History` / `__Previews` / backup folders depending on settings.

## 3) If it’s been saved over: manual backups / `*.Bak` / autosave
If Local History is off (or purged), the only “older versions” will be:
- `*.SchDoc.Bak`, `*.PcbDoc.Bak`
- your own copied folders / zipped releases
- Windows Previous Versions (if File History / OneDrive versioning is on)

---

### Based on your screenshot
You’ve got a **Notes / History-looking panel on the left with timestamps and your username**. That strongly suggests you may already have some kind of **history/logging enabled** (possibly workspace history or local history viewer).

**Quick check:** is your project in an Altium 365 workspace (you see “Workspace Projects” / “Explorer” with server items), or is it a normal local folder project?

If it’s a workspace project, I’ll tell you where to click to get **full revision history** (and how to open old revs side-by-side). If it’s local-only, I’ll walk you through **Local History** + where the files are stored on disk.

[M7] ME (2026-03-05 20:05):
It’s on the 365 server

[M8] AI (2026-03-05 20:05):
Perfect — if it’s on **Altium 365 (Managed Project)** then yes: you can view (and open) older versions via the project **History / Revisions** in the Workspace panels.

### The clean way (recommended): open a previous **Project Version**
1) **View → Panels → Explorer** (sometimes called **Storage Manager** in some setups)
2) In Explorer, switch to your **Workspace** (top drop-down).
3) Go to **Projects** → find your project.
4) Open the **History / Versions** view (wording varies: *History*, *Versions*, or *Releases*).
5) You’ll see a timeline/list of **versions** with timestamps, user, comment.
6) Select the version you want → **Open** (usually opens as that revision / read-only).

What you get:
- You can inspect the old SCH/PCB exactly as it was at that version.
- Usually read-only unless you “make a new working copy” from it.

### If you want an older version of a **single file** (PcbDoc/SchDoc)
Sometimes easier:
1) Open the file (e.g. `RBL-0008-9.PcbDoc`)
2) **File → History** / **Show History** (or right-click the document tab if your build exposes it)
3) Choose an older revision → open/compare.

### Compare (so you can see what changed)
- Use Altium’s **Compare** (Diff) if available in your licensing/build:
  - In Explorer/History: pick two versions → **Compare**
  - Or open current + old and use a document compare tool.

### Practical tip for your net-name problem
If you suspect the `1V8` net already existed in an earlier revision and got introduced/duplicated:
- Open the **last known-good project version**
- Search for **1V8** in Navigator
- Then compare with the current version to find where the second `1V8` (or the rail rename) appeared.

---

If you tell me which panel you currently have on the left (Explorer vs something else) and your Altium build shows **“Explorer”** or **“Storage Manager”**, I’ll give you the exact click-path matching your UI labels.

[M9] ME (2026-03-05 20:32):
[image]
Why when I thicken this track it fails? 
[attached file: IMG_03B2AF54-950D-4294-98EA-F06AFA193A25.jpeg]

[M10] AI (2026-03-05 20:32):
From your screenshot I can see the cause. When you increase the width of that track it **violates the clearance to the nearby copper/polygon**, so Altium refuses the change.

The clues visible in your image:

- The **purple hatched area** is a **polygon pour**.
- Your track is currently passing **through a narrow gap between pads** and the polygon.
- When the track width increases, it **encroaches into the polygon clearance boundary**.
- DRC then blocks the edit (because *Online DRC* is active).

In short: **the route corridor is only just wide enough for the current track width.**

### What exactly is colliding
Likely one of these:

1. **Track-to-polygon clearance**
2. **Track-to-pad clearance**
3. **Track-to-via clearance**

Given the screenshot, #1 is most likely.

### Quick ways to confirm
Press:

**D → R → C**

to view the **Clearance Rule**, or:

**Right click → Violations → Show Violations**

Then try widening the track again and the exact violation will highlight.

### Fix options

**Option 1 — Move the track slightly**
Just shift the route a bit away from the polygon edge.

**Option 2 — Repour polygon**
Sometimes the polygon hasn’t updated.

```
T → G → A
```

Repour all polygons.

**Option 3 — Increase polygon clearance**
If appropriate:

```
Design → Rules → Clearance
```

Adjust the polygon rule.

**Option 4 — Pour over same net**
If that polygon is actually the **same net** as the track:

Polygon Properties → enable  
**"Pour over same net objects"**

Then clearance won't block it.

---

### One more thing I notice
The nets in your screenshot show names like:

```
NetP7_1
NetR10_1
```

That usually means the **nets aren’t being driven by the schematic anymore** (Altium has generated automatic net names). This could be related to the earlier **1V8 rename issue** you mentioned.

If you want, I can also show you a **very fast way to repair schematic ↔ PCB net linking**, because the autogenerated net names suggest the ECO sync might be broken.

[M11] ME (2026-03-05 20:33):
No that’s a 3d body 

[M12] AI (2026-03-05 20:33):
Got you — if that purple/hatched thing is a **3D Body**, then the “fails when I thicken” is *not* a copper clearance issue. In that case, the two most common reasons are:

## 1) You’re hitting a **routing width constraint** (rule-driven)
Altium won’t let you widen beyond what the active rules allow for that net/class/layer.

**Check:**
- Click the track → look in **Properties**:
  - Does it show **Width = (rule)** or is it locked to a specific value?
- Press **D, R** (Design → Rules) → look at **Routing → Width**
  - Find the rule that applies to that net/layer.
  - Check **Min / Preferred / Max**.
  - If your new width > **Max**, Altium will reject the edit.

**Fix:**
- Increase the **Max** (or create a higher-priority rule just for that net / region).
- Or use **Interactive Routing Width** and pick a width that’s allowed by the rule.

## 2) **Online DRC** is blocking because widening would violate **clearance to copper**
Even though the hatched object is a 3D body, there’s still plenty of copper nearby (pads / other tracks / pours). Widening the track can clip clearance to:
- the adjacent pad/via field (looks like a dense via/pad column in your pic),
- the big pad you’re routing into,
- or another track on the same layer.

**Fast prove-it test:**
- Temporarily disable Online DRC:
  - **Tools → Design Rule Check → Online** (toggle off), *or*
  - press **Shift + D** then choose **Online DRC Off** (depending on your keybinds/version).
- Now try widening.
  - If it works with Online DRC off → it’s definitely a clearance/width rule interaction.
  - Undo afterwards.

**Then identify the exact rule being broken:**
- After attempting the widen, look at the bottom bar / Messages panel for the violation name.
- Or run **Tools → Design Rule Check** and read the first violation entry — it will literally say which rule.

## 3) The track segment is part of an **interactive route** with “hugging” constraints
If you’re editing during interactive routing, the router may be trying to maintain clearance and can’t re-fit the path at the new width.

**Fix:**
- Finish route (right click → **Finish**), then edit width.
- Or re-route that short section with the desired width.

---

### What I need from you (one detail, no back-and-forth)
When you try to widen it, what *exactly* happens?
- A) It snaps back to the old width silently  
- B) It refuses and shows a message/DRC text at the bottom  
- C) It widens some segments but not others

If you can tell me A/B/C, I’ll tell you the precise click-path to fix it in one go.
