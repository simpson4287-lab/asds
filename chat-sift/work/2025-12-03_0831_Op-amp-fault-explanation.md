# Op amp fault explanation
Date (UTC): 2025-12-03 08:31
Conversation ID: 692ff518-2a78-8326-bc38-c3c8b6cca909
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-001.json

[M1] ME (2025-12-03 08:31):
I’ve got a fault on op amp ic circuit where the non inverting pin slowly charges up when I hold I meter on it. 

[M2] AI (2025-12-03 08:32):
What you’re seeing is **almost certainly not a “mystical fault” in the IC**, but the combination of:

- A **very high-impedance op-amp input**, plus  
- The **input bias current of the op-amp**, plus  
- The **input resistance & capacitance of your meter**  

…all acting together like a tiny **RC integrator**, so the node “slowly charges up” when you touch it with the meter.

---

## What’s probably happening

1. **The op-amp input is effectively floating or near-floating**

   - If the non-inverting pin isn’t tied firmly to a low-impedance source (e.g. sensor, reference, or small resistor to ground / mid-rail), then it’s *very* high impedance.
   - A high-impedance input + any stray capacitance = a node whose voltage can drift or charge with almost no current.

2. **Your meter has ~10 MΩ input resistance (in voltage mode)**

   - When you put a DMM on that node, you’ve effectively connected a **10 MΩ resistor to ground (or to the other probe node)**.
   - The op-amp’s **input bias current** (often tens of nA to a few µA depending on the device) flows through that big resistance.
   - That current charges the **input capacitance** (the op-amp input plus any PCB stray C) so the voltage ramps slowly instead of jumping.

   Rough idea:  
   - Say Ibias ≈ 50 nA and meter Rin ≈ 10 MΩ → Ibias × Rin ≈ 0.5 V  
   - With some pF–nF of capacitance, that 0.5 V might **appear slowly** over a second or more = “it charges up when I hold the meter on it.”

3. **If the meter is in resistance / continuity / diode mode**

   - In those modes the meter **injects its own test current** into the node.
   - On a high-impedance op-amp input, that test current will **force the input voltage to move**, again charging any capacitance and making it look like a slow charge ramp.
   - This can be even more pronounced and confusing than voltage mode.

4. **Op-amp behaviour with a floating input**

   - A floating non-inverting input will often cause the op-amp output to **rail** (go near + or – supply).
   - When you touch it with a meter, you’re giving it a defined (but very weak) path, so the input and output wander to some “random” level that can slowly change.

---

## How to tell if it’s a *real* fault

This behaviour **alone** does *not* prove the IC is bad. It’s actually quite normal in a high-impedance node.

You should start to suspect an actual IC fault only if:

- With the input **properly biased** (e.g. tied via a moderate resistor to a known voltage), the node still behaves wildly, or  
- The op-amp **output** is stuck at a rail even when both inputs are clearly within normal common-mode range and correctly biased, or  
- The supply currents or chip temperature suggest something is shorted internally.

---

## How to measure this node properly

To get a sensible reading and avoid the slow “charging” effect:

1. **Give the input a defined bias path**
   - Tie the non-inverting input to a reference using a **moderate resistor** (e.g. 10 k–100 k) instead of leaving it effectively floating.
   - Example: non-inverting pin → 47 k → mid-supply reference (or ground, depending on your design).

2. **Measure in DC voltage mode only**
   - Don’t use resistance / continuity / diode mode on that pin – those inject current.
   - Use the meter’s regular **VDC range**.

3. **Check the output at the same time**
   - If you bias the non-inverting input to, say, 2.5 V and configure the op-amp as a unity-gain follower, the output should sit very close to 2.5 V.
   - If it does, the op-amp is most likely healthy.

4. **If the impedance must be very high in your design**
   - For true high-impedance nodes (sensor inputs, integrators, etc.), use:
     - A **scope probe** with 10 MΩ / low capacitance,
     - Or add a **buffer stage** (another op-amp as a follower) to give you a low-impedance measurement point.

---

## Quick checklist for your fault-finding

- [ ] Is the non-inverting input connected to a **real source or reference**, not effectively floating?  
- [ ] Are you measuring in **voltage mode**, not continuity/ohms/diode?  
- [ ] Does the op-amp output behave correctly when you **apply a known DC input**?  
- [ ] Is there any large capacitor from that node to ground or another node that would accentuate the slow RC charge?

If you want, describe how that non-inverting pin is wired (e.g. “+ input via X k to Y V reference, feedback from output, etc.”), and I can walk through what voltage you *should* see and how to confirm whether the IC is actually bad.

[M3] ME (2025-12-03 08:33):
Bits it’s zero on the other board, which is healthy: both boards have suffered from faults in these circuits so I’m thinking there is still a path somewhere that’s at fault 

[M4] AI (2025-12-03 08:33):
Gotcha – that extra detail changes things quite a bit.

If the **healthy board’s non-inverting pin sits rock-solid at 0 V** under the same conditions, but the **suspect board slowly creeps up when you probe it**, that *does* point to a real leakage/path difference, not just “normal high-impedance weirdness”.

Think of it as: same circuit + same meter + same measurement method, but different behaviour → **something on that bad board is different**.

---

## What that slow “charge” usually means *when only one board does it*

On the dodgy board you almost certainly have **one of these**:

1. **Damaged op-amp input structure**
   - The internal ESD / clamp diodes from the input pin to the supply rails can become **leaky** after a fault.
   - That gives you a tiny but real current into the pin, which, together with the meter and any capacitance, makes the voltage slowly ramp.

2. **Leaky external part on that node**
   - e.g. a **protection diode, TVS, or small capacitor** from that input to some other node/rail that has been stressed.
   - After an overvoltage/transient, these can turn into a **high-value resistor** instead of being an open circuit.
   - That leakage feeds current into the input node and you see the “charge-up” when you watch it with a meter.

3. **PCB leakage / carbon tracking / flux**
   - If that area saw heat, sparks, or contamination, the board itself can have **megohm-range leakage** between traces.
   - That’s enough to nudge a high-impedance node like an op-amp input.

Because the other board behaves cleanly, the “just input bias + meter” explanation is much less convincing here. It’s much more likely there’s **extra unintended resistance to some rail or signal** on the bad one.

---

## Concrete tests to pin it down

### 1. Power-off resistance comparison

With power **off** on both boards:

1. Put meter in **resistance** mode.
2. On the good board, measure resistance from the non-inverting pin to:
   - +V rail  
   - –V rail  
   - Ground  
   - Any nearby reference node it is *supposed* to be tied to via a resistor  
3. Repeat the exact same measurements on the bad board.

You’re looking for a **clear difference** – e.g.:

- Good board: >20 MΩ everywhere (or only the expected resistor value)  
- Bad board: maybe 200 kΩ or 2 MΩ to one of the rails or another node.

If you see a noticeably lower resistance on the bad board, you’ve found the **leakage path direction**.

---

### 2. Is it inside the op-amp or outside?

To separate “IC is damaged” vs “something on the PCB is leaky”, do this on the bad board:

**Option A – lift the input pin (best diagnostic)**  
- Desolder and slightly lift the **non-inverting pin** of the op-amp so it no longer connects to the pad/track.
- Then:

  - Measure the **pin itself** (still on the op-amp package) with the meter.
    - If it still slowly charges → **input stage of the op-amp is damaged**.
  - Measure the **pad/track on the PCB** separately.
    - If *that* slowly charges or shows low resistance to a rail → the **leak is on the PCB or in other parts**, not the op-amp.

**Option B – swap the ICs between boards (if practical)**  
- Move the op-amp from the “good” board to the “bad” board and vice versa.
- If the fault **moves with the chip**, it’s the IC.  
- If the fault stays with the PCB, it’s external (part/board).

---

### 3. Suspect parts checklist on that node

Look at **everything directly connected** to that non-inverting pin on the schematic and PCB:

- Any **series resistor** into the pin
- Any **capacitor** to ground, to output, or to some reference
- Any **clamp diode / BAT / TVS** to rails or to another signal
- Any **RC network** for filtering

On the bad board:

- Temporarily **lift one leg** of each suspect component (one at a time) and see if the slow-charging behaviour **disappears** when you measure the pin.
  - If lifting a capacitor or diode suddenly makes the pin behave like the good board → that part was leaky / damaged.
- If you lift them all and the behaviour is still there, you’re back to:
  - Op-amp input itself, or  
  - PCB leakage.

---

### 4. Clean and inspect the PCB

Because you’ve had **faults in these circuits before**:

- Inspect the area under good light / magnification for:
  - Tiny darkened spots between tracks (carbonised FR-4)
  - Solder “whiskers”
  - Dried flux bridges, especially between input node and nearby rails.
- Thoroughly clean with **IPA and a toothbrush**, let it dry, then re-test.
  - If behaviour improves or disappears, you had **surface leakage**.

---

## How I’d sequence this in practice

1. **Compare resistance to rails** (power off, good vs bad board).
2. If difference exists, note *which rail* it’s leaking toward.
3. **Lift the op-amp input pin** on the bad board:
   - If pin alone is weird → replace op-amp.
   - If pad/track is weird → hunt components / PCB leakage.
4. One-by-one **lift external parts** on that node to see which one is feeding the leak.
5. Clean and visually inspect if nothing obvious shows up.

---

If you tell me roughly what that non-inverting input is connected to (e.g. “+ input has a 47 k to mid-rail reference, 1 nF to ground, and a BAT54 to +5 V”), I can point to the **most likely single culprit** in that network so you don’t have to shotgun everything.

[M5] ME (2025-12-03 08:46):
Definitely higher resistance on the bad board. Supply rails 700k. The good board they are 300-400k

[M6] AI (2025-12-03 08:46):
Nice, that measurement is actually a really helpful clue.

You’ve basically just proved this:

- **Bad board → higher resistance (≈700 kΩ to rails)**  
- **Good board → lower resistance (≈300–400 kΩ to rails)**  

So the bad board is *more* isolated from the rails, i.e. **more high-impedance / more “floating”**, not more leaky.

That fits **perfectly** with the behaviour:

- Good board: node has a stronger DC path → it sits solid at 0 V, doesn’t wander when you put the meter on it.  
- Bad board: node has lost some of that DC path (open / cracked resistor, bad joint, broken track, or damaged input structure) → it’s more floating, so the tiny bias currents + meter load slowly “charge” it.

So: the fault is now most likely a **missing or weakened DC bias path**, not an extra leakage path.

---

## What this likely means in real terms

On the **bad board**, one of these is probably true:

1. **A bias resistor has gone high or open**
   - e.g. a resistor from the non-inverting pin to:
     - Ground  
     - Mid-rail reference  
     - Some other DC reference  
   - If that resistor is cracked, half-lifted, or cooked by a previous fault, the effective resistance to the rails goes up → your 700 kΩ reading.

2. **A track or via has gone open**
   - The resistor itself might still measure fine end-to-end, but the **connection from the op-amp pin to that network** is broken.
   - Result: the pin sees only some weak, secondary path (e.g. through another resistor chain), so your meter sees a larger total resistance than on the good board.

3. **Op-amp input structure partly damaged (open-ish)**
   - Less common than “resistor open”, but the internal ESD / protection network could be **less connected** to the rails than on the good one.
   - That also increases the measured resistance and makes the node floatier.

---

## How to home in on it quickly

### 1. Compare to the *intended* bias node, not just the rails

Look at the schematic: what DC network should bias that non-inverting pin?

For example, if it’s meant to be:

- + input → 100 k → ground  
- + input → 200 k → reference, etc.

Then, with **power off**:

1. Measure on the **good board**:
   - Resistance **from + input to ground**  
   - Resistance **from + input to the bias/reference node**  
   - These should correspond (roughly) to known resistor values / parallel combos.

2. Do the **same on the bad board**:
   - If one of those is **higher or open** on the bad board → that’s exactly where the fault is.

---

### 2. Buzz the actual bias resistor(s)

For every resistor that touches the non-inverting pin:

1. Measure the resistor **in-circuit** on the good board versus the bad board.
2. If the values look about right, also:
   - Put one probe on the **op-amp pin** itself,  
   - Other probe on the **far end of that resistor**.
   - You should read **close to the resistor value**.
   - If it’s way higher or open on the bad board but not on the good → there’s a cracked joint or track in between.

---

### 3. Check the op-amp itself vs the PCB

If you want to separate “IC vs board”:

- Gently **lift the non-inverting pin** on the bad board:
  - Measure resistance from that lifted pin to the rails:
    - If now it matches the good board’s value → the PCB/network is the issue.
    - If it’s still “odd” → the IC’s input structure is different → likely damaged.

(Or simpler but more work: swap op-amps between boards and see if the weird behaviour follows the chip.)

---

## Why the slow charging happens *more* on the bad board

With that higher resistance, you’ve effectively:

- Reduced the DC “anchor” on the node, so it’s **free to drift**.
- Even a tiny **bias current** (or meter current) flowing into a few pF of capacitance will cause the voltage to rise or fall over seconds.
- On the good board, the stronger bias (300–400 kΩ total) holds it near 0 V and swamps that tiny current.

So the symptom + your resistance readings are 100% consistent with:

> **“Something that should be tying this input down has gone weak or open on the bad board.”**

---

If you tell me *roughly* what that + input is connected to in the schematic (e.g. “47 k to ground, 100 k to 2.5 V ref, 1 nF to ground”), I can even suggest **which exact resistor / link is most suspicious** so you can go right to it instead of hunting the whole area.

[M7] ME (2025-12-03 09:22):
The non inverting I put to ground on good board is stable 10k. On the bad board it does a small charging effect in the negative domain and then after 2-3 seconds becomes stable at 54k

[M8] AI (2025-12-03 09:23):
Nice, that 10 k vs 54 k detail is *exactly* what we needed.

### What your measurement is really telling us

- **Good board:**  
  Non-inverting pin → ground = **stable 10 kΩ**  
  → The pin is seeing its intended **10 k bias to ground** directly.

- **Bad board:**  
  Non-inverting pin → ground:
  - First you see a little “charging” (that’s your meter injecting a small current and charging some capacitance via a big resistance).
  - Then it settles at **≈54 kΩ**.

54 k is *not* a random number. It’s very close to **10 k + ~47 k** in series. That strongly suggests:

> From the *pin’s point of view*, the direct 10 k path to ground is gone or bypassed, and you’re now measuring a **longer, more convoluted path** that includes *another* resistor around 47 k.

In other words, the bad board’s input is **more floating** and only tied to ground via some indirect series path (e.g. through feedback / other bias resistors / op-amp internals), not directly via the 10 k like the good board.

That’s exactly why it “charges” and wanders when you touch it: very high effective impedance + a bit of capacitance + meter current.

---

### Likely fault types

On the **bad board**, one of these is almost certainly true:

1. **The 10 k bias path from the pin to ground is broken**
   - Cracked / cooked 10 k resistor
   - Dry joint at the op-amp pin or resistor pad
   - Broken track / via between pin and that resistor

2. **The pin has been “rerouted” by damage**
   - Internal damage in the op-amp input structure so the pin currents now flow via some other node (e.g. another input, feedback node) that eventually sees ground through ~47 k.

Either way: **the pin no longer has a clean 10 k to ground**.

---

### How to nail it in a few targeted checks

All with **power off**.

#### 1. Measure the actual 10 k resistor

On both boards, measure directly across the 10 k bias resistor pads:

- Good board: should be ~10 k.
- Bad board: check if it’s still ~10 k.
  - If it’s way off or open → replace it.

#### 2. Check continuity from pin to the 10 k

On the **bad board**:

- Put one probe on the **op-amp non-inverting pin** (the leg itself).  
- Put the other probe on the **10 k pad that’s supposed to connect to that pin**.

You should see **almost 0 Ω** (a fraction of an ohm). If instead you see:

- **kΩs or “OL”** → there’s a broken track, cracked via, or bad solder joint between the pin and the resistor.

If you find that:

- Reflow the pin and that resistor pad (add a touch of fresh solder).
- If still no joy, run a **thin jumper wire** from the op-amp pin straight to the resistor pad to bypass the broken copper.

#### 3. Confirm the other side of the 10 k is really ground

Still on the **bad board**:

- Measure from the **ground side** of the 10 k to a known ground point (ground test pad, big ground pin of a connector, large ground pour).
- It should be effectively **0 Ω**.
- If that’s not the case, the 10 k may be sitting on a “ground island” that lost its connection to the main ground.

---

### About the “negative domain / charging effect”

That weird behaviour (a brief negative reading or wandering value that stabilises after 2–3 s) is just:

- The meter pushing a **tiny test current** through
- A **large effective resistance (~54 k)** and
- Some **capacitance on that node**

→ classic RC charge/discharge. Perfectly in line with “this node is now *much* higher impedance than the good board and no longer clamped by 10 k”.

---

### Summary

- Good board: non-inverting pin has a solid 10 k to ground → stable, well-behaved.
- Bad board: effective path from pin to ground ≈54 k and shows RC charging → the intended 10 k bias **is not properly connected** to the pin.
- Most probable fix: **restore that 10 k path** (resistor, solder joints, or track/via; jumper if needed).

If you can tell me the actual resistor values in that input network (e.g. “10 k to ground, 47 k in feedback, etc.”), I can even say “it’s almost certainly this exact Rxx link that’s open” – but even without that, the continuity test pin ↔ 10 k pad is your fastest next step.

[M9] ME (2025-12-03 09:27):
[image]
There is no tok resistor. The circuit looks like this. I removed ic6, c4 
[attached file: A4049482-EF6E-4F97-9080-B4D074FDA863.jpeg]

[M10] AI (2025-12-03 09:31):
Ahh, that helps a lot – I recognise this bit of the schematic now.

So, in words, that node coming from the left is fanned out through:

- R81 / R298 / R304 = **0 Ω links** into the three ADA4817 stages (x1, x2, x4)  
- On some of those stages you’ve got a **330 Ω to 0 V** (R297, R303) on the *same node* as the non-inverting input  
- IC6 and C4 just sit upstream as a switch + AC-coupler, and you’ve removed both.

So right now that input node is basically:

> “left bus” → 0R link → **non-inverting input of ADA4817** (+ any 330 Ω to ground if that resistor is fitted).

There is **no 10 k resistor** in the schematic, so the “10 k to ground” you saw on the good board is just the ohmmeter looking into the op-amp input structure and the surrounding network – not an actual 10 k part.

Given that:

- Good board: +IN to 0 V reads **stable ~10 k**  
- Bad board: +IN to 0 V gives a little **RC-ish movement in the negative direction, then settles at ~54 k**  

…and you’ve already isolated the node from IC6 and C4, the only things left that can explain the difference are:

1. **The ADA4817 input itself on that board is damaged / different**, or  
2. **The local bias network into that pin (0R link, 330R to ground, tracks/vias) is cracked or open** so the meter is seeing it through some indirect path.

Because both readings (10 k and 54 k) are completely different from what the bare resistor network would give, the op-amp input is definitely in the game here.

---

## What I’d do next (concrete steps)

All with power **off**.

### 1. Measure at two places: pin vs bus

Pick the suspect channel’s ADA4817:

- Measure **from the pad/bus just *before* the 0 Ω link (R81 / R298 / R304)** to 0 V.
- Then measure **from the actual non-inverting pin pad** (right on the IC leg) to 0 V.

Do this on **both** boards.

If on the bad board the value changes noticeably between “bus” and “pin”, then the 0R link or its solder joints / track are suspect.

---

### 2. Check the local ground resistor(s)

For the channel you’re probing:

- Find the resistor that ties that node to 0 V (e.g. R297 or R303 on your print).  
- Measure directly across that resistor on both boards:
  - It should be around its nominal value if fitted (e.g. 330 Ω).
- Then put one probe on the **non-inverting pin**, the other on 0 V.  
  - If you don’t see roughly that resistor value (plus a bit), there is a broken connection between pin and resistor or between resistor and ground.

If those resistors are actually **“NNF” (not fitted) in this build**, then the *only* DC path is through the op-amp input itself – which makes the difference between 10 k and 54 k almost certainly **inside the chip**.

---

### 3. The definitive test: pull the ADA4817

On the **bad board**, desolder that ADA4817 (just the channel you’re measuring):

- With the IC **removed**, measure the resistance from the now-empty **+IN pad to 0 V**.
  - If it now reads something sensible and stable (or very high) and the odd “charging then 54 k” behaviour is gone, then the ADA4817 input structure was providing that weird path.
  - If it *still* does the same thing with the IC gone, there’s a sneaky path on the PCB (other components or contamination).

Given that you’ve already isolated IC6 and C4, if pulling the ADA4817 makes the behaviour disappear, it’s pretty safe to call that op-amp **toast**.

---

## Why the numbers are different between boards

With this topology and no explicit 10 k, the ohmmeter is really measuring:

> “whatever DC path the ADA4817’s input protection / bias network + stray resistors + any fitted R297/R303 give you, **as seen through the meter’s test current**”

On a healthy input that might look like ~10 k; on a stressed or partially zapped one, some junctions go leaky or open and the apparent resistance shifts to 50 k, 100 k, etc, and you see that **little RC wobble** as the meter charges the node through a much higher effective resistance.

So:

- The **good** board’s “nice, stable 10 k” is just its particular healthy silicon + fitted parts.  
- The **bad** board’s “drifts then settles at 54 k” is a big red flag that the **input path is different** – most likely a damaged ADA4817 on that channel, or a cracked connection in its immediate resistor network.

---

If you tell me exactly which of the three channels (x1 / x2 / x4) you’re probing and which resistors are actually stuffed on your build, I can point at the *most likely single component* to replace first – but from what you’ve shown so far, I’d put decent money on that ADA4817 input having taken a hit.

[M11] ME (2026-01-11 17:17):
What was the filter we discussed?

[M12] AI (2026-01-11 17:17):
In this section of the schematic, the “filter” we were implicitly talking about is the **small RC low-pass formed at the op-amp non-inverting input by the series feed resistance into the pin and the shunt capacitor footprint to 0 V**.

On your drawing that corresponds to:

- **Series element into +IN:**  
  - For x2 and x4 you have **330 Ω** in the feed path (e.g. R296/R302 shown as 330 Ω / 1 k depending on the channel).  
  - For x1 it looks like **0 Ω** links are used (R81 etc.), so there is effectively no series R unless you populate an alternative.

- **Shunt capacitor to 0 V at the +IN node:**  
  - The capacitors marked **NNF** (not normally fitted) and the one labeled **C74** in the x1 block are the “C to ground” option at that node (same idea for C179 / C181 in the x2/x4 blocks).

So the filter is: **R (series) + C (to ground) → single-pole low-pass** at the non-inverting input.

If you fit it, the corner frequency is:

\[
f_c = \frac{1}{2\pi R C}
\]

Examples (just to anchor it):
- R = 330 Ω, C = 1 nF → \( f_c \approx 482 \text{ kHz} \)  
- R = 330 Ω, C = 10 nF → \( f_c \approx 48 \text{ kHz} \)

If you want, tell me what value C74/C179/C181 are (or intended to be) and which channel (x1/x2/x4) you mean, and I’ll give you the exact pole and what it’s doing in terms of stability/noise/bandwidth.
