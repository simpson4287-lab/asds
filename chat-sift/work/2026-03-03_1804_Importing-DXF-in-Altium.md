# Importing DXF in Altium
Date (UTC): 2026-03-03 18:04
Conversation ID: 69a722ab-d6d8-838f-9df6-fa6f7c0fea9f
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-03 18:04):
How do I import dxf 

[M2] AI (2026-03-03 18:04):
In **Altium Designer**, DXF import depends on *where* you want it to land:

## 1) Import DXF into a PCB (board outline / mech / copper)
1. Open the **PCB**.
2. Go to **File → Import → DXF/DWG…**
3. In the import dialog:
   - **Units**: set correctly (mm vs inch) or you’ll get a crazy scale.
   - **Layers mapping**: map DXF layers to Altium layers (typically **Mechanical layers** for outlines; sometimes **Top/Bottom** if you truly want copper shapes).
4. Finish import.
5. If it came in offset: use **Edit → Move → Move Selection** (or set the origin properly).

**Board outline specifically:**  
- Import it onto a **Mechanical layer** first, then use **Design → Board Shape → Define from selected objects** (select the outline lines/arcs first).

## 2) Import DXF into a Schematic (rare)
Altium doesn’t really use DXF for schematics in a clean way. Usually you’d import DXF into a **PCB mechanical layer** or into a **PCB library footprint** if it’s a mechanical outline.

## 3) Import DXF into a PCB Library footprint (e.g., keepout/courtyard)
1. Open the **.PcbLib**.
2. **File → Import → DXF/DWG…**
3. Map to mech layers (Courtyard/Assembly/Keepout style) as needed.

## Common gotchas (90% of “why is this wrong?”)
- **Wrong units / scale** (mm vs inch).
- DXF entities are **splines**: Altium may approximate them or drop weird segments. If you can, export as **polylines/arcs** from CAD.
- The DXF is not a *closed* outline (tiny gaps). Board-shape-from-selected will fail unless it’s continuous.

If you tell me **what you’re importing it for** (board outline, panel, enclosure keepout, logo copper, etc.), I’ll give you the exact best-practice layer mapping and the “clean-up” steps.

[M3] ME (2026-03-03 18:06):
[image]
[attached file: IMG_526478EF-E5DB-4946-9F83-936F37F1F8A4.jpeg]

[M4] AI (2026-03-03 18:06):
Yep — your screenshot shows you’re in the **Edit** menu, which is why you can’t see DXF import.

In Altium, DXF comes in via the **File** menu (and it only appears in the right editor context).

### Import DXF into a PCB (outline / mech)
1. Make sure you’re actually in the **PCB editor** (open your `*.PcbDoc`).
2. Go to **File → Import → DXF/DWG…**
3. Set:
   - **Units** (mm vs inch) correctly
   - **Layer mapping** (DXF layers → Altium Mechanical layers, etc.)
4. Finish.

**If it’s a board outline:** import onto a Mechanical layer, select the outline, then:
- **Design → Board Shape → Define from Selected Objects**

### If you *don’t* see “File → Import → DXF/DWG…”
Most common reasons:
- You’re in a **schematic** (`*.SchDoc`) or **library** editor that doesn’t offer that import route.
- The DXF/DWG importer extension isn’t installed/enabled.

Quick checks:
- Confirm the active document tab is **`.PcbDoc`**
- Try **File → Import** from the top menu (not right-click / not Edit)

If you tell me what you’re trying to import it *into* (PCB outline, footprint courtyard, logo on silkscreen/copper), I’ll give you the exact layer mapping + the cleanest workflow.

[M5] ME (2026-03-03 18:06):
I am in PCB editor 

[M6] AI (2026-03-03 18:06):
Got it. If you’re definitely in a **.PcbDoc** and still can’t see DXF import, it’s almost always one of these:

## 1) You’re looking in the wrong menu
DXF import is **not** under **Edit** (like your screenshot). It’s here:

- **File → Import → DXF/DWG…**

So click **File** (top-left of the main menu bar), not Edit.

## 2) The “Import” item is hidden because of menu customization / simple menus
Try:
- **View → Toolbars → Customization…** (or *Customize…* depending on version)
- Or reset menus: **DXP → Customize… → Toolbars/Menus → Reset** (wording varies)

Also try the nuclear option:
- **Search** (top-right search box if enabled) and type **DXF** or **Import**.

## 3) The DXF/DWG importer extension isn’t installed/enabled
Check:
- **DXP → Extensions and Updates** (or **Extensions & Updates**)
- Look for something like **DXF/DWG Importer** (AutoCAD / DXF-DWG support) and enable/install it.
- Restart Altium after enabling.

## 4) Use the “PCB panel” import (alternate route)
Some setups expose it via a panel command:
- **Panels → PCB →** look for an **Import** / **DXF/DWG** entry (depends on version/config)

## Fast sanity check
Look at the document tab name: it should literally end **`.PcbDoc`**. If yes, then either **(1)** you’re just in Edit, or **(3)** importer not enabled.

If you can, send a quick screenshot of your **File** menu opened (not Edit). I can tell instantly which case you’re in.

[M7] ME (2026-03-03 18:07):
[image]
[attached file: IMG_49576A4C-1E09-48B6-A0AF-6A47BEE9ACFF.jpeg]

[M8] AI (2026-03-03 18:07):
Ah — your screenshot is the key: **you don’t have a “File” menu at all** (your menu bar starts at **Edit**). That’s why you can’t find **File → Import → DXF/DWG…**.

That usually means the menu has been **customised/stripped**. Here are the fastest ways to get DXF import back.

## Option A (fastest): Run the command from the Command panel
1. **View → Panels → Command** (or “Panels” button bottom-right → **Command**).
2. In the Command panel, search **DXF** or **DWG**.
3. Run **Import DXF/DWG** (it will launch the importer even if the menu item is missing).

## Option B: Reset menus/toolbars to default
1. Go to **DXP → Customize…**
2. Find the **Menus** / **Toolbars** area and hit **Reset** (reset the main menus / PCB editor menus).
3. Close Altium and reopen if it doesn’t immediately repopulate **File**.

## Option C: Add “Import DXF/DWG” back onto a toolbar/menu
1. **DXP → Customize…**
2. **Commands** tab → category **File** (or search **DXF**).
3. Drag **Import DXF/DWG…** onto a toolbar (or back into the top menu bar if it allows).

---

Once you can access it, the path is:
**File → Import → DXF/DWG…**

If you tell me what the DXF is (board outline vs mechanical vs copper logo), I’ll tell you the correct layer mapping so it comes in cleanly first time.

[M9] ME (2026-03-03 18:10):
Is there a way to enhance graphics on machine. It’s a high spec 

[M10] AI (2026-03-03 18:10):
Yes — but in Altium “blocky / ugly / slow graphics” is usually **settings**, not raw spec. Here’s the short hit-list that actually moves the needle.

## 1) Force Altium onto the discrete GPU
**Windows Settings → System → Display → Graphics**
- Add `DXP.EXE` (Altium)
- Set to **High performance**

Also check **NVIDIA Control Panel / AMD Adrenalin**
- Program settings → Altium → **High-performance GPU**
- Power management: **Prefer maximum performance**

## 2) Switch Altium’s graphics engine (this is the big one)
In Altium go:
**DXP → Preferences → System → Graphics** (wording varies by version)

Try these combinations:
- **Hardware acceleration ON**
- Rendering engine: **DirectX 11** (or whatever modern option you have)
If it’s currently “software”/“GDI”, switching away from that is night-and-day.

After changing: **restart Altium**.

## 3) Turn off the stuff that kills redraw in PCB
In the PCB editor:
- Disable **View → Connections → Show All** (ratsnest) unless needed
- Reduce **real-time DRC / online clearance display** if it’s heavy
- Turn off **3D bodies** temporarily (or use 3D only when needed)

## 4) Windows/UI scaling (fixes fuzzy text + weird zoom)
If it looks “soft” rather than slow:
- Right-click `DXP.EXE` → **Properties → Compatibility → Change high DPI settings**
  - Tick **Override high DPI scaling behavior**
  - Set to **Application**
- In Windows Display, try 100% or 125% scaling (avoid odd custom scaling)

## 5) Update the right drivers
Make sure you’re on the **latest GPU driver** (NVIDIA Studio drivers are often more stable for CAD than Game Ready).

---

If you answer these two, I’ll tell you exactly what to flip first:
1) Are you on a **laptop** with Intel iGPU + NVIDIA/AMD dGPU, or a desktop?  
2) Is the problem **performance (lag)** or **visual quality (fuzzy/jaggy)**?

[M11] ME (2026-03-03 18:13):
[image]
Turn windows games off?
[attached file: IMG_52A85514-81C4-490C-9D72-1E1DA0488889.jpeg]

[M12] AI (2026-03-03 18:13):
You’re in the right place — and yes, it can help to **turn the “games/windowed optimisations” stuff off** for CAD apps like Altium if you’re seeing weird redraw, blur, flicker, or input lag.

From your screenshot I can see:
- **Optimisations for windowed games** = **On**
- **Hardware-accelerated GPU scheduling (HAGS)** = **On**
- Altium is already set to **High performance (RTX 2000 Ada)** ✅ (good)

### What I’d do (safe + reversible)
#### 1) Turn **Optimisations for windowed games** OFF
- It’s mainly aimed at games (flip model, VRR behaviours). Some pro apps behave better without it.
- After changing: **restart Altium** (sometimes needs sign-out/reboot, but usually app restart is enough).

#### 2) If Altium still feels “off”: try toggling **HAGS**
HAGS can be great, but on some driver/app combos it causes stutter.
- Try **HAGS OFF**, reboot, test Altium.
- If no improvement, put it back **ON**.

### Also do this in NVIDIA Control Panel (worth it)
**NVIDIA Control Panel → Manage 3D settings → Program Settings → DXP.EXE**
- **Power management mode** → *Prefer maximum performance*
- **OpenGL rendering GPU** → RTX 2000 Ada (if that option appears)
- Leave AA/AF etc. as “Application-controlled”

### If your goal is “sharper graphics” (not performance)
Then the bigger win is usually **Windows DPI scaling** + Altium graphics engine:
- `DXP.EXE` → Properties → Compatibility → **High DPI settings** → override scaling = **Application**
- In Altium: **Preferences → System → Graphics** → ensure you’re on the best **hardware/DirectX** mode.

If you tell me what the symptom is (laggy panning, jagged lines, blurry text, flicker), I’ll tell you which single toggle is most likely to fix it.

[M13] ME (2026-03-03 18:14):
[image]
I remoten into it. I’ve chose this 
[attached file: IMG_BB4941CA-B286-436F-BADC-7BE0A06DCD79.jpeg]

[M14] AI (2026-03-03 18:14):
Nice — that’s the right setting **for local use**: Altium is pinned to **High performance (RTX 2000 Ada)** and you’ve turned **Optimizations for windowed games = Off** for Altium. ✅

But the big catch is your line: **“I remote into it.”**  
If you’re using **Windows Remote Desktop (mstsc)**, the GPU you “feel” is often **not** the local RTX in the way you expect. RDP can render using a *remote graphics driver / software path* unless you explicitly enable GPU acceleration for RDP sessions.

### What to do (in order)

## 1) Keep what you’ve done (good)
- Altium: **High performance GPU**
- Windowed games optimizations: **Off**

## 2) Fix RDP so it can actually use the RTX
On the **remote workstation** (the machine running Altium):

### A) Group Policy (best method)
1. Run `gpedit.msc`
2. Go to:  
   **Computer Configuration → Administrative Templates → Windows Components → Remote Desktop Services → Remote Desktop Session Host → Remote Session Environment**
3. Enable:
- **Use hardware graphics adapters for all Remote Desktop Services sessions** = **Enabled**
4. Also set:
- **Configure H.264/AVC hardware encoding for Remote Desktop Connections** = **Enabled** (if present)

Reboot after changing.

### B) If you don’t have gpedit (or want registry)
Tell me if it’s Windows Pro vs Home and I’ll give you the exact registry keys.

## 3) RDP client settings (your local machine)
In **Remote Desktop Connection** (mstsc):
- **Show Options → Experience tab**
  - Tick **Persistent bitmap caching**
  - Set connection speed appropriately (LAN if you’re on it)
- **Display tab**
  - Don’t go crazy on resolution/scale if your link is weak (it can feel “laggy” even with a monster GPU)

## 4) Consider using a better remoting tool for CAD (if allowed)
For 3D-heavy CAD and fast pan/zoom:
- **HP Anyware / Teradici**, **Parsec**, or **NiceDCV** often feel *much* snappier than RDP for graphics.
(If IT policy locks you to RDP, the Group Policy above is the key fix.)

---

### Quick diagnostic question (no screenshots needed)
When you’re remoted in, does Altium look:
1) **laggy** (pan/zoom stutter), or  
2) **blurry/soft** (text/jaggy lines), or  
3) **both**?

And are you using **mstsc (built-in RDP)** or something else (AnyDesk/TeamViewer/etc.)?

[M15] ME (2026-03-03 18:16):
[image]
[attached file: IMG_71DF3695-F938-4559-824F-9AFF827447C0.jpeg]

[M16] AI (2026-03-03 18:16):
Yep — that view means you’ve opened **Local Group Policy Editor**, but it’s currently not actually showing the policy tree (or you’ve selected the root node and the right pane is empty). You need to expand down to the RDP policies.

Do this:

1) In the **left pane**, click the little **triangle / +** next to:
- **Local Computer Policy**
- then **Computer Configuration**
- then **Administrative Templates**
- then **Windows Components**
- then **Remote Desktop Services**
- then **Remote Desktop Session Host**
- then **Remote Session Environment**

2) In **Remote Session Environment**, set these:

- **Use hardware graphics adapters for all Remote Desktop Services sessions**  
  → **Enabled**

- **Configure H.264/AVC hardware encoding for Remote Desktop Connections** (if present)  
  → **Enabled**

3) Close Group Policy Editor, then run:
- `gpupdate /force`
…and ideally **reboot** the remote machine.

### If you *can’t* expand “Local Computer Policy”
A couple of common causes:
- You’re in the **Standard** view but it’s glitching: click **Extended** at the bottom (you already have tabs “Extended / Standard”).
- The MMC snap-in is not loading correctly: close it and re-open via **Win+R → gpedit.msc** (run as admin if possible).

### If gpedit is “empty” because of Windows edition / IT lockdown
Some corporate images restrict local policy snap-ins, or policies are domain-controlled. In that case, you can still apply the setting via registry (admin required) — tell me if you have admin rights on this machine and I’ll give you the exact keys/values.

One more thing I can see from your desktop: you likely *are* on a Pro/Workstation-type build (since gpedit opens), so expanding the tree should work.

Try expanding that left tree first — if it still won’t expand, send a pic of the left pane showing what nodes you can see (or tell me if “Computer Configuration” is visible).

[M17] ME (2026-03-03 18:18):
Is there any settings in the program?

[M18] AI (2026-03-03 18:18):
Yes — **Altium itself has a couple of graphics knobs** worth changing, especially when you’re using it over RDP.

## 1) Pick the best rendering engine
In Altium:
**DXP → Preferences → System → Graphics**

Look for settings like:
- **Use Hardware Acceleration** → **ON**
- Rendering / Graphics engine (if offered) → choose the most modern option (often **DirectX**).  
If you see something like **GDI / Software / Legacy** vs **DirectX**, pick **DirectX**.

Then **restart Altium**.

## 2) Reduce “live” visual load while remote
In the PCB editor (while you’re panning/working):
- Turn off **live ratsnest** unless needed:  
  **View → Connections → Hide All** (or similar)
- Reduce/disable **Online DRC** while doing heavy moves:  
  **Preferences → PCB Editor → General / DRC** (wording varies)
- In **View Configuration** (press **L**):
  - Temporarily hide **Rooms**, **Polygons**, **3D Bodies**, or other heavy layers while editing

These don’t change quality as much as they change *responsiveness* over remote.

## 3) Anti-aliasing / smoothness (if available)
Some versions expose:
- **Smooth graphics / anti-aliasing**
- **Use OpenGL/DirectX primitives**

If you see anti-aliasing: turn it **ON** for nicer lines/text, but if performance tanks over RDP, turn it back **OFF**.

---

### Quick pointer for *your specific situation (RDP)*
If the graphics engine is already hardware accelerated locally, but looks worse only when remote, the biggest win is still the **RDP hardware adapter policy** we discussed. Altium settings help, but RDP can bottleneck them.

If you tell me your **Altium version** (looks like AD26 from your earlier path) and what you see inside **Preferences → System → Graphics** (a quick photo is fine), I’ll tell you exactly what to set.

[M19] ME (2026-03-03 18:19):
[image]
[attached file: IMG_AE31C5AA-6198-48D4-AB7C-11C9B2FE779E.jpeg]

[M20] AI (2026-03-03 18:19):
Yes — but you’re currently in **System → Navigation** (your search “grap” is matching *graphical* / *connective graph*), not the **graphics renderer** settings.

Do this to get to the right place:

## 1) Open the Graphics renderer settings
In **Preferences**:
- In the left tree, expand **System**
- Look for **Graphics** (sometimes called **View** or **Display** depending on version)

Or use the search box and type **render** / **DirectX** / **hardware acceleration** (better keywords than “grap”).

When you find it, set:
- **Use hardware acceleration** = **ON**
- Renderer = **DirectX** (or the most modern option offered)
Then **restart Altium**.

## 2) PCB-side visual quality / performance knobs (while you’re here)
In Preferences, also check:
- **PCB Editor → General**: “Show pad outlines / show polygons / …” (can affect redraw)
- **PCB Editor → Display** (if present): anti-aliasing / smooth graphics options

## 3) Super practical: View Configuration (per-document)
In the PCB editor press **L** (View Configuration):
- Turn on **Smooth/anti-aliased** options if available
- Hide heavy stuff while remote (rooms, polygons, 3D bodies) to improve responsiveness

### Why your screenshot matters
It confirms you *can* reach preferences fine — we just need the **System → Graphics** page.

If you can, type **DirectX** in that search box and send the next screenshot that comes up — I’ll tell you exactly which toggles to set on that page.

[M21] ME (2026-03-03 18:19):
[image]
[attached file: IMG_D4E25AD0-1DAA-4232-AAC7-2D2823E7A409.jpeg]

[M22] AI (2026-03-03 18:19):
Perfect — this view shows you **don’t have a “System → Graphics” page** in this build (you’ve got **System → View / Transparency / Navigation**, etc.). That’s normal on some Altium versions/configs: the renderer options are tucked elsewhere.

Here’s where to go *instead* (in order), and what to set.

## 1) System → View (the closest equivalent)
Click **System → View** (left pane).

Look for anything like:
- **Use DirectX / Use GDI / Legacy graphics**
- **Hardware acceleration**
- **Anti-aliasing / Smooth graphics**
- **Use OpenGL** (rare)

Set:
- **Hardware acceleration / advanced graphics = ON** (if present)
- **DirectX** / modern renderer (if there’s a choice)

Then **restart Altium**.

## 2) PCB Editor → Display (most likely place)
Expand **PCB Editor** then look for:
- **Display**
- **General**
- **Board Insight / Interactive Routing** (sometimes has “advanced display” toggles)

What you want:
- Any option that mentions **accelerated graphics**, **DirectX**, **anti-alias**, **smooth**, **quality**, **rendering**.

## 3) View Configuration (per PCB doc) — quickest impact
In the PCB editor press **L** (View Configuration) and check:
- **Display / Rendering quality**
- **Show polygons as solid vs outline**
- **Smooth (anti-aliased) primitives** (if present)

For remote sessions, a good combo is:
- **Polygons = outline** while editing (massively improves pan/zoom)
- Turn **solid** only when you need to inspect

## 4) Since you’re on RDP: stop Altium looking “soft”
If your main complaint is **blurry text/lines** (not just lag), do this on the **remote workstation**:

Right-click `DXP.EXE` → **Properties → Compatibility → Change high DPI settings**
- Tick **Override high DPI scaling behavior**
- Set to **Application**
Then restart Altium.

---

### What I need from you (one screenshot)
Click **System → View** and snap that page.  
From that single screen I can tell you exactly what toggles to change on your setup.

[M23] ME (2026-03-03 18:20):
[image]
[attached file: IMG_FED6D607-0F30-4149-AC8C-529C9D2BB4D5.jpeg]

[M24] AI (2026-03-03 18:20):
Great — this **System → View** page confirms it: there are **no renderer / DirectX / hardware acceleration controls here**. This page is purely UI behaviour (panels, animations, doc bar), so it won’t improve PCB graphics quality/performance.

What you *can* do from here that helps a bit over RDP:
- **Untick “Use animation”** (Popup Panels).  
  This reduces UI “faff” and can make remote interaction feel snappier. Not a huge win, but free.

Now for the real graphics levers (these are the ones that matter):

## 1) PCB editor view settings (biggest day-to-day win)
Open the PCB, then press **L** (View Configuration).

Do this while remoted in:
- **Polygons**: set to **Outline** (or “Draft”) while routing/placing  
  (huge improvement in pan/zoom if you have big pours)
- Turn off/hide heavy layers you don’t need while editing:
  - **Rooms**
  - **3D Bodies**
  - Excess mech layers

Then when you need to check copper: switch polygons back to **Solid**.

## 2) Turn off “live stuff” that causes lag
In PCB editor menus (names vary slightly):
- **View → Connections → Hide All** (ratsnest off) unless you need it
- Temporarily relax **Online DRC** while moving large blocks  
  (**Preferences → PCB Editor → General / DRC**)

## 3) Fix “soft/blurry” look (DPI scaling)
On the **remote workstation**:
Right-click `DXP.EXE` → **Properties → Compatibility → Change high DPI settings**
- ✅ Override high DPI scaling behavior → **Application**
Restart Altium.

This is the most common fix for “Altium looks mushy over RDP”.

## 4) The real fix for RDP GPU use (if you have admin)
Even with an RTX 2000 Ada, RDP can still force a software render path unless the policy is enabled:
**Use hardware graphics adapters for all Remote Desktop Services sessions**.

(If your gpedit tree won’t expand, we can do the same via registry.)

---

### Quick direction check
When you say “enhance graphics”, which is it?
- **A)** It’s *blurry/soft* (text and lines not crisp), or
- **B)** It’s *laggy/stuttery* when panning/zooming?

Pick A or B and I’ll tell you the single best next change.

[M25] ME (2026-03-03 18:21):
[image]
[attached file: IMG_77A8C6B5-E021-4059-A495-3846BF54CFC5.jpeg]

[M26] AI (2026-03-03 18:21):
Yep — **this** is one of the right places. On your screenshot you’re in **PCB Editor → Display** and you’ve got:

- ✅ **Antialiasing = ON** (this improves line quality)
- ✅/❌ **Use Animation = ON** (this can make remote pan/zoom feel worse)

### What I’d change right now (given you’re remoting in)
1) **Turn OFF “Use Animation”**  
   This often reduces “swimmy” lag / sluggish feel over RDP.

2) Keep **Antialiasing ON** *unless* performance is bad.  
   - If you’re chasing *crispness*, keep it **ON**.  
   - If you’re chasing *speed* and it’s stuttery, try it **OFF** as a test.

Then click **Apply** and **restart Altium** (restart matters more than people expect for display settings).

---

## Next two PCB settings that usually make the biggest difference
In the left tree, go to:

### A) **PCB Editor → Board Insight Display**
This is where Altium can do “fancy” real-time highlighting.
- If you see options like **Board Insight**, **dynamic highlighting**, **hover previews**, consider **disabling/reducing** them for remote sessions.

### B) **PCB Editor → Interactive Routing**
Look for “online” display options, shove/drag visualisations, etc.  
These can hammer redraw when remote.

---

## One more high-impact trick (not in Preferences)
In the PCB editor press **L** (View Configuration) and:
- Set **Polygons** to **Outline** while you work (solid pours are a redraw killer over RDP)
- Hide **Rooms** / **3D Bodies** unless needed

---

If you tell me what the pain is **now** (blurry vs laggy), I’ll tell you whether to prioritise:
- antialias/DPI settings (sharpness), or
- animations/board insight/polygon outlines (responsiveness).

[M27] ME (2026-03-03 18:23):
[image]
[attached file: IMG_61127A33-4360-410B-BBD7-8F04AEB1B488.jpeg]

[M28] AI (2026-03-03 18:23):
Nice — this screen is exactly one of the “hidden performance sinks”.

On **PCB Editor → Board Insight Display** you currently have:

- ✅ **Live Highlighting = Enabled**
- ✅ **Live Highlighting only when Shift key down = Enabled** (so it *should* mostly be quiet unless Shift is held)

### What to set (especially for RDP)
#### 1) Disable Live Highlighting completely (best for responsiveness)
- Untick **Live Highlighting → Enabled**
- (This stops Altium constantly doing hover/selection analysis + redraw overlays.)

If you *like* the feature, keep it but make sure it’s **only when Shift is down** (you already have that ticked), and just be aware it will still cost a bit.

#### 2) Locked texture option
You’ve got **Only When Live Highlighting** selected — that’s fine.  
If you disable Live Highlighting, this effectively won’t do anything.

#### 3) Single Layer Mode options
These don’t affect general performance much unless you’re flipping single-layer mode a lot. Leave as-is.

Then **Apply** and restart Altium if it doesn’t feel different immediately.

---

## Next high-impact step (the “big hammer” for remote lag)
In the PCB editor itself:
- Press **L** → set **Polygons** to **Outline** while working.
- Turn off ratsnest: **View → Connections → Hide All**

These two usually dwarf everything else when you’ve got big pours / dense nets.

---

If you tell me whether the issue is **laggy pan/zoom** vs **blurry/fuzzy**, I’ll steer you to the last 1–2 changes (DPI override vs RDP hardware adapter policy).

[M29] ME (2026-03-03 18:24):
[image]
Like that?
[attached file: IMG_056A79E9-9F71-4CCF-A7BF-A73EE7B7BF76.jpeg]

[M30] AI (2026-03-03 18:24):
Nearly — you’ve done the **opposite** of what you want.

In your screenshot:
- **Live Highlighting = Enabled** ✅ (still ON)
- **“Live Highlighting only when Shift key down” = unticked** ❌

That means live highlighting will run **all the time**, which is *worse* for remote performance.

### Set it like this (pick one)

#### Option 1 (best for speed over RDP): turn it OFF
- Untick **Enabled** under **Live Highlighting**  
  (then the Shift option becomes irrelevant)

#### Option 2 (keep the feature but tame it)
- Keep **Enabled** ticked
- Tick **“Live Highlighting only when Shift Key Down”**

Then hit **Apply**.

If your goal is smoother pan/zoom remotely, I’d go with **Option 1 (OFF)**.

Next, also do:
- **PCB Editor → Display**: turn **Use Animation** OFF
- In PCB view: press **L** → set **Polygons = Outline** while working

That combo usually makes Altium feel “local” again even through RDP.

[M31] ME (2026-03-03 18:25):
[image]
[attached file: IMG_F0A9E620-901B-46B2-AC9A-4FF68208770F.jpeg]

[M32] AI (2026-03-03 18:25):
Yep — you’re in the right general area, but this screen (**PCB Editor → Defaults → Polygon**) is **polygon *rules/behaviour* defaults**, not the **display mode** that speeds up remote graphics.

So: **don’t change anything here** unless you specifically want to alter how pours behave (island removal, necks, etc.).

### What you actually want (to make it faster / cleaner over RDP)

## 1) Set polygon *display* to Outline (fastest)
In the PCB editor (not Preferences):
- Press **L** (View Configuration)
- Find **Polygons**
- Set to **Outline** (or “Draft”) while you work  
  (switch back to Solid when you need to inspect copper)

If you can’t find it in View Config:
- Try **View → Board Insight →** (or similar) and look for polygon display options, OR
- Open the **PCB panel** and search “Polygon” display.

## 2) Confirm you fixed the Live Highlighting mistake
Go back to:
**PCB Editor → Board Insight Display**
- Best: **Live Highlighting = OFF**
(or keep it ON but tick “only when Shift is down”)

## 3) Turn off PCB display animations
You already saw this:
**PCB Editor → Display**
- **Use Animation = OFF**
(keep Antialiasing ON if you want nicer lines)

---

### Quick check
What are you seeing that you don’t like right now:
- **laggy pan/zoom**, or
- **blurry/jagged lines**, or
- **both**?

And if you can, press **L** and send a photo of the **View Configuration** panel — I’ll point to the exact polygon display toggle on your version.

[M33] ME (2026-03-03 18:28):
[image]
Like that?
[attached file: IMG_746A9C43-3500-4B7C-B07E-B1FF1314072B.jpeg]

[M34] AI (2026-03-03 18:28):
Yes — **that’s exactly the panel I meant**. 👍 You’ve already got the key speed switch set:

- **Polygons → Draft = ON** ✅  
That’s the “outline/draft pours” mode and it’s one of the biggest wins over RDP.

A couple of tweaks from this same panel that usually make it even smoother:

## 1) Turn off 3D stuff while remote
In **Object Visibility**:
- **3D Body** → tick **Draft** (or just hide 3D bodies if you don’t need them)
And keep **3D** at the top **Off** (you already have 3D Off ✅).

## 2) Rooms can be surprisingly heavy
If you’re not actively using rooms:
- Set **Rooms → Draft** ON, or hide rooms via their visibility (depends on your workflow).

## 3) Keep “All Objects = Mixed” under control
Because “All Objects” is Mixed, some items may still be in “pretty” mode. Your big hitter (Polygons) is already draft, so you’re good.

## 4) If it’s still laggy
Next culprits (outside this panel):
- **Ratsnest**: **View → Connections → Hide All**
- **Live Highlighting**: turn it **OFF** (or Shift-only)
- **PCB Editor → Display → Use Animation = OFF**

### Quick confirmation
After setting polygons to draft, does pan/zoom feel noticeably better? If not, the limiting factor is likely **RDP’s rendering path**, and we should finish the **“use hardware graphics adapters for all RDP sessions”** policy/registry step.

[M35] ME (2026-03-03 18:55):
What later should it all go on?

[M36] AI (2026-03-03 18:55):
If you mean **a DXF you’re importing** (outline / mechanical detail / logo), best practice is: **keep it off copper until you’re sure it’s correct**, and put it on the most appropriate *mechanical* or *overlay* layer.

### Recommended targets in Altium

**1) Board outline / cut-outs**
- Import to a **Mechanical layer** (e.g. *Mechanical 1* named “Board Outline”)
- Then: **Design → Board Shape → Define from Selected Objects**
- Internal cut-outs: **Design → Board Shape → Define Board Cutout** (select the imported loop)

**2) Component courtyard / assembly outline**
- **Courtyard**: a dedicated **Mechanical layer** (often *Mech 13/15* depending on your house standard)
- **Assembly outline**: a dedicated **Mechanical layer** (often *Mech 1/2* as “Top Assembly / Bottom Assembly”)

**3) Fabrication drawing / dimensions**
- **Mechanical layer** used for fab drawing (separate from outline/courtyard if you can)

**4) Keep-out shapes**
- Import to **Keep-Out Layer** if it’s genuinely a keepout boundary, or
- Import to a mech layer first, then convert/copy to keepout once verified

**5) Logos / markings**
- For silkscreen: **Top Overlay / Bottom Overlay**
- For copper art: **Top Layer / Bottom Layer** (only if you *really* want copper features)
- For soldermask openings: **Top/Bottom Solder Mask**

### Simple rule of thumb
- **Geometry that defines the PCB** → *Mechanical “Board Outline”*  
- **Geometry that informs manufacturing/placement** → *Mechanical (Fab/Assembly/Courtyard)*  
- **Geometry that prints** → *Overlay*  
- **Geometry that affects copper** → *Copper layers* (last, and deliberately)

If you tell me what the DXF actually contains (board perimeter? enclosure? logo? courtyard?), I’ll tell you the exact layer + the next command to turn it into a board shape/cutout/keepout.

[M37] ME (2026-03-03 19:02):
[image]
What options?
[attached file: IMG_39241874-0C97-40AF-B60B-D07740E17F0C.jpeg]

[M38] AI (2026-03-03 19:02):
You’re in Altium’s **DXF/DWG Import** dialog now — perfect. For a **headboard outline DXF** (mechanical geometry), these are the sane options.

## The two most important choices

### 1) **Blocks: Import as primitives**
✅ Pick **Import as primitives**  
(“Import as components” is only useful if the DXF has repeated blocks you want as placed component-like objects. For outlines, it’s a pain.)

### 2) **Scale / Units**
This is where most people get burned.

- If the DXF was drawn in **mm** (very likely): set **Scale = mm**.
- Your dialog currently shows **1 AutoCAD unit = 1 mil** and a size like **688 mil (17.48 mm)** — that smells like a **unit mismatch**.

**Best practice:** set Scale to **mm** first and see if the reported size now matches what you expect (e.g. 100 mm should show ~100 mm).

## Other options (recommended defaults)

### Drawing Space: **Model**
✅ **Model** (Paper space is for plotted sheets/layouts)

### Fonts: **Stroke**
✅ **Stroke** (more predictable; TrueType can import weirdly)

### Default Line Width
Doesn’t really matter if you’re importing to mechanical layers, but:
- Set something sensible like **0.1 mm** if it’s going to fab/mech layers.
(Your current 0.0127 mm is “hairline”; it’s fine but sometimes hard to see.)

## Layer mappings (this is “what layer should it go on?”)
Down the bottom you map **AutoCAD layers → Altium layers**.

For a board/headboard outline:
- Map the DXF outline layer (often “0”, “OUTLINE”, etc.) to a **Mechanical layer** you dedicate to outline, e.g.  
  **Mechanical 1 = Board Outline** (or “Mech 1 / Outline”)

**Do NOT map it to copper** unless you intentionally want copper shapes.

In your screenshot, it’s mapping one layer to **Top Placement** — I’d change that to a **Mechanical layer**.

## Donut-to-pad conversion
That section is only relevant if your DXF contains donut circles that represent pads/holes.
- For an outline DXF: set conversion condition to **None / disable** if possible (or leave it but ensure it won’t accidentally convert circles).
If your DXF includes mounting holes and you *want* pads: we can use it deliberately, but don’t do it by accident.

---

### Quick “do this now” checklist for your dialog
1) **Import as primitives**
2) **Scale = mm** (most likely)
3) **Model**
4) Map outline DXF layer → **Mechanical 1 (Board Outline)**
5) OK

After import, if it’s meant to become the PCB outline:
- Select the imported outline (must be a closed loop)
- **Design → Board Shape → Define from Selected Objects**

If you tell me the *expected real size* of that headboard (e.g. “it should be 120 mm dia” or whatever), I can tell you instantly whether your units are currently wrong from the size readout.

[M39] ME (2026-03-03 19:22):
[image]
How do I change the layer of the outline? To board outline rather than keep out
[attached file: IMG_9A1935C3-3805-4286-A825-BB570731B23C.jpeg]

[M40] AI (2026-03-03 19:22):
You’ve selected a **Keepout – Arc**, so it’s currently a **keepout primitive**, not a “board outline” primitive. That’s why the Properties panel says it’s restricted to **Keep-Out Layer**.

To make it the **board outline**, you normally do **not** “change its layer” to a special Board Outline layer. You put the outline geometry on a **Mechanical layer**, then *define the board shape from it*.

Here are the clean options:

## Option A (best): Put the geometry on a Mechanical layer, then define board shape
1. **Select the outline objects** (all arcs/lines that form the perimeter).
2. **Convert them from keepout primitives to tracks/arcs**:
   - Right-click selection → **Convert →** (look for) **Convert to Track/Arc** or **Explode / Convert to primitives**  
   - Or use **Tools → Convert → Create Primitives from Keepout** (wording varies)
   - The goal: they become normal **Track/Arc** objects, not “Keepout – Arc”.
3. With them now normal objects, in the **Properties** panel change:
   - **Layer** → set to a **Mechanical layer** (e.g. *Mechanical 1*) and name it “Board Outline”.
4. Now define the board:
   - Select that outline loop → **Design → Board Shape → Define from Selected Objects**

## Option B (quick but less controlled): Redraw board shape
If conversion is awkward:
- Leave the keepout as-is (use it as a reference)
- Draw/trace the outline on a mechanical layer using **Place → Arc/Line**
- Then **Design → Board Shape → Define from Selected Objects**

## Option C: If you truly just want it “not keepout” (but not necessarily board shape)
You can keep the geometry as tracks/arcs on a mech layer and stop it affecting routing:
- Convert off keepout (as above)
- Put on **Mechanical layer**
- Don’t use keepout restrictions at all

---

### Why you can’t just pick “Board Outline” in the layer drop-down
Altium’s **board outline isn’t a normal layer object**; it’s the **Board Shape**. The usual workflow is “geometry on mech → define board shape”.

If you tell me which Altium version you’re on (looks like AD26) and whether the outline is **a closed loop of arcs/lines**, I can give you the exact right-click menu path you’ll see for the conversion step.

[M41] ME (2026-03-03 19:23):
[image]
[attached file: IMG_6D68F0CC-A8B7-4DD9-B5D5-A93687AE5B67.jpeg]

[M42] AI (2026-03-03 19:23):
Yep — that menu confirms what’s going on: you’ve got **Keepout** objects placed, and Altium won’t let you “just change the layer” because *Keepout is its own object type*.

Here’s the clean way to turn that outline into the **board shape**.

## Goal
Get your outline onto a **Mechanical layer** as normal **Lines/Arcs**, then:
**Design → Board Shape → Define from Selected Objects**

## Step-by-step (works with what you’re showing)

### 1) Select the entire outline
- Click one segment
- Use **Shift+Click** to add more, or drag a selection box around the perimeter.
- (If it’s hard, use **Edit → Find Similar Objects** on one arc, then select all arcs on keepout.)

### 2) Convert Keepout primitives into “real” primitives
With the keepout outline selected:
- Look in the **Properties** panel for a conversion option (often **“Convert” / “Create Primitives” / “Explode”**)
- Or right-click and look for something like:
  - **Convert → To Track/Arc**
  - **Tools → Convert → Create Primitives from Keepout**
  - **Explode** (turns special objects into basic arcs/lines)

Different installs show this in slightly different places, but the keyword is **Convert** or **Explode**.

**Result you want:** the Properties panel should say **Arc** or **Track**, *not* “Keepout – Arc”.

### 3) Move the converted outline onto a Mechanical layer
Once they’re normal arcs/lines:
- In **Properties → Layer**, set to **Mechanical 1** (or whichever you use), and rename that mech layer “Board Outline”.

### 4) Define board shape
- Select the outline loop
- **Design → Board Shape → Define from Selected Objects**

---

## If you can’t find “Convert/Explode” anywhere
Fast workaround:
1. Set active layer to **Mechanical 1**
2. **Place → Arc / Line** and trace over the keepout (snap endpoints)
3. Then **Define from Selected Objects**

It’s dumb, but it’s 100% reliable.

---

### Quick diagnostic
When you click one segment, does the Properties panel say **“Keepout – Arc”** (as earlier)? If yes, you’re still in keepout type and must convert/trace before it can become board outline.

If you send a screenshot of the **Properties panel** for a selected outline segment *while that right-click menu is open*, I can tell you exactly where your build exposes the **convert** function.

[M43] ME (2026-03-03 19:24):
[image]
[attached file: IMG_F8462628-9CA3-45F8-AEB8-E9AF8DA4A6FE.jpeg]

[M44] AI (2026-03-03 19:24):
Yep — that confirms it: the outline entities are **Keepout – Arc**, and Altium is enforcing **Restricted for Layer: Keep-Out Layer**, so you *cannot* re-layer them directly. You have to **convert** them into normal primitives first, then move them to a mechanical layer and use them to define the board shape.

Here are the two reliable ways to do it in AD26:

## Method 1 (preferred): Copy → Paste Special as “Primitives”
1. **Select the whole outline** (all arcs/lines that form the perimeter).
2. **Ctrl+C**
3. Go to **Edit → Paste Special…**
4. In Paste Special, choose something like:
   - **Paste as: Tracks/Arcs (Primitives)** (wording varies: “Primitives”, “Tracks”, “Lines/Arcs”)
   - Set destination **Layer = Mechanical 1** (or your outline mech layer)
5. Click OK.

Now you’ll have a duplicate outline made of normal arcs/tracks on a mechanical layer.

Then:
- Select that mech outline → **Design → Board Shape → Define from Selected Objects**

Finally (optional):
- Delete the original keepout outline.

## Method 2: Re-import DXF with correct layer mapping
If this keepout came from the importer mapping to Keep-Out:
1. Delete the imported keepout outline.
2. Re-import DXF and in **Layer Mappings** map the DXF outline layer to a **Mechanical layer**, not Keep-Out / Top Placement.
3. Define board shape from selected objects.

## Quick sanity: what “layer” should it end up on?
- Put the outline geometry on **Mechanical 1** (or a dedicated mech layer you name “Board Outline”)
- The actual “board outline” becomes the **Board Shape** via **Define from Selected Objects**.

---

### If you can’t find Paste Special
It’s sometimes hidden; but **Ctrl+Alt+V** often opens Paste Special in Altium.

If you tell me whether your outline is a **single closed loop** (looks like it), Method 1 will work immediately and is the least faff.

[M45] ME (2026-03-03 19:27):
[image]
Says it son there but hasn’t turned green 
[attached file: IMG_A94CF049-6648-421D-BFE0-379690E4520B.jpeg]

[M46] AI (2026-03-03 19:27):
You’ve actually **done the hard bit**: the object is now a normal **Arc** (not “Keepout – Arc”) and its **Layer = Mechanical 15**. ✅

The reason it “hasn’t turned green” is almost certainly **not the layer assignment** — it’s **your view / display mode**:

### 1) You’re likely still seeing the old keepout outline (magenta) on top
If the original keepout arcs are still there, you’ll still see the **Keep-Out Layer colour** (magenta/purple) even though your *new* arc is on Mechanical 15.

Do this quick test:
- Temporarily **hide the Keep-Out Layer**:
  - Press **L** (View Configuration) → in Layers, untick **Keep-Out Layer**
  - or use the **View Configuration / Layers** panel to turn it off
If the magenta outline disappears and your mech-15 arc is there, you’re good.

### 2) Mechanical layer colour is controlled by “Layer Colors”
Even if it’s on Mechanical 15, it won’t necessarily look “green” unless Mechanical 15 is set to green (or you’re not in a monochrome/single-layer mode).

Check:
- Press **L** → make sure you’re **not** in **Single Layer Mode** (Shift+S toggles it)
- Also check **PCB Editor → Layer Colors** (Preferences) to see what colour Mechanical 15 is.

### 3) “Green” only happens when it becomes the Board Shape
If what you mean is the **actual board outline** (board shape) going green/clear:
- Select the *entire closed loop* of outline arcs/lines on Mechanical 15
- **Design → Board Shape → Define from Selected Objects**
After that, the board edge will follow that shape (and you’ll see the board boundary update).

---

## What I’d do in your situation (fast)
1) Hide **Keep-Out Layer** to confirm you’re not looking at the old outline.
2) Select all the arcs on **Mechanical 15** (Find Similar is handy).
3) **Design → Board Shape → Define from Selected Objects**
4) Delete the old keepout arcs once you’re happy.

If you tell me what you expect to see “turn green” (the outline itself, or the board edge/board shape), I’ll point you to the exact visual cue to look for.
