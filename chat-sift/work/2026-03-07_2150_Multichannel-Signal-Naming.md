# Multichannel Signal Naming
Date (UTC): 2026-03-07 21:50
Conversation ID: 69ac9d77-c73c-8386-bc8e-ea6adf3c9a42
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-07 21:50):
What’s the principles with multi channel signal naming using ports. I have 7 sheets I’ve created 7 channels for. Each channel has 4 clocks and they are numbered clk 1-28

[M2] AI (2026-03-07 21:50):
The main principle is this:

**Inside a multichannel sheet, name signals by function, not by global absolute number.**  
Then let the **channel context** create uniqueness.

So for your case, the clean approach is usually:

- within the repeated sheet: `CLK_A`, `CLK_B`, `CLK_C`, `CLK_D`
- or `CLK1`, `CLK2`, `CLK3`, `CLK4` **per channel**
- then Altium makes them unique by channel index/path

That is normally better than trying to hard-code `CLK1` to `CLK28` across the repeated sheets.

## Why

In multichannel design, the repeated sheet is supposed to represent **one reusable circuit block**.  
So signal names inside that block should describe the signal’s **role within the block**, not its final system-wide instance number.

Think of it like this:

- Sheet block = one channel template
- Channel instance = Ch1, Ch2, Ch3 … Ch7
- Local signals inside template = `CLK1..CLK4`
- Final compiled identity becomes something like:
  - Channel1.`CLK1`
  - Channel2.`CLK1`
  - Channel3.`CLK1`

So the repeated block stays tidy and easy to maintain.

---

## Good naming strategy

### Best practice inside each repeated channel sheet
Use:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

or even clearer:

- `CLK_A`
- `CLK_B`
- `CLK_C`
- `CLK_D`

Then identify the channel at the **sheet entry / harness / parent sheet** level.

### At the parent sheet
Name the channel instances clearly, for example:

- `CH01`
- `CH02`
- `CH03`
- `CH04`
- `CH05`
- `CH06`
- `CH07`

Then the compiled nets remain logically separated by channel.

---

## What not to do unless you really need system-global names

Avoid building the repeated child sheet so that one copy contains:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

and the next contains:

- `CLK5`
- `CLK6`
- `CLK7`
- `CLK8`

and so on manually.

Why this becomes awkward:

- it defeats the point of a reusable repeated block
- harder to edit later
- more error-prone
- harder to review and debug
- channel replication becomes less clean

If one block changes, you want it to change once, not 7 separately renumbered variants.

---

## Ports specifically

With **ports**, the same rule applies:

- ports on the repeated child sheet should usually be **local functional names**
- uniqueness should come from the **sheet instance**, not from forcing unique absolute numbering into the port names

So your child sheet ports would ideally be:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

not:

- `CLK1`, `CLK2`, `CLK3`, `CLK4` on sheet 1
- `CLK5`, `CLK6`, `CLK7`, `CLK8` on sheet 2

unless the sheets are actually intended to be different non-repeated designs.

---

## When global numbering can make sense

Absolute naming like `CLK1` to `CLK28` can be useful when:

- the clocks are routed to an FPGA pin list or connector pinout that is already fixed globally
- test documentation or external interfaces expect absolute names
- you want a board-level naming convention visible outside the repeated hierarchy

In that case, the better pattern is often:

### Option 1: keep local names internally, map globally at top level
Inside each repeated block:

- `CLK1..CLK4`

At top level or interface:

- `CH1_CLK1`
- `CH1_CLK2`
- `CH1_CLK3`
- `CH1_CLK4`
- …
- `CH7_CLK4`

This is much clearer than flat `CLK1..CLK28`, because the channel grouping remains obvious.

### Option 2: if absolute numbering is required, still encode channel grouping
For example:

- `CH1_CLK1`
- `CH1_CLK2`
- `CH1_CLK3`
- `CH1_CLK4`
- `CH2_CLK1`
- …
- `CH7_CLK4`

That is usually better engineering notation than just `CLK1..CLK28`, because you can immediately see structure.

---

## Practical recommendation for your design

For **7 repeated channels with 4 clocks each**, I would recommend:

### Inside the repeated child sheet
Use:
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

### Channel identifiers
Use:
- `CH1` … `CH7`

### Externally / documentation / FPGA pin mapping
Refer to them as:
- `CH1_CLK1` to `CH1_CLK4`
- `CH2_CLK1` to `CH2_CLK4`
- …
- `CH7_CLK1` to `CH7_CLK4`

That gives you:
- clean reusable schematic blocks
- good multichannel behaviour
- readable PCB/net/debug naming
- easier documentation

---

## Key principle with ports vs net labels

A useful rule:

- **Ports** define connectivity between sheets
- **Net labels** define local net naming within a sheet
- **Multichannel uniqueness** comes from the repeated sheet instance, not from manually making every port globally unique

So in repeated designs, do not panic if the same child-sheet port names repeat. That is normal, as long as the multichannel structure is set up correctly.

---

## One warning

If you flatten or partially break multichannel hierarchy, repeated simple names like `CLK1` can collide unexpectedly.

So make sure:

- the repeated sheets are properly instantiated as channels
- you are not mixing accidental flat connectivity
- ports/sheet entries are aligned consistently
- you inspect the **compiled document / compiled nets** to confirm the final naming behaviour

That compiled view is the truth.

---

## Rule of thumb

Use this decision test:

**Ask:** “Is this name describing the signal’s job in one channel, or its unique identity on the whole board?”

- if it describes the job in one repeated channel → use `CLK1..CLK4`
- if it describes a board-wide interface → use `CHx_CLKy`

For your case, the most robust convention is probably:

**schematic block internal names:** `CLK1..CLK4`  
**system-level names/documentation:** `CH1_CLK1` … `CH7_CLK4`

If you want, I can sketch exactly how I’d name the **ports, sheet entries, harnesses, and FPGA-side nets** for a 7-channel Altium multichannel project so it stays clean during ECO and PCB back-annotation.

[M3] ME (2026-03-07 22:01):
[image]
So like that and so forth 
[attached file: IMG_1B1D5755-6E7C-48A0-8095-A8BBF594E875.jpeg]

[M4] AI (2026-03-07 22:01):
Yes — **that is the right sort of idea**, but with one important distinction:

What you have shown is **two layers of repetition at once**:

- the **sheet itself** is repeated `Repeat(CLK_,1,7)` → 7 channel instances
- then some **sheet entries inside it** are also repeated, for example `Repeat(CLK_1,1,4)`

That can be valid, but you need to be clear what each repetition means.

## What your image currently means

Your sheet symbol says:

- `Repeat(CLK_,1,7)`

So Altium will create 7 instances:

- `CLK_1`
- `CLK_2`
- `CLK_3`
- `CLK_4`
- `CLK_5`
- `CLK_6`
- `CLK_7`

Then inside each of those, you have entries like:

- `Repeat(CLK_1,1,4)`
- `Repeat(CLK_2,1,4)`
- `Repeat(CLK_3,1,4)`
- `Repeat(CLK_4,1,4)`

So that is effectively saying:

for **each channel sheet**, generate four instances of each of those entry patterns.

That is probably **not what you want** if your intention is simply:

- 7 channels
- each channel has 4 clocks

Because right now you are mixing:
- **channel repetition**
with
- **clock-index repetition**
in a way that may explode into more names than intended.

---

# Cleaner principle

For your case, the best structure is usually:

## Option A — most sensible
Repeat the **sheet only**, and keep the ports fixed within the child sheet.

### Parent sheet symbol
- `Repeat(CH,1,7)`

### Sheet entries on that symbol
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`
- maybe `SR_IN`
- maybe `SR_OUT`

### Child sheet ports
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`
- `SR_IN`
- `SR_OUT`

That gives you:

- Channel 1 has `CLK1..CLK4`
- Channel 2 has `CLK1..CLK4`
- etc

Compiled, Altium distinguishes them by channel path.

This is normally the cleanest multichannel method.

---

## What I would avoid here

I would avoid naming the sheet itself `CLK_` and then also having entries like `CLK_1`, `CLK_2`, etc.

That gets confusing fast because:

- is `CLK_1` the **channel name**?
- or the **first clock**?
- or both?

You want one naming axis for **channel number** and another for **clock number**.

---

# Better naming convention

Use:

## Repeated sheet designation
- `CH`

with:
- `Repeat(CH,1,7)`

Then inside each channel:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

So conceptually you get:

- `CH1.CLK1`
- `CH1.CLK2`
- `CH1.CLK3`
- `CH1.CLK4`
- `CH2.CLK1`
- etc

That is much easier to read than:

- `CLK_1` sheet
- with `CLK_1`, `CLK_2`, `CLK_3`, `CLK_4` entries

because those names overlap in meaning.

---

# For your exact screen

So instead of this sort of thing:

- `Repeat(CLK_,1,7)`
- `Repeat(CLK_1,1,4)`
- `Repeat(CLK_2,1,4)`
- `Repeat(CLK_3,1,4)`
- `Repeat(CLK_4,1,4)`

I would usually make it:

## Sheet symbol
- `Repeat(CH,1,7)`

## Entries
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`
- `SR_IN`
- `SR_OUT`

And on the child sheet use those exact port names.

---

# When would repeated sheet entries make sense?

Repeated entries like:

- `Repeat(DATA,1,8)`

make sense when **one channel itself contains an array/bus-like repeated interface**.

For example:
- one ADC channel with 8 data bits
- one control block with 16 gain lines
- one sensor block with 12 repeated outputs

But in your case, with just **4 distinct clocks per channel**, it is normally simpler to just write:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

manually.

That is clearer and less fragile.

---

# So, direct answer

**Yes, “like that and so forth” in principle — repeated sheet for 7 channels — yes.**  
But I would **not** structure the clock entries exactly the way shown unless you specifically need nested repetition.

I would change it to:

### Parent repeated sheet
`Repeat(CH,1,7)`

### Fixed ports on that sheet
`CLK1`, `CLK2`, `CLK3`, `CLK4`, `SR_IN`, `SR_OUT`

That is the clean multichannel approach.

---

# Practical rule

Use this split:

- **sheet repetition** = channel count
- **port names** = signal role within one channel

So:

- channel identity from the repeated sheet
- clock identity from the port name

not both mixed into one label.

---

# Your target naming model should be

Not:
- `CLK_1 ... CLK_28`

Better:
- `CH1_CLK1`
- `CH1_CLK2`
- `CH1_CLK3`
- `CH1_CLK4`
- `CH2_CLK1`
- ...
- `CH7_CLK4`

Even if Altium internally compiles them hierarchically, that is the mental model you want.

---

The one thing I’d watch next is your **`SR_IN` / `SR_OUT` chain**, because that may need to be treated differently from the four per-channel clocks if it is daisy-chained between channels rather than independent. That part changes how the top-level sheet entries should be connected.

[M5] ME (2026-03-07 22:07):
[image]
Like that?
[attached file: IMG_2B5306FB-F288-425B-8CAC-FF34D7D009DB.jpeg]

[M6] AI (2026-03-07 22:08):
Yes — **that is much closer**.

You now have a sensible separation:

- `Repeat(CH,1,7)` = 7 channel instances
- `Repeat(CLK,1,4)` = 4 clock signals per channel

That is the right general structure for:

- 7 repeated sheets
- each with 4 repeated clocks

## What this now means

Altium will interpret it roughly as:

- `CH1` has `CLK1..CLK4`
- `CH2` has `CLK1..CLK4`
- ...
- `CH7` has `CLK1..CLK4`

So conceptually:

- `CH1.CLK1`
- `CH1.CLK2`
- `CH1.CLK3`
- `CH1.CLK4`
- `CH2.CLK1`
- etc

That is a clean multichannel model.

---

## But one important point

Your other entries are still:

- `Repeat(CLK_IN,1,7)`
- `Repeat(SR_IN,1,7)`
- `Repeat(SR_OUT,1,7)`

Those should only be repeated **if they are genuinely separate per-channel signals at this parent level**.

So ask what each one really is.

### `CLK`
If each channel has 4 separate clock outputs, then:
- `Repeat(CLK,1,4)` is fine

### `CLK_IN`
If there is only **one clock feed into each child sheet** and that then generates/distributes 4 internal clocks, then `Repeat(CLK_IN,1,7)` may be fine.

But if the four clocks are the actual per-channel interfaces, then `CLK_IN` may be redundant or wrong.

### `SR_IN` / `SR_OUT`
This depends on architecture:

- if each channel has its own independent `SR_IN` and `SR_OUT`, repeating them is fine
- if the shift register path is **daisy-chained between channels**, then you usually do **not** want them treated as 7 unrelated repeated nets without care

That is the bit most likely to trip you up.

---

# Cleanest version depends on your real circuit intent

## Case 1 — independent per-channel control
Each channel is standalone and has:
- one `SR_IN`
- one `SR_OUT`
- four clocks

Then your setup is broadly fine.

## Case 2 — daisy chain across all 7 channels
For example:
- top level `SER_DATA_IN` enters CH1
- CH1 `SR_OUT` goes to CH2 `SR_IN`
- CH2 `SR_OUT` goes to CH3 `SR_IN`
- ...
- CH7 `SR_OUT` becomes final chain output

Then `SR_IN` and `SR_OUT` are not just “7 separate repeated I/Os” in the same sense. They are part of an inter-channel chain, and you need to wire that chain deliberately at the parent level.

---

# One naming refinement I would suggest

What you have is valid, but I would personally make the clock port slightly clearer:

- `Repeat(CLK,1,4)`

is okay, but a bit generic.

You may prefer:

- `Repeat(CLK_OUT,1,4)`

or if these are four named phases/functions:

- `CLK_A`, `CLK_B`, `CLK_C`, `CLK_D`

Reason: when debugging compiled names, plain `CLK1` can still be a little vague.

But this is optional. Structurally your version is fine.

---

# The key check now

Open the **compiled hierarchy / compiled nets** and verify you get something like:

- `CH1\CLK1`
- `CH1\CLK2`
- `CH1\CLK3`
- `CH1\CLK4`
- `CH2\CLK1`
- etc

and not accidental flattening or collisions.

That compiled result is the real answer.

---

# My verdict on your screenshot

**Yes, that is the right direction.**  
This is now much more correct than the earlier version.

The only thing still needing thought is whether:

- `Repeat(CLK_IN,1,7)`
- `Repeat(SR_IN,1,7)`
-

[M7] ME (2026-03-07 22:08):
One thing st a time 

[M8] AI (2026-03-07 22:08):
Yes — **that is much closer**.

But for **one thing at a time**, here is the single point:

## The sheet repeat is right
`Repeat(CH,1,7)` is the correct idea for **7 channel instances**.

## The bit to watch
`Repeat(CLK,1,4)` will create:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

That is fine **if the child sheet port is also set up to match that repeated entry scheme**.

So at this stage:

- `Repeat(CH,1,7)` = good
- `Repeat(CLK,1,4)` = also good in principle

## But
I would **not** also repeat `CLK_IN`, `SR_IN`, `SR_OUT` by `1,7` on that same sheet symbol unless those are genuinely meant to be separate per-channel signals at that hierarchy level.

For now, the main answer to your question is:

**Yes, that is the right direction.**

Next thing to check is just this:

On the child sheet `CH.SchDoc`, do you have:
- a single port called `CLK`
that is itself repeated internally,

or do you have:
- ports `CLK1` to `CLK4`?

That one detail determines whether `Repeat(CLK,1,4)` is correct or not.

[M9] ME (2026-03-07 22:09):
[image]
So how do I get the ports sorted out in the child sheets 
[attached file: IMG_74862C2C-CF21-4AEA-AB02-25A6D0C809A8.jpeg]

[M10] AI (2026-03-07 22:09):
In the child sheet, make the ports match the repeated entry pattern.

Since your parent sheet now has:

- `Repeat(CH,1,7)`
- `Repeat(CLK,1,4)`

the child sheet should usually have **one port base name**, not four manually different ones.

## What to do in the child sheet

On `CH.SchDoc`, place a port and name it:

- `CLK`

Then use the port’s repeat setting so Altium expands it to:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

So do **not** manually place separate child-sheet ports called:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

if you are already using `Repeat(CLK,1,4)` at the sheet-symbol level.

## In practice

For each repeated signal family:

- parent sheet entry: `Repeat(CLK,1,4)`
- child sheet port: `Repeat(CLK,1,4)` or port name `CLK` with the repeat definition in its properties

The exact field depends on version/UI, but the principle is:
- same base token
- same repeat count/range
- same direction as needed

## For your screenshot

That top one currently says `CLK1`.  
Change that approach to a repeated port definition based on `CLK`, not a one-off explicit `CLK1`.

So instead of building the child sheet with explicit individual ports, make it a repeated port group.

## The logic

You want:

- parent creates 7 channel instances
- within each channel, the clock port group expands to 4 nets

So the child is a **template**, not a manually numbered instance.

## What the end result should look like conceptually

At parent:
- `Repeat(CH,1,7)`
- `Repeat(CLK,1,4)`

At child:
- `Repeat(CLK,1,4)`

Then compiled result becomes something like:
- `CH1\CLK1`
- `CH1\CLK2`
- `CH1\CLK3`
- `CH1\CLK4`
- `CH2\CLK1`
- etc

## Important trap

Do not mix:
- parent entry `Repeat(CLK,1,4)`
with child ports manually named `CLK0`, `CLK1`, `CLK2`, `CLK3`

That often causes mismatch or confusion.

Also, I can see on your screenshot the existing net labels look like `CLK0`, `CLK1`, maybe higher. That is okay internally, but the **port naming scheme must match the repeated interface scheme**. Ideally standardise them all one way.

## Best next move

On the child sheet:

1. Delete the manually separate clock ports.
2. Place one port.
3. Set it to repeated as `CLK` from 1 to 4.
4. Then tie the internal nets to those four expanded clock nets consistently.

One more detail: your schematic seems to use `CLK0`, `CLK1`, etc. If so, decide now whether your clock numbering is:
- `1..4`
or
- `0..3`

and keep it consistent everywhere. Do not mix both.

For clarity, if the parent says `Repeat(CLK,1,4)`, then child nets should also be `CLK1..CLK4`, not `CLK0..CLK3`.

[M11] ME (2026-03-07 22:12):
[image]
[attached file: IMG_827B26DC-CE6A-47E4-AF4C-D7437342AB4D.jpeg]

[M12] AI (2026-03-07 22:12):
Yes — that is the correct form **in principle**.

`repeat(CLK,1,4)` on the child-sheet port is the right sort of thing for generating:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

## But your next check is the important one

Your actual nets on the sheet look like they are named:

- `CLK0`
- `CLK1`
- ...
- `CLK7`

So at the moment there is a mismatch.

If the port says:

- `repeat(CLK,1,4)`

then inside this child sheet it expects to connect to:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

not `CLK0` and not `CLK7`.

## So right now you need to choose one convention

### Option 1
Use:
- `repeat(CLK,1,4)`

Then rename the internal nets for that channel to:
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

This is the cleanest.

### Option 2
If you really want zero-based numbering, use:
- `repeat(CLK,0,3)`

Then your child-sheet nets should be:
- `CLK0`
- `CLK1`
- `CLK2`
- `CLK3`

That would also be valid.

---

## The bigger issue

I can also see net labels like `CLK7` on this same child sheet.

That suggests this child sheet may currently contain **absolute board-wide clock names**, not **template per-channel names**.

For a repeated child sheet, that is usually wrong.

The child sheet should describe **one channel template only**.

So inside one repeated child sheet, you generally want only:

- `CLK1..CLK4`
or
- `CLK0..CLK3`

not:
- `CLK0..CLK7`

because `CLK7` sounds like a board-level absolute signal, not a within-channel signal.

---

## So the immediate answer

**Yes, that port text is right.**  
But to make it work properly, the child-sheet internal net names must match the repeat range exactly.

For example, if you keep:

`repeat(CLK,1,4)`

then the nets that connect to those ports in this sheet must be:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

and this sheet should represent just one reusable channel, not all 7-channel absolute names mixed in.

## Best next step

Rename the four clock nets in this child sheet to one consistent local set:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Then leave the parent as:
- `Repeat(CH,1,7)`
- `Repeat(CLK,1,4)`

That is the clean model.

[M13] ME (2026-03-07 22:16):
[image]
[image]
[attached file: IMG_0BF28FDD-550C-48A1-84FA-20CC0F1DA8E1.jpeg]
[attached file: IMG_48618A7C-7C34-453E-B683-210D4F7B75BF.jpeg]

[M14] AI (2026-03-07 22:16):
You’re nearly there. The key point from those screenshots is:

**the repeated port is fine, but it does not rename your existing net labels for you.**

So when you place:

- `repeat(CLK,1,4)`

Altium creates the **port interface family** `CLK1..CLK4`.

But the wire it connects to still has to resolve cleanly on the child sheet.

## What your screenshots are showing

You have things like:

- `CLK1`
- `CLK2`
- and also compiled suffix text like `CH[8B]`, `CH[8C]`

That means Altium is already trying to apply multichannel context. That part is good.

So the important check is simply this:

### For each clock wire in the child sheet
it should connect to a repeated port member that matches its local name:

- clock wire 1 → `CLK1`
- clock wire 2 → `CLK2`
- clock wire 3 → `CLK3`
- clock wire 4 → `CLK4`

## What to do now

On the child sheet, do **not** try to make one repeated port physically connect to multiple unrelated wires by magic.

Instead, place the repeated port family and connect each expanded member to the matching local net.

In practice, that means:

- keep `repeat(CLK,1,4)`
- make sure the four nets beside it are named `CLK1`, `CLK2`, `CLK3`, `CLK4`
- wire each one to the correct connection point

## From your screenshots

The top image shows the wire label as `CLK1` and the next as `CLK2`.  
That is correct **provided** you continue with:

- `CLK3`
- `CLK4`

for the other two.

So yes, that part looks right.

## The only thing to avoid

Do not leave the child sheet with mixed absolute names like:

- `CLK7`
- `P901_CLK7`
- etc

as the actual logical channel clock names.

Those reference designators are fine as component names, but the **net labels/ports for the repeated interface** should stay as the template names:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

The repeated channel hierarchy will make them unique later.

## So the answer

Yes — the screenshots suggest you are now doing the right thing:

- repeated child-sheet port: `repeat(CLK,1,4)`
- local child-sheet clock nets: `CLK1`, `CLK2`, etc

That is the correct pattern.

The next step is just to do the same for all four clocks, compile, and then check the compiled names resolve as separate channel instances rather than one flat set.

[M15] ME (2026-03-07 22:18):
It only allows for 1 net as soon as i introduce two as per my pictures it moves to the latest updated 

[M16] AI (2026-03-07 22:18):
Yes — that behaviour is the clue.

A **single port object** on the child sheet can only attach to **one wire/net** at one physical location.

So when you use one port labelled:

`repeat(CLK,1,4)`

Altium is treating that as **one repeated interface definition**, not as four separate physical port symbols you can connect to four different wires in four places. That is why it keeps “moving” to the most recently attached net.

## So the practical answer is

For the child sheet, use **four separate ports**.

Name them:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

and connect each one to its own wire.

## Then at the parent sheet

You can still use:

- `Repeat(CH,1,7)`

But for the clock entries, the cleanest approach is often just:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

on the sheet symbol as four normal sheet entries.

That already gives you:

- CH1 → CLK1..CLK4
- CH2 → CLK1..CLK4
- etc

because the **sheet repetition** is what creates the channel instances.

## The key correction

I was pushing the repeated-port idea too far for this use case.

For **four separate physical clock nets within one repeated channel sheet**, do **not** try to use one repeated child-sheet port object to represent all four connections.

Use:

- one repeated sheet block for the **7 channels**
- four normal ports in the child for the **4 clocks**

That is the stable way to do it.

## In your case, do this

### Child sheet `CH.SchDoc`
Place four ports:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

### Parent sheet symbol
Keep:

- `Repeat(CH,1,7)`

Then add four sheet entries:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

not `Repeat(CLK,1,4)`.

## Why this works better

Because the channel repetition is already giving you the array behaviour you need.

You do **not** need a second layer of repeat for the four clocks unless you are doing something much more array-like and uniform.

Right now you just want:

- 7 repeated channels
- each channel has 4 named clock connections

That is simpler as **plain named ports** inside the repeated sheet.

## Resulting compiled intent

You will effectively get:

- `CH1.CLK1`
- `CH1.CLK2`
- `CH1.CLK3`
- `CH1.CLK4`
- `CH2.CLK1`
- ...
- `CH7.CLK4`

without fighting the editor.

## Bottom line

Because each clock is a separate physical connection, the child sheet should have **four separate ports**, not one repeated port object.

So yes — the fact it only lets one net stick is exactly why you should now switch to:

- child ports = `CLK1..CLK4`
- parent repeated sheet = `Repeat(CH,1,7)`

That is the right model here.

[M17] ME (2026-03-07 22:20):
[image]
Like that?
[attached file: IMG_8542F6E2-314B-42C2-BDC6-956C63982657.jpeg]

[M18] AI (2026-03-07 22:20):
Yes — **that is the right approach**.

You now want the child sheet to have **separate normal ports**:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

each attached to its own local clock net.

## So your model is now

### Parent sheet symbol
- `Repeat(CH,1,7)`

with sheet entries:
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

### Child sheet
ports:
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

That is the clean, stable setup for:
- 7 repeated channels
- 4 clocks per channel

## One thing to check in your screenshot

I can still see text like:

- `CLK2 CH[8C]`

That is Altium showing compiled channel context, which is fine.  
But make sure the **actual local net label** for that wire is just:

- `CLK2`

not some absolute/global variant.

## Next step

Do the same for all four clocks, then go back to the parent sheet and make sure the repeated channel block has four matching sheet entries:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

No `Repeat(CLK,1,4)` needed now.

## Bottom line

**Yes — like that.**  
This is the right way for your case.

[M19] ME (2026-03-07 22:20):
So I delete my previous signal nets 

[M20] AI (2026-03-07 22:20):
Yes — **if those previous signal net labels were only there to force the old global naming scheme**.

Keep this distinction clear:

## Keep
- the **actual wires**
- the **ports** `CLK1`, `CLK2`, `CLK3`, `CLK4`
- any component designators like `P901_CLK7` etc

## Delete or rename
- the old **net labels** that are imposing absolute names like `CLK7`, `CLK12`, etc on the child sheet

Because the child sheet should now be a **template channel**, not a globally numbered instance.

So on the repeated child sheet, the logical signal names should just be:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

## Important rule
If a wire is directly connected to a port, you often do **not** need a separate matching net label as well.

So for each clock wire in the child sheet, you can usually do either:

- port named `CLK1` attached to that wire

or

- net label `CLK1` on that wire

but you do not need both unless it helps readability.

## Best clean-up for your case
For the child sheet:

- remove old global clock net labels
- keep the new local ports
- only add local net labels `CLK1..CLK4` if needed for clarity elsewhere on the sheet

## What not to leave behind
Do not leave a child-sheet wire with:
- port `CLK1`
and also
- net label `CLK7`

That creates naming conflict/confusion.

## So the practical answer
Yes — **delete the old signal net labels if they represent the previous absolute numbering scheme** and replace that naming with the new local per-channel naming.

The child sheet should look like one reusable channel, not channel 7 specifically.

[M21] ME (2026-03-07 22:25):
[image]
Where is it getting that cool 7 from before the channel number 
[attached file: IMG_A640B1AE-5E66-4F80-9620-6D117D8591E3.jpeg]

[M22] AI (2026-03-07 22:25):
That **7** is almost certainly coming from the **existing local net name**, not from the channel index.

From your screenshot, names like:

- `J905_CLK7_CH4`
- `P915_CLK7_CH4`

show Altium thinks the underlying net is something like:

- `CLK7_CH4`

So it has combined:

- **clock name** = `CLK7`
- **channel context** = `CH4`

## In other words

The `7` is probably being inherited from one of these on that child sheet:

- an old **net label** like `CLK7`
- a **port** named `CLK7`
- a **sheet entry** named `CLK7`
- possibly a parameter-driven compiled name from the original multichannel setup

## Most likely in your case

Because you previously had absolute clock numbering, the child sheet still contains legacy signal naming such as:

- `CLK7`

and then Altium is appending the repeated sheet context:

- `CH4`

So you end up with:

- `CLK7_CH4`

That is actually useful, because it tells you the old naming is still present somewhere.

## Where to look

Check on the child sheet for any of these still attached to that wire:

- red **net label** `CLK7`
- yellow **port** `CLK7`
- off-sheet connector / harness label tied to `CLK7`
- hidden power-style or directive-driven naming
- sheet entry on the parent still called `CLK7`

## Fastest way to prove it

Click that wire or port and open **Properties**. Look for:

- **Net**
- **Name**
- **Compiled Name**

If compiled name says `CLK7_CH4`, then the source name is still `CLK7`.

## Another clue from your screenshot

Your component designators are things like:

- `J905_CLK7_CH4`

That suggests the component itself may have been **annotated while the net was still called `CLK7_CH4`**.

So even if you remove the net label now, the component designator text may still show the old naming until you re-annotate or update parameters.

That means there are really two things:

### 1. Current net naming
What the wire is called now.

### 2. Historical component naming
Text strings that were generated earlier from the old net name.

## What to do next

On that exact clock wire:

1. Click the wire.
2. Check whether there is still a **net label** on it called `CLK7`.
3. Check the attached **port** name.
4. Remove any old `CLK7` label.
5. Replace with the new local template name:
   - `CLK1` or `CLK2` or `CLK3` or `CLK4`

depending which clock it really is in the repeated channel.

## Important distinction

If this is the **4th channel’s first clock**, the child sheet should usually call it just:

- `CLK1`

and Altium will make it unique by channel.

It should **not** be called `CLK7` locally unless you are intentionally keeping global numbering.

## So the direct answer

That `7` is coming from an **old inherited net name** somewhere in the schematic connectivity for that signal — almost certainly a leftover `CLK7` label/port/sheet-entry — and Altium is then appending the repeated channel context afterward.

The next thing to do is inspect that exact wire’s properties and remove the legacy `CLK7` source naming.

[M23] ME (2026-03-09 03:52):
[image]
[image]
Struggling again.
[attached file: IMG_ACA13154-480C-4F53-9D80-EDF3B4D3A9CF.jpeg]
[attached file: IMG_8B9BF1D3-286B-4F4A-ABF0-91239C90F968.jpeg]

[M24] AI (2026-03-09 03:52):
Yes — I can see the problem. You’ve got the **repeat syntax the wrong way round now**.

You have:

- parent sheet symbol already repeated: `REPEAT(CH,1,7)`
- child ports showing: `REPEAT(CLK1,1,7)`, `REPEAT(CLK2,1,7)` etc

That is the bit that is fighting you.

## What is wrong

Inside the child sheet, `CLK1`, `CLK2`, `CLK3`, `CLK4` are already the **four distinct signals for one channel**.

They should **not** also be repeated `1,7`.

Why not:

- the **channel sheet** is what repeats 7 times
- the **clock ports** inside that sheet stay fixed as `CLK1..CLK4`

At the moment Altium is being told:

- repeat the sheet 7 times
- and also repeat each clock port 7 times

That is creating nested repetition you do not want.

## Correct setup

### Parent sheet symbol
Keep:
- `REPEAT(CH,1,7)`

### Parent sheet entries
Use plain entries:
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Not:
- `Repeat(CLK1,1,7)`
- `Repeat(CLK2,1,7)`

### Child sheet ports
Use plain ports:
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Not:
- `REPEAT(CLK1,1,7)`
- etc

## So the rule is

For your case:

- **repeat only the sheet**
- **do not repeat the individual clock ports**

## What to change right now

### On the parent sheet symbol
Change these four entries:

- `Repeat(CLK1,1,7)`
- `Repeat(CLK2,1,7)`
- `Repeat(CLK3,1,7)`
- `Repeat(CLK4,1,7)`

to just:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

### On `CH.SchDoc`
Change these ports:

- `REPEAT(CLK1,1,7)`
- `REPEAT(CLK2,1,7)`
- `REPEAT(CLK3,1,7)`
- `REPEAT(CLK4,1,7)`

to just:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

## What the final meaning becomes

Because the sheet is repeated as `CH1..CH7`, Altium will already interpret them as:

- CH1.CLK1
- CH1.CLK2
- CH1.CLK3
- CH1.CLK4
- CH2.CLK1
- CH2.CLK2
- etc

You do **not** have to force the `1,7` onto each port.

## Why you got tangled

You were mixing two different ideas:

1. repeated **sheet instances**
2. repeated **signal arrays**

You only need the first one here.

Your design is:

- 7 channels
- each channel has 4 fixed named clock lines

That is **not** the same as “one channel has 7 copies of CLK1”.

## Do this exact cleanup

1. In `CH.SchDoc`, rename every repeated port to plain:
   - `CLK1`
   - `CLK2`
   - `CLK3`
   - `CLK4`

2. On the parent repeated sheet symbol, rename the entries to plain:
   - `CLK1`
   - `CLK2`
   - `CLK3`
   - `CLK4`

3. Leave only the sheet itself as:
   - `REPEAT(CH,1,7)`

4. Compile again.

## One more thing

Your left-side signals like:

- `CB1_FAST_CLOCK_0_N`
- `CB1_FAST_CLOCK_0_P`
- etc

are top-level system names. That is fine.

But on the repeated sheet interface for the repeated block, keep the channel-facing ports simple and local:
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Then map those to your external names at the parent level.

So yes — the fix is: **remove all `REPEAT(...,1,7)` from the clock ports and sheet entries. Only the sheet should repeat.**

[M25] ME (2026-03-09 11:11):
[image]
Ok, rewind. I have a child sheet with 7 repeats. Each sheet has 4 clocks. I want 28 independent clocks. What’s do I do on this screen first 
[attached file: IMG_9A8839F0-21AE-4970-9DCC-9823B26D714F.jpeg]

[M26] AI (2026-03-09 11:11):
First on **this screen**, do **not** try to create 28 clocks here.

Do this:

## Step 1 on this screen
Keep the **sheet repeat only**:

- `Repeat(U_CH,1,7)`

That is correct.

## Step 2 on this screen
On the repeated sheet symbol, create **four normal sheet entries** for the four clocks:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Not:
- `Repeat(CLK1,1,7)`
- not `Repeat(CLK,1,4)`

Just plain entries:
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

## Why
Because this screen defines **one channel template**.

You are saying:

- repeat this channel 7 times
- each channel has 4 clock ports

That already gives you **28 independent compiled clocks** automatically through hierarchy:

- U_CH1.CLK1
- U_CH1.CLK2
- U_CH1.CLK3
- U_CH1.CLK4
- U_CH2.CLK1
- ...
- U_CH7.CLK4

So the **28** comes from:

- 7 repeated sheets
- × 4 fixed clock ports each

not by writing 28 names on this symbol.

## So on this exact screen
Your right-hand side should be:

- `SR_D_OUT`
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

And the child sheet `CH.SchDoc` must also have ports named exactly:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

## Important point
Those left-side names like:

- `FAST_CLOCK_1_1_N`
- `FAST_CLOCK_1_1_P`
- etc

look like top-level external names. That is fine if they are genuinely separate interfaces.

But the four per-channel outputs on the repeated side should stay simple:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

## So the first action here
Rename/check the four right-side entries so they are just:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

and leave the sheet itself as:

- `Repeat(U_CH,1,7)`

That is the correct starting point.

After that, the next step is wiring those four ports on the parent sheet to whatever top-level 28-clock naming you want.

[M27] ME (2026-03-09 11:13):
[image]
[image]
[attached file: 4704F0CE-206C-437A-B449-5803670379FA.jpeg]
[attached file: IMG_F24E1AC2-E898-4431-8F5A-CC39555B15D2.jpeg]

[M28] AI (2026-03-09 11:13):
Yes — **this is now the right structure**.

You’ve now got:

- repeated sheet symbol: `Repeat(U_CH,1,7)`
- child-sheet ports: `CLK1`, `CLK2`, `CLK3`, `CLK4`
- local wires in child sheet named `CLK1`, `CLK2`

That part is correct.

## What `Cover[4B]` means
That `Cover[4B]` text is just **compiled hierarchical context**.  
It is Altium showing the path of that repeated instance, not changing the actual port name.

So:

- actual port/net name = `CLK1`
- compiled instance context = `Cover[4B]`

Nothing wrong there.

## What this gives you
This already creates **28 independent hierarchical clocks**:

- `U_CH1.CLK1`
- `U_CH1.CLK2`
- `U_CH1.CLK3`
- `U_CH1.CLK4`
- `U_CH2.CLK1`
- ...
- `U_CH7.CLK4`

So the repeated hierarchy is doing its job.

## Next thing to do
Now go to the **parent sheet above this repeated block** and decide how you want to expose or connect those 28 clocks.

Two sensible options:

### Option A — keep hierarchy, simplest
Just wire each repeated channel instance to whatever drives that channel.  
No need to flatten into `CLK1..CLK28` unless you really want to.

### Option B — explicit top-level unique names
If you want visible board-level names, map them at the parent/top level as:

- `CH1_CLK1`
- `CH1_CLK2`
- `CH1_CLK3`
- `CH1_CLK4`
- ...
- `CH7_CLK4`

That is much clearer than flat `CLK1..CLK28`.

## One thing to avoid
Do **not** rename the child-sheet ports themselves to global names.  
Keep the child sheet as the reusable template:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

and only create global uniqueness at the parent/top level if needed.

## So where you are now
You are past the hard bit.  
This screen is set up properly.

The next step is simply deciding:

- do you want to leave the 28 clocks as **hierarchical compiled names**, or
- do you want to **map them to explicit top-level names** for readability or FPGA pin mapping?

If you show the parent sheet wiring above this repeated block, I can tell you exactly how to wire the 28 clocks cleanly from here.

[M29] ME (2026-03-09 11:15):
Top-level readability 

[M30] AI (2026-03-09 11:15):
Then the clean approach is:

## Keep the child sheet generic
Leave `CH.SchDoc` as:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

and keep the sheet repeat:

- `Repeat(U_CH,1,7)`

Do **not** rename anything in the child to `CLK1..CLK28`.

## Make readability happen at the parent/top level
At the sheet above, name the nets that connect to each repeated channel entry as explicit unique names, for example:

- `CH1_CLK1`
- `CH1_CLK2`
- `CH1_CLK3`
- `CH1_CLK4`

- `CH2_CLK1`
- `CH2_CLK2`
- `CH2_CLK3`
- `CH2_CLK4`

...
- `CH7_CLK4`

That is the nicest readable convention.

## Why this is best
You get both:

- **reusable child template**
- **clear top-level board naming**

So the hierarchy stays clean, but your top sheet is readable.

## What to do practically
On the parent sheet, for each of the seven channel instances, wire the four entries:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

to top-level nets labelled:

- `CHx_CLK1`
- `CHx_CLK2`
- `CHx_CLK3`
- `CHx_CLK4`

where `x` is 1 to 7.

## Example
For channel 1 instance:

- `U_CH1.CLK1` wire label at parent = `CH1_CLK1`
- `U_CH1.CLK2` = `CH1_CLK2`
- `U_CH1.CLK3` = `CH1_CLK3`
- `U_CH1.CLK4` = `CH1_CLK4`

For channel 2:

- `CH2_CLK1`
- `CH2_CLK2`
- `CH2_CLK3`
- `CH2_CLK4`

## Best naming format
I’d strongly recommend:

- `CH1_CLK1`
- `CH1_CLK2`
- …
- `CH7_CLK4`

rather than flat:
- `CLK1` to `CLK28`

Because with `CHx_CLKy`, you can instantly see channel grouping.

## Important
If your current left-side names like:

- `FAST_CLOCK_1_1_N`
- `FAST_CLOCK_1_1_P`

are the actual board-level interface names, you can keep those too. But for the single-ended derived clocks, map them consistently at top level.

For example:

- `FAST_CLOCK_1_1_P/N` feeds channel 1 clock path
- resulting readable net = `CH1_CLK1`

## So your next move
Do not change the child sheet anymore.

Instead, on the top-level parent sheet:
- place net labels on the wires coming from each repeated sheet instance
- label them `CH1_CLK1` … `CH7_CLK4`

That is the correct place to get top-level readability.

[M31] ME (2026-03-09 11:16):
[image]
Like that?
[attached file: IMG_55EF9556-0AF8-492B-9D96-1B85C5B7F3AF.jpeg]

[M32] AI (2026-03-09 11:16):
Not like that on the **repeated sheet symbol**.

Those entries should still be the **generic child-sheet port names**:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

What you’ve done there is hard-code instance names onto the repeated symbol, and that breaks the template idea. Also I can see it’s inconsistent already:

- `CH1_CLK1`
- `CH1_CLK2`
- `CH1_CLK3`
- `CH4_CLK4`

That is exactly the sort of thing to avoid.

## On this green repeated block
Use only:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

## Where `CH1_CLK1` etc should go
They should go on the **wires outside this block**, on the parent/top-level connectivity, not as the sheet-entry names on the repeated symbol.

So the pattern is:

### Repeated sheet symbol entries
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

### Net labels on the external wires connected to each repeated instance
- `CH1_CLK1`
- `CH1_CLK2`
- `CH1_CLK3`
- `CH1_CLK4`
- `CH2_CLK1`
- ...
- `CH7_CLK4`

## Rule
- **port/sheet-entry names** = generic template names
- **wire net labels outside the block** = readable top-level unique names

## So fix this screen by changing back to
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Then, on the schematic sheet where these wires actually fan out, label the wires themselves with `CHx_CLKy`.

That is the correct way.

[M33] ME (2026-03-09 11:17):
[image]
[attached file: IMG_9B7DCCD4-E7CE-4A98-AC99-85F21EBB6243.jpeg]

[M34] AI (2026-03-09 11:17):
Still **no** on the green block.

Those are **sheet entries**, so they must stay as the **child port names**:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Not `CH1_CLK1` etc.

## Why
That green symbol is the **template being repeated 7 times**.  
If you write `CH1_CLK1` on it, you are baking channel 1 naming into every repeated instance.

So all four of those need changing back to:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

## Where `CH1_CLK1` belongs
On the **wire outside the block**, after the sheet entry.

So visually it should be:

`[green block entry CLK1]──wire──net label CH1_CLK1`

not:

`[green block entry CH1_CLK1]`

## Simple rule
- **On the block:** generic names
- **On the connecting wires:** readable unique names

## Do this now
On that screen, rename:

- `CH1_CLK1` → `CLK1`
- `CH1_CLK2` → `CLK2`
- `CH1_CLK3` → `CLK3`
- `CH1_CLK4` → `CLK4`

Then show me the sheet **one level above**, where those wires fan out. That is where the `CH1_CLK1` labels should go.

[M35] ME (2026-03-09 11:19):
[image]
[image]
[attached file: IMG_13ECFFBF-803C-4F2C-AF3D-DC898103DB7B.jpeg]
[attached file: IMG_15E6A17E-6B30-4C4B-8065-6693F16695F5.jpeg]

[M36] AI (2026-03-09 11:19):
Yes — **that screen is now correct** for the repeated block.

You now have:

- `Repeat(U_CH,1,7)`
- sheet entries on the right:
  - `CLK1`
  - `CLK2`
  - `CLK3`
  - `CLK4`

That is exactly what you want **on this symbol**.

## What this means
This block now represents:

- one child sheet template
- repeated 7 times
- each repeated instance has 4 clock outputs

So Altium will create 28 independent hierarchical signals automatically.

## Next step
The readable names like:

- `CH1_CLK1`
- `CH1_CLK2`
- …
- `CH7_CLK4`

should **not** go on this green symbol.

They go on the **sheet above this one**, on the wires connected to these four entries for each repeated instance.

## So from here
Leave this block alone now.

The next thing to do is go **up one level** and wire/label the outputs from each repeated instance.

That parent sheet will be where you make it readable.

## One note
Your left-side names such as:

- `FAST_CLOCK_1_N`
- `FAST_CLOCK_1_P`
- etc

are fine if those are the actual interface names for one channel template.

But the right-side `CLK1..CLK4` is now set correctly.

## Bottom line
**Yes — this is the correct setup for the repeated child-sheet symbol.**

The next place to work is the parent sheet wiring, not this block anymore.

[M37] ME (2026-03-09 11:20):
[image]
That’s on the top sheet. Do I need another layer 
[attached file: IMG_340B808C-3259-471D-8134-371D7A301EC7.jpeg]

[M38] AI (2026-03-09 11:20):
No — you do **not** need another layer just for this.

From your project tree, `Cover.SchDoc` is already your top sheet, so the readable names should be created **there**, on the wires connected to the repeated `CH.SchDoc` block.

## So the hierarchy should be

- `Cover.SchDoc` = top level
- `CH.SchDoc` = repeated child sheet
- no extra sheet needed just to name clocks

## What to do on `Cover.SchDoc`

On `Cover.SchDoc`, place your repeated `CH.SchDoc` symbol with:

- `Repeat(U_CH,1,7)`

and the four generic entries:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Then the readable naming is done by the **wires/net labels attached to those entries on Cover**.

So on Cover, you would have nets labelled like:

- `CH1_CLK1`
- `CH1_CLK2`
- `CH1_CLK3`
- `CH1_CLK4`
- `CH2_CLK1`
- ...
- `CH7_CLK4`

## But there is one practical catch

Because the block itself is repeated, you usually do **not** manually get seven separate visible sheet symbols on the page. Altium compiles those instances hierarchically.

So for readability, you have two choices:

### Best engineering choice
Accept the hierarchical names as the real uniqueness:
- `U_CH1.CLK1`
- `U_CH2.CLK1`
- etc

and use compiled navigation/documentation for clarity.

### Best visual readability choice
Do **not** repeat the sheet symbol.  
Instead, place **7 separate sheet symbols manually** on `Cover.SchDoc`:

- `U_CH1`
- `U_CH2`
- `U_CH3`
- ...
- `U_CH7`

all pointing to the same `CH.SchDoc`, with entries:
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Then you can visibly label the wires:

- `CH1_CLK1`
- `CH1_CLK2`
- ...
- `CH7_CLK4`

This gives maximum top-level readability.

## So direct answer

You do **not** need another layer.  
But if your goal is **human-readable top-sheet visibility**, the better move may be:

- stop using `Repeat(U_CH,1,7)` on the top sheet
- place 7 individual sheet symbols referencing `CH.SchDoc`

That is often easier to read, debug, and review than a repeated symbol when you care about explicit top-level naming.

## Decision rule

If you want:
- **compact elegant hierarchy** → keep repeated sheet
- **obvious visual top-level readability** → place 7 manual instances on Cover

For your stated goal, I would lean toward **7 manual sheet symbols on Cover**, all using the same child sheet. That gives you the cleanest readable `CH1_CLK1` to `CH7_CLK4` naming without fighting the hierarchy.

[M39] ME (2026-03-09 11:23):
[image]
[image]
I’ve added 2 in for now 
[attached file: IMG_97A53864-6859-4BCC-891F-0145FE35B5F8.jpeg]
[attached file: IMG_E207C5C2-7E00-41FD-BF86-7F0796EE0F71.jpeg]

[M40] AI (2026-03-09 11:23):
Yes — **this is the right direction**.

You’ve now switched to the readable top-level approach:

- `U_CH1` = first instance of `CH.SchDoc`
- `U_CH2` = second instance of `CH.SchDoc`

That is exactly how to get clear top-level naming without fighting multichannel repeat syntax.

## What to do next

For each block instance, keep the **sheet entries** generic:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

Do **not** rename those entries themselves.

## Then add readable names on the wires
On the wires connected to `U_CH1`, place net labels:

- `CH1_CLK1`
- `CH1_CLK2`
- `CH1_CLK3`
- `CH1_CLK4`

On the wires connected to `U_CH2`, place:

- `CH2_CLK1`
- `CH2_CLK2`
- `CH2_CLK3`
- `CH2_CLK4`

and so on for the rest.

## So the pattern is

### Block title/designator
- `U_CH1`
- `U_CH2`
- `U_CH3`
- ...

### Sheet entries on each block
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

### Net labels on external wires
- `CH1_CLK1`
- `CH1_CLK2`
- ...
- `CH7_CLK4`

## Important
Do not change the child sheet `CH.SchDoc`.  
Keep that as the reusable template with:

- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

## Practical next steps
1. Copy this block until you have all 7:
   - `U_CH1` to `U_CH7`

2. Give each one a unique designator:
   - `U_CH1`, `U_CH2`, etc

3. On the outputs of each one, wire and label:
   - `CHx_CLK1`
   - `CHx_CLK2`
   - `CHx_CLK3`
   - `CHx_CLK4`

4. Compile and check there are no duplicate sheet designators.

## Tiny naming recommendation
Because these are sheet symbols, I’d personally use something like:

- `CH1`
- `CH2`
- `CH3`

rather than `U_CH1`, `U_CH2`

But if your naming style is already `U_CH1`, that is fine — just keep it consistent.

## Bottom line
Yes — **adding 2 manually like this is the correct approach** for top-level readability.

The next move is simply to wire them and label the wires, not the sheet entries.

[M41] ME (2026-03-09 11:27):
[image]
Like that?
[attached file: IMG_805A2AA6-DFCF-4E52-9C19-76E689BA1273.jpeg]

[M42] AI (2026-03-09 11:27):
Yes — **that is the right idea**.

You’ve now got:

- separate top-level child-sheet instances: `U_CH1`, `U_CH2`
- generic outputs on each block: `CLK1..CLK4`
- external readable labels grouped per channel

That is the structure you wanted.

## One improvement
I would rename those yellow labels from:

- `CLK 1 1`
- `CLK 1 2`
- `CLK 1 3`
- `CLK 1 4`

to a cleaner net naming style:

- `CH1_CLK1`
- `CH1_CLK2`
- `CH1_CLK3`
- `CH1_CLK4`

and for the second block:

- `CH2_CLK1`
- `CH2_CLK2`
- `CH2_CLK3`
- `CH2_CLK4`

That will read much better everywhere:
- compiled nets
- PCB
- reports
- FPGA mapping
- debug

## So yes
**Structurally: correct.**  
**Naming style: just tidy it to `CHx_CLKy`.**

## Also
Those yellow items look like a **harness/port block** rather than simple net labels. That is fine if that is what you intend, but the names still want to be:

- `CH1_CLK1` … `CH1_CLK4`
- `CH2_CLK1` … `CH2_CLK4`

## Next move
Copy this through to all 7 channels, then compile and check for duplicate names or unintended shorts.

[M43] ME (2026-03-09 11:31):
[image]
But when I’ve added those two sheets it’s created two more circuit blocks 
[attached file: IMG_1CB81B10-D3B2-4430-B445-CECEFCD2BACF.jpeg]

[M44] AI (2026-03-09 11:31):
Yes — that makes sense. What you’re seeing is **not two extra different documents** being created. Altium has created **compiled sheet-channel views** for those new top-level sheet symbols.

Those tabs like:

- `CH2`
- `CH3`
- …
- `CH7`
- `U_CH1`
- `U_CH2`

are Altium’s **compiled/instantiated channel tabs** for `CH.SchDoc`.

## Why it happened

Previously you had the repeated sheet, so Altium compiled channel instances like:

- `CH2`
- `CH3`
- etc

Now you have also placed **manual instances**:

- `U_CH1`
- `U_CH2`

So Altium is showing those as additional compiled sheet contexts too.

It is not duplicating the underlying source file physically.  
It is showing different **instantiations** of the same child schematic.

## What this means in practice

Right now you likely have **both** of these in the design:

- the old repeated version of `CH.SchDoc`
- the new manually placed `U_CH1`, `U_CH2`

So Altium is correctly compiling both sets.

## What you need to do

You must choose **one method only**:

### Option A
Use the old repeated block:
- `Repeat(U_CH,1,7)`

### Option B
Use manual readable instances:
- `U_CH1`
- `U_CH2`
- …
- `U_CH7`

For your readability goal, you want **Option B**.

## So the fix is

Delete or remove from the top sheet the old repeated sheet symbol:

- `Repeat(U_CH,1,7)`

and keep only the manually placed instances:

- `U_CH1`
- `U_CH2`
- …
- `U_CH7`

Then recompile.

After that, those old `CH2…CH7` compiled tabs should disappear, leaving only your manual instances.

## In plain terms

You currently have:
- one multichannel repeated block
- plus two manual blocks

So Altium sees **9 instantiated channels**.

That is why you’re getting extra circuit blocks/tabs.

## What to do next
On `Cover.SchDoc`, find and delete the original repeated `CH.SchDoc` block, then keep building out the seven manual sheet symbols only.

[M45] ME (2026-03-09 11:33):
But then it won’t be repeat and linked for design changes?

[M46] AI (2026-03-09 11:33):
It **will still be linked for design changes** as long as all 7 sheet symbols point to the same `CH.SchDoc`.

That is the key distinction:

## Same child document, multiple sheet symbols
If you place:

- `U_CH1` → `CH.SchDoc`
- `U_CH2` → `CH.SchDoc`
- ...
- `U_CH7` → `CH.SchDoc`

then all seven are still using the **same source schematic**.

So if you edit `CH.SchDoc`, all seven instances update, because they are all references to that one child sheet.

## What you lose
What you lose is the **automatic repeat syntax**:

- `Repeat(U_CH,1,7)`

## What you keep
What you keep is the actual reuse/linking:

- one child design
- instantiated multiple times
- edits to `CH.SchDoc` propagate to all instances

So from a design-maintenance point of view, it is still linked.

## The difference is really this

### Repeated sheet symbol
- compact
- elegant
- less readable at top level

### Multiple manual sheet symbols all referencing same child sheet
- still linked to one source
- much more readable
- slightly more manual to place and wire

## Important caveat
This is true for **schematic changes** to the common child sheet.

If later you want Altium’s automated multichannel placement/replication conveniences on PCB, the formal repeated-sheet method can be more helpful.

But for the schematic itself, multiple instances of the same child sheet are still reused and linked.

## So the honest answer
Yes, it stays linked for design edits to `CH.SchDoc`.  
No, it is not the same as using formal `Repeat(...)` multichannel syntax.

## Best practical guidance for your case
Because you care about **top-level readability**, I’d do this:

- use 7 manual sheet symbols, all pointing to `CH.SchDoc`
- keep the child sheet identical and generic
- use readable top-level names like `CH1_CLK1`

That gives you:
- readable schematic
- one child source to maintain

The tradeoff is just that it is less “automatic multichannel syntax” and more “multiple linked instances.”

If you want, I can give you the exact decision rule for whether your PCB replication workflow later means you should stick with `Repeat(...)` instead.

[M47] ME (2026-03-09 11:40):
[image]
[image]
[image]
[image]
[attached file: IMG_95FCDD7E-6BA6-4E9B-AA04-80BFB118FFC1.jpeg]
[attached file: IMG_5F4AEC9F-61A2-49BC-B5BA-540E84683D44.jpeg]
[attached file: IMG_38BC3C96-53A2-4F45-9616-C173FFCE512D.jpeg]
[attached file: IMG_6FE9856D-F5A0-4634-A4BD-3CFB06E63580.jpeg]

[M48] AI (2026-03-09 11:40):
Yes — you’re basically there.

The only thing I’d change now is the **naming style**.

## What looks right
- `CH1`, `CH2` tabs at the bottom: good — those are your instantiated child sheets.
- Child sheet ports `CLK1..CLK4`: good.
- Top-level channel grouping on `CCD38x_Interface`: good.

## What I would fix
Change labels like:

- `CLK 1 2`
- `CLK 1 3`
- `CLK 1 4`

to:

- `CH1_CLK2`
- `CH1_CLK3`
- `CH1_CLK4`

And similarly for channel 2:

- `CH2_CLK1`
- `CH2_CLK2`
- `CH2_CLK3`
- `CH2_CLK4`

Do the same for all channels.

## Why
`CLK 1 2` is hard to read and easy to confuse:
- is it clock 12?
- channel 1 clock 2?
- a bus member?

`CH1_CLK2` is unambiguous everywhere:
- schematic
- PCB net names
- reports
- FPGA mapping
- test docs

## So your structure should be

### In `CH.SchDoc`
Keep:
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

### On `Cover.SchDoc`
Each sheet symbol:
- `CH1`
- `CH2`
- `CH3`
- etc

### On the top-level interface sheet / external labels
Use:
- `CH1_CLK1`
- `CH1_CLK2`
- `CH1_CLK3`
- `CH1_CLK4`

Then:
- `CH2_CLK1`
- `CH2_CLK2`
- etc

## Looking at your last image
For **CHANNEL 1**, I’d rename:

- `CLK1` → `CH1_CLK1`
- `CLK 1 2` → `CH1_CLK2`
- `CLK 1 3` → `CH1_CLK3`
- `CLK 1 4` → `CH1_CLK4`

That would be the clean finished version.

## One extra tidy-up
I’d also prefer the sheet designators to be simply:

- `CH1`
- `CH2`
- `CH3`

rather than `U_CH1`, `U_CH2`

because these are channel blocks, not really components. But that is optional.

So: **architecture is now fine; just normalise the names to `CHx_CLKy` and carry that through consistently.**

[M49] ME (2026-03-09 11:41):
Naming is a luxury right now!! It’s still not working can’t you see

[M50] AI (2026-03-09 11:41):
Yes — I can see it’s **still not actually connected through properly**. The naming is not the real problem.

From your screenshots, the clue is this:

- on `Cover.SchDoc` you have sheet symbols `CH1`, `CH2`
- on the child sheet tabs you have `CH1`, `CH2`
- but on the interface sheet you are still seeing odd isolated labels and not a clean propagated net structure

So the issue is likely one of these three things:

## 1. The top sheet symbol entries are not matching the child sheet ports exactly
They must match **character for character**.

So for one channel block:

### On `Cover.SchDoc` sheet symbol
must be exactly:
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

### On `CH.SchDoc` ports
must be exactly:
- `CLK1`
- `CLK2`
- `CLK3`
- `CLK4`

No spaces, no hidden repeats, no old names.

## 2. You are using harness entries / ports / net labels inconsistently
From the yellow objects, some look like ports or sheet entries, and some may be net labels/harness entries.

For now, strip it back brutally.

### Test with one signal only
Do this with **just CH1 CLK1**:

On `Cover.SchDoc`:
- one sheet symbol pointing to `CH.SchDoc`
- designator `CH1`
- one sheet entry only: `CLK1`

On `CH.SchDoc`:
- one port only: `CLK1`
- connected directly to one obvious wire in the schematic

Then compile.

If that one does not propagate, the hierarchy is wrong.  
If that one works, add `CLK2`, then `CLK3`, then `CLK4`.

## 3. You may be looking at compiled sheet tabs, not actual top-level wire naming
The tabs `CH1`, `CH2` at the bottom are just instance views. They do not guarantee the nets are exposed the way you want on the parent sheet.

So the real test is:

### In `Cover.SchDoc`
place a **net label** directly on the wire coming off the `CLK1` sheet entry of `CH1`.

Call it something simple like:
- `TEST_CH1_CLK1`

Then compile and see whether that exact net name appears on the corresponding wire in the `CH1` compiled sheet view.

If it does, the hierarchy link works.

If it does not, the problem is connectivity between:
- sheet entry on parent
- matching port in child

---

# What I think is most likely wrong

You have too many layers of abstraction active at once:

- sheet symbols
- ports
- net labels
- possibly harness-style grouped labels
- interface sheet remapping

That makes it hard to see where the break is.

So the fastest recovery is:

## Minimal debug procedure

### Step A
Temporarily ignore all 4 clocks except one.

### Step B
On `CH.SchDoc`:
- delete or ignore everything except one port named `CLK1`
- connect it to one visible wire

### Step C
On `Cover.SchDoc`:
- one sheet symbol only: `CH1`
- one matching sheet entry only: `CLK1`
- one wire from that entry
- one plain net label on that wire: `TEST_CH1_CLK1`

### Step D
Compile

### Expected result
In compiled `CH1` view, that signal should resolve through the hierarchy.

If it fails, then the hierarchy setup is still wrong.  
If it works, your architecture is fine and the problem is just the extra wrapping around it.

---

# Very likely specific fault from your screenshots

On your interface sheet, I can see labels like:
- `CLK1`
- `CLK_H1`
- `CLK_L1`
- `Ødc`
- `SØ1`
- `SØ2`

That suggests you are trying to map one child output into several differently named functional nets.

That is fine, but only **after** the basic sheet-entry-to-port path works.

At the moment, I suspect one of these:
- the `CLK1` label is sitting on a disconnected stub
- the label object is not on the same net segment as the sheet entry wire
- one of the objects is a port where you needed a net label
- or the sheet entry/port names do not exactly match

---

# What I want you to do next

Do not keep iterating the whole structure yet.

Take screenshots of only these two things:

1. `Cover.SchDoc` with **one** block `CH1`, showing the sheet entry `CLK1` and the wire/net label coming off it.
2. `CH.SchDoc` showing the `CLK1` port and the wire it is attached to.

That will show exactly where the hierarchy is breaking.

The short answer is: **yes, I can see it’s still not working — the problem is not naming now, it’s that the parent sheet entry and child port path has not been reduced to one known-good connection yet.**

[M51] ME (2026-03-09 11:43):
[image]
I think it’s something to do with this 
[attached file: IMG_28F1F702-9287-4799-96BC-D0858213EBE1.jpeg]

[M52] AI (2026-03-09 11:43):
Yes — that **very likely is the issue**.

For what you are doing, the project should be using **Hierarchical**, not Flat/Global confusion, and the option set needs to match how you’ve built the sheets.

## What to set

Use:

- **Net Identifier Scope** = **Strict Hierarchical**
  or plain **Hierarchical**

For your structure, I would start with:

- **Strict Hierarchical**

because you now have:
- top sheet with sheet symbols
- child sheet with matching ports
- no need for accidental global name leakage

## And keep these enabled
- **Allow Ports to Name Nets** = on
- **Allow Sheet Entries to Name Nets** = on

## What Strict Hierarchical does
It forces connectivity through:

- parent **sheet entry**
- matching child **port**

That is exactly what you want.

It stops random/global same-name nets elsewhere from shorting together unexpectedly.

## What can go wrong with other modes
If it is on the wrong mode, Altium may:
- treat labels too globally
- ignore intended hierarchy behaviour
- create weird compiled naming that looks disconnected
- let same names join when you do not want them to

That fits what you’ve been seeing.

## So do this now

1. Set **Net Identifier Scope** to **Strict Hierarchical**
2. Leave:
   - **Allow Ports to Name Nets** = checked
   - **Allow Sheet Entries to Name Nets** = checked
3. Click **OK**
4. Recompile the project fully

## Then test one path
After compile, test just one signal:

- `Cover.SchDoc` → `CH1` sheet symbol → `CLK1` entry
- `CH.SchDoc` → `CLK1` port

If that works, the rest will likely fall into place.

## One extra thing to avoid
Do not rely on net labels alone to cross hierarchy now.  
With **Strict Hierarchical**, the intended path is:

- wire on parent
- sheet entry
- matching child port
- wire on child

That is good discipline here.

## My recommendation
Set it to **Strict Hierarchical** first.  
If something still behaves oddly, try **Hierarchical** next, but **Strict Hierarchical** is the correct clean starting point for this design.

[M53] ME (2026-03-09 11:46):
It makes me think that a lot of failed attempts earlier were due to this 

[M54] AI (2026-03-09 11:46):
Yes — very likely.

A wrong **Net Identifier Scope** can make a hierarchy setup look broken even when the symbols and ports are mostly right.

That would explain a lot of what you were seeing earlier:

- names appearing to “stick” strangely
- signals not resolving the way expected
- compiled views looking inconsistent
- seeming clashes between local and higher-level names
- confusion over whether ports, sheet entries, or labels were in control

With multichannel and repeated child sheets, that setting matters a lot more than in a flat design.

## In your case
You were building a genuinely hierarchical design:

- top sheet
- child sheet
- sheet entries
- matching ports
- repeated/instanced channels

So if the project options were not aligned to **hierarchical resolution**, Altium could absolutely have been undermining the whole setup.

## Honest read
Not every failed attempt was only because of that setting.  
Some of the earlier confusion was also from mixing:

- repeated sheet syntax
- manual instances
- repeated ports
- top-level readable naming
- generic child naming

But yes — a wrong hierarchy/net-scope setting could have made all of that **much harder than it should have been**.

## Practical takeaway
Now that you’ve found this, I’d do three things:

1. Set **Strict Hierarchical**
2. Recompile from clean
3. Re-test one simple signal path first before rebuilding confidence in the whole structure

That should give you a much truer picture of whether the actual sheet-entry/port setup is now sound.

So yes — your instinct is probably right. That option may have been a major part of the pain.

[M55] ME (2026-03-09 11:51):
Right, let’s go again then 

[M56] AI (2026-03-09 11:51):
Good. Strip it right back and prove one path first.

## Set the project first
In Project Options:

- **Net Identifier Scope** = **Strict Hierarchical**
- **Allow Ports to Name Nets** = **ON**
- **Allow Sheet Entries to Name Nets** = **ON**

Then **OK** and **Compile**.

## Now rebuild the hierarchy in the simplest possible way

### On `CH.SchDoc`
Only worry about one signal first.

Have:
- one **Port** named `CLK1`

Make sure that port is wired directly to the actual child-sheet net you want to expose.

Do not use:
- repeat syntax
- extra net labels with different names
- harness tricks

For the test, just:
- wire
- port `CLK1`

### On `Cover.SchDoc`
Place one sheet symbol for `CH.SchDoc`.

Set:
- designator: `CH1`

Add only one sheet entry:
- `CLK1`

Then draw one wire from that sheet entry and put a plain **net label** on that wire, for example:
- `TEST_CH1_CLK1`

## Compile and check
If that works, then the hierarchy is good.

Then add:

- `CLK2`
- `CLK3`
- `CLK4`

one by one, same method.

## After that
Add `CH2` as a second manual instance of the same `CH.SchDoc`.

Then:
- `CH2` sheet symbol
- sheet entry `CLK1`
- wire label `TEST_CH2_CLK1`

Compile again.

## Rules for this pass
Do not use:
- `Repeat(...)`
- `CLK 1 1` style labels
- renamed sheet entries like `CH1_CLK1`
- extra abstraction layers

For now the logic is:

- child port = `CLK1`
- parent sheet entry = `CLK1`
- parent wire label = `TEST_CH1_CLK1`

## When that works
Then we rename the top-level labels properly to:
- `CH1_CLK1`
- `CH1_CLK2`
- etc

Start with just `CLK1` on `CH1` and send me those two screenshots:
- `Cover.SchDoc` showing `CH1` and its `CLK1` wire
- `CH.SchDoc` showing the `CLK1` port and attached wire

[M57] ME (2026-03-09 11:56):
[image]
[image]
[attached file: IMG_CDAC4295-3201-40C5-9FC2-9DA568A8A31D.jpeg]
[attached file: IMG_06DCAA6B-312A-4414-8B24-0881ECE32545.jpeg]

[M58] AI (2026-03-09 11:56):
Yes — I can see the break now.

## The problem is on the top sheet
In your first screenshot, the wire coming off the sheet entry `CLK1` goes to a **Port object still named `Port`**.

That is wrong for this test.

So right now you effectively have:

- sheet entry = `CLK1`
- wire connected to a **port called `Port`**

With your project settings, that can easily rename or confuse the net.

## The child sheet actually looks okay
Your second screenshot shows:

- child port `CLK1`
- connected to the intended wire

So the child side is not the main issue now.

## Fix this exactly
On `Cover.SchDoc`:

### Option 1 — best for this test
Delete that yellow `Port` object completely.

Then place a **Net Label** on the wire and call it:

- `TEST_CH1_CLK1`

Not a port. A **net label**.

So the top sheet should be:

- sheet symbol entry `CLK1`
- short wire
- **net label** `TEST_CH1_CLK1`

## Why
A **Port** is for off-sheet hierarchical connection.  
Here, coming straight off a child sheet symbol entry, you just want to **name the wire**.

Right now your `Port` object is introducing another naming/control point.

## Also
For this one-signal debug, do not use:

- `Repeat(CH,1,7)`

Strip it back to a single manual instance:

- sheet symbol for `CH.SchDoc`
- designator `CH1`
- one sheet entry `CLK1`

That removes another source of confusion.

## So the clean one-signal test should be

### On `Cover.SchDoc`
- one sheet symbol: `CH1`
- linked to `CH.SchDoc`
- one sheet entry: `CLK1`
- one wire from it
- one **net label** on that wire: `TEST_CH1_CLK1`

### On `CH.SchDoc`
- one port: `CLK1`
- directly wired to the actual child net

## What I think is happening now
That yellow `Port` named `Port` is likely overriding or muddying the net naming on the top sheet.

So yes — this screenshot is finally showing a very concrete fault.

## Do this next
Remove the top-sheet `Port` object, replace it with a **net label**, compile, and then check whether the child compiled view shows the path cleanly.

[M59] ME (2026-03-09 11:57):
[image]
Was an old photos  
[attached file: IMG_53C35FE0-1C5A-4CF4-B8E2-F958A1B16BEC.jpeg]

[M60] AI (2026-03-09 11:58):
Got it — that changes things.

So that screenshot with:

- `Repeat(CH,1,7)`
- `CLK1`
- `CLK 1 1`

was **not the current state**, so we can ignore it.

That means the real issue is in the **current manual-instance setup**, not that old repeated-block picture.

## So let’s reset the target
We are now only interested in the current arrangement:

- `Cover.SchDoc`
- manual sheet symbols like `CH1`, `CH2`
- `CH.SchDoc` child ports like `CLK1`, `CLK2`, etc
- **Strict Hierarchical**

## One thing to confirm next
On the **current** `Cover.SchDoc`, are you now using:

- separate sheet symbols `CH1`, `CH2`, etc

or are you still using:
- one `Repeat(CH,1,7)` block?

Please answer with just one of these:
- **manual CH1/CH2 blocks**
- **repeat block**

[M61] ME (2026-03-09 11:58):
Repeat

[M62] AI (2026-03-09 11:58):
Good — then keep the **repeat block**. Do **not** switch to manual CH1/CH2 blocks.

Next step: on the top sheet, the wire coming off `CLK1` should have a **net label**, not a port.

So on `Cover.SchDoc`, for just this one test signal:

- keep `Repeat(CH,1,7)`
- keep sheet entry `CLK1`
- delete the yellow object if it is a **Port**
- place a **Net Label** on that wire instead, named something simple like `TEST_CLK1`

Can you check that yellow object’s type first: is it a **Port** or a **Net Label**?

[M63] ME (2026-03-09 12:00):
[image]
Now a net label 
[attached file: IMG_C2A1522E-FBA1-45C6-9E15-4112413DCC89.jpeg]

[M64] AI (2026-03-09 12:00):
Good — that part is now correct.

You have:

- sheet entry: `CLK1`
- wire
- **net label** on the wire

That is the right object type.

## Next single check
Now make the net label something very plain and unambiguous:

- `TEST_CH1_CLK1`

instead of:
- `CLK 1 1`

Because spaces can muddy things.

Then **compile** and check whether the corresponding child-sheet signal resolves through.

So the one step now is:

**rename that net label to `TEST_CH1_CLK1` and recompile.**

[M65] ME (2026-03-09 12:01):
It’s underscores, and the naming isn’t the problem 

[M66] AI (2026-03-09 12:01):
Fair — then the object type was the important bit, not the label text.

So the top sheet now has the right pattern:

- sheet entry `CLK1`
- wire
- net label

That means the next likely issue is **the sheet-entry/port hierarchy itself**, not the label.

Check this one thing only:

On `CH.SchDoc`, is the child object a **Port** named exactly `CLK1`, or is it a **Net Label** named `CLK1`?

[M67] ME (2026-03-09 12:01):
Port 

[M68] AI (2026-03-09 12:01):
Good. That’s the right object in the child.

So you now have the correct hierarchy objects:

- parent sheet symbol entry = `CLK1`
- child sheet port = `CLK1`
- parent wire has a net label

That means the remaining problem is very likely one of these two:

## 1. `Repeat(CH,1,7)` is still complicating the test
For a one-signal proof, multichannel repeat is still adding another variable.

## 2. The parent net label is **not supposed to propagate into the child** the way you’re expecting
With hierarchical design, the child net is named by the child port/path, not by “pushing down” the parent wire label as a flat rename.

So the real test is not “does the child wire become `CLK_1_1`”.  
The real test is “does the parent sheet entry connect to the child port electrically”.

## One question to pin it down
When you click that `CLK1` wire **inside `CH.SchDoc`**, what compiled text do you see next to it, if any?

Is it something like:
- `CLK1 Cover[...]`
or just
- `CLK1`
or
- nothing extra?

[M69] ME (2026-03-09 13:51):
[image]
There a neatbwaybtomjoin nets from one name to another more meaningful one 
[attached file: IMG_FB117739-62EC-497D-B74B-BAC4670B9AB5.jpeg]

[M70] AI (2026-03-09 13:51):
Yes. The neat way is to use a **Net Tie**.

For your case, where you want:

- one internal/functional name
- one external/readable name

without directly shorting differently named nets together, **Net Tie** is the proper Altium method.

## Why not just wire two net labels together
If you put two different net labels on one continuous wire, one wins and the other loses.  
They do not become “aliases”.

So you cannot cleanly say:
- this same copper is both `CLK1`
and
- `C1_S1`

using labels alone.

## Best methods

### Method 1 — Net Tie
Use this when you want two separately named nets intentionally joined.

Example:
- `CLK1_CH1`
joined to
- `C1_S1`

This is the cleanest engineering method, especially if both names matter in different places.

### Method 2 — keep one real net name, add text/comment
Use this when you only need human readability on the schematic.

Example:
- actual net label = `CLK1_CH1`
- nearby text note = `C1_S1`

This is simpler, but it does **not** create two net identities.

---

## For your screenshot
Because you seem to want:

- internal repeated channel names like `CLK1`, `CLK2`
- plus more meaningful interface names like `C1_S1`, `SO2`

I’d say:

- use **Net Tie** where you truly need both names to exist as separate nets
- otherwise keep one real net name and use plain text for the functional alias

---

## Practical Net Tie setup
Create a tiny 2-pin component with:
- pin 1 on net A
- pin 2 on net B
- footprint type = Net Tie footprint

Then connect:
- `CLK1_CH1` → one side
- `C1_S1` → other side

Altium treats them as intentionally joined while preserving the two net names.

---

## Rule of thumb
Ask:

**Do I need two actual net names in reports/PCB/connectivity?**

- **Yes** → use **Net Tie**
- **No, I just want clearer schematic meaning** → use **one net name + text note**

---

## For now
Since you are still stabilising hierarchy, I would **not** introduce net ties yet unless you really must.

First get:
- `CLK1_CH1`
- `CLK2_CH1`
- etc

working cleanly.

Then add meaning by either:
- renaming those nets properly, or
- adding net ties to interface aliases.

The next choice is: do you want the **meaningful name** to be the real PCB net name, or just a schematic-facing alias?

[M71] ME (2026-03-09 13:56):
So it doesn’t matter if it doesn’t have a foot print?

[M72] AI (2026-03-09 13:56):
For a **schematic-only alias trick**, yes — it can be a schematic component and not go to PCB.

But for a **proper Altium Net Tie**, it normally **does matter** if you want the PCB to understand the intentional short cleanly.

## The distinction

### Schematic-only helper component
- can have no footprint
- useful just for documentation or logic grouping
- does **not** create a proper physical copper join on PCB

### Real net tie component
- should have a **net-tie footprint**
- used when two differently named PCB nets are intentionally joined
- PCB and rules then understand that short is deliberate

## So for your use case
Ask yourself one thing:

**Do these two names need to be separate all the way into PCB/netlist, then intentionally joined?**

- If **yes**, use a real **Net Tie with footprint**
- If **no**, don’t use a net tie; just choose one real net name and add text/comment for readability

## In your situation
Because you’re still trying to get the hierarchy and naming stable, I would **not** use a footprintless fake net tie right now. That will just add more ambiguity.

Better first decide:
- what the actual net name should be
- where that name should live in the hierarchy

Then only use net ties later if you truly need:
- one internal name
- one external connector/interface name
- both preserved as separate PCB nets

## Practical answer
**Yes, it can exist without a footprint, but then it is not really solving the PCB net-join problem properly.**

So for a real electrical intentional join in Altium, you generally want the net tie to have a footprint.

[M73] ME (2026-03-10 09:12):
So why am I getting duplicate net names for ground connections now 

[M74] AI (2026-03-10 09:12):
Because ground is now being resolved under your **hierarchical rules**, and Altium is finding **more than one net-naming object trying to name the same ground segment**.

Most likely causes are:

- a **GND/0V power port**
- plus a **net label**
- plus possibly a **sheet entry/port**
- all landing on the same wire or same connected copper

With **Strict Hierarchical**, Altium gets fussier about who is allowed to name what.

## The common pattern

You’ll get duplicate net name complaints when one connected wire has, for example:

- a power port `0V`
- and a net label `0V`
- or a sheet entry/port also forcing `0V`

Altium then says, in effect:

“this net is already named, and you’re naming it again.”

## For ground specifically

Ground should usually be done with just:

- a **power port** (`0V`, `GND`, whatever your project standard is)

and **not** also:
- a normal net label of the same name on the same segment
- a hierarchical port/sheet entry trying to pass ground around unnecessarily

## Best rule

For ground and rails:

- use **power ports**
- don’t route them through hierarchy unless you have a very specific reason
- don’t duplicate them with matching net labels on the same net

## What to check right now

On one of the failing ground points, look for any combination of:

- `0V` power port
- `0V` net label
- `0V` port
- `0V` sheet entry

If more than one of those is on the same connected net, that is probably the error.

## What to remove

Usually remove the **normal net label** or **hierarchical port**, and leave only the **power port**.

So if you have:

- wire
- power port `0V`
- net label `0V`

delete the net label.

If you have:

- child sheet port `0V`
- parent sheet entry `0V`
- and also local power ports `0V`

then stop passing ground through the sheet symbol and just use local power ports.

## Why it may have appeared now

Because earlier your project options may have been masking or flattening some of this.  
Now that the hierarchy rules are stricter, Altium is exposing the duplicate naming objects properly.

## Practical guidance for your design

For `0V` / `GND`:
- place **power ports** where needed in child sheets
- do not create sheet entries for them
- do not add matching net labels on the same wire

That is usually the cleanest fix.

If you send one screenshot of an actual duplicate-ground error location, I can tell you exactly which object to delete.

[M75] ME (2026-03-10 09:14):
[image]
[attached file: IMG_CE8737BD-7B4F-486C-9C85-BF902F9B402C.jpeg]

[M76] AI (2026-03-10 09:15):
Yes — that messages panel tells the story.

This is **not just a ground problem**. You’ve got lots of errors of the form:

- `Duplicate Net Names Wire 0V`
- `Duplicate Net Names Wire +3V3D`
- `Duplicate Net Names Wire DRAIN_0`
- `Duplicate Net Names Wire FC1_P`
- etc

So the issue is broader:

## What it means
Altium is seeing the **same wire segment** being named by more than one naming object.

Usually that means one wire has some combination of:

- a **net label**
- a **port**
- a **sheet entry**
- a **power port**

all trying to name it.

With **Strict Hierarchical**, Altium is now enforcing that more clearly.

## Why 0V shows up a lot
Because 0V is often the one net where people accidentally have both:

- a **power port `0V`**
- and a **net label `0V`**

on the same wire.

That alone will trigger this error.

## But your list proves the bigger pattern
Since it also happens on things like:

- `FC1_P`
- `DRAIN_0`
- `REM_SPI_CLK`
- `OD_0`

you almost certainly have a repeated mistake across the design:

**ports/sheet entries are being used to pass names, while net labels are also still sitting on the same wires.**

## The fix pattern
For any given signal wire, choose **one naming method** at that point.

### Inside child sheets
Usually:
- **Port** at the sheet boundary
- normal wire inside
- local net label only if needed elsewhere on that sheet

### On parent sheets
Usually:
- **Sheet entry** at the child symbol
- wire out from it
- optional **net label** on that parent wire if you want a parent-level name

### For power rails and ground
Usually:
- **Power port only**
- no matching net label on the same wire
- no need to pass power through sheet entries unless there is a very specific reason

## So for `0V`
Go to one of those 0V errors and you will probably find something like:

- wire
- `0V` power port
- `0V` net label

Delete the **net label** and leave the **power port**.

## For normal signals like `FC1_P`
You will probably find:

- wire
- a **Port** named `FC1_P`
- and a **Net Label** also named `FC1_P`

or:

- sheet entry + port path
- plus an extra local net label naming the same segment

Delete the redundant one.

## Practical rule
On a single connected wire segment, do not stack naming objects unless there is a real reason.

Bad:
- power port + net label
- port + net label on same boundary wire
- sheet entry feeding a wire that also has another identical naming object unnecessarily

Good:
- one naming object per net segment at that hierarchy boundary

## Fastest cleanup method
Start with the worst offenders:

### 1. Ground and rails
Remove duplicate net labels from:
- `0V`
- `+3V3D`
- `+6`
- `-6`
- `+1V8D`

Leave only power ports.

### 2. Boundary signals
For each child-sheet boundary signal, decide:
- boundary object is **Port/Sheet Entry**
- internal readability is optional text or carefully placed local labels
- don’t place another identical naming object right on the same segment

## Why this appeared now
Because earlier your looser settings were masking it.  
Now the compiler is showing where your schematic has multiple concurrent name sources.

## Best next move
Open one `Duplicate Net Names Wire 0V` item, zoom to it, and check whether that exact wire has both a power port and a net label. That is the pattern to remove everywhere.

[M77] ME (2026-03-10 09:27):
[image]
Change bar to a port like this 
[attached file: IMG_2EE95AB3-2E47-4541-B027-BD7774C32668.jpeg]

[M78] AI (2026-03-10 09:27):
No — not like that.

For `-6V`, use a **power port**, not a normal **Port**.

What your screenshot shows is:

- a `-6V` power port on the net
- and also a yellow **Port** object on the same net, still named `Port`

That is exactly the kind of duplicate naming object causing your compiler errors.

## What to do here
Delete the yellow **Port**.

Leave only the red **power port** `-6V`.

## Rule
For supply rails like:

- `0V`
- `-6V`
- `+6V`
- `+3V3D`
- `+1V8D`

use **power ports only**.

Do **not** also put:
- normal ports
- extra net labels
- sheet entries

on the same local rail wire unless you have a very specific reason.

## So:
- **signal nets** crossing hierarchy → use **Port / Sheet Entry**
- **power rails** like `-6V` → use **Power Port**

That screenshot should end up with just the `-6V` power port on that wire.

Then recompile and see if that particular duplicate-net error disappears.

[M79] ME (2026-03-10 09:34):
[image]
 Well it was like that 
[attached file: IMG_2332BF14-4525-4E15-9FC1-106F276BA7C8.jpeg]

[M80] AI (2026-03-10 09:34):
Then the duplicate is likely **not from that exact spot alone**.

Your screenshot shows the rail itself is already using **power ports only**, which is fine. So the duplicate net-name errors are probably coming from one of these elsewhere:

- the **same rail also has a normal net label** somewhere else on that sheet
- the rail is being brought through a **sheet entry/port** as well as a power port
- the same connected wire segment has been named twice after hierarchy expansion

The fact your message list shows duplicates for many nets, not just power rails, still points to a broader “multiple naming objects on one net” problem.

## Important correction
I also notice something odd in that left sheet:

- one branch is tagged `+6V`
- another branch nearby is tagged `-6V`

If those are connected into the same vertical trunk, that is a much bigger problem than duplicate names.

So first check whether that vertical bus/trunk is actually joining:
- `+6V`
and
- `-6V`

If yes, that is wrong and will absolutely confuse compilation.

## What to do now
Click one duplicate error for `+6V`, then one for `-6V`, and let Altium zoom to each exact location. At each spot check:

- is there a **power port only**
- or is there also a **net label / port / sheet entry**
- are `+6V` and `-6V` accidentally on the same connected trunk

## My read from this screenshot
This image suggests the real issue may be that your left-hand distribution sheet has a shared vertical rail with multiple branches, and at least one branch is being named `+6V` and another `-6V`. If those are electrically connected through that trunk, the compiler is right to complain.

So the next question is not “should it be a port”, but:

**Are `+6V` and `-6V` actually touching the same rail on that left sheet?**

[M81] ME (2026-03-10 09:36):
[image]
I think it’s the extra sheets in the hierarchy 
[attached file: IMG_01873500-3416-409E-A33D-49634059BC2C.jpeg]

[M82] AI (2026-03-10 09:36):
Yes — that is a very plausible root cause.

If you have **extra sheet symbols / extra compiled instances / leftover hierarchy paths** still present, Altium can end up compiling the same child logic more than once, and then you see cascades like:

- duplicate net names
- duplicated ports
- “has only one pin”
- repeated channel tabs
- odd cross-reference contexts

That fits what you’ve been seeing.

## What to check
On `Cover.SchDoc`, you want only the sheet symbols you truly intend to instantiate.

So ask:

- are there any old `Repeat(...)` blocks still on the cover sheet?
- are there any manual instances **and** a repeat block both present?
- are there any unused sheet symbols still pointing to the same child docs?
- are there multiple top-level paths reaching the same child sheet unexpectedly?

## The likely failure mode
If `CH.SchDoc` or the PoGo sheets are being instantiated more than once through different paths, Altium will compile multiple copies of the same nets. Then if those nets also have global-ish naming objects like power ports or flat labels, the compiler starts shouting about duplicates everywhere.

## Best recovery now
Do a hierarchy cleanup, not a signal-by-signal cleanup.

### On the top sheet only
Keep only the sheet symbols you actually want.

Delete or temporarily remove:
- old test symbols
- old repeat blocks
- duplicate child-sheet instances
- orphaned hierarchy experiments

### Then compile again
If the error count drops dramatically, you’ve proved the problem is hierarchy duplication rather than local net naming alone.

## Fast isolation method
A very effective test is:

1. Save a copy of the project.
2. On `Cover.SchDoc`, temporarily delete or comment out all but:
   - one child sheet instance you care about
   - maybe power sheet if essential
3. Compile.

If the duplicate-net storm disappears, the issue is absolutely coming from extra hierarchy paths or duplicated sheet instantiation.

## My read
Given:
- the huge number of duplicate-net errors
- earlier repeat/manual mixing
- extra compiled tabs
- lots of hierarchy experimentation

I think you’re right that **extra sheets in the hierarchy are probably a major contributor**.

## What I’d do next
Reduce the project to the smallest valid hierarchy:

- `Cover.SchDoc`
- `Power.SchDoc`
- one `CH.SchDoc` path only

Compile that. Then add the other sheets back one at a time until the duplicates return. That will tell you exactly which hierarchy branch is poisoning the compile.

[M83] ME (2026-03-10 16:29):
Do the way I’ve solved it is to have unique power names on each sheet 

[M84] AI (2026-03-10 16:29):
Not really — that’s more of a workaround than a clean fix.

If you give each sheet unique power names, you can suppress duplicate-name conflicts, but you also lose the normal meaning of a shared rail like:

- `0V`
- `+6V`
- `-6V`
- `+3V3D`

and then you have to rejoin or remap them later.

## The proper fix
The proper fix is:

- keep shared rails with their normal names
- remove duplicate naming objects on the same net
- clean up the hierarchy so each child sheet is instantiated only the way you intend

## When unique power names are valid
Unique per-sheet power names only make sense if the rails are **actually different isolated rails**, for example:

- `CH1_0V`
- `CH2_0V`

because they are intentionally separate domains.

If they are all meant to be the same board ground or same supply, then renaming them per sheet is not the right underlying solution.

## So:
- **same real rail across sheets** → keep same power-port name, fix hierarchy/naming duplication
- **intentionally isolated rails** → unique names are fine

## In your case
From everything you’ve shown, the issue looks more like:
- extra hierarchy instances
- duplicate ports/labels/power ports
- old repeat/manual experiments still compiling

not that the power nets should genuinely all be different.

So I would treat unique power names as a temporary diagnostic trick, not the final architecture.

[M85] ME (2026-03-10 16:29):
But when I delete ALL references it still does it 

[M86] AI (2026-03-10 16:30):
Then the duplicates are probably **not coming from hierarchy references anymore**.

If you can delete all the obvious extra sheet references and it still happens, that points to one of these deeper causes:

## 1. Multiple naming objects on the same wire segment
Even with no extra hierarchy, Altium will still complain if one net segment has more than one namer, for example:

- power port + net label
- port + net label
- off-sheet connector + net label
- sheet entry + another naming object on the same segment

This is still the most common cause.

## 2. Hidden compiled leftovers from old objects
Sometimes after lots of hierarchy edits, Altium can act dirty until you do a proper reset:

- save all
- close schematic docs
- Project » Compile
- or close/reopen project
- sometimes remove generated outputs / recompile from clean

## 3. Power ports are global by definition
This is the big one.

If the project is set so power ports are global, then `0V`, `+6V`, `-6V` everywhere are already joined project-wide.  
So even if you remove hierarchy references, the compiler still sees those rails globally.

That means the duplicate might still be caused by:
- global power port
plus
- local naming object on that same net

## 4. Off-sheet connectors / ports still naming nets
A lot of the yellow objects you’ve shown were ports. If some of those are still present in places where they should just be labels, they can keep causing duplicates even after hierarchy cleanup.

---

# What to do now: isolate one actual failing net

Do not chase the whole project.

Pick **one** error only, ideally:
- `Duplicate Net Names Wire 0V`

Then at that exact location, inspect the connected segment and list every naming object on it.

For that one segment, check whether it has any of:

- power port
- net label
- port
- off-sheet connector
- sheet entry

If the answer is more than one, that is your cause.

---

# Fast diagnostic test

Take a tiny empty test area or copy of a page and do this:

- one wire
- one power port `0V`

Compile: should be fine.

Then add:
- net label `0V` on same wire

Compile: if duplicate appears, you’ve proved the behaviour.

That gives you a known pattern to hunt for.

---

# Most likely answer in your case

Because you say **even after deleting all references it still does it**, I think the main culprit is now:

**power ports + another namer on the same net**, not hierarchy.

Especially since your message list included many rails and signals, not just hierarchical clocks.

---

# Practical next move

Click one duplicate error, zoom to it, and tell me exactly which objects are sitting on that one failing wire:
- power port?
- net label?
- port?
- off-sheet connector?

That will pin it down fast.

[M87] ME (2026-03-10 16:31):
Yes, it fixed it when I change the name. But then doesn’t like different new names in different sheets 

[M88] AI (2026-03-10 16:31):
Yes — that confirms it.

What you’ve proved is:

- the duplicate error is caused by **same-name global connectivity**
- changing the name removes the clash
- but different names on different sheets then stop being treated as the same rail

So Altium is behaving consistently — just not the way you want yet.

## What that means
For things like power ports, Altium treats same-named rails as the **same global net**.

So:

- `0V` on many sheets → all one net
- rename one to `0V_CH1` → now it is a different net

That is why the duplicate disappears when you rename it, but then the sheets no longer share the rail.

## The real issue
You still have **more than one naming source** on the original rail.

So when the name is the same everywhere, Altium sees:
- one global rail name
- plus another naming object somewhere on that same connected net

When you rename it, you break the connection and the conflict disappears.

## So the fix is not “unique names everywhere”
The fix is:

- keep the real shared rail names the same
- remove the extra namer that is colliding with the power port

## For shared rails like
- `0V`
- `+6V`
- `-6V`
- `+3V3D`

use:
- **power ports only**

and remove:
- normal ports
- off-sheet connectors
- net labels of the same name
- sheet-entry passing of those rails unless absolutely necessary

## Why different new names cause trouble
Because then they are no longer one shared rail.  
You’ve turned one supply into separate isolated nets.

That is only correct if they really are isolated domains.

## Bottom line
Changing the name proved the fault, but it is a **diagnostic**, not the final solution.

The final solution is:
- restore the correct common rail name
- find and remove the other object that is also naming that same rail

## Best next move
Pick one troublesome rail, like `0V`, and on one sheet remove everything except the **power port**. If the duplicate vanishes there, repeat that pattern across the design.

[M89] ME (2026-03-10 16:37):
[image]
[image]
So here’s a test. Fresh power ports not used anywhere else on the design. Used in two sheets. Error!! This isn’t right 
[attached file: IMG_8B2F36DB-8778-4ED9-BDED-11BB42A33FCC.jpeg]
[attached file: IMG_56A515DB-26A8-45A7-93E6-B743D87F794A.jpeg]

[M90] AI (2026-03-10 16:37):
You’ve found the real culprit.

**This is because you set Net Identifier Scope to `Strict Hierarchical`.** In Altium, that mode makes **power ports local**, not global.

So `+12` and `0VT` are treated like ordinary local net names on each sheet. If the same sheet has multiple separate stubs with `+12` or `0VT`, Altium flags them as duplicate net names.

That is why your test feels wrong: for shared rails, you expect power ports to behave globally across sheets.

## Change this
Set:

- **Project Options → Options → Net Identifier Scope = `Hierarchical`**
  not `Strict Hierarchical`

Use the one described like:
- **Hierarchical (sheet entry ↔ port connections, power ports global)**

## Why
That gives you:

- **Ports / sheet entries** still used for hierarchy
- **Power ports** treated as global shared rails, which is what you want for:
  - `+12`
  - `0V`
  - `0VT`
  - `+6V`
  - `-6V`

## So the rule becomes
- **Signals between sheets** → ports + sheet entries
- **Power rails** → power ports, global

## One more thing
You do still have a separate error in your screenshot:

- `Bus range syntax error -5VA[2]`

That one is unrelated and will need fixing separately.

So yes — your instinct was right. **Strict Hierarchical is the wrong mode for your power-port usage.** Switch to **Hierarchical** and recompile.
