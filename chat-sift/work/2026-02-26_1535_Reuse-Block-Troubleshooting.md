# Reuse Block Troubleshooting
Date (UTC): 2026-02-26 15:35
Conversation ID: 69a0681f-f4cc-8393-8392-9155b5b0e97a
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-02-26 15:35):
I got two of 3 reuse blocks working after some figuring out process. However the third one is being problematic and I think it’s to do with my method . Same through it please 

[M2] AI (2026-02-26 15:35):
Yep — let’s do it methodically. Reuse blocks in Altium are *very* sensitive to **how the snippet was created** and **what context it expects** (project/managed components/parameters/unique IDs). When one of three refuses to behave, it’s usually because that one block was produced slightly differently.

Below is a “walk the chain” checklist that will almost always expose what’s different about the bad one, plus the cleanest recovery path.

## 1) Prove what kind of snippet you actually have
Open the problematic reuse block’s snippet file (the *.SchDot / *.SchDoc snippet / *.Snip / whatever you’re using).

Check these three things:

### A) Does it reference a **Sheet Symbol / Device Sheet** boundary correctly?
- If the block was created from a sheet that had ports/harnesses, but you captured it without the same boundary objects, it’ll place but won’t wire/compile cleanly.

### B) Are the **Ports / Harness Connectors** present and named exactly as expected?
- One character difference, hidden whitespace, or case change can stop net connectivity.
- If two blocks work and one doesn’t, compare port names side-by-side.

### C) Are components in the block **real components** or “dumb primitives”?
A bad sign is if the block contains:
- components that have lost their links (no comment/footprint/parameters),
- designators shown in brackets or “?”,
- or the block compiles but doesn’t push designators/parameters as expected.

That usually means this block was made **before** you had stable library links (or from a different library mode).

---

## 2) The most common failure modes (and how to spot each quickly)

### Failure mode 1 — Duplicate Unique IDs / Designator clash on placement
**Symptom:** block places, but compile throws “duplicate unique id”, designators go bracketed, or ECO is nonsense.

**Fix (quick):**
- In the target schematic: `Tools → Reset Component Unique IDs` (or `Tools → Annotation → Reset Unique IDs`, depending on version).
- Then: `Tools → Annotate Schematics…` and re-annotate *only* what’s needed.
- Re-compile.

If you want to preserve designators: do **not** “fully annotate all”; use incremental / selected sheets where possible.

---

### Failure mode 2 — Snippet captured with “local” library references
**Symptom:** components in the block lose footprints/parameters when placed into the main project, or don’t back-annotate.

**Fix (clean):**
- Open the original source schematic that the snippet came from.
- Make sure every component is properly linked (managed or file libs) in *that* project.
- Then **re-create the snippet** from that clean source (this is often faster than debugging the broken snippet).

---

### Failure mode 3 — Net connectivity broken by port direction/type mismatch
**Symptom:** block looks wired, but nets don’t join in the parent sheet, or harnesses don’t resolve.

**Fix:**
- Standardise ports: exact names, same port type, same harness definitions.
- In the parent sheet, ensure the sheet symbol entries match the internal port names exactly.

---

### Failure mode 4 — Parameters not allowed / not resolving inside reuse blocks
**Symptom:** your “p” parameters (or any custom parameters) don’t pull through when you Update/Compile.

**Fix:**
- If you’re relying on parameters on *wires/net labels* inside the block, be aware reuse blocks can be weird about parameter propagation.
- Prefer:
  - Parameters on **components** (or on **ports**) rather than on wires,
  - Or push those parameters via the **sheet symbol** that instantiates the block.

---

## 3) The fastest compare test (do this)
Since you have 2 working blocks, use them as your reference standard.

For each of the 3 blocks, compare:

1. **How it was created**  
   - created from inside a project?  
   - created from a standalone SchDoc?  
   - created via copy/paste vs “Create Snippet”?

2. **Objects used at the interface**  
   - Ports vs Net Labels  
   - Harness connectors?  
   - Sheet entries?  

3. **Library mode** at time of capture  
   - Managed components / DBLib / File libs / “compiled integrated library”?

4. **Designator state** inside the snippet  
   - fixed designators vs “?”  
   - bracketed designators on placement?

Nine times out of ten, the odd one out jumps off the page.

---

## 4) Recovery path I recommend (lowest pain, highest reliability)
If the problematic one is *structurally correct* but behaves inconsistently:

1) Go back to the *original* schematic sheet that represents that block (the “golden” version).  
2) Ensure it compiles cleanly *as its own little project* with the same libraries as your main project.  
3) Recreate the reuse block/snippet from that sheet **again**, using the same process you used for the two working ones.  
4) Place fresh in the main project.  
5) Only then do annotation / ECO / PCB update.

This avoids chasing ghosts like stale Unique IDs and half-linked components.

---

## 5) Tell me what to look at (no extra questions, just send evidence)
To “same through it” properly, paste or screenshot any of the following and I’ll pin it down immediately:

- The compile messages for the failing block (the *Messages* panel lines)
- A screenshot of the failing block placed **next to** a working block showing:
  - ports/harnesses/sheet entries
  - designators (are they bracketed?)
- The snippet/reuse block settings dialog (where it points / how it instantiates)
- The exact symptom: “won’t wire”, “won’t keep designators”, “ECO pulls random parts”, “parameters missing”, etc.

If you give me just the compile error lines and one screenshot of the interface (ports/sheet symbol), I can usually tell you the root cause in one pass.

[M3] ME (2026-02-26 15:58):
I’m not using snippets just pasting from separate projects. Works the same it seems 

[M4] AI (2026-02-26 15:58):
Ah — that explains *exactly* why 2/3 “work” and the third goes weird.

Copy/paste between separate Altium projects can look identical on-screen, but it’s **not equivalent to a reuse block/snippet** because you’re dragging across a bunch of hidden identity + linkage state:

- **Unique IDs** (GUIDs) on components/primitives
- **Component link state** (managed vs file-lib vs DBLib)
- **Variants / parameters / model links**
- **Harness/port/net identity rules**
- **Annotation state** (designators locked, compiled ownership, etc.)

So: yes, it *can* “work the same”… until one pasted sheet has one extra gotcha (usually duplicate Unique IDs or mismatched library linkage).

Here’s the clean, repeatable “paste-from-other-project” method that makes it behave 100% like a proper reusable block.

---

## The “Paste as Reuse Block” workflow (but without snippets)

### 1) In the TARGET project (main board)
1. **Compile first** (Project → Compile) so you start from a known-good state.
2. Save.

### 2) Paste the block
Paste the sheet contents in.

### 3) Immediately de-contaminate IDs
This is the big one.

- Run: **Tools → Reset Component Unique IDs** (or similar wording) on the **newly pasted components**.
  - If Altium won’t let you do “selected only”, do it on the whole sheet; it’s still usually fine.

Why: the pasted block can carry the *same* GUIDs as the source project. If two blocks happened not to overlap (or one was already regenerated) they appear fine; the third can collide and cause bracketed designators, ECO chaos, or “not pulling through” behaviour.

### 4) Normalise designators (choose one strategy)
Pick one of these and stick to it:

**Strategy A — keep designators from the source block**
- Before copy: in the SOURCE project, make sure designators are final and locked how you want.
- After paste: run **Annotate Schematics**, but configure it to **only annotate “?”** or only the new sheet (depending on dialog options).
- Avoid global re-annotation.

**Strategy B — let the main project own all designators**
- After paste + Reset Unique IDs: run **Annotate Schematics** on the main project and let it assign everything cleanly.

Mixing strategies across blocks is another reason “2 work, 1 doesn’t”.

### 5) Re-link components to the TARGET libraries
This is the second big one.

If your third block came from a project that used a different library source (even subtly), you can paste parts that *look* right but aren’t resolvable the same way when compiling/updating PCB.

Do this in the TARGET:
- **Tools → Update From Libraries** (or Equivalent) for those components
- Or use the **Properties** panel to confirm:
  - the component’s **source** (managed component / file library / DBLib)
  - the **footprint model** is present and resolves
  - key parameters exist (your “p” etc.)

If you paste from Project A into Project B, but Project A had libs in its Installed Libraries list that Project B doesn’t, you’ll get “half alive” components.

### 6) Compile + inspect Messages
Now compile and look specifically for:
- Duplicate Unique ID warnings
- Components not found / models not found
- Net/harness/port mismatch warnings

---

## Why only the third block fails (typical causes)
When paste works twice and fails once, it’s usually one of these:

1) **That block was copied from an older revision** (so it carried legacy GUIDs / older library refs)
2) **That block includes harness/ports/off-sheet connectors** where name/type differs slightly vs your other blocks
3) **It has locked designators or “special” annotation state** (copy brings the lock state too)
4) **It includes compiled primitives that don’t merge cleanly** (rare, but happens with harnesses / multi-part / variants)

---

## Quick diagnostic: 30-second checks
On the failing pasted block, click one component and look at its Properties:

- Does it show a clean library source, or does it look “unlinked”?
- Is the footprint listed and resolvable?
- Are designators bracketed or showing as “?” after compile?
- Do nets connect through sheet ports properly (highlight a net and see if it propagates)?

---

## If you want the simplest “make it behave” fix
Do this order on the failing one:

1) Delete the pasted block from the main project.
2) Paste again.
3) **Reset Component Unique IDs** immediately.
4) **Update From Libraries** immediately.
5) Compile.

That sequence alone fixes most “3rd one is cursed” cases.

---

If you drop **one screenshot of the compile Messages panel** after placing the bad block (and ideally one showing the bracketed designators / missing params behaviour), I’ll tell you *exactly* which of the above is biting you and the precise menu path in your Altium version.

[M5] ME (2026-02-26 15:59):
Differentiate between schematic and layout blocks and seance instruction 

[M6] ME (2026-02-26 16:00):
No, in your instructions above you say block, which block, more specific in sequence and instruction for creating reuse blacks please 

[M7] AI (2026-02-26 16:00):
Got you — I was being sloppy with the word **“block”**. In Altium there are *three different “block-like” things* people conflate:

## 1) What “block” means in Altium (be precise)

### A) Schematic reuse block (what you want)
A **schematic reuse block** is a *schematic-level* chunk you can place repeatedly:
- Implemented via **Snippet / Reuse Block / Device Sheet** workflows
- Contains **schematic objects** (components, nets, ports, harnesses, parameters)
- Goal: repeat circuitry cleanly on schematic, then ECO into PCB

### B) PCB layout “block” (not the same thing)
A **PCB block** (copy/paste rooms, copy component groups, replicate layout, etc.) is *PCB-level*:
- Implemented via **Rooms / Copy Selected / Paste / Replicate**
- Contains **footprints, placement, routes, polygons**, etc.
- Goal: repeat placement/routing patterns
- It does **not** solve schematic identity/linkage problems

### C) What you’re currently doing (manual copy/paste between projects)
This is neither a true reuse block nor a PCB block:
- It’s **raw clipboard copy** of schematic primitives from another project
- It can work, but you must “sanitize” IDs + relink libraries, or it becomes inconsistent (exactly what you’re seeing)

---

## 2) Your requested deliverable: exact sequence for creating schematic reuse blocks

Below are two solid methods. Use **Method 1** if you want the closest thing to “Cadstar-style reuse”. Use **Method 2** if you want a “drop-in circuit chunk” fast.

---

# Method 1 (Recommended): Device Sheet + Sheet Symbol (most robust reuse)
This is the “real” hierarchical reuse approach.

### Step-by-step
1) **Create a Device Sheet**
   - Create a new schematic document that will *only* contain the reusable circuit (e.g. `PowerStage.SchDoc`)
   - Put the circuit inside it.

2) **Define the interface**
   - Use **Ports** (Place → Port) for every external connection.
   - Name ports exactly how you want the parent sheet to see them (`VIN`, `VOUT`, `EN`, `SCL`, etc.)
   - For buses/harness: use Harness Connectors / Harness Entries consistently.

3) **Make it a “Device Sheet” / reusable sheet**
   - In many Altium setups this is just a disciplined hierarchical sheet.
   - (If you have the explicit “Device Sheet” feature enabled, use it; otherwise the standard hierarchical approach still works.)

4) **Instantiate it in the top sheet**
   - On your top-level schematic: Place → **Sheet Symbol**
   - Point it at `PowerStage.SchDoc`
   - Then **Sheet Entries** can be auto-generated from ports (right-click sheet symbol options) depending on settings/version.

5) **Repeat instances cleanly**
   - Copy the *Sheet Symbol* to make “instances” (e.g. `PSU_A`, `PSU_B`, `PSU_C`)
   - Use **Parameters on the Sheet Symbol** (e.g. `CHANNEL=A`) if you need per-instance variation.

6) **Compile and ECO**
   - Project → Compile
   - Design → Update PCB Document

**Why this works:** every instance has its own identity; Altium expects this pattern; far fewer GUID/designator nightmares.

---

# Method 2: Snippet / Reuse Block (fast chunk reuse)
This is what most people mean by “reuse block” in casual talk.

### Create the reuse block
1) Open the source schematic containing the circuit.
2) Select the circuit area (components + wires + ports/harness you want).
3) Create snippet / reuse item:
   - Tools → **Snippets** (or Place → Snippet, depending on version)
   - Create snippet from selection
4) Save it in a known location (preferably under version control).

### Place the reuse block
1) In the target schematic:
2) Place the snippet (the reuse block)
3) **Immediately after placing**:
   - Reset Unique IDs (if your workflow/version requires it)
   - Update from libraries (to ensure all links resolve)
4) Compile + ECO

**Why this works better than clipboard:** it’s a managed chunk with expected behaviour, rather than raw pasted primitives.

---

## 3) Where my earlier “block” fits in the sequence (for your current paste-based method)

If you insist on copy/paste between projects, here is the **exact sequence** and what each “block” refers to:

### Sequence: “Clipboard Reuse Block” (manual but repeatable)
**In SOURCE project**
1) Compile source project (so it’s “clean”)
2) Confirm library links are valid (no “not found” parts)
3) Select the circuit area you want to reuse (this selection is the “block”)
4) Copy

**In TARGET project**
5) Paste onto a dedicated sheet (or correct location)
6) Run **Reset Component Unique IDs** (critical)
7) Run **Update From Libraries** (critical)
8) Run **Annotate Schematics** using your chosen strategy:
   - Either only annotate “?” or annotate selected/new sheet
9) Compile
10) ECO to PCB

If step 6 or 7 is skipped, you get the classic “two work, third goes rogue” behaviour.

---

## 4) Minimal rule-set so you don’t get bitten again
- **Schematic reuse = hierarchical device sheet** (best) or **snippet** (okay)
- **PCB reuse = rooms / replicate layout** (separate topic)
- **Clipboard reuse must include:** reset unique IDs + relink libraries + controlled annotation

---

If you tell me which Altium flavour you’re on (Altium Designer version number is fine) and whether you want **hierarchical sheet reuse** (Device Sheet approach) or **drop-in chunk reuse** (Snippet approach), I’ll tailor the exact menu paths and the “do this / don’t do this” rules to your setup.

[M8] ME (2026-02-26 16:11):
[image]
Ok, this is a problem, I’ll get a bit tangled up with libraries 
[attached file: IMG_72C07E78-8310-4350-9386-B2A719818264.jpeg]

[M9] AI (2026-02-26 16:12):
Yep — that screenshot is *exactly* the “why my 3rd copied block is cursed” symptom.

You’re in **Update From Libraries** (or similar) and a chunk of parts are showing **Library Name = `<Not Found>`**.

That means:

- The schematic components you pasted **still reference the source project’s libraries** (by library name / library path / component key),
- …but your *current* project does **not** have those libraries available in its search path,
- so Altium can’t resolve them → you get inconsistent compile/ECO/parameter behaviour.

### What you’re looking at in the table
- Rows that say `Blocks.SCHLIB` are fine (Altium can find that library).
- Rows that say `<Not Found>` are the problem parts. They’ll still “exist” on the schematic, but they’re effectively **unlinked** (so updates, parameters, footprint links, etc. become unpredictable).

---

## Fix it cleanly (recommended): make the target project able to resolve the same libs

### Step 1 — Don’t press Finish yet (unless you’ve already mapped them)
If you press **Finish** while lots are `<Not Found>`, you’re basically accepting a half-broken library state.

Hit **Cancel** for now.

### Step 2 — Identify *which* libraries are missing
On the schematic, click one of the offending components → **Properties** panel.

Look for fields like:
- **Library Reference / Source / Component Link**
- Anything that indicates *where the symbol came from* (library name/path, vault/managed component, DBLib, etc.)

You’re trying to answer: *“What library did this come from in the source project?”*

### Step 3 — Add those libraries to the TARGET project (so `<Not Found>` becomes found)
In the target project:

1) **Panels → Components** (or Libraries panel)
2) Make sure the missing SCHLIBs/IntLibs are available via one of:
   - **Project Libraries** (best for stability): add the `.SchLib` / `.IntLib` files into the project
   - Or **Preferences → Data Management → File-based Libraries** (Installed libraries) if you prefer global

**Best practice:** keep a folder like  
`/Libraries/Blocks/Blocks.SchLib` (+ matching `.PcbLib` or `.IntLib`)  
and add that to every project that uses these reusable circuits.

### Step 4 — Run Update From Libraries again
Now go back:
- **Tools → Update From Libraries…**

Those `<Not Found>` entries should now resolve.

### Step 5 — Then (important) sanitize after copy/paste reuse
After you paste a reusable circuit from another project, do this order:

1) Paste
2) **Tools → Reset Component Unique IDs** (avoid GUID collisions)
3) **Tools → Update From Libraries**
4) **Annotate** (using one consistent strategy)
5) Compile
6) ECO to PCB

That sequence prevents the “2 work, 1 breaks” randomness.

---

## If you *can’t* get the missing libraries (quick salvage option)
If you don’t have the original libs, you can still recover:

1) In that Update From Libraries dialog, for each `<Not Found>` row:
   - select it
   - click **Choose Component…** (bottom-left)
   - map it to an equivalent part in your current libraries  
2) Then Finish.

This is slower and riskier (easy to map wrong footprints), but it gets you unstuck.

---

## The real root cause (so it doesn’t happen again)
Copy/paste reuse across projects only behaves nicely if **all reusable circuits pull parts from a common, portable library set** (or managed components).

If one of your three source projects was using a slightly different library setup (even just one resistor symbol library), that third paste will produce exactly what you’re seeing.

---

If you send **one close-up screenshot of the Properties panel** for one of the `<Not Found>` components (showing its “Source/Library Reference/Link” fields), I can tell you *precisely* whether it’s:
- missing file-based SCHLIB/IntLib,
- DBLib/SQL lib link,
- managed component link,
- or just a library-name mismatch.

[M10] ME (2026-02-26 16:14):
That’s what I did with the previous 2 jobs, local
Libraries, but things were getting messy 

[M11] AI (2026-02-26 16:14):
Yep — that “local libs per job” approach *works* short-term, but it inevitably turns into spaghetti once you start reusing circuitry across projects (exactly where you are now).

Here’s the clean way to stop it getting messier **without** forcing you into a full corporate managed-content rollout.

## What’s going wrong with “local libs”
When you paste circuitry from Project A into Project B, each schematic component carries a pointer like:

- “I came from **X.SchLib** component **R_0402**”
- plus model links (“this footprint lives in **Y.PcbLib**”)

If Project B doesn’t have those exact libs (or has a different file with the same name), you get:
- `<Not Found>` in Update From Libraries
- bracketed designators / weird ECO
- parameters not pulling consistently
- footprints going missing later

So the goal is: **one common library set**, referenced consistently, for everything you intend to reuse.

---

# A pragmatic, low-drama library strategy that fixes this

## Option A (recommended): One shared “Blocks” library set
Create a single shared folder (can still be “local” on your machine, but common across projects):

```
...\Altium_Libs\
   Symbols\Blocks.SchLib
   Footprints\Blocks.PcbLib
   Integrated\Blocks.IntLib   (optional)
```

### Rules:
1) **Every reusable circuit only uses parts from this shared set** (or from your main master libs).
2) Each project references *the same path* to those libs.
3) Never keep “random extra libs” inside individual projects unless they are truly project-specific.

### How to implement quickly
- Put your existing working libraries into that shared folder (don’t duplicate copies).
- In Altium:
  - Add them as **Installed Libraries** (global), *or*
  - Better: add them as **Project Libraries** by linking to the same shared files.

**Result:** copy/paste between projects stops breaking, because the target project can always resolve the same library sources.

---

## Option B: Package reusable blocks as an Integrated Library (IntLib)
If you want reuse blocks to be portable and “self-contained”:

1) Create a small “library project” that builds an **IntLib**
2) That IntLib contains the symbols + footprints you need for your reusable circuitry
3) Add that IntLib to every project that uses those blocks

**Result:** fewer missing links, easier sharing, but updating parts becomes more “build the IntLib” discipline.

---

# What I would do in your exact situation (today)
Because you already have `Blocks.SCHLIB` and you’re seeing `<Not Found>`:

## Step 1 — Stop the bleeding
- Pick ONE canonical location for `Blocks.SchLib` (and matching PcbLib/IntLib)
- Delete/ignore all duplicates lying around in old project folders

## Step 2 — Make every project point to the same canonical libs
For each project:
- Add the canonical libs as **Project Libraries** (or Installed if you prefer global)
- Verify Update From Libraries shows **no `<Not Found>`**

## Step 3 — Normalise the “problem block” project
Open the source project that produced the troublesome paste:
- Ensure it uses the **same canonical libs**
- Then re-copy the circuitry into your main project
- Immediately run:
  1) Reset Unique IDs  
  2) Update From Libraries  
  3) Compile

That usually fixes the third one instantly.

---

# A simple “library hygiene” checklist (to keep it tidy)
- **One folder** = one truth source for your reusable libs
- **No duplicated library filenames** in different folders (Altium will happily pick the wrong one)
- Put a version tag in the lib name if needed: `Blocks_v1.SchLib`
- If a component is truly project-specific, keep it in `ProjectName_ProjectOnly.SchLib` so it’s obvious

---

## Quick question (but you can answer with a screenshot instead)
Are your `<Not Found>` parts meant to come from:
- the same `Blocks.SchLib` (but Altium can’t locate the file), **or**
- other “random” SchLibs that only existed in the source projects?

If you open one `<Not Found>` component’s **Properties** and show the “Source / Library Reference” bit, I’ll tell you exactly which camp you’re in and the fastest path to clean it up.

[M12] ME (2026-02-26 16:19):
So if I put the libraries in the folder, is this easy to resolve?

[M13] AI (2026-02-26 16:19):
Yes — **if you put the correct libraries in a known folder and make Altium point to them consistently**, this becomes straightforward to resolve. The key is: *Altium must be able to find the exact SCHLIB/IntLib (and matching PCB models) that the pasted components reference*, and you must avoid duplicates with the same filename.

Here’s the clean, low-risk way to do it.

## 1) Put libs in a single “canonical” folder
Example:

- `D:\Altium_Libs\Symbols\Blocks.SchLib`
- `D:\Altium_Libs\Footprints\Blocks.PcbLib` *(or an IntLib that contains both)*

**Rule:** only one copy of `Blocks.SchLib` on your machine (or at least only one copy that Altium can see).

## 2) Make the *target project* aware of that folder (preferred: Project Libraries)
In the target project:
1. Open the **Projects** panel
2. Under the project, find **Libraries** (or right-click the project)
3. **Add Existing to Project…** and add:
   - `Blocks.SchLib`
   - and the corresponding `Blocks.PcbLib` (or `Blocks.IntLib`)

This is the most stable approach because the project explicitly carries the library references.

*(Alternative: add them as Installed Libraries globally in Preferences, but project-level is less “mystery behaviour”.)*

## 3) Re-run “Update From Libraries”
Now go:
- **Tools → Update From Libraries…**

Your `<Not Found>` rows should flip to a real library name.

If they *don’t*, it’s usually because of one of these:
- The component is pointing to a *different library name* than the one you added
- You added a library file, but it doesn’t contain that component name
- There are duplicate library files with the same name and Altium is picking the wrong one

## 4) If some still show `<Not Found>`: map them in the dialog
In that same dialog:
- Select the `<Not Found>` rows
- Click **Choose Component…**
- Pick the correct symbol from your now-available libraries

After that, Finish.

## 5) Do the two “post-paste stabilisers”
After the library links are resolved, do:
1) **Reset Component Unique IDs** (prevents weird collisions)
2) **Compile** (check Messages)
3) Then ECO to PCB

---

# What “easy” looks like in practice
- If all those `<Not Found>` parts are supposed to come from `Blocks.SchLib` (or a small set of libs you actually have): **it’s a quick fix**.
- If they came from lots of one-off libraries scattered across old projects: you can still fix it, but you’ll spend time either **collecting those libs** or **mapping

[M14] ME (2026-02-26 16:20):
No, I mean pu then in the project folder, like the other blocks 

[M15] AI (2026-02-26 16:20):
Yes — putting the libs **in the project folder** can be easy to resolve, *as long as you do it deliberately and consistently*.

The key is: you must make Altium treat those files as **Project Libraries**, and you must avoid having multiple different copies of “the same” library name across projects (that’s how it gets messy).

## The clean “project-folder library” method

### 1) Create a standard libs subfolder in every project
Inside each project root:

```
<ProjectRoot>\
   Libs\
      Symbols\
      Footprints\
      (optional) Integrated\
```

Put your `Blocks.SchLib` and matching `Blocks.PcbLib` (or `Blocks.IntLib`) in there.

### 2) Add them to the project properly
In Altium:
- Add the `.SchLib` / `.PcbLib` / `.IntLib` **to the project** (so they appear under the project tree), and/or
- Use the Libraries panel to add them as **Project Libraries**.

(You want them discovered via the project, not via some random installed library list.)

### 3) Re-link the “Not Found” parts
Now run:
- **Tools → Update From Libraries…**

Those `<Not Found>` rows should turn into the correct library name and you can **Finish**.

### 4) Lock down the “copy/paste reuse” sequence
After pasting circuitry from another project:
1) Paste
2) **Reset Component Unique IDs**
3) **Update From Libraries**
4) Compile

This prevents the “two work, one doesn’t” behaviour.

---

## The one big trap (why this can still get messy)
If every project has its own copy of `Blocks.SchLib`, you’ll end up with:
- Project A: `Blocks.SchLib` (version 1)
- Project B: `Blocks.SchLib` (version 2)
- Project C: `Blocks.SchLib` (version 3)

Then copy/paste between them becomes ambiguous, and “Update From Libraries” may map to the *wrong* copy depending on search order.

### To avoid that trap, choose one policy:

**Policy A (portable projects):**  
Project-folder libs are allowed, but **version the filename**:
- `Blocks_v1.SchLib`, `Blocks_v1.PcbLib`
- If you change the library, bump the version.

**Policy B (single source of truth):**  
Keep one master library folder outside projects, and projects only *reference* it.

Policy A is usually best if you move projects between machines / want self-contained archives.

---

## What I’d do for you, right now (fastest fix)
Since your Update From Libraries shows `<Not Found>`:

1) Copy the missing library files used by that block into:
   - `ProjectRoot\Libs\...`
2) Add those libs to the project (so Altium sees them as project libs)
3) Run **Update From Libraries** again
4) Finish

That will resolve it cleanly **provided the missing parts truly exist in those libs**.

---

If you want, tell me what library files you currently have for those blocks (e.g. `Blocks.SchLib` only? or also `Blocks.PcbLib` / `IntLib`), and I’ll tell you the best of the two policies for your situation.

[M16] ME (2026-02-26 16:20):
Ok, tell me method to get everything bonded back to local libraries in folder 

[M17] AI (2026-02-26 16:20):
Got it. You want a **repeatable method** to take a schematic you’ve copied/pasted (or inherited) and **re-bind every component** so it references **local libraries sitting in the project folder** (e.g. `.\Libs\Symbols\` and `.\Libs\Footprints\`), with *no* `<Not Found>` and no hidden dependency on old projects.

Below is the workflow I use for “make this project self-contained”.

---

## Folder structure (do this first)
Inside your project root:

```text
<Project>\Libs\Symbols\
<Project>\Libs\Footprints\
(optional) <Project>\Libs\Integrated\
```

Put in:
- your local symbol libs: `*.SchLib` into `Symbols\`
- your local footprint libs: `*.PcbLib` into `Footprints\`
- OR a built `*.IntLib` into `Integrated\` (if you prefer IntLib)

**Tip:** If you have both SchLib + PcbLib, don’t rely on SchLib alone — the footprint links often live in the component models.

---

## Step-by-step: bind schematic components back to local libs

### Step 1 — Add the local libs as *Project Libraries*
In Altium (target project):

1) **Projects panel** → right-click the project
2) **Add Existing to Project…**
3) Add:
   - all needed `.\Libs\Symbols\*.SchLib`
   - all needed `.\Libs\Footprints\*.PcbLib` (or your `.\Libs\Integrated\*.IntLib`)

Now the libs appear under the project tree, and Altium can resolve them reliably.

---

### Step 2 — Force a re-link pass using “Update From Libraries”
1) Open any schematic in the project
2) Run: **Tools → Update From Libraries…**
3) In the dialog you screenshotted:
   - Anything showing `<Not Found>` means Altium still can’t match it
   - For each `<Not Found>` group:
     - select the rows
     - click **Choose Component…**
     - pick the correct component from your **project-local** libs
4) Finish

This step rebinds the **symbol** source (and often brings parameters back in line).

---

### Step 3 — Verify footprints are coming from local libs too
Now you need to confirm each component has a valid footprint model:

1) Click a few key components on the schematic
2) In the **Properties** panel, find **Models / Footprint**
3) Confirm the footprint name exists in your local `*.PcbLib` (or IntLib)

If you find missing footprints:
- open the relevant `*.PcbLib` and confirm the footprint exists
- then run **Update From Libraries** again (or manually re-add footprint model)

---

### Step 4 — Kill “stale identity” after copy/paste reuse
Do this *after* the library rebinding, especially if you pasted from other projects:

- **Tools → Reset Component Unique IDs** (run on the sheet or whole project)
- Then **Project → Compile**

This prevents weird ECO behaviour and designator bracket madness.

---

### Step 5 — Push the corrected binding into PCB (if you have a PCB)
1) **Design → Update PCB Document…**
2) In the ECO, check that:
   - footprints are correct
   - no unexpected component substitutions occurred

---

## “Make everything local” checklist (what success looks like)
- **Tools → Update From Libraries** shows no `<Not Found>`
- Components show a real **Library Name** (your local libs)
- Footprints resolve from your local `PcbLib` / `IntLib`
- Compile has no “component not found” / “model not found”
- ECO is predictable

---

## Two common gotchas (worth avoiding)
1) **Duplicate library filenames**
   - If you have `Blocks.SchLib` in 3 places, Altium can bind to the wrong one.
   - In a self-contained project, keep *one* copy in `.\Libs\...`.

2) **Library component names don’t match**
   - If the schematic calls the part `100R-0402-RC32` but your lib calls it `R_100R_0402`, automatic matching may fail.
   - That’s when you use **Choose Component…** in bulk.

---

## If you want, I can make it surgical
If you send:
- a zoomed shot of one `<Not Found>` row (showing the component name columns),
- and the **Properties panel** of that component on the schematic,

…I’ll tell you whether Altium can auto-match it (name/ID match) or whether you’ll need a manual “Choose Component” mapping pass, and the quickest way to do it in bulk.

[M18] ME (2026-02-26 16:23):
[image]
Yes but how do I get them all the same and local 
[attached file: IMG_99C54BFF-BEAA-41AE-94A4-3485F6E8A1CB.jpeg]

[M19] AI (2026-02-26 16:23):
Right — your screenshot is the “index” view of **Update From Library** showing that your design is currently pulling symbols from **multiple SCHLIBs**:

- `Blocks.SCHLIB`
- `CS_SCM_Lib.SCHLIB`
- `CLK.SCHLIB`
- `CLK.SCHLIB` etc.

You’ve got two distinct goals mixed together:

1) **Local** = the libraries live inside *this project folder* (portable, self-contained)  
2) **All the same** = every component resolves from a *single* library (or at least a single controlled set)

You can absolutely do both. Here are the two sane ways, pick one.

---

## Option 1 (fastest, least disruption): Keep multiple libs, but make them all local
This makes the project self-contained without forcing you to merge libraries.

### A) Create local lib folders
In your project folder:
- `.\Libs\Symbols\`
- `.\Libs\Footprints\` (if you use local PCB libs too)

### B) Copy the required SCHLIB files into that folder
Copy **the actual library files** you’re using:
- `Blocks.SchLib`
- `CS_SCM_Lib.SchLib`
- `CLK.SchLib`
…into `.\Libs\Symbols\`

### C) Add them to the project as *Project Libraries*
In Altium:
- **Projects panel → right-click project → Add Existing to Project…**
- add those SCHLIBs from `.\Libs\Symbols\`

### D) Rebind the schematic to these local copies
Now run:
- **Tools → Update From Libraries…**
- Step through and ensure there are **no `<Not Found>`**
- Finish.

✅ Result: everything stays split across multiple libs, but they’re **all local and stable**.

**This is the best move if you just want it working cleanly today.**

---

## Option 2 (what you’re actually asking): Make everything come from ONE local library
This is “all the same”.

### Overview
1) Create a new local “master” symbol lib in the project folder  
2) Copy/merge the required components from the other SCHLIBs into it  
3) Replace/relink the schematic components so they all point at the master

### Step-by-step

#### 1) Create a new master SCHLIB
- File → New → Library → **Schematic Library**
- Save as: `.\Libs\Symbols\Project_Master.SchLib`

#### 2) Merge symbols into it
Open each source SCHLIB (`Blocks`, `CS_SCM_Lib`, `CLK`) and copy the needed components into `Project_Master.SchLib`.

**Important rule:** if there are name clashes (same component name exists in two libs), rename one *now* in the master so you don’t create ambiguous links.

#### 3) Add ONLY the master library to the project (temporarily)
To force relinking cleanly, do this:
- Keep `Project_Master.SchLib` as a Project Library
- Temporarily remove/disable the other SCHLIBs from the project (or at least ensure the master is the only available one)

#### 4) Re-link schematic components to the master
Now you need to “swap” each placed component to the one in the master library.

The most reliable method is:

- **Tools → Update From Libraries…**
- For any line that doesn’t already resolve to `Project_Master.SchLib`:
  - select the row
  - click **Choose Component…**
  - pick the equivalent component from `Project_Master.SchLib`

Do it group-by-group (resistors, caps, testpoints, ICs). Once mapped, Finish.

#### 5) Re-add other libs only if you still need them
Ideally, once everything is bound to `Project_Master.SchLib`, you don’t need the others for this project.

✅ Result: everything points at **one local library**.

---

## Which option should you choose?
- If you’re untangling this project and want stability **now**: **Option 1**
- If you’re building a reusable “block ecosystem” and want sanity long-term: **Option 2**, but accept you’ll spend time doing the mapping once.

---

## One thing I need you to check (quick)
In your screenshot, you’re only looking at **schematic symbol libraries**. Do you also need footprints to be local?

If yes, we should do the same for:
- `*.PcbLib` (or `*.IntLib`) in `.\Libs\Footprints\` and make sure each component’s footprint model resolves locally too.

If you tell me whether your footprints are coming from local PcbLibs, an IntLib, or a managed library, I’ll give you the exact “make PCB models local as well” sequence.

[M20] ME (2026-02-26 17:38):
[image]
On the properties it says it finds the library, on the library update panel it says it can’t . Is it because it’s a reuse block 
[attached file: IMG_BA1402D4-D0C0-4B68-87FC-83BEB1F22A59.jpeg]

[M21] AI (2026-02-26 17:38):
Not because it’s a reuse block. What you’re seeing is a **linkage mismatch**:

- The **component instance** on the schematic still *remembers* its **Source = `CS_SCM_Lib.SCHLIB`** (that’s what the Properties panel is showing).
- But **Update From Libraries** is trying to actually **locate that library component in the currently-available libraries/search path** so it can compare and update it.
- Right now, Altium can’t resolve that source library/component *for the update operation*, so it flags it as **`<Not Found>`** in the update table.

So: **Properties shows what it *thinks* it’s linked to; Update panel shows what it can *actually* find right now to update from.** Those can disagree.

This usually happens for one of these reasons (in order of likelihood):

## 1) You have the library file, but it’s not in the library search path used by Update
“Source” is just text metadata. Update From Libraries needs the library to be loaded as an **Available/Installed/Project** library.

✅ Fix:
1) Put `CS_SCM_Lib.SchLib` into your project folder: `.\Libs\Symbols\`
2) In **Projects panel** → right-click project → **Add Existing to Project…**
3) Add `CS_SCM_Lib.SchLib` (from that local folder)
4) Re-run **Tools → Update From Libraries…**

If it now resolves, you’re done.

## 2) There are *two* libraries with the same name, and Update is looking at the wrong one (or none)
Altium can get confused if you have multiple copies of `CS_SCM_Lib.SchLib` in different places, or you renamed/moved it.

✅ Fix:
- Ensure only **one** copy is referenced (project-local is best)
- Remove/disable the other instances from Installed Libraries
- Restart Altium if it’s holding onto stale paths
- Re-run Update From Libraries

## 3) The library is loaded, but the component name doesn’t exist in that library
In your Properties panel:
- **Design Item ID = `EL7457CLZ_CPS`**
- **Source = `CS_SCM_Lib.SCHLIB`**

Update panel will say `<Not Found>` if **that exact component** isn’t inside the loaded `CS_SCM_Lib.SchLib` (e.g. it was renamed, or you’re loading a different revision).

✅ Fix:
- Open `CS_SCM_Lib.SchLib`
- Search for `EL7457CLZ_CPS`
  - If it’s not there: you’re pointing at the wrong lib file/revision.
  - If it *is* there: it’s a path/search-order issue.

## 4) “Full Replace” behaviour is off / restricted
Your update dialog text mentions that **Full Replace is not being performed**. When Full Replace is constrained, Altium can be picky about “found vs not found” in that UI.

✅ Fix:
- In the Update dialog, click the **Advanced** / settings on that page (if available in your version) and ensure it’s allowed to fully match/replace.
- But: this is usually secondary; if the lib is correctly loaded it will still stop saying `<Not Found>`.

---

# The quickest way to prove which case you’re in (30 seconds)
1) Open `CS_SCM_Lib.SchLib` directly in Altium (File → Open).
2) Use the library search/filter for `EL7457CLZ_CPS`.

### Outcomes:
- **Found in the library** → your issue is *library availability / path / duplication* (Fix #1/#2).
- **Not found** → you’re loading the wrong file or it was renamed (Fix #3).

---

# Why reuse blocks feel implicated (but aren’t the root cause)
Reuse blocks / copy-paste can *introduce* components whose **Source** points at some other project’s library setup — so they *trigger* this situation — but the mechanism is still just: **library not loaded / wrong revision / duplicate libs**.

---

## Do this now (most likely fix)
Because your project clearly has multiple libraries involved, I’d do:

1) Create `.\Libs\Symbols\`
2) Copy in: `Blocks.SchLib`, `CS_SCM_Lib.SchLib`, `CLK.SchLib` (every lib showing in your earlier list)
3) Add them all to the project via **Add Existing to Project**
4) Remove/disable any global Installed Library copies of those same files (to prevent ambiguity)
5) Restart Altium (optional but often clears cached library pointers)
6) Run **Update From Libraries** again

If you want, send a screenshot of your **Projects panel → Libraries section** (just the list of libraries currently attached/installed) and I’ll tell you exactly what to remove/keep so Update From Libraries stops lying to you.

[M22] ME (2026-02-26 17:49):
Back to reuse 
I’ve pasted in the circuit
Now I will annotate the references? Do I do this before adding the PCB block?

[M23] AI (2026-02-26 17:49):
Do the **PCB block after** you’ve stabilised the schematic.

Reason: the PCB “block” (placement/room/replicated layout) only makes sense once the schematic components have **final designators + stable unique IDs**, otherwise you end up copying a layout tied to parts that later renumber or collide.

Here’s the correct sequence when you paste a reusable circuit into an existing project.

## Correct sequence (schematic-first, then PCB)

### 1) Paste the circuit into the schematic
Paste onto the target sheet.

### 2) Immediately stabilise identity
- **Tools → Reset Component Unique IDs** (at least on the pasted set / sheet)

This prevents “same GUID” collisions that cause bracketed designators and ECO weirdness later.

### 3) Fix library binding (if needed)
- **Tools → Update From Libraries**
- Resolve any `<Not Found>` / wrong library references
- Finish

Do this *before* annotation, because some library updates can alter parameters (and you want everything consistent before numbering).

### 4) Annotate designators (yes, do this now)
Pick one strategy and stick to it:

**Preferred for reuse:**  
- Annotate only the new stuff / only the sheet / only “?” designators  
(so you don’t renumber the whole project)

In the Annotate dialog, look for options like:
- “Annotate only unannotated components”
- “Selected sheets only”
- “Reset existing” **OFF** (unless you want a full renumber)

### 5) Compile
- **Project → Compile**
Check Messages panel for anything structural (duplicate IDs, missing models, etc.)

### 6) Update PCB from schematic (ECO)
- **Design → Update PCB Document**
Apply ECO so the pasted circuit generates/updates the PCB components.

### 7) Now do your PCB “block” work
Only now should you:
- copy/paste placement + routing,
- create/replicate rooms,
- or otherwise replicate layout patterns.

Because now the PCB components correspond to stable schematic designators.

---

## One nuance: if your “PCB block” is a pre-routed module you want to copy
If you already have a PCB layout for that exact circuit in another project, the safest approach is:

1) Paste circuit in schematic
2) Reset Unique IDs
3) Bind libraries
4) Annotate
5) ECO to PCB (creates the new footprints)
6) **Then** copy placement/routing from the source PCB and paste/replicate onto the new footprints (or use rooms)

---

### Quick rule of thumb
**If the designators might change → do NOT start PCB replication yet.**

If you tell me which PCB reuse method you mean (Rooms? copy/paste components? replicate layout?), I’ll give you the exact “click path” and the gotchas for that method.

[M24] ME (2026-02-26 18:16):
[image]
Partially worked 
[attached file: IMG_D48F14CF-2E54-454F-A064-A1EAB0252771.jpeg]

[M25] AI (2026-02-26 18:16):
Yep — that screenshot is classic **“partially applied ECO / partially linked component set”**.

What I can see:

- You’ve got a green **room / component class region** (so *some* of the circuitry made it into PCB as a coherent group).
- But the placement looks like a mash-up: some parts are sitting in the right cluster, others look like they’ve come in separately / not matched to an existing layout, and the ratsnest suggests nets are not matching the intended “block” mapping.

That happens when **some components matched existing PCB components by designator/unique ID**, but others were treated as **new components** (or got re-linked to different library parts).

Here’s how to get it from “partial” to “clean” reliably.

---

## 1) Don’t try to fix this on the PCB first
PCB “block reuse” only works if the schematic side is stable:

- **Designators stable**
- **Unique IDs stable**
- **Library links stable**
- **No `<Not Found>` in Update From Libraries**
- **Compile clean**

If any of those are shaky, you’ll always get “partial”.

---

## 2) The usual root cause: mixed identity (some old, some new)
After paste, you likely did one (or more) of these in a different order:

- annotated *after* ECO (so designators changed after components were created on PCB)
- reset unique IDs on only some components (or not at all)
- some components were still “Not Found” / mis-linked so footprints didn’t match
- existing PCB had components with same designators, so Altium tried to match them

Result: half the set maps, half doesn’t.

---

## 3) The clean recovery sequence (do this now)

### Step A — In PCB: delete the broken room instance (clean slate)
In PCB:
1) Click the **room outline** (green rectangle)
2) Right-click → **Rooms → Delete Room** (or similar)
3) Then delete the components that belong to that failed import **if they’re not used elsewhere**

If you’re unsure which are “new”, use:
- PCB panel → **Components** sort by designator range / recently added
- Or temporarily filter by room membership

Goal: remove the half-created footprint set so the next ECO can be clean.

### Step B — In schematic: stabilise the pasted circuit
On the sheet containing the pasted block:

1) **Reset Component Unique IDs**  
   Do it for the whole sheet if you can’t isolate the selection.

2) **Update From Libraries**  
   Ensure **zero `<Not Found>`** and that footprints/models are correct.

3) **Annotate schematics** (only new parts)  
   Configure annotation so it **doesn’t renumber the whole project**.
   - annotate only “?” or only selected sheet
   - keep “reset existing designators” OFF

4) **Compile**  
   Check Messages for duplicates/missing models.

### Step C — ECO again
Now:
- **Design → Update PCB Document**
- Apply ECO

This time you should get a consistent “all-or-nothing” component creation for that block.

---

## 4) If you are trying to *reuse an existing PCB layout block*
There are two different intents:

### Intent 1: “Create new footprints then copy placement/routing”
Do the ECO first (as above), then:
- copy/paste the placement/routing pattern from the source PCB
- or use Rooms/Replicate

### Intent 2: “I already have the layout for this block and want it to map”
Then **designators must match** between the source PCB block and the new schematic instance *before* the ECO.

If you annotate after ECO, Altium can’t match footprints to the layout you’re trying to reuse.

---

## 5) One quick diagnostic from your screenshot
If you click one of the “wrong” components in PCB and check its properties:
- Does it show a **Room** membership for that block?
- Does its **designator** match what you expected from the schematic?
- Does it have the correct footprint?

If one is off, that’s why it’s only partial.

---

## What I need from you to pinpoint it in one pass
Tell me which “partial” you mean:

1) **Some components didn’t come across at all**, or  
2) **They all came across but aren’t matching the layout block**, or  
3) **Designators changed and now the PCB has duplicates**, or  
4) **Footprints are wrong/mixed**

If you can, send a screenshot of the **ECO changes list** (the Update PCB dialog showing what it plans to Add/Update/Remove). That list will immediately reveal whether Altium is:
- adding “new” components instead of matching,
- failing to find footprints,
- or refusing updates due to conflicts.

[M26] ME (2026-02-26 18:42):
[image]
When I component link from schematic to PCB what happens to all
Of the extra gates. It’s caused this problem with extra components ch
[attached file: IMG_9E210757-6611-4D7E-987E-88BF9C8BBFB2.jpeg]

[M27] AI (2026-02-26 18:42):
Yep — that picture is the smoking gun: you’ve got **duplicate PCB footprints created for “extra gates / parts” that the schematic thinks exist**, but which your intended block/layout doesn’t account for. It’s not “extra gates” being ignored — it’s **Altium instantiating additional component parts** because of multi-part components / repeated channels / annotation/linkage drift.

Let me break down what’s happening and how to stop it.

---

## What happens to “extra gates” when you link schematic → PCB?
### Key rule
**Only the schematic parts that have a PCB footprint model get a footprint on the PCB.**

So:
- If you have a multi-part component (e.g., U1A/U1B/U1C/U1D), **each part shares the same Designator** (U1) but each *part* is a separate schematic “slot”.
- In PCB there is still **one footprint** for U1 (because physically it’s one package).

### So why are you getting “extra components” on PCB?
Because Altium has decided those schematic parts are **not parts of the same physical package anymore**, or it can’t reconcile them during ECO, so it creates **additional physical components** (extra footprints) with **IC?** etc.

This typically happens due to one of these:

1) **Multi-part packaging info is missing / inconsistent**
   - The symbol in one library has “Parts = 1”
   - Another version (or pasted copy) has “Parts = N”
   - Or the pasted instance lost the “part” metadata

2) **You pasted a circuit containing multi-part components, then relinked to a *different library component* with a different part count**
   - Schematic still has U? parts floating around
   - ECO interprets them as new devices

3) **Annotation / Unique IDs changed after PCB already had a footprint**
   - Some parts match the existing footprint, others appear as “new” and get spawned as extra footprints

4) **You have “gates” that are meant to be invisible / schematic-only, but they still have a footprint model assigned**
   - So Altium rightfully generates PCB components for them.

---

## How to diagnose which it is (fast)
Click one of the **extra IC? footprints** on the right.

In PCB **Properties** check:
- **Designator** (is it `IC?` or something unexpected?)
- **Source / SCH link** (does it link to a schematic component? which designator/part?)
- **Footprint name** (is it the same as the real one?)

Then go to the schematic and click the corresponding component:
- Does it show **Part = 1** or **Part = A/B/C**?
- Does it show **Number of parts**?

If the extras link to schematic components that *should* be gates of an existing IC, your packaging metadata is wrong.

---

## The fix (do this in the right order)

### Step 1 — Stabilise the multi-part components in the schematic
For any IC that has multiple schematic parts (A/B/C…):
1) On schematic: right-click the component → **Part Actions** (or similar)
2) Confirm:
   - correct **part count**
   - correct **current part** (A, B, etc.)
   - all parts share the same **designator** (e.g., U7A/U7B but designator base U7)

If your library symbol is wrong (parts=1 when it should be parts=4), fix it in the library first, then **Update From Libraries**.

### Step 2 — Remove the extra PCB footprints (they’re ghosts)
In PCB:
- delete the extra `IC?` footprints that shouldn’t exist  
(Do this only once you’ve fixed the schematic packaging, otherwise they’ll come back.)

### Step 3 — Reset IDs (only if you’ve been copy/pasting)
In schematic:
- **Reset Component Unique IDs**
- Re-compile

### Step 4 — ECO again
- **Design → Update PCB Document**
Now Altium should map multi-part components to **one physical footprint**.

---

## Prevent it happening again when you “reuse” a circuit
When copying/pasting a reusable circuit that contains multi-part ICs:

1) Paste schematic
2) **Update From Libraries** immediately  
   (this ensures the pasted parts pick up correct “parts per component” metadata)
3) Annotate
4) Compile
5) ECO

If you annotate/ECO before library rebinding, the multi-part part IDs get out of sync and you get the ghost footprints.

---

## One important question (no fluff)
Are those “extra gates” things like:
- multi-channel buffers/receivers (e.g., DS90LV032 style quads)
- logic gate packs (74HCxx)
- op-amps (dual/quad)
- resistor networks / arrays

If you tell me which component(s) are producing the duplicates (design item ID / comment from schematic), I’ll tell you exactly which property to check (part count, packaging, footprint model assignment) and the quickest correction route.

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] AI (2026-02-26 15:59):
Got it. In Altium there are *two fundamentally different “block” concepts* people mix up:

1) **Schematic blocks** (logic/connectivity)  
2) **Layout/PCB blocks** (physical placement/routing)

They behave differently, have different identity rules, and they break in different ways. Here’s the clean differentiation, then a **sequence (step order) that works reliably**.

---

## 1) Schematic blocks (logical)
**What they are:** A reusable chunk of circuitry that defines **nets, ports, components, parameters, design intent**.

**Common forms in Altium:**
- **Reuse Block** (official feature)
- **Snippet / Managed Schematic Sheet / Template-based reuse**
- Or your current approach: **copy/paste from another project** (works, but carries baggage)

**What matters in schematic blocks:**
- **Connectivity**: net labels, ports, harnesses, sheet entries
- **Identity**: component Unique IDs (GUIDs), designators, multi-part gate mapping
- **Library linkage**: symbol ↔ footprint ↔ parameters ↔ models
- **Compilation rules**: duplicate IDs, net name resolution, parameter propagation

**Failure modes you see:**
- Designators go **bracketed** or turn into “?” after compile
- ECO tries to delete/re-add parts, or pushes wrong footprint
- Nets don’t connect through ports/harnesses
- Parameters “don’t pull through”

---

## 2) Layout blocks (physical)
**What they are:** A reusable chunk of **placement + routing geometry** on the PCB.

**Common forms in Altium:**
- **Rooms** (generated from schematics, used to group components)
- **PCB Snippets** (copy/paste geometry)
- **Copy/paste groups** of components/tracks between PCB documents
- **Replicated layout by Room / Copy Room formats** (varies by version/workflow)

**What matters in layout blocks:**
- **Physical geometry**: footprints, placement, routing, vias, keepouts, rules
- **PCB constraints**: clearance rules, diff-pair rules, net classes
- **Component matching**: the PCB objects must correspond to the *right* schematic components (designators/unique IDs drive this)

**Failure modes you see:**
- Routes detach or end up on “No Net”
- Differential pairs lose rules
- Copied geometry doesn’t match the target nets/components
- Rooms don’t populate or get “wrong parts” if IDs/designators aren’t stable

---

## The key principle
**Schematic blocks define *what* the circuit is.**  
**Layout blocks define *how* it’s physically realized.**

If the schematic identity is unstable (GUIDs/designators/library links), the PCB side becomes unpredictable.

---

# Sequence instruction (the order that prevents pain)

## A) If your “block” starts life in schematics (most common)
### Step 0 — Standardise the *source* project
In the source project (the one you copy from):
1. Compile it cleanly.
2. Ensure libraries resolve (symbols + footprints + parameters).
3. Finalise port/net naming at the block boundary.

### Step 1 — Bring schematic into target
In the target (main) project:
1. Paste the schematic circuitry onto the correct sheet.
2. **Immediately reset Unique IDs** (this is non-negotiable for copy/paste workflows).
3. Decide designator strategy:
   - Either keep source designators (careful, requires discipline),
   - or re-annotate in the target (usually safer).

### Step 2 — Normalise component linkage
In the target:
1. Run **Update From Libraries** (or your equivalent) so every pasted component is linked *the same way as the rest of the project*.
2. Confirm footprints exist and are the correct variants.

### Step 3 — Compile and fix only schematic issues
1. Compile.
2. Resolve warnings about:
   - duplicate IDs
   - missing models
   - port/harness mismatches
   - net naming collisions

### Step 4 — Only now go to PCB (ECO)
1. Run the ECO to update PCB.
2. Confirm rooms (if used) are created correctly.
3. Place/arrange by room/module.

### Step 5 — Layout reuse (optional, only after Step 4)
If you want to replicate placement/routing:
1. Use Rooms / PCB snippet / copy-paste layout **after** the components exist on PCB and match correctly.
2. Then re-run DRC and verify diff-pair rules, impedance rules, etc.

---

## B) If your “block” starts life on PCB (less common)
This is only safe if the schematic identity already exists.

1. Create/confirm the schematic for
