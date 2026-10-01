# Altium comment mismatch
Date (UTC): 2026-04-24 00:23
Conversation ID: 69eab7d8-d498-83eb-ab5b-8e13889156a9
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-24 00:23):
[image]
[image]
[image]
Why are these comments coming though slightly misshaped to myreuse block?
[attached file: IMG_E3889A62-F648-46E3-9C6D-0915FE4D708D.jpeg]
[attached file: IMG_DD3C1434-9A1F-4A5F-A85D-9D98142F5B34.jpeg]
[attached file: IMG_9DA27ED5-B742-4BE8-9BD0-2F0BD640E258.jpeg]

[M2] AI (2026-04-24 00:23):
This looks like an **Altium unique-ID / channel-index mismatch**, not just a graphical comment/display problem.

In your screenshots, the giveaway is this:

- Schematic unmatched: **IC6**
- PCB unmatched: **IC10**
- Details differ: schematic says something like **SOIC-9 / ADA4817…**, PCB says **SOIC-8 / 5AD…**
- PCB designators and comments are coming through with suffixes like **`_6_OSO`**, e.g. `IC1_6_OSO`, `R28_6_OSO`, etc.

That means Altium thinks some PCB components belong to a different logical/component instance than the schematic thinks. In a reuse block or repeated channel, the **visible designator/comment may look right-ish**, but the underlying **component Unique IDs** are not aligned.

## What is probably happening

Your reuse block has been copied/imported/updated in a way that preserved or partly preserved old PCB component identity. So Altium is trying to reconcile:

**Schematic component identity**
→ “This is IC6 from this schematic/channel”

against

**PCB component identity**
→ “This physical footprint is IC10 / from another copied block / old channel instance”

The comment strings then appear “misshaped” or slightly wrong because they are not simply free text. They are tied to the schematic component parameters and channel naming system. If the matched pair is wrong, the comment that gets pushed to the PCB can be from the wrong logical instance.

## Do not just press Perform Update yet

In the first image, Altium is offering to match unmatched schematic and PCB components. If you blindly pair **IC6** to **IC10**, you may force a bad match. That can scramble the reuse block further.

Before updating, check whether IC6 in the schematic is genuinely meant to correspond to IC10 on the PCB. From the details shown, it does **not** look like a clean match.

## Immediate fix route

In the matching dialog:

1. **Untick Footprint** temporarily if it is blocking sensible matches.
2. Keep **Designator** ticked only if your designators are truly meant to match.
3. Use the mask boxes to isolate one component at a time, e.g. `IC6`, `IC10`, `R28`.
4. Only manually match parts where:
   - the schematic designator is correct,
   - the PCB designator is correct,
   - the comment/value matches,
   - the footprint matches,
   - and it belongs to the same channel/reuse block.

If the PCB component is genuinely wrong, do **not** match it. Let Altium remove/re-add or update it properly through ECO.

## The likely proper repair

For a copied reuse block, I’d usually do this:

### 1. Save a backup first

Seriously. Before touching unique IDs, save a copy of the project/PCB.

### 2. Reset component links rather than force-matching bad pairs

In PCB:

**Project > Component Links**

Then look for unmatched or wrongly matched components. You want Altium to pair each schematic component to the correct PCB footprint by **designator/comment/footprint**, then regenerate the unique IDs.

Use **Add Pairs Matched By >>** only where the pairing is genuinely correct.

### 3. Push schematic to PCB again

Then run:

**Design > Update PCB Document**

Review the ECO carefully. If it wants to remove and re-add large numbers of parts, stop and inspect. If it only wants to update component links, parameters, rooms, and nets, that is more promising.

## Why the `_6_OSO` style text appears

That looks like Altium’s repeated-channel naming coming through. Something like:

`R28_6_OSO`

means approximately:

`R28` from channel/index `6`, probably under an `OSO` channel/sheet context.

That is normal in multi-channel designs, but it becomes ugly/confusing if the channel mapping or reuse block identity is not clean.

If this is meant to be a reusable block, check:

- the child sheet instance name,
- the room name,
- the channel designator format,
- whether the schematic sheets were copied with old unique IDs,
- whether the PCB room was copied from an old instance.

## Also check parameter visibility

If by “comments” you literally mean the visible text on the PCB looking malformed, check the component overlay strings too:

Right-click component → **Properties** → check visible strings for:

- Designator
- Comment
- any custom parameter strings

Sometimes copied reuse blocks end up showing a parameter string like `.Comment` or a channelised full designator instead of the intended local comment/value.

But from your screenshots, I’d treat this primarily as a **component matching / unique-ID problem** first.

## Best practical approach from where you are

I would do this:

1. Cancel the current update.
2. Open **Project > Component Links**.
3. Clear obvious bad matches if needed.
4. Match only correct schematic ↔ PCB pairs.
5. Use designator/comment/footprint matching cautiously.
6. Run **Update PCB** again.
7. When ECO appears, reject anything that wants to unexpectedly delete/recreate your placed reuse block.

The key point: **the reuse block geometry may be okay, but Altium has lost confidence that the schematic components and PCB components are the same objects.** That is why the comments/designators are coming through oddly.

[M3] ME (2026-04-24 00:36):
[image]
Learn delete the components the tracks are left 
[attached file: IMG_7A38259A-639A-406D-B561-EF8823F6B289.jpeg]

[M4] AI (2026-04-24 00:36):
Yes — that is expected behaviour in Altium if you delete components from the PCB manually. **Deleting a component does not automatically delete its connected tracks/vias/polygons/text.** The copper becomes orphaned/free primitives.

You now have basically got **loose routing left behind from the removed reuse block**.

### Fast cleanup

Select the area containing the leftover block, then use:

**Edit → Select → Connected Copper**

or right-click one of the leftover tracks and look for selection options such as **Select Connected Copper** / **Select Connected Objects** depending on your Altium version.

Then press **Delete**.

### Safer cleanup method

If you only want to remove the old abandoned routing:

1. Turn on only relevant layers: **Top Layer**, **Bottom Layer**, vias, maybe overlay.
2. Box-select the leftover area.
3. Use the PCB Filter panel if needed:
   ```text
   IsTrack Or IsVia Or IsArc Or IsText
   ```
4. Delete selected objects.

Be careful not to include board outline, mechanical layers, rooms, or any genuine reused placement you still want.

### Better way when replacing a reuse block

Rather than deleting only components, use the ECO/update flow to remove the old components **and then manually clear the abandoned copper**, or select the whole old placement/routing block as a physical region before deleting.

For reuse blocks, I’d do this:

1. Save a backup.
2. Delete the bad copied block area: components **plus** tracks/vias/text.
3. Re-run **Design → Update PCB Document** from schematic.
4. Let Altium bring the components back cleanly.
5. Reapply/replicate the placement/routing from the known-good block.

### Why it has happened

The tracks are not “owned” by the component in the same way pads are. Pads disappear with the component footprint, but tracks are independent PCB primitives. So when the component vanishes, Altium leaves copper segments sitting there, often still on the original net names, or sometimes as no-net / broken-net fragments.

This is annoying, but it is normal.

[M5] ME (2026-04-24 00:40):
[image]
These 4 are jumbled so I’ll take them back out and read?
[attached file: IMG_2F6EDDDA-706E-4F05-A4FA-658B40782147.jpeg]

[M6] AI (2026-04-24 00:40):
Yes — **take those four back out before you perform the update**.

Those are not safely matched. In the screenshot Altium has paired them like this:

- Sch **IC7** → PCB **IC6**
- Sch **IC8** → PCB **IC7**
- Sch **IC9** → PCB **IC8**
- Sch **IC10** → PCB **IC9**

That is a classic off-by-one/jumbled unique-ID match. If you hit **Perform Update** with those accepted, Altium will write those bad pairings into the PCB and the reuse block will stay confused.

Select those four rows and press **`<`** to move them back out of **Matched Components**.

Then re-add them manually one-by-one so the designators line up:

- **IC7 → IC7**
- **IC8 → IC8**
- **IC9 → IC9**
- **IC10 → IC10**

Before moving them right, temporarily tick more match criteria at the bottom:

- **Designator**
- **Comment**
- **Footprint**

That should stop Altium doing a lazy “near enough” match by sequence.

After they are correctly paired, then press **Perform Update**.

Also note: **IC8 showing “Comment”** is a red flag. That component may have a blank/default comment on one side or a missing parameter. After matching, check IC8 properties in the schematic and PCB to confirm the real component comment/value is present.

[M7] ME (2026-04-24 00:41):
What if the ic numbers do t match but the part numbers do?

[M8] AI (2026-04-24 00:41):
Then **match by the actual circuit function / part identity, not blindly by IC number**.

In Altium, the designator is only a label. If the schematic was reannotated, copied, or reused, it is possible that:

- schematic **IC7** is genuinely the same physical part as PCB **IC6**
- schematic **IC8** is genuinely the same physical part as PCB **IC7**
- etc.

So the question is not “do the numbers match?” — it is:

**Does this schematic component correspond to that exact PCB footprint in the circuit?**

For each suspect IC, check these four things:

1. **Same part/comment**  
   Example: ADA4817, ADG704, comparator, logic gate, etc.

2. **Same footprint**  
   SOIC-8, SOIC-9, SOT23-5, SOD-523, etc.

3. **Same nets on the pins**  
   This is the big one. The connected nets should make sense: input, output, supply rails, clamp node, OSO node, etc.

4. **Same physical role in the block**  
   For example, “this is the left-hand OSO buffer amp”, not just “some SOIC-9 part”.

If the **part numbers match but the designators do not**, that can be okay, but only if the net/function match is also correct.

### In your case

Because the list looked offset:

- IC7 → IC6  
- IC8 → IC7  
- IC9 → IC8  
- IC10 → IC9  

that might actually mean the **PCB was annotated differently from the schematic**, rather than being wrong. But I would not trust it from the list alone.

### Best way to verify

Click one suspect matched row, then use cross-probe / zoom to locate both sides:

- schematic IC7: what is it doing?
- PCB IC6: where is it physically and what nets go to it?

If they are the same circuit block position, leave the match.

If they are only the same package or same generic “SOIC-9 op-amp”, but not the same role, take it back out.

### Practical rule

For reused analogue blocks, I’d rank matching confidence like this:

**Unique ID > exact circuit function/nets > part number/comment > footprint > designator**

So yes, **part number can override designator**, but **nets/function must confirm it**.

[M9] ME (2026-04-24 00:43):
I’ve I perform that update do I eco?

[M10] AI (2026-04-24 00:43):
Yes — **Perform Update is effectively committing the component-link update**, but it is **not the same as doing a normal schematic-to-PCB ECO**.

Think of it as two stages:

### 1. Component Links dialog — fixes identity

When you press **Perform Update** in that dialog, Altium writes the schematic ↔ PCB component pairings / unique IDs.

That tells Altium:

> “This schematic IC7 is this PCB IC6,”  
> or  
> “This schematic IC7 is this PCB IC7.”

So only press it once you are happy the matches are correct.

### 2. Then run normal ECO

After that, run:

**Design → Update PCB Document**

That creates the normal ECO to update:

- comments/parameters
- footprints if different
- nets
- rooms/classes
- component removals/additions
- designator changes

Then inspect the ECO before executing.

### What I’d do in your situation

Because you are in a reuse/multi-channel mess, do it carefully:

1. **Save a backup copy first.**
2. In **Component Links**, only keep matches you are confident are correct.
3. Press **Perform Update**.
4. Then run **Design → Update PCB Document**.
5. In the ECO dialog, check carefully for anything scary like:
   - removing lots of components
   - re-adding components you already placed
   - changing many designators unexpectedly
   - changing footprints unexpectedly
   - ripping up nets/rooms

If the ECO mostly says **Update Component Links / Update Parameters / Update Nets**, that is normal.

If it wants to delete/recreate the whole reuse block, cancel and reassess.

So yes: **Perform Update first, then ECO via Update PCB.**

[M11] ME (2026-04-24 00:44):
[image]
I didn’t, then ran it again and got that 
[attached file: IMG_512AF800-9AFB-4A6E-A89F-DA1FA97EC851.jpeg]

[M12] AI (2026-04-24 00:44):
That’s actually a **good sign**.

The ECO is only saying:

**Add Component Class Member: IC9 to OS_Re-Use**

That means the schematic/PCB component links are now mostly accepted, and Altium is only trying to tidy up the **component class membership** for the reuse block/project class.

It is **not** trying to delete parts, re-add footprints, change nets, or reassign loads of designators. So this ECO looks safe.

I’d do this:

1. Leave it ticked.
2. Press **Execute Changes**.
3. Save the PCB.
4. Recompile / validate again.
5. Run **Design → Update PCB Document** once more.

After that, ideally you want either:

- no ECO changes, or
- only harmless class/room/parameter updates.

The thing to check next is whether the four ICs still have sensible links. Open **Project → Component Links** again and confirm there are no unmatched ICs and no obvious offset/jumbled matches.

This one-line ECO is not the scary one — this is just Altium saying, “IC9 belongs in the OS_Re-Use component class.”

[M13] ME (2026-04-24 00:46):
When copying from an existing design into a reuse block do I need to reset the detonators or keep them tied 

[M14] AI (2026-04-24 00:46):
For a **clean Altium reuse block**, you generally want to **keep the internal/local designators consistent with the source block**, not randomly reset them.

So if the original proven block used:

- IC1, IC2, IC3…
- R1, R2, R3…
- C1, C2, C3…

then the reuse block schematic and reuse block PCB should also use the same local designators.

The important distinction is:

**Keep the designator text. Reset/regenerate the Unique IDs if the block was copied badly.**

### Best practice

When copying an existing design into a reuse block:

1. **Keep the local designators the same**
   - `IC1` in the schematic should correspond to `IC1` in the reuse PCB.
   - `R28` should correspond to `R28`.
   - This makes component linking sane.

2. **Do not keep stale component links/Unique IDs from the old parent PCB**
   - That is what causes Altium to think schematic `IC7` is PCB `IC6`, etc.
   - The designators can stay; the identity links need to be remade cleanly.

3. **Use Component Links to establish the relationship**
   - Match by **Designator + Comment + Footprint** where possible.
   - Then press **Perform Update**.
   - Then run the normal ECO.

### In your situation

Because this is a reuse block, I would **not reset the designators to new random numbers** unless you have a specific reason. I would aim for:

```text
OS_Re-Use.SchDoc IC1  -> OS_Re-Use.PcbDoc IC1
OS_Re-Use.SchDoc IC2  -> OS_Re-Use.PcbDoc IC2
OS_Re-Use.SchDoc R1   -> OS_Re-Use.PcbDoc R1
OS_Re-Use.SchDoc C1   -> OS_Re-Use.PcbDoc C1
```

Then when that block is instantiated in the top-level multi-channel design, Altium can generate the expanded/channelised designators separately, like:

```text
IC1_1
IC1_2
IC1_3
```

or whatever your project naming scheme uses.

### When would you reset designators?

Only reset them if:

- you are deliberately renumbering the reuse block from scratch,
- the schematic and PCB were copied from different versions,
- the old designators are duplicated/conflicting inside the same flat document,
- or the copied block has inherited nonsensical annotation.

But if the PCB placement/routing came from the same schematic block, **keep the designators aligned**.

### Practical rule

For reuse blocks:

**Local designators should match between the reuse schematic and reuse PCB.  
Unique IDs should be regenerated/relinked cleanly.  
Top-level channel names should be allowed to expand later.**

So: **keep the designators tied/aligned, but do not trust old copied unique-ID links.**

[M15] ME (2026-04-24 00:49):
And then when I place the block? Do I need designators to reset then ?

[M16] AI (2026-04-24 00:49):
No — **do not manually reset the designators when you place the reuse block into the real design**.

Keep it like this:

```text
Inside OS_Re-Use.SchDoc / OS_Re-Use.PcbDoc:
IC1, IC2, IC3...
R1, R2, R3...
C1, C2, C3...
```

Then when you place/instantiate that block in the parent design, let Altium handle the **expanded/channel designators**.

So the reuse block stays locally clean:

```text
IC1
IC2
IC3
```

The parent/multi-channel design then resolves them as something like:

```text
IC1_1
IC1_2
IC1_3
```

or:

```text
IC1A
IC1B
IC1C
```

depending on your annotation/channel naming settings.

### What not to do

Do **not** go into the reuse block and rename everything before placing it, e.g.:

```text
IC101, IC102, IC103...
```

unless you are deliberately making it a one-off flat block. That defeats some of the usefulness of reuse/multi-channel structure and can make Component Links/rooms more painful.

### When you place the block into the final PCB

The safe order is:

1. Keep reuse schematic and reuse PCB internally matched.
2. Place/instantiate the sheet/reuse block in the parent project.
3. Compile the project.
4. Run annotation/update from the parent.
5. Let Altium create the channelised designators.
6. Generate rooms / update PCB.
7. Replicate or import the PCB placement/routing for that channel.

### Key rule

**The reuse block should keep stable local designators.  
The parent design decides the final expanded designators.**

So yes: keep them tied inside the reuse block. When placing the block, let Altium do the reset/expansion — don’t manually reset them yourself.

[M17] ME (2026-04-24 00:50):
I mean do I set it to reset desk gators in place 

[M18] AI (2026-04-24 00:50):
No — **don’t use “Reset Designators” when placing the reuse block**, unless you are intentionally making it a completely new unrelated copy.

For your case, choose the option that **preserves/keeps existing designators**.

You want:

```text
Reuse source:
IC1, IC2, R1, R2, C1, C2...

Placed block:
IC1, IC2, R1, R2, C1, C2...
```

Then let the **parent project annotation / multi-channel naming** sort out the final expanded names later.

### Why

If you tick **Reset Designators on place**, Altium may turn things into:

```text
IC?, R?, C?
```

or allocate new free numbers. That breaks the easy one-to-one relationship between:

```text
OS_Re-Use.SchDoc IC7
OS_Re-Use.PcbDoc IC7
```

and makes component linking much more likely to go sideways.

For a reuse block, stable internal designators are your anchor. The unique IDs/component links can be repaired, but if the designators also get reset, you lose the simple reference map.

### Use this rule

For placing your reuse block:

- **Reset Designators:** **No / unticked**
- **Keep/Preserve Designators:** **Yes**
- **Reset Unique IDs:** generally **Yes**, or repair them afterwards through **Project → Component Links**
- **Then run annotation/update from the parent design**

So for your current workflow: **keep the designators, don’t reset them on place.**

[M19] ME (2026-04-24 00:51):
But what if thee is if 1 already in the design elsewhere 

[M20] AI (2026-04-24 00:51):
That’s exactly where **multi-channel annotation** is supposed to help.

You can have **IC1 inside the reuse sheet** even if there is already an **IC1 elsewhere**, provided the design is hierarchical/repeated correctly. Altium treats the local sheet component as a source instance, then generates the final physical designators during annotation.

So conceptually:

```text
Reuse sheet local designator:     IC1
Top-level final designator:       IC101 or IC1_2 or U_OSO1_IC1
Existing design IC1 elsewhere:    IC1
```

The important bit is that the **local reuse-block designator** and the **final compiled/physical designator** are not always the same thing.

## What I would do

When placing the reuse block:

- **Do not reset designators on place**
- Keep the reuse block internally as `IC1`, `IC2`, `R1`, etc.
- Then run the parent project annotation after placement.

In Altium, use something like:

**Tools → Annotation → Annotate Schematics**

or for multi-channel:

**Tools → Annotation → Board Level Annotate**

depending on your setup/version.

That is where you resolve duplicates into final board-level designators.

## The rule

Inside the block:

```text
IC1, IC2, R1, R2, C1...
```

Across the whole board after annotation:

```text
IC101, IC102, R101...
```

or:

```text
IC1_1, IC1_2, R1_1, R1_2...
```

depending on your project annotation format.

## Where people get burned

If you reset designators while placing the block, Altium may give you `IC?`, `R?`, `C?`, or arbitrary new numbers before the block is properly linked. Then the PCB reuse placement has nothing stable to match against.

So even if there is already an IC1 elsewhere, **do not panic-reset the block designators at placement**. Keep the block stable, then let **project/board-level annotation** resolve the real final names.

For your reuse workflow, the clean aim is:

```text
OS_Re-Use.SchDoc IC1  ↔  OS_Re-Use.PcbDoc IC1
Parent design instance later becomes ICxxx / IC1_6 / whatever
```

That gives Altium a stable internal map and still avoids duplicate final designators on the real board.

[M21] ME (2026-04-24 01:05):
[image]
Right, it’s coped the block over but there are meant to be two channels. And it has dropped components for two channels below it so there are effectively 3 channels worth of
[attached file: IMG_563F1429-81D8-4173-929C-84EC77635473.jpeg]

[M22] AI (2026-04-24 01:05):
Yes — that means Altium has done **two separate things at once**:

1. It copied/placed your **PCB reuse block** as a routed physical block.
2. It also generated the **compiled channel components** from the schematic update/ECO.

So now you have:

- the copied routed reuse block at the top,
- plus channel 1 generated components below,
- plus channel 2 generated components below.

That is why it looks like **three channels’ worth**.

## What has gone wrong

Your copied PCB block is probably **not linked to the actual compiled channel components**. Altium sees it as extra physical PCB objects, then says:

> “The schematic has two channel instances, so I need to add two sets of components.”

So it adds the two proper channel sets separately.

## Do not route/clean this manually yet

Do **not** just delete random components yet. First identify which items are the real schematic-linked channel components.

The “dropped below” parts are probably the valid components created by the ECO. The copied routed block is probably the orphan/unlinked physical reuse placement.

## What to do now

### Option A — preferred if you want to use PCB reuse placement

Use the copied routed block as the placement/routing for one real channel, but you must **link it** to one compiled channel.

Process:

1. Save a backup.
2. Open **Project → Component Links**.
3. Check whether the routed copied block components are unmatched.
4. Match the routed copied block components to **one channel’s schematic components**.
5. Press **Perform Update**.
6. Run **Design → Update PCB Document** again.
7. The ECO should stop trying to add that first channel as loose components.
8. Then use placement/room replication for the second channel.

### Option B — easier if it is already messy

Delete the copied routed block and let Altium generate the two channel component sets cleanly.

Then:

1. Keep the two generated channel component sets.
2. Place one channel nicely.
3. Route it or import/replicate from your known-good block.
4. Use **Rooms / Copy Room Formats** or reuse-block tools to replicate placement/routing to the second channel.

Given your screenshot, this may be the cleaner route.

## The key decision

You need to decide which of these should survive:

```text
A) The copied routed block
B) The two dropped schematic-generated channels
```

You do **not** want all three.

For a proper two-channel design, you want exactly:

```text
Channel 1 physical components + routing
Channel 2 physical components + routing
```

not:

```text
Copied source block + Channel 1 + Channel 2
```

## My recommendation

At this stage I’d treat the copied routed block as the **placement/routing donor**, not as a final part of the board.

So:

1. Keep it temporarily as a reference.
2. Use the two generated channel component sets as the real schematic-linked parts.
3. Apply/replicate placement and routing from the donor block onto the real channel rooms.
4. Once the real channels are placed/routed, delete the donor block.

That avoids fighting Altium’s Unique ID logic.

The bottom components are probably the real ones. The top copied block is probably just geometry with stale identity.
