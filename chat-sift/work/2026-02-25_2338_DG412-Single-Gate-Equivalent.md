# DG412 Single Gate Equivalent
Date (UTC): 2026-02-25 23:38
Conversation ID: 699f87fe-b384-8389-92aa-fb11bda8b2ae
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-02-25 23:38):
Is there a single gate equivalent to dg412 

[M2] AI (2026-02-25 23:39):
Yes — the closest **single-channel (1× SPST) “gate” equivalent** to a **DG412 (normally-open)** is:

- **DG418** — **single SPST, normally open (NO)** citeturn3view0turn2view0

(For completeness: **DG417** is the **normally-closed (NC)** single-SPST sibling, analogous to DG411.) citeturn2view0turn3view0

Both DG417/DG418 run on similar supply ranges (single +10 to +30 V or ±4.5 to ±20 V class) and are intended as the “single switch” versions in the same general family of parts. citeturn2view0turn3view0

[M3] ME (2026-02-26 19:24):
Do they not come in sot23/5

[M4] AI (2026-02-26 19:24):
Not really, no — **DG417/DG418 (the “direct” single-SPST equivalents)** don’t come in **SOT-23-5**.

**Smallest official package in that family is 8-pin**, e.g. the **DG417L/DG418L/DG419L** variants which explicitly call out a **“Tiny 8-Pin µMax”** package. citeturn1search4  
(And the older DG418 is commonly PDIP/SOIC/CDIP style packages, not SOT-23-5.) citeturn1search2

### If you specifically need “tiny like SOT-23”
Two practical routes:

1) **High-voltage SPST in SOT-23 footprint (closest electrically to DG412 use-cases)**  
- **ADG1201 / ADG1202** (SPST, low leakage/charge injection, **±15 V / +12 V class**, “in SOT-23”). citeturn0search2turn0search1  
*(Note: these are typically SOT-23 with 6 leads, not 5.)*

2) **True SOT-23-5 SPST switches exist, but they’re usually low-voltage**  
- Example: **TI TS12A4514** is an SPST analog switch in **SOT-23 (5-pin)**. citeturn0search4  
*(But it’s “low-voltage/single-supply” class — so only suitable if your signal/supply rails are much lower than DG412’s typical ±/high-voltage realm.)*

If you tell me your **signal range / supplies** (e.g., ±15 V? 0–10 V? single 5 V?) and whether you need **NO vs NC**, I’ll point you at the cleanest SOT-23 option that truly matches.

[M5] ME (2026-02-26 19:26):
OS clamp, typically 25V

[M6] AI (2026-02-26 19:26):
If you need to **pass/clamp signals around ~25 V**, then **SOT-23-5 is basically a dead end** for “DG412-class” parts. What *does* exist in a very small footprint is **SOT-23-6**.

### Good tiny-footprint options that can actually handle 25 V signals

**1) MAX4648 (SPST, normally-open) — SOT-23-6, up to +36 V supply**
- Runs from **+9 V to +36 V single supply** (or ± rails) and is explicitly an **SPST analog switch in SOT-23-6**. citeturn0search1  
This is the closest “single-gate” concept to a DG412, but in a tiny package.

**2) ADG1201 (SPST, normally-closed) — SOT-23-6, iCMOS high-voltage process**
- Available in **SOT-23-6**. citeturn0search0turn0search2  
However: the key gotcha is **your signal range must sit within the device supply rails**. So it’s only a fit if you’re actually powering it with rails that accommodate that 25 V node (e.g., a high single supply), not if you’re on +5 V/+12 V logic rails.

### Practical takeaway
- **For ~25 V analog levels:** look for **SOT-23-6 SPST** parts like **MAX4648** (NO). citeturn0search1  
- **SOT-23-5:** you’ll mostly find **low-voltage** switches there; they won’t tolerate a 25 V signal.

If you tell me:
- is your switch **NO or NC** (DG412 is NO), and  
- what are your **actual supply rails** (single 30 V? ±15 V? +12 V only?),  
…I’ll point you at the cleanest exact part number(s) that meet **signal range + R\_ON + leakage** without surprises.

[M7] ME (2026-02-26 19:27):
Normally open

[M8] AI (2026-02-26 19:27):
For **normally-open** and needing to tolerate **~25 V** on the analog node, the clean “tiny package” answer is:

- **MAX4648** — **1× SPST, Normally-Open (NO)**, **SOT-23-6**, operates from **+9 V to +36 V** (or ±4.5 V to ±20 V). citeturn0search0turn0search1

That’s about as close as you’ll get to a **DG412-style single switch** in a *very* small footprint **while still being happy at 25 V**.

Two important practical notes:
- **SOT-23-5 specifically**: you’ll struggle to find genuine **25–36 V analog switches** in that 5-pin body; the high-voltage ones are typically **SOT-23-6** (need the extra pin for supply/control/NC arrangements). citeturn0search0  
- As always with analog switches, your **signal must remain within the powered rails** (so if you want to pass 25 V, your supply needs to accommodate that — e.g. a high single supply). citeturn0search0

If you tell me your **allowed RON** (DG412 is relatively low; MAX4648 is ~25 Ω class), I can suggest whether MAX4648 is fine or whether you’ll need to accept a bigger package to get lower RON.

[M9] ME (2026-02-26 19:28):
What’s the different between the dg412

[M10] AI (2026-02-26 19:28):
Assuming you mean **vs the MAX4648 I suggested** (single NO in SOT-23-6), the key differences are:

### DG412 (quad) vs MAX4648 (single)
- **Channels**
  - **DG412:** **4× SPST**, **normally-open** (NO). citeturn5view0  
  - **MAX4648:** **1× SPST**, **normally-open** (NO). citeturn6view0  

- **Package**
  - **DG412:** multi-pin packages like **DIP / SO / TSSOP** (not SOT-23). citeturn5view0  
  - **MAX4648:** **SOT-23-6** (“tiny 6-pin SOT23”). citeturn6view0  

- **On-resistance (RDS(ON))**
  - **DG412:** **35 Ω max** (and emphasizes good channel-to-channel matching/flatness). citeturn5view0  
  - **MAX4648:** **25 Ω max** (±15 V supplies), flatness **2 Ω max** over signal range. citeturn6view0  

- **Leakage**
  - **DG412:** off-leakage **<5 nA at +85 °C** (called out as an improvement). citeturn5view0  
  - **MAX4648:** off-leakage **1 nA max at +25 °C**. citeturn6view0  

- **Charge injection (S/H friendliness)**
  - **DG412:** **10 pC max** called out. citeturn5view0  
  - **MAX4648:** not highlighted the same way on the front page; you’d check the electrical table if that’s critical. citeturn6view0  

- **Supplies / signal range**
  - Both can run from **single high supply** or **± rails**:
    - **DG412:** +10 to +30 V or ±4.5 to ±20 V citeturn5view0  
    - **MAX4648:** +9 to +36 V or ±4.5 to ±20 V citeturn6view0  

If you tell me what matters most for your “OS clamp” use (RON, leakage at temp, charge injection, bandwidth), I can steer you to the best small-package NO option—even if it means stepping up from SOT-23-6 to a tiny DFN/QFN to get lower RON.

[M11] ME (2026-02-26 19:30):
It looks like max is superior anyway 

[M12] AI (2026-02-26 19:30):
On paper it **does look “better” in a few headline specs**, but it’s not a straight “superior” across the board — it’s more **different optimisation + different integration level**.

### Where MAX4648 genuinely looks better (vs DG412)
- **Higher single-supply ceiling:** **+36 V** vs **+30 V**. citeturn0search0turn0search1  
- **Lower max RON (headline):** **25 Ω max** (MAX4648) vs **35 Ω max** (DG412). citeturn0search1turn0search0  
- **Much smaller package:** SOT-23-6 vs multi-pin IC packages. citeturn0search1turn0search0  

### Where DG412 can still be the better choice
- **You need 4 switches in one IC.** DG412 gives you 4× SPST NO; MAX4648 is 1×. Board area *might* still favour DG412 if you need several channels (and routing/decoupling is simpler). citeturn0search0turn0search1  
- **Off-leakage across temperature.** DG412 explicitly calls out **<5 nA at +85 °C**; MAX4648’s headline leakage spec is quoted at **+25 °C** (you’d want to check the full table/conditions if leakage at hot is critical). citeturn0search0turn0search1  
- **Charge injection is explicitly specified for DG412** (10 pC max is front-and-centre), which matters in sample/hold or precision clamping. MAX4648 may be fine, but you’d verify the exact test conditions/spec in the electrical characteristics. citeturn0search0turn0search1  

### Practical verdict for your use (NO, ~25 V clamp)
If you only need **one gate** and you want a **tiny footprint**, **MAX4648 is a very strong pick**. If your clamp node is **high impedance** or you care about **behaviour at elevated temperature** (oven/chamber vibes), I’d compare:
- **Ioff / Ion leakage vs temperature**
- **charge injection**
- **RON flatness over your signal swing**

If you tell me your rough clamp topology (e.g., “switch connects node to reference through R”, expected node impedance, and temperature range), I’ll sanity-check whether **MAX4648’s leakage/charge injection** could become the dominant error term.

[M13] ME (2026-02-26 19:34):
[image]
[attached file: IMG_D585E17E-34E9-444B-8069-A9ED7A44E332.jpeg]

[M14] AI (2026-02-26 19:35):
Yep — **in your clamp topology, MAX4648 is very likely “as good or better” in practice**, but for **reasons that matter in *this* circuit**, not because the headline R\_ON number is lower.

### What your snippet is doing
You’ve got **C4 (10 µF) as the clamp/storage cap**, and the **DG412LE switch** connects the incoming side to the post-cap node **through R153 = 1 kΩ** during the clamp window, i.e. a classic “restore/clamp” action. (Your symbol even notes *“switches shown for logic ‘0’ input”* in the DG411–DG413 datasheet.) citeturn5view0

That **1 kΩ dominates** the clamp charge/discharge behaviour, so the switch’s **25 Ω vs 35 Ω** is basically in the noise.

### The specs that actually matter here
1) **Off leakage (I\_OFF) when the switch is open**  
That leakage is what will slowly “walk” the voltage on the C4 node between clamp pulses.

- DG412 family highlights **< 5 nA at +85 °C**. citeturn5view0  
- MAX4648 headline is **1 nA max** (and it’s a single NO switch). citeturn1view0turn0search0  

Back-of-envelope droop if leakage were the only error term:  
- 5 nA into 10 µF → **0.5 mV/s**  
- 1 nA into 10 µF → **0.1 mV/s**  
So either is usually fine unless you’re holding for ages or you’re chasing microvolt-level baseline stability.

2) **Charge injection / feedthrough during the clamp edge**  
DG412 explicitly calls out **10 pC max** charge injection. citeturn5view0  
MAX4648 doesn’t shout that spec on the front page; you’d verify in the tables if your clamp edge is creating a visible “tick” that matters. citeturn1view0  

3) **Voltage headroom**
- DG412: **+10 to +30 V** (single supply). citeturn5view0  
- MAX4648: **+9 to +36 V** (single supply). citeturn1view0turn0search0  

For your “typically 25 V” clamp world, MAX4648 gives **more margin**.

### Practical “gotchas” to check before swapping
- **Logic sense:** DG412 is shown “for logic 0 input” (i.e., your symbol indicates the closure condition). citeturn5view0  
  Confirm MAX4648’s truth table matches what you want (it is NO, but input polarity still matters). citeturn1view0turn0search0  
- **Signal must stay within the analog rails** (whichever part you use). If you’re clamping around ~25 V, you must actually be powering the switch so that 25 V is inside its COM/NO range. citeturn1view0turn5view0  

If you want, tell me:
- what are the **switch rails** in this design (single +30? +28? +36?),
- and what’s the **clamp pulse rate / hold time**,
and I’ll sanity-check leakage-droop and whether charge injection could be visible at the ADA4817 input.

[M15] ME (2026-02-26 19:38):
30max
500khz 

[M16] AI (2026-02-26 19:38):
Got it: **V\_ANALOG up to 30 V** and you’re talking **~500 kHz clamp activity**.

### 1) Leakage droop is utterly negligible at 500 kHz
Period at 500 kHz is **2 µs**.

Even if you pessimistically take **I\_OFF = 5 nA** (DG412 worst-case headline at +85 °C), your cap is **C4 = 10 µF**, so droop per cycle is:

\[
\Delta V = \frac{I \cdot \Delta t}{C}
= \frac{5\text{ nA}\cdot 2\text{ µs}}{10\text{ µF}}
= 1\text{ nV}
\]

So from a “hold the clamp level between updates” standpoint, **both DG412 and MAX4648 are effectively perfect** at that rate.

### 2) The elephant in the room: your RC is 10 ms
You’ve got **R153 = 1 kΩ** into **C4 = 10 µF**, so:

\[
\tau = R C = 1\text{k}\Omega \cdot 10\text{ µF} = 10\text{ ms}
\]

At **500 kHz**, one period is **2 µs**, which is:

\[
\frac{2\text{ µs}}{10\text{ ms}} = 0.0002 = 0.02\% \text{ of a time constant}
\]

Meaning: if you’re truly *trying to correct/update the clamp level every 2 µs*, this network **cannot move the capacitor meaningfully per cycle**. In practice that usually means either:

- 500 kHz is the **signal bandwidth / pixel rate**, and the clamp happens at a much lower rate (line/frame/blanking), **or**
- the clamp switch is toggling fast, but the cap node is intended to be **very stiff** and only “nudged” slowly (less common).

So before worrying DG412 vs MAX4648, the key sanity check is: **what is the actual clamp update window and how long is it held closed?**

### 3) What *might* matter at 500 kHz: feedthrough/glitching
With a big 10 µF to ground, **charge injection steps are tiny** if they land on that node:

- even 10 pC into 10 µF → **1 µV** step.

But at 500 kHz you can still get **AC feedthrough** via the switch’s parasitic capacitances and the series resistor network, which can show up as a small ripple at the high-impedance summing node going into your ADA4817 stage. That effect depends more on **C\_OFF / C\_ON, layout, and what impedance the node “sees” at 500 kHz** than on the DC R\_ON headline.

### What I’d do next (no extra questions, just the useful fork)
- If **the clamp is meant to operate at line/frame blanking** (i.e., not 500 kHz), then **MAX4648 is a nice improvement purely for package and voltage headroom**, and performance will likely be indistinguishable or slightly better.
- If you *really* mean **the clamp is pulsing at 500 kHz**, then the **RC values dominate** and I’d revisit **R153/C4** (or confirm the intent is slow averaging).

If you paste one more zoomed-out snip showing what drives **CLAMP** and what node the switch is clamping *to* (0 V? a reference?), I can tell you immediately whether this is a conventional “blanking clamp” (and your 500 kHz is just the signal), or a genuinely high-rate clamp where the RC needs rethinking.

[M17] ME (2026-02-26 20:36):
[image]
Previously used this on the 412, suggest the same? Lots of caps for since a small component 
[attached file: IMG_51C1EE88-6886-4AEC-B6AC-6674D33C7F70.jpeg]

[M18] AI (2026-02-26 20:36):
Yep — **that decoupling approach is the right idea**, and I’d do essentially the same *style* of thing for any of these analog switches.

What you’re doing in that screenshot (for the DG412) is basically:

- **Local HF decoupling (100 nF)** close to the IC pins
- **Local bulk (a few µF)** to keep the rails stiff during switching transients
- Doing it on **both rails** (V+ and V−) plus the **logic rail (VL)**

That’s exactly what you want.

## Why “lots of caps” for a tiny switch IC?
Because the switch momentarily **dumps/steals charge** from its supply rails when it changes state (gate drive + parasitic C’s). If the supply impedance is high (long traces, shared rails, thin pours), that transient shows up as:
- extra **glitch / feedthrough** onto your analog node
- extra **charge injection error**
- sometimes even logic misbehaviour if VL bounces

So, yes, the caps are cheap insurance.

## What I’d recommend (practical, layout-driven)

### If you keep **±5 V rails** (as your screenshot shows)
Do this per switch IC:

- **V+ to 0V:** 100 nF (X7R) *right at the pin*  
- **V− to 0V:** 100 nF (X7R) *right at the pin*  
- **Bulk:** 1–4.7 µF on V+ to 0V and 1–4.7 µF on V− to 0V (can be one of each per IC or one pair shared per small cluster if placement is still tight)
- **VL to 0V:** 100 nF right at VL pin (and optionally 1 µF if your logic rail is noisy)

Optional but sometimes helpful:
- **Small cap across V+ to V−** (e.g., 10–100 nF) *if* your ± rails are “floating-ish” or long-fed. Don’t do this blindly if your rails have sequencing/soft-start quirks, but in many mixed-signal boards it reduces differential rail bounce.

### If you move to **MAX4648 at ~25–30 V analog**
Then it’s the same pattern, just adapted:

- **VDD (high rail) to 0V:** 100 nF right at the pin  
- **+ a local 1 µF (or 2.2 µF)** close by (your “bulk”)
- **VL to 0V:** 100 nF at the pin

If you’re running it **single-supply at 30 V**, I’d bias toward **one good 100 nF + one 1 µF** per IC, placed tight, and not worry about stacking multiple 4.7 µF unless the 30 V rail is long/skinny/shared with other fast loads.

## Placement rule that matters more than values
- Put the **100 nF** so the loop **pin → cap → ground → pin** is as tiny as possible (short trace, one via to solid plane).
- Bulk cap can be a bit further away, but still “local”.

So: **yes, suggest the same concept**. If anything, for the clamp/glitch sensitivity you’ve got, I’d *keep* the local 100 nFs even if it feels excessive.

If you tell me which way you’re powering the replacement switch (**±5 like before** vs **single 30 V**), I’ll give you an exact “minimal cap set” that’s sensible and not overkill.
