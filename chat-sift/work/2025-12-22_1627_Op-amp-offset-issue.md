# Op amp offset issue
Date (UTC): 2025-12-22 16:27
Conversation ID: 69497158-bc08-8328-9db6-4e3198f1a817
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-002.json

[M1] ME (2025-12-22 16:27):
I have a 15mv offset between op amp input pins. Is this an issue

[M2] AI (2025-12-22 16:27):
It *can* be an issue — but whether it matters depends on **(1) what op-amp**, **(2) your closed-loop gain**, and **(3) what your circuit is trying to measure**.

### What a 15 mV “between input pins” usually means
That’s effectively an **input offset voltage** (plus any bias-current-through-resistors effects, plus measurement error). In a closed-loop circuit, that offset gets “amplified” into an output error.

A good rule of thumb:
- **Output offset ≈ Input offset × (Noise gain)**  
  - For **non-inverting** gain \(1 + R_f/R_g\): noise gain = closed-loop gain  
  - For **inverting** gain \(-R_f/R_{in}\): noise gain = \(1 + R_f/R_{in}\)

Example: if noise gain = 101, then  
- 15 mV × 101 ≈ **1.5 V** of output error (big deal)

If noise gain = 2, then  
- 15 mV × 2 = **30 mV** at the output (maybe fine, maybe not)

### When 15 mV is a red flag
- You’re doing **precision DC**, sensor conditioning, ADC front ends, current sense, or anything expecting millivolt accuracy.
- You have **high gain** (even moderate gain can make it significant).
- The output is **near a rail** or you’re losing headroom / saturating.
- It changes a lot with **temperature** (suggests drift or something else going on).

### When it might be totally fine
- It’s an **audio / AC-coupled** stage and the DC offset is blocked later.
- You only care about relative changes and you can **calibrate out** DC error.
- Gain is low and the downstream system tolerates tens of mV at the output.

### Things that commonly *masquerade* as “op-amp offset”
If you measured 15 mV with a DMM across the inputs while it’s in-circuit, that number can be distorted by:
- **Input bias currents** flowing through mismatched source resistances
- **Input common-mode range** being violated (op-amp behaves weird)
- **Output saturation** (inputs can sit “wrong” when railed)
- **Thermoelectric voltages** (dissimilar metals, temp gradients) — usually µV–mV but can surprise you in sensitive setups
- **Meter loading / ground reference mistakes**

### Quick sanity checks you can do
1. **Is the output railed or close to a rail?** If yes, fix that first.
2. **What is your noise gain?** Multiply it by 15 mV and see if the implied output error matches what you observe.
3. **Swap the op-amp (same circuit)**: if it changes a lot, it’s probably op-amp offset / damage.
4. **Short the inputs together at the op-amp pins** (if safe for your circuit) and see what remains — that isolates “true” input offset vs external resistor/bias effects.

If you tell me:
- op-amp part number,
- configuration (inverting/non-inverting) + resistor values,
- supply rails,
- and what the output is doing,

…I’ll tell you immediately if **15 mV is expected**, **tolerable**, or **a sign something’s off**.

[M3] ME (2025-12-22 16:27):
As8063

[M4] AI (2025-12-22 16:28):
If you mean **AD8063** (often mistyped as “AS8063”): **15 mV between the inputs is not normal**.

The AD8061/AD8062/AD8063 datasheet lists **input offset voltage** as about **1 mV typical** and **6 mV max** (at 25 °C, across the supply conditions shown). citeturn3view0  
So **15 mV is >2× the max spec**, which usually means **you’re not measuring “true Vos”**, or the part/circuit is in a bad operating condition.

### Most common reasons you’ll “see” ~10–20 mV between inputs in-circuit
- **Output is saturated / near a rail** → the loop can’t correct, and the inputs can separate.
- **Input common-mode range violation** (AD8063 input CM range is limited near the positive rail) → offset/error increases a lot as you approach the headroom limit. citeturn2view0
- **Input bias current + resistor imbalance**: AD8063 bias current is **µA-level** (not nA), so with tens of kΩ you can easily create **many mV** of “apparent offset.” citeturn3view0
- **Measurement method**: probing directly across pins with a DMM while the amp is actively controlling can be misleading.

### Quick checks (fast)
1. **Is Vout pinned close to a rail?** If yes, fix headroom/load first.
2. **What are your input/feedback resistor values?** (If you’ve got, say, 10k–100k ranges, bias current effects can dominate.)
3. **What’s your supply and input common-mode level?** (Especially if single-supply and the inputs sit high.)

If you paste your config (inverting/non-inverting), resistor values, supply rails, and where the inputs sit (DC), I’ll tell you which of the above is most likely and what offset you *should* expect.

[M5] ME (2025-12-22 16:30):
[image]
What could it be? I’ve marked the points on the circuit with red dots. I’ve isolated it from the previous circuit by removing the relay. Ic42 was recently changed. But may have been stressed during hot air soldering.
[attached file: IMG_34B50C8B-48BE-4632-B2DC-C9CF6DD873F0.jpeg]

[M6] AI (2025-12-22 16:30):
Thanks for the schematic photo – that helps a lot.  
Short answer first: **yes, a damaged or marginal AD8063 (IC42) is a very plausible cause**, but there are **two other very common contributors in *this exact topology*** that can easily give you ~10–20 mV between the inputs even with a “good” device.

I’ll walk through it in a structured way, starting with the most likely.

---

## 1. Bias current + source impedance imbalance (very likely here)

This is the big one people underestimate with the **AD8063**.

Key facts:
- AD8063 input bias current is **µA-level** (not nA).
- You have **asymmetric source impedances** into + and − inputs.

Looking at IC42:
- **Non-inverting input (pin 3)** is fed via **R109 = 150 Ω** from −5 V and clamped by a zener.
- **Inverting input (pin 2)** sees **R32 = 150 Ω**, but *also* the feedback network and the downstream protection / clamp circuitry.

Even if both resistors are nominally 150 Ω, the **effective DC impedance is not matched**.

Order-of-magnitude check:
- Bias current ≈ 1–3 µA (typical for AD8063)
- ΔR of only **5–10 Ω effective mismatch** is enough:

\[
1\ \mu A \times 15\ \Omega = 15\ mV
\]

So:
- **15 mV across the inputs is entirely believable without a faulty op-amp**
- This is *especially* true because you’re sitting near the **input clamp / protection network**, not a clean mid-rail bias

👉 **Test**  
Temporarily:
- Lift R32 or R109 and replace both with **matched resistors (e.g. 100 Ω + 100 Ω to a quiet reference)**  
- Or short the inputs together *right at the op-amp pins* (only briefly, safe condition)

If the 15 mV collapses → it’s bias current, not damage.

---

## 2. Output headroom / common-mode stress (also very likely)

You’re running:
- **±5 V supplies**
- Inputs sitting around **−3 V**
- Output feeding protection, LPF, ADC front-end

The AD8063:
- Has **limited input common-mode range**, especially as you approach rails
- Loses linearity *before* it fully rails

If the output is:
- Loaded by the clamp network
- Slewing
- Or even lightly saturated

Then the loop opens slightly and the inputs **separate by millivolts to tens of millivolts**.

👉 **Test**
- Measure **Vout of IC42**
- If it’s within ~500 mV of a rail → input pin delta is *expected*
- Temporarily disconnect the downstream load (lift R293) and re-measure the input delta

---

## 3. Thermal / soldering damage (possible, but not my first bet)

Hot-air stress *can* damage AD8063s, but when it does:
- Offset is usually **way worse** (50–200 mV)
- Or it **drifts wildly** with temperature
- Or bias current skyrockets and the output pins hard

Your symptom (stable ~15 mV) actually looks **too “clean”** for a cooked die.

👉 **Quick confidence check**
- Gently warm IC42 with a finger or hot air at distance
- If the input delta shifts rapidly (several mV per second), suspect damage
- If it’s stable → circuit physics, not silicon failure

---

## 4. Measurement artefact (worth checking)

Measuring *between* op-amp inputs with a DMM:
- You’re inserting meter bias currents
- You’re measuring two high-gain nodes under feedback

Better:
- Measure each input **to ground**
- Subtract manually

You’ll often find the “15 mV” shrinks.

---

## What I would do next (in order)

1. **Measure Vout of IC42** and confirm it’s not near a rail  
2. **Short inputs together briefly at the pins** → does ΔV vanish?
3. **Lift R293** (disconnect ADC / LPF load) → does ΔV reduce?
4. **Swap IC42 again only if 1–3 don’t explain it**

---

## Bottom line

- **15 mV is high for AD8063 offset**
- **But it is completely believable in *this circuit* without a faulty op-amp**
- Bias current + impedance mismatch + clamp networks is the #1 suspect
- Hot-air damage is possible but not yet proven

If you want, next step I can:
- Calculate the *expected* input delta from your exact resistor network, or  
- Suggest a small tweak (one resistor or cap) to collapse that offset without redesigning the stage.

[M7] ME (2025-12-22 16:32):
V out is 58mv. This is an attenuation of the input to pin 3 non inverting of 73mv

[M8] AI (2025-12-22 16:32):
Got it. If **V+ (pin 3) = 73 mV** and **Vout (pin 6) = 58 mV**, then you’ve effectively got **~0.79× “gain”** (58/73). In a normal non-inverting stage with healthy negative feedback, you’d expect **V− (pin 2) to sit extremely close to V+** (typically within microvolts to maybe a millivolt or two for this kind of op-amp in a sane circuit).

So **15 mV input pin-to-pin is not “normal behaviour”** here unless **the loop isn’t actually in control**.

### The 3 most likely causes, given your numbers

#### 1) Feedback path not actually closing (most common)
Even a hairline crack / bad joint on **R32 / the trace from Vout back to pin 2** will do exactly this: the op-amp output drifts somewhere, and the inputs no longer “track”.

**Check:**
- Continuity from **IC42 pin 6 → through R32 → IC42 pin 2**
- R32 value in-circuit (150 Ω)
- Solder joints on pins **2 and 6** specifically

#### 2) Output is being *pulled* by the downstream network (clamp/LPF/ADC node)
Your op-amp output goes through **R293 (33 Ω)** into the “ADC_IN_05H” node with caps to ground and whatever the ADC input network is doing. If that node (or an external connection) is clamping/leaking, the op-amp can be forced to sit at a value that’s “too low” vs V+.

**Fast isolation test:**
- Temporarily **lift R293** (or disconnect the ADC node) and re-measure:
  - Vout
  - V+ (pin 3)
  - V− (pin 2)

If Vout jumps up to match V+ (and the 15 mV collapses), the issue is **downstream loading/clamp/leak**, not IC42.

#### 3) IC42 input stage damaged (plausible with hot air, but verify with the tests above)
If feedback is confirmed good and downstream load is removed and you *still* see ~15 mV between pins, then yes: **IC42 is suspect**.

### One key measurement that will decide it
Please measure **V− (pin 2) to ground** (same reference as the others).

- If **V− ≈ Vout** (e.g., ~58 mV) while **V+ = 73 mV** → feedback is working *as wired*, but you’ve got either **a deliberate attenuator topology** you’re not accounting for, **or** the output/feedback node is being dragged.
- If **V− is floating / not near either** → broken feedback / bad joint is very likely.

If you tell me what **pin 2 measures** (and whether lifting **R293** changes anything), I can pin this down to “feedback fault vs load clamp vs dead op-amp” with high confidence.

[M9] ME (2025-12-22 16:35):
V- tracks the output, 58mv

[M10] AI (2025-12-22 16:35):
That’s a really useful result.

If **V− = Vout = 58 mV**, your **feedback loop is intact** (at least at DC): the inverting input is doing what it should.

So the “problem” is simply:

- **V+ (pin 3) = 73 mV**
- **Vout/V− = 58 mV**
- **Δ = 15 mV**

In a unity follower, Vout should sit *very* close to V+. A steady 15 mV gap usually means one of these is true:

## 1) Pin 3 isn’t actually being driven (most likely given you removed the relay)
With the relay removed, the node feeding **pin 3** may be **floating** or only weakly biased/leaking through the clamp/bias network (R109/D3 etc.). A floating non-inverting input can happily sit at “some” millivolts that look real on a DMM, but it’s not a solid reference the op-amp can follow accurately.

**Quick proof:** temporarily force pin 3 with a low-impedance source:
- Tie **pin 3 to 0 V** through **~100 Ω to 1 kΩ** (or directly if you’re confident it won’t fight anything).
- If the op-amp is healthy and not being dragged, **Vout should move to ~0 V** and the pin-to-pin difference should collapse to ~mV.

If it doesn’t: then look at (2) or (3).

## 2) Output is being pulled/clamped by the downstream network
Even with good feedback, if something after **R293 (33 Ω)** is leaking/clamping to ground or another rail, it can “pin” the output node and you’ll see V− tracking that pinned output.

**Fast isolation test:** lift **R293** (disconnect ADC/LPF load) and re-measure.
- If Vout snaps up to match V+ (and the 15 mV disappears), the fault is **downstream loading/clamp/ADC input**.
- If nothing changes, go to (3).

## 3) IC42 damage (possible, but only after the above tests)
If pin 3 is definitely driven low impedance and the output load is disconnected, yet you still see ~15 mV error, then **IC42 is suspect** (offset/bias damage from heat/ESD).

If you tell me one thing: **with R293 lifted, what are V+ and Vout?**  
That single test will basically pinpoint whether it’s “downstream pull” vs “IC42 / pin3 drive issue.”

[M11] ME (2025-12-22 17:27):
But when the relay was in circuit those voltages were finding there way back to earlier circuits. By removing the relay the earlier circuits are fine. All nodes around if 42 should be close to 0mv.son this offset is likely coming from the output 

[M12] AI (2025-12-22 17:27):
Yep — with what you’ve described, it’s very likely the **58 mV is being generated at (or pulled onto) IC42’s output node**, and because **V− tracks Vout**, that 58 mV then becomes “the truth” for the whole feedback loop. The **15 mV gap** is simply the op-amp failing to pull Vout all the way to wherever V+ happens to be sitting (73 mV), because something is **biasing/clamping/leaking** the output node.

Given your schematic, there are only a few realistic ways the output can get “pinned” to ~tens of mV:

## Most likely causes (in your exact circuit)

### 1) Downstream load/leak via the ADC/LPF node
IC42 output goes through **R293 (33 Ω)** to **ADC_IN_05H**, with caps to ground (C109/C204) and whatever the ADC input structure is doing. Any of these can create a small DC bias:
- ADC input leakage (especially if powered weirdly / not at same ground / or clamped)
- Something else connected to ADC_IN_05H injecting current
- Flux residue / contamination around that node causing a µA-scale leak → tens of mV across 33 Ω is easy

**Best test:** lift **R293**.  
If Vout collapses to ~0 mV, the “offset” is not IC42, it’s **everything after R293**.

### 2) The clamp/zener network around the inputs is leaking
You’ve got **D3 (BZX55-C3V0)** tied to the pin-3 node (through R109 to −5 V). Zeners can leak, and after heat they can leak more. A microamp of leakage through 150 Ω / clamp paths can set a small bias that the op-amp then “follows” imperfectly.

But your key clue is: **earlier stages got dragged only when the relay was in**. That screams “a DC bias or leakage current from this stage was back-feeding through the relay path”.

### 3) IC42 itself has output bias/offset (possible)
If IC42 has been stressed, it can develop:
- higher input bias current
- higher offset
- output stage leakage / crossover weirdness around 0 V

But I’d still prove (1) first because it’s the classic: “op-amp seems off by ~50 mV” → actually the ADC/clamp network is injecting current.

## A simple way to think about it
Because you measured:
- **V− = Vout**
the loop is behaving: it’s trying to force V− = V+.  
But it can’t get there. That usually means:

- **The output node is being held** (by load/clamp/leak), OR
- **The op-amp is too weak/unhappy around that operating point**, OR
- **V+ isn’t really 73 mV (it’s a floating/leaky reading)**

## The 2 killer isolation checks (do these and you’ll know)

### A) Lift R293 (disconnect ADC_IN_05H)
Re-measure:
- Vout
- V+
- V−

**Outcomes**
- **Vout goes to ~0 mV** → fault is downstream of R293 (ADC/clamp/leak/contamination)
- **Vout stays ~58 mV** → fault is local to IC42 / its immediate feedback/input network

### B) Force V+ hard to 0 V (low impedance)
Temporarily tie pin 3 to ground through ~100 Ω–1 kΩ.
- If Vout still sits at ~58 mV → output is being pinned or IC42 is damaged
- If Vout follows to ~0 → your 73 mV at V+ was just a weak/floating/leaky bias

## Why the relay mattered
With the relay in, whatever small DC bias current exists at IC42’s node(s) had a path back into earlier circuitry. Removing the relay removed that backfeed path — exactly consistent with **a leak/bias source in this stage** (often “after R293” or around the clamp network).

If you do just one thing next: **lift R293 and tell me what Vout becomes.** That will cleanly separate “ADC side pulling it” from “IC42 / local network”.

[M13] ME (2025-12-22 17:28):
But there’s a series dc block
Via the capacitor from ic42 output to adc input 

[M14] AI (2025-12-22 17:28):
Right — **if the ADC is truly only connected through a *series* coupling cap**, then (in an ideal world) it **can’t impose a DC load back onto IC42’s output**.

But two important gotchas apply here:

### 1) The “DC block” might be *after* the point that’s being biased
In your snippet, IC42’s output is still directly connected (at DC) to:
- the **feedback path** (since V− tracks Vout)
- any **shunt components to ground on the op-amp side** (e.g., the 56 pF to 0 V you’ve got at that node)
- any **clamp / protection parts** that touch that node (directly or via small resistors)
- leakage paths from contamination/flux

So even if the ADC input is AC-coupled, the **op-amp output node can still sit at tens of mV DC** because of *local* leakage/bias currents.

### 2) Real capacitors aren’t perfect DC isolators in fault conditions
Normally, film/NP0 leakage is tiny. But if:
- the cap is damaged,
- there’s flux/residue providing a path across pads,
- or the “ADC side” has ESD clamps to rails and you’ve got some unintended DC path around the capacitor,

…then you can still get a small DC bias current that creates **tens of mV** across small resistances (33 Ω / 150 Ω etc.).

---

## Given your measurements, what it most strongly implies
- **V− = Vout** means the loop is behaving normally.
- The **58 mV is effectively the loop’s DC equilibrium point**.
- That equilibrium is usually set by **input bias currents + leakage paths + any clamp networks**, not by the ADC if it’s genuinely AC-coupled.

So your instinct (“it’s likely coming from the output”) is fair — but I’d phrase it as:

> the output is where you *see* it, but the *cause* is typically a tiny DC current somewhere that forces the output to that value.

---

## Two decisive checks (fast, no guessing)

### A) Lift the coupling capacitor (the DC block) completely
If Vout stays ~58 mV with the cap removed, the ADC side is 100% innocent.

### B) Lift **R293 (33 Ω)** as well
Even with a coupling cap, there may be other connections on the “ADC node” side (test points, ESD, etc.). Lifting R293 isolates the whole downstream network.

**If Vout collapses** → something downstream is biasing it (even if not “through the cap” in the way you expect).  
**If Vout doesn’t change** → it’s local to IC42 / its input clamp/bias network / PCB leakage.

---

If you tell me which component is the “series DC block” part number on that drawing (I’m guessing it’s **C204**?), I can be more specific about which node is truly isolated and where the DC path still exists.

[M15] ME (2025-12-22 17:32):
C204

[M16] AI (2025-12-22 17:32):
Yep — **C204 is the series DC-block** (it’s in series from the node after **R293** to **ADC_IN_05H**). So **in a healthy build the ADC side can’t “pull” DC back into IC42 through C204**.

That means your **58 mV DC at Vout (and V−)** is almost certainly being set on the **IC42 side of C204**, by one of these:

## 1) There’s DC current through R293 into something to ground (most likely)
Even though the ADC is AC-coupled, the node **between R293 and C204** still has:
- **C109 to 0 V** (should be open at DC, but leakage/contamination can make it not-open)
- whatever else is connected to that node (test points, pads, residue, etc.)

### Do this measurement (it’s the fastest “smoking gun”)
Measure **both ends of R293**:
- **Pin 6 (Vout of IC42)** = you have 58 mV
- **Node between R293 and C204** (the “LPF node”)

**If there’s more than ~1–2 mV across R293**, that implies DC current:
\[
I \approx \Delta V / 33\Omega
\]
Example: 10 mV across R293 ≈ 0.30 mA of unwanted DC being sunk/sourced.

If you *do* see a drop, the usual culprits are:
- flux/ionic contamination around that node/cap pads
- a leaky/heat-stressed capacitor to ground (rare but possible)
- some other hidden connection on that net

## 2) C204 itself (or its pads) is leaking to the other side (possible)
In theory it blocks DC; in practice leakage across the component or across dirty pads can create a small DC path.

### Quick isolation
Temporarily **lift one end of C204**.
- If nothing changes at Vout → ADC side is innocent.
- If Vout shifts toward 0 → you’ve got leakage/alternate path via the ADC side.

## 3) Pin 3 isn’t truly “0 mV” (it’s sitting at 73 mV because of leakage/bias)
Since **V− follows Vout perfectly**, the “error” is that the op-amp is not making Vout = V+. That can happen if **V+ is a weak/floating node** (especially after removing the relay).

### Quick proof
Temporarily force **pin 3 to 0 V** with a **100 Ω–1 kΩ** resistor.
- A healthy, unloaded follower should drive **Vout ~0 mV**.
- If it stubbornly stays ~58 mV, something is pinning the output node (or IC42 is damaged).

---

### What I’d do in order (no desolder marathon)
1) Measure both sides of **R293** (is there DC drop?)  
2) Lift **C204** (rule out “DC block” leakage / alternate path)  
3) If still weird, lift **R293** (removes the whole LPF/ADC net from IC42 output)

If you tell me the **voltage on the LPF node (between R293 and C204)** and the **voltage on the ADC side of C204**, I can say exactly which branch is creating the DC bias.

[M17] ME (2025-12-23 05:44):
Ok, removed c204, still fault.
Removed the c109 to ground, still fault.
Measured across r293 (33r), 0v. So likely op amp fault?

[M18] AI (2025-12-23 05:44):
Given those results, **yes — IC42 is now the prime suspect**, or something **right at its pins / feedback network** is effectively “inside the loop”.

Your isolation sequence was exactly the right way to do it:

- **C204 removed** → ADC side cannot be influencing DC.
- **C109 removed** → shunt cap/leak to ground on the post-R293 node eliminated.
- **0 V across R293** → there’s essentially **no DC current** being sunk/sourced into the downstream node, so the output isn’t being “pulled” through R293.

So the **58 mV offset exists locally at IC42 and its immediate connections**, not downstream.

### What that leaves (in order of likelihood)

## 1) IC42 is damaged / out of spec
A healthy AD8063 in a unity-ish configuration should not sit with a stable **~15 mV input differential** at tens of mV output unless something is wrong. Heat/ESD during rework can absolutely do this.

**Strong tell:** does the 15 mV and/or Vout shift noticeably as IC42 warms by a few °C? If yes → even more likely the silicon is stressed.

## 2) The non-inverting input (pin 3) isn’t actually a solid 0 mV node
You said “all nodes around IC42 should be close to 0 mV”, but with the relay removed it’s easy for that node to be **weakly biased/floating**, and a DMM will still show “73 mV”.

**One decisive test:**
Temporarily force **pin 3 hard to 0 V** (e.g. clip lead to ground, or 100 Ω–1 kΩ to ground).
- If **Vout snaps to ~0 mV** and the pin-to-pin delta collapses → IC42 is probably OK; your pin 3 node is just not being driven.
- If **Vout stubbornly stays around ~58 mV** → IC42 (or its soldering/pins) is the issue.

## 3) Solder / pin integrity around pins 2, 3, 6
A tiny solder bridge, partial open, or damaged pad/via can create exactly this kind of “looks closed loop but isn’t behaving” symptom.

**Check with a meter (power off):**
- Pin 6 → R32 → pin 2 continuity and correct resistance
- Pin 3 to its source net continuity (and that it’s not unintentionally tied through residue)

### Quick “call it” move
If you can, **swap IC42 again** (ideally from a known-good reel) *after* cleaning the area (IPA + brush, dry well). Given everything you’ve ruled out, that’s now a rational next step.

If you tell me what the configuration is supposed to be at IC42 (is it intended as a **follower/buffer** with R32=150 Ω as a series isolator, or some other gain?), I can sanity-check whether 73 mV vs 58 mV could ever be “expected” in the intended topology. But based on your isolation tests: **op-amp damage or pin-node integrity** is where I’d bet.

[M19] ME (2025-12-23 05:45):
What I could do it strap that node where I have empty relay. There is a free pad to link to ground 

[M20] AI (2025-12-23 05:45):
Yes — that’s a really good, low-effort diagnostic.

If the relay used to connect the “previous stage” into IC42’s **pin-3 (non-inverting) node**, then with the relay removed that node can be **floating / weakly biased**, and your DMM can happily show ~73 mV that isn’t a stiff drive.

### What strapping it to ground will tell you
Use that free pad to **force the pin-3 node solidly to 0 V** (ground):

**Expected outcomes**

1) **Vout collapses to ~0 mV** (and V− follows it)
- ✅ IC42 is almost certainly fine
- The 73 mV was coming from a floating/leaky node (or bias current effects)
- The “fault” was backfeeding only because the relay reconnected that weak node into earlier circuitry

2) **Vout stays ~58 mV** (or barely changes)
- Strong evidence IC42 is faulty *or* there’s a local issue around pins 2/6
- Because with V+ hard at 0 V, a healthy closed-loop buffer should drive Vout to ~0

3) **Vout moves partway but not to 0**
- Suggests there’s still some DC bias path at the output node (less likely now given 0 V across R293), or pin-3 isn’t actually the same net you think it is.

### How to do it safely
- Don’t hard-short if you’re unsure what else is on that net.
- Best: strap to ground through **100 Ω to 1 kΩ** first.
  - If nothing complains and you want a stronger clamp, you can go lower or direct.

### Also measure these three voltages after strapping
- **Pin 3 (V+)**
- **Pin 6 (Vout)**
- **Pin 2 (V−)**

If you tell me what they become, we can call it confidently in one step.

[M21] ME (2025-12-23 05:51):
Ok. Tied that node to ground. The other side of r101 (33r) is 1-2mv. The output of the ic42 is -4.1. So feels like if fault

[M22] AI (2025-12-23 05:51):
Yeah — with **that node forced hard to 0 V**, an intact buffer/closed-loop stage should sit **very close to 0 V at the output**.

Seeing **IC42 output at −4.1 V** (i.e., hard toward the negative rail) is a strong sign that **the loop is no longer behaving normally**. At this point it’s *either* a **local connectivity fault** around IC42 (more common than you’d think after hot air), *or* **IC42 itself is damaged / wrong part / orientation issue**.

Here’s what your new measurements imply:

- The node on the far side of the **33 Ω** being **1–2 mV** says your “ground strap” is doing its job (that node is genuinely near 0 V).
- The fact the **output rails negative** means the op-amp is “deciding” the inverting input is *above* the non-inverting input (or the feedback isn’t actually closing as intended), so it drives hard negative trying to correct.

## Most likely causes now (in order)

### 1) Feedback path issue (open/poor joint) between output and V−
Even if it *looked* like V− tracked output before, after rework it’s very easy to have:
- a cracked pad/via
- an intermittent joint on **pin 2 / pin 6**
- a damaged or wrong-value **R32 (150 Ω)**

**Do this (power off):**
- Measure resistance **pin 6 → pin 2** and confirm it is **~150 Ω** (or whatever it should be through R32).
- Wiggle-test gently (probe pressure) while watching continuity — bad pads show up here.

### 2) Output pin or V− pin shorted/leaking to the −5 V rail (flux/bridge)
A tiny solder whisker or flux contamination can bias the summing node/output negative.

**Checks:**
- Resistance **pin 6 → −5 V** (should be high, not “low-ish”)
- Resistance **pin 2 → −5 V** (should also be high)

### 3) Wrong device / rotated device / pinout mismatch
Your earlier “AD8063” vs what’s actually fitted matters a lot: a pinout mismatch can behave *exactly* like this (railing weirdly).

**Quick sanity:**
- Confirm the exact marking on IC42 and that **pin-1 orientation** is correct for the footprint.

### 4) IC42 genuinely damaged
After you’ve ruled out (1)–(3), a railed output with V+ hard at 0 V is absolutely consistent with a stressed op-amp input stage.

## Fast decisive measurement (if you can do one more)
With your ground strap still in place, measure:
- **V+ (pin 3)** to ground (should be ~0 mV)
- **V− (pin 2)** to ground (will likely be near −4.1 V if the feedback is intact)
- **Vout** (you have −4.1 V)

If **V− ≈ Vout** while both are railed, the op-amp still has a DC feedback connection — which points more toward **IC42 fault or wrong part/pinout** (or a short/leak forcing the loop). If **V− is not following**, it’s a **feedback/open/joint** problem.

But honestly: based on what you’ve already done, I’d start with **continuity pin 6 → R32 → pin 2**, and a **very close inspection/clean** around pins 2/3/6 and the −5 V pin, then **swap IC42** with a known-good part once those basics check out.

[M23] ME (2025-12-23 05:54):
[image]
[attached file: A5D3C292-EB90-4958-82C3-7B205ED65E6F.jpeg]

[M24] AI (2025-12-23 05:54):
Thanks for the photo — that basically seals it.

Based on **everything you’ve measured** *and* what’s visible on the board, this is **not a “system-level bias” issue anymore**. This is almost certainly **a local fault at IC42 itself (or its immediate pins/pads)**.

Let me tie it together cleanly.

---

## What your last test definitively proves

You forced the **non-inverting input node hard to ground**.

Expected behaviour (healthy AD8063 in unity-ish loop):
- V+ = 0 mV  
- V− ≈ 0 mV  
- Vout ≈ 0 mV  

What you actually got:
- Node after 33 Ω ≈ 1–2 mV → ground strap is real
- **IC42 output = −4.1 V** → near negative rail

That means:

👉 **The op-amp is actively driving negative with V+ at 0 V**  
👉 This is *not* being caused by the ADC, C204, C109, or downstream loading  
👉 The loop is either **internally broken** or the **input stage is damaged**

---

## What the photo adds (important)

Looking closely at the IC42 area:

### 1) Hot-air rework risk is real here
- Fine-pitch SOIC/TSSOP
- Dense surrounding copper
- Multiple thermal paths
- Nearby ground pours

The AD8063 input stage is **not robust to heat/ESD abuse**. A partially damaged input pair will do *exactly* what you’re seeing:
- Large effective offset
- Output rails when the loop should balance
- Looks “alive” but behaves wrong at DC

### 2) No obvious gross solder bridge — but that doesn’t clear the die
I don’t see a blatant solder short in the photo, but:
- **Internal damage will not be visible**
- Micro-cracked pads or vias under the package also won’t show

Your electrical tests already ruled out:
- Downstream bias
- DC leakage through caps
- Output loading
- Floating V+ node

That leaves **IC42 or its pins**.

---

## One final sanity check (optional but fast)

With power **off**:
- Measure resistance:
  - Pin 6 → −5 V
  - Pin 2 → −5 V
  - Pin 3 → −5 V

Compare to a known-good channel (if you have one).

If IC42 is damaged, you’ll often see:
- One input pin reading noticeably lower resistance to a rail than the others

But honestly — you’ve already crossed the confidence threshold.

---

## Conclusion (clear call)

✅ **IC42 is faulty**  
Most likely:
- Input stage damage from hot-air rework  
- Possibly compounded by ESD or thermal overstress  

This is **not** a subtle offset or bias-current issue anymore — a healthy AD8063 **cannot** rail to −4.1 V with V+ strapped to ground in a closed loop.

---

## Recommendation

1. Remove IC42
2. Clean pads thoroughly (IPA + brush)
3. Inspect pads/vias carefully
4. Fit a **known-good replacement** (preferably hand-soldered or very controlled hot air)
5. Re-test *before* reconnecting the relay or earlier stages

If you want, I can also:
- sanity-check the **pinout vs footprint** one last time, or  
- suggest a **drop-in replacement** that’s a bit more rework-tolerant if this area ever needs touching again.

But based on the evidence: **you found the fault**.

[M25] ME (2025-12-23 05:55):
No, if 42 out is -4.1mv

[M26] AI (2025-12-23 05:55):
Ah! **−4.1 mV** (millivolts) changes everything — that’s **totally fine** and actually a *good* sign.

With you strapping the (relay) node to **0 V** and seeing:

- **IC42 Vout ≈ −4.1 mV**
- “Other side of the 33 Ω” ≈ **1–2 mV**

…that says **IC42 is behaving normally** in closed loop. An output sitting a few mV off zero is exactly what you’d expect from real-world offset + bias currents + measurement noise.

So **it’s not an op-amp fault** based on that result.

## What this now points to
Your earlier condition (relay removed) gave:
- **V+ (pin 3) ≈ 73 mV**
- **Vout/V− ≈ 58 mV**
- ~15 mV difference

That pattern is classic for: **the non-inverting input node is not being held to a defined DC potential** (floating / weakly biased / leaking), so it wanders to tens of mV, and the loop finds an equilibrium a bit away from it due to **input bias currents + whatever clamp/bias network is still connected**.

When you strap that node hard to ground, everything snaps back to ~0 mV ⇒ **the “fault” is the node biasing, not IC42**.

## Why the relay made earlier circuits go weird
When the relay is in, that “floaty” or biased node becomes connected back into earlier stages, so the small DC bias/leak current **backfeeds** through the relay path and upsets prior circuitry.

## Practical fix
Give that input node a **defined DC reference** when the relay is open / removed.

Typical options:
- **100 kΩ to 0 V** (very light, often enough)
- **10 kΩ to 0 V** (stronger bias, still usually benign)
- If it’s a high-speed node and you care about noise/loading, start with **100 kΩ** and go down only if needed.

If the node is *supposed* to sit at 0 V when disconnected, a **pulldown** is the cleanest solution.

## Next quick check
With the relay removed (your “bad” condition), measure:
- Resistance of that pin-3 node to ground (power off)

If it’s megaohms/open, that confirms it’s floating.

If you tell me what that node is meant to be (input from DAC? clamp? bias point?), I can suggest the best pulldown value so it doesn’t disturb the intended signal when the relay is closed.

[M27] ME (2025-12-23 06:01):
Thank you. 
[voice]

[M28] AI (2025-12-23 06:01):
Got it! So with that clarification, it all makes perfect sense: the op-amp itself is behaving just fine.
[voice]

[M29] ME (2025-12-23 06:17):
Ok, well I’ve now tied that node to ground with a 47k. And it crept back up to 60mv. Could the input cap c8  to pin 3 be leaky?

[M30] AI (2025-12-23 06:17):
Yes — **a leaky C8 (or anything else on the pin-3 node)** is absolutely a credible way to get back to **~60 mV** even with a **47 kΩ pulldown**.

### Why 47 kΩ doesn’t “force” it to 0 mV if there’s leakage
47 kΩ to ground means you only need a tiny DC current to create tens of mV:

\[
I = \frac{V}{R} = \frac{60\,mV}{47\,k\Omega} \approx 1.28\,\mu A
\]

So **~1–2 µA of leakage** into that node will lift it to the level you’re seeing. That’s small enough to come from:
- a **leaky capacitor** (C8),
- **flux/ionic contamination** around the pad,
- **input bias current** paths through other components connected to that node,
- or a clamp/protection diode path.

### Is a leaky capacitor plausible?
Depends on what C8 is:
- **Electrolytic / tantalum**: leakage in the µA range is common/fairly plausible, especially after stress.
- **X7R ceramic**: true dielectric leakage is usually tiny, but **board contamination** around it is a *very* common “looks like leaky cap” failure mode.
- **Film/NP0**: leakage is usually extremely low unless cracked/contaminated.

### Fast, decisive tests
Do these in order; they’ll pinpoint it quickly.

#### 1) Lift one end of C8 (best single test)
With C8 disconnected:
- If the node now sits near **0 mV** with 47 kΩ → **C8 or the “other side” of C8 is the source**.
- If it still creeps → leakage is elsewhere on that net (flux, IC pin, other components).

#### 2) Measure the DC current implied by the pulldown
Measure the node voltage (you already have ~60 mV) and confirm R=47 kΩ.
That’s ~1.3 µA. Now try:
- Change pulldown to **10 kΩ** temporarily.
  - If it drops to ~10–15 mV, that strongly indicates a roughly constant µA leakage source.
  - If it barely changes, something lower impedance is driving it.

#### 3) Clean the area aggressively
IPA + brush, then dry thoroughly (warm air helps). Ionic residue can easily create µA leakage across solder mask, especially around high impedance nodes.

### One more important question (but you can answer by measuring, no guessing)
When it “creeps” up, is it:
- **toward +60 mV** or **−60 mV**?
That polarity tells you whether the leakage is sourcing from a positive node or sinking toward a negative node (very helpful for locating the culprit).

But bottom line: **yes, C8 could be the culprit**, and the math says you only need **~1 µA** of leakage to get the behaviour you’re seeing.

[M31] ME (2025-12-23 06:27):
[image]
Ok, that hasn’t changed much. Noncurrent through that input resistor mind. So 58mv at input. 48mv at output and non inverting input 
[attached file: IMG_BD7A8F62-08C5-463D-AACE-1308F5DB828E.jpeg]

[M32] AI (2025-12-23 06:27):
That result actually *fits* a very simple explanation:

### If there’s ~no drop across the 33 Ω, the 58 mV isn’t coming “through” that resistor
Your note “no current through that input resistor” (i.e., **R101 = 33 Ω**) matches the fact you’re seeing essentially the same DC on both sides. So the node is being biased by something **local / high-impedance**, not by a low-impedance driver through 33 Ω.

### 47 kΩ to ground + µA-level bias current ⇒ ~50–60 mV
With a 47 k pulldown, you only need ~1 µA to create what you’re seeing:

\[
I \approx \frac{58mV}{47k\Omega} \approx 1.2\ \mu A
\]

High-speed **bipolar** input op-amps (and some high-speed parts in general) commonly have **input bias currents in the µA range**. If that current flows **into or out of the non-inverting input node**, it will “self-bias” the node to tens of mV even with your 47 k pulldown. That’s completely consistent with:

- **~58 mV at the non-inverting input node**
- **~48 mV at the output** (unity follower will follow, but you can still see several mV to ~10 mV of residual error from offset + bias-current effects + the rest of the network)

### The quickest way to prove it (no more guesswork)
Swap the pulldown value temporarily:

- Change **47 k → 10 k**
  - Expected node voltage if it’s bias current dominated:
  \[
  58mV \times \frac{10k}{47k} \approx 12mV
  \]
- Change **47 k → 1 k**
  - Expected:
  \[
  \approx 1.2mV
  \]

If the node voltage scales roughly with R, it’s **input bias current (or a tiny leakage current)**, not a “mystery source” elsewhere.

### Could C8 be leaky?
It *could*, but your data points more strongly to **µA-level current**, and **bias current is the most common µA source** here. A leaky cap/contamination would behave similarly — but the resistor-scaling test above separates them cleanly.

If you tell me the **exact op-amp part number actually fitted at IC42** (your earlier “AD8063” vs the schematic text you’ve shown elsewhere), I can sanity-check whether µA bias is expected and what typical DC error you should see.

[M33] ME (2025-12-23 06:34):
10k in, it’s gone down to 33mv

[M34] AI (2025-12-23 06:34):
Perfect diagnostic — that scaling basically confirms it’s **a (roughly) constant leakage/bias current** setting the node voltage.

### What your 10 k result means
With 47 k you saw ~58–60 mV.  
With 10 k you now see **33 mV**.

That implies a DC current into/out of that node of about:

\[
I \approx \frac{33mV}{10k\Omega} \approx 3.3\ \mu A
\]

If it were *purely* a fixed current source and nothing else, you’d expect 58 mV → ~12 mV when going 47 k → 10 k. Since you got **33 mV**, that tells us there’s **also another resistance path** (or another DC source) involved — but the key point remains:

✅ the behaviour is strongly consistent with **µA-level bias/leakage**, not a “mysterious voltage source”.

### Most likely sources of that ~3 µA
1) **Input bias current of IC42** (if it’s a high-speed bipolar input op-amp, µA is normal)  
2) **Leakage via the protection network** around that node (zener/diode paths, relay pad contamination)  
3) **Board contamination / flux** creating a “soft” resistor to some rail (this is *super* common after hot air)

### The next “one-step” test
Go to **1 kΩ** to ground temporarily.

- If it drops to a few mV (say ~3–5 mV), you’ve got ~3 µA bias/leak and it’s not a hard short.
- If it *doesn’t* drop proportionally, then there’s a lower-impedance path to a rail somewhere (contamination/component fault).

### Practical fix (without overloading your source)
If that node must sit at ~0 mV when the relay is open, you can choose a pulldown that makes the bias harmless:

- Want ≤ **5 mV** at that node with ~3 µA leakage:
\[
R \le \frac{5mV}{3\mu A} \approx 1.7k\Omega
\]

So **1 k–1.5 k** will clamp it near zero.

But you also have to consider what drives that node when the relay is closed — if it’s a DAC output or precision stage, a 1 k load might be too heavy. In that case:
- keep the pulldown higher (10–47 k),
- and instead **remove the leakage source** (cleaning, replace suspect part, etc.)

### Fast way to distinguish “IC bias current” vs “leak to a rail”
Measure the node voltage with the pulldown installed, then power **only the op-amp** (±5 V present) while keeping the relay/open input disconnected:
- If the node bias is present with only IC42 powered → points to **IC42 bias current**.
- If it changes depending on other rails being present (e.g. −5 V, clamp rails, etc.) → points to **leakage via other components/contamination**.

If you can, tell me:
- does the node drift positive or negative,
- and what exact part IC42 is (marking / BOM).  
Then I can tell you whether **~3 µA** is expected bias current or “too high” (damage/leak).

[M35] ME (2025-12-23 07:20):
Ok, well the other circuit behaves exactly the same when relays removed 

[M36] AI (2025-12-23 07:20):
That’s actually a strong hint that this is **normal/expected behaviour of the topology when the relay is open**, not a one-off fault.

If **both channels** do the same thing with the relay removed, the common causes are:

## What’s really happening
With the relay out, that node (your “OSH2 / pin-3 feed”) is effectively **high impedance**. A high-speed op-amp input + any clamp/protection parts will have **µA-level bias/leakage**. That current has to go somewhere, so it flows through whatever “bleeder” you’ve added to ground, creating a small DC voltage:

\[
V \approx I \times R
\]

Your 10 k test giving **33 mV** implies ~**3.3 µA** total bias/leak current on that node — very plausible for a fast front end + protection network.

So when the relay is removed/open, **you should expect tens of mV of DC wandering** unless you provide a defined DC path (or a proper bias network).

## Why it “finds its way back” when the relay is in
When you reconnect the relay, that bias/leak current now has an easier path back into the previous stage. If that previous stage is also high impedance (or referenced differently), it will get nudged by the same µA current and you’ll see the offset propagate.

## What to do about it (practical options)

### Option A — Accept it (if relay-open is not an operating mode)
If the relay is only removed for debug, you can ignore it. In the real assembled state, the relay closes and the upstream stage defines the DC level.

### Option B — Add a “parking” resistor so it behaves when open
If you need the circuit to sit nicely with relay open, add a bleed resistor to ground sized by what you can tolerate:

- If leakage/bias is ~3 µA and you want **<5 mV**, you need **≤1.6 kΩ**.
- If **10 kΩ** gives you **33 mV**, that’s consistent.

But: **don’t load the upstream source too much when the relay is closed**.
A neat trick is to use a **larger resistor (say 47 k–100 k)** plus a **very small capacitor** to ground to keep it quiet at AC without forcing DC too hard — depends on what the node is meant to do.

### Option C — Bias it to a defined reference instead of ground
If this node is meant to sit at some midscale/common-mode (not 0 V), then tie it (through a resistor) to that reference instead, not ground.

## One quick check before you “fix” it
When the relay is *in* and the upstream circuit is connected normally, do these offsets still exist?
- If **they disappear** in the normal configuration → everything is fine.
- If **they remain** → then it’s a genuine bias/offset problem in the assembled path.

If you tell me what that relay is selecting (DAC output? clamp bias? cal source?) and what DC level the node should sit at in normal operation, I’ll suggest the safest bleed/bias scheme that won’t mess with bandwidth or loading.

[M37] ME (2025-12-23 07:22):
It’s ad8063. It has an auxiliary pins 8 andn5 which are b high and low. They then get powered  by plus and minus 5 on 7 and 4 respectively 

[M38] AI (2025-12-23 07:22):
Got it — and one important correction:

On an **AD8063 (single op-amp, SOIC-8)** the pins are:

- **7 = +Vs**
- **4 = −Vs**
- **3 = +IN**
- **2 = −IN**
- **6 = OUT**
- **1 & 5 = NC (no connect)**
- **8 = NC (no connect)**

So pins **8 and 5 are *not* “aux high/low rails”** on an AD8063. If you’re seeing “VH/VL” style pins on the schematic, that’s the pin naming for a **different op-amp family** (e.g., some ADC drivers / clamp amps), not the AD8063.

### Why that matters
If your PCB footprint/schematic expects an op-amp with **VH/VL** pins and you fitted an **AD8063**, you can end up with:
- NC pins unintentionally tied into bias/clamp networks,
- or worse, mis-powering / wrong pin mapping,
and you’ll get exactly this kind of weird “creeping” DC behaviour.

### But your measured behaviour (µA effect) is still consistent with AD8063
AD8063 has **µA-level input bias current**, so a floating input with a 47 k pulldown can easily sit at tens of mV. Your 10 k pulldown test showing a lower voltage supports that.

### Two concrete things to do now

#### 1) Verify the part vs footprint vs pinout (critical)
Please check the top marking on the IC and confirm:
- Package (SOIC-8? MSOP-8?)
- Orientation (pin-1 dot/notch)
- That pins 7 and 4 really go to ±5 V
- That pin 6 really goes to the output net you think it does
- That pins 2 and 3 go where expected

If the board silkscreen/schematic calls it something like “AD8036/AD8036AR” (I saw that on your earlier sheet), that is **not** an AD8063.

#### 2) If the relay-open mode must be stable at 0 V
You likely need a **stronger DC reference** on the non-inverting node than 47 k, because the AD8063 bias current will lift it.

Given you inferred ~3 µA, to keep it under:
- **5 mV**, you need **≤1.6 kΩ**
- **10 mV**, you need **≤3.3 kΩ**

But only do that if it won’t load the driving source when the relay is closed.

---

If you can, send a close photo of **IC42 top marking** and tell me what the PCB silkscreen says (IC42 + any part code). Right now, the biggest risk is that there’s a **part mismatch** (your schematic labelling looked like a different op-amp), and that’s more dangerous than a 30–60 mV creep.

[M39] ME (2025-12-23 07:24):
Sorry 8036

[M40] AI (2025-12-23 07:24):
Ah — **AD8036** makes this make much more sense.

### Key point
With an **AD8036**, **µA-level input bias current is normal**, and with the relay removed your non-inverting input node is effectively **high impedance**, so it will “self-bias” to tens of mV unless you give it a firm DC path.

Your measurements line up perfectly with that:

- 47 k pulldown → ~58–60 mV  
  \(\;I \approx 60mV/47k \approx 1.3µA\)
- 10 k pulldown → 33 mV  
  \(\;I \approx 33mV/10k \approx 3.3µA\)

That’s exactly the kind of µA-ish current you expect to see from **input bias + small leakage paths** around protection parts / board contamination. And the fact the *other channel behaves the same* strongly indicates **it’s inherent**, not a fault.

### Why Vout is ~48 mV while V+ is ~58 mV
In a follower, Vout should follow V+, but you can still see a residual difference from:
- input offset voltage,
- input bias current flowing through whatever impedance the inverting input “sees”,
- any series/feedback resistors and clamp network asymmetry.

With high-speed parts like AD8036, a few to a few-tens of mV in a “floating / relay-open” condition is not shocking.

---

## What to do (practical)

### If relay-open is *not* a real operating mode
Ignore it. When the relay is present/closed, the upstream stage will define the DC level and the bias current has a proper return path.

### If relay-open must sit near 0 mV
You need a **stronger DC reference** than 47 k.

Rule of thumb with ~3 µA:
- For **≤10 mV**, use **≤3.3 kΩ**
- For **≤5 mV**, use **≤1.6 kΩ**

Try **2.2 kΩ** to ground as a starting point (temporary test). If it clamps the node close to 0 and doesn’t upset the driving stage when the relay is closed, you’ve got your fix.

### Even better: match impedances seen by both inputs
If you can make the **DC resistance seen by V− roughly equal to V+**, the bias-current induced error cancels better.

---

## One definitive check
With the relay **installed and in the normal connected state**, what are:
- V+ (pin 3)
- Vout
- V−

If those go close to zero / expected levels, then nothing is “wrong” — you’re just observing the behaviour of a high-speed bipolar-input amp with a floating input when the relay is absent.

[M41] ME (2025-12-23 07:34):
[image]
[image]
Back to the original circuit for now. So there is this annoying offer present. I’ve removed the ic above and it’s still there.
When I remove the capacitor it goes away. But I’ve changed the capacitor and it’s still there 
[attached file: 73513D4A-4A53-4422-9E26-A4D1F54CDE2A.jpeg]
[attached file: 19302F57-B02E-405E-8826-7DC0BDAE4045.jpeg]

[M42] AI (2025-12-23 07:34):
From those two schematics/photos, what you’re seeing is very consistent with a **classic “AC-coupled node with no DC return path” problem**, not a “bad capacitor” problem.

### Why it goes away when you remove the capacitor (but comes back with a new one)
That series cap (looks like **C4 = 10 µF**) is the only thing connecting the left-hand network to the right-hand node. When it’s fitted, the node on the **right side of C4** is effectively **floating at DC** unless something provides it a DC reference.

In that situation, a small current (µA-ish) from *any* of these will charge the cap until the node sits at some clamp/bias point:
- **input bias current** of the following op-amp stage
- **ESD/clamp diodes** on the next IC’s input (often clamp around ~±0.3 to 0.7 V relative to some rail/ground)
- **leakage/contamination** on the PCB
- any “off” switch leakage (but you said you removed the IC above and it remained — so it’s likely downstream)

That’s why you keep landing around **~−0.3 V**: that value screams “**a diode junction is just starting to conduct**” and is pinning the node.

### Key clue in your note
> “I’ve removed the ic above and it’s still there.”

So it’s almost certainly **not** DG412 leakage. It’s the **node after C4** being biased/clamped by whatever it feeds next.

---

## What to do (the proper fix)
Give the **right-hand side of C4** a defined DC reference with a “bleeder” resistor.

Typical values:
- Start with **100 kΩ to 0 V** from the **right side of C4** (the node that’s currently at −0.3 V).
- If it still sits off, go stronger: **47 kΩ**, then **10 kΩ**.

(Choose the highest value that reliably parks it where you want, so you don’t load the signal path unnecessarily.)

If the signal is meant to be biased to something other than 0 V, tie that resistor to the correct **bias reference** instead of ground.

### Why this works
It provides a **DC return path** for input bias currents, so the node can’t “charge up” until a diode clamps it.

---

## Two quick measurements that will confirm this in 30 seconds
With the circuit in the “bad” state (cap fitted, relay open), measure DC:
1) **Left side of C4** (P51_05L side)
2) **Right side of C4** (node that goes to R153 / R81 etc.)

If left is ~0 V and right is ~−0.3 V, that proves the offset is being generated **on the right side** (bias/clamp), not through the capacitor.

---

## One more practical gotcha
If C4 is electrolytic/tantalum: double-check **polarity**. In your case you’re seeing **negative DC** on the right side — if the cap is polarised the wrong way for the DC it develops in this floating condition, it can get leaky over time and make the symptom worse (but it still wouldn’t explain why a brand-new cap behaves the same immediately).

---

If you tell me exactly **where the right side of C4 goes next** (which IC/input pin), I can suggest the best bleeder location/value and whether it should go to **0 V** or to a **mid-bias reference**.

[M43] ME (2025-12-23 07:36):
Could it be because I don’t have the relays fitted to the right 

[M44] AI (2025-12-23 07:36):
Yes — **very plausibly**, and it fits your “−0.3 V appears unless I remove the coupling cap” symptom.

### Why missing relays on the right can create this
Those relays (and the networks they connect to) often provide the **DC return / bias path** for an **AC-coupled** node.

When the relays aren’t fitted (or are open), the node on the far side of your coupling cap (C4 / C8 etc.) can become **floating at DC**. Then:

- tiny **input bias currents** / leakage currents charge the coupling cap,
- the node drifts until something clamps it,
- and it commonly clamps around **~±0.3 V** because you’re just forward-biasing some internal ESD/clamp diode somewhere.

That’s exactly what you’re observing:
- cap in → node floats → creeps to ~−0.3 V  
- cap out → node is no longer connected → offset “disappears”

### Quick way to prove it
Pick the node that sits at **−0.3 V** and temporarily add a **bleeder**:

- **100 kΩ to 0 V** (start here)
- if still drifts, try **47 kΩ**, then **10 kΩ**

If the offset stops and the node parks near 0 V, you’ve confirmed the cause is **missing/absent DC path**, which the relay path would normally provide.

### What value should you keep long-term?
- If the relay will be fitted in the real design: you can treat this as a “debug artefact” and just add a temporary bleeder for testing.
- If you want the board to behave nicely even without relays: keep a bleeder permanently (often **100 kΩ** is enough and won’t load anything meaningful).

### One caution
If that node is supposed to sit at some **bias level** (not 0 V) when operating (e.g., midscale for an ADC driver), then the bleeder should go to that **bias reference**, not ground.

If you point to the exact node (right side of C4 / after which resistor) and tell me what it normally connects to through the relay, I’ll suggest the cleanest bleeder placement/value so it doesn’t change your AC response.

[M45] ME (2025-12-23 07:43):
I’m wondering now as sometimes it’s ok sometimes it’s not it may be my power on sequence 

[M46] AI (2025-12-23 07:43):
Yeah — **power-on sequence can absolutely make this “sometimes OK, sometimes not”** when you’ve got **AC-coupled / floating nodes** and **clamps** in the path. What you’re describing (random-ish offset that disappears when you remove the coupling cap) is exactly the kind of thing that becomes *stateful* at startup.

### What’s likely happening
With the relay missing/open, the node after the coupling cap has **no DC return**. On power-up:

- one side of the cap comes up first (DAC/op-amp),
- the other side (ADC/input stage/rails) comes up later,
- internal **ESD/clamp diodes** on the “later” side conduct briefly,
- the coupling cap gets **charged to some DC value**,
- and because there’s no bleed path, it *stays* there until something discharges it.

Depending on which rail rises first and how fast, you end up with:
- near 0 V (good startup), or
- a parked value like **~−0.3 V** (diode clamp point

[M47] ME (2025-12-23 07:43):
Which is best plus 5v or minus dirst

[M48] AI (2025-12-23 07:43):
Short answer: **bring the analogue supply rails up together**.  
If you must choose an order, **−5 V first (or at least not after +5 V)** is usually safer for *this kind of circuit* — but the real fix is to **remove the floating condition**, not rely on sequencing.

Here’s why, in practical terms.

---

## What’s going wrong at power-up in your circuit

You have:
- **AC-coupled nodes**
- **missing relays (open circuits)**
- **input clamp / ESD diodes**
- **op-amps with µA bias currents**

When a node is floating at DC, **power-up order determines which internal diode conducts first**, and that **charges the coupling capacitor** to some arbitrary value. With no bleed path, it stays there.

That’s why you see:
- sometimes ~0 V (good)
- sometimes ~−0.3 V (classic diode clamp voltage)

---

## Why +5 V first is usually worse

If **+5 V comes up first** while −5 V (or ground reference of the next stage) is not yet valid:

- Internal ESD/clamp diodes from the input to **−Vs or substrate** can conduct
- The AC-coupling cap charges negatively
- The node parks around **−0.2 to −0.4 V**
- With no DC return path, it stays there

This exactly matches your symptoms.

---

## Why −5 V first is *slightly* safer

If **−5 V is present before +5 V**:
- There’s a valid sink for bias currents
- Clamp diodes are less likely to forward-bias in the “wrong” direction
- The cap is less likely to be charged to a negative offset

So **if forced to choose**:
> ✅ **−5 V first, +5 V second**

But…

---

## The important truth (and the real fix)

**Power-up sequencing is not the right thing to rely on here.**

Your circuit is telling you this very clearly:
- Removing the coupling capacitor makes the problem disappear
- Adding bleed resistors reduces or removes it
- Behaviour is random across power cycles

That means the node **needs a DC reference**.

---

## What actually fixes it (robustly)

One of these (ranked best → acceptable):

### ✅ Best: DC bleed on the floating side of the coupling cap
- **47 kΩ–100 kΩ** to the correct reference (often 0 V or bias node)
- Enough to sink µA bias currents
- Won’t affect AC response meaningfully

### ✅ Also good: bias both sides symmetrically
Match DC impedance seen by +IN and −IN so bias currents cancel.

### ⚠️ Temporary/debug only: rely on sequencing
Works on the bench, fails in the field.

---

## Rule of thumb you can keep
> If a node can ever be AC-coupled **and** disconnected by a relay/switch,  
> **it must have a defined DC path** — or power-up will be non-deterministic.

---

If you want, next I can:
- suggest **exact resistor values** that won’t disturb your bandwidth,
- sanity-check **which side of which cap** should get the bleed,
- or help you design a **“relay absent” safe bias** that behaves identically to “relay present”.

You’ve debugged this very cleanly — the behaviour is logical, just annoying 😄

[M49] ME (2025-12-23 07:48):
But if a refit ic6 dg412 that should help keep things tied correctly 

[M50] AI (2025-12-23 07:48):
Refitting **IC6 (DG412)** will *help* only if, in your design, that switch is what provides the **DC return / defined bias** for the node when everything is “in its normal state”.

But it won’t magically fix the underlying issue **unless the DG412 is actually CLOSED (or providing a DC path) at the times you care about**.

### When refitting DG412 *will* fix it
If IC6 is meant to connect that AC-coupled node to:
- a **bleeder to 0 V**, or
- a **defined bias reference**, or
- the next stage input that has a defined DC return,

…and it’s **guaranteed to be on** during power-up / normal operation, then yes: it can stop the node floating and prevent the “sometimes −0.3 V” state.

### When it *won’t* fix it (common)
- The DG412 defaults **OFF** at power-up (logic not valid yet), so the node still floats and the cap can still charge.
- The DG412 only switches the AC path, but the **DC return is still missing** when open.
- The DG412 has **leakage** (nA–µA) which is enough to charge a floating node over seconds (especially with 10 µF coupling caps).
- Your issue is happening **before** IC6 is commanded (during rail ramp).

### The robust approach (even with DG412 fitted)
Even if you refit IC6, I’d still recommend adding a **high-value bleed** on the floating side of the coupling cap so startup is deterministic:

- Start with **100 kΩ to the correct reference** (0 V or the intended bias point).
- If you still see drift, go to **47 kΩ**.

That won’t interfere with the DG412 function, but it stops the “charged cap + diode clamp” lottery.

### Quick test to predict whether DG412 refit will help
Ask yourself / measure:
- In the “bad” case, is the node sitting at about **−0.3 V** because it’s clamped?
- Does toggling the DG412 control (if you can) immediately pull it to the expected level?

If yes → DG412 closure provides the missing DC path, so refitting likely resolves.

If it only fixes it **after** firmware asserts the control → you’ll still get random startup unless you add a bleed.

If you show me the DG412 connections around that node (what S/D are tied to), I can tell you definitively whether IC6 provides a DC reference in *both* switch states or only when on.

[M51] ME (2025-12-23 07:52):
Yes so when I power positive first it stays at a positive voltage, and when negatives first it stays at negative. The value to variable from test to test. Perhaps this is to do with relays not fitted

[M52] AI (2025-12-23 07:52):
Yep — that pattern is almost a textbook sign of a **floating, AC-coupled node** that’s being **“charged” during power-up** and then **remembering** whatever charge it got.

What you’re seeing:

- **+5 first → node ends up positive**
- **−5 first → node ends up negative**
- **value varies run-to-run**

…means the node has **no solid DC reference** during the ramp, so tiny leakage/bias currents and clamp diodes decide where it parks. The coupling capacitor then holds that DC like a little memory cell.

### Are missing relays the reason?
Very plausibly, yes.

Relays (or the DG412) often provide the **DC return/bias path** in the real, fully-assembled configuration. With them not fitted, you’ve removed the thing that normally:
- clamps the node to a defined potential, or
- connects it to a bias/reference network, or
- connects it to the next stage which has a DC path.

So you’re left with an “open” node + coupling cap = **random startup offset**.

### What fixes it robustly (no reliance on sequence)
Add a **bleeder / bias resistor** on the floating side of the coupling cap (or on the node that floats when relays are absent).

Typical:
- **100 kΩ to 0 V** (start here)
- If still drifting, **47 kΩ**
- If you need it to settle fast and firmly, **10 kΩ**

If the node is supposed to sit at a bias point (not 0 V), bleed it to that **bias reference** instead.

You can also add a **small cap to ground** (e.g., 1–10 nF) if you need to quiet it, but the resistor is the key for DC determinism.

### Why the value varies
Because during ramp:
- clamp diodes conduct briefly depending on rail timing,
- leakage currents vary with temperature, board residue, and previous charge state,
- so the final DC across the coupling cap differs each time.

### Best next step
Since you’ve proved it’s sequence-dependent, do this quick experiment:

1) Pick the floating node (the one that parks ± randomly).
2) Add **100 kΩ to 0 V** temporarily.
3) Power + first and − first again.

If the node now reliably comes up near the same value every time (usually ~0 or your bias), you’ve confirmed it’s a **missing DC return path** issue — which the relays being absent would absolutely cause.

If you want, point to the exact node (right side of which coupling cap) and tell me what it *should* be biased to in normal operation, and I’ll give you the best resistor value/location that won’t mess up your signal bandwidth.

[M53] ME (2025-12-23 07:54):
[image]
If it is t the relays then its ic9
[attached file: IMG_965696C6-2208-4947-9304-09311CA71225.jpeg]

[M54] AI (2025-12-23 07:54):
It **doesn’t have to be IC9**.

From that schematic, the **−0.3 V node is on the *right side of C4*** (after the 10 µF coupling cap). That node is being “parked” by **whatever it connects to on the right**, *not* by IC9 on the left, as long as IC9 is AC-coupled through C4.

Key points in your drawing:

- **IC9 output → R12 (1 k) → P44 → (DG412 would connect here) → R153 (1 k) → C4 (10 µF) → right-hand node**
- You’ve removed DG412 and the relays, so the right-hand node has **no guaranteed DC path**.
- With **C4 fitted**, that right-hand node can float until it hits a clamp, often around **±0.3 V** (diode conduction), and it will depend on **power-up order** — exactly what you observed.

### How to prove it’s *not* IC9 in 60 seconds
Add a temporary **bleeder resistor on the right side of C4** (the node you’ve marked −0.3 V):

- Try **100 kΩ to 0 V** first.
- If it still lands near −0.3 V, try **47 kΩ**, then **10 kΩ**.

If the node stops “remembering” and comes up consistently near 0 V, then **IC9 is innocent** — the node was simply floating because the relay/switch path that normally biases it isn’t present.

### Why replacing C4 didn’t help
Because C4 isn’t “causing” the offset — it’s just the element that allows the floating node to be charged and hold charge. Swap the cap all day and you’ll still get the same behaviour if there’s no DC return.

### When it *would* be IC9
Only if you see the same DC offset **on the left side of C4** (IC9 side) *with the right side bled to a defined reference*. If left side is clean and right side floats, it’s downstream.

---

If you tell me what the right side of C4 feeds (which op-amp / ADC pin / clamp network), I can suggest the best permanent “park” resistor value that won’t disturb your bandwidth when the relays are fitted.

[M55] ME (2025-12-23 07:55):
Fresh device

[M56] AI (2025-12-23 07:56):
If **IC9 is a fresh device**, that still doesn’t rule it in or out — but with this topology it’s *still* much more likely you’re seeing **a floating, AC-coupled node being clamped downstream**, not IC9 “generating” a DC offset.

Here’s the clean way to separate them without guessing.

## Do these two measurements (cap fitted, DG412/relays absent)

### 1) Measure **both sides of C4** at DC
- **Left side of C4** (IC9/DG412/R153 side)
- **Right side of C4** (the node you marked ~−0.3 V)

**Interpretation**
- If left side is near 0 V but right side is ~±0.3 V → **IC9 is not the source**. The right node is floating and finding a clamp point.
- If left side is also offset strongly → then IC9 (or its local biasing) is involved.

### 2) Add a bleeder on the **right side of C4**
Temporarily tack:
- **100 kΩ to 0 V** (then 47 k, then 10 k if needed)

If the −0.3 V disappears and becomes repeatable across power cycles, you’ve proven it’s a **missing DC return path** (because relays/switch not fitted), not a bad IC9.

## Why your “power + first / − first” observation matters
That “sign depends on rail order” behaviour is the giveaway: it’s what happens when a node is **charging a coupling capacitor through bias/leak/clamp paths during ramp**, then holding that charge.

IC9 being “fresh” is compatible with that — even a perfect IC9 can’t stop a *downstream floating node* from doing this.

---

If you want the simplest practical fix while debugging with relays removed:
- tack **47 kΩ from the right side of C4 to 0 V**  
That’s usually enough to kill the random ±0.3 V “memory” without loading the AC path much.

If you tell me the DC readings on **both sides of C4**, I’ll call it instantly.

[M57] ME (2025-12-23 07:56):
No, if refitted ic6 dg412 with a fresh

[M58] AI (2025-12-23 07:56):
Got you — if you **refit IC6 (DG412) with a fresh part**, then **yes, that can absolutely stop the node floating** *provided the switch is actually ON (or providing a DC path) when you measure / during power-up*.

But two gotchas matter a lot here:

## 1) DG412 “fresh” doesn’t help if it’s OFF at startup
DG412 powers up **open** (effectively), until the logic input is at a valid level. If your **CLAMP control** is undefined during ramp, the switch state can be random, and you’ll still see the “sometimes positive, sometimes negative” behaviour.

**What to do:**
- Force the DG412 control pin to a known state at power-up with a pull-up/down (e.g. 10 k to logic rail/ground).
- Or, for debug, manually strap IN so the switch is definitely ON.

## 2) Even when ON, you still need a DC return path on the “far side”
Look at your path:

IC9 → R12 → (DG412) → R153 → **C4 (series cap)** → right-side node

Even if DG412 is ON, **C4 still blocks DC**. So the right-side node *still floats* unless there is a bleed/reference on that node (or in the circuit it feeds).

So DG412 helps only if what it connects to ultimately gives the right-side node a DC reference through some other path (e.g., the downstream input network, relays, bias resistors).

## The single best test
Refit DG412, then do this:

1) Confirm DG412 is definitely ON (measure continuity S–D or observe the expected AC path).
2) Measure DC on **right side of C4**.

**If it still sits around ±0.3 V and is sequence-dependent**, DG412 being present isn’t the missing piece — the missing piece is still **a DC return on the right side of C4**.

## Practical fix that works regardless of DG412/relays
Add a bleeder on the right side of C4:
- **100 kΩ to 0 V** (start)
- 47 kΩ if needed

This won’t fight the DG412, and it makes power-up deterministic even when relays aren’t fitted.

---

If you tell me: when DG412 is refitted, is the **CLAMP logic definitely driven high/low at reset**, or is it floating? That’s the difference between “DG412 fixes it” and “still random.”

[M59] ME (2025-12-23 08:00):
Fitted the relay on one channel and it’s still there.

[M60] AI (2025-12-23 08:00):
If you’ve now **fitted the relay** on one channel and the **± / −0.3 V “memory” is still there**, that’s a strong sign the root cause is **not simply “missing relay = floating node”**.

At this point, treat it as: **the node on the right side of C4 is being clamped/bias-charged by whatever it connects to**, and the relay you fitted **is not providing a DC return in the state you’re testing** (or the return path is still open somewhere else).

Here are the most likely reasons, in priority order, and the quickest way to prove each.

---

## 1) The relay contact state isn’t what you think (most common)
Even with the relay physically fitted:
- the **coil may not be energised**
- you might be on the **wrong throw (NC vs NO)**
- the CPLD/driver may not be driving it at power-up

### Test (no guessing)
With power applied, measure:
- **relay coil voltage** (is it actually switching?)
- DC continuity from the floating node to its intended reference through the relay contact (in each state)

---

## 2) The node is still AC-coupled and *still has no DC return*
Even if the relay connects some signal, you may still have **C4 in series**, so DC is blocked unless there is a resistor/reference on the *right* side.

### The “call it instantly” test
Measure DC on **both sides of C4**:
- Left side (IC9/R153 side)
- Right side (problem node)

If right side wanders/clamps but left side is stable → the DC return is missing on the right, *relay or not*.

---

## 3) There’s an actual clamp path on the right side (ESD diodes / input protection)
If the node feeds an op-amp/ADC input, it likely has protection diodes to rails/ground. During ramp they conduct and charge C4 until the node sits around **~0.3 V**.

This explains perfectly:
- sign depends on which rail rises first
- value varies run to run

---

## 4) The easiest way to stop the symptom (and diagnose in one step)
Put a temporary **bleeder resistor** on the **right side of C4** to the intended reference:

- Start **100 kΩ to 0 V**
- If still not stable, **47 kΩ**, then **10 kΩ**

**If the “−0.3 V memory” disappears**, you’ve proven it’s a *missing DC return* problem, regardless of relay state.

---

## What I’d like you to measure (3 numbers)
Right now, please measure these DC voltages in the “bad” condition:

1) **Left side of C4**  
2) **Right side of C4**  
3) **Relay coil voltage** (or coil on/off state)

With just those, I can tell you whether the relay isn’t switching, or it’s switching but not providing a DC path, or the clamp is downstream.

If you want the fastest “fix while debugging”: tack **47 kΩ from right side of C4 to 0 V** and see if it becomes deterministic across power cycles.

[M61] ME (2025-12-23 08:01):
It’s the same on both video chains so must be something common

[M62] AI (2025-12-23 08:01):
Agreed — if it’s **identical on both video chains**, the cause is almost certainly something **common/shared** (or something that’s *common in the design*, like “this node has no DC return when the clamp path is open”).

From your symptoms (± sign depends on rail order, value varies, sits around ~0.3 V, disappears when the coupling cap is removed), the most common “shared” culprits are:

## 1) Power-up sequencing / rails not tracking (shared supply issue)
Both channels will behave the same if:
- +5 and −5 don’t come up together
- one rail is slow / brownouts / overshoots
- analogue ground reference is moving during ramp

This makes the clamp diodes on the receiving side conduct differently each time and “charge” the coupling cap.

**Quick check:** scope +5, −5, and 0V (ground) during power-up. If one lags or ramps slowly, that explains the randomness.

## 2) The node is *designed* to need a DC return that currently isn’t present (shared missing bias path)
Even if you fitted a relay in one channel, if the control logic / clamp mode at startup leaves the path open, both channels are still effectively floating at DC until firmware asserts control.

**Practical test:** add a **temporary bleeder** on the floating side of the coupling cap (right side of C4 in your drawing):
- 100 k → then 47 k → then 10 k to 0 V

If both channels become stable immediately, you’ve proven the “common cause” is simply **floating AC-coupled node + clamp during ramp**.

## 3) A shared clamp/control signal (CPLD) leaving the DG412/relays undefined at reset
If CLAMP control is floating at reset, both DG412s/relays may be random until the CPLD config is done. That produces exactly “sometimes OK sometimes not” and affects both channels the same.

**Fix:** add a pull-up/pull-down on the CLAMP control so it defaults to a known safe state.

---

## The single most decisive experiment (takes 2 minutes)
Tack **47 kΩ from the problem node (right side of C4) to 0 V** on *one* channel.

- If the randomness disappears and it always powers up near 0 V → it’s not a bad component, it’s **missing DC return during power-up**, shared by design/supplies/control.
- If nothing changes → then it’s more likely a **rail sequencing problem** (one rail is forcing a clamp regardless of bleeder strength), and you should scope the rails.

If you tell me:
- exact node where you measure ±0.3 V (right side of which capacitor),
- and whether CLAMP is asserted at power-up,

I can tell you whether the “right” permanent fix is a **bleeder**, a **default state on CLAMP**, or a **rail sequencing change**.

[M63] ME (2025-12-23 08:05):
But the other board I have works well

[M64] AI (2025-12-23 08:05):
That’s a really useful clue: if **an identical board works well**, then this is almost certainly **not “inherent to the design”**, but a difference in **startup conditions** or a **small leakage/assembly difference** on your problem board that makes the “floating AC-coupled node” behaviour show up.

Given everything you’ve described (sign depends on which rail comes up first, value varies, ~0.3 V clamp-ish level, disappears when the coupling cap is removed), the “good board vs bad board” split usually comes from one of these **common differences**:

## 1) Rail ramp / sequencing is different on the bad board
Even if you power them the same way, one board can ramp differently because of:
- extra load on +5 or −5
- a leaky IC/cap dragging one rail
- poor connection / higher resistance in one supply lead
- a regulator/decoupler issue

**Best test:** scope **+5, −5, and 0V** on *both boards* during power-up (same supply, same leads).  
If the bad board has a slower/lagging rail, you’ve found it.

## 2) One tiny leakage path on the “floating node” side
If that node is high impedance (especially with relays/switches open), then **µA** of leakage is enough to charge the coupling cap and park it at a clamp level. The good board might simply be cleaner / less leaky.

Causes:
- flux residue / contamination
- slightly damaged clamp diode/input structure on the receiving IC
- a leaky capacitor (less common if you already swapped)
- hairline solder bridge to a rail

**Fast test:** add a temporary **47 kΩ bleeder** to ground on the problem node on the bad board.  
- If it fixes the bad board but the good board never needed it → that strongly indicates a leakage/float sensitivity on the bad board.

## 3) Control defaults (DG412/relay control) differ between boards
If the control line that enables the DC path is:
- floating on one board due to missing pullup/down,
- or held in a different state because of a solder fault,
then one board will power-up “clean”, the other will be random.

**Test:** measure the **logic level** of the relevant control pin at reset/power-up on both boards.

---

## The quickest “A/B” diagnosis
Do this with both boards side-by-side:

1) Measure DC on the problem node after power-up (the ±0.3 V node).  
2) Power-cycle 5–10 times and note if it’s repeatable.  
3) Add **47 kΩ to ground** on that node on the bad board only.  
4) Repeat the power-cycle test.

**Outcomes**
- **Bleeder makes the bad board stable** → you’ve got a floating node + leakage/sequence sensitivity on the bad board (cleaning or adding a proper bias path fixes it).
- **Bleeder doesn’t help** → then it’s much more likely a **rail ramp** problem or a clamp path that overwhelms the bleeder (scope rails next).

If you can share which exact node it is (e.g., “right side of C4 at R81/R153 junction”) and what DC level the *good board* shows there at startup, I’ll tell you exactly what to compare next.

[M65] ME (2025-12-23 08:15):
[image]
So clamp comes from a pull down circuit. Therefore it depends on ic9 health to have this pinned right 
[attached file: IMG_76B096D0-A3F0-4142-9D28-4E271F790979.jpeg]

[M66] AI (2025-12-23 08:15):
I see why you’re thinking that, but **the −0.3 V you’ve marked is *after the series coupling capacitor C4***. That one detail means **IC9 cannot “pin it” at DC**, even if IC9 is perfect, because **C4 blocks DC**.

So the logic is:

- **IC9 + DG412 + R153** can set the **DC level on the *left* side of C4**.
- The **right side of C4** (your −0.3 V node) will only be pinned at DC if **something on the right provides a DC return/bias**.

If that right-side DC return is missing (or only present sometimes during power-up), the node will float and land wherever **clamp diodes/leakage** take it — often around **±0.3 V**, and sensitive to sequencing (exactly your symptom).

### The simplest proof (takes 1 minute)
Measure DC on **both sides of C4** in the “bad” state:

1) **Left side of C4** (between R153 and C4)  
2) **Right side of C4** (node you marked −0.3 V)

**If left side is sane but right side is ~−0.3 V**, IC9 is *not* the cause.

### Why the “good board” can behave differently
Two boards can differ in this floating behaviour because of tiny differences in:
- rail ramp timing,
- leakage/contamination,
- input clamp diode behaviour on the next stage,
- whether downstream circuitry is powered/biased early enough to provide a DC return.

### What will actually fix the right-side node (robustly)
Add a **bleeder** on the right side of C4 to the intended reference (often 0 V):

- start **100 kΩ to 0 V**
- if still drifts, **47 kΩ**
- if you need it solid, **10 kΩ**

That makes startup deterministic regardless of IC9 health or clamp timing.

### One nuance
DG412 being fitted/working only helps DC on the **left** of C4. It will not prevent the right side from floating unless the right-side network has a defined DC path.

If you tell me what **R81/RB** and the next stage input are (where that node goes on the right), I can suggest the best bleeder value/location that won’t mess with the clamp function when everything is assembled.

[M67] ME (2025-12-23 08:16):
[image]
Right side of c4
[attached file: IMG_400999BE-3C81-473E-AA38-B23D2E194286.jpeg]

[M68] AI (2025-12-23 08:16):
Yep — that **right side of C4** is exactly the node that will “remember” a random DC level if there isn’t a proper DC return. And on your schematic, that node goes straight into the **ADA4817** front end through **0 Ω links (R81/R301 etc.)**.

That’s the smoking gun:

- **ADA4817 inputs have ESD/clamp structures** to the rails.  
- During power-up (especially if +5 and −5 don’t track), those diodes will conduct briefly and will happily **charge C4** until the node lands at a diode-ish voltage like **~±0.3 V**.
- With no DC bleed path, it just sits there → varies run-to-run → depends on rail order.

### Why IC9 can’t be the thing “pinning” this node
IC9 is on the **left** of C4. C4 blocks DC. So IC9 can swing AC, but it can’t set the DC of the right-hand node unless there’s some separate DC path on the right (there isn’t one shown, aside from the ADA4817 input/clamps).

### What to do next (fast + definitive)

#### 1) Add a bleeder on the right side of C4
Tack a resistor from that node to **0 V**:

- Start **100 kΩ**
- If you still see it hang around tens/hundreds of mV, try **47 kΩ**, then **10 kΩ**

This will:
- stop the random ±0.3 V state
- make both boards behave identically
- remove dependence on rail order

#### 2) If you want it to settle quickly after power-on
The settling time is roughly \(R \times C\).

With **C4 = 10 µF**:
- 100 kΩ → τ ≈ 1 s (a few seconds to fully settle)
- 10 kΩ → τ ≈ 0.1 s (much quicker)

So if you need it to be “good immediately”, go lower.

### One caution
Make sure this bleed resistor doesn’t mess with your intended signal source when the clamp path is active. Because it’s on the **high impedance input node** feeding the ADA4817, you can usually get away with **47 k–100 k** without affecting anything important at AC.

---

### Why your “good board” can look fine without this
Tiny differences in:
- rail ramp rate,
- leakage,
- how quickly the ADA4817 rails come up,
- residual charge on C4,

…can make one board “usually” land near 0 and the other “usually” hit a clamp level.

But electrically, this node is inherently vulnerable unless it has a DC return.

If you try **47 k to ground** on that node and tell me what the DC becomes after power-up (and whether it’s now repeatable), we’ll have the answer in one step.

[M69] ME (2025-12-23 08:18):
[image]
It’s not on the left side of c4! It’s feeding into that node.
[attached file: 777A2930-ED16-4AB4-90EE-1FC9FEF7BBFF.jpeg]

[M70] AI (2025-12-23 08:18):
You’re right that **IC9 feeds into that node** *through* the chain (R12 → DG412 → R153), but **it still can’t control the DC level of the node you’ve marked because C4 is in series**.

Let’s name the nodes to make it crystal clear:

- **Node A** = IC9 output side / left of R12 (low-Z drive when IC9 is alive)
- **Node B** = after DG412 + after R153 **before** C4 (left plate of C4)
- **Node C** = **right side of C4** (the node you marked −0.3 V, going to R81/ADA4817)

IC9 (via DG412/R153) drives **Node B**.
But **Node C is separated by C4**, so at **DC**:

- Current through C4 = 0 (after transients settle)
- Therefore IC9 has **no DC authority** over Node C
- Node C will sit wherever **leakage / bias / clamp diodes on the right side** park it

IC9 *does* affect Node C during **transients** (power-up, switching), because C4 passes changing signals. That’s why it “seems like” it’s feeding it — it is, but only **AC / charge injection**, not DC regulation.

### Why you keep seeing ~±0.3 V specifically
That value is the signature of **a diode clamp** (ESD diode or protection structure) on the right-hand circuitry (ADA4817 input network, or anything tied to that node). During power-up the cap gets charged until a clamp conducts, then it stays there because there’s no DC bleed.

### The one measurement that settles the argument instantly
With the bad condition present, measure:

1) **Node B** (between R153 and C4)  
2) **Node C** (right side of C4)

You’ll almost certainly find Node B is near whatever IC9 is doing, while Node C is stuck around ±0.3 V (or wandering). That proves C4 is blocking DC control.

### Practical fix (and definitive test)
Add a bleeder on **Node C**:

- tack **47 kΩ to 0 V** from Node C (right side of C4)

If the −0.3 V “memory” disappears and becomes repeatable, you’ve proven the mechanism: **floating node + clamp during ramp**. IC9 can still be “feeding” the node in the AC sense, but the DC offset problem is on Node C’s side.

### If you’re worried IC9 is charging it the “wrong way” at startup
That’s possible (through startup transients), but the cure is still the same:
- either make Node C have a DC reference (bleeder), or
- ensure rails and clamp control come up in a defined way so the cap can’t get charged unpredictably.

If you tell me what you measure on **Node B vs Node C** right after power-up (same cycle), I’ll tell you exactly which clamp path is winning.

[M71] ME (2025-12-23 08:19):
[image]
The. Ode we are investigating at the indeterminebt values is marked R on this drawing. The right side of c4 
[attached file: DB695657-D86E-49FB-996F-8F078F69C4B3.jpeg]

[M72] AI (2025-12-23 08:19):
Got it — **node “R” = right side of C4** (the node that wanders and sometimes sits around ±0.3 V).

On that node, two things are simultaneously true:

1) **IC9 absolutely can inject charge into node R** (because it drives the left side of C4 through R153, and C4 passes transients).  
2) **IC9 still cannot *hold* node R at a defined DC value** unless there is a DC return path on node R itself (because at steady state, C4 is an open circuit for DC).

So what you’re seeing is: **C4 + node R behave like a “sample-and-hold”**. Whatever happens during power-up (rail sequencing, clamp diodes, switch/relay state, IC9 output transient) charges C4 and leaves node R “stuck” at an arbitrary DC level until it leaks away.

### Why the value lands near ±0.3 V
That is the tell-tale of **a diode clamp** on node R — very likely the input protection/clamp structures of the **ADA4817** stage that node R feeds (through the 0 Ω links). During ramp, those diodes conduct and pin the node around a diode drop.

### The fastest way to settle this (and fix it)
Put a **bleeder resistor on node R**.

- Start: **47 kΩ from node R to 0 V**
- If you want it to settle faster / clamp harder: **10 kΩ**
- If you want minimal loading: **100 kΩ** (slower settling)

This gives node R a DC “home” so it can’t keep a random charge.

**Time constant:** \( \tau = R \cdot C \) with C4 = 10 µF  
- 47 k → ~0.47 s (a couple seconds to settle fully)  
- 10 k → ~0.10 s

### A single measurement that proves the mechanism
With power on and node R sitting at, say, −0.3 V, tack **10 k to 0 V** on node R.

- If node R immediately moves toward 0 V and becomes repeatable across power cycles → confirmed: **floating node + stored charge**.

### One more subtlety: why the “good board” behaves
The good board likely has either:
- slightly different rail ramp / clamp timing, or
- lower leakage so node R naturally bleeds toward 0, or
- the downstream stage powers in a way that doesn’t forward-bias its clamps at startup.

But electrically, node R is still vulnerable unless it has a DC return.

---

If you tell me whether adding **10 k to ground at node R** makes it completely deterministic (and what the clamp DC becomes), I can tell you the best permanent value that won’t disturb your intended clamp waveform.

[M73] ME (2025-12-23 08:23):
Ok reset!!!
Ic9 creates a voltage or reference ground. It feeds into the clamp analogue switch dg412 which is defaulted to pull down at power up. The voltage or reference from ic9 passes through this switch and onto the node. So likely something wrong with this arrangement is not properly referencing it 

[M74] AI (2025-12-23 08:23):
Yes — *that arrangement* can absolutely be the root cause, but the key is **what “onto the node” means in your drawing**.

### The crucial detail
If the node you’re complaining about is **node R (right side of C4)**, then **IC9 cannot directly “reference” it at DC**, even if DG412 is ON and pulling down, because **C4 is in series**.

What IC9 + DG412 *can* do is set the DC of the **left side of C4** (the R153/C4 junction). Any “referencing” of node R then depends on **a DC return on node R’s side** (the ADA4817 input network, bleed resistors, etc.).

So there are two possible cases:

## Case A — You’re actually measuring node R (right side of C4)
Then your diagnosis becomes:

- DG412 default pull-down defines **left plate of C4**
- Node R is still free to float and will land where **downstream clamps** put it during ramp
- Rail sequencing makes it random

✅ Fix: add a **bleeder** on node R (47k–100k to 0V or to the intended bias reference), or ensure the downstream stage provides that DC path.

## Case B — The problem is on the left side of C4 (R153/C4 junction)
Then your new “reset” theory is spot on:

- IC9 must be healthy and stable
- DG412 must truly default to the pull-down state
- The CLAMP control must not be floating during power-up
- The pull-down destination must be a solid reference (0V/bias)

✅ Fix: force the DG412 control with a pull-up/down, verify the pull-down network, and verify IC9 output at startup.

---

# Do this one test to separate A vs B instantly
Measure three DC voltages right after power-up (same cycle):

1) **IC9 output** (pin 1)
2) **R153/C4 junction (left side of C4)**
3) **Node R (right side of C4)**

**Interpretation:**
- If (1) and (2) look correct but (3) is random/±0.3 → it’s Case A (floating node R).
- If (2) is also wrong/random → it’s Case B (DG412/default/reference issue).

No more debate after those three numbers.

---

## One more gotcha: “DG412 defaults to pull-down”
A DG412 **does not inherently default** to a pull-down. It defaults to **whatever the logic pin is** (and if that logic pin is floating during reset, the switch state can be random). So check:
- Is the CLAMP control pin held with a resistor at reset?
- Is the logic rail present early enough?

---

If you tell me what you get for those 3 voltages, I’ll tell you exactly which side is failing and the cleanest fix.

[M75] ME (2025-12-23 08:51):
What’s a well

[M76] AI (2025-12-23 08:51):
In this context, a **“well”** means a **defined, low-impedance reference node** that a circuit point can reliably settle to at **DC**, especially during **power-up**.

Think of it as a place where charge can **safely drain away** instead of being trapped.

### In practical circuit terms
A node is **“well referenced”** if it has:
- a **clear DC path** to ground, a bias voltage, or a rail  
- through a **resistor, active driver, or switch that is guaranteed on**

A node is **“floating”** (your problem case) if:
- it’s only connected through **capacitors**
- or through **switches/relays that may be open at reset**
- so it has **no DC escape path**

### Why this matters in your circuit
Your node **R (right side of C4)**:
- can receive charge through C4 during startup
- but **cannot get rid of it**
- so it “parks” at whatever voltage clamp diodes allow (≈ ±0.3 V)

That means it does **not** have a “well”.

### What a “well” looks like electrically
Any of these would count:

- **47 kΩ–100 kΩ to 0 V**
- **resistor to a mid-bias reference**
- **switch that is guaranteed closed at reset**
- **input of a stage that has a defined DC bias**

Without one, the node behaves like a **sample-and-hold capacitor**.

### One-sentence rule (very useful)
> If a node can ever be AC-coupled *and* disconnected by a switch, it must have a DC well — or startup will be nondeterministic.

### In your case
- IC9 + DG412 define the **left side of C4**
- **Nothing defines the right side**
- So node R has **no well**
- Rail order decides the final voltage

That’s why:
- power-up order flips the sign
- values vary
- removing C4 “fixes” it
- the good board “gets lucky”

If you want, I can suggest **exactly where and what value** to add to give node R a proper well without affecting bandwidth.

[M77] ME (2025-12-23 09:17):
[image]
Ok, I’ve removed the 0r resistors to the inputs. Still 0.3
[attached file: IMG_86FD71B5-7F34-436D-B822-6ED536D17444.jpeg]

[M78] AI (2025-12-23 09:18):
That’s a really strong result — and it narrows it down a lot.

If you’ve **removed the 0 Ω links into the ADA4817 inputs** (RB3 / R10 etc.) and the node is **still sitting around −0.3 V**, then the ADA4817 input clamps are **not** what’s pinning it.

So what can still hold that node at ~0.3 V?

### What remains connected to the node (from your schematic)
On the “problem” node you’ve marked (right side of the coupling cap, after **R157 1 k**), you still have:

- **R157 (1 k)** up to the DG412 path
- **the coupling capacitor** (C? 10 µF) *into* that node
- any **testpoint / pad leakage**
- and crucially: the **DG412 itself (IC6-B)** has **internal substrate/ESD diodes** to its supply rails and to logic domains

Even if the switch is “open”, those protection structures can clamp a floating node during power-up and leave it sitting at a diode-ish voltage.

Also: with the 0 Ω resistors removed, the node is now even **more floating**, so it will clamp even more cleanly.

---

## The single most decisive isolation step now
**Lift R157 (the 1 k) or lift the series coupling capacitor** so the node is completely isolated from the DG412 path.

- If you lift **R157** and the node immediately stops sitting at −0.3 V → the clamp path is coming **through IC6-B / its rails / its leakage**.
- If you lift **the coupling cap** and it stops → it’s being held by charge on that cap + leakage elsewhere.

Given you’ve already seen “remove the capacitor and it goes away” earlier, this is still consistent with a floating node, but the fact it **stays at exactly ~0.3 V** even when the ADA4817 is disconnected makes me suspect **the DG412 rail/ESD clamp path** (or something else still tied to that node).

---

## Two quick measurements that will pinpoint it without more desoldering
### 1) Measure **both sides of R157**
- Top of R157 (DG412 side)
- Bottom of R157 (node side)

If you see a DC drop across R157, then there’s real DC current flowing and you can compute it:
\[
I = \Delta V / 1k
\]

### 2) Measure DG412 supply rails at power-up
DG412 analog switch behaviour during ramp depends a lot on its supplies.
Check if its **V+ / V− / GND** are clean and come up together.

A mis-powered DG412 (or one rail missing briefly) can make its protection diodes conduct and “park” the node.

---

## Practical fix (even if you don’t chase the exact diode)
Even if the clamp path is via IC6 or some leakage, the robust cure is still to give the node a **DC well**:

- Add **47 kΩ–100 kΩ to 0 V** from that node.

Because your node is being held at ~0.3 V by some microamp-ish current, even 47 k will usually collapse it toward 0 V.

(If 47 k doesn’t move it, that means the clamp path is *stronger* than a µA — and then lifting R157 becomes the quickest proof.)

---

### What I’d do next
1) Measure both sides of **R157** (tell me the two voltages)
2) If needed, temporarily tack **47 k to ground** on the node and see if it drops from −0.3 V

Those two steps will tell us whether this is:
- **a weak leakage current** (bleeder fixes it), or
- **a hard diode clamp path** (isolate via R157 / DG412 rails).

[M79] ME (2025-12-23 09:23):
R157 - both sides discharging gradually together 

[M80] AI (2025-12-23 09:23):
That’s an excellent observation — and it basically confirms what’s going on:

✅ **There is no DC current through R157.**  
If both sides of R157 “discharge together”, the resistor isn’t dropping anything, so nothing is actively clamping/pulling through that path.

So the **−0.3 V is just stored charge on the coupling capacitor + a floating node**, bleeding away slowly through very small leakage paths (meter input, PCB contamination, switch leakage, etc.). The exact starting value (~0.3 V) is just where it *ended up* during power-up due to rail sequencing / transient clamp events, not because something is holding it there.

### Why it’s ~0.3 V and varies with power sequence
During ramp, some diode somewhere (could be in IC6, could be elsewhere, could be the next stage before you lifted 0R links) conducts briefly and charges the cap until a diode drop is reached. When things settle, the node is left floating and **remembers that charge**.

Then you measure later and see it slowly drifting back toward 0.

### What this means practically
There isn’t a “faulty part” necessarily — it’s a **missing DC reference** for that node when the relays/switch paths aren’t in their normal operating configuration (or during startup before control signals assert).

### The fix
Give that node a DC “well” so it can’t float:

- Tack **100 kΩ to 0 V** from the node (right side of the coupling cap).
- If you want it to discharge faster / be more deterministic, use **47 kΩ** or **10 kΩ**.

With C ≈ 10 µF:
- 100 k → τ ≈ 1 s
- 47 k → τ ≈ 0.47 s
- 10 k → τ ≈ 0.1 s

So even 100 k should stop the “stuck at random offset for ages” behaviour.

### One more very telling test
After you add the bleeder, power up:
- +5 first, then −5
- −5 first, then +5

If the node now always ends up near 0 V (and doesn’t “remember” ± offsets), you’ve proven conclusively it was a floating-capacitor startup memory effect.

If you tell me whether that node is *supposed* to be centred at 0 V or at some bias level during normal operation, I’ll tell you whether the bleeder should go to **0 V** or to a **bias reference** instead.

[M81] ME (2026-01-08 10:05):
Ok, I’ve resolved the issue… that quite likely was never really there. This all seems to be about start conditions and ensuring the pano stage is reliably referenced 

[M82] AI (2026-01-08 10:05):
Understood. That conclusion is consistent with everything you observed:

- The “offset” polarity flipping with **rail order**
- The value varying run-to-run
- The node slowly drifting (capacitor “memory”)
- Both channels behaving similarly
- Isolation tests showing no sustained DC current through the series resistor path

All of that points to **startup state + floating/AC-coupled nodes + clamp/bias structures**, not a hard component fault.

If you want to make it robust so it never reappears in a less controlled setup, the usual engineering actions are:

1) **Define the DC well** for any node that can be AC-coupled and momentarily disconnected (relay/switch open at reset).  
   - Add a high-value bleed to the intended reference (often 47–100 kΩ to 0 V or to the clamp bias reference).

2) **Force deterministic switch/relay states at power-up** (pull-ups/downs on control lines so DG412/relays are never floating during ramp).

3) **Bring ± rails up together** (or ensure the stage you’re referencing has its rails valid before it is connected to sensitive nodes).

4) Where practical, **match DC impedances** seen by op-amp inputs to minimise bias-current-induced offsets when inputs are otherwise floating.

If you tell me which node(s) you want guaranteed (e.g., “right side of C4” and/or the ADA4817 input summing node) and what its *intended* quiescent level is (0 V or a bias voltage), I can suggest a minimal set of resistors/pull defaults that won’t disturb your bandwidth or noise.

[M83] ME (2026-01-08 10:09):
[image]
Would the bleed not effect video performance?
[attached file: IMG_54729A6E-B0B6-42CB-BA27-6181F9EEE0E5.jpeg]

[M84] AI (2026-01-08 10:09):
Short answer: **no, not in any meaningful way** — *if you choose the value sensibly*.

Long answer, with numbers tied to **your exact node**:

---

## What that bleed resistor actually “does” in your circuit

You’re proposing something like **100 kΩ from node R (right side of C4) to 0 V**.

That node feeds:
- ADA4817 inputs through **0 Ω links**
- video bandwidth stages (×1 / ×2 / ×4)

At **DC**, the resistor simply provides a **well** so the node can’t float.

At **video frequencies**, the resistor is effectively invisible.

---

## Frequency impact (quantitative)

Your coupling cap is **C4 = 10 µF**.

The bleed forms a **high-pass corner** with C4:

\[
f_c = \frac{1}{2\pi R C}
\]

### For different bleed values:

| R_bleed | f_c |
|------|------|
| 100 kΩ | **0.16 Hz** |
| 47 kΩ | **0.34 Hz** |
| 10 kΩ | **1.6 Hz** |

Even **10 kΩ** only rolls off below **2 Hz** — utterly irrelevant for video (kHz–MHz).

---

## Noise and loading

### Loading
The ADA4817 input bias currents are in the µA range; the bleed resistor is far larger than any signal source impedance here, so it does **not** materially load the signal.

### Thermal noise of the bleed
Thermal noise of 100 kΩ:

\[
\sqrt{4kTR} \approx 40\ \text{nV}/\sqrt{\text{Hz}}
\]

But:
- it’s in parallel with a **low-impedance driven node** at video frequencies,
- the op-amp input noise dominates,
- and the high-pass nature pushes any effect to sub-Hz.

Practically: **completely negligible**.

---

## Why the “good board” works without it
The good board is just:
- getting lucky with rail ramp,
- or has slightly lower leakage,
- or clamps in a friendlier order.

The bleed makes the behaviour **deterministic** instead of “usually OK”.

---

## Best practice recommendation for *this* design
I’d do exactly what you sketched:

- **100 kΩ from node R to 0 V** (per channel)
- Place it physically close to C4 / the ADA4817 input node
- Treat it as a *startup bias / bleed*, not part of the video path

If you want faster settling after clamp release, go **47 kΩ**.

---

### One-line rule to keep
> Any AC-coupled video node that can be disconnected at reset **must** have a DC bleed — it costs nothing in performance and saves days of debug.

You’ve diagnosed this correctly. The bleed is the right, professional fix.

[M85] ME (2026-01-08 10:10):
[image]
The other thing would be to ensure the 0v and clamp are and enabled on startup? Discharging any anwanted charge
[attached file: IMG_35E5F581-CD8F-41DE-BA3D-E5088636C287.jpeg]

[M86] AI (2026-01-08 10:10):
Yes — ensuring the node is **actively referenced at startup** (and that any stored charge is discharged) is a valid approach. In practice, though, you want to separate two goals:

1) **Deterministic DC reference at all times** (prevents the problem)
2) **Fast discharge / known initial condition on power-up** (improves startup)

### 1) The “always works” fix: a bleed (your 100 k to 0 V)
That bleed gives the node a DC well regardless of control timing, relay fitment, or rail order. It is the most robust solution and generally the least risky.

### 2) Startup control: force CLAMP to a known state at reset
If you can guarantee the clamp switch/relay **is ON (or in “pull-down”) before the analogue rails and the following stages are in an undefined state**, then yes, you reduce charge injection and prevent the capacitor from being left with a random voltage.

Concretely:

- Put a **pull-down (or pull-up)** on the **CLAMP control line** so it defaults to the *safe* state while the CPLD/FPGA pins are Hi-Z during configuration.
- Make sure the logic rail that defines that default is present early (or use a resistor to 0 V rather than to a logic rail that may itself float).

This addresses the “sometimes OK, sometimes not” aspect caused by the switch state being undefined during ramp.

### 3) A dedicated discharge path (optional)
If you want the node to settle quickly after power-up or after clamp release, you can add an RC discharge path that does not load video:

- Keep the **100 k** bleed for DC determinism.
- If you need faster settling, reduce to **47 k** (usually still harmless).
- Or, if you have a spare switch pole, use it to momentarily connect the node to 0 V during reset (a true “reset discharge”).

### Practical recommendation for your board
Given you’re dealing with video bandwidth and you’ve already proven this is a **startup/charge memory** phenomenon:

- **Do the 100 k bleed** on the right side of C4 (per channel). This is your safety net.
- Also add a **defined CLAMP default** (pull resistor on the CLAMP control) so DG412/relays are never floating at reset.

That combination makes the system robust even if one of the two measures is delayed.

### One check to make sure you don’t create a new problem
If CLAMP control comes from a CPLD/FPGA that is 3.3 V but the DG412 control is on a different domain, ensure the default pull doesn’t accidentally forward-bias any protection diode (i.e., don’t pull a control pin above its supply when the supply is still at 0 V).

If you tell me what drives **CLAMP** (CPLD pin with internal pull? open drain? 3.3 V logic?) and whether DG412 logic supply is present at the same time as the analogue rails, I can specify the safest pull-up/down arrangement.

[M87] ME (2026-01-08 10:11):
So if we made that clamp voltage 0.5v. We are always reference and repeatable 

[M88] AI (2026-01-08 10:11):
If you set the clamp/bias so the node reliably comes up at **+0.5 V**, you *can* make startup repeatable — but only if you satisfy one condition:

**Node R (right side of C4) must have a DC path to that 0.5 V reference.**  
Otherwise, you’re still just “charging a capacitor during ramp” and it will still be sequence-dependent, just around a different point.

### Why “0.5 V clamp” alone is not sufficient
- IC9/DG412 define the **left side of C4**.
- C4 blocks DC.
- So the **right side** will only sit at 0.5 V if you provide a **bleed/reference** to 0.5 V on that side.

### The right way to do it
If you want node R to park at +0.5 V deterministically:

- Add **Rbleed from node R to the 0.5 V reference** (not to 0 V).

Pick value based on settling and loading:
- **100 kΩ** gives a very light “park” and long time constant (≈ 1 s with 10 µF).
- **47 kΩ** is a good compromise.
- **10 kΩ** makes it settle fast (≈ 0.1 s) but loads more.

This guarantees:
- repeatable DC level at startup
- predictable discharge of stored charge
- no dependence on rail order

### Will 0.5 V hurt video?
For an AC-coupled video chain, the DC level is normally removed by the coupling anyway. The only caveat is **headroom** and **clamp range** in the next stage:
- Ensure the ADA4817 stage and any clamp/protection network can accept +0.5 V common-mode without forward-biasing anything unintentionally.
- If the intended video baseline is 0 V, biasing at 0.5 V is fine as long as you have enough swing around it.

### A design note
Using **0.5 V** as the “well” can be preferable to 0 V if:
- you want to stay away from diode conduction around 0.2–0.4 V,
- you want a defined pedestal level,
- or your downstream stage expects a biased common-mode.

But the determinism comes from the **DC return path**, not from the chosen voltage.

If you tell me what generates the 0.5 V reference (DAC output? divider? bandgap?) and the expected video amplitude, I can recommend a resistor value that won’t affect gain/settling/noise in your clamp interval.

[M89] ME (2026-01-08 10:13):
[image]
So maybe it’s arrow A1 as opposed to arrow 2?
[attached file: IMG_371A9DEF-91DF-414B-9A3C-88E0708A64F8.jpeg]

[M90] AI (2026-01-08 10:13):
Yes — **Arrow 2 is the correct place for the “well” if your symptom is the indeterminate DC on the *right side of C4*** (the node you marked −0.3 V).

### Why Arrow 2 is correct
That wandering node is **downstream of C4**, so it is **DC-isolated** from everything on the left. A resistor at Arrow 2 provides the missing **DC return path** for that node and will stop the “charge memory” behaviour.

### Why Arrow 1 won’t solve the problem (on its own)
Arrow 1 is on the **left side** (before the DG412 / before the coupling cap path). A resistor there only references the **left plate** side. Because **C4 blocks DC**, Arrow 1 does not reliably set the DC of the right-side node.

Arrow 1 can still be useful for different reasons:
- it can define the DG412 input node during reset if that side can float,
- it can reduce charge injection effects,
- it can help if IC9/DG412 are ever Hi-Z and you want a defined input state.

But it will not stop the *right side of C4* from ending up at ±random values.

### Recommendation
- Fit **100 kΩ to 0 V at Arrow 2** (right side of DG412, same node as R153/C4 junction leading into the video chain’s input node after C4).
- If you also want belt-and-braces determinism during unusual switch states, you can optionally add a **higher value** (e.g., 100 k–1 M) at Arrow 1, but treat that as secondary.

### Quick sanity check
After adding the Arrow-2 bleed, do a few power cycles with:
- +5 first / −5 first
- fast on/off

If the node always comes up near the same DC (and doesn’t “stick” around 0.3 V), you’ve fixed the real mechanism.

If you tell me what the nominal clamp mode expects at that node (0 V pedestal or a non-zero bias), I can suggest whether the bleed should go to **0 V** or to the **clamp bias reference** instead.

[M91] ME (2026-01-08 10:16):
[image]
I envisaged that 
[attached file: IMG_6C229FF1-586C-42C7-BF28-8F29891F64E9.jpeg]

[M92] AI (2026-01-08 10:16):
Yes — what you’ve drawn is a reasonable mental model, but there’s one subtlety:

### What your sketch gets right
When **IC6-B (DG412) is closed** in the “pull-down” state, you’re effectively doing two useful things:

1) Providing a **low-impedance path** from the node (through **R157 = 1 k**) back to the clamp reference source (IC19 output), and  
2) Providing a **discharge route** for any stored charge via that path and the reference network.

So in *principle*, that can “park” the node.

### The catch
Even with the switch closed, your node is still **AC-coupled via the 10 µF capacitor (C?10u) to another net**. That capacitor can retain charge and re-inject it depending on what the other side is doing.

Also, during power-up:
- the DG412 may be **open** until its supplies and control are valid,
- IC19/IC9 may not be in a defined state yet,
- and the downstream stage input clamps may conduct first.

So “closed clamp” only guarantees discharge if it is **closed early enough** and the reference it connects to is already **valid**.

### Why the 100 k “well” is still valuable
The 100 k at the problem node is a **guaranteed DC return** that works even if:
- DG412 is open at reset
- relays aren’t fitted
- IC19/IC9 outputs are tri-stated or slewing
- rails come up in the “wrong” order

It doesn’t fight your clamp action; it just prevents the node from being a memory cell.

### Best practice for robust startup
If you want the behaviour you drew *every time*:

1) Ensure **DG412 control is defined** at reset (pull-up/down on CLAMP so it is not floating).  
2) Ensure **DG412 supplies are valid early**, or at least don’t lag badly.  
3) Add a **high-value well** (47–100 k) at the node so even if (1)/(2) don’t happen instantly, the node can’t wander.

### How to implement your intent with minimal impact
- Keep your existing clamp pull-down scheme.
- Add **100 k to 0 V** at the node (or to the clamp reference if you truly want a non-zero pedestal).
- Optionally add a **small cap (1–10 nF) to 0 V** at the node if you want to reduce susceptibility to charge injection during ramp (usually not necessary in video chains unless the node is extremely high impedance during reset).

If you tell me whether CLAMP is guaranteed asserted before the analogue rails are stable (and whether DG412 is powered from the same rails), I can tell you if you can rely on “closed clamp at startup” alone, or if the 100 k is effectively mandatory for deterministic behaviour.

[M93] ME (2026-01-08 10:18):
No problem with the 100k, just worried about defect on video. So glad is fast 15-20Mhz

[M94] AI (2026-01-08 10:18):
A **100 kΩ bleed will not degrade 15–20 MHz video performance** in any meaningful way in this topology.

### Why it won’t hurt bandwidth or amplitude
At 20 MHz, the impedance of your coupling capacitor **C4 = 10 µF** is tiny:

\[
|X_C|=\frac{1}{2\pi f C}\approx \frac{1}{2\pi\cdot 20\text{M}\cdot 10\mu}\approx 0.0008\ \Omega
\]

So for video, C4 is effectively a short; the node impedance is set by the driver/op-amp network and input network, not by the bleed resistor.

A **100 kΩ to ground** in parallel with that node is effectively an open circuit compared to any realistic video-path impedance (typically tens of ohms to a few kΩ).

### It only affects DC / very low frequency content
The bleed + C4 form a high-pass corner:

\[
f_c=\frac{1}{2\pi RC}
\]

With **R = 100 kΩ** and **C = 10 µF**:

\[
f_c\approx 0.16\ \text{Hz}
\]

So it only influences **sub-Hz baseline behaviour**, not 15–20 MHz video.

### Noise impact is negligible
Thermal noise of 100 kΩ is ~40 nV/√Hz, but in practice the node is driven by low impedance at video frequencies and the amplifier’s own noise dominates. You won’t see a measurable SNR hit from the bleed.

### What it *will* improve
- deterministic startup (no random ±0.3 V “memory”)
- faster recovery to a known baseline after clamp/switch events

### If you want an extra safety margin
Use **100 kΩ** as you propose. If you ever need faster settling, you can drop to **47 kΩ** without affecting video bandwidth either.

If you want, tell me roughly what the **video source impedance** into that node is (e.g., 75 Ω, 1 k, etc.) and I’ll sanity-check worst-case gain error—though with 100 k it will be essentially zero.

[M95] ME (2026-01-08 10:20):
47k

[M96] AI (2026-01-08 10:20):
47 kΩ is still entirely safe for 15–20 MHz video in your circuit.

### What changes vs 100 kΩ
- **Stronger DC well** (more deterministic)
- **Faster discharge/settling** after power-up or clamp events

Corner frequency with **C4 = 10 µF**:

\[
f_c=\frac{1}{2\pi RC}=\frac{1}{2\pi\cdot 47k\cdot 10\mu}\approx 0.34\ \text{Hz}
\]

So it only affects **sub-1 Hz baseline**, not video.

### Loading / gain impact
A 47 kΩ shunt on a video node is negligible unless your source impedance is also tens of kΩ (it won’t be in a 20 MHz chain). Relative to typical source impedances (tens of ohms to a few kΩ), 47 kΩ is effectively open.

### Practical recommendation
- Fit **47 kΩ from the right side of C4 (node R) to 0 V** on each channel.
- Place it physically close to that node (near C4 / the ADA4817 input area) to minimise any parasitic pickup.

If you want a quick confidence check after fitting: scope the node with a fast edge / test pattern and confirm no visible amplitude change or added ringing; in practice you should see no difference other than cleaner startup baseline.

[M97] ME (2026-01-08 10:50):
So where does that c4 charge come from?

[M98] AI (2026-01-08 10:50):
The charge that ends up on C4 (the coupling capacitor) during power-up comes from **transient currents flowing through the circuit as the supply rails and switches settle**.

In other words, at startup, the following factors contribute to that “mystery” charge:

1. **Power Rail Sequencing and Clamp Diodes:**
   When the ±5 V rails (or other supply rails) come up, **input protection diodes** on the downstream stage (like the ADA4817 inputs) may briefly conduct. These ESD/clamp diodes can pull current from the node, injecting a small charge onto the capacitor. Depending on which rail comes up first, the node might get nudged positive or negative before stabilizing.

2. **Analog Switch (DG412) State at Power-Up:**
   If the DG412 control line is floating or not yet defined at power-up, the switch may momentarily be in an undefined state. During that time, the node can drift and the capacitor can charge to some intermediate voltage. Once the switch is controlled or clamped, the node may already have a small residual charge.

3. **Op-Amp and Bias Currents:**
   Any small input bias currents or leakage currents from the op-amp (IC9) or other surrounding components can slowly charge the capacitor when the node is floating. Without a DC bleed, that tiny current has nowhere to go, so it accumulates on the capacitor.

4. **Capacitive Coupling from Adjacent Nodes:**
   During initial power-on, any rapid changes in nearby signals or nodes can capacitively couple into this node. That initial transient can place a tiny initial charge on the capacitor, which then “sticks” because there’s no immediate discharge path.

In summary, the charge on C4 is essentially a result of the **start-up transients, rail sequencing, and the absence of a defined DC path**. That’s why you see the node sometimes sit at around ±0.3 V (a typical diode forward voltage)—it’s simply the point where a protection diode or leakage path clamped the node during a brief power-up moment.

By adding the 47 kΩ bleed, you’re giving that charge a place to go, ensuring the node settles to a predictable DC level rather than holding a random offset. This eliminates the start-up variability you’ve been seeing. In normal operation at video frequencies, the bleed has no noticeable impact. It just ensures that at DC (including power-up), the node is no longer left floating. This is a standard and effective way to handle AC-coupled nodes that need a defined baseline.

[M99] ME (2026-01-08 11:00):
It’s on the right side of analog switch for now. But they may moan about that. The alternative is to have it on the left side and ensure there is a startup software scrip that sets the clamp bias to zero and closes the the analog switch to discharge startup stray charge. Then opens the switch when ready for operation?

[M100] AI (2026-01-08 11:00):
Putting the **47 kΩ on the right side** (node R, the video-chain side) is the **electrically correct** way to make that node deterministic. If someone “moans” about it, the technical argument is simple: **it provides the only guaranteed DC return for a node that is DC-isolated by C4**.

That said, your alternative (software-controlled discharge) can work, but it is **not as robust** unless you design it very carefully.

## Why “left side only + startup script” is fragile
Because the problem node is **right of C4**. Even if you:
- set clamp bias to 0 V, and
- close DG412,

you are only forcing the **left plate of C4** to 0 V. The **right plate (node R)** will only be forced to 0 V *if the right side has a DC path* (or if the switch is closed early enough and the right side isn’t being clamped elsewhere during ramp).

In practice, at power-up you can’t guarantee:
- DG412 is closed before rails are valid,
- clamp bias op-amp output is defined (not slewing),
- downstream input clamps won’t conduct first,
- CPLD/FPGA pins aren’t floating during configuration.

So the node can still get charged before your script runs, and then it **stays charged** because it’s floating.

## What I’d recommend (best engineering compromise)

### Option 1: Keep the 47 kΩ on the right side (recommended)
Pros:
- Deterministic regardless of firmware, relay fitment, or rail order
- Eliminates “random startup” completely
- No measurable impact at 15–20 MHz

Cons:
- Some people dislike “extra parts” on sensitive nodes (but electrically it’s benign)

### Option 2: If politics demand “no resistor on the video node”
Do a hybrid that remains hardware-deterministic:

1) Add a **very high value** on node R, e.g. **470 kΩ–1 MΩ to 0 V**  
   - Usually nobody objects to this
   - Still provides a DC well, just weaker/slower

2) Then do your **startup discharge procedure** in firmware:
   - Force **CLAMP control** to a known state at reset with a pull-up/down (hardware)
   - Close DG412 and set clamp bias to 0 V for X ms
   - Then open DG412 and proceed

This gives you robustness even if software is delayed, while still meeting the “don’t load video node” concern.

### Option 3: Pure software-only (least recommended)
Only acceptable if you can guarantee all of the following:
- DG412 supplies are valid early
- CLAMP logic is valid from reset (not tri-stated)
- clamp-bias op-amp output is valid early
- downstream stages do not clamp that node before your discharge runs

If any one of those is violated, you’re back to nondeterministic startup.

## A clean argument to justify the right-side resistor
At 20 MHz, 47 kΩ is effectively infinite. What it changes is only:
- DC
- very low frequency baseline (<1 Hz)

It is a standard “bleeder / bias return” for AC-coupled nodes.

---

If you tell me who “they” are (test/QA/design authority) and what their specific objection is (loading, noise, EMC, calibration purity), I can tailor the justification and suggest the least contentious value (e.g., 470 k vs 47 k) while still guaranteeing deterministic startup.

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] ME (2025-12-23 05:54):
Might be red herring, but there was some glue left from
The relay that joins the track and ground. This couldn’t been a good bases for leaky path.

[A2] ME (2025-12-23 07:55):
I fitted dg412

[A3] ME (2026-01-08 10:20):
So what’s best here 100k or 57k?
