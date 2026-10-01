# Clock Net Naming Fix
Date (UTC): 2026-03-09 03:54
Conversation ID: 69ae4482-7738-8390-92ae-72b820ffb379
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-09 03:54):
[image]
Like that?
[attached file: IMG_F82F411F-E493-4E58-BF1B-DE3B94BA88BA.jpeg]

[M2] AI (2026-03-09 03:54):
Almost — but I can see one problem straight away:

You’ve got:

- `CLK1`
- `CLK2`
- `CLK2`
- `CLK4`

So one of those should presumably be `CLK3`.

And more importantly, if these are meant to be **per-channel unique nets**, they still look too generic. `CLK1`, `CLK2` etc will collide unless the multichannel naming is being applied above them.

What you want is:

- either the **local child-sheet ports** named simply `CLK1`, `CLK2`, `CLK3`, `CLK4`
- and then the **compiled/resulting nets** become channelised automatically by the harness/sheet entries

or, if you are forcing unique names manually:

- `CLK1_CH_1`
- `CLK2_CH_1`
- `CLK3_CH_1`
- `CLK4_CH_1`

Right now the top one is channelised as `SR_DATA-OUT_CH_1`, but the clock ones are not matching that pattern.

So: **not quite yet**. First fix the duplicate `CLK2`, then make sure the clock nets follow the same per-channel naming method as `SR_DATA-OUT_CH_1`.

Send the child-sheet schematic view with the ports visible and I’ll tell you exactly what each port should be named.

[M3] ME (2026-03-09 03:56):
[image]
[attached file: IMG_E07A046D-5987-452E-9CB6-AD83E9DC7568.jpeg]

[M4] AI (2026-03-09 03:56):
That’s the issue.

`REPEAT(CLK1,1,7)` should **not** be written as the port name like that.

For a normal multichannel design, the **port itself** on the child sheet should usually just be named:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

And then the **sheet symbol / channel repeat** mechanism above it generates the per-channel expansion.

So here, change those ports from:

- `REPEAT(CLK1,1,7)`
- `REPEAT(CLK2,1,7)`

to simply:

- `CLK1`
- `CLK2`

and same for the others.

## What `REPEAT(...)` is for
`REPEAT(...)` is used where Altium expects a repeated naming pattern, typically on the **parent sheet / sheet entries / harness context**, not as a literal child-sheet port name in the way you’ve got it there.

At the moment Altium is likely treating that whole text string as the actual net/port name, which is why things are going odd.

## What I’d do next
On the child sheet:

1. Rename all those ports to plain names only:
   - `CLK1`
   - `CLK2`
   - `CLK3`
   - `CLK4`
   - `SR_DATA_OUT` or whatever your base name is

2. Make sure the **parent sheet symbol entries** match those same base names exactly.

3. Let the **sheet repeat / channel indexing** generate the channelised versions.

## One important detail
Also avoid mixing separators/styles unless deliberate. In your screenshots you have things like:

- `SR_DATA-OUT_CH_1`
- `CLK1`

I’d strongly recommend consistent naming, for example:

- `SR_DATA_OUT`
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Then let Altium compile them into channelised nets.

## Sanity check
If your intention is:

- 7 repeated sheets
- each sheet has 4 clocks
- each repeated instance should stay isolated

then the child sheet ports should be **base names only**, not manually channel-suffixed and not wrapped in `REPEAT(...)`.

Send the **parent sheet symbol** next — the block that calls this child sheet — and I’ll tell you exactly what to type into the sheet entries and repeat definition.

[M5] ME (2026-03-09 04:04):
[image]
[attached file: IMG_C5449036-5A23-464B-9362-5D6D3CAE393C.jpeg]

[M6] AI (2026-03-09 04:04):
Closer, but still not right.

The **sheet symbol itself** should be repeated:

- `REPEAT(CH,1,7)`

But the **sheet entries on that symbol** should normally be just the base signal names:

- `SR_D_IN`
- `SR_D_OUT`
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Not:

- `Repeat(CLK1,1,7)`
- `Repeat(SR_D-OUT,1,7)`

## So change this exact screen to:
Top text on the sheet symbol:
- `REPEAT(CH,1,7)`

Sheet entries:
- `SR_D_IN`
- `SR_D_OUT`
- `SR_CLOCK`
- `SR_LATCH`
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

And on the **child sheet ports**, use those same plain names exactly.

## Why
You already told Altium to instantiate this sheet 7 times with:

`REPEAT(CH,1,7)`

That is the repetition mechanism.

If you also put `Repeat(...,1,7)` on each sheet entry, you are effectively trying to repeat the entries themselves as well, which is not the normal pattern and is why the naming/connection behaviour is getting messy.

## Important clean-up points from your screenshot
1. Use underscore consistently:
   - `SR_D_IN`
   - `SR_D_OUT`
   not `SR_D-IN` / `SR_D-OUT`

2. Keep the child-sheet port names identical to the parent sheet entries.

3. Leave global non-repeated signals as plain names too, for example:
   - `SR_CLOCK`
   - `SR_LATCH`

If those are intended to be common to all 7 channels, then plain names are correct.

## Correct structure
**Parent sheet symbol**
- `REPEAT(CH,1,7)`

**Parent sheet entries**
- `SR_D_IN`
- `SR_D_OUT`
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

**Child sheet ports**
- `SR_D_IN`
- `SR_D_OUT`
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Then Altium compiles them into channelised forms internally.

## One more thing
From your earlier PCB screenshot, names like `SR_DATA-OUT_CH_1` suggest you may be partly doing this manually and partly using multichannel compile naming. Don’t mix the two. Pick one method.

For multichannel, the right approach is:
- plain names on entries/ports
- repeat only on the **sheet symbol**

Go ahead and remove all the `Repeat(...)` text from the entries first. Then compile again and show me the compiled/net result or the Messages panel if it still misbehaves.

[M7] ME (2026-03-09 04:06):
[image]
Like that
[attached file: IMG_8DCD0F58-3059-4ED3-ADB9-E5665B37FD0F.jpeg]

[M8] AI (2026-03-09 04:06):
Yes — **that structure is now right** for the sheet symbol.

You’ve now got the correct pattern:

- sheet symbol name: `REPEAT(CH,1,7)`
- sheet entries as plain base names:
  - `SR_D-IN`
  - `SR_D-OUT`
  - `SR_CLOCK`
  - `SR_LATCH`
  - `CLK1`
  - `CLK2`
  - `CLK3`
  - `CLK4`

That is the right direction.

Two tidy-ups before you go further:

1. **Use underscores, not hyphens, in net names**
   Change:
   - `SR_D-IN` → `SR_D_IN`
   - `SR_D-OUT` → `SR_D_OUT`

   Hyphens can make names harder to read and are worth avoiding.

2. **Make the child-sheet ports match exactly**
   Inside `CH.SchDoc`, the ports should be named exactly the same:
   - `SR_D_IN`
   - `SR_D_OUT`
   - `SR_CLOCK`
   - `SR_LATCH`
   - `CLK1`
   - `CLK2`
   - `CLK3`
   - `CLK4`

After that:

- compile the project
- check the Navigator / compiled nets
- then push ECO to PCB

Expected result:
- `SR_CLOCK` and `SR_LATCH` stay common if they are intended to be shared
- `CLK1..CLK4`, `SR_D_IN`, `SR_D_OUT` become properly channel-contextual through the repeated sheet

If the PCB still shows odd names after this, the next place to inspect is **Project Options → Multi-Channel** because that controls how the compiled names are presented.

[M9] ME (2026-03-09 04:09):
[image]
How do they get there independence when they are individual clocks. It’s clocks 1-28 with 4 on each sheet across 7 sheets 
[attached file: IMG_4ECD1BC2-90D5-4161-B6A6-DB991691B64D.jpeg]

[M10] AI (2026-03-09 04:09):
They get their independence from the **repeated sheet context**, not from the plain port text alone.

So although each child sheet says:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Altium internally treats them more like:

- `CH1\CLK1`
- `CH1\CLK2`
- `CH1\CLK3`
- `CH1\CLK4`

on sheet 1, then:

- `CH2\CLK1`
- `CH2\CLK2`
- `CH2\CLK3`
- `CH2\CLK4`

on sheet 2

…all the way to sheet 7.

That is how you end up with **28 distinct compiled nets**, even though the visible local names repeat.

So conceptually you do **not** have:
- one global `CLK1`

You have:
- `CLK1` **inside CH1**
- `CLK1` **inside CH2**
- `CLK1` **inside CH3**
- etc.

Those are different because the **channel index is part of the compiled path**.

## Your structure
You have 7 repeated channels, each containing 4 local clocks:

- CH1: `CLK1` `CLK2` `CLK3` `CLK4`
- CH2: `CLK1` `CLK2` `CLK3` `CLK4`
- CH3: `CLK1` `CLK2` `CLK3` `CLK4`
- …
- CH7: `CLK1` `CLK2` `CLK3` `CLK4`

So total = 28 unique signals in the compiled design.

## Why that is valid
In a repeated sheet, `CLK1` is only “local” unless you intentionally tie it to something global.

It stays independent because:
- the port name is local to that repeated instance
- the repeated sheet tag `CH1..CH7` scopes it

## When they would accidentally lose independence
They become commoned together if you use things like:

- a **net label** outside the repeated context that ties them all together
- a **port/sheet entry arrangement** that collapses them to one parent net
- a **power port / global net / harness misuse**
- explicit naming on the parent that bypasses channel context

## Important distinction in your case
You have two different categories of signals:

### 1. Shared/common across all 7 sheets
These should remain plain/common if intended:
- `SR_CLOCK`
- `SR_LATCH`

These are broadcast signals.

### 2. Unique per sheet
These are local to each repeated instance:
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`
- `SR_D_IN`
- `SR_D_OUT`

These should compile as 7 independent copies.

## If you want true numbering 1–28
Altium does not naturally rename them as:

- `CLK1` to `CLK28`

from that structure alone.

Instead it keeps the logical hierarchy, something like:
- CH1.CLK1
- CH1.CLK2
- CH1.CLK3
- CH1.CLK4
- CH2.CLK1
- CH2.CLK2
- etc.

That is actually better for multichannel design, because it preserves the sheet structure.

If you really want absolute names `CLK1`…`CLK28`, then you would have to **manually name them that way**, for example:

- sheet CH1 contains `CLK1` `CLK2` `CLK3` `CLK4`
- sheet CH2 contains `CLK5` `CLK6` `CLK7` `CLK8`

…but that defeats the point of repeated sheets.

## Best practice here
Keep:

- child sheet ports = `CLK1..CLK4`
- repeated sheet = `REPEAT(CH,1,7)`

Then let Altium compile them as channelised nets.

## How to check it
Open:

- **Project Options → Multi-Channel**
- then **Compile**
- then inspect compiled nets / navigator / cross probe

You should see the signals resolved by channel context, not all shorted together.

## Simple mental model
Think of each repeated sheet as its own folder:

- folder `CH1` contains `CLK1..CLK4`
- folder `CH2` contains `CLK1..CLK4`
- folder `CH3` contains `CLK1..CLK4`

Same filenames, different folders, therefore different objects.

That’s exactly how their independence is maintained.

The next thing to verify is whether on the **parent sheet** you are trying to drive those 28 lines individually, or whether they only need to exist locally inside each channel. That decides whether you should keep plain sheet entries or move to harness/bus style naming.

[M11] ME (2026-03-09 04:11):
[image]
The why do connectors say j5 channel 5 for example but the clocks still just say base number 
[attached file: IMG_456A6ADA-611E-4E21-8923-33B92B71D430.jpeg]

[M12] AI (2026-03-09 04:11):
Because **components** and **nets** are being handled differently.

`J5_CH5` is a **component designator after multichannel annotation**.  
`CLK1` is just the **local net/port label text shown on the schematic**.

Those are not the same thing.

## What’s happening

### Components
When Altium repeats a channel, it can annotate the duplicated parts so they become unique, for example:

- `J5_CH1`
- `J5_CH2`
- `J5_CH3`
- …
- `J5_CH5`

So the connector itself gets a channel suffix in the **designator**.

### Nets / ports
The text you see on the sheet is usually the **base local name**:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Altium often leaves that visible text unchanged on each repeated child sheet, because the uniqueness is carried in the **compiled channel context**, not by rewriting the visible label.

So although you see `CLK1`, internally it is more like:

- `CH1.CLK1`
- `CH2.CLK1`
- `CH3.CLK1`
- …
- `CH5.CLK1`

## So why doesn’t the label visibly change?
Because that label is just the schematic’s local declaration.

Think of it like this:

- `J5_CH5` = the actual unique component instance name
- `CLK1` = the local signal name inside that sheet template

The sheet tab `CH5` at the bottom is already telling you which instance you are looking at. So on the `CH5` tab, that `CLK1` is effectively **the CH5 instance of CLK1**.

## Simple analogy
Like a repeated folder structure:

- Folder `CH1` contains file `CLK1`
- Folder `CH2` contains file `CLK1`
- Folder `CH5` contains file `CLK1`

Same visible filename, different folder path.

But components are more like physical items in a master list, so Altium gives them globally unique identifiers such as `J5_CH5`.

## What to trust
Trust the **compiled context**, not just the visible child-sheet text.

If you want to prove it:

- Compile the project
- Open the **Navigator** or compiled document view
- Cross-probe from the PCB pad/net
- Check which compiled net name/path Altium reports

You should find that `CLK1` on `CH5` is not the same net as `CLK1` on `CH4`.

## The key rule
Visible sheet text:
- often stays as base name

Compiled identity:
- includes channel scope

Component designators:
- usually get explicit suffixes so each placed part is globally unique

That is why `J5_CH5` looks expanded, while the clock still appears as just `CLK1`.

The next useful check is to click the `CLK1` wire or port and open its properties / compiled net info so we can confirm exactly how your Altium settings are presenting the channelised net names.

[M13] ME (2026-03-09 04:11):
[image]
But when I hover over it 
[attached file: IMG_93FE4F73-8953-454E-B5EC-0659A9079461.jpeg]

[M14] AI (2026-03-09 04:11):
That hover is the important clue — and it suggests something is **not right yet**.

You are on the **CH5 tab**, but the tooltip is showing:

- `Port CLK1 (Output)`
- `NetP12_CH1_1 (Physical Name)`

If that is genuinely the CH5 instance, I would expect something reflecting **CH5**, not **CH1**.

So this means one of two things:

## Most likely
Altium is showing the **physical compiled net name inherited from the original template/master channel**, while the visible sheet tab is just the repeated view.

That can happen in some multichannel views: the **displayed instance** is CH5, but the underlying “physical name” shown in the hover comes from the compiled naming convention based on the seed/original channel object.

## But there is also a possible problem
If cross-probing and PCB updates are behaving oddly, then this may mean the nets are **not being separated the way you expect**.

So don’t trust the hover text alone. Verify it properly.

## What the tooltip fields mean
You’re seeing two different identities:

- `CLK1` = the **logical port name**
- `NetP12_CH1_1` = the **physical compiled net name**

The physical name is what matters for uniqueness.

The worrying bit is that it says **CH1** while you are looking at **CH5**.

## First thing to check
Click the **wire**, not just the port, and open **Properties**.  
See whether the **Compiled Net Name / Physical Name** stays as `CH1` everywhere, or changes by channel.

Do this on:
- CH1 `CLK1`
- CH5 `CLK1`

If both say the same physical name, then they are not independent.  
If CH1 says `...CH1...` and CH5 says `...CH5...`, then you are fine and the earlier hover may have been misleading.

## Best verification method
Do one of these:

### Method 1 — PCB side
In PCB:
- click the pad for `P12_CH5`
- inspect the connected net name
- compare with `P12_CH1`

Those should be on different nets.

### Method 2 — Navigator / compiled nets
After compile:
- open **Navigator**
- locate `CLK1` in CH1 and CH5
- check whether they resolve to separate compiled nets

### Method 3 — compile messages / connection matrix
Run a full compile and inspect whether Altium reports repeated-channel uniqueness correctly.

## My current reading
From this screenshot alone, I would say:

- your **sheet-entry structure is now broadly correct**
- but the **compiled physical naming still needs verifying**
- the `CH1` in the hover on a `CH5` sheet is suspicious enough that I would not assume it is correct yet

## Practical next step
Check one very concrete thing:

Hover or inspect these two nets and compare:
- `P12` on **CH1**
- `P12` on **CH5**

If both show the same physical net name, the channels are collapsing.  
If they show different physical net names, then you are okay and Altium is just presenting the local port text separately.

The cleanest proof will be a screenshot of:
- **CH1 CLK1 hover**
- **CH5 CLK1

[M15] ME (2026-03-09 04:17):
And also, how do I best change that net name when it enters another sheet to something meaningful like image_1

[M16] AI (2026-03-09 04:17):
Best practice is: **don’t rename the same net at every sheet boundary unless you truly want a new logical signal name**.

For your case, there are really two clean options.

## Option 1 — keep the local repeated name, rename it only at the top-level destination
Use this when `CLK1` is just a local channel signal, but once it reaches another functional block you want it described by purpose.

Example:

- in repeated sheet: `CLK1`
- on parent repeated-sheet entry: `CLK1`
- then on the receiving/top-level side, connect that sheet entry to a net label like:
  - `IMAGE_1`
  - `IMAGE_CLK_A`
  - `SENSOR1_PIXCLK`

That way:
- the repeated block stays tidy and reusable
- the higher-level sheet carries the meaningful system name

This is usually the best approach.

## Option 2 — rename the port/sheet entry itself
Use this when the signal is not really a generic `CLK1`, but actually always represents `IMAGE_1`.

Then rename consistently:

- child-sheet port: `IMAGE_1`
- parent sheet entry: `IMAGE_1`

But if you do this inside a repeated channel, you would typically want something generic enough to repeat cleanly, otherwise the repeated-sheet abstraction starts breaking down.

---

## What I would recommend for you
Because you have:

- 7 repeated sheets
- 4 clocks per sheet
- likely a reusable channel template

I would keep the channel sheet generic:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Then on the parent/top sheet, where those outputs feed the next block, give them meaningful names there.

For example:

- `CH1.CLK1` goes to net label `IMAGE_1`
- `CH1.CLK2` goes to `IMAGE_2`
- `CH1.CLK3` goes to `IMAGE_3`
- `CH1.CLK4` goes to `IMAGE_4`

- `CH2.CLK1` goes to `IMAGE_5`
- etc.

That is much easier to manage.

---

## How to do it in Altium
On the receiving sheet, just place a **Net Label** on the wire after the port/sheet entry connection and call it `IMAGE_1`.

Important point:
- if two directly connected wire segments have different net labels, Altium will not let them both define different names for the same continuous net cleanly
- so the usual method is to connect through the hierarchical port/sheet-entry boundary, then apply the meaningful label on the destination side

In other words:

**Sheet A**
- port = `CLK1`

**Top sheet**
- sheet entry from repeated block = `CLK1`
- wire from that entry goes to receiving block
- place net label on that wire: `IMAGE_1`

**Receiving sheet**
- matching port = `IMAGE_1`

So the rename happens at the hierarchical interface.

---

## Important rule
A **port-to-sheet-entry transition** is the cleanest place to rename by function.

A **continuous wire with two different labels** is not.

---

## For your exact use case
If you want `CLK1` from a repeated channel to become `IMAGE_1` in another sheet, do this:

1. In repeated child sheet, keep port as `CLK1`
2. On parent repeated sheet symbol, keep entry as `CLK1`
3. Route that connection on the parent sheet to the next block
4. Name that parent-level net `IMAGE_1`
5. On the destination child sheet, use port `IMAGE_1`

That gives:
- reusable repeated channel
- meaningful system naming outside it

---

## One caution
Because you have 28 such signals, hand-renaming them one by one can get messy fast.

So choose one scheme and stick to it, for example:

- `IMAGE_01` to `IMAGE_28`

or

- `CH1_IMAGE_1`
- `CH1_IMAGE_2`
- ...
- `CH7_IMAGE_4`

The second scheme is often easier to debug.

---

## My recommendation
Use:

- inside repeated sheet: `CLK1..CLK4`
- at top-level parent interconnect: `CHx_IMAGE_y` or `IMAGE_01..28`

That keeps the repeated sheet reusable and the system wiring meaningful.

If you show me the next-sheet interface, I can tell you exactly where to place the port, sheet entry, and net label so `CLK1` becomes `IMAGE_1` cleanly.

[M17] ME (2026-03-09 04:37):
[image]
I’ve readied it all from
Foundations of updated reuse block 
[attached file: IMG_948BA77A-A9B3-4CBC-A52C-0DC310BC16F0.jpeg]

[M18] AI (2026-03-09 04:37):
That looks much healthier.

What I can see now is:

- component instance is channelised: `P12_CH2`
- local port label is still `CLK1`
- you are viewing the `CH2` instance tab

That is the pattern I’d expect from a repeated reusable block.

So at this point, the **reuse block foundation looks broadly correct**.

## What this means
You’ve now got two layers working together:

- **physical component identity**  
  `P12_CH2`, `J5_CH5`, etc

- **logical local signal identity inside the reused channel**  
  `CLK1`, `CLK2`, `CLK3`, `CLK4`

That is exactly how a reusable multichannel block is meant to look.

## What to do next
Now stop changing names inside the child sheet and move to **verification**.

### 1. Compile the project
Run a full compile first.

You want to check that:
- no duplicate-net errors appear for the repeated channels
- no port/sheet-entry mismatches remain
- no accidental global-net warnings appear

### 2. Compare one signal across two channels
Pick the same signal in two channels, for example:

- `P12_CH1`
- `P12_CH2`

Then inspect or hover both and compare the **physical net name**.

They should not be the same physical net.

### 3. Push ECO to PCB
If compile is clean:
- Design » Update PCB
- inspect the ECO carefully before executing

You want to see:
- channelised component designators carried through
- no unexpected component deletions
- no collapsing of equivalent nets across channels

### 4. Only rename at the top level if needed
Do **not** rename `CLK1` inside the reused block now.

If later you want meaningful system names such as:
- `IMAGE_1`
- `IMAGE_2`
- `IMAGE_3`

do that on the **parent/interconnect sheet**, not inside the reusable child block.

## My recommendation from here
Treat the child block as frozen:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`
- `SR_D_IN`
- `SR_D_OUT`

Then map those to meaningful external names at the next hierarchical level.

## One small cleanup
You still have names like:

- `SR_D-IN`
- `SR_D-OUT`

I would still change those to:

- `SR_D_IN`
- `SR_D_OUT`

before finalising, just to avoid awkward naming later.

## Decision point
If your goal now is to get this into the main design safely, the next critical step is not more renaming — it is:

**compile, inspect physical net uniqueness, then ECO to PCB**

Show me the compile result or the ECO preview next.

[M19] ME (2026-03-09 04:39):
[image]
Saying it’s got all these extra components 
[attached file: IMG_F51BB937-9464-4687-92E7-894C8B6F51F3.jpeg]

[M20] AI (2026-03-09 04:39):
Yes — that message is about the **PCB not having those repeated-channel parts yet**, not that the multichannel setup is wrong.

`[Extra Component] ... Comparator [IC2_CH1] ... [IC2_CH2] ...`

means:

- those components exist in the **schematic**
- but Altium cannot find matching linked components in the **PCB**
- so from the comparator’s point of view they are “extra” on the schematic side

In practice, with what you’ve just built, that is often exactly what you’d expect before a proper update.

## Why you’re seeing loads of them
Because once you turned the block into:

- `CH1`
- `CH2`
- `CH3`
- ...
- `CH7`

Altium instantiated all those repeated parts, so one original component became:

- `IC2_CH1`
- `IC2_CH2`
- `IC2_CH3`
- ...
- `IC2_CH7`

If the PCB only had the old non-repeated version, or only one seed version, the comparator now sees the other channel instances as new schematic components.

## So this does **not** automatically mean failure
It usually means one of these situations:

### Case 1 — expected and okay
You have created the repeated channels in schematic, but have **not yet added/linked them into PCB**.

Then “Extra Component” on the schematic side is normal.

### Case 2 — old links are stale
The PCB still has old component links from before the reuse/multichannel conversion, so Altium cannot match the new `_CHx` designators to the old parts.

### Case 3 — dangerous if mixed with deletions
If the ECO also wants to **remove** lots of legacy PCB parts unexpectedly, then you need to stop and inspect carefully before executing.

## What to do right now
Do **not** judge from the Messages panel alone.  
Open the actual **Engineering Change Order preview** and inspect both:

- components to be **added**
- components to be **removed**
- component **matches/links**

## What you want to see
Ideally:

- new `_CH1` to `_CH7` components being added if they are genuinely new
- no accidental deletion of unrelated legacy board circuitry
- repeated-channel parts grouped consistently

## What would worry me
If ECO is trying to:

- remove your existing main design blocks
- replace good existing components with a different channel instance
- relink unrelated parts to the wrong `_CHx` instance

That would suggest link corruption rather than a clean multichannel expansion.

## The likely root cause in your case
Given your earlier struggle, I suspect this is mainly:

- the schematic has now expanded properly into repeated channel instances
- the PCB component links have not yet been reconciled to that new structure

So the comparator is just telling you:
“these schematic components have no PCB counterpart yet.”

## The clean way to think about it
Before repeat:
- one `IC2`

After repeat:
- `IC2_CH1`
- `IC2_CH2`
- `IC2_CH3`
- ...
- `IC2_CH7`

If the PCB only knew about one old `IC2`, then six or seven “extra component” notices are expected.

## What I’d do next
Go to:

- **Design → Update PCB Document**
- inspect the **ECO list itself**, not just Messages

Then look specifically for:

1. **Add Component**
   for the `_CHx` parts

2. **Remove Component**
   anything legacy or unrelated

3. **Match Components**
   whether old parts are being matched sensibly or not

## Decision rule
If the ECO is mainly:

- **adding** `_CHx` channel parts
- and not deleting unrelated existing circuitry

then you are probably on the right path.

If the ECO is:

- adding the channels
- **and** removing chunks of your original board that should stay

then stop, because the component links need sorting first.

## One important note
Because you are merging this into an existing design, the comparator messages alone can look alarming. “Extra Component” does not mean “bad component”; it just means “present in one domain, not matched in the other.”

The next screenshot I need is the **ECO preview window** showing:
- Add Component
- Remove Component
- Update Net / Class / Room items

That will tell us whether it is safe to proceed.

[M21] ME (2026-03-09 04:43):
[image]
[image]
Saying things duplicate even though it has an out and in 
[attached file: IMG_DBEB15F2-DDB2-412D-861A-DC89649C6550.jpeg]
[attached file: IMG_EB257425-108F-41DF-9D37-02ED66EE3A35.jpeg]

[M22] AI (2026-03-09 04:43):
What you’re showing is most likely **not an in/out-direction problem**.

An `Output` on one sheet and an `Input` on another does **not** by itself cause a duplicate-net-name issue. If they are meant to connect, that is normal.

The actual problem is usually one of these:

## 1. You have two different naming objects on the same continuous wire
For example on the same connected net you may have:

- a **Port** called `DRAIN_0`
- and a **Net Label** also trying to name it
- or another port/net label nearby with a conflicting effective name

If the wire is continuous, Altium expects **one net identity**, not multiple competing definitions.

## 2. You are mixing sheet-entry/port naming with direct net labels
If the signal comes through hierarchy, then usually:

- **port/sheet entry** handles the hierarchy crossing
- **net label** handles the local wire naming

If you use both in a way that renames the same piece of wire twice, Altium can complain.

## 3. Off-grid / tiny gap / accidental junction issue
From photos like this, a classic Altium problem is:

- it looks connected
- but one end is slightly off-grid or not snapped
- so one short wire segment has one name
- the adjacent segment has another
- then the compiler reports duplicate/conflicting net identifiers

## 4. Harness/bus entry confusion
Those arrow-looking objects can sometimes be sheet entries / ports / off-sheet connectors depending on what was placed. If one side is a **Port** and the other is actually a **Net Label** or **Off-Sheet Connector**, Altium may be treating the naming differently than you expect.

---

## The key thing
**Input vs Output is for ERC checking.**  
**Net naming is separate.**

So “one is in and one is out” does not solve duplicate naming if the same wire is being named twice inconsistently.

---

## What to do now
On the offending signal, inspect each object one at a time.

For `DRAIN_0`:

1. Click the arrow object on one side  
   Check whether it is:
   - Port
   - Off-sheet connector
   - Harness entry
   - Net label

2. Click the wire itself  
   See what net name it says.

3. Click the object on the other side  
   Confirm it is the same object type and same name.

4. Look for any extra **net label** hidden on that same wire segment.

---

## Clean rule to use
For hierarchical sheet-to-sheet connections, use this pattern:

- **Port** on child sheet
- **Sheet Entry** on parent sheet
- matching names
- no extra net label unless you intentionally want the parent-sheet wire named there

So for example:

**Child sheet A**
- Port: `DRAIN_0`

**Parent sheet**
- Sheet entry from child A: `DRAIN_0`
- wire
- sheet entry into child B: `DRAIN_0`

**Child sheet B**
- Port: `DRAIN_0`

That is clean.

If instead you do this on one continuous connection:

- Port `DRAIN_0`
- plus net label `GATE_1`
- plus another hierarchical object

then Altium can quite reasonably complain.

---

## From your screenshots
I suspect one of these two is happening:

### Most likely
There is a **local wire/net label naming conflict** on that line, not a direction conflict.

### Also possible
You have placed the wrong object type on one side — for example an **Off-Sheet Connector** or label where a **Port** should be.

---

## Fastest way to prove it
Use one troublesome signal only, say `DRAIN_0`, and simplify it:

- remove any extra net labels on that wire
- leave only the hierarchy objects
- make sure both ends are true **Ports** in child sheets and **Sheet Entries** in parent
- recompile

If the duplicate error disappears, the issue was naming-object overlap.

---

## Practical debugging sequence
For one signal:

1. Delete the wire and redraw it on-grid.
2. Delete and replace both end objects deliberately:
   - child sheets = **Port**
   - parent sheet = **Sheet Entry**
3. Remove any separate net label from the same connection.
4. Compile again.

That usually flushes out this exact class of issue.

If you send the actual compiler text for one of the duplicate messages, I can decode exactly which two objects Altium thinks are fighting.

[M23] ME (2026-03-09 04:44):
[image]
One of them says it’s a netxxx
[attached file: IMG_6FAACA66-A4B2-4F34-9BDB-DC4D3555AD11.jpeg]

[M24] AI (2026-03-09 04:44):
Yes — that explains it.

Altium is telling you the **same physical wire is being given two different names**:

- `Wire DRAIN_0`
- `Wire NetJ3_F20`

So the duplicate is not because one end is input and the other output.  
It is because one object says the net is `DRAIN_0`, while another object on that same connection is causing Altium to auto-name it as `NetJ3_F20`.

## What `NetJ3_F20` means
That is an **automatic net name** Altium has generated from an unlabelled connection, typically from a pin, such as:

- connector `J3`
- pin `F20`

So somewhere on that path, Altium thinks the wire is just an unnamed net attached to `J3-F20`.

## Why this happens
Usually one of these is true:

### 1. The wire is not actually continuous
It looks connected, but there is:
- a tiny gap
- off-grid join
- broken segment
- missing junction

So one side is called `DRAIN_0`, and the other disconnected side gets auto-named `NetJ3_F20`.

### 2. Wrong object type
You may have:
- a **Port** on one side
- an **Off-Sheet Connector** or **Net Label** on the other
- or a sheet-entry/port mismatch

That can leave one part hierarchical and another part local/unnamed.

### 3. The label is not attached to the exact wire segment you think
Sometimes the net label or port is sitting visually on the wire, but not snapped properly, so Altium does not apply the intended name.

## What to do for this exact error
For `DRAIN_0`, do this very mechanically:

### On the sheet where the error is flagged:
1. Delete the existing wire segment for that signal.
2. Delete the `DRAIN_0` naming object on that segment too.
3. Re-place the correct object:
   - **Net Label** if it is a local sheet connection
   - **Port** if it is crossing hierarchy
4. Re-draw the wire **on-grid** from the actual pin to the object.
5. Make sure the connection highlights as one continuous net.

## Important rule
If the signal is crossing between sheets, use:

- **Port** on child sheet
- **Sheet Entry** on parent sheet

Do **not** rely on a local net label alone for that hierarchical crossing.

If it is only local within one sheet, then use a **Net Label** and no port.

## Your specific clue
Because Altium says:

- one is `DRAIN_0`
- one is `NetJ3_F20`

that strongly suggests the intended name is not reaching the connector pin cleanly.

So I would start at the connector end near `J3 F20` and remake that connection first.

## Fast test
After redrawing, hover the wire near the connector pin.

You want it to say only:
- `DRAIN_0`

and **not**:
- `NetJ3_F20`

## Best fix sequence
For one offending net only:

1. Zoom right in.
2. Turn snap/grid sensible.
3. Delete wire + label/port.
4. Re-add the correct naming object.
5. Rewire from the pin.
6. Compile again.

If that clears one, repeat for the others.

## What this means overall
Your compiler is not saying “duplicate net name exists elsewhere in the project.”  
It is saying “this one connection currently has two competing identities.”

That is much more fixable.

If you show the actual `J3/F20` end of the `DRAIN_0` connection, I can tell you exactly whether that end should be a net label, port, or sheet entry.

[M25] ME (2026-03-09 04:47):
[image]
But it highlights as it should on both 
[attached file: IMG_6BAEA844-9748-4B58-AFEA-F6E43998828B.jpeg]

[M26] AI (2026-03-09 04:47):
Yes — and that’s the trap with Altium.

**Highlighting proves electrical continuity of the selected connection path.**  
It does **not** prove there is only one naming source on that path.

So both of these can be true at once:

- the wire highlights end-to-end
- the compiler still says the wire has two names:
  - `DRAIN_0`
  - `NetJ3_F20`

That means the connection is continuous, but Altium still sees **two net identifiers attached to the same connected copper/wire**.

## What that usually means
One of these objects on that highlighted path is imposing a second name:

- a **Net Label**
- a **Port**
- an **Off-Sheet Connector**
- a **Sheet Entry**
- sometimes a hidden naming object copied in by accident

So the issue is not “is it connected?”  
The issue is “how many different naming objects are naming it?”

## Your screenshot gives a strong clue
You have a dense field of red arrow-style hierarchical objects around that area. In that situation the usual failure mode is:

- one side names the net `DRAIN_0`
- another hierarchical object or label on the same continuous path is still effectively naming it from the connector side, so Altium falls back to `NetJ3_F20`

## The important distinction
**Connection highlight** follows the wire network.  
**Compiler duplicate-name check** compares net identities applied to that network.

So highlight can look perfect while compile still fails.

## What to do next for `DRAIN_0`
Do this on just that one signal:

### 1. Click every object on the highlighted path
Not just the wire. Click:
- the red arrow on the right
- the left-side naming object
- any label on or near the wire
- the connector pin end

Look in Properties and identify exactly what each one is.

You are looking for an accidental mix such as:
- Port on one side
- Off-sheet connector on the other
- plus a net label on the wire

That will do it.

### 2. Temporarily strip naming back
For `DRAIN_0` only:

- delete the wire
- delete both end naming objects
- re-place only the correct hierarchical objects
- redraw the wire on-grid

### 3. Use one naming method only
For sheet-to-sheet hierarchical connection, the clean method is:

- child sheet: **Port** named `DRAIN_0`
- parent sheet: **Sheet Entry** named `DRAIN_0`

Do not also place a separate net label on the same parent wire unless you really need it.

## Very likely in your case
Those red double-chevron objects look like hierarchical connectors, but in dense copied designs it is easy to end up with:
- an off-sheet connector where a port should be, or
- a net label sitting on top of a port entry

Visually they can look “fine” and highlight fine, but compiler still sees two naming authorities.

## Best proof
Open the exact compiler error row and look at the **Details** pane, like you did before.  
If it lists:

- `Wire DRAIN_0`
- `Wire NetJ3_F20`

then one object on that same connection is still unnamed or differently named from the connector side.

## Fastest cleanup method
For each bad net:

1. Delete the whole signal path between the connector and the hierarchical entry.
2. Re-place the correct object type at the boundary.
3. Rewire it fresh.
4. Recompile immediately.

This is often faster than hunting invisible copied naming artefacts.

## One thing I’d check specifically
Because the autogenerated name is `NetJ3_F20`, inspect the **J3 pin F20 end** closely. That is the end Altium thinks is still carrying an unnamed/local identity. The fault is often right there:
- tiny off-grid join
- label not snapped
- wrong connector object type at the boundary

If you send a zoomed-in shot of just the `J3 / F20 / DRAIN_0` region with one object selected so Properties are visible, I can tell you exactly which object is wrong.

[M27] ME (2026-03-09 05:02):
[image]
[image]
When I call drain 0 drain 1 they go from both not working to both working 
[attached file: IMG_03DACFAB-9F4C-415E-B1DA-A67C745BE453.jpeg]
[attached file: IMG_62E90A8E-CA43-4D67-851C-6F12A8688F6D.jpeg]

[M28] AI (2026-03-09 05:02):
That points to the real issue: this is almost certainly **not a wire-break problem**.

It means the error is driven by **name collisions elsewhere in the project hierarchy**.

When you rename:

- `DRAIN_0` → `DRAIN_1`

and then suddenly both compile cleanly, that tells us Altium is not objecting to the local connection itself. It is objecting because `DRAIN_0` is already being asserted somewhere else in a way the compiler dislikes.

## What that means
`DRAIN_0` is probably already present as one of these somewhere else:

- another **Port**
- another **Sheet Entry**
- another **Off-Sheet Connector**
- a **Net Label** on a different sheet
- or a repeated-sheet compiled name that resolves onto the same parent scope

So with `DRAIN_0`, Altium sees two naming authorities that clash.

When you change it to `DRAIN_1`, you move away from that collision, so it clears.

## Why both can “start working”
Because the issue is by **name**, not by that specific wire geometry.

You are effectively moving the conflict from one identifier to another.

## Most likely cause in your design
From the screenshots, you have a lot of similarly named hierarchical signals:

- `DRAIN_0`
- `DRAIN_1`
- `DRAIN_2`
- `DRAIN_3`
- `GATE_0`
- etc.

And you also have repeated blocks plus top-level interface sheets.

So the most likely problem is:

### You have the same signal name appearing in more than one hierarchical context, but not consistently through pure port/sheet-entry flow.

Common examples:
- `DRAIN_0` exists as a port on one child sheet and also as a net label on the parent
- `DRAIN_0` exists on two sibling sheets with flat/global behaviour somewhere
- an off-sheet connector is making the name effectively global within the document
- project hierarchy mode/settings are not matching the way the sheets were drawn

## Big clue from your screenshots
Those red chevron objects are very likely **Off-Sheet Connectors**, not Ports.

That matters a lot.

### Off-Sheet Connectors
- connect nets between sheets at the same hierarchical level / within flat style usage
- can easily create naming collisions

### Ports
- are for true hierarchical sheet entry/exit

If you are using **Off-Sheet Connectors** where you should be using **Ports**, Altium can absolutely produce this kind of “duplicate net” behaviour.

## I think this is the key issue
On hierarchical designs, for child-sheet interfaces, use:

- **Ports** on the child sheets
- **Sheet Entries** on the parent sheet symbols

Not off-sheet connectors.

Your red double-chevron symbols look like off-sheet connectors, and that would explain why names are colliding unpredictably.

## What to do
### On these interface sheets:
Check the object type of `DRAIN_0`, `DRAIN_1`, etc.

If they are **Off-Sheet Connectors**, replace them with **Ports** where hierarchy is intended.

Use this rule:

- **Same sheet only**: wire + net label
- **Across hierarchical sheets**: port + sheet entry
- **Off-sheet connector**: only when intentionally using document-level off-sheet connectivity, not normal parent/child hierarchy

## Why this matches your symptom
With off-sheet connectors, names like `DRAIN_0` can become effectively shared across places you did not intend.

So:
- `DRAIN_0` may conflict
- `DRAIN_1` may not
- changing one name can make another suddenly “work”

That is classic wrong-connectivity-object behaviour.

## Practical fix
For one test signal only:

1. Delete the red `DRAIN_0` connector object.
2. Place a **Port** instead, named `DRAIN_0`.
3. On the parent sheet symbol, make sure the matching **Sheet Entry** is also `DRAIN_0`.
4. Recompile.

If that fixes the duplicate issue for that signal, you’ve found it.

## Also check project hierarchy mode
In Project Options, inspect the connection style / hierarchy handling. A mismatch between:
- hierarchical design intent
- and flat/off-sheet style objects

can make this much worse.

## What I think is happening in plain English
You are mixing **hierarchical multichannel/reuse-block design** with **off-sheet style connectors**.

That makes names like `DRAIN_0` behave as broader-scope names than you expect, so the compiler flags duplicates.

## Best next move
Select one of those red arrows and confirm its object type. If it says **Off-Sheet Connector**, that is the first thing to change.

[M29] ME (2026-03-09 05:46):
A if these signal go somewhere on same sheet keep the signal red but as they go another sheet add a port?

[M30] AI (2026-03-09 05:46):
Yes — that’s the clean rule.

## Use these objects like this

### Same sheet only
Use:
- **wire**
- **net label**

That keeps the signal local to that schematic sheet.

Example on one sheet:
- wire
- net label `DRAIN_0`

### Going into / out of another sheet hierarchically
Use:
- **Port** on the child sheet
- **Sheet Entry** on the parent sheet symbol

That is the proper hierarchical method.

Example:
- child sheet port: `DRAIN_0`
- parent sheet symbol entry: `DRAIN_0`

### Do not use Off-Sheet Connectors for this hierarchical flow
Those red arrows are often the thing that causes the confusion if the design is meant to be hierarchical.

---

## So for your case
If a signal just routes around **within TOP_PoGo_Interface.SchDoc**, keep it as:

- wire
- net label

If that signal needs to leave that sheet and connect through the hierarchy, then at the boundary use a:

- **Port**

and on the parent sheet use the matching:

- **Sheet Entry**

---

## Simple decision test
Ask:

“Does this signal need to cross a sheet boundary?”

- **No** → wire + net label
- **Yes** → port + sheet entry

---

## One important caution
Do not leave both on the same boundary path unless you really mean it.

For example, avoid:
- red off-sheet connector
- plus port
- plus extra net label

on one interface, because that is exactly how duplicate naming trouble starts.

---

## Recommended cleanup
For these interface sheets:

- replace the red off-sheet style connectors with **Ports** where they connect to another sheet
- keep plain local net labels only for signals that stay inside that sheet

That should make the hierarchy behave much more predictably.

If you show one full parent/child example, I’ll tell you exactly which side gets the port and which side gets the sheet entry.

[M31] ME (2026-03-09 05:48):
So I can have both? If a single stays on sheet and also goes to another sheet

[M32] AI (2026-03-09 05:48):
Yes.

That is normal.

If a signal is used **locally on the sheet** and also needs to **leave the sheet**, you can have:

- the **wire** on that sheet
- a **net label** naming that local net
- a **port** connected to that same wire so it passes through hierarchy

So one continuous local net can both:
- feed circuitry on the current sheet
- and go out through a port to another sheet

## Correct pattern
On the child sheet:

- wire from source
- local circuitry taps onto that wire
- net label `DRAIN_0` on the wire
- port `DRAIN_0` also attached to the same wire

That is fine.

Then on the parent sheet:
- matching **sheet entry** `DRAIN_0`

## What is fine
**Net label + Port with the same name on the same net**  
That is usually okay and often useful.

## What is not fine
- net label `DRAIN_0`
- port `DRAIN_1`

on the same wire

or mixing in:
- off-sheet connector
- another different naming object

on that same net

That creates the duplicate/conflict problem.

## Best practice
If the signal leaves the sheet, I’d usually do:

- local wire
- **Port** for hierarchy crossing
- optional **net label** only if it helps readability

If the port name already makes it obvious, sometimes you can skip the extra net label and just use the port as the identifier on that sheet boundary.

## Simple rule
Same net can have:
- **local usage**
- **port to parent**
- **same signal name**

That is okay.

The names just need to match exactly.

So in your case:
- local wire name = `DRAIN_0`
- port name = `DRAIN_0`
- parent sheet entry = `DRAIN_0`

That is the safe setup.

[M33] ME (2026-03-09 06:31):
But it’s saying duplicate net names 

[M34] AI (2026-03-09 06:31):
Right — and that means Altium is seeing **more than one net-naming object for the same connected net**, or the wrong connectivity object type.

Having both is allowed only if they are:

- on the **same wire**
- and have the **same exact name**
- and you are using the **right object types**

## Safe combination
This is okay:

- local **Net Label** = `DRAIN_0`
- **Port** on same wire = `DRAIN_0`

because both say the same thing.

## What causes “Duplicate Net Names”
Usually one of these:

- **Net Label** `DRAIN_0` on the wire, but **Port** is actually `DRAIN_1`
- a hidden/overlapping second naming object
- using an **Off-Sheet Connector** instead of a **Port**
- same signal name appearing elsewhere through flat/off-sheet connectivity
- wire looks connected, but naming object is snapped to a different segment
- hierarchy mismatch: **Port** on child but no matching **Sheet Entry** on parent, or mixed styles

## In your case, the biggest suspect
Those red arrow objects are very likely **Off-Sheet Connectors**.

If so, that is probably the cause.

For a hierarchical design, replace them with:

- **Port** on child sheet
- **Sheet Entry** on parent

Do not use Off-Sheet Connectors for parent/child hierarchy.

## Clean rule for your design
On child sheet:
- local circuitry connected by wire
- optional **Net Label** for readability
- **Port** to leave sheet

All with the **same name**.

On parent sheet:
- matching **Sheet Entry**

## Fastest fix
For one bad signal, e.g. `DRAIN_0`:

1. Delete the red arrow object.
2. Place a **Port** named `DRAIN_0`.
3. Keep or add a **Net Label** `DRAIN_0` on the same wire if you want.
4. Check parent sheet symbol has **Sheet Entry** `DRAIN_0`.
5. Recompile.

If that clears it, repeat for the others.

## The key point
You **can** have both a net label and a port.

You **cannot** have mixed naming/connectivity styles on the same signal and expect Altium not to complain.

Select one of the red arrows and check its object type. If it says **Off-Sheet Connector**, replace it with a **Port**.

[M35] ME (2026-03-09 06:33):
[image]
These ones. Regs go elsewhere on sheet, ports go off sheet 
[attached file: IMG_77CBFB38-07D2-499F-9D47-454892E302A1.jpeg]

[M36] AI (2026-03-09 06:33):
Yes — that arrangement is fine.

What I’m seeing there is:

- **yellow net labels** on the local wires for on-sheet use
- **red ports** on the same nets for hierarchical off-sheet connection

That is a valid pattern **provided the names match exactly** on each net.

So for example, this is okay:

- local net label: `LOC_SPI_1_CLK`
- port on same wire: `LOC_SPI_1_CLK`

and likewise for:
- `LOC_SPI_1_MOSI`
- `LOC_SPI_1_MISO`

## Why this works
The yellow label gives the wire its local sheet name.  
The red port exposes that same net through the sheet boundary.

That lets the signal:
- feed circuitry on the current sheet
- and also leave the sheet

## The catch
From your screenshot, the red port text appears to include extra hierarchical path text after the signal name, for example something like:

- `LOC_SPI_1_CLK Digital_Control[...]`

That suggests you may be looking at **compiled display text**, or the object is carrying more than just the simple name.

For clean hierarchy, the actual **port name** should just be:

- `LOC_SPI_1_CLK`
- `LOC_SPI_1_MOSI`
- `LOC_SPI_1_MISO`

Nothing more.

If the visible long suffix is really part of the port’s actual name, that will cause trouble.

## What to check
Click one red object and look in Properties.

You want:
- **Object Type** = `Port`
- **Name** = just the signal name, e.g. `LOC_SPI_1_CLK`

If it says **Off-Sheet Connector**, that is the wrong object for hierarchical child-sheet export.

## Correct rule
Use:

- **Net Label** for local same-sheet naming
- **Port** for leaving the sheet
- **Sheet Entry** on the parent sheet symbol

That is exactly the method you’re describing.

## So the answer is
Yes:
- **labels** where the signal also stays on this sheet
- **ports** where the same signal goes off to another sheet

And both can sit on the same net.

## One strict condition
They must all use the **same exact simple signal name**.

So not:
- label = `LOC_SPI_1_CLK`
- port = `LOC_SPI_1_CLK Digital_Control[2D]`

That would be a mismatch.

## Best practice here
Keep the local names simple and identical across the hierarchy boundary:

- child sheet wire label: `LOC_SPI_1_CLK`
- child sheet port: `LOC_SPI_1_CLK`
- parent sheet entry: `LOC_SPI_1_CLK`

That will be the cleanest setup.

[M37] ME (2026-03-09 06:33):
[image]
Why is it giving me an error then 
[attached file: IMG_FD71709B-1AAA-466A-85FA-9B31D7D2CB7B.jpeg]

[M38] AI (2026-03-09 06:33):
Because Altium is seeing **two separate net-naming objects of the same name on one sheet**, not one label plus one port in a clean hierarchical boundary.

Your message says:

- `Duplicate Net Names Wire LOC_SPI_1_CLK`
- `Duplicate Net Names Wire LOC_SPI_1_MISO`
- `Duplicate Net Names Wire LOC_SPI_1_MOSI`

That usually means **the same net name is being asserted more than once in a way the compiler treats as duplicate**, most often on the same sheet.

## The likely reason in your screenshot
You have:

- a **yellow net label** `LOC_SPI_1_CLK`
- and a **red hierarchical object** also named `LOC_SPI_1_CLK`

If that red object is a **Port**, this can still trip duplicate-net-name checking depending on project settings and object arrangement. If it is an **Off-Sheet Connector**, it is even more likely.

So although electrically the idea is valid, **Altium’s compiler is objecting to two explicit naming objects on the same wire**.

## Best fix
For signals that leave the sheet hierarchically, use just:

- **Port** on the child sheet

and remove the extra **Net Label** if it has the same name.

So for these three:
- `LOC_SPI_1_CLK`
- `LOC_SPI_1_MISO`
- `LOC_SPI_1_MOSI`

do this on the child sheet:

- keep the wire
- keep the **Port**
- delete the yellow **Net Label**

The port itself is enough to name the net locally and hierarchically.

## Why this works
A port already gives that wire its name on the sheet.  
You do not need a second naming object with the same text on the same net.

## What to keep labels for
Use a yellow **Net Label** when the signal is only local to the sheet.

Use a **Port** when the signal leaves the sheet.

If a signal both stays local and leaves the sheet, the **Port alone** is usually enough. The local circuitry can still connect to that wire.

## So the practical rule becomes
- local-only net → **Net Label**
- off-sheet hierarchical net → **Port**
- avoid label + port of same name on the same wire unless you know your settings allow it cleanly

## One more issue in your error list
You also have:

- `Missing child-sheet in OS.SchDoc in Symbol Repeat(U_OS,1,2) ...`

That is separate, but important. It means one repeated sheet symbol is pointing at a child sheet Altium cannot resolve. That can also destabilise compile behaviour, so fix that too.

## Do this next
1. Remove the yellow labels from:
   - `LOC_SPI_1_CLK`
   - `LOC_SPI_1_MISO`
   - `LOC_SPI_1_MOSI`
2. Leave only the ports for those nets.
3. Recompile.
4. Then fix the missing child-sheet reference.

That should tell you quickly whether these duplicate-net errors are simply from double naming.

[M39] ME (2026-03-09 06:36):
[image]
[image]
Still doing it 
[attached file: IMG_5010A714-9B27-40C3-9BD1-D9161A97E358.jpeg]
[attached file: IMG_23A1EA8F-1C75-41E7-9E43-C6ED82577907.jpeg]

[M40] AI (2026-03-09 06:36):
That means there is **still another `LOC_SPI_1_CLK / MISO / MOSI` naming object somewhere else on the same schematic document**, on a **different disconnected wire**.

The clue is the exact wording:

- `Duplicate Net Names Wire LOC_SPI_1_CLK`

That usually means **two separate wires** in that sheet are both being named `LOC_SPI_1_CLK`.

Not:
- a port-direction issue
- not usually a continuity issue
- not because the one shown is wrong by itself

## What is most likely happening
On `U_Digital_Control` you now have one visible label here:

- `LOC_SPI_1_CLK`
- `LOC_SPI_1_MISO`
- `LOC_SPI_1_MOSI`

but somewhere else on that same sheet there is probably another:

- net label
- port
- or copied naming object

with the same names, on wires that are **not physically connected**.

That is exactly what triggers this error.

## Why it still happens after removing the red ports
Because the conflict is no longer “label + port on same wire”.

It is now more likely:
- `LOC_SPI_1_CLK` exists in **two places on the sheet**
- same for MOSI and MISO

## What to do now
On `U_Digital_Control.SchDoc`:

### 1. Search for each name on that sheet
Use Find / Navigator / SCH Filter and search:

- `LOC_SPI_1_CLK`
- `LOC_SPI_1_MISO`
- `LOC_SPI_1_MOSI`

You are looking for **more than one object** with each name.

### 2. Check whether they are actually connected
If two `LOC_SPI_1_CLK` labels are on separate wires, Altium flags duplicate net names.

### 3. Keep only one naming origin per disconnected net
So either:
- connect them physically if they are meant to be the same net

or
- rename one of them if they are actually different signals

## Fastest practical method
Click the error row, then look in the **Details** pane at the bottom.  
It should list the conflicting objects for that error.

If you expand / click that error carefully, Altium usually reveals the two objects involved.

## Very likely scenario in your design
Because this is a big hierarchical design, I suspect you have one of these elsewhere on the same sheet:

- another local label near a port block
- another copied label from an earlier interface version
- a hidden/overlapped label under other text
- a second sheet entry/port conversion remnant

## Important distinction
It is perfectly fine to use `LOC_SPI_1_CLK` on **another sheet**.

It is **not** fine to have **two disconnected nets on the same sheet document** both called `LOC_SPI_1_CLK`.

## Also fix this separately
You still have:

- `Missing child-sheet in OS.SchDoc in Symbol Repeat(U_OS,1,2)`

That is a different compile problem and should be fixed too, but it is not the root cause of these SPI duplicate-name errors.

## Best next step
On `U_Digital_Control.SchDoc`, search for `LOC_SPI_1_CLK` and count how many objects exist with that exact text. If it is more than one disconnected location, that is the fault.

[M41] ME (2026-03-09 06:37):
[image]
Yes it’s a bus used multiple times over the sheet 
[attached file: IMG_035375F2-B170-4D44-875A-BB5E87B85620.jpeg]

[M42] AI (2026-03-09 06:37):
That’s it.

If `LOC_SPI_1_CLK`, `LOC_SPI_1_MISO`, `LOC_SPI_1_MOSI` are being used **multiple times on the same sheet** on **separate disconnected wire stubs**, Altium will flag **Duplicate Net Names**.

## Why
A **net label** names a local net on that sheet.

So if you place `LOC_SPI_1_CLK` in two different places on the same sheet, Altium reads that as:

- one net called `LOC_SPI_1_CLK` here
- another separate net also called `LOC_SPI_1_CLK` there

If they are not physically connected, that is a duplicate-name error.

## Important distinction
This is different from a **bus**.

A bus is just an organisational drawing object. It does **not** magically permit repeating the same net label all over the sheet unless the connections are actually resolved properly.

## What to do instead

### If they are meant to be the same signal all across the sheet
Use one of these methods:

- physically wire them together
- or use **Ports / Sheet Entries** through hierarchy
- or use **Off-Sheet Connectors** only if you are intentionally using flat same-level sheet connectivity
- or use a proper bus/harness breakout with unique members

### If you want the same signal to appear in several places on one sheet without long wires
Do **not** just scatter identical net labels everywhere if your project settings flag duplicates.

Instead use:
- ports/hierarchy properly, or
- a single named source and route cleanly, or
- off-sheet connectors if that document is intentionally flat

## In your exact case
Because this is one big sheet and you’re reusing those SPI names in multiple locations, the compiler is effectively saying:

“You have several disconnected wires all called `LOC_SPI_1_CLK` on this same document.”

That is why it errors.

## Best fix for this sheet
For these SPI signals, pick one method and stay consistent:

### Best hierarchical method
- keep the signal named once locally where it originates
- use **Ports** where it leaves the sheet
- use matching **Sheet Entries** on parent sheets
- avoid repeating the same yellow net label on multiple disconnected places of the same sheet

### If this sheet is meant to be a single flat sheet with repeated references
Use **Off-Sheet Connectors** or another approved sheet-to-sheet method, not multiple isolated local net labels.

## Practical rule
On one sheet:

- one net label name should normally correspond to one connected local net
- if the same name appears again elsewhere on that sheet, it should usually be physically the same net or you’ll get this error

## So yes:
The reason is **not** that the names are wrong.  
It is that they are being used **multiple times on the same sheet as separate islands**.

## What I’d do now
For `LOC_SPI_1_CLK`, `MISO`, `MOSI`:

- remove repeated yellow labels from secondary locations
- keep the naming at the true source/interface point
- use ports/hierarchical connectivity for the rest

That should clear those duplicate errors.

[M43] ME (2026-03-09 07:30):
So a bus?

[M44] AI (2026-03-09 07:30):
Not by itself.

A **bus** helps organise and draw grouped signals, but it does **not** solve “same net label repeated on separate disconnected wires” on its own.

## What a bus does
A bus is mainly for grouping signals like:

- `LOC_SPI_1_CLK`
- `LOC_SPI_1_MISO`
- `LOC_SPI_1_MOSI`

or more typically indexed signals like:

- `DATA[0..7]`

It makes the drawing cleaner.

## What a bus does not do
A bus does **not** mean you can place `LOC_SPI_1_CLK` in several disconnected places on the same sheet and expect Altium to treat them as one net automatically.

Each actual signal still needs a proper connection method.

## In your case
For named SPI lines repeated around one sheet, a plain bus is probably **not the main fix**.

You have three realistic options:

### 1. Proper wires
Physically wire them across the sheet.
Messy, but unambiguous.

### 2. Ports / sheet entries
Best if they are really moving between sheets hierarchically.

### 3. Off-sheet connectors
Use only if this is intended as flat same-level sheet connectivity, not parent/child hierarchy.

## For one large sheet used like a distribution page
If you want to reference the same SPI lines in multiple places on the **same sheet** without long wires, then Altium usually wants one of these approaches:

- physically connect them
- or restructure the design so those interfaces cross sheets through ports
- or use sheet-level connectivity objects intentionally

But **multiple isolated net labels with the same name on one sheet** is what is causing your error.

## So: “So a bus?”
A bus can help presentation, but the real fix is:

- **not repeating disconnected local net labels on the same sheet**

If you want, I can tell you the best structure for your exact SPI case:
- keep on one big sheet,
- split into smaller sheets with ports,
- or use harness/bus entries properly.

[M45] ME (2026-03-09 07:30):
It’s all on the same sheet and complains when same signal ref I used 

[M46] AI (2026-03-09 07:30):
That’s expected in Altium.

On the **same sheet**, you generally **cannot use the same net label on multiple disconnected wires** and expect it to behave like a “named jump.” Altium treats that as **duplicate net names**.

So if it is all on one sheet:

- `LOC_SPI_1_CLK` here
- `LOC_SPI_1_CLK` elsewhere
- and they are **not physically wired together**

then the compiler complains.

## So what Altium wants on one sheet
On a single sheet, a net label is naming **that connected wire network** only.

It is **not** a global same-sheet teleporter.

## Your options on one sheet

### Best/cleanest
Physically wire the same signal to everywhere it goes.

### If the sheet is getting too crowded
Split the design into smaller sheets and use:
- **Ports**
- **Sheet Entries**

That is usually the proper scalable fix.

### Do not do this
Do not scatter the same local net label around one sheet in multiple islands.

That is exactly what the compiler is rejecting.

## So the answer is
Because it is **all on the same sheet**, the repeated signal reference is being interpreted as:

- multiple separate nets
- all claiming the same name

Hence the error.

## Practical rule
On one sheet:
- one net name should normally appear on one connected network

If you want the same signal in several places without long wires, that is usually a sign the sheet wants breaking up hierarchically.

## For your SPI lines
Since they are repeated around the sheet, the proper choices are:

- wire them properly across the sheet, or
- split the logic into child sheets and use ports

A bus alone will not fix that naming rule.

[M47] ME (2026-03-09 07:58):
[image]
How do you turn off sheet links. The blue text here 
[attached file: IMG_13E482AA-E63D-4F75-8851-D2EDEB3C7E3F.jpeg]

[M48] AI (2026-03-09 07:58):
That blue text is the **connection / sheet link display** overlay.

To turn it off in Altium schematic:

**View → Connections → Hide All**  
or toggle off the specific connection display option from that same menu.

On many versions, the quickest route is:

- **View**
- **Connections**
- choose **Hide All**

If it is specifically showing compiled sheet links / net connection paths, also try:

- **View → Connections → Off Sheet Connections**
- untick it

or

- **View → Connections → Net Names**
- untick as needed

From your screenshot, you’re already in the right area — the menu is open at **View**, and the item you want is under **Connections**.

So:
1. Click **View**
2. Hover **Connections**
3. Select **Hide All**

That should clear the blue overlay text.

If it stays on, send the next submenu screenshot and I’ll point at the exact checkbox.

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] ME (2026-03-09 04:03):
[image]
[image]
[attached file: IMG_7AC6162B-D2E9-4548-AF73-05B5A0A8A7C2.jpeg]
[attached file: IMG_0DD2A7AF-EF77-40A9-AA8E-AA661D94C6CB.jpeg]

[A2] AI (2026-03-09 04:03):
Yes — **that second screenshot is the right direction**.

Your child-sheet ports now look correctly named as plain base names:

-
