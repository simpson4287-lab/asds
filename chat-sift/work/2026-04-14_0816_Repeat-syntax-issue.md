# Repeat syntax issue
Date (UTC): 2026-04-14 08:16
Conversation ID: 69ddf7c3-5260-8392-a36d-5006fdae50b0
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-14 08:16):
[image]
Why is this re-use working not working? It seems inconsistent hwerenit works in some but not others 
[attached file: IMG_DA259DAB-2239-448A-8E22-D724C7DBE173.jpeg]

[M2] AI (2026-04-14 08:16):
This is almost certainly **Repeat syntax / net naming mismatch**, not Altium being random.

In Altium multi-channel reuse, `Repeat(...)` only works cleanly when the **base net name inside the repeated sheet matches exactly** what the parent sheet expects.

From your screenshot you have things like:

`CLMPV_CH1`  
`CLIPV_CH0`  
`GAIN_CH0`

but the harness/port on the repeated block appears to expect:

`Repeat(GAIN)`  
`Repeat(CLMP-V)`  
`CLIP-V`

That is inconsistent.

### Key rule

For `Repeat(GAIN)` to expand correctly, the repeated child sheet should expose a port/net called:

`GAIN`

Then Altium generates channelised nets such as:

`GAIN_1`, `GAIN_2`, etc.

But if your source nets are already manually named:

`GAIN_CH0`, `GAIN_CH1`

then Altium may not map them through `Repeat(GAIN)` as expected.

### The likely issues in your screenshot

1. **Manual channel suffixes**
   - `CLMPV_CH1`
   - `CLMPV_CH2`
   - `GAIN_CH0`

   These fight against Altium’s own repeat naming.

2. **Hyphen mismatch**
   - You have `CLMPV_CH1`
   - But the repeat label is `Repeat(CLMP-V)`

   `CLMPV` and `CLMP-V` are not the same net name.

3. **Different naming between OS0/OS1**
   - Some use `CH0`
   - Some use `CH1`
   - Some use `CH2`

   Altium will not infer that those are members of the same repeated signal unless the naming structure is exact.

### What I’d do

Inside the reusable child sheet, keep the ports generic:

```text
CLMPV
CLIPV
GAIN
CLC_P
CLC_N
```

At the parent/top level, use:

```text
Repeat(CLMPV)
Repeat(CLIPV)
Repeat(GAIN)
Repeat(CLC_P)
Repeat(CLC_N)
```

Do **not** manually add `_CH0`, `_CH1`, etc. Let Altium generate the channel suffixes.

### Also check this

Right-click the repeated sheet symbol and check:

**Sheet Symbol Designator** should be something like:

```text
OS[0..1]
```

or

```text
Repeat(OS, 0, 1)
```

Then make sure the sheet entries use matching `Repeat(...)` syntax.

Your `repeat(OS,0,1)` at the top looks suspicious too — Altium is usually picky about the exact reuse setup between the sheet symbol designator and sheet entries.

The clean fix is: **remove manual channel suffixes and make the child-sheet ports match the `Repeat(...)` names exactly.**

[M3] ME (2026-04-14 08:22):
[image]
I've got inlt to this 
[attached file: IMG_90FEA9F3-4D66-48D8-8E90-1F264C626892.jpeg]

[M4] AI (2026-04-14 08:22):
You’re closer, but the names still don’t match.

You currently have parent nets like:

```text
GAIN_SEL_OS
CLIP_BIAS_OS
CLAMP_BIAS_O
```

But the sheet entries say:

```text
Repeat(GAIN)
Repeat(CLIP-V)
Repeat(CLMP-V)
```

That won’t bind properly because Altium is looking for the repeated base names `GAIN`, `CLIP-V`, `CLMP-V`, while your connected net labels are different.

Use one naming scheme only.

For example, make the three parent labels:

```text
GAIN
CLIP-V
CLMP-V
```

Then the sheet entries:

```text
Repeat(GAIN)
Repeat(CLIP-V)
Repeat(CLMP-V)
```

And inside each repeated OS sheet, the ports should also be exactly:

```text
GAIN
CLIP-V
CLMP-V
```

Not:

```text
GAIN_SEL_OS0
CLIP_BIAS_OS1
CLAMP_BIAS_OS0
```

Also, I’d avoid the hyphen if possible. Altium usually copes, but for sanity I’d use underscores:

```text
GAIN_SEL
CLIP_BIAS
CLAMP_BIAS
```

Then:

```text
Repeat(GAIN_SEL)
Repeat(CLIP_BIAS)
Repeat(CLAMP_BIAS)
```

Main thing: **the name inside `Repeat(...)` must match the base net/port name exactly.**

[M5] ME (2026-04-14 08:28):
Ok they are all
Working exceptncor the dark green Gain-ch0

[M6] AI (2026-04-14 08:28):
That dark green one is probably **not actually electrically joined** to the vertical bus/wire, even though it visually touches.

In Altium, do this on `GAIN_CH0`:

1. **Click the green wire segment** and check the net name in the Properties panel.
2. It should show the same net as the sheet entry expansion, likely something like `GAIN_CH0` / `GAIN0` depending on your repeat setup.
3. If it says **

[M7] ME (2026-04-14 08:28):
[image]
[attached file: IMG_9BA6FC15-5A0E-4F1C-B0D5-FD38ED63492F.jpeg]

[M8] AI (2026-04-14 08:28):
That looks like a **wire junction issue**, not a repeat issue now.

`GAIN_CH0` appears dark green because Altium is treating it as a **separate net segment**. The small green dot on the left suggests it may be connected to the port, but the right-hand end into the vertical bus/wire likely is **not truly joined**.

Do this:

1. Delete the `GAIN_CH0` wire segment completely.
2. Re-draw it from the port pin to the vertical wire/bus in one action.
3. Make sure a junction dot appears where it meets the vertical line.
4. Recompile.

Also check the label:

`GAIN_CH0` should feed into the repeated parent net `GAIN_CH`, which then maps to:

```text
Repeat(GAIN)
```

But if the child port is called `GAIN`, the parent side ideally wants:

```text
GAIN_CH
Repeat(GAIN)
```

and the individual channels should be generated by the repeat system, not manually forced.

Very likely fix: **delete and redraw that one connection**. Altium often leaves a wire visually touching but electrically disconnected when it was moved or copied.
