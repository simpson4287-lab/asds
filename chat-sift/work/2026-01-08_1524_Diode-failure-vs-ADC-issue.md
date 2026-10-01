# Diode failure vs ADC issue
Date (UTC): 2026-01-08 15:24
Conversation ID: 695fcc02-8b00-8333-9a97-3d6c681fbb97
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-003.json

[M1] ME (2026-01-08 15:24):
[image]
What about here? Do you think that diode is gone or the adc below input out of alignment?
[attached file: C499A3B4-C89C-4C6F-9EAB-67CDE1421162.jpeg]

[M2] AI (2026-01-08 15:24):
Based on what you’ve marked and the topology shown, this looks much more like the **input clamp diode has failed (leaky / shorted)** rather than the ADC input itself being “out of alignment”.

Let me break it down in a disciplined way.

---

## What the circuit is intended to do

Each ADC input has:

- A **BAT54S dual Schottky** (to +1V8D and to 0V)
- The ADC input pin sitting between those clamps
- A local decoupled reference rail (+1V8D)
- No series resistor shown (important)

In normal operation:

- The ADC input should track the source (up to ~1.8 V)
- The BAT54 to +1V8D should only conduct if the input rises above ~1.8 V + Vf
- The BAT54 to GND should only conduct if the input goes below ~−0.2 V

So with a valid ~1.8 V input, **neither diode should be conducting**.

---

## Your observations

Left channel:
- ~1.8 V at ADC_IN
- Behaves correctly  
→ This is the control case

Right channel:
- Source looks correct upstream
- ADC_IN node collapses to:
  - ~1.25 V steady
  - ~0.5 V seen across the diode path
- Marked “Bad”

This is the key symptom.

---

## Why this points to the BAT54, not the ADC

### 1. The voltage levels match a Schottky failure signature

- **~0.45–0.55 V** is textbook BAT54 forward conduction
- **~1.25 V** strongly suggests:
  - Input is being **clamped through a partially shorted diode**
  - Likely the upper diode to +1V8D is leaky or shorted

If the ADC input itself were damaged:
- You would expect:
  - Rail-to-rail short (0 V or ~1.8 V)
  - Large input current
  - Crosstalk into adjacent ADC pins
- Not a clean Schottky-like clamp voltage

---

### 2. ADC input structures almost never fail “softly”

ADC ESD/input structures tend to fail in one of three ways:
- Open (floating, noisy)
- Hard short to VDD or GND
- Severe leakage causing gross loading

They do **not** normally create a neat ~0.5 V clamp unless:
- The external clamp diode is involved

The fact that the node lands at a **stable intermediate voltage** is a huge tell.

---

### 3. The symmetric channel comparison is decisive

You have:
- Same ADC silicon
- Same reference rails
- Same PCB layout
- One good, one bad

The only unique component per channel is:
- **That BAT54S**

This is classic “sacrificial protection diode did its job and died”.

---

## Likely failure mechanism

Very plausible causes:

- Input exceeded rails at some point (power sequencing, hot-plug, ESD, sensor transient)
- BAT54 conducted heavily
- Junction partially shorted afterwards
- Now behaves as a **permanent clamp**

Because there’s **no series resistor**, the BAT54 takes the full hit.

---

## How to confirm conclusively (quick bench checks)

### Test 1 – Remove or lift the BAT54
If you can:
- Lift the BAT54S (or just the upper diode pin)
- Re-measure ADC_IN

**If the node jumps back to ~1.8 V → case closed**

---

### Test 2 – Power off diode check
With power removed:
- DMM diode-test between ADC_IN and +1V8D
- Compare good vs bad channel

You will almost certainly see:
- Much lower forward voltage or leakage on the bad side

---

### Test 3 – Measure current into +1V8D
With the bad channel driven:
- Watch +1V8D current
- A leaky clamp will back-feed that rail slightly

---

## Is there any chance it’s ADC misalignment?

Practically: **no**.

ADC “alignment” issues show up as:
- Gain/offset error in conversions
- Digital codes wrong
- Not a **hard analog voltage clamp**

What you’re seeing is analog-domain behavior upstream of sampling.

---

## Design note (worth fixing long-term)

If this input ever sees:
- External connectors
- CMOS sensors
- Power sequencing uncertainty

You really want:
- **Series resistor (100 Ω – 1 kΩ)** before the clamp
- Or a **proper TVS** instead of BAT54s
- Or move the clamp to the sensor side

Right now, the BAT54 is the weakest and first-to-die part — exactly as observed.

---

## Bottom line

**High confidence conclusion:**
- The BAT54 clamp diode on the bad channel is damaged (leaky or partially shorted).
- The ADC input itself is almost certainly fine.

If you want, next step we can:
- Work out a robust replacement strategy
- Or decide whether to remove the clamp entirely and rely on ADC internal protection
- Or tune series resistance so this never happens again

Just say how far you want to take it.

[M3] ME (2026-01-08 15:50):
It seemed fine in the multimeter. Changed it a anyway 

[M4] AI (2026-01-08 15:50):
Understood—and that can happen. A DMM diode-test (or resistance check) often won’t reveal the exact failure mode you care about here.

Why it can “test fine” yet still be the culprit:

- **Leakage under bias**: The BAT54 can become leaky at the operating voltages/currents involved, but still look normal at the DMM’s low test current.
- **Dynamic/AC behaviour**: The ADC input is a sampled system (fast edge currents, charge injection). A diode that behaves at DC can still clamp or distort during sampling.
- **Partial short that is load-dependent**: Some Schottky failures only show up when the node is being driven from a low-impedance source or when the rail is present.

Since you replaced it anyway, the most useful next step is to make the outcome binary.

## After replacement: what changed?

1) **Does ADC_IN now sit at ~1.8 V (matching the good channel)?**
- If yes: you’ve effectively confirmed the diode as the fault, regardless of what the multimeter said.

2) **If it’s still wrong: isolate whether the ADC pin is loading it**
- Measure ADC_IN with the **driver disconnected/high-Z** (if you can lift a series link / disconnect the source).
  - If the node rises/floats normally with the source removed, the issue is upstream.
  - If it still gets dragged/clamped with the source removed, the load is local (ADC pin, solder bridge, or the clamp network/rail).

## Two quick checks that usually settle it

- **Compare +1V8D at that clamp to the good channel under the same conditions**  
  If the “bad” side +1V8D is sagging, noisy, or not actually at 1.8 V locally, the clamp can appear to conduct when it shouldn’t.

- **Thermal tell**  
  With the system powered (carefully), does the replaced area/ADC package run warmer than the good channel? A damaged ADC input that’s leaking significantly often shows up as heat or elevated rail current.

## Also worth doing (since you’ve been in that area)

- Inspect for **pad damage / micro-bridge** after rework. On BAT54S footprints it’s easy to leave a hairline solder whisker to the rail or ground pad.
- Confirm orientation: BAT54S pinout mistakes create exactly the kind of “mystery clamp” you described.

If you tell me one thing—**what is ADC_IN now after the diode change (and what are the two clamp rail voltages locally)?**—I can give you a very tight next diagnostic step and likely root cause.

[M5] ME (2026-01-08 16:10):
Forget that last bit. Measurement error.
My
Problem remains with one of the gain branches. The x11 gain usually runs up to 6000 counts on gain cal. But is only achieving 2500. What could that be?

[M6] AI (2026-01-08 16:10):
If the *high-gain branch* (your x11 path) is topping out at ~2500 counts when it normally reaches ~6000 on the same gain-cal stimulus, that is almost always one of three classes of problem:

1) **The x11 path is not actually x11** (effective gain reduced because the wrong feedback network is engaged, or a shunt/leak is present)  
2) **The x11 path is being bandwidth/settling limited** (so the sampled amplitude is lower than the true analog peak)  
3) **The x11 path is being attenuated/clipped/loaded before the ADC** (clamp, input network, switch leakage, RC, or bias/reference issue specific to that branch)

Below is a practical fault-tree that maps cleanly onto CCD/ADC front ends and switched-gain PGAs.

---

## 1) Wrong gain selected / gain-switch network fault (most common)

### What it looks like
- Low-gain branch behaves normally.
- High-gain branch gives a stable but reduced amplitude (often ~½ to ~⅓ of expected), with otherwise “sane” waveforms.

### Typical causes
- **Analog switch/FET not fully turning on** (gate drive missing, wrong logic level, broken trace, ESD-damaged switch).
- **Wrong resistor engaged** (open feedback resistor, cracked resistor, tombstone, wrong value in the x11 ladder).
- **Leakage path across the feedback element** (flux residue, contamination, ESD damage) effectively lowering feedback resistance and reducing gain.

### Quick checks
- Measure the **control pin** for the gain switch during x11 selection (scope if possible). Confirm it reaches the correct logic level referenced to the switch’s supply.
- Power off: measure the **feedback resistor(s)** in-circuit *comparatively* (good channel vs bad channel). Even if absolute readings are skewed, relative differences show opens/wrong value.
- If it’s a muxed ladder: check for **unexpected continuity** between nodes that should be isolated in x11 mode.

---

## 2) Settling / bandwidth / stability issue (very plausible in x11 only)

High gain reduces phase margin and increases sensitivity to:
- extra capacitance,
- changed compensation,
- longer routing,
- clamp diode capacitance,
- an op-amp that’s marginal or oscillating.

### What it looks like
- Peak amplitude reduced and/or counts “soft” compared with expectation.
- More reduction at higher pixel rates / faster sampling.
- Sometimes more noise, or a “hairy” baseline, or subtle oscillation you only see on a fast scope.

### Typical causes
- **Op-amp oscillation** in x11 mode: the ADC effectively measures a lower average because the waveform is unstable/ringing.
- **Compensation capacitor open/shifted** (or wrong value) in the x11 feedback network.
- **Added capacitance** on the input/output node (damaged clamp diode, rework residue, longer lead, etc.) causing under-settled sampling.

### Quick checks
- Repeat gain cal at **slower pixel clock / longer sample window** (if you can).  
  - If counts increase toward normal, it’s a settling/bandwidth issue, not a pure gain ratio issue.
- Scope the x11 output with enough bandwidth. Look for:
  - ringing at transitions,
  - sustained oscillation,
  - slow settling tail.
- Compare x1 vs x11 noise floor: oscillation often increases noise noticeably.

---

## 3) Attenuation/clamp/loading on that branch

Even if the diode tested “fine,” the high-gain path may be the only one that swings into a region where a clamp, bias network, or protection path starts conducting (or the only one that is routed through a particular series element).

### Typical causes
- **Clamp diode leakage or wrong rail reference** (local +1V8D not actually 1.8 V under load).
- **Series resistor/open** causing a divider with input impedance in x11 configuration.
- **ADC input network** (RC anti-alias/filter) wrong value or damaged on the x11 line only.
- **Bias/reference node** wrong on the high-gain amplifier stage (common-mode shift reduces usable swing).

### Quick checks
- Measure the **local rails** at the x11 stage (not “somewhere on 1V8”). Compare good vs bad under operation.
- Measure DC bias/common-mode at the op-amp inputs and output in x11 mode; compare to the good channel.
- If there is any **series element** into the ADC, measure both sides during a test pattern; a drop indicates loading/divider.

---

## 4) The op-amp itself has lost open-loop gain / drive capability (less common, but real)

An ESD or overvoltage event can partially degrade an amplifier. In high gain it shows first.

### Indicators
- Offsets/bias currents differ vs the good channel.
- Output can’t swing or drive the same load at x11.
- Behaviour worsens with temperature.

### Check
- Swap the op-amp between channels (if feasible) or compare output drive into a known load.

---

# A tight diagnostic sequence (minimal effort, maximum discrimination)

1) **Confirm the x11 path is being commanded correctly**
   - Log/measure the gain select lines during calibration.
2) **Slow the timing**
   - Reduce pixel rate / extend sample window and rerun gain cal.
   - If counts rise materially → settling/stability.
3) **Compare DC operating points good vs bad in x11**
   - Op-amp output DC level, input bias level, reference rails local to that stage.
   - Any big difference → component/rail/solder fault around that stage.
4) **Scope for oscillation**
   - Even a few mV of HF oscillation can collapse effective amplitude at the ADC.
5) **Component-value sanity checks in the x11 feedback network**
   - Particularly the feedback resistor and any parallel cap.

---

## One specific, high-probability culprit given your symptoms

If your “x11” result is ~2500 vs 6000 (about 0.42× of expected), that often corresponds to:
- the feedback ratio being wrong because **one resistor in the x11 ladder is open or not being switched in**, leaving you at an intermediate gain (e.g., ~x4–x5 instead of x11), or
- a **gain switch not fully enhanced** (effectively adding resistance in series with the intended feedback element).

That is why checking the gain-control signal integrity and the ladder/switch continuity is usually the fastest win.

---

## To narrow it decisively, tell me these three details

1) What ADC bit depth / full-scale is “6000 counts” relative to (e.g., 14-bit, 16-bit)?  
2) Does the x1 (or low gain) branch hit the expected counts on the same calibration?  
3) If you slow the pixel clock or extend the sample window, do the x11 counts increase?

Answering those will let me point you to the most likely single fault (switch/ratio vs settling/oscillation vs loading) and the exact node to probe next.

[M7] ME (2026-01-08 16:12):
I’ve proved that the x11 stage works as expected. It then goes into a second stage x1. This same x1 stage is shared with the other branches of the pre stage. 3 in total; x1, x2, x11.

[M8] AI (2026-01-08 16:12):
If the *x11 pre-stage itself is correct*, and everything then feeds a **shared second-stage x1**, yet only the x11 *system* result is low, the fault is almost certainly in the **handoff between x11 and the shared stage** (i.e., the selection/mixing network and the loading/settling conditions it creates), not in the shared amplifier core.

In practice, that narrows to a small set of mechanisms.

## What can reduce amplitude only for the x11 branch (even though the shared x1 stage is “fine” for x1/x2)

### 1) The x11-to-stage2 selection path is not truly low-impedance
Even if stage2 is shared, each branch typically reaches it via its own:
- analog switch / mux,
- series resistor,
- RC filter,
- clamp/protection,
- jumper/0R link.

A slightly **high series resistance**, a **half-driven analog switch**, or a **cracked 0R** can create a divider with stage2’s input impedance (or its sampling network), reducing amplitude. Because x11 has the largest signal / fastest edges, it can look worst there.

**Fast discriminant test**
- Measure the waveform **at the output of x11 stage** and **at the input pin of the shared x1 stage** *during x11 mode*.  
  If the amplitude drops across that link, you’ve proven it’s the interconnect/switch network.

### 2) The shared x1 stage is being driven into a different settling regime by x11
Even if x11 stage amplitude is correct, the *source impedance* or *bandwidth* seen by stage2 may be different in x11 mode (because the x11 path may have a different output network, compensation, or switch capacitance). If stage2 drives a sampling ADC (or a CDS front end), inadequate settling can show up as a lower measured peak.

**Fast discriminant test**
- Re-run gain cal with **longer acquisition/hold time** (or slower pixel/sample rate).  
  If counts rise toward normal only for x11, it’s a **settling / bandwidth / drive** issue at the stage2 input/output chain, not gain ratio.

### 3) A clamp/protection element conducts only for the x11 branch
Because x11 swings largest, it’s the one that will first:
- hit Schottky clamps,
- forward-bias ESD structures,
- exceed common-mode range of stage2 input,
- exceed input swing limits of the ADC driver.

This can happen even if you never reach the rail: a leaky clamp plus dynamic current spikes can “soft clip” peaks.

**Fast discriminant test**
- Scope the stage2 input and look for **flattening of peaks** in x11 mode.
- Also measure the local clamp rails during the event (e.g., +1V8D) for **kickback**.

### 4) Mux / selection logic overlap or partial selection
If, in x11 mode, the mux accidentally leaves another path partially on (or not fully off), you can load the x11 output with the x1/x2 network (often a lower impedance), pulling amplitude down.

**Fast discriminant test**
- During x11 selection, verify the **on/off states** of *all* branch select controls (not just “x11 = on”).  
- Check for any period where two selects overlap (timing hazard), especially around gain-cal transitions.

### 5) Wrong termination at stage2 input for x11 path (component-value drift)
It is common for each branch to have a different series resistor/RC into the common node. If the x11 branch has, say, a 1 k instead of 100 Ω (or a capacitor short/leak), you’ll get a consistent attenuation and/or bandwidth loss.

**Fast discriminant test**
- Compare the x11 branch input network values against the good channel (or against BOM): series R, shunt C, any 0R links.

---

## A tight, high-yield measurement plan (no guesswork)

1) **Probe 3 nodes simultaneously if possible**
- Node A: x11 stage output (immediately at op-amp output pin)
- Node B: stage2 input pin (after the mux / series elements)
- Node C: stage2 output (feeding ADC)

You’re looking for *where* the amplitude falls:
- A OK, B low → mux/series/termination/clamp between stages
- A OK, B OK, C low → stage2 stability/drive/headroom
- A shows clipping/tilt only in-system → loading from the handoff network

2) **Timing sensitivity check**
- Slow sampling / extend settling time and rerun.
- If x11 improves materially: it’s settling/drive or switch capacitance-related.

3) **Isolation check**
- Force the mux so only x11 is connected, and confirm x1/x2 are hard-off.
- If your design allows, temporarily remove/disable the other branch connections (lift 0R links) and see if x11 recovers.

---

## Most likely root cause given your architecture
With “x11 stage proven OK” and “shared x1 stage OK for other branches,” the highest-probability faults are:

1) **Analog switch / mux issue on the x11 branch** (not fully on, wrong supply, degraded Ron, gate not reaching rail)
2) **Wrong series/RC component on the x11-to-stage2 path** (value error, partial short, cracked resistor/0R)
3) **Soft clamp / loading on the x11 path** (Schottky/ESD/protection conducting only in that mode)
4) **Settling limitation due to higher source impedance / added capacitance in x11 path**

---

If you answer just these two items, I can tell you which branch of the tree you’re on and what to check next:

1) When you probe **stage2 input (node B)** in x11 mode, is the amplitude already reduced versus node A?  
2) If you slow the sampling/extend settling, do x11 counts rise significantly?

[M9] ME (2026-01-08 16:15):
[image]
At there is is a single relay contact. Test is shared 
[attached file: A4BBE59F-C72B-42E9-BFF9-7705741F833C.jpeg]

[M10] AI (2026-01-08 16:15):
Understood. With this topology, the “handoff” from each pre-gain op-amp into the shared node is **one relay contact per branch** (RL4-B for x1, RL5-B for x2, and the x11 branch uses its own relay contact on the same common bus). The post-bus network (R98 33 Ω and C3 100 pF) is shared.

If **x11 pre-stage output is proven correct** but the *delivered* amplitude at the shared node (and therefore ADC counts) is low only when the x11 relay is selected, then the highest-probability faults are very tightly constrained to:

## 1) The x11 relay contact path has gone high-resistance (most likely)
A reed relay contact can “look fine” on a DMM continuity check yet behave badly under real, fast analog conditions—especially if you’re sampling quickly and the source impedance is non-trivial.

**Mechanisms**
- Contact contamination / wear → tens to hundreds of ohms dynamic/contact resistance
- Marginal closure (coil drive low, wrong polarity, bad transistor) → intermittent/partial contact
- Cracked solder joint on the relay pin → behaves like a resistor/capacitor at speed

**What that would do**
- Creates an unintended divider with the bus load and whatever the next stage input impedance is
- Creates RC settling loss with C3 (100 pF) and any downstream sampling capacitance
- Produces exactly what you see: **counts reduced only for that branch**

**Fast proof**
- Scope **at the x11 op-amp output pin (before relay)** and at the **bus node (after relay, before R98)** during x11 mode.
  - If amplitude is good before, low after: it’s the relay contact/soldering/net.

## 2) You are unintentionally loading x11 with another branch (relay overlap)
If x11 relay closes but x1 or x2 relay is not fully open (or there is overlap in control timing), the x11 output will be loaded by the other amplifier/output network.

**Fast proof**
- In x11 mode, verify the **coil drive signals** for *all* relays: only the x11 coil should be energised.
- If you can, temporarily disable the other two relays (lift a coil drive resistor or pull the control low) and see whether x11 counts recover.

## 3) The bus network is fine, but x11 is uniquely sensitive to settling at that node
Even with a perfect relay, x11 might be the only branch that drives this node with a source impedance / bandwidth that interacts badly with:
- C3 100 pF
- R98 33 Ω
- the next stage / ADC sampling capacitance

However, you said you’ve proven x11 stage “works as expected” — the key is whether you proved it **under the same load** (i.e., driving through the relay into the bus), or just on its local output.

**Fast proof**
- Slow the sampling / extend acquisition time. If x11 counts rise materially, it’s settling rather than pure attenuation. If they don’t, it’s almost certainly relay/contact/connection.

---

# The single best diagnostic action
Measure the **voltage drop across the relay contact** in x11 mode under a steady calibration signal:

- Put probe A on the **op-amp output pin** (relay input)
- Probe B on the **bus node** (relay output)

If you see a meaningful delta (even 100–300 mV on a ~1–2 V signal), that relay contact path is not healthy.

---

# Quick “swap” test if the PCB permits
If RL4/RL5 are identical parts and footprints:
- swap the *relay devices* between a known-good branch and the x11 branch, or
- reroute controls temporarily (force x11 using the x1 relay path) if there are test points or bodge options.

If the fault follows the relay/contact, you have a definitive root cause.

---

If you tell me one thing, I can be exact about the next step: when x11 is selected, is the **bus node** (the junction feeding R98) already low compared to the x11 op-amp output, or is it only low after R98 / at the ADC driver? That splits “relay/contact” versus “settling/next-stage load” immediately.

[M11] ME (2026-01-08 16:22):
So if I
 Expecting around 6000 and getting nearly 3000. Then suspect whatever’s happy inf is a divide by 2?

[M12] AI (2026-01-08 16:22):
A ~6000 → ~3000 drop is consistent with an *effective* divide-by-two, but you should treat it as a **strong hint**, not a guarantee of a literal 2:1 resistor divider.

In this architecture (op-amp → relay contact → shared node → 33 Ω / 100 pF → next stage/ADC), the ways you get “about half” typically fall into three buckets:

## 1) True attenuation from a divider (very plausible)
This happens if, in x11 mode only, you’ve introduced a series resistance that is comparable to the load impedance at the shared node.

Common causes:
- **Relay contact has gone resistive** (or cracked solder joint on relay pin).
- **Unexpected series resistance** in the x11 path (track damage, via crack, 0R link gone high, etc.).
- **Parallel load accidentally present** (another relay partially on, or the x11 node is tied into another network).

Why it looks like ÷2:
- If your “added series R” ≈ the effective input impedance seen at the bus, you get ~half amplitude.

## 2) Sampling/settling loss that *presents* like ÷2 (also plausible)
If the waveform at the shared node is not settled by the time the ADC samples, the measured peak can be roughly half even though the steady-state analog value would be correct.

Causes:
- Relay/contact resistance + C3 (100 pF) + ADC sampling cap → too much RC.
- Stage driving the bus is marginally stable in x11 path and has slow settling tail.

Tell-tale:
- If you slow the sample clock or extend acquisition, the measured counts rise toward normal.

## 3) Gain selection logic error upstream (less likely given your earlier proof)
If you were actually measuring an intermediate gain rather than x11 (e.g., x5–x6), you can land near half. But you’ve said x11 stage is behaving as expected, so I’d prioritise the interconnect/selection and settling.

---

# The decisive check (do this next)
In x11 mode, measure *amplitude at two nodes*:

1) **Before the relay** (x11 op-amp output pin)
2) **After the relay** (the common bus node feeding R98)

Interpretation:
- **Before relay ≈ expected, after relay ≈ half** → divider/contact/connection (relay path problem).
- **Before relay ≈ expected, after relay ≈ expected, but ADC counts ≈ half** → settling/next-stage/sampling issue.
- **Before relay already low** → your “x11 proven good” test didn’t replicate the real load condition.

If you can only do one measurement, do the bus node (after relay) with an analogue scope during gain cal.

---

# Practical expectation
Given you have a **single relay contact per branch** and only one branch is affected, a “÷2-like” result most often comes from:
- **high-resistance relay contact** or
- **a poor solder joint / via** on that contact path,
creating a voltage divider into the shared node and/or an RC settling deficit.

If you confirm the halving occurs across the relay, your next action is straightforward: reflow relay pins, inspect/measure continuity under flex, and if still present, replace that relay.
