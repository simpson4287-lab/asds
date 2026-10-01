# Unclear Explanation
Date (UTC): 2026-03-04 10:09
Conversation ID: 69a804c9-b7e0-838a-ab9d-889565de602e
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-04 10:09):
[image]
[image]
[image]
[image]
[image]
In altium using multi channel. I’ve got it working on my test project, but my realm project is it behaving the same way. This is the test project 
[attached file: IMG_C306BCF3-927A-4E8B-8E9D-84B41EC9DC4B.jpeg]
[attached file: IMG_756A03B1-4885-459D-8EDC-C404F3DCCBBD.jpeg]
[attached file: IMG_E163947D-913A-4ACF-83ED-8673713213A7.jpeg]
[attached file: IMG_B1BF008C-C9A8-4A23-A2AE-4031D4B94815.jpeg]
[attached file: IMG_64451333-688A-4904-B883-71151BCC017B.jpeg]

[M2] ME (2026-03-04 10:10):
[image]
[image]
This is my main one. Don’t understand it 
[attached file: IMG_A64C7C41-3FF7-4813-8D07-D25C8557883E.jpeg]
[attached file: IMG_1B20BECA-0F4B-41CF-B82A-A914D3FB2DFE.jpeg]

[M3] AI (2026-03-04 10:10):
I can see what’s happening from your screenshots. Your **test project is structured correctly for Altium multi-channel**, but your **real project is not actually using the hierarchical multi-channel mechanism**, even though the sheet symbol says `Repeat(...)`.

This is a very common Altium trap.

Let’s walk through what your screenshots show.

---

# What is correct in your TEST project
Your test project has the proper multi-channel hierarchy:

**Top sheet**
```
Repeat(CLK,1,4)
Sheet2.SchDoc
```

Inside that sheet you have nets like:

```
CLK_IN
SR_IN
SR_OUT
CLK_DUT
```

Altium then automatically creates channels:

```
CLK1
CLK2
CLK3
CLK4
```

And when you open the sheet tabs you see:

```
CLK1
CLK2
CLK3
CLK4
```

That means Altium is expanding the sheet **virtually into 4 instances**.

This is correct behaviour.

---

# What is different in your REAL project

Your real project structure looks like this:

```
4_Clock_Chain.SchDoc
5_Clock_Chain_2.SchDoc
6_Clock_Chain_3.SchDoc
7_Clock_Chain_4.SchDoc
8_Clock_Chain_5.SchDoc
```

So instead of **one sheet repeated**, you have **five physical sheets**.

Then on the cover sheet you wrote:

```
Repeat(CLK,1,4)
4 Clock Chain.SchDoc
```

But **Altium will only repeat ONE sheet document**.

Right now your design already has **separate sheets**, so the repeat does nothing meaningful.

Essentially you mixed two architectures:

| Architecture | Description |
|---|---|
| **Multi-channel** | One sheet repeated automatically |
| **Multi-sheet manual** | Multiple sheets duplicated manually |

Your test project = **multi-channel**  
Your real project = **manual duplication**

---

# The correct multi-channel architecture

Your project should look like this:

```
Cover Sheet
    └── Sheet Symbol
        Repeat(CLK,1,4)
        Clock_Chain.SchDoc
```

And **only one**:

```
Clock_Chain.SchDoc
```

NOT:

```
Clock_Chain_1
Clock_Chain_2
Clock_Chain_3
Clock_Chain_4
```

---

# What your project should look like

Delete these:

```
5_Clock_Chain_2.SchDoc
6_Clock_Chain_3.SchDoc
7_Clock_Chain_4.SchDoc
8_Clock_Chain_5.SchDoc
```

Keep **only one**:

```
4_Clock_Chain.SchDoc
```

Then the top sheet:

```
Repeat(CLK,1,4)
Clock_Chain.SchDoc
```

Altium will create:

```
CLK1
CLK2
CLK3
CLK4
```

---

# How you know it worked

After compile:

Open the sheet and you should see tabs at the bottom:

```
CLK1
CLK2
CLK3
CLK4
```

Just like your test project.

---

# One more thing I noticed

Your sheet title currently says:

```
Repeat(CLK,1,4)
4 Clock Chain.SchDoc
```

The **"4" in the filename is confusing the hierarchy**.

Rename the sheet to something clean like:

```
Clock_Chain.SchDoc
```

---

# The correct final structure

```
Project
 ├ Cover_Sheet.SchDoc
 │    Repeat(CLK,1,4)
 │    Clock_Chain.SchDoc
 │
 └ Clock_Chain.SchDoc
```

Nothing else.

---

# Once that is fixed

Your PCB will suddenly behave properly and you will be able to:

- replicate rooms
- route one channel
- propagate routing
- maintain matched nets

Exactly what you want for the CCD driver chains.

---

💡 If you want, I can also show you the **pro way to structure this project** for your CCD headboard because you actually have **three nested multi-channel structures**:

- Clock chains
- Wave drivers
- Bias chains

Using **nested multi-channel hierarchy** will make the PCB replication almost automatic.

And for a board like yours it saves **days of layout work**.

[M4] ME (2026-03-04 10:16):
[image]
[image]
[attached file: IMG_CCB30084-B453-499B-A5AB-A65BD9704C6B.jpeg]
[attached file: IMG_DE4E3AE0-724E-4ED2-B70F-C767C6349392.jpeg]

[M5] AI (2026-03-04 10:16):
You’re **very close now** — the structure you just showed is actually correct. The issue now is just **Altium not compiling the multi-channel expansion**, so it still behaves like a single sheet.

Let me explain exactly what I see in your screenshots.

---

## What is now correct
Your project tree shows:

```
Cover_Sheet.SchDoc
Clock_Chain.SchDoc
```

And your sheet symbol says:

```
Repeat(U_Clock_Chain,1,6)
Clock_Chain.SchDoc
```

That is **perfect multi-channel syntax**.

This means Altium should generate:

```
U_Clock_Chain1
U_Clock_Chain2
U_Clock_Chain3
U_Clock_Chain4
U_Clock_Chain5
U_Clock_Chain6
```

---

## Why it still looks like one sheet
Altium **only expands multi-channel hierarchy after compile**.

Right now the project hasn’t generated the virtual channels.

---

## Fix (this is the important step)

Do this exactly:

**Project → Compile PCB Project**

or press

```
Ctrl + K
```

Then reopen the sheet.

---

## What you should then see
At the bottom of the schematic window you should now see **channel tabs**, like your test project:

```
U_Clock_Chain1
U_Clock_Chain2
U_Clock_Chain3
U_Clock_Chain4
U_Clock_Chain5
U_Clock_Chain6
```

That means the multi-channel engine is active.

---

## If the tabs still don’t appear
Then check this setting:

**Project → Project Options → Multi-Channel**

Make sure:

```
Enable Multi-Channel Design ✔
```

and

```
Channel Naming = ChannelIndex
```

---

## One more small thing (not critical but cleaner)

Your repeat name is currently:

```
Repeat(U_Clock_Chain,1,6)
```

That will generate designators like:

```
U_Clock_Chain1_R3
```

Most engineers prefer something shorter like:

```
Repeat(CLK,1,6)
```

Which produces:

```
CLK1_R3
CLK2_R3
```

Much easier when debugging nets and rooms.

---

## When this is working correctly
Your PCB will suddenly become **very powerful**:

You will be able to:

- route **one clock chain**
- use **Design → Rooms → Replicate Layout**
- replicate all **6 channels automatically**

For something like your **CCD headboard clock drivers**, that saves **hours or days**.

---

💡 If you want, I can also show you one **very powerful trick** most Altium users never discover:

How to structure the project so you can replicate:

```
Clock chains
Wave drivers
Bias chains
```

all automatically using **nested multi-channel hierarchy**.

For a board like yours that’s basically the **professional method** used in big FPGA and detector boards.

[M6] ME (2026-03-04 10:18):
So the order is
Place reuse circuit 
Create sheet symbol on cover
Change name to repeat
Compile 

[M7] AI (2026-03-04 10:18):
Yes — that’s essentially the right flow. I’d tighten it to this exact order so Altium doesn’t “half-link” anything:

## Recommended order (clean + repeatable)

1) **Create/insert the channel sheet**
- Make the *child* sheet first (e.g. `Clock_Chain.SchDoc`)
- Paste/place your reuse block/circuit **inside that child sheet**
- Make sure it compiles clean on its own (no floating nets/power ports weirdness)

2) **Go to the top (cover) sheet**
- **Place → Sheet Symbol**
- In the sheet symbol properties, set **Sheet File Name** = `Clock_Chain.SchDoc`

3) **Add multi-channel repeat**
- Click the sheet symbol
- In the **Text** / **Parameters** for the sheet symbol, set:
  - `Repeat(<ChannelName>, <Start>, <End>)`
  - e.g. `Repeat(CLK,1,6)`

4) **Compile**
- **Project → Compile PCB Project**
- Confirm you now see channel tabs / expansion (CLK1..CLK6) and/or the Navigator shows channels.

---

## Two gotchas that bite people

- **The Repeat string is not the sheet symbol “Name” field.**  
  It must be the **Sheet Symbol designator/text** that Altium interprets (as you’re doing in the screenshots). If you only rename a parameter called “Name”, Altium may not treat it as a repeat directive.

- **Only one physical child sheet.**  
  Don’t keep `Clock_Chain_2.SchDoc`, `Clock_Chain_3.SchDoc`, etc. Multi-channel wants **one source sheet** + virtual instances.

---

## Quick verification after compile
If it worked, when you open `Clock_Chain.SchDoc` you’ll see tabs like:

- `CLK1`, `CLK2`, … `CLK6`

(or a Navigator/Compiler view showing those channels).

If you don’t see that, tell me what you see in **Messages** after Compile (often it’ll hint exactly what’s blocking expansion).

[M8] ME (2026-03-04 10:21):
[image]
[attached file: IMG_1308CC0E-D5A4-4EBE-89A9-AAF50733DB04.jpeg]

[M9] AI (2026-03-04 10:21):
This error list actually **confirms the multi-channel is now expanding** 👍  
The errors you see are **exactly what happens before annotation** in a repeated channel design.

So the behaviour is now **correct**, but the designators haven't been **made channel-aware yet**.

---

# What the errors mean

You are seeing things like:

```
Duplicate Component Designators C?
Duplicate Component Designators IC?
Duplicate Component Designators R?
Duplicate Net Names Wire NetC?_1
```

That means Altium is currently seeing something like this internally:

Channel 1
```
R1
R2
C1
IC1
```

Channel 2
```
R1
R2
C1
IC1
```

Channel 3
```
R1
R2
C1
IC1
```

Since they all have the **same designators**, the compiler complains.

Multi-channel needs **annotation to generate unique designators per channel**.

---

# The fix (this is the normal next step)

Go to:

```
Tools → Annotation → Annotate Schematics Quietly
```

or

```
Tools → Annotation → Annotate Schematics
```

Choose the option:

```
Reset All Designators
```

Then run annotation.

---

# What will happen after annotation

Your channels will become something like:

Channel 1
```
R101
R102
C101
IC101
```

Channel 2
```
R201
R202
C201
IC201
```

Channel 3
```
R301
R302
C301
IC301
```

or depending on settings:

```
CLK1_R1
CLK2_R1
CLK3_R1
```

Both are fine.

---

# The duplicate net warnings

These will **disappear automatically after annotation** because Altium will namespace the nets internally like:

```
CLK1_NET1
CLK2_NET1
CLK3_NET1
```

---

# After annotation workflow becomes

1. **Compile**
2. **Annotate**
3. **Compile again**
4. Errors gone

Then you can push to PCB.

---

# One more tip (very important for your board)

When using multi-channel for driver chains like this, enable:

```
Project Options → Multi-Channel
```

Set:

```
Component Naming = ChannelIndex
```

This makes the PCB replication **much cleaner later**.

---

# Good news

Your multi-channel architecture is now **working properly**.

You are basically at the stage where you can:

```
route one clock chain
→ replicate layout 6 times
```

Which is exactly what this system is meant for.

---

If you'd like, I can also show you a **very powerful trick used on large detector boards**:

How to make Altium auto-replicate the PCB **without using rooms at all** (much more stable for designs like your CCD driver chains).

[M10] ME (2026-03-04 10:49):
[image]
[image]
How do I delete these old bets. They won’t select 
[attached file: IMG_5010E6E7-0DF2-4F5A-9CE8-1994E2E590C0.jpeg]
[attached file: IMG_718B66DC-71BE-4915-99A2-7B84ED61A8F9.jpeg]

[M11] AI (2026-03-04 10:49):
Got it — when copper/labels “won’t select” in Altium PCB, it’s almost always one of these three things:

1) **Your selection filter is excluding them**  
2) **They’re on a different layer and you’ve got “select only on current layer” / single-layer mode behaviour**  
3) **They’re locked, or they’re not free tracks at all (they’re footprint primitives)**

Here’s the quickest, deterministic way to delete them.

---

## 1) Make sure Altium is allowed to select tracks/text
Open **Panels → Selection Filter** (bottom-right panel list).

- Hit **All Objects** (or tick at least: **Tracks**, **Pads/Vias**, **Regions/Fills**, **Strings**).
- Also open **Panels → PCB Filter** and hit **Clear** (a stale query can block selection).

Now try click one of the red tracks.

---

## 2) Fix “wrong layer / single layer mode” issues
Two keyboard checks:

- Press **Shift + S** a few times until you’re back to normal view (exits single-layer mode).
- Press **L** (View Configuration) and make sure you’re not hiding the layer they’re on.

Also: click the layer tabs at the bottom to make the right copper layer active:
- click **Top Layer** then try selecting
- click **Bottom Layer** then try selecting (those blue verticals look like bottom-layer tracks)

If you have the preference enabled “only select on current layer”, you *must* activate the correct layer first.

---

## 3) If you can select them but can’t delete: they’re locked
When you click one, look in the **Properties** panel for **Locked**.

Fast unlock options:

- **Edit → Unlock → All** (or **Tools → Unlock Objects** depending on your menus/version)
- Or box-select the area, then in Properties untick **Locked**

Then **Delete**.

---

## 4) If you cannot select them at all: they’re probably footprint primitives
This happens if those tracks/strings are actually part of a **component footprint** (embedded copper in the footprint). In that case you *won’t* pick them up as “free tracks” in the PCB.

Test:
- Click near them and see if Altium selects a whole **component** instead (even if you can’t easily see the body outline).
- Or use **Panels → PCB Inspector** and see what object type is under the cursor.

Fix:
- Right-click the component → **Edit Footprint** (or open the footprint in the library) and delete the copper/text **in the footprint**, then update the PCB.
  - If you just delete them in PCB they’ll come back next update.

---

### The “nuclear” way (when you just want them gone)
Use **PCB Filter** to grab them by type and delete:

1. Panels → **PCB Filter**
2. Enter: `IsTrack` (or `IsString`)  
3. Click **Apply**
4. Now you can delete the selection

(If you only want those in a specific area, window-select first, then apply filter.)

---

If you tell me **whether any of them highlight at all** when you click (and what the Properties panel says the object type is: Track/String/Component Primitive), I’ll point you to the exact one of the four paths above that will fix it in one shot.

[M12] ME (2026-03-04 11:06):
Ok, if I can get it working in my test project can I easily migrate it over?

[M13] AI (2026-03-04 11:06):
Yes — **you can migrate the working multi-channel scheme from the test project**, but “easy” depends on *what you’re migrating*:

- **Easy/clean:** the *hierarchy + channel sheet(s)* (sheet symbols, Repeat(), ports, harnessing)
- **Medium:** bringing over the PCB *and* keeping placement/routing
- **Hard (avoid if possible):** trying to merge into an already-messy project that still has duplicated sheets/half-linked rooms

Here’s the safest, fastest way that keeps you in control.

---

## Option A (recommended): migrate the *structure*, not the mess
**Goal:** copy the proven hierarchy + channel sheet(s) into the real project, then re-attach your real circuitry.

1) **In the test project**  
   - Identify the **top sheet** and the **child channel sheet** (the one being repeated).

2) **Copy the sheet symbol(s) from the test top sheet**  
   - Copy/paste into your real project’s cover sheet.
   - Make sure the **Sheet File Name** points to the correct child sheet in the real project.

3) **Copy the child sheet document(s)**  
   - Easiest: right-click the child sheet in the Projects panel → **Add Existing to Project** (or copy the .SchDoc file into the real project folder then add it).
   - Keep file names clean (no “4_Clock_Chain_…” numbering).

4) **Compile + Annotate** in the real project  
   - Compile
   - Annotate (reset designators)
   - Compile again  
   This is your “it’s alive” confirmation.

5) **Now move your real circuitry into the repeated child sheet**  
   - Paste the proven reuse block(s) into the child sheet (or rebuild the channel inside it).
   - Keep all per-channel nets local to that sheet; only expose what must go up via Ports.

This avoids dragging in legacy duplicates and broken links.

---

## Option B: migrate *schematic + PCB* as a known-good “module”
**Goal:** you want the repeated channels **and** their placement/routing to come across.

1) Make a “module” project from the test project:
   - Ensure it compiles clean
   - Ensure annotation is correct
   - Push to PCB and save

2) In your real project:
   - **Import the PCB** as a block only if you can accept re-linking components (often painful if designators differ)
   - Otherwise: use **Copy/Paste Special** PCB objects (placement + routing) once the real project has matching designators and rooms.

This works well only when **designators and channel naming match exactly**.

---

## The golden rule (so you don’t get burned)
**Do not copy PCB placement/routing over until:**
- the real project compiles with **no duplicate designators**
- channels exist (CLK1..CLK6 etc)
- annotation is stable

If you copy placement before that, you’ll end up with the “can’t select / ghost primitives / wrong links” mess again.

---

## Practical “migration checklist” (fast)
In the real project, before touching PCB:

- ✅ One child sheet per repeated function (e.g., `Clock_Chain.SchDoc`)
- ✅ Cover sheet has sheet symbol referencing it
- ✅ Sheet symbol text contains `Repeat(X,1,N)`
- ✅ Compile: channels appear
- ✅ Annotate: duplicates disappear
- ✅ Compile again: clean

Then push to PCB.

---

If you want, tell me which of these you’re aiming for:

1) **Just get schematic multi-channel working in the real project** (fastest, safest)  
2) **Also bring the PCB placement/routing from test into real** (doable, but must be done in a specific order)

…and I’ll give you the exact click-path for that route.

[M14] ME (2026-03-04 11:27):
Ok, I have them in the sheet as a separate PCB. I’ve prevented update of designators and renumberes all multi channel starting with 900 so no clash . How do I now get these over to main design. Won’t let me cut as was going to cut and paste 

[M15] AI (2026-03-04 11:27):
Understood. What’s blocking you is that **Altium won’t let you “cut/paste” PCB objects between different PCB documents in the naïve way**, especially when the objects are **component primitives / rooms / locked / part of a compiled multi-channel update**.

You’ve got two viable ways to bring a “module PCB” into the main PCB. One is quick-and-dirty (geometry only). The other is the *correct* way (keeps links to schematic/components).

---

## First: decide what you’re trying to transfer
### A) **Just the PCB geometry** (placement + routing + polygons)  
You don’t care if it’s linked to your real schematic components yet.  
➡️ Use **Copy / Paste Special**.

### B) **Placement/routing that stays linked to the real components in the main design**  
This is what you really want for multi-channel replication.  
➡️ Use **Rooms + Replicate Layout** in the *main* PCB once the schematic is channelised.

I’ll give you both.

---

# Option A — Copy placement/routing as raw PCB objects (works even if schematic differs)

### 1) Make sure you can actually select them
- Press **Shift+S** until normal view (not single layer mode)
- Panels → **Selection Filter** → enable **Components + Tracks + Vias + Regions + Text**
- Ensure nothing is filtered by PCB Filter panel (clear it)

### 2) Select the module area
- Drag a selection box around the whole block
- If components won’t box-select: try **Edit → Select → Inside Area** after drawing a polygon/rectangle selection

### 3) Copy (not cut)
Use **Ctrl+C** (copy).  
Don’t use cut — cut is often blocked by “from schematic / locked / component primitives”.

### 4) Paste special into the main PCB
Go to the **main PCB** then:

**Edit → Paste Special…**

In Paste Special tick what you want:
- ✅ Components
- ✅ Tracks
- ✅ Vias
- ✅ Fills/Regions
- ✅ Polygons (if needed)
- ✅ Text

Then place it.

**If it pastes but components are “dumb” / not linked:** that’s expected in Option A. It’s just geometry.

### 5) If Paste Special is greyed out or nothing pastes
That usually means what you selected are **not free objects** (they’re part of footprints) or are being blocked by selection filters/locks. In that case:
- Select the **components themselves** (click designators) rather than copper.
- Or use PCB Filter: `InComponent` / `IsTrack` etc.

---

# Option B — The correct way (recommended): replicate layout to the *real* multi-channel components

Since you’ve already renumbered the module to 900-series to avoid clashes, you’re *thinking in the right direction*, but you don’t actually need to “import” that PCB as real components.

### Proper workflow:
1) In the **main project**, get multi-channel working and annotated (no duplicate designators)
2) Push schematic → PCB (ECO) so the main PCB contains all real components
3) Ensure each channel creates **rooms** (Design → Rooms)
4) Place + route **one** channel room perfectly
5) Use:
**Design → Rooms → Copy Room Formats**
and/or
**Design → Rooms → Replicate Layout**

That will copy placement + routing to the other channels while keeping everything linked.

This is the stable method. For a repeated CCD driver chain it’s *exactly* what you want.

---

# Why you “can’t cut”
Common causes:
- Objects are **Locked**
- Objects belong to **component footprints** (can’t cut primitives unless you edit the footprint)
- You’re in a mode that restricts selection (**single layer mode**, filter query active, etc.)
- You’re selecting a **Room** or **Compile result** object rather than real primitives

Quick test:
Click one of the uncuttable items and look at the **Properties panel**:
- If it says **Component Primitive** → it’s inside a footprint
- If it says **Room** → delete/disable rooms, don’t cut
- If it says **Locked** → unlock

---

## The fastest path for you (given what you said)
If your goal is “get that laid-out channel into the main design and then replicate it”:

1) Don’t try to cut it over.
2) Get main design multi-channel + annotation clean.
3) ECO update main PCB so all real components exist.
4) Manually place/route **one channel** (you can use your module PCB as a visual reference).
5) Replicate layout across rooms.

---

If you snap me one screenshot of the **Properties panel** when you click one of the “uncuttable” items (it will say Track / Component / Room / Component Primitive), I’ll tell you *exactly* which of A or B is the correct move and the exact menu path to make it work first time.

[M16] ME (2026-03-04 11:28):
[image]
[image]
They are already in room. I need to get these into here 
[attached file: IMG_8DC02859-5372-4E86-95C7-1CB922CD6E9F.jpeg]
[attached file: IMG_41CFEC26-13E6-40B6-836C-5E5096CC8139.jpeg]

[M17] AI (2026-03-04 11:28):
Got it. You’ve got the **clock-chain layout already done in a separate PCB** (left image), and you want that **placement + routing** to land into the **main board PCB** (right image) *inside the corresponding room(s)*.

You do **not** want to “cut/paste the PCB file into another PCB” (Altium doesn’t work like that cleanly). You want to **replicate layout** from a *source room/channel* to a *target room/channel* in the main PCB.

Here’s the cleanest way that works.

---

# Best method: Replicate Layout between Rooms (keeps components linked)

## 0) Pre-conditions (must be true)
In the **main PCB**:
- The clock-chain components you want to place must already exist (from ECO).
- They must be in a **Room** per channel (which you say they are).
- The designators/netnames must match the schematic channelisation (they can be 900-series, that’s fine as long as the main PCB has the same components).

If the main PCB’s clock-chain components are *not the same* ones (different designators / different footprints / missing parts), replication will fail or go weird.

---

## 1) Put one room “source” room in a good place
In the **main PCB**, pick one room (e.g. `CLK1`) and make it your **destination reference location**.

You have two ways:

### Way A (recommended): Copy the room *format* first (outline, rotation, component classes)
- **Design → Rooms → Copy Room Formats**
- Click the **source room** (the one you’ve already placed nicely / or any room with the right shape)
- Then click the other rooms to paste the same orientation/shape

This makes room boundaries consistent so layout replication behaves.

---

## 2) Replicate placement + routing from the “done” channel to the target channels
In the **main PCB**:

- **Design → Rooms → Replicate Layout…**

In the dialog:
- **Source Room** = the channel you have fully routed/placed (e.g. `CLK1`)
- **Target Rooms** = `CLK2…CLK6`
- Tick:
  - ✅ Component Placement
  - ✅ Routed Nets
  - ✅ Vias
  - ✅ Polygons (only if you truly want them copied)
  - ✅ Component Text (optional)

Run it.

This is the “Altium-native” way.

---

# But your “done layout” is in a different PCB file
Right — so you need to make that done layout exist as the **source room in the main PCB**, at least once.

You have two options:

---

## Option 1 (clean): recreate one channel layout in the main PCB, then replicate
This sounds painful, but it’s usually fastest overall because replication then works perfectly.

You use your “module PCB” purely as a visual guide, then:
- Place + route **just one room** in the main PCB
- Replicate it to the other rooms

Given you already have the pattern, doing one channel cleanly goes quick.

---

## Option 2 (works if designators match): Copy/Paste Special from module PCB into the main PCB *only for one room*
This gets your finished room into the main PCB without manually re-routing.

### Steps:
1) Open the **module PCB** (the one with the stacked rooms)
2) **Select ONE room’s components + routing only**
   - Click the **Room** outline (so that room is active)
   - Then: **Right click → Select → Inside Room** (or similar wording)
3) **Ctrl+C**
4) Switch to the **main PCB**
5) **Edit → Paste Special…**
   - ✅ Components
   - ✅ Tracks
   - ✅ Vias
   - ✅ Text (optional)
6) Place it roughly where the target room is.

### Critical: Ensure it maps to the existing components
If the pasted components appear as *new components*, stop — that means the main PCB does not have matching component identities/designators, and you’ll create duplicates.

If it pastes and “snaps” onto existing designators, great — you now have your **source room** in the main PCB.

Then you can run **Replicate Layout** to the other rooms.

---

# Why yours isn’t just “drag it into there”
Because Altium treats PCBs as separate databases. You can’t “merge PCBs” directly. You either:
- replicate between rooms on the same PCB, or
- paste geometry and then re-associate it (fragile)

---

# What I need from you to pick the exact route (no guesswork)
On the **main PCB**, click one clock-chain component in a room and tell me:

- does it have the **same designator range** (900-series) as your module PCB?
- or is it still the original numbering?

If the main PCB is **not** using those 900 designators, Option 2 will create duplicates and you’ll hate life — in that case Option 1 is the correct play: route/place one channel in main, then replicate.

If you want, send one close-up screenshot of a component designator in:
- module PCB room (left)
- main PCB room (right)

…and I’ll tell you in one line whether you can Paste Special safely or whether you must do “one-room then replicate”.

[M18] ME (2026-03-04 12:13):
It’s doing it again where I can’t select anything 

[M19] AI (2026-03-04 12:13):
Yep — that “can’t select anything” state in Altium PCB is almost always one of a handful of toggles that gets hit accidentally (especially when you’re jumping between rooms / pasted objects).

Do these in this order — it’s the fastest way to get selection back.

---

## 1) Clear any active filter query (most common)
Open **Panels → PCB Filter** (bottom/right).

- Click **Clear** / **Clear Filter**
- If there’s a query box, delete it and press **Apply** (or just Clear)

A stale filter can make *nothing* selectable.

---

## 2) Reset Selection Filter (second most common)
Open **Panels → Selection Filter**.

- Click **All Objects** (or tick at least **Components**, **Tracks**, **Vias**, **Strings**, **Regions**)

If “Components” is unticked, it will feel like the whole PCB is dead.

---

## 3) Exit single-layer / selection-limited modes
Press these keys one by one:

- **Shift + S** (press 2–3 times) → exits single layer mode / cycles view
- **Ctrl + D** → Redraw (sometimes fixes “stuck” UI state)

Also check you’re not in an active command (route/place):
- Press **Esc** a couple of times.

---

## 4) Check you’re not locked into a room/union selection state
Sometimes after room ops you’re effectively selecting the “room object” not contents.

- Try: **Edit → Select → All** (if that selects nothing, you’re filtered)
- Or right-click → **Selection → Select Touching Rectangle** (drag a box)

If *still* nothing highlights, you’re filtered/locked.

---

## 5) Quick “nuclear reset” that always works
1. **View → Workspace Panels → System → Preferences**
2. Search “selection”
3. Temporarily disable any “only select on current layer” / “restrict selection” options if enabled
4. Back to PCB

(But usually steps 1–3 fix it in 10 seconds.)

---

## Tell me what you see so I can pin it instantly
When you click anywhere on the PCB, does the bottom-right **Properties** panel show *anything at all* (even “No object selected”)?

And: is the **PCB Filter** panel showing a query like `InRoom` / `IsComponent` etc?

If you answer those two, I’ll tell you exactly which toggle you’ve hit.

[M20] ME (2026-03-04 12:56):
Going back to the design merge. I wonder if I could turn my main design into a reuse block. And merge it all that way. Start with the design with my multichannel that’s working and add in the the main part as a reuse block

[M21] AI (2026-03-04 12:56):
Yes — that approach can work, and it’s often the **least painful** way to “salvage” a big legacy schematic into a clean multi-channel top-level.

But you need to do it in a way that **doesn’t drag the old project’s annotation/net naming chaos into the new one**.

Here’s the practical, safe way to do what you’re proposing.

---

# The right concept
You want:

- **New “clean” project** = your working multi-channel structure (top sheet + repeated channel sheets)
- **Old “main” circuitry** = imported as **one or more reuse blocks** (or better: functional pages) underneath that clean top level

That’s a good strategy **if you partition it** properly.

---

# Don’t make the entire main design a single reuse block
Technically you can, but it becomes a nightmare because:
- reuse blocks don’t like being a “whole system” (power + connectors + multiple domains)
- you end up with one enormous sheet with global nets/ports that are hard to reason about
- any small change means replacing a monster block and dealing with re-annotation

**Better:** split the old main design into **2–6 reuse blocks by function**:
- Power entry / regulation
- Digital / CPLD / interface
- Video chain
- Clock chain (now multi-channel)
- Connectors / PoGo / harness
- Misc / notes / testpoints

This gives you clean boundaries and controlled ports.

---

# Recommended migration flow (works reliably)

## 1) Start from the “working multi-channel” project (your new master)
This becomes the canonical project.

- Cover/top sheet contains:
  - `Repeat(CLK,1,6) → Clock_Chain.SchDoc`
  - plus whatever other channels you will repeat

## 2) Bring old main design in as **sheet documents**, not as a block (first)
Before reuse-blocking anything, do this:

- Copy the old project’s `.SchDoc` sheets into the new project folder
- **Add Existing to Project** in the new project
- Compile

This step is just to see what you’re dealing with in a controlled context.

## 3) Clean boundaries in the old pages
On each old functional sheet you intend to reuse:
- Replace any messy global net labels with **Ports**
- Prefer **Harness connectors** for grouped signals
- Keep power nets global if you must (GND, +5V, etc), but don’t leave random global net labels everywhere

Goal: every block has a sensible “interface”.

## 4) Turn each functional sheet into a Reuse Block (or Snippet)
Now convert **each function** into a reusable thing:

- **Design → Create Reusable Block** (wording varies by version; can be “Create Sheet Symbol From Sheet” + “Convert to Reuse Block”)
- Or use **Snippets**:
  - Select area → **Create Snippet**
  - Place snippet in top-level

**I prefer Snippets for migration** because they are less “magical” than reuse blocks and easier to debug.

## 5) Place those blocks onto your new top level
On the new top-level pages:
- Place the blocks (power, IO, video, etc)
- Wire them together via ports/harness

## 6) Then do annotation, then ECO to PCB
Only once the structure is stable:
- Compile
- Annotate (reset if needed)
- Compile again
- ECO to PCB

---

# Key gotcha: designators
Your multi-channel channels will want stable naming (CLK1_…, CLK2_… etc).

So in the “new master”:
- Keep **channel naming** consistent (use short channel IDs)
- Let Altium handle multi-channel designators
- For imported blocks, you can:
  - either keep their designators (if stable)
  - or re-annotate them into a clean range (like your 900 trick)

Either works — but **don’t mix “locked designators” and “free annotation” randomly**. Be deliberate.

---

# When this approach is *not* ideal
If your “main” design includes the PCB layout you must preserve exactly, then reuse-block migration can force re-linking work.

In that case, better is:
- keep the original project as the canonical
- refactor only the multi-channel portion into a repeated sheet
- then replicate layout via rooms

But if your priority is **getting multi-channel sane and rebuildable**, your “new master + reuse blocks” plan is solid.

---

# If you want the quickest “minimum risk” version
Do this:

1) New master project (working multi-channel)  
2) Import old design sheets as-is  
3) Choose ONE block (e.g. power) → snippet it and connect it  
4) Compile + annotate until clean  
5) Repeat block-by-block

That keeps you from breaking everything at once.

---

If you tell me roughly how many functional pages your old design is (power / digital / video etc.), I’ll propose an exact partitioning + sheet hierarchy (top sheet + child sheets + which ones should become snippets vs reuse blocks) that will keep the ECO/PCB side stable.

[M22] ME (2026-03-04 21:09):
Before I do that I’m trying to add main part to the multichannel design. Everything seems to be located in terms of links, but then eco removes all of the legacy stuff.
Chain of events
Multi channel working in project A
Copy in project b schematics and PCB.
Exclude put channel from design
Check component links with new channel b data - ok
Eco - fine - clean
Add back in the multi channel sheets
Then component links fail fully 

[M23] AI (2026-03-04 21:09):
What you’re seeing is *exactly* what Altium does when the **compiled source design changes identity mid-stream**.

Two key behaviours to keep in mind:

1) **ECO is driven by the *currently compiled schematic*.**  
If, at ECO time, a sheet is excluded (or not in the hierarchy), Altium treats those components as **not part of the design** and will happily **remove them from the PCB** as “deleted from schematic”.

2) **Component links are fragile when you change hierarchy / multi-channel after the PCB has been synchronised.**  
When you add the multi-channel sheets back in, Altium often:
- re-annotates designators (or at least changes channel prefixes)
- regenerates / changes **Unique IDs**
- changes the hierarchical path (e.g. `CLK1\U5` vs `U5`)

Result: the PCB components no longer match the compiled schematic identities → **component links collapse** → ECO then proposes deletes/adds.

So your chain of events is basically guaranteeing a “wipe”:

- You ECO with multi-channel excluded → PCB becomes “truth” for only the legacy set  
- Then you re-introduce multi-channel → compiled design identity changes → links break → ECO wants to reconcile by removing/replacing

---

## The stable workflow (do this instead)

### Rule 1: **Never ECO while sheets are excluded / half the hierarchy is missing**
If you must stage it, do staging **without letting ECO remove anything** (see below).

### Rule 2: Choose ONE “master truth” and converge to it
You either:
- keep **Project B PCB** as the master physical layout and make the schematic converge to it, **with multi-channel present from the start**, or
- start from **Project A** and import legacy schematics carefully, then regenerate PCB.

Given you want to keep the legacy PCB, do the first.

---

## Recommended sequence (keeps legacy PCB)

### 1) In ONE project (the one containing the PCB you want)
- Add **all schematic sheets**: legacy + multi-channel sheets
- Make sure the multi-channel sheet symbol(s) are correct and the project **compiles**
- Fix duplicate designators (Annotate) until compile is clean

**Do not update PCB yet**.

### 2) Stabilise annotation before any PCB sync
- **Tools → Annotation → Annotate Schematics**  
  Use a predictable scheme (channel naming + numbering) and stick with it.
- Compile again.

The goal is: the schematic has a stable identity *before* you ask the PCB to match it.

### 3) Now do **Project → Component Links**
Open the Component Links dialog and deliberately set matching to recover the links:

- Prefer **Match by Designator** (and Footprint if needed) for this recovery phase
- Avoid “Unique ID only” matching if you’ve moved sheets/hierarchy around

Then **Apply / Execute** to rebuild links.

### 4) ECO, but **do not allow removals on the first pass**
Run **Design → Update PCB Document** (ECO), but in the ECO list:

- **UNTICK all “Remove component” / “Delete…” changes** the first time
- Apply only “Add / Link / Update parameters” changes

This prevents Altium from deleting your legacy placement while you’re still relinking.

### 5) Re-check links, then do a second ECO
Once links are solid, run ECO again. Now removals (if any) will be *real*, not caused by broken identity.

---

## Why “exclude then re-include” breaks it so hard
Excluding multi-channel sheets changes the compiled project from something like:

- `CLK1\U3, CLK2\U3, ...`

to:

- `U3` (or no channel path at all)

That’s not a cosmetic change; it’s a **different component identity space**. ECO interprets that as legitimate deletion/replacement.

---

## If you’re already in the broken state (fast recovery)
1) Re-include **all sheets** (legacy + multichannel)  
2) Compile  
3) Annotate (if duplicates)  
4) Open **Component Links** and re-link by **Designator**  
5) ECO but **block deletions** on first run

That normally gets you back without losing the PCB.

---

### One clarifying check that matters (but you can answer with a screenshot)
When links “fail fully” after adding the multi-channel sheets back:
- does Component Links show **0 matched components**, or is it matching but “wrong” ones?

If you can screenshot the **Component Links** dialog (just the top half showing match criteria + counts), I can tell you exactly which match rule to use (Designator only vs Designator+Comment+Footprint) to snap it back instantly.

[M24] ME (2026-03-05 10:32):
[image]
It’s not picking up legacy schematic stuff
[attached file: IMG_9DC07F12-7FB9-448B-AB6B-73C30F581CC6.jpeg]

[M25] AI (2026-03-05 10:32):
This screenshot actually shows the **exact problem** clearly.

Look at the top of the dialog:

> **Edit Component Links between Schematic Document (Cover.SchDoc)**

So Altium is currently only looking at **Cover.SchDoc** when trying to link components.

Your **legacy components are not on the cover sheet**, they are on the other schematic pages (Power, Video, Interface etc). Therefore the left side is empty.

So the PCB components (right side) appear **unmatched**, even though the schematic actually contains them — just not on that sheet.

---

# Why this happened
You opened **Component Links from the Cover sheet**, which limits the scope to that sheet only.

With multi-sheet designs you must run component linking at the **project level**, not a single schematic.

---

# The fix (this will immediately show the legacy parts)

Close that window.

Then open it properly from the project:

### Go to
```
Project
→ Component Links
```

NOT from the schematic editor.

Now the dialog will say something like:

```
Edit Component Links between Schematic and PCB
```

(with no sheet name).

Now the left panel should populate with **all schematic components from all sheets**.

Then click:

```
Add Pairs Matched By >>
Designator ✓
```

Leave **Comment** and **Footprint** unticked for now.

This will instantly relink most of the legacy parts.

---

# Important: don't run ECO yet
After linking:

1. Click **Apply**
2. **Compile project**
3. Re-open **Component Links** and check counts.

Only then run:

```
Design → Update PCB Document
```

---

# One more thing I can see in your screenshot
Your PCB has components like:

```
P900
CLK1
```

which means your **multi-channel designators are different from the legacy numbering**.

That's fine — but it means those parts **will not match by designator**, which is expected.

What matters is that the **legacy parts (C1, R12, U3 etc)** match first.

---

# Good news
Your PCB layout itself looks intact — nothing has been destroyed.

You just need to restore the **component identity mapping** between schematic and PCB.

Once the legacy components appear in the left panel, the rest of the process becomes straightforward.

---

# If you want, send one more screenshot after opening **Project → Component Links**

I can tell you in about **10 seconds** whether the matching rule should be:

```
Designator
Designator + Footprint
Footprint only
```

which avoids the ECO wiping your board again.

[M26] ME (2026-03-05 10:33):
I have run it from PCB view projects component links 

[M27] AI (2026-03-05 10:33):
Ok — if you launched it from the PCB/Projects side and it **still** says it’s linking **Cover.SchDoc ↔ PCB**, then Altium is not treating the rest of your legacy sheets as *part of the compiled hierarchy*.

In other words: **your project is currently compiling only the cover sheet branch**, so Component Links can only “see” that sheet.

This is 100% consistent with “ECO removes legacy stuff”: from the compiler’s perspective, that legacy circuitry “doesn’t exist”.

Here’s how to fix it deterministically.

---

# 1) Make sure the legacy sheets are actually *in the hierarchy*
In Altium, sheets don’t become part of the design just because they’re listed under “Source Documents”. They must be reached via **sheet symbols** starting from the top sheet.

### On `Cover.SchDoc` you must have sheet symbols for:
- Power / Peripherals
- Digital control
- Video control
- Interfaces
- etc

If those legacy sheets are just “loose” SchDocs with no sheet symbol pointing to them, they are **orphan sheets** → compiler ignores them → links won’t appear.

✅ Quick test:
- **Project → Compile**
- Panels → **Navigator** (or **Projects / Messages**)  
If the legacy sheets do **not** show as children under the top sheet hierarchy, they’re not in the design.

### Fix:
On Cover sheet:
- **Place → Sheet Symbol**
- Set **Sheet File Name** to each legacy `.SchDoc`
- Add ports/harness later; for now you just need them included in the compile tree.

Then **Compile** again.

---

# 2) Check you’re not accidentally using a “Top-Level only”/flat compile configuration
Go:
**Project → Project Options → Error Reporting / Multi-Channel / (Hierarchy)**

Depending on your version, ensure:
- hierarchy mode is normal (not “Do not compile child sheets”)
- nothing is set to compile only the active sheet

Even if the UI differs, the symptom is the same: only one sheet compiles.

---

# 3) Confirm the legacy sheets aren’t “Excluded from compilation”
Right-click a legacy SchDoc in Projects panel and look for:
- **Exclude from compilation**
- **Enable / Disable document**
- **Remove from project** (obviously not)

Make sure they are **not excluded**.

(Excluding a sheet makes it invisible to compile, links, ECO, everything.)

---

# 4) After you fix hierarchy: rebuild links the correct way
Now do:

1. **Project → Compile PCB Project**
2. **Project → Component Links**
   - You should now see lots of schematic components on the left
3. Click **Add Pairs Matched By >>**
   - ✅ Designator
   - (Only tick Footprint if you have non-unique designators)

Then **Apply**.

---

# 5) Stop ECO from deleting anything while you’re stabilising
When you run ECO next:
- **untick all “Remove Component” / “Delete…” operations**
- Apply only “Add / Update / Link” ops first

Do a second ECO once links are stable.

---

## The key insight
**Component Links can only link what the compiler considers “in the design”.**  
Right now, the compiler thinks the design is basically just `Cover.SchDoc` + whatever sheet symbols are on it (your repeat block, etc). Your legacy sheets are not reachable, so they may as well not exist.

---

If you send one screenshot of your **Cover.SchDoc** showing the sheet symbols (Project panel + the cover sheet area), I can tell you immediately whether your legacy pages are orphaned (99% likely) or whether something else (like exclusion/variant/compile scope) is the culprit.
