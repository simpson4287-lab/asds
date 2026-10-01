# SMBJ15A Transient Protection
Date (UTC): 2026-06-09 16:03
Conversation ID: 6a28390e-d910-83ed-8607-3f4e0d783d00
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-06-09 16:03):
Protecting a 15v rail. I think part SMBJ15A would be a good fit good 

[M2] AI (2026-06-09 16:03):
I’ll sanity-check it against the actual TVS parameters that matter for a 15 V rail: standoff voltage, breakdown range, clamping voltage, and what fault energy you expect it to absorb.

[M3] AI (2026-06-09 16:03):
Yes — **SMBJ15A is a sensible fit for transient protection on a nominal 15 V rail**, but only if you understand what it will and will not do.

For SMBJ15A, typical key figures are:

| Parameter | SMBJ15A value | Meaning |
|---|---:|---|
| Reverse standoff voltage, **VRWM** | **15 V** | It should not conduct significantly at 15 V |
| Breakdown voltage, **VBR min** | **16.7 V** | It starts conducting somewhere above the rail |
| Max clamp voltage, **VC** | **24.4 V** | During a large surge, the rail may still rise to about this level |
| Peak pulse power | usually **600 W**, 10/1000 µs pulse | Good for short transients, not continuous faults |

Sources list SMBJ15A as **15 V standoff**, **16.7 V minimum breakdown**, and around **24.4 V maximum clamp voltage**. citeturn398363search7turn398363search9

So the important point is:

**SMBJ15A protects against spikes, not against a sustained overvoltage.**  
If your 15 V rail normally sits at 15.0 V or maybe 15.3 V, SMBJ15A is about right. It should stay mostly off in normal operation and only conduct on excursions above roughly 16.7 V.

But if your circuit cannot tolerate more than, say, **18–20 V**, then SMBJ15A alone may not be enough, because under a hard transient it can clamp as high as **~24.4 V**. That is normal TVS behaviour.

For a robust rail protection arrangement, I’d usually do:

```text
15 V input/rail
   |
 fuse / polyfuse / current limit
   |
 TVS to 0 V: SMBJ15A
   |
 protected circuit
```

The fuse/current limit matters because if the rail is accidentally connected to, say, 24 V continuously, the TVS may go short or overheat unless something upstream limits or disconnects the current.

**Verdict:**  
**Good choice for transient suppression on a 15 V rail.**  
Not sufficient by itself for sustained overvoltage protection. For that, add a fuse/current limit, crowbar, eFuse, or OV shutdown depending on how serious the fault case is.

[M4] ME (2026-06-10 07:02):
I have a board and the capacitors keep blowing on it. It’s during power on of a wider system. I’ve previously changed them all. Now it’s happening again. I out the TVs in place but it’s still happening.

[M5] AI (2026-06-10 07:02):
That symptom is bigger than “add a TVS”: repeated capacitor failures at system power-on usually means either reverse polarity, overvoltage/inrush/ringing, wrong capacitor derating, or a rail sequencing/backfeed issue. I’ll frame this as a fault-finding path rather than assuming the TVS part is wrong.

[M6] AI (2026-06-10 07:02):
A TVS **not fixing it is actually useful evidence**. It suggests the problem is probably **not just a short high-voltage spike**, or the TVS is placed/selected in a way that cannot protect the capacitors from the actual failure mechanism.

For a **15 V rail where capacitors keep blowing during power-on**, I’d suspect these in roughly this order:

## 1. The capacitors may be under-rated

For a 15 V rail, I would not use **16 V capacitors** unless absolutely unavoidable.

Use at least:

```text
15 V rail → 25 V capacitors minimum
Harsh / long cable / inductive system → 35 V capacitors preferred
```

If they are electrolytics or tantalums, 16 V parts on a 15 V rail are a classic failure setup. Even a small overshoot or tolerance stack can kill them.

For ceramic MLCCs, voltage rating matters too, but they usually crack/short rather than violently “blow”.

## 2. If they are tantalum, that is a huge red flag

If the failed capacitors are **tantalum capacitors**, especially across a power rail, power-on inrush can destroy them.

Tantalums dislike:

```text
high inrush current
low-impedance supply rails
hot-plugging
rail overshoot
reverse voltage
insufficient voltage derating
```

For a 15 V rail, I would be very cautious using tantalum unless they are **surge-rated**, heavily derated, and protected by series impedance.

Rule of thumb:

```text
15 V rail with tantalum → use 35 V or 50 V parts, not 16 V or 25 V
```

If these are tantalums and they are physically exploding, my first move would be to replace them with **aluminium electrolytic / polymer / MLCC combination**, depending on the circuit need.

## 3. The TVS may not clamp low enough to save the capacitors

Your earlier SMBJ15A choice has:

```text
VRWM ≈ 15 V
breakdown starts ≈ 16.7 V
large-surge clamp ≈ 24 V
```

That means the rail can still reach something like **20–24 V during a hard transient** before the TVS meaningfully limits it.

So if you have **16 V or 20 V capacitors**, the TVS may still allow a voltage high enough to damage them.

For example:

```text
15 V rail
SMBJ15A clamps hard at maybe 20–24 V
16 V capacitor sees overvoltage
capacitor fails
```

So the TVS may be working, but the capacitors may still be inadequately rated.

## 4. The TVS cannot survive or clamp properly without source impedance

A TVS needs something upstream to limit current:

```text
supply/cable → fuse/PTC/resistor/inductor/current limit → protected rail → TVS to ground
```

If the wider system has a big low-impedance supply and long cables, power-on can dump a lot of energy into the board. The TVS may briefly conduct, but if the source can provide huge current, the rail can still ring or the TVS may not be enough.

A TVS is not a regulator. It is a surge shunt.

## 5. Long cable / harness inductance can cause power-on ringing

This is very plausible in a wider system.

At power-on you can get:

```text
long cable inductance + board input capacitance + fast supply edge = LC ringing
```

So a nominal 15 V rail can momentarily overshoot well above 15 V.

Example:

```text
Supply steps to 15 V
Cable inductance resonates with input caps
Rail rings to 25–35 V for microseconds
Caps take the hit
```

A TVS helps only if:

```text
it is close to the capacitors
it has a short low-inductance ground return
it clamps below the capacitor damage threshold
it has enough pulse power
there is enough source impedance/current limiting
```

If the TVS is physically far from the failed caps, or grounded through a thin/long track, it may not protect them effectively.

## 6. Check for reverse polarity or negative spikes

Capacitors blowing at power-on can also be caused by a rail briefly going negative, especially if there are multiple supplies sequencing.

Causes include:

```text
supply rails powering in the wrong order
backfeeding through IC protection diodes
motors/relays/solenoids on the same system
inductive loads sharing ground/supply wiring
connector mate/de-mate order
ground bounce
```

Electrolytics and tantalums really hate reverse voltage.

A TVS like SMBJ15A, if unidirectional, mainly protects positive overvoltage. It may clamp negative excursions around a diode drop, but layout and current path matter. A bidirectional TVS behaves differently and may not protect against negative rail events in the same way.

## The first things I’d check

### A. Identify the failed capacitor type and rating

For every capacitor that has blown, note:

```text
cap type: electrolytic / tantalum / ceramic / polymer
capacitance
voltage rating
polarity
location on rail
manufacturer/series if known
```

If you tell me “they are 15 V rail, 22 µF 16 V tantalums”, the answer becomes very direct: **they are not suitably robust for that rail**.

### B. Scope the rail properly at power-on

You need to capture the first few milliseconds, ideally with:

```text
scope probe directly across the failing capacitor
short spring ground, not long crocodile ground
single-shot trigger
wide bandwidth initially
```

Look for:

```text
positive overshoot above 18–20 V
ringing above 25 V
negative dip below 0 V
slow ramp plus sudden spike
multiple pulses as other boards power up
```

Do not only probe at the PSU output. The capacitor is failing on the board, so measure **at the capacitor pads**.

### C. Power the board alone from a current-limited bench supply

Try:

```text
board alone
15 V bench supply
current limit set low
slow ramp if available
```

If the caps survive when powered alone but fail in the wider system, that strongly points to:

```text
system inrush
cable/ringing
sequencing
backfeed
ground shift
hot-plug transient
```

If they fail even on a gentle bench supply, the board itself may have:

```text
wrong polarity capacitor fitted
wrong capacitor voltage rating
shorted downstream rail
regulator fault
incorrect BOM/footprint polarity
```

## What I’d likely change

For a robust 15 V input rail, I’d lean toward something like:

```text
15 V input
   |
fuse / PTC / current limit / small series impedance
   |
bulk electrolytic, 35 V
   |
MLCCs, 25 V or 50 V
   |
TVS to ground, close to connector/input caps
```

If the input is cable-fed or hot-plugged, consider adding damping:

```text
small series resistor / NTC / ferrite / inrush limiter
or RC snubber
or input π filter with damping
```

A very common practical fix is:

```text
replace marginal 16 V/tantalum caps with 35 V aluminium electrolytic or polymer
add TVS at the connector
add some source impedance/current limiting
verify power-on waveform with scope
```

## My strongest suspicion

Given your wording — **“during power on of a wider system”** and **“I changed them all, now it’s happening again”** — I would suspect:

```text
15 V system rail has power-on overshoot/ringing or sequencing/backfeed,
and the capacitors are not sufficiently derated for the real transient.
```

The SMBJ15A may be too soft/late to protect low-rated caps, especially if the failed caps are **16 V or 20 V** parts.

The most important next fact is: **what are the capacitor voltage ratings and type?** If they are tantalum or 16 V electrolytics on a 15 V rail, I’d treat that as the primary problem.

[M7] ME (2026-06-10 07:06):
Tantalum, 25V, 10uf. Sure the polarity isn’t reversed as it’s an established system.

[M8] AI (2026-06-10 07:06):
Yes — **25 V, 10 µF tantalum on a 15 V rail is still quite vulnerable**, especially at system power-on.

Even though the nominal derating looks okay-ish:

```text
15 V rail on 25 V tantalum = 60% of rated voltage
```

that is **not generous for tantalum**, particularly if the rail is low impedance, cable-fed, hot-plugged, or has power-on ringing. For tantalums on supply rails, I’d much rather see:

```text
15 V rail → 35 V tantalum minimum
15 V rail with nasty power-on / system harness → 50 V, or avoid tantalum
```

The polarity being correct does **not** rule out the main tantalum failure modes.

## Why the TVS may not have saved it

An **SMBJ15A** does not clamp at 15 V. It starts conducting above the rail and, under a real surge, the clamp can be much higher.

So the rough picture is:

```text
15 V nominal rail
25 V tantalum capacitor
SMBJ15A TVS

Power-on transient/ringing maybe reaches 24–30 V locally
TVS conducts, but not low/fast enough at the capacitor
tantalum sees surge voltage + huge inrush
capacitor fails short/explodes
```

A 25 V tantalum may survive normal 15 V use for years, then fail when the wider system produces a harsher startup transient than usual.

## Tantalum has a second problem: surge current

Even if the voltage never goes much above 25 V, tantalums can fail from **high dV/dt / surge current** during power-on.

At startup, a discharged 10 µF tantalum looks like a short for a brief moment. If the upstream supply/cable can dump current hard into it, the capacitor can develop a microscopic defect, go into thermal runaway, then fail short.

That is why tantalum application notes often require **series impedance** or significant derating on low-impedance rails.

## My diagnosis would be

Most likely:

```text
The 15 V rail is experiencing power-on overshoot, ringing, or very high inrush current,
and 25 V tantalums are not robust enough in that position.
```

Less likely, but still possible:

```text
a rail sequencing/backfeed event briefly pulls the capacitor reverse-biased
a downstream regulator/input stage is failing and stressing the cap
the TVS is placed too far from the failing capacitor
the TVS has failed open or is not actually connected effectively
```

## What I would change first

I would **stop replacing them with the same tantalums**.

For repair/prototype debugging, I’d replace the failed 10 µF 25 V tantalums with either:

```text
10 µF to 22 µF aluminium electrolytic, 35 V or 50 V
```

or:

```text
10 µF polymer capacitor, 35 V or higher
```

plus nearby ceramics, for example:

```text
100 nF ceramic, 50 V
1 µF ceramic, 50 V
```

If ESR matters for a regulator, check the regulator datasheet before swapping tantalum to ceramic/polymer, because some older regulators rely on tantalum-like ESR for stability.

## Protection improvement

Your current protection is probably incomplete. I’d prefer:

```text
15 V input
   |
fuse / PTC / current-limited source / small series resistor
   |
TVS to 0 V near board input
   |
bulk capacitance
   |
local decoupling near loads
```

For the local 10 µF capacitors, the real fix may be one of these:

```text
replace 25 V tantalum with 35/50 V aluminium/polymer
add small series resistance or ferrite before the local cap
slow the 15 V rail rise
add inrush limiting
move/add TVS closer to the board input
add reverse/negative transient clamp if sequencing causes dips
```

## One very useful test

Scope directly across the capacitor pads at power-on:

```text
probe tip on capacitor +
spring ground on capacitor -
single-shot trigger
fast timebase for first few µs/ms
also capture slower 0–100 ms startup
```

You are looking for:

```text
positive overshoot above ~20–25 V
ringing
negative voltage
multiple startup bumps
very fast edge from a low-impedance source
```

Do **not** use a long oscilloscope ground lead for this test. It can invent or hide exactly the kind of spike you’re trying to see.

## Practical verdict

A **25 V tantalum on a 15 V rail in an established system can still be the weak point**. The fact that it happens during wider-system power-on strongly points to **surge/ringing/inrush**, not simple polarity error.

My first practical fix would be:

```text
replace the 10 µF 25 V tantalums with 10–22 µF 35/50 V aluminium electrolytic or polymer parts
keep/add 100 nF ceramic locally
verify regulator stability
scope the rail at the capacitor during system power-on
```

I would not trust another set of 25 V tantalums until you’ve seen the actual startup waveform.

[M9] ME (2026-06-10 07:10):
They had added two 100nF caps at the input. I didn’t see the point in this 

[M10] AI (2026-06-10 07:10):
You were probably right to be sceptical: **two 100 nF caps at the input are not a meaningful fix for tantalums blowing on a 15 V rail**.

They may help with **very high-frequency noise**, but they do almost nothing for the likely failure mechanisms:

```text
100 nF + 100 nF = 200 nF total
Existing tantalum = 10 µF each
```

So even two 100 nF caps only add:

```text
0.2 µF
```

That is **2% of one 10 µF capacitor**. In terms of bulk energy/inrush/ringing control, it is tiny.

Where they **can** help:

```text
fast switching noise
RF pickup
very sharp local edges
providing a low-inductance HF bypass near a connector or IC
```

Where they **will not** solve much:

```text
15 V power-on overshoot
long-cable LC ringing at lower frequency
large inrush current
sustained overvoltage
tantalum surge failure
rail sequencing/backfeed
```

In fact, adding ceramics at the input can sometimes make power-on ringing **sharper**, because ceramics have very low ESR. They reduce high-frequency impedance, but they do not provide damping. If the source cable/wiring is inductive, adding low-ESR capacitance can contribute to an LC tank unless there is some loss/resistance in the path.

The input really wants one of these, depending on the actual waveform:

```text
TVS + fuse/current limit
35/50 V bulk electrolytic or polymer
some damping impedance
inrush limiting
RC snubber
better rail sequencing/backfeed protection
```

For your case, I’d treat the two 100 nF caps as **decoupling hygiene**, not protection.

A better mental model:

```text
100 nF ceramic = high-frequency bypass
10 µF tantalum = local bulk/decoupling
TVS = transient shunt
fuse/current limit = energy limiter
electrolytic/polymer ESR or resistor = damping
```

So if the tantalums are still failing, the 100 nF additions were almost certainly addressing the wrong layer of the problem.

My suspicion remains:

```text
15 V rail power-on transient/ringing/inrush
+
25 V tantalums
+
not enough damping/current limiting
=
repeat capacitor failure
```

The next most useful step is to **replace one affected tantalum position with a 35 V or 50 V aluminium electrolytic/polymer**, then scope the rail at that position during full-system power-on.

[M11] ME (2026-06-10 07:11):
The tantalum’s support some opamps used as signal amplifiers. The inputs to these amplifiers have 0R. Could that possibly be an issue?

[M12] AI (2026-06-10 07:11):
Yes, **it could be related**, but not in the simple sense of “0 Ω input resistors make tantalums blow.”

A **0 Ω series link on an op-amp input** is usually just a configurable jumper or placeholder. On its own, it should not stress the 15 V rail decoupling capacitors.

But it becomes suspicious if the op-amp input signal can be present when the op-amp supply rail is off, ramping, or unstable.

## The possible failure path

If the signal input arrives before the op-amp is powered, or comes from another board/system with a different power sequence, the op-amp input protection structures can conduct into the op-amp supply rail.

That can create a backfeed path like this:

```text
external signal source
   |
0 Ω input link
   |
op-amp input pin
   |
internal ESD / input protection diode
   |
op-amp supply rail
   |
local 10 µF tantalum
```

So during wider-system power-on, the local rail may be charged, discharged, pulled negative, or partially powered through the signal input rather than through the intended supply path.

That can absolutely cause nasty behaviour around the local rail capacitors.

## Why the 0 Ω matters

With **0 Ω**, there is essentially no current limiting into the op-amp input protection network.

If the input signal is present while the op-amp supply is missing or ramping, the only things limiting current may be:

```text
source driver impedance
cable impedance
op-amp internal diode/ESD structure
PCB traces
the rail capacitor itself
```

That is not ideal.

A small series resistor would limit fault/backfeed current:

```text
0 Ω replaced by 1 kΩ to 10 kΩ
```

For many signal amplifier inputs, even **100 Ω to 1 kΩ** can make a huge difference while having minimal effect on normal operation. The right value depends on signal bandwidth, source impedance, bias current, and noise requirements.

## How this could blow the tantalum

There are a few plausible mechanisms:

### 1. Back-powering the op-amp rail

A signal arrives before the 15 V supply. Current flows through the input protection diode into the rail and charges the local tantalum in an uncontrolled way.

That can cause:

```text
high surge current
partial rail rise
rail collapse when main power arrives
oscillation/ringing
reverse stress if another rail moves differently
```

### 2. Input below ground or above rail during sequencing

If the input goes outside the op-amp rails during power-up, the op-amp clamps it internally. That injected current has to go somewhere — often into the supply rail.

### 3. Dual-supply op-amp issue

If the op-amps use something like:

```text
+15 V and -15 V
```

then sequencing becomes even more important. One rail may come up first, while input signals or feedback paths pull the other rail around. A tantalum from rail to ground can briefly see reverse or overvoltage stress.

### 4. Signal source has stored energy

If the op-amp inputs are connected to long cables, other boards, sensors, or outputs with capacitors, then the input may not be a harmless high-impedance node during power-on. It may have enough stored or driven energy to inject current into the op-amp rail.

## What I’d check

Scope these during full-system power-on:

```text
op-amp +15 V rail at the tantalum
op-amp input pin
input signal source side of the 0 Ω link
op-amp output
if present, op-amp -15 V rail
```

You are looking for this kind of thing:

```text
input signal present before op-amp rail
input pin > V+ + 0.3 V
input pin < V- - 0.3 V
local 15 V rail rising before the main 15 V arrives
local rail going negative
large rail bump when the wider system powers on
```

If the input is ever outside the op-amp supply rails during power-up, the 0 Ω link is very relevant.

## Quick practical experiment

Replace the 0 Ω links temporarily with resistors:

```text
start with 1 kΩ
```

Then power the wider system and see whether the fault stops or the rail waveform improves.

If the input bandwidth is low, try:

```text
4.7 kΩ or 10 kΩ
```

If it is a faster analogue signal, use something smaller:

```text
47 Ω, 100 Ω, 220 Ω, 1 kΩ
```

Even **100 Ω** is vastly better than 0 Ω for limiting clamp current.

## But I would still change the tantalums

Even if the 0 Ω input links are contributing, **25 V tantalums on a 15 V rail remain marginal in a harsh power-up environment**.

For op-amp rail decoupling I’d prefer:

```text
100 nF ceramic close to each op-amp supply pin
+
1 µF to 10 µF ceramic / electrolytic / polymer nearby
```

For the 15 V rail bulk/local support:

```text
10 µF aluminium electrolytic or polymer, 35 V or 50 V
```

or if tantalum must remain:

```text
35 V or 50 V surge-rated tantalum
with some series impedance/inrush control
```

## My verdict

The **0 Ω input links could definitely be part of the root cause** if the op-amp inputs are connected to signals from elsewhere in the wider system and those signals power up in a different order.

The most likely mechanism would be:

```text
input signal arrives during power sequencing
→ op-amp input protection conducts
→ local 15 V rail is backfed or pulled around
→ 25 V tantalum sees surge/reverse/overvoltage stress
→ capacitor fails
```

So yes: I would investigate the 0 Ω links seriously, especially if the amplifier inputs come from another board, cable, sensor, ADC/DAC module, or externally powered source.

[M13] ME (2026-06-10 07:51):
They are just opamps buffing signals. So there should t be any reason why they have to be rants?

[M14] AI (2026-06-10 07:51):
Correct — for **ordinary op-amp signal buffering**, there is usually **no strong reason those local 10 µF rail capacitors have to be tantalum**.

In fact, given they are repeatedly failing, I would actively move away from tantalum unless there is a very specific stability or legacy reason.

For op-amp supply decoupling, the usual requirement is simply:

```text
each op-amp supply pin:
100 nF ceramic close to the pin

each local op-amp area / rail section:
1 µF to 10 µF local bulk capacitance
```

That local bulk cap can often be:

```text
10 µF aluminium electrolytic, 35 V or 50 V
10 µF polymer, 35 V or 50 V
4.7–10 µF MLCC, 25 V or 50 V, if suitable
```

For a 15 V rail, I’d personally favour **35 V or 50 V aluminium electrolytic/polymer** for the replacement, not another 25 V tantalum.

The only reasons tantalum might have been used originally are things like:

```text
compact size
known ESR for stability
low leakage compared with old electrolytics
legacy BOM choice
mil/aerospace-style design habits
availability at the time
```

But for op-amp buffers, those are rarely mandatory.

One caution: if the op-amp circuit includes a regulator nearby, or the tantalum is actually on the **output of an older linear regulator**, then ESR might matter. Some older LDOs were designed assuming tantalum-like ESR and can oscillate with very low-ESR ceramics. But if these caps are just across the op-amp ±15 V or +15 V rail as local decoupling, replacing them with suitable electrolytic/polymer parts is normally fine.

I’d probably do this:

```text
Remove failed 10 µF 25 V tantalum
Fit 10 µF to 22 µF aluminium electrolytic, 35 V or 50 V
Keep/add 100 nF ceramic close to op-amp supply pins
Scope the rail during full-system power-on
```

If space allows, a **10 µF 50 V aluminium electrolytic** is a very safe diagnostic substitution. It may not be as neat or compact, but it is much more forgiving of surge and power-on abuse than a tantalum.

So yes: **unless there is a known stability requirement, I see no reason they need to be tantalum in a simple op-amp buffer supply role.**
