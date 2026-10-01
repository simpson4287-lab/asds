# Text Positioning Issues
Date (UTC): 2026-03-22 15:45
Conversation ID: 69c00e90-1ef0-838e-8877-c73b2c53e284
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-22 15:45):
[image]
[image]
Why is it that I sent my parts up like that and they come though off position 
[attached file: IMG_A7B06FFE-1844-49C2-BBE4-924EAEEB978A.jpeg]
[attached file: IMG_094CAEDE-B676-4C1A-B4AB-6E894A9D0347.jpeg]

[M2] AI (2026-03-22 15:45):
Most likely because the **designator/comment text is not actually locked to the exact visual position you set in the SchLib the way you expect**.

What’s happening is usually one of these:

1. **Autoposition is enabled** on the designator/comment.  
   In Altium, auto-positioning makes the text stay in a chosen relative location as the component is moved or rotated, rather than preserving an arbitrary hand-placed offset. That can make the placed part look different from how it looked in the library editor. citeturn807240search4turn807240search17

2. **You moved the text on the placed schematic part**, so that instance is now using its own placement behavior.  
   Altium’s docs note that dragging parameter text directly can switch it to a manual positioning mode for that placed object. citeturn807240search11turn807240search1

3. **Library display settings / parameter handling are overriding what you thought you saved.**  
   Designator and Comment are special child parameters of the component, and their visibility/location is controlled through the component/library parameter settings rather than as ordinary graphics. citeturn807240search1turn807240search5

From your screenshots, the library symbol has **R?** sitting quite high above the body, while the placed resistor shows **R42** tucked much closer to the symbol. That is very typical of either:
- the placed instance having its own manual text position already, or
- the library using autoposition rules that resolve slightly differently once placed.

### Best fix
Open the part in the **SchLib** and check both **Designator** and **Comment**:

- select the **Designator**
- look at **Autoposition**
- do the same for **Comment**

Then choose one approach and use it consistently:

**Option A — stable library-driven layout**
- keep **Autoposition enabled**
- place designator/comment where Altium expects them
- avoid dragging them around on the schematic afterwards

**Option B — exact manual visual layout**
- set the text placement manually in the library
- make sure the placed instances are not being re-autopositioned
- replace/update existing placed parts so they take the library definition cleanly

### Important gotcha
Updating a component in the library does **not always force existing placed parts to fully adopt new parameter text positions** if those instances have already been edited. So even if the symbol is correct in the SchLib, existing schematic parts can keep their own old text placement behavior. That follows from how component child parameters are managed on placed parts. citeturn807240search1turn807240search3

### What I’d do in your case
For a resistor/capacitor library where you want clean consistency:

- set **Designator** and **Comment** once in the SchLib
- keep them on **Autoposition**
- update the component
- on the schematic, delete and re-place one test part to confirm it comes in correctly

If the newly placed test part looks right but the old one does not, then the problem is the **existing instance**, not the library symbol.

If you want, send one screenshot of the **full Properties panel for the designator in the SchLib** and I’ll tell you exactly which setting is causing it.

[M3] ME (2026-03-22 15:47):
Doni lock it?

[M4] AI (2026-03-22 15:48):
No, **lock parameter** is usually **not the main fix** here.

In Altium:

- **Lock Parameter** mainly stops casual editing of that text/parameter
- it does **not reliably solve the repositioning behaviour**
- the setting that matters more is **Autoposition**

So for this issue, check this first:

- select **Designator** in the SchLib
- turn **Autoposition** **off** if you want to place it exactly by hand and keep that offset
- do the same for **Comment/Value**
- save library
- update schematic component, or better, place a fresh test part

Use **Lock Parameter** only if you want to stop accidental edits after that.

So the practical answer is:

- **Autoposition off** = better for fixed manual placement
- **Lock Parameter** = optional, but not the core cause

Also, if an existing resistor on the schematic has already had its text moved, it may keep its own local position anyway. In that case, a **freshly placed part** is the best test.

Show me the designator properties after you click the **R?** text in the library, and I’ll point to the exact checkbox.

[M5] ME (2026-03-22 15:48):
Why auto position if I want it had ice placed it 

[M6] AI (2026-03-22 15:48):
Because **Autoposition is meant to keep the text in a rule-based location relative to the symbol**, not to preserve the exact spot you dragged it to.

So Altium’s logic is basically:

- **manual placement** = “put it exactly here”
- **autoposition** = “keep it above/below/left/right the part in a tidy way”

Why it exists at all:
- if the part is rotated or mirrored, the text stays sensible
- if symbol sizes vary, text stays in a consistent relationship
- libraries look more uniform
- it helps stop designators/comments ending up half-overlapping wires or graphics

So in your case, if you’ve **already placed it nicely by hand**, then yes — **autoposition can work against you**. It may reinterpret your intended location as just “top” or “bottom” and then place it according to its own offset rules.

For what you want:

- click the **R?** text in the SchLib
- **untick Autoposition**
- do the same for the **value/comment**
- save
- compile/update
- then place a **fresh new part** to test

That should make the library keep the exact coordinates you set.

One annoying Altium quirk: old placed parts may still hang on to their previous text behaviour, so the clean test is always a **new placement**, not just looking at an old instance.

So the real answer is: **Autoposition is for consistent automatic layout, not precision manual text placement.** In your case, turn it off.

[M7] ME (2026-03-22 15:49):
Can you change auto psoitonnriles?

[M8] AI (2026-03-22 15:49):
Yes, but only **to a point**.

In Altium you can change the **autoposition setting/style** for the designator/comment, but you generally **cannot define your own custom “rule engine”** for how it calculates the offset. It’s more like choosing from built-in positioning behavior, or switching to manual placement. citeturn340098search3turn340098search7turn340098search14

For what you’re doing, the important bit is this:

- **Autoposition ON** = Altium keeps the text in a chosen automatic relationship to the symbol as it moves/rotates. citeturn340098search3turn340098search9
- **Manual** = you can freely place the text where you want, and dragging the text directly switches it to manual behavior. citeturn340098search7

So the real answer is:

- **Yes**, you can change the autoposition **mode/style**
- **No**, not really into a fully custom set of rules like “always 37 mil above body center unless vertical then shift right 12 mil”

### What to do
In your symbol or placed part:

1. Click the **designator** or **comment/value** text.
2. In **Properties**, find **Autoposition**.
3. Change it to **Manual** if you want exact hand placement. citeturn340098search7turn340098search14

If you leave it automatic, Altium will keep trying to place it according to its own built-in behavior when the part is moved or rotated. citeturn340098search3turn340098search9

### Best practice for your library
For resistors/caps where you want them to come in neatly every time:

- set designator/value in the **SchLib**
- use **Manual** if you want exact fixed locations
- save library
- place a **fresh test component**

That last step matters because an existing placed component may already have its own instance-specific text position. The docs note that dragging text directly affects its positioning behavior. citeturn340098search7turn340098search14

### In your case
Since you’ve already positioned **R?** and **2k7** exactly where you want them, I’d set both to **Manual**, not automatic.

If you want, I can tell you exactly where that field is in **Altium 26.3**, based on your screenshot.

[M9] ME (2026-03-22 15:51):
Which of these 3 looks bets?

[M10] ME (2026-03-22 15:51):
[image]
[attached file: IMG_C4A29B82-5617-40A8-8317-436C1E3E1A84.jpeg]

[M11] AI (2026-03-22 15:51):
The **middle one** looks best.

Why:
- **R? above, value below** is the cleanest standard read
- both texts are **centred on the body**, so it feels balanced
- easiest to scan in a crowded schematic
- least likely to look messy when repeated many times

My ranking:
1. **Middle**
2. **Top**
3. **Bottom**

Notes on each:
- **Top:** not bad, but the value being off to the right makes it feel a bit unbalanced
- **Middle:** nicest symmetry and most professional-looking
- **Bottom:** weakest, because the designator off to the right looks a bit accidental rather than deliberate

For a resistor library I’d go with:
- **designator centred above**
- **value centred below**
- keep both just far enough off the body that they don’t visually touch when zoomed out

I’d also reduce the gap slightly on the middle one so it stays compact on dense schematics.

[M12] ME (2026-03-22 15:51):
That's what I want. So I need to
Turn off autonpositon for this?

[M13] AI (2026-03-22 15:51):
Yes — for **that exact centred-above / centred-below layout**, turn **Autoposition off** for both the **Designator** and the **Comment/Value**.

That tells Altium:
- don’t apply its own placement logic
- keep the text where I manually put it

Do this in the **SchLib**:
- click **R?**
- untick **Autoposition**
- click **2k7**
- untick **Autoposition**
- save

Then test by **placing a fresh resistor** onto the schematic.

That last part matters because old placed parts may still keep their own text position from before.

So the clean workflow is:
1. fix in **SchLib**
2. save
3. place a **new instance**
4. if that looks right, then update/replace old ones as needed

One extra point: if Altium still nudges them a bit, make sure you are selecting the **actual parameter text objects** in the library, not just the component body.

[M14] ME (2026-03-22 17:15):
How do you run altium with two sessions that are linked 

[M15] AI (2026-03-22 17:15):
Yes — but “linked” can mean two slightly different things in Altium.

**If you mean two views of the same project open at once**, the usual way is:
1. Open the project normally.
2. Drag one open document tab out so it becomes a **separate window**.
3. Put that on the second monitor.
4. In **Preferences → System**, enable **“Remember window for each document kind”** so schematics/PCBs keep reopening in those separate windows next time. Altium explicitly describes this for dual-monitor use. citeturn389027search8turn389027search2

That gives you effectively **two linked working windows in the same Altium session**:
- one window can show a schematic
- the other can show PCB
- both are still the **same project / same live design environment** citeturn389027search10turn389027search2

**If you mean literally launching Altium twice and opening the same project in two separate app sessions**, that is generally **not the recommended workflow**. Altium is designed as a unified environment with multiple documents/projects open in one application, rather than two independent app instances editing the same design at once. That risks confusion, stale views, and file/version conflicts, especially on local projects. citeturn389027search1turn389027search2

So the best answer is:

- **Yes** to two windows/views: do it inside **one Altium session**
- **No real need** to run two independent Altium instances for this

For your use, I’d set it up as:
- **left screen:** SchDoc
- **right screen:** PcbDoc or SchLib
- enable **Remember window for each document kind**

If you want, I can give you the exact clicks in **26.3** to split it across two monitors.

[M16] ME (2026-03-22 17:18):
[image]
Doesn't s o work. Opened pcn and it opened in same. Do I need to open a separate altoum instance 
[attached file: IMG_E7616A0E-999A-485D-8664-738CB71A262D.jpeg]

[M17] AI (2026-03-22 17:19):
No — you normally **do not need a second Altium instance**.

What’s happening is:

- opening another document tab just opens it in the **same main Altium frame**
- to get it onto the other monitor, you need to make that document a **floating window**

Try this:

1. Open the **PCB doc**.
2. Grab the **PCB tab** at the top.
3. **Drag the tab itself** away from the tab bar and out of the main Altium window.
4. It should become a **separate floating document window**.
5. Move that floating window onto the other screen.
6. Leave the schematic/main project on the first screen.

If dragging the tab does nothing, try:
- **right-click the document tab** and look for something like **Float / Undock / New Window**
- then move that floated window to monitor 2

The key point is: simply opening the PCB while Altium is maximised will still keep it as another tab in the same container. You must **undock/float** the document.

Also check this:
- **Preferences / System / View** area
- enable anything like **desktop panels**, **separate document windows**, or **remember window for each document kind** if present

If Altium is being stubborn, then yes, a **second instance** can be used as a workaround:
- launch Altium again
- open the same project read-only if possible, or at least be careful
- use one instance for schematic, one for PCB

But I’d treat that as **plan B**, because two instances on the same project can get messy.

From your photo, I suspect you’ve only opened the PCB as another **tab**, not floated it yet.

Try dragging the **actual PCB document tab** hard out into empty desktop space — not just the inner view.
