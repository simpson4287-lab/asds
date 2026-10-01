# OS Current Measurement
Date (UTC): 2026-03-04 16:51
Conversation ID: 69a862ba-f250-8387-917f-0707ee87c851
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-04 16:51):
I gave a requirement to measure the os current of ccd. The os goes through a follower with collector connected to id. Sounds like they want the first and second stage measurement 

[M2] AI (2026-03-04 16:51):
Yep — that reading makes sense, and it’s a very common “gotcha” with CCD OS/OD biasing.

If your **OS current** is flowing through a **follower stage where the follower transistor’s collector is tied to ID (or another upstream rail)**, then a single “measure OS current” requirement is ambiguous, because there are *two physically different currents you could mean*:

## 1) True OS pin current (at the CCD OS/OD pin)
This is the current actually sourced/sunk by the **CCD OS node itself** (what the device pin is doing). This is the one you usually want for:
- verifying CCD biasing is within datasheet limits
- correlating with blooming / charge handling / odd OS behaviour
- device health / leakage checks

**How to measure:** put the measurement element *in series with the CCD OS pin feed* (Kelvin sense if you care about µA/mA accuracy). This point is “before” any buffering transistor path splits.

## 2) “Follower stage” current (buffer / transistor path)
Once OS is routed through a follower, the **stage current** can include:
- **base/gate drive current** (if BJT base current exists)
- **collector/emitter current** that may be drawn from **ID** (because collector is on ID)
- bias network currents (pulls, clamps, protection, etc.)

So the “OS current” someone might ask for could actually mean:
- “How much does this OS driver/buffer load the ID rail?” (power/thermal budget)
- “Is the follower biased correctly?” (stage health)
- “Is OS doing something weird or is it the follower?” (debug separation)

**How to measure:** measure in series with the **follower’s supply leg** (e.g., the collector feed from ID), and/or the emitter/source leg depending on topology.

---

# What they likely mean by “first and second stage measurement”
In your wording:

- **First stage** = current associated with the **CCD OS pin feed** (true OS current).
- **Second stage** = current associated with the **follower stage whose collector is on ID** (i.e., incremental current pulled from ID because OS is being driven/buffered).

That interpretation is consistent with “collector connected to ID” — because that topology makes it *very easy* to confuse “OS current” with “ID rail current caused by the OS buffer*.

---

# How I’d rewrite your requirement so nobody can misread it
Use two explicit requirements:

1. **OS_PIN_CURRENT:** *Measure the current delivered into the CCD OS pin (series measurement in the OS bias feed at the CCD pin), excluding any downstream buffer stage supply currents.*

2. **OS_BUFFER_SUPPLY_CURRENT:** *Measure the current drawn by the OS follower/buffer stage from the ID rail (series measurement in the follower collector feed from ID), to allow separation of CCD pin current from buffer loading.*

Optionally add:
- “Simultaneously sampled” if they want correlation
- expected range / resolution (µA? mA?) and bandwidth (DC only? slow logging?)

---

# Practical note (important in CCD land)
If you insert a shunt in the OS pin feed, you can unintentionally add compliance drop/noise into OS. So usually you want either:
- a **very low-ohm shunt + amplifier**, Kelvin sense, and maybe place it upstream with a dedicated sense lead to the CCD pin, or
- a **high-side current monitor** with appropriate common-mode and noise performance.

---

If you paste the exact follower snippet (even just: BJT/MOSFET type + where emitter/source goes + any resistors), I’ll tell you *exactly* where the two measurement points should go so you get clean separation without disturbing the OS bias.

[M3] ME (2026-03-04 17:15):
So I measure across base resistor?

[M4] AI (2026-03-04 17:15):
Short answer: **no — measuring across the base resistor will only give you base current**, not the OS current they probably care about.

Let’s walk through the topology you described.

You said:

- **OS → follower**
- **collector connected to ID**

That strongly suggests a **BJT emitter follower** like this:

```
        ID
         |
         |
      C  |
        |\
OS ----Rb-| B
        |/
      E
         |
       output / load
```

Where:
- **Rb** = base resistor from OS
- **collector** tied to **ID**
- **emitter** provides the buffered OS level

---

# What you get if you measure across the base resistor

If you measure the voltage across **Rb**:

```
I_base = V_Rb / Rb
```

That gives **base current only**.

But the transistor current relationship is:

```
I_emitter ≈ β × I_base
I_collector ≈ I_emitter
```

So the **actual stage current is much larger** than the base current.

Example:

If β = 100 and:

```
I_base = 10 µA
```

Then:

```
I_collector ≈ 1 mA
```

So measuring the base resistor would **massively underestimate the current** being drawn from ID.

---

# Where the useful measurements actually are

## 1️⃣ True OS pin current

Measure **in series with the OS line** before the base resistor.

```
OS ---- Rsense ---- Rb ---- base
```

Then:

```
I_OS = V_Rsense / Rsense
```

This tells you what **the CCD OS pin is supplying**.

---

## 2️⃣ Follower stage current (from ID)

Measure **in series with the collector feed**.

```
ID ---- Rsense ---- collector
```

Then:

```
I_stage = V_Rsense / Rsense
```

This tells you **how much current the follower stage is pulling from the ID rail**.

---

# Why they probably want both

Because they answer **different questions**:

| Measurement | What it tells you |
|---|---|
| OS pin current | CCD bias behaviour |
| follower collector current | load on ID rail |
| base resistor current | transistor drive current |

---

# In CCD test electronics (important point)

Usually the **OS current requirement means the first one**:

**current flowing into the CCD OS pin**

because that’s what affects the sensor operation.

The follower current is normally just **driver overhead**.

---

✔️ **Rule of thumb**

If the requirement literally says:

> *Measure OS current*

then measure **in series with the OS pin feed**, **not across the base resistor**.

---

If you want, sketch or send the **exact circuit fragment**, because CCD OS drivers sometimes use **cascode followers or MOS followers**, and the correct measurement point changes slightly.

[M5] ME (2026-03-04 17:34):
[image]
So at these two positions?
[attached file: IMG_F6DF56F6-605C-432B-BDD1-1C326A13FF3D.jpeg]

[M6] AI (2026-03-04 17:35):
From what I can see in your snippet: **yes — those two “in-line” positions on the left (OD_CCD path near P54 and OS_CCD path near P58 / OS0_CCD) are the right places to measure the *CCD pin* current**.

### What those two positions give you
- **OD_CCD (P54 → R135 330R → rest of network):**  
  If *all* OD pin current flows through **R135**, you can simply measure **V across R135** and calculate:  
  \[
  I_{OD\_PIN} = \frac{V_{R135}}{330\ \Omega}
  \]
  (This is often the nicest way because you don’t have to “break” the net.)

- **OS_CCD (P58 → your series link/shunt position → OS0_CCD → rest):**  
  That position is the equivalent “CCD pin current” measurement point for OS — **provided OS_CCD doesn’t have any other parallel feed path** that bypasses the shunt/link.

### What those positions do **not** give you
They do **not** give you the “second stage” / follower loading current from **ID**.

In your diagram the follower/base drive goes via **R142 (100R)** into the transistor. Measuring across **R142** only tells you **base drive current (and edge/transient behaviour)** — not the collector/ID current.

### If they truly want “second stage current”
Add/measure a shunt **in series with the follower’s supply path**:
- i.e. **between ID and the transistor collector node** (or whatever rail is feeding that follower stage).

That separates:
- **CCD OS pin current** (your left shunt)
from
- **buffer/follower supply current** (ID shunt)

If you want, zoom a touch to show where the transistor collector ties to **ID** on the right, and I’ll point at the exact net to break / where to put the shunt so it doesn’t get bypassed.

[M7] ME (2026-03-04 18:00):
What’s a typical ccd output current? I’m going through a x500 amplifier. What resistor ball park?

[M8] AI (2026-03-04 18:01):
It depends *which* “CCD output current” you mean:

- **Video output signal current (the sense node itself):** typically **tiny** (µA-ish). You normally treat it as a **voltage source with some output impedance** rather than “a current you measure”.
- **CCD on-chip output amplifier / OD/OS bias currents:** typically **mA-ish** (order of **1–10 mA**, sometimes **tens of mA** on some parts / higher speed modes). That’s usually what people mean when they say “output drain current / output stage current”.

Given you’re talking about **measuring current** and you’ve got a **×500 amplifier**, you’re almost certainly building a **shunt + gain** current monitor. In that case, the right way to choose the resistor is based on **allowed voltage drop** and **max expected current**, not on some “typical” number.

## Pick the shunt by allowed drop (good rule)
Decide what drop you can tolerate in the bias feed (often **50–200 mV max** to avoid messing up the bias).

Then:
\[
R_{shunt} \approx \frac{V_{drop,max}}{I_{max}}
\]

### Practical ballparks (very usable)
If you design for **100 mV at full-scale**:

- If \(I_{max}=10\text{ mA}\) ⇒ **R ≈ 10 Ω**  
- If \(I_{max}=20\text{ mA}\) ⇒ **R ≈ 5 Ω**  
- If \(I_{max}=50\text{ mA}\) ⇒ **R ≈ 2 Ω**  
- If \(I_{max}=100\text{ mA}\) ⇒ **R ≈ 1 Ω**

That’s the “normal” region for shunt sensing in bias rails.

## What ×500 gain implies for resistor choice
With gain **500**, even small shunt voltages become big:

- 1 mA through **10 Ω** ⇒ 10 mV ⇒ ×500 = **5 V** (already near rail!)
- 10 mA through **10 Ω** ⇒ 100 mV ⇒ ×500 = **50 V** (impossible)

So with ×500 you generally want a **much smaller shunt** or you only expect **sub-mA**.

### Therefore, two sensible starting points
- Expect **a few mA to tens of mA** (common for OD/OS/output stage supply currents):  
  **Rshunt = 0.5 Ω to 5 Ω** (and ×500 may be too high unless you clamp/scale)
- Expect **tens to hundreds of µA** (true “pin leakage / tiny current” measurement):  
  **Rshunt = 10 Ω to 330 Ω** can make sense with ×500

## Quick sanity check you can do right now
Tell me two numbers and I’ll give you a clean resistor + scaling suggestion:
1) **Max current you want to measure** (guess is fine: 1 mA / 10 mA / 50 mA?)  
2) **Max drop you can tolerate** in that rail (e.g., 50 mV, 100 mV, 200 mV)

If you don’t know, a safe engineering default for CCD bias rails is:
- assume **Imax = 20 mA**
- allow **Vdrop = 100 mV**
→ **Rshunt ≈ 5 Ω** (and you’d typically use **gain ~20–50**, not 500)

One more key question: is the ×500 stage measuring **across the shunt directly**, or is it part of a bigger chain (filtering/ADC scaling)?

[M9] ME (2026-03-04 18:04):
Second stage 10ma. Got that covered. Just wondering about the raw os. Say 1mA max?

[M10] AI (2026-03-04 18:04):
If you want to treat the **raw OS pin current** as **up to ~1 mA max**, then yes — you can design a shunt around that and it becomes very manageable.

### Pick a shunt that doesn’t disturb OS bias
For CCD bias pins (OS/OD), I generally try to keep the added drop small-ish:

- **Target full-scale drop:** 50–100 mV (nice compromise)

So for **Imax = 1 mA**:

- **50 mV FS:** \(R = 0.05 / 0.001 = 50\ \Omega\)
- **100 mV FS:** \(R = 0.1 / 0.001 = 100\ \Omega\)

**Ballpark:** **47 Ω to 100 Ω** is a sensible starting range.

### Check against your ×500 gain
With gain = 500:

- **1 mA × 50 Ω = 50 mV** → output = **25 V** (will rail hard)
- **1 mA × 10 Ω = 10 mV** → output = **5 V** (borderline, depends on supply/headroom)
- **1 mA × 4.7 Ω = 4.7 mV** → output = **2.35 V** (comfortable)
- **1 mA × 2 Ω = 2 mV** → output = **1.0 V** (very safe)

So if you **must keep ×500**, your shunt wants to be more like:

**~2 Ω to 10 Ω**, depending on ADC range and amplifier rails.

### Recommended “just works” numbers
Assuming you want **1 mA FS** and an output in a sane range:

- If your measurement chain likes **~2.5 V full scale**:  
  pick **Rshunt ≈ 5 Ω** (1 mA → 5 mV → ×500 = 2.5 V)

- If your ADC is **0–5 V** and you want near full use:  
  pick **Rshunt ≈ 10 Ω** (1 mA → 10 mV → ×500 = 5 V)

That also keeps OS drop tiny (5–10 mV at 1 mA), i.e. it won’t perturb the bias.

### Power rating (easy)
At 1 mA:
- even 100 Ω is only \(I^2R = 0.001^2×100 = 0.1\ \text{mW}\)
So power is irrelevant; choose for tolerance/tempco/connection style instead.

---

**So:**
- If you want minimal disturbance and to suit ×500: **5–10 Ω**.
- If you didn’t have ×500 and wanted easier sensing: **47–100 Ω**.

If you tell me your amplifier supply rails and ADC input range (e.g., 0–2.5 V, 0–3.3 V, ±1.25 V), I’ll pin it to one exact value and suggest any clamp/filter so it doesn’t saturate on transients.

[M11] ME (2026-03-04 18:05):
The part has good bandwidth. Also though a 2c cmr 

[M12] AI (2026-03-04 18:05):
Got you. If the amp has **good bandwidth** *and* you’re relying on **CMR (common-mode rejection)** (I think your “2C CMR” comment is basically *

[M13] ME (2026-03-04 18:06):
2V cmr

[M14] AI (2026-03-04 18:06):
Ah — **2 V common-mode range** changes the game.

If your current-sense amplifier only tolerates **~2 V of input common-mode**, then you **cannot** directly measure a shunt that is sitting on a node that can sit at (say) **10–30 V OS bias**. The amp inputs would be riding at that common-mode, and it’ll either saturate or misbehave.

### What that implies
- **Low-side shunt (near 0 V)** ✅ works with 2 V CMR  
- **High-side shunt (OS rail at tens of volts)** ❌ won’t work with 2 V CMR (unless you level-shift)

So you need to decide *where* you’re measuring OS current:

## Option A — Low-side sense the OS return path
If OS current ultimately returns to **0 V through a defined resistor/network** (or you can route it that way), put the shunt **in the return leg** so both inputs stay near ground.

Pros:
- Compatible with your 2 V CMR amp
- Easy, stable, no special parts

Cons:
- Only valid if **all OS current returns through that leg** (no alternate ground returns), otherwise it lies.

## Option B — Use a proper high-side current-sense amplifier
If you truly need the shunt in series with **OS at the CCD pin**, and OS can be high voltage, you want a device specified for **high common-mode** (often 36–80 V depending on part).

Pros:
- Measures “true” OS pin feed current where you want it
- Doesn’t disturb your grounding scheme

Cons:
- Different IC, different error terms (gain/offset), sometimes more noise

(Your existing “good bandwidth” amp doesn’t help if it simply can’t tolerate the common-mode.)

## Option C — Level shift / difference amp with resistor network (only if you’re careful)
You *can* build a diff front-end that attenuates the common-mode (matched dividers into the diff amp), but for accurate current measurement you’ll be fighting:
- resistor matching / tempco
- CMRR degradation
- noise pickup at high impedance

I’d only do this if you’re forced.

---

# Practical recommendation for your case (CCD OS)
Because OS can be up to ~30 V (your schematic even hints “FOR 30V OS MAX”), **assume OS common-mode can be high**.

So either:
1) **move the measurement to a low-side return** (best if topology allows), or  
2) **swap the sensing element to a high-side current sense IC**.

---

# Quick check to lock it down
In your snippet I saw OS has a pull-down-ish network (e.g., the 5k6 to 0V), but the OS pin feed itself is sitting at OS potential.

If you answer just this, I can tell you which option is cleanest:

- When OS is biased up (e.g., 20–30 V), does the **OS pin current return to 0 V mainly through that 5k6 path**, or does it return elsewhere (through the CCD / other bias pins / internal structures)?

If it’s **mostly that defined path**, then **low-side shunt in the return** is a really tidy solution with your 2 V CMR amp. If not, go **high-side current sense IC**.

[M15] ME (2026-03-04 18:07):
It’s a differential current sense amplifier.

[M16] AI (2026-03-04 18:07):
Yep — but “differential” doesn’t automatically mean “high-side capable”.

A **differential (current-sense) amplifier** still has two separate limits:

1) **Differential input range** (e.g., ±50 mV, ±100 mV across the shunt)  
2) **Input common-mode range (VCM)** (the average of the two shunt terminals)

Your earlier note “**2 V CMR**” reads like the **allowed common-mode range is only ~2 V** (typical of lots of fast op-amp diff stages / instrumentation front ends that are *not* true high-side current sense parts).

### The key check (do this on the datasheet)
Compute:
\[
V_{CM}=\frac{V_+ + V_-}{2}
\]
For a shunt in the OS feed, both \(V_+\) and \(V_-\) sit near the **OS bias voltage** (say 10–30 V), so \(V_{CM}\approx 10–30\text{ V}\).

If your amplifier’s allowable \(V_{CM}\) is only up to ~2 V, it will saturate even though the shunt drop is only millivolts.

### So, two cases

#### Case A — It’s a *true current-sense amplifier* (high-side)
These are designed for high common-mode (e.g., 26 V / 36 V / 60 V / 80 V).  
Then you *can* place the shunt in the OS feed and you’re fine.

#### Case B — It’s a generic differential / instrumentation stage
Often the inputs must stay near the amplifier supply rails (e.g., 0–5 V), so you **must**:
- sense **low-side** (near 0 V), or
- change the front end to a high-side current sense IC.

### What I need from you to answer definitively
What’s the **part number** of the “differential current sense amplifier”?

If you don’t have it to hand, tell me:
- its **supply voltage** (3.3 V? 5 V? ±5 V?)
- the datasheet line for **input common-mode range** (sometimes called “VICM”, “common-mode input voltage range”, or “input voltage range”).

### Meanwhile, practical guidance for your earlier “1 mA OS max”
- If you **can** sense high-side: choose **5–10 Ω** with your ×500 gain (1 mA → 2.5–5 V out).
- If you **cannot** sense high-side: place the shunt in the **OS return path to ground** (so VCM is <2 V), still **5–10 Ω** works nicely.

If you paste the amplifier PN (or a screenshot of that datasheet section), I’ll tell you straight away whether it’s Case A or B and where the shunt must go.

[M17] ME (2026-03-04 18:10):
Max4173

[M18] AI (2026-03-04 18:10):
MAX4173 is a **proper high-side current-sense amp** — its **input common-mode range is 0 to +28V (independent of supply)**, so your earlier “2V cmr” worry doesn’t apply to this part. citeturn0search0turn0search3

Now for **raw OS current ~1 mA max**: pick the shunt from two constraints:

## 1) Don’t exceed MAX4173 sense input range
MAX4173 is designed around a **full-scale sense voltage of ~150 mV** (across RSENSE). citeturn0search7  
So absolute upper bound:
\[
R_{SENSE} \le \frac{150\text{ mV}}{1\text{ mA}} = 150\ \Omega
\]

## 2) Don’t disturb the OS bias
OS is usually a “biasy” pin; you generally don’t want to drop a lot of voltage in series with it. So a practical target is more like **10–50 mV** at full scale:

- **10 mV @ 1 mA ⇒ 10 Ω**
- **25 mV @ 1 mA ⇒ 25 Ω**
- **50 mV @ 1 mA ⇒ 50 Ω**

That’s a very sane ballpark.

## What voltage will you get out?
MAX4173 comes in fixed gain versions: **20 V/V (T), 50 V/V (F), 100 V/V (H)**. citeturn0search0turn0search3

\[
V_{OUT} = G \cdot (I \cdot R_{SENSE})
\]

So at **1 mA**:

### If you have MAX4173T (20 V/V)
- 10 Ω → 10 mV sense → **0.2 V out**
- 25 Ω → 25 mV → **0.5 V out**
- 50 Ω → 50 mV → **1.0 V out**
- 100 Ω → 100 mV → **2.0 V out**

### If you have MAX4173F (50 V/V)
- 10 Ω → **0.5 V out**
- 25 Ω → **1.25 V out**
- 50 Ω → **2.5 V out**
- 100 Ω → **5.0 V out** (often perfect if your ADC is 0–5 V)

### If you have MAX4173H (100 V/V)
- 10 Ω → **1.0 V out**
- 25 Ω → **2.5 V out**
- 33 Ω → 3.3 V out at 1 mA (nice for 0–3.3 V ADC)
- 50 Ω → **5.0 V out** (rails if you’re on 3.3 V)

## My “do this and it’ll work” picks
- If your ADC is **0–3.3 V**:
  - **MAX4173H:** **33 Ω** (≈3.3 V at 1 mA)
  - **MAX4173F:** **68 Ω** (≈3.4 V at 1 mA, slightly high—56 Ω gives 2.8 V)
- If your ADC is **0–5 V**:
  - **MAX4173F:** **100 Ω** (≈5 V at 1 mA)
  - **MAX4173T:** **150 Ω** gives 3 V at 1 mA (but that’s the 150 mV FS limit, and it’s a chunky drop on OS)

If you tell me which suffix you have (**T/F/H**) and what your ADC full-scale is (**2.5 / 3.3 / 5 V**), I’ll give you one exact RSENSE value + a quick note on headroom for “oops it’s 2 mA in corner cases”.

[M19] ME (2026-03-04 18:13):
[image]
So theee already a 100R there. Improve its tolerance? Kelvin?
[attached file: 700CE2E0-6660-4762-8F9E-AE3A1AAF226A.jpeg]

[M20] AI (2026-03-04 18:13):
That **100 Ω (R142)** in your screenshot is **not** a good candidate for “OS current sense”.

It’s the **base/gate series resistor into the follower transistor** (i.e., it sets/limits *drive* into the transistor). The voltage across it corresponds to **base current (plus transient charge/discharge effects)**, not the **OS pin current** and not the **collector/ID (“second stage”) current**.

So: **improving its tolerance or Kelvin-sensing it won’t give you the measurement you think you’re getting.**

## What to do instead (with MAX4173)

### Measure raw OS pin current (the “first stage”)
Put a **dedicated shunt resistor in series with OS_CCD** *before the node splits* (i.e., between P58 and the rest of the OS network).

- For your earlier assumption **I_OS ≤ 1 mA**, you can use something like:
  - **10 Ω** → 10 mV @ 1 mA (nice, minimal disturbance)
  - **20 Ω** → 20 mV @ 1 mA (more signal, still tiny drop)

Then feed that shunt into the MAX4173 inputs (Kelvin).

### Measure follower / “second stage” current (you said ~10 mA)
Put another shunt **in series with the transistor collector feed from ID** (not visible in this crop, but it’ll be where the collector ties to the ID rail).

- For **10 mA**, typical shunts are:
  - **1 Ω** → 10 mV @ 10 mA
  - **2 Ω** → 20 mV @ 10 mA

## Kelvin / tolerance guidance (yes, here it matters)
For the **actual shunt(s)** (not R142):

- **Kelvin sense:** yes — route the MAX4173 inputs as **separate sense traces** from the *inner* pads of the shunt (don’t share load copper).
- **Resistor type:** ideally a **4-terminal current sense** resistor if you’ve got the footprint space; otherwise a normal resistor with **Kelvin pads**.
- **Tolerance / tempco:** 1% is usually fine for “engineering monitor”; go **0.1% / low tempco** if you want real accuracy across temperature.

## Quick sanity check on your existing 5k6 to 0V
That 5k6 pull-down is a **DC load path** on OS. If OS can be high (your note says “30 V OS max”), then that alone implies up to:
- 30 V / 5.6 kΩ ≈ **5.4 mA**
So your “1 mA max” for “raw OS” is only plausible if OS isn’t actually sitting at 30 V in that mode, or the 5k6 isn’t always connected the way it looks.

If you tell me what **OS voltage range** is in normal operation (e.g., 3–5 V? 10 V? 20–30 V?), I’ll give you the exact shunt values that won’t upset biasing and will land the MAX4173 output nicely in your ADC range.

But bottom line: **don’t repurpose the 100 Ω base resistor as a sense shunt**. Use a **real series shunt** on OS_CCD and Kelvin it.

[M21] ME (2026-03-04 18:16):
28V

[M22] AI (2026-03-04 18:16):
28 V changes the “raw OS current” picture a lot.

In *your* schematic, OS_CCD is tied to **0 V through 5k6 (R145)**. If OS really sits at **28 V**, that path alone draws:

\[
I \approx \frac{28\text{ V}}{5.6\text{ k}\Omega} = 5.0\text{ mA}
\]

So the **raw OS current cannot be ~1 mA** in that configuration — it’s **~5 mA minimum**, plus whatever the follower/base network takes (usually small in DC terms, but can spike dynamically).

Also note the dissipation in that 5k6:
\[
P=\frac{V^2}{R}=\frac{28^2}{5600}\approx 0.14\text{ W}
\]
Your “0.33 W” marking makes sense.

## What shunt value makes sense now (with MAX4173)
Design for at least **10 mA full-scale** to cover:
- ~5 mA DC via the 5k6
- margin for other paths / tolerances / transients

Keep the shunt drop modest so you don’t disturb the bias.

A good target is **50–100 mV at max current**:

- **Rsense = 10 Ω** → 10 mA gives **100 mV** (and at 5 mA you get 50 mV)
- **Rsense = 5.1 Ω** → 10 mA gives **51 mV** (and at 5 mA you get 25 mV)

Both are well within MAX4173’s typical sense range and won’t upset 28 V OS materially.

### Output scaling (rule)
\[
V_{OUT} = G \cdot (I \cdot R_{SENSE})
\]
So pick Rsense based on what gain version you used (20/50/100 V/V) and what ADC range you have. Practically:
- If you have **gain 50** and use **5.1 Ω**:  
  10 mA → 51 mV → **2.55 V out** (nice for 3.3 V ADC)
- If you have **gain 50** and use **10 Ω**:  
  10 mA → 100 mV → **5 V out** (nice for 5 V ADC)

## Kelvin / tolerance
- **Yes, Kelvin sense the shunt** (separate thin sense traces from each shunt pad to IN+ / IN–).
- **Tolerance:** 1% is fine for monitoring; **0.1%** if you want it to be a “measurement” rather than an indicator.
- If space allows, a **4-terminal sense resistor** is the cleanest.

## Important: don’t use R142 (100 Ω) for this
As before: **R142 is base-drive series**. Measuring it tells you **base/transient current**, not the OS feed current.

If you tell me which MAX4173 gain suffix you actually placed (T/F/H) and your ADC full-scale (3.3 V or 5 V), I’ll give you the single best Rsense value and the expected output at 28 V OS.

[M23] ME (2026-03-04 18:19):
Want the highest bandwidths 100 I’m guessing 

[M24] AI (2026-03-04 18:20):
If you mean **highest bandwidth MAX4173 variant**, yes: the **gain = 100 V/V (“H” version)** is the one you’d typically pick when you want the **best small-signal sensitivity** and you’re keeping the sense voltage small. But two important caveats:

1) **Bandwidth is not just gain** — it’s the whole chain: shunt value, input RC filtering, layout/Kelvin, output loading, and how close you drive it to clipping.
2) With your OS sitting at **28 V** and an always-present **5k6 to 0V**, you’re already at **~5 mA DC**, so gain=100 can saturate fast unless you keep RSENSE low.

## Work the numbers with OS ≈ 28 V
Baseline current through R145:
- \(28/5.6k \approx 5\text{ mA}\)

If you pick **MAX4173H (G=100)**, then:

### Choose RSENSE to avoid rail/saturation
\[
V_{OUT} = 100 \cdot I \cdot R_{SENSE}
\]

Assuming you want:
- **~2.5 V** at a “max expected” current (good headroom on 3.3 V ADC)
- and you want room for spikes / tolerance

#### If you design for **Imax = 10 mA**
\[
R_{SENSE} = \frac{2.5}{100 \cdot 0.01} = 2.5\ \Omega
\]

That’s the sweet spot.

**Pick:** **2.49 Ω (1%)** or **2.00 Ω** if you want even more headroom.

What you’ll see:
- At **5 mA** (just the 5k6 load):  
  2.49 Ω → Vsense 12.5 mV → **Vout ≈ 1.25 V**
- At **10 mA**:  
  Vsense 24.9 mV → **Vout ≈ 2.49 V**
- At **20 mA** (unexpected corner):  
  Vsense 49.8 mV → **Vout ≈ 4.98 V** (fine on 5 V, clips on 3.3 V)

#### If your ADC is **0–3.3 V**
I’d stay conservative:
- **2.00 Ω** gives:
  - 5 mA → 1.0 V
  - 10 mA → 2.0 V
  - 15 mA → 3.0 V

That’s very clean and leaves margin.

## Bandwidth: what actually matters on the PCB
If you want “highest bandwidth”, the biggest wins are:

- **True Kelvin routing** to the shunt (separate sense traces from the inner pads)
- Keep IN+ and IN– **tightly coupled** (pair route, no stubs)
- Shunt physically **right at the rail feed point** you care about
- Avoid big RC filtering on the inputs unless you explicitly need it (it kills bandwidth)
- Don’t hang a big capacitance directly on VOUT (check datasheet stability guidance)

## Recommendation (actionable)
- If you’re going **MAX4173H (100 V/V)** for OS current at 28 V:
  - **RSENSE = 2.00 Ω** (best general choice for 3.3 V systems)
  - or **2.49 Ω** (if you’re on 5 V or want higher swing)

And yes: **use a Kelvin/4-terminal sense resistor footprint** if you can.

If you tell me your **ADC full-scale (3.3 vs 5 V)** and whether you care about **fast transients** vs mostly DC logging, I’ll also suggest whether to add a tiny input RC (and where) without wrecking bandwidth.

[M25] ME (2026-03-04 18:22):
So do I put it in series with the 5k6 at the ground side?

[M26] AI (2026-03-04 18:22):
If your goal is **“raw OS pin current”**, then **no — don’t put the shunt just in series with the 5k6 to ground**, *unless* you are explicitly happy measuring **only the 5k6 bleed current**.

### Why
In your snippet, the OS node has **multiple current paths**:
- the **5k6 to 0V** (R145) (a deliberate bleed/load)
- the **follower/base network** (via R142 into the transistor, and then ultimately to ID/other rails)
- possibly other branches not shown in the crop

If you put the shunt **only under the 5k6**, you measure:

✅ **I through R145 only**  
❌ **not** the total OS node current (and definitely not what the CCD pin is sourcing if there are other branches)

### The correct placement for “raw OS” (total OS feed / CCD pin current)
Put the shunt **in series with OS_CCD coming in from the CCD connector**, *before the node splits*:

**P58 / OS_CCD → RSENSE → OS0_CCD node → (R145 to GND, switch, R142, etc.)**

That way the shunt current is:
\[
I_{RSENSE} = I_{R145} + I_{base/network} + \text{any other OS branch}
\]
…i.e. the **total OS pin supply current**.

### When *would* ground-side-under-5k6 be OK?
If the requirement is really:
- “Measure the **bleed current** / verify the 5k6 path / confirm OS is present”
then yes, shunting the 5k6 return is a neat, low-noise proxy.

But that’s a *different requirement* than “OS pin current”.

---

## Practical note with MAX4173
MAX4173 is happy **high-side**, so placing RSENSE in the **28 V OS feed** is fine — just Kelvin route it.

---

**So:**
- **Want true OS pin current?** → shunt **in series with OS_CCD feed** (before split) ✅  
- **Want just the 5k6 bleed current?** → shunt **in series with 5k6 to ground** ✅

If you want, tell me whether you need **total OS pin current** or **bleed-only**, and your MAX4173 gain suffix (T/F/H), and I’ll give you a single RSENSE value + where to Kelvin-route it on the PCB.

[M27] ME (2026-03-04 18:45):
X100, raw os, suggest resistor. Assume adc if 3.3v

[M28] AI (2026-03-04 18:46):
Given:

- **MAX4173H (×100)**
- **Raw OS current**
- **OS ≈ 28 V**
- Your schematic shows **5k6 to 0 V** on the OS node ⇒ baseline **~5 mA**
- **ADC full-scale = 3.3 V**

You want RSENSE so you don’t rail the ADC, but still get good resolution.

### Recommended RSENSE
**2.00 Ω** (or **2.0 Ω, 0.1–1%, low tempco**)

### Why (numbers)
\[
V_{OUT}=100\cdot I\cdot R
\]

- At the unavoidable baseline **~5 mA**:
  - Vsense = 5 mA × 2 Ω = **10 mV**
  - Vout = 100 × 10 mV = **1.0 V**

- At **10 mA** (nice design “max expected” with headroom):
  - Vsense = 20 mV
  - Vout = **2.0 V**

- You won’t hit **3.3 V** until:
\[
I = \frac{3.3

[M29] ME (2026-03-04 18:46):
Part number?

[M30] AI (2026-03-04 18:46):
For your case (**2 Ω shunt, Kelvin sensing, good bandwidth, stable over temperature**), use a **proper current-sense resistor** rather than a generic thick-film resistor.

Here are solid choices that are easy to source and layout well.

---

## 1️⃣ Best engineering choice (4-terminal Kelvin sense)
**entity["product","Vishay WSLF2010R0020FEA","2 mΩ current sense resistor series WSLF 2010 2 Ω"]**

*(Note: WSLF family includes Kelvin versions; choose the **2 Ω variant**.)*

Typical parameters:

- **Resistance:** 2.0 Ω  
- **Tolerance:** 1% (0.5% options exist)  
- **Tempco:** ~75 ppm/°C  
- **Package:** 2010  
- **4-terminal Kelvin pads**

Why this is good:

- Accurate sensing for the MAX4173
- Kelvin pads reduce copper trace error
- Stable over temperature

---

## 2️⃣ Very common alternative (also excellent)
**entity["product","Bourns CSS2H-2512R-L200F","Bourns CSS2H current sense resistor 2 Ω"]**

Specs:

- **2.0 Ω**
- **1%**
- **50 ppm/°C**
- **2512 package**
- Designed specifically for current sensing

---

## 3️⃣ If you want compact but still accurate
**entity["product","Susumu KRL1632E-R002-F-T1","Susumu KRL metal foil current sense resistor 2 Ω"]**

Specs:

- **2.0 Ω**
- **1%**
- **±50 ppm**
- **metal foil style**

Very stable and clean for measurement circuits.

---

# Layout advice (important for your bandwidth)
Since you're using **MAX4173 ×100**:

✔ Place the **shunt right in the OS feed before the node splits**  
✔ Run **two thin Kelvin traces** from each shunt pad directly to **IN+ / IN-**  
✔ Keep them **tight differential pair**  
✔ No load current in those traces

That will preserve **bandwidth and accuracy**.

---

✅ **My pick for this board:**  
**Vishay WSLF2010 2 Ω Kelvin sense resistor**

It’s robust, easy to route, and perfect for instrumentation.

---

If you want, I can also show **exactly where on your schematic the resistor should go** (with a small annotated diagram), because placing it **one node wrong** will cause you to measure the wrong current.

[M31] ME (2026-03-04 18:50):
That range only goes to 0.1

[M32] AI (2026-03-04 18:51):
Ah — if you mean **your current-sense resistor series/footprint family only goes up to 0.1 Ω**, then you’ve basically got two choices:

## Option 1 (recommended): keep RSENSE ≤ 0.1 Ω and accept a small signal
With **MAX4173H (×100)** and **ADC 3.3 V**:

\[
V_{OUT}=100\cdot I \cdot R_{SENSE}
\]

At your OS node, you’ve already got ~**5 mA DC** via **28 V / 5.6 kΩ**.

If **R = 0.1 Ω**:
- 5 mA → Vsense = 0.5 mV → Vout = **50 mV**
- 10 mA → 1.0 mV → **100 mV**
- 20 mA → 2.0 mV → **200 mV**

So it will work, but you’re using only a small slice of ADC range — meaning **offset + noise** matter a lot more.

If your goal is **high bandwidth trend/relative measurement**, this can still be perfectly fine.

### What to do then
- **Yes: Kelvin sense** becomes *more important*, not less (mV-level signals).  
- Use a **low-TC metal element shunt** (not thick film).

A concrete part example in the **0.1 Ω** class:
- **Susumu PRL1632-R100-F-T5** (0.1 Ω, 1%, ~50 ppm/°C). citeturn0search7  
(That’s just to anchor the “type” of part; pick package/power to suit your layout.)

## Option 2: if you actually want to use the ADC range properly, RSENSE must be ~2 Ω
To get the nice scaling we discussed earlier (≈1 V at 5 mA, ≈2 V at 10 mA with ×100), you need **~2 Ω** in series with the OS feed.

Many *current-sense* resistor **families** don’t go that high because they’re aimed at mΩ. In that case, just use a **precision resistor** (thin-film / metal-film), not a “current sense” shunt.

Example class: 2 Ω, 0.1%, 25–50 ppm/°C in 1206/1210/2010, etc. (Plenty exist, but the exact PN depends on package and power you want.)

## Quick reality check (important)
Because your OS node already sinks **~5 mA** through the 5k6 at 28 V, designing for “**raw OS max 1 mA**” isn’t consistent with the shown circuit. Your measurement range should comfortably cover **at least 5–10 mA**.

---

# My practical recommendation
- If you’re constrained to **≤0.1 Ω**, do it — but treat it as a **monitor**, not a precision absolute measurement:
  - **RSENSE = 0.1 Ω**
  - **Kelvin it**
  - Expect outputs in the **50–200 mV** region for 5–20 mA.

If you tell me your ADC resolution (e.g. **12-bit? 16-bit?**) and whether you care about **absolute accuracy** vs “shape/trends”, I’ll tell you whether 0.1 Ω is good enough or whether it’s worth stepping up to a 2 Ω precision resistor + maybe reducing the MAX4173 gain.

[M33] ME (2026-03-04 18:53):
The os dips below the 28v. So should I sit it around mid rail?

[M34] AI (2026-03-04 18:53):
No — **don’t try to “mid-rail bias” the OS node** just to suit the measurement. OS is a **CCD bias pin**, and its absolute level and dynamic behaviour are part of the sensor’s operating point. If you artificially centre it, you’ll almost certainly change charge handling / output stage behaviour.

What you *should* do is make the **measurement tolerate OS moving around**.

## With MAX4173 you already can
MAX4173 is high-side and will tolerate the OS common-mode moving anywhere in its allowed range. So the question becomes: **how to avoid output clipping when OS current varies**, not how to recenter OS voltage.

### If you’re using MAX4173H (×100) + 3.3 V ADC
Design the shunt so worst-case current *never* makes Vout exceed 3.3 V:

\[
V_{OUT}=100\cdot I_{MAX}\cdot R_{SENSE} \le 3.3
\Rightarrow R_{SENSE} \le \frac{3.3}{100\,I_{MAX}}
\]

Pick \(I_{MAX}\) based on the real current swings when OS dips (likely several mA because of that 5k6 path plus any other branches).

### Practical pick if you’re stuck at ≤0.1 Ω
If your resistor family tops out at **0.1 Ω**, then:

- At **5 mA**: Vout ≈ **50 mV**
- At **20 mA**: Vout ≈ **200 mV**

That’s totally fine as a **high-bandwidth monitor**, just low amplitude. If you need more ADC utilisation, add gain later (or use a higher-gain ADC range), but **don’t move OS bias**.

## Why “OS dips below 28 V” matters
If OS droops because the circuit draws more current at certain times, that’s *exactly the behaviour you’re trying to observe*. Setting it “mid-rail” would mask the droop mechanism.

## What you can do instead (safe/clean)
1) **Keep OS biasing as intended** (28 V nominal, allow droop).  
2) Put **RSENSE in series with the OS feed before the node splits**.  
3) If you need more resolution than 0.1 Ω gives:
   - use a **higher resolution ADC** / smaller ADC range, or
   - switch to **MAX4173F/T** plus a larger shunt (but that’s a design change), or
   - add a **post-amp** on Vout (careful: bandwidth + stability).

## Quick sanity check
Do you know your **ADC resolution** (12-bit vs 16-bit) and sampling rate?  
Because with a 12-bit, 3.3 V ADC, 50 mV is only ~62 counts — still usable, but noise/offset starts to matter. With 16-bit it’s plenty.

Bottom line: **don’t centre OS. Size the shunt + gain so the measurement stays in range while OS does what it needs to do.**

[M35] ME (2026-03-04 18:57):
But im not expecting it to go above 28v as thats supply limitation. So shouldn’t the 28v nominal 5ma read at the higher end of the range

[M36] AI (2026-03-04 18:57):
You’re right about **voltage**: OS won’t exceed 28 V if that’s the supply limit.

But your measurement range is set by **current**, not voltage.

Because of the **5k6 to 0V**, the *minimum* DC current at 28 V is ~5 mA, and as OS droops the 5k6 current actually **drops** (it’s \(I=V/5.6k\)). So 28 V is the **highest** *bleed* current point, yes.

The catch is: the OS node current may include **other paths** that can make the **total current >5 mA**, even while OS stays ≤28 V:
- follower / clamp network currents
- transient charging currents into caps / base drive during edges
- any additional loads on OS0_CCD

So the “top end” you should design around is **I\_max**, not 28 V.

---

## If you want 28 V (≈5 mA) near the top of a 3.3 V ADC range

With MAX4173H (×100):

\[
V_{out}=100\cdot I \cdot R
\]

Set \(V_{out}\approx 3.0\text{ V}\) at \(I=5\text{ mA}\):

\[
R \approx \frac{3.0}{100\cdot 0.005}=6\ \Omega
\]

So **~6.2 Ω** is the “nice scaling” value.

But… only if you are confident **total OS feed current will not exceed ~5–6 mA**. Because if current hits 10 mA:

- with 6.2 Ω: \(Vout = 100×0.01×6.2 = 6.2\text{ V}\) → **hard rail**.

That’s why earlier I pushed you toward designing for **10 mA-ish** unless you’re sure.

---

## The practical compromise (what I’d do)
Design so **28 V / 5 mA sits around mid-to-upper range**, *and* you don’t instantly rail on modest excursions:

### Recommendation for 3.3 V ADC, ×100 gain
- **Rsense = 2.0 Ω to 3.0 Ω**

Examples:
- **2.0 Ω:** 5 mA → **1.0 V**, 10 mA → **2.0 V**, 15 mA → **3.0 V**
- **3.0 Ω:** 5 mA → **1.5 V**, 10 mA → **3.0 V** (tight headroom)

So if you want to “use the range” while keeping margin, **2.0 Ω** is the safe sweet spot; **2.7 Ω** is a bit punchier but risks clipping sooner.

---

## If you’re constrained to ≤0.1 Ω shunts
Then no — you simply *can’t* make 5 mA land near full-scale with MAX4173H. Physics:

- 0.1 Ω at 5 mA is 0.5 mV → ×100 = 50 mV.

That’s fine for monitoring, but it won’t fill the ADC range unless you add more gain later.

---

## Bottom line
- Want 5 mA near top-of-range? **~6.2 Ω**, but only if you can guarantee total current won’t exceed ~5–6 mA.
- Want robust headroom (my pick): **2.0 Ω** (Kelvin).
- If your resistor family tops at 0.1 Ω, accept the small signal or add a post-gain stage.

If you tell me **whether any other OS loads exist besides the 5k6 + follower input** (caps, clamps, etc.), I’ll tell you whether 6.2 Ω is safe or whether you’ll rail in real operation.

[M37] ME (2026-03-04 18:58):
That’s why I was saying sit the 28v mid rail of the adc

[M38] ME (2026-03-04 18:58):
I’m not doing anything with os

[M39] AI (2026-03-04 18:58):
Ah — understood now. You’re **not controlling OS**, just **monitoring its current**, and you want the **nominal 28 V / ~5 mA point to sit roughly mid-range of a 3.3 V ADC**. That’s a perfectly sensible design goal.

Given:

- **MAX4173H (gain = 100 V/V)**
- **ADC full scale = 3.3 V**
- **Nominal OS current ≈ 5 mA** (from 28 V / 5.6 kΩ)

You want:

\[
V_{out} \approx 1.6\text{–}1.8\,\text{V at } 5\,\text{mA}
\]

### Solve for Rsense
\[
V_{out} = 100 \cdot I \cdot R
\]

\[
R = \frac{1.65}{100 \cdot 0.005}
\]

\[
R \approx 3.3\,\Omega
\]

### Recommended value
**3.32 Ω (E96)**

This gives:

| Current | Vsense | ADC input |
|-------|-------|-------|
| 5 mA (nominal) | 16.6 mV | **1.66 V** |
| 3 mA (OS droop) | 10 mV | **1.0 V** |
| 8 mA | 26 mV | **2.6 V** |
| 10 mA | 33 mV | **3.3 V (top)** |

So you get:

- **Nominal OS current ≈ mid-scale**
- **room for upward excursions to ~10 mA**
- good ADC utilisation.

### Drop on OS rail
At 5 mA:

\[
V = I \cdot R = 5\,\text{mA} \times 3.3\,\Omega \approx 16\,\text{mV}
\]

Completely negligible for a **28 V bias rail**.

### Implementation tips
- Place **RSENSE in series with OS_CCD before the node splits**.
- Use **Kelvin routing** to MAX4173 inputs.
- 1 % tolerance is fine; 0.1 % if you want nicer calibration.

### Example resistor parts
Good, stable thin-film options:

- **Yageo RT1206FRE073R32L** (3.32 Ω, 1%, 1206)  
- **Vishay TNPW12063R32BEEN** (0.1%, thin film)  
- **Susumu RG2012P-332-B-T5** (0.1%, 0805)

---

✅ **Summary:**  
Use **3.32 Ω RSENSE** with the **MAX4173H**. It puts the **28 V / 5 mA nominal OS current right around mid-scale of a 3.3 V ADC**, which is exactly the behaviour you were aiming for.

[M40] ME (2026-03-05 23:53):
The adc is only rated to 200ksps so that’s not going to be good for a single of 500khz

[M41] AI (2026-03-05 23:53):
You’re right: **200 kS/s will not capture a 500 kHz waveform** in any faithful way.

- Nyquist for 500 kHz is **≥1 MS/s** just to avoid aliasing.
- In practice you want **2–5 MS/s+** if you care about shape, not just presence.

So the question becomes: **what do you actually need from the OS current measurement?**

## If you want to observe the 500 kHz behaviour
You need one of these approaches:

### 1) Don’t use the slow ADC — use a scope/fast ADC tap
Bring out:
- MAX4173 output (or even the shunt diff nodes via a high-imp probe/front end)
to a **test point / SMA** and view on a scope or digitiser.

That gives you the bandwidth you want without redesigning your whole acquisition.

### 2) Envelope / RMS / peak detect (recommended with your 200 kS/s ADC)
If your purpose is “is the 500 kHz current present / how big is it”, then **measure a processed quantity**:

- **Rectify + low-pass** (envelope detector) → gives amplitude vs time
- **True RMS-to-DC converter** (overkill but elegant) → gives RMS current level
- **Peak detector** → gives worst-case current peaks

Then the ADC samples the **slow envelope**, not the 500 kHz carrier.

This is *exactly* what you do when you can’t sample the carrier.

### 3) Synchronous detection (if you have the clock)
If you have a coherent 500 kHz reference and want amplitude/phase, you can do a simple lock-in style multiply + LPF. Usually more effort than it’s worth here.

## If you only care about DC / average OS current
Then 200 kS/s is absolutely fine — you just need an **anti-alias filter** so the 500 kHz content doesn’t fold into your measurement.

### Minimum to stop aliasing
Add a **low-pass** before the ADC input, with cutoff comfortably below 100 kHz (since Nyquist is 100 kHz at 200 kS/s).

Simple practical choice:
- 1-pole RC at, say, **20–50 kHz** (or 2-pole if you want it cleaner).

Example:
- R = 1 kΩ, C = 3.3 nF → fc ≈ 48 kHz

That way, your ADC reads “average/slow variations” in OS current and ignores the 500 kHz.

## Critical point: without filtering, the ADC will lie
If you feed a 500 kHz-rich signal straight into a 200 kS/s ADC:
- you’ll get **aliasing** that looks like random low-frequency junk or beating.
So you *must* either:
- sample fast enough, **or**
- filter/detect/envelope.

## What I’d do on your board (low effort, high value)
- Keep your **RSENSE + MAX4173H** as we discussed (e.g., 3.32 Ω if you want mid-scale at 5 mA DC).
- Provide **two measurement paths** from VOUT:
  1) **Unfiltered “wideband” output** to a testpoint/SMA for scope
  2) **Filtered/envelope output** into the ADC (RC or detector + RC)

That gives you both: **engineering debug bandwidth** and **reliable telemetry**.

If you tell me which of these you want:
- (A) **average current only**, or
- (B) **amplitude of the 500 kHz component**, or
- (C) **time-domain waveform**,

…I’ll give you the exact little circuit (values) that matches your 200 kS/s ADC.

[M42] ME (2026-03-05 23:55):
They def want to be able to get this raw os out is sounds. Sma not possible in chamber. The system has 4os feeds and the board is only using two in the video chain. So perhaps I could tap off the raw os and feed it onto the differential output spares into the system conditioning. Keeping x1 gain though out 

[M43] AI (2026-03-05 23:55):
Yep — that’s a credible architecture, and it matches the “we want the raw OS out” vibe **without needing an SMA in the chamber**.

### The core idea
Treat **OS current sense** as just another **wideband analogue channel**, and export it using the system’s existing **differential analogue transport / conditioning path** (the spare differential channels), instead of trying to sample it on a 200 kS/s ADC.

That gets you bandwidth out of the chamber **using the wiring you already trust**.

---

## How to do it cleanly

### 1) Sense the current locally (in the chamber board)
- Keep your **shunt in series with OS_CCD feed** (before the node splits).
- Use a **Kelvin sense layout** (this matters a lot for 500 kHz content).

If you truly want “raw”, the most “raw” quantity is actually:
- **Vshunt(t)** (millivolts), wideband, directly proportional to current.

You can export either:
- **Vshunt(t)** (preferred for bandwidth/purity), or
- **Vout from MAX4173** (already amplified, but you must ensure the chain doesn’t saturate / bandwidth-limit).

### 2) Convert to differential and drive the spare differential output
Use a **fully differential amplifier / line driver** to map your single-ended sense signal into the spare differential pair, **at unity gain (×1)**.

Block diagram:

**Shunt (Kelvin) → (optional small gain/atten) → FDA diff driver (G≈1) → spare diff pair out → existing conditioning**

Key constraints to match your system conditioning:
- Output **common-mode** level (Vcm) must match what the receiver expects
- Output swing must stay within the receiver’s linear range
- Bandwidth comfortably > 500 kHz (most FDAs will do MHz easily)

### 3) Use the spare channels smartly
You have **4 OS feeds**, board uses **2** in the video chain → you’ve got spare “lanes”.

Options:
- **Export two raw OS channels** simultaneously (ideal).
- Or if only one spare lane, add a **wideband analogue MUX** to select which OS sense you’re exporting (but MUX adds distortion/charge injection; only do this if necessary).

---

## Why “keep ×1 gain throughout” is sensible
At 500 kHz, the issues are usually **linearity + stability + avoiding saturation**, not SNR.

So unity gain is great if you choose the shunt so that:
- the differential export swing is “useful” but not huge.

Example: if you end up with, say, **10–30 mV** across the shunt at nominal conditions, you can still export that through the conditioning chain and measure it later with the proper bandwidth ADC/scope on the warm side.

If you need more swing, add gain **outside the chamber** where it’s easier/safer.

---

## Two practical implementation patterns

### Pattern A (most raw): export Vshunt directly (as differential)
- Kelvin sense shunt
- FDA at **G = 1**
- Output common-mode set to whatever the diff link expects

Pros: maximum fidelity, minimal “amp personality” in the chamber  
Cons: small signal (mV) must survive the link + receiver noise

### Pattern B (more robust): export the MAX4173 output (buffered) as differential
- MAX4173 gives you a bigger signal
- Then use FDA as a **differential buffer** (still G=1)

Pros: higher amplitude over the link  
Cons: you inherit MAX4173 output behaviour (offset, any bandwidth limiting, saturation recovery if overdriven)

---

## One caution (important)
If your existing “differential video chain” is **AC-coupled** or has a defined input range/bias, you must match that:

- If the chain is expecting something like a video common-mode, you’ll want an FDA that can **set Vcm** accordingly.
- If it’s AC-coupled, you may need to ensure your signal is centred appropriately or accept that you lose DC content (depends what “raw OS” means to them: waveform vs average).

---

## What I’d do on your board (no extra drama)
1) **Keep the shunt + Kelvin** on each OS you care about.
2) Put footprints for:
   - a **unity-gain FDA diff driver** per exported channel
   - optional **0 Ω / small R** links so you can choose whether the driver input is **Vshunt** or **MAX4173 Vout**
3) Route the FDA outputs to the **spare differential outputs** that already go through the chamber harness.

That gives you a flexible “A/B” path without committing blindly.

---

If you paste (or describe) what the “spare differential outputs into system conditioning” electrically are (e.g. **LVDS into ADC? analogue diff into an instrumentation front end? impedance/termination? AC-coupled? expected Vcm?**), I’ll pin this down to a concrete schematic: which block (FDA vs simple op-amp diff), where to set common-mode, and what termination to use so 500 kHz looks clean at the far end.

[M44] ME (2026-03-06 00:00):
Is max4173 optimal
For the job? Could we do better?

[M45] AI (2026-03-06 00:00):
MAX4173 is **pretty good** for what you’re trying to do — but whether it’s “optimal” depends on what *exactly* “raw OS out” means (true wideband waveform vs just “don’t-lowpass it”).

### What MAX4173 does well
- **High-side at 28 V common-mode** (that’s exactly its wheelhouse). citeturn0search6turn0search0  
- **Bandwidth ~1.7 MHz**, so a **500 kHz** component is realistically measurable (you’ll see amplitude/shape, not just average). citeturn0search6turn0search0  
- Simple: shunt + one IC gives you a ground-referred output.

### Where you *can* do better
“Better” usually means one of these:

1) **More bandwidth / faster edges**  
   MAX4173 at 1.7 MHz is OK for 500 kHz, but if you care about harmonics/edge detail, a faster architecture can help (current-sense amps with several MHz to tens of MHz BW exist, but you’ll trade noise/offset/stability).

2) **Lower offset / better low-level accuracy**  
   If you end up forced into a tiny shunt (e.g., 0.1 Ω max), then your signal is in the **mV** region and **offset/noise** start to dominate. Some newer/zero-drift parts win here, but many have **much lower bandwidth** (kHz–hundreds of kHz class).

3) **Differential “raw export”**  
   If the actual requirement is “get the waveform out of the chamber over spare differential analog transport”, you may be better off exporting **Vshunt (Kelvin)** through a **wideband fully-differential driver at unity gain**, rather than relying on a current-sense amp’s output stage/behavior. (This is often the cleanest “raw” path.)

### A very relevant comparison part-class
For example, Maxim/ADI “MAX437x” family includes parts that are explicitly **500 kHz** bandwidth high-side current sense (so borderline for your 500 kHz tone) — fine for amplitude, not great for waveform fidelity. citeturn0search1  
MAX4173’s **1.7 MHz** is materially better for your use. citeturn0search6turn0search0

---

## Recommendation for your situation
Given:
- 28 V OS
- 500 kHz content you want to preserve
- no SMA
- spare differential “lanes” out of the chamber

### Best practical architecture
- **Keep MAX4173 if you want a robust, ground-referenced signal** with enough BW to represent 500 kHz sensibly. citeturn0search6turn0search0  
- Then **buffer/convert its output to differential at ×1** onto your spare differential channel.

### If you truly want the most “raw” representation
Skip the current-sense amp output and instead:
- Kelvin-sense the shunt
- feed that into a **wideband fully differential amplifier** (unity gain) and export **Vshunt(t)** directly.

This avoids any “personality” of the current-sense IC output stage and is the closest you’ll get to “raw current waveform” over a harness.

---

## Quick decision rule
- If the stakeholders want **“raw OS current waveform”**: prefer **Vshunt → FDA diff driver → spare diff pair**.
- If they want **“a current telemetry signal that still contains the 500 kHz component”**: **MAX4173 is fine** (1.7 MHz BW) and simpler. citeturn0search6turn0search0

If you tell me what the “spare differential outputs into system conditioning” electrically are (analogue diff into an ADC front end? impedance/termination? expected common-mode?), I’ll pin down the cleanest of the two and suggest concrete IC candidates for the diff driver.

[M46] ME (2026-03-06 11:47):
The interpretation was to take the full signal riding on the 28v out. Is there any reduction in measurement by doing it as we’ve outlined above?

[M47] AI (2026-03-06 11:47):
Yes — **there is a reduction**, and it’s an important one.

What you’ve outlined so far with **shunt + MAX4173** is a **current measurement**.  
If their interpretation is actually:

> **“bring out the full OS voltage waveform that sits on top of the 28 V bias”**

then that is a **different measurement entirely**.

## What gets lost with the current-sense approach
With the shunt/current-sense path, you are no longer exporting:

- the **actual OS voltage waveform**
- the **true 28 V common-mode plus its AC modulation**
- the exact waveform as seen by the CCD node

You are exporting a signal proportional to:

- **current through the shunt**

That may correlate with OS behaviour, but it is **not the same thing**.

So if they literally want the **full raw OS signal riding on 28 V**, then:

### Shunt + MAX4173 path gives:
- **I(OS)** or total OS feed current
- bandwidth limited by the current-sense amp and output chain
- a translated, ground-referenced representation

### Raw tap + differential export gives:
- **V(OS)** itself
- the actual waveform riding on the bias
- much closer to what they appear to be asking for

---

## So is the “tap raw OS into spare differential conditioning path” idea better?
For that requirement: **yes, much better**.

If you can:
- **high-impedance tap the OS node**
- buffer it appropriately
- level-shift / convert to a differential signal
- send it out at **x1** through the spare conditioning path

then that is much closer to a true **raw OS monitor**.

## But there are still some caveats
You do still lose a little, unless the transport is ideal:

### 1) Loading
Your tap must be **very high impedance**.  
If you hang the spare chain directly on OS without buffering, you risk perturbing the node.

### 2) Common-mode handling
A signal “riding on 28 V” means the receiver cannot usually just take it directly unless it tolerates that common-mode.  
So you normally need a **buffer/attenuator/level-shift stage**.

### 3) Bandwidth of the export chain
If the spare differential conditioning path is not truly wideband enough, you will still lose edge detail / amplitude.  
At **500 kHz**, you want comfortable analogue bandwidth above that — ideally several MHz of clean small-signal bandwidth to preserve shape. The MAX4173 itself is specified at **1.7 MHz bandwidth**, which is usable for 500 kHz current monitoring, but it is still a conditioned measurement, not a transparent raw-voltage export. citeturn0search0turn0search1

---

## The clean distinction
### If they want:
**“What current is OS drawing?”**  
Use **shunt + MAX4173**.

### If they want:
**“What is the OS waveform itself, sitting on the 28 V pedestal?”**  
Use a **high-impedance voltage tap**, then **buffer/translate/export as differential**.

---

## Best fit for what you’ve now said
From your wording, it sounds like they want:

> **the actual OS voltage waveform on the 28 V bias**

So I would **not** treat MAX4173 as the primary solution for that requirement.

I would instead do:

**OS node → very high impedance buffer / attenuator → differential driver at x1 (or defined attenuation) → spare differential channel**

That preserves the actual waveform far better.

## One subtle point
If you do the differential export at **x1**, but the signal is sitting on **28 V DC**, then the receiving chain must either:
- tolerate that common-mode, or
- you must **subtract/shift the 28 V pedestal** before transmission.

Usually the practical solution is:

- **tap OS**
- **attenuate if needed**
- **buffer**
- **level shift to the receiver’s allowed common-mode**
- then send differentially

So it is not truly “raw” in an electrical sense, but it is still a **voltage-faithful representation** of the OS waveform.

## Bottom line
**Yes — there is a reduction if you use the current-sense scheme.**  
You would be measuring **current**, not exporting the **raw OS voltage waveform**.

If their real requirement is the latter, your idea of using the spare differential outputs as a **buffered raw OS voltage monitor path** is the right direction.

If you want, I’ll sketch the exact front-end architecture for that path — including whether it should be **direct x1 buffered**, **attenuated**, or **AC-coupled around the 28 V pedestal**.

[M48] ME (2026-03-06 11:50):
So I tap off single end into a attenuator say div 10. Then single into differential 

[M49] AI (2026-03-06 11:50):
Yes — **that is the right direction** for a **voltage monitor** of OS.

The chain would be:

**OS node (single-ended, riding on ~28 V DC) → high-impedance attenuator → buffer / single-ended-to-differential driver → spare differential pair**

That is fundamentally different from the **MAX4173 path**, which measures **current** rather than the raw OS voltage waveform. MAX4173 is a high-side current-sense part with fixed gains of 20/50/100 V/V, a 0 to 28 V input common-mode range, and about 1.7 MHz bandwidth, so it is fine for current telemetry, but it is not the most direct way to export the **actual OS voltage waveform on its 28 V pedestal**. citeturn0search0turn0search1

A few design points matter:

**1) Use a very light tap.**  
Make the divider impedance high enough that you do not load OS meaningfully, but not so high that parasitic capacitance kills bandwidth. For a 500 kHz-class signal, a divider in the rough region of **90 k / 10 k** or **180 k / 20 k** is a sensible starting point. That gives about **÷10** attenuation and keeps input loading modest.

**2) Buffer after the divider.**  
Do not feed the divider straight into a long route or diff stage if you can avoid it. A buffer keeps the divider from interacting with the driver input and preserves waveform fidelity.

**3) Then convert to differential.**  
Yes: **single-ended into differential** after attenuation is the normal way to do this. Set the output common-mode to whatever the receiving conditioning chain expects.

**4) Accept that it is not perfectly “raw.”**  
You will preserve the **waveform shape far better** than with a current-sense scheme, but the divider and buffer still introduce:
- finite bandwidth,
- attenuation tolerance error,
- some added capacitance/loading,
- amplifier offset/noise.

So it is a **faithful scaled representation** of raw OS, not a literal direct copy.

**5) Watch the receiver common-mode.**  
If the spare differential conditioning path is built for a low-voltage analogue differential signal, this architecture is ideal. If that path is AC-coupled, you may lose the DC pedestal information and only see the AC riding on it.

So, in plain terms: **yes, tap single-ended, attenuate, then convert to differential** is the right architecture if the requirement is truly to bring out the **full OS voltage waveform riding on 28 V**.

My recommendation would be:
- start with **÷10 attenuation**,
- use a **high-input-impedance wideband buffer/FDA**,
- export that at **unity differential gain**,
- and keep the **MAX4173 only if you also want OS current as a separate measurement**.

If you show me what the **spare differential conditioning input** expects electrically — voltage range, termination, AC/DC coupling, and common-mode — I’ll turn that into a concrete front end with actual resistor values.

[M50] ME (2026-03-06 11:51):
Is divider the best approach or can’t the buffer do the attenuation?

[M51] AI (2026-03-06 11:51):
Yes — the **buffer stage can do the attenuation**, and in many cases that is the **better approach**.

You’ve basically got two architectures:

## 1) Passive divider first, then buffer
**OS → resistor divider → buffer / single-to-diff**

### Pros
- very simple
- robust
- no active stage seeing full 28 V if that matters
- attenuation fixed by two resistors

### Cons
- divider loads the OS node
- divider parasitic capacitance can shave bandwidth
- the buffer only sees the reduced signal, so any buffer input noise is referred back more badly
- tolerance and frequency response depend on the divider network itself

---

## 2) High-impedance buffer / differential amp with gain < 1
**OS → active front end that presents high input impedance and attenuates in the feedback/gain network**

### Pros
- much lighter loading on OS
- usually better bandwidth control
- cleaner, more deliberate scaling
- easier to trim gain accurately
- lets you set output common-mode nicely for the differential chain

### Cons
- the active stage must tolerate the input common-mode / absolute input voltage
- can be more design effort
- stability needs checking, especially at gain < 1 or with capacitive load / long routing

---

# In your case
If the real requirement is:

> **export the full OS voltage waveform riding on 28 V**

then the best answer is usually:

## **Use an active differential receiver / FDA style front end with attenuation built in**
rather than a big passive divider hanging off the node.

That way:
- the OS node sees **very high input impedance**
- you can set the gain to, say, **0.1 V/V**
- then send it into the spare differential path at the right amplitude/common-mode

---

# But there is one big catch
The amplifier must be able to **handle the input common-mode**.

If OS is around **28 V single-ended**, a normal low-voltage op-amp or FDA running on 5 V cannot simply take that at its input, even if the closed-loop gain is 0.1.

So one of these must be true:

### A) The amplifier is a high-voltage input type
Then yes, let the active stage do the attenuation.

### B) The amplifier is low-voltage only
Then you still need **some passive attenuation or level shifting first**, so the amp input never sees 28 V.

That’s the practical reason dividers are so common here.

---

# Practical rule
## If your buffer cannot tolerate 28 V input:
Use a **passive divider first**.

## If your front end can tolerate the full OS voltage:
Let the **active stage set the attenuation**.

---

# What I would do
For a chamber monitor path like yours, I’d usually favour a **hybrid**:

## Small passive attenuation first, then active differential buffer
Not necessarily ÷10 straight away — maybe just enough to make the input safe and comfortable.

Example idea:
- **OS → ÷4 or ÷5 resistive attenuator**
- into a **wideband high-input-impedance differential driver / buffer**
- set final gain there to land nicely in the spare conditioning range

Why this is often best:
- keeps the active stage safe
- reduces stress/common-mode issues
- avoids an excessively high-value divider that kills bandwidth
- still gives you a buffered, well-controlled differential output

---

# So, direct answer
**No, a divider is not automatically the best approach.**  
If the buffer stage can legally and cleanly accept the OS voltage, then **doing the attenuation in the active stage is usually better**.

But if the buffer is a normal low-voltage part, then **you still need a passive divider or equivalent input attenuation first**, because the amplifier input itself cannot just sit at 28 V.

The real deciding factor is the **input voltage/common-mode capability of the buffer or single-to-differential stage**.

If you want, I’ll sketch the two cleanest versions:
- **passive divider + diff driver**
- **high-voltage active attenuating buffer + diff driver**
with ballpark resistor values for a **28 V OS, 500 kHz signal, spare differential analogue link**.

[M52] ME (2026-03-06 11:53):
Suggest parts and topology 

[M53] AI (2026-03-06 11:53):
Yes. For **“bring the full OS waveform riding on ~28 V out of the chamber”**, I would **not** make MAX4173 the primary path. It is a **current-sense amplifier** with about **1.7 MHz bandwidth** and is best when the deliverable is current telemetry, not a faithful exported copy of the OS voltage waveform. citeturn0search0turn0search4

The cleanest topology is:

**OS node → light passive attenuator → wideband single-ended-to-differential driver → spare differential pair**

That is the safest option because most fast fully differential amplifiers run from low supplies like **3 V to 7 V** or **2.7 V to 5.4 V**, so they cannot accept the raw 28 V node directly at their input. citeturn0search4turn0search1

## Recommended topology

Use a **passive divider first**, then an FDA.

A good starting point is:

- **Rtop = 90.9 kΩ**
- **Rbot = 10.0 kΩ**

That gives about **÷10**, so **28 V becomes ~2.8 V** at the amplifier input. That is a comfortable level for a 5 V FDA stage, and the divider only loads OS by about **277 µA** total, which is light compared with the ~5 mA you already have through 5.6 kΩ at 28 V. That loading figure is just Ohm’s law from the divider value. citeturn0search1turn0search4

Then feed that into a **fully differential amplifier at gain = 1** with output common-mode set to whatever your system conditioning expects.

## Parts I’d shortlist

### Best practical default: **TI THS4551**
Use this if you want a modern, low-power, easy FDA stage. It has **150 MHz bandwidth at gain = 1**, **220 V/µs differential slew rate**, runs from **2.7 V to 5.4 V**, and has adjustable output common-mode. That is vastly more than enough for a 500 kHz monitor path. citeturn0search1turn0search5

Why I like it here:
- plenty of bandwidth margin for 500 kHz, citeturn0search1turn0search5
- low supply current, citeturn0search1turn0search5
- easy to use as single-ended to differential. citeturn0search1

### Higher-performance option: **ADI ADA4940-1**
This is another strong choice if you want a cleaner, higher-performance ADC-driver style part. It has **260 MHz small-signal bandwidth**, **rail-to-rail output close to the rails**, adjustable output common-mode, and runs from **3 V to 7 V**. citeturn0search0turn0search4

Use this if:
- you want more analogue performance margin than THS4551,
- or you expect the downstream conditioning to benefit from a very clean differential source. citeturn0search0turn0search4

### Very fast classic option: **ADI AD8138**
If you want an aggressively fast diff driver, AD8138 is a classic. It has **320 MHz bandwidth** and is explicitly suited to **single-ended-to-differential** conversion. citeturn0search3turn0search7

I would pick it only if:
- speed is the top priority,
- and you are happy with an older, more power-hungry style part. citeturn0search7

## Part I would avoid for this specific job

### **TI INA149**
This one is interesting because it can handle very high common-mode directly and works as a **unity-gain difference amplifier**, but its bandwidth is only about **500 kHz**. That makes it too close to your signal of interest to be comfortable if the goal is a faithful 500 kHz waveform export. It is more “just about possible” than “good engineering margin.” citeturn0search6turn0search14

## My recommendation

I’d build it this way:

**OS node → 90.9 k / 10 k divider → THS4551 at gain 1 → spare differential pair**

That gives you:
- low loading on OS,
- safe input voltage for the active stage,
- lots of bandwidth margin over 500 kHz,
- and a proper differential output for your spare conditioning path. citeturn0search1turn0search5

## Small but important implementation notes

Put a **small capacitor across the lower divider resistor** only if you need to trim the HF response after layout; otherwise leave pads and fit DNI first. High-value dividers pick up parasitic capacitance, so it is worth giving yourself tuning options. That is an engineering recommendation rather than a datasheet fact.

Also:
- keep the divider physically close to the OS tap,
- put the FDA close to the differential output connector,
- route the differential pair tightly and symmetrically.

## Bottom line

For this requirement, I would choose:

**Topology:** passive ÷10 attenuator + FDA  
**Primary part:** **THS4551**  
**Upgrade option:** **ADA4940-1**  
**Avoid as primary path:** **MAX4173** for voltage export, **INA149** for bandwidth margin. citeturn0search1turn0search5turn0search0turn0search4turn0search6turn0search14

If you want, I’ll turn that into a concrete little schematic with resistor values and a suggested output common-mode.

[M54] ME (2026-03-06 12:25):
Could I just split down the already 5k6 load resistor. Sat 5k and 600r and tap off that?

[M55] AI (2026-03-06 12:25):
Yes, you **could**, but only if you’re happy that the new split resistor still does **both jobs** correctly:

1. keeps the **intended OS load/bias behaviour**, and  
2. gives you a **usable tap point** for the monitor path.

For example, replacing **5k6** with:

- **5k0 top**
- **604 Ω bottom**

keeps the total about **5.6 kΩ**, so the **overall DC load on OS stays about the same**.

At **28 V**:
- total current is still about **5 mA**
- voltage across the **604 Ω** section is about  
  \[
  28 \times \frac{604}{5604} \approx 3.0\text{ V}
  \]

That is attractive, because it gives you a tap near **0 to 3 V** when OS moves between 0 and 28 V.

## So electrically, the idea is valid
You’d have:

**OS node → 5k0 → tap node → 604 Ω → 0 V**

and the tap node is a **scaled copy of OS** at about **÷9.3**.

That means you may not need a separate divider at all.

## But there are two important catches

### 1) The tap must be high impedance
If you connect that tap straight into something with any real loading, you change the divider ratio and therefore change the **effective OS load**.

So the tap should go into:
- a **buffer**
- or a **very high input impedance amplifier**

not straight into something uncertain.

### 2) You are altering the original grounding/load network physically
A single 5k6 to ground is a very simple, clean load.
Splitting it creates a **mid-node**, which can pick up noise and capacitively couple rubbish unless laid out cleanly.

Also, if you later hang capacitance on that tap, you are no longer just “observing” the 5k6 load — you are shaping the OS waveform through the split network.

That can matter at **500 kHz**.

## My view
For a quick, elegant monitor path, this is actually a **good idea** provided you do it properly:

- split the 5k6 into **two precision resistors**
- take the tap into a **high-Z wideband buffer / FDA**
- keep the tap trace short
- avoid adding capacitance there unless intentional

## Better than a separate extra divider?
Often, yes.

Why:
- no extra loading beyond what was already there
- fewer components
- the scaling is built into an existing resistor that already belongs in the circuit

## Suggested values
Use standard values that sum close to 5k6 and give you a nice scale:

- **4.99 kΩ + 604 Ω** → about **3.02 V at 28 V**
- **5.11 kΩ + 499 Ω** → about **2.50 V at 28 V**
- **5.23 kΩ + 374 Ω** → about **1.87 V at 28 V**

So pick based on what the next stage wants.

### Best practical choice
If your downstream stage likes about **0–2.5 V**, then:

- **5.11 kΩ top**
- **499 Ω bottom**

is very neat.

If you want to use more range:
- **4.99 kΩ + 604 Ω**

is fine too.

## Recommendation
Yes — **splitting the existing 5k6 and tapping the midpoint is a sensible topology** for this job, and probably cleaner than adding a completely separate divider, **as long as the tap is buffered**.

I would do:
- **5.11 kΩ / 499 Ω**
- tap the midpoint
- feed that into a **high-input-impedance diff driver / buffer**

That gives you a scaled version of the full OS waveform without materially changing the total OS load.

If you want, I’ll sketch the exact next stage after that midpoint tap.

[M56] ME (2026-03-06 12:27):
No the tap will go to a single in differential out best spec part possible

[M57] AI (2026-03-06 12:27):
Yes — if you’re **splitting the existing 5k6** and taking the midpoint into a **single-ended to differential driver**, that’s a sound topology.

For your case, I’d do:

**OS node → 4.99 k / 604 Ω split load → tap midpoint → fully differential amplifier (gain = 1) → spare differential pair**

At 28 V, that midpoint is about **3.0 V**, while the total load stays essentially **5.6 kΩ**, so you preserve the original DC loading of the OS node. The tap only works properly if the next stage is **high impedance**. citeturn0search2turn0search0

## Best-spec part
If by “best spec” you mean **highest speed / most transparent at 500 kHz**, my first pick is:

### **AD8138**
Why:
- specifically intended for **single-ended-to-differential conversion**
- **320 MHz** small-signal bandwidth at gain 1
- **1150 V/µs** slew rate
- adjustable output common-mode
- very strong fit for exporting an analogue waveform cleanly. citeturn0search2turn0search5

That gives you far more analogue headroom than you need for a 500 kHz signal, which is exactly what you want if the ask is “get the raw OS waveform out” rather than “measure an average.” citeturn0search2turn0search5

## My second pick
### **ADA4940-1**
This is the cleaner “modern ADC-driver” style choice:
- low-power differential amplifier
- intended for high-resolution ADC interfacing
- good from dc to **1 MHz** applications
- adjustable output common-mode. citeturn0search1turn0search4

I’d choose this if you care more about a tidy precision path than absolute speed margin.

## My third pick
### **THS4551**
Also a very good part:
- **150 MHz** bandwidth at gain 1
- designed for precision differential drive
- low offset, low noise
- very low supply current. citeturn0search0turn0search3turn0search9

I’d choose this if you want a practical, efficient solution rather than the fastest one available.

## Recommendation
For **your stated goal**, I’d rank them:

1. **AD8138** — best pure waveform-driver choice  
2. **ADA4940-1** — best precision/ADC-driver style choice  
3. **THS4551** — best low-power practical choice. citeturn0search2turn0search1turn0search0

## Topology details
Use the split resistor as the attenuator, then:

- tap midpoint into the FDA input
- configure FDA for **gain = 1**
- set output common-mode to whatever the receiving conditioning expects
- keep the tap trace short
- keep the differential outputs tightly coupled.

One important caution: the split-load tap is fine **only if the FDA input is genuinely high impedance** and you do **not** hang extra capacitance on that midpoint, otherwise you start altering the OS waveform itself.

So yes — **splitting the 5k6 and feeding that midpoint into an AD8138** is probably the cleanest version of what you’re trying to do.

If you want, I’ll draw the exact resistor/gain/common-mode hookup for **AD8138** around that 4.99 k / 604 Ω tap.

[M58] ME (2026-03-06 12:31):
So this would also cater for the current measurement? By way of calaculation

[M59] AI (2026-03-06 12:31):
Yes — **partly**.

If you split the **5k6 load resistor** and tap the midpoint, then you can calculate the **current through that 5k6 load path** directly.

## If you split it like:
- **Rtop = 5k0**
- **Rbot = 600 Ω**
- total ≈ **5.6 kΩ**

and take the tap at the junction, then:

\[
I_{load} = \frac{V_{tap}}{600\ \Omega}
\]

Because the same current flows through both resistors.

So if:
- \(V_{tap} = 3.0\text{ V}\)

then:

\[
I_{load} = \frac{3.0}{600} = 5\text{ mA}
\]

That also means the full OS voltage is:

\[
V_{OS} = V_{tap} \times \frac{5600}{600}
\]

So yes, from that one tap you can derive:
- **scaled OS voltage**
- **current through the split 5k6 path**

---

## But this is the important limitation
That is **not the full OS current**, unless the **only** current path from OS is through that 5k6 branch.

In your circuit, OS also appears to feed:
- the follower/input network
- possibly other branches

So:

### What you can calculate from the split 5k6 tap
✅ **bleed/load current through the 5k6 path**

### What you cannot get from it directly
❌ **total OS source current**  
unless that 5k6 is the only load

---

## So the answer is:
- **Yes**, it caters for **current measurement by calculation**
- but only for the **split load resistor branch**
- **not necessarily total raw OS current**

---

## In practical terms
If their requirement is:

### “Get the raw OS waveform out”
then this topology is good.

If their requirement is also:

### “Know the 5k6 bleed current”
then yes, you get that for free from the tap.

If they want:

### “Know total OS current from the source”
then you still need a **true series current shunt** in the OS feed.

---

## Best way to think of it
The split-5k6 method gives you:
- **voltage monitor**
- plus **one known branch current**

It does **not** automatically replace a real total-current measurement.

If you want, I can show the exact equations for a couple of split values like **4.99k/604R** and **5.11k/499R** so you can pick the nicest tap voltage.

[M60] ME (2026-03-06 12:34):
There is a relay that toggles the line away from that follower base. This is done during noise cal where the OD is fed into the follower. So it is reasonable to say that the measurement could be taken in that state whereby all is current goes into that 5k6 branch 

[M61] AI (2026-03-06 12:34):
Yes — **that is a reasonable and defensible interpretation**, **provided the relay state genuinely disconnects the follower-base path** so the OS node is left with only the **5k6-to-ground branch** as its DC load.

In that calibration state:

- **OS current = 5k6 branch current**
- so the midpoint tap becomes a valid proxy for **total OS current**
- and you can derive it directly from the lower resistor voltage

So in that mode, your statement would be:

> During noise-cal relay state, the follower input is switched away from OS, therefore the OS node current is directed solely through the 5.6 kΩ load branch. In this state, OS current can be inferred directly from the split-load tap voltage.

That is technically sound.

## The condition you must be sure about
You need to confirm there is **no other significant parallel path** left on OS in that relay position, for example:

- clamp/leakage path
- monitor input loading
- protection network
- relay off-state leakage if it matters
- any hidden CCD internal path in that mode

If those are negligible relative to ~5 mA, then for engineering purposes:

**I_OS ≈ I_5k6**

and the method is good.

## Why this is actually quite a nice solution
It gives you, in that relay state:

- **raw OS waveform monitor** from the tap
- **OS current by calculation**
- no separate current shunt needed
- no extra series disturbance in the 28 V line

That is elegant.

## Equation
If you split the 5k6 into:

- \(R_{TOP}\)
- \(R_{BOT}\)

then in that calibration state:

\[
I_{OS} = \frac{V_{tap}}{R_{BOT}}
\]

and

\[
V_{OS} = V_{tap}\cdot\frac{R_{TOP}+R_{BOT}}{R_{BOT}}
\]

So for something like **4.99 k + 604 Ω**:

- at 28 V, tap is about **3.0 V**
- current is:
\[
I_{OS}=\frac{3.0}{604}\approx 5\,\text{mA}
\]

## The right wording
I would avoid saying it measures OS current in all modes.

I’d say:

> **In the noise-cal relay state, where the follower path is switched away, the OS current may be inferred from the split 5.6 kΩ load branch because this branch becomes the dominant or sole OS current path.**

That is precise and hard to argue with.

## Bottom line
Yes — **in that relay state, it is reasonable to treat the split 5k6 branch current as the OS current**, assuming no meaningful parallel path remains. That makes the split-load tap approach much stronger.

If you want, I’ll turn that into a short requirement note / design justification you can drop straight into the schematic comments or design review.

[M62] ME (2026-03-06 12:35):
It’s just that the OD (output drain) is connected into the follower instead. If that’s a potential issue I could use another relay gate but that then leaves the follower input floating 

[M63] AI (2026-03-06 12:35):
Yes — that **could be an issue**.

If the relay switches the follower input from **OS** over to **OD**, then in that calibration state the follower is **not disconnected**, it is just being **re-pointed**. So the split 5k6 branch is only a valid proxy for total **OS** current if:

- OS is no longer feeding the follower path at all, **and**
- there is no other meaningful OS branch left.

From what you’ve just said, that sounds true for **OS**, because the follower input is now looking at **OD instead**. In that case:

- **OS current measurement via the split 5k6 branch is still valid**
- but only for **OS**
- and only in that **noise-cal relay state**

So the main question becomes the **follower input behaviour** when switched.

## If you add another relay and leave the follower input floating
I would avoid that.

A floating follower input is usually bad news because it can:
- wander to an undefined bias point
- pick up noise
- intermittently turn the transistor on/off
- inject rubbish into your measurement path

So if you use another relay pole to disconnect OD as well, the follower input should **not** be left floating.

## Better options
### Best simple option
Give the follower input a **defined park state** when disconnected.

For example:
- a resistor to a known bias
- or a resistor to ground / a safe reference
- or switch it to a dummy source

That way the follower always sees a defined condition.

### Even better
Use the extra relay pole so the follower input is switched between:
- **normal signal source**
- **cal source**
- **defined quiet park node**

That is much cleaner than “connected” versus “floating”.

## For your specific measurement question
You do **not** need to disconnect the follower from OD just to make the **OS current** inference valid, provided:

- OS is genuinely switched away from the follower input
- the only remaining material OS path is the split 5k6 branch

So the fact that the follower is now watching **OD** is not itself a problem for the **OS-current-by-calculation** idea.

It only becomes a problem if:
- relay leakage/coupling still links OS into that path, or
- you were hoping the follower path was globally inactive.

## Practical conclusion
- **No, you do not need another relay just because the follower is now fed from OD.**
- **Yes, the split-5k6 method can still represent OS current in that state**, assuming OS is otherwise isolated.
- **Do not leave the follower input floating** if you do add more switching.

The clean engineering wording would be:

> In noise-cal mode, the relay diverts the follower input from OS to OD. Therefore OS no longer drives the follower path, and OS current may be inferred from the split 5.6 kΩ load branch, provided no other significant OS current path remains.

If you want, I can sketch the cleanest 2-relay-state arrangement so the follower input is always tied either to **OS**, **OD**, or a **park bias**, never floating.

[M64] ME (2026-03-06 12:39):
Can you review this precious content as see if anything could be missed opportunity regarding the use of threat spare relay gate?
[attached file: OK.docx]

[M65] AI (2026-03-06 12:39):
Yes — there **is** a missed opportunity, and it’s a useful one.

The earlier thread leaned mainly toward using the spare relay gate to **further isolate or park the follower input**, but the stronger opportunity is actually to use that spare pole to make the **measurement state explicit and deterministic**, not just “less floating.” That lines up with the broader design themes in your prior content: defined safe states, clean measurement access, and avoiding ambiguous alternate paths. fileciteturn1file0 fileciteturn1file3

## The key missed opportunity
Use the spare relay gate as a **measurement-mode topology switch** so that in noise-cal / OS-monitor mode you deliberately create:

- **OS connected only to the split 5k6 measurement branch**
- **follower input connected to OD or to a defined park node**
- **no floating analogue input anywhere**
- **no ambiguity about whether the inferred current is total OS current or just one branch**

That is better than just “extra isolation” because it gives you a **defined calibration state** you can document and verify.

## Best use of the spare relay gate
I’d rank the options like this:

### 1) Best option: switch follower input between **OD** and a **park bias**
This is the cleanest use.

In normal noise-cal:
- follower input = **OD**

In dedicated OS-measure mode:
- follower input = **parked**, not floating

That gives you:
- OS fully removed from follower loading
- follower not left wandering
- a true “OS current inferred from split 5k6 branch” state, assuming no other meaningful OS leakage path remains

A park node could be:
- a quiet DC bias near the follower’s normal operating region, or
- ground/reference via a resistor, depending on the transistor topology

This is better than simply disconnecting and floating the follower base.

### 2) Very good option: use the spare pole to create a **documented calibration mode**
This is more architectural:

- Relay state A: **normal**
- Relay state B: **noise-cal / OD to follower**
- Relay state C, using spare pole support: **OS isolated measurement state**

Even if you only have two logical modes, the spare pole can ensure one of those modes is truly metrologically clean.

That is valuable because your earlier content repeatedly emphasised **testability** and **controlled measurement paths**. fileciteturn1file6 fileciteturn1file10

### 3) Less valuable option: use it only to “disconnect something else”
That helps, but it misses the real value, which is **state definition**.

---

## What I would avoid
I would avoid using the spare relay gate just to:
- add more switching without a defined parked state
- leave the follower input high-Z
- multiplex yet another analogue path “just in case”

That creates exactly the kind of indeterminate behaviour your previous design notes were trying to stamp out. fileciteturn1file3

## The strongest configuration
Based on what you’ve described, the best arrangement is:

### Normal imaging mode
- follower input ← OS

### Noise-cal mode
- follower input ← OD

### OS measurement mode enabled by spare pole behaviour
- follower input ← park bias
- OS remains connected only to split 5k6 branch and monitor tap

Then in that third state you can legitimately say:

> OS current is inferred from the split load branch because the follower path is intentionally removed and the follower input is held in a defined inactive state.

That is much stronger than “probably all the current goes that way.”

## Another missed opportunity: diagnostics
The spare relay pole could also give you a very useful **sanity-check mode**:

- one mode where follower is on OD
- one mode where follower is parked

If the inferred OS current changes materially between those two when OS should be isolated, you’ve just exposed a hidden alternate path or leakage issue.

That is a nice built-in debug feature.

## My recommendation
Use the spare relay gate to **park the follower input in a defined bias state during OS-measure mode**, rather than merely disconnecting more things. That gives you:

- cleaner OS current inference
- no floating node
- a defensible calibration state
- a better story for review and verification

If you want, I can sketch the exact relay truth table for the three useful states so you can decide whether to implement it with the existing relay plus the spare pole.

[M66] ME (2026-03-06 19:42):
On the other end of the os differential routing it terminates into a two pin header. Could this be taken straight to a scope?

[M67] AI (2026-03-06 19:42):
Yes, **potentially**, but there’s a big catch:

## If that 2-pin header carries the **differential monitor signal**
then yes, it can be taken to a scope **provided the scope connection matches the signal type**.

### Safe / proper ways
- **Differential probe across the two pins** — best option
- Two scope channels, one on each pin, then **A−B maths** — can work
- A scope input that is genuinely **floating differential** — also fine

## The catch
If you use a normal bench scope probe with the ground clip, the probe ground is usually tied to **earth**.

So if either side of that 2-pin header is:
- not ground,
- riding on some common-mode voltage,
- or part of an actively driven differential pair,

then clipping scope ground to one pin can:
- short one side of the signal to earth
- disturb the measurement
- possibly damage the circuit or scope

## In your case
Because you were talking about **OS riding on 28 V**, or a conditioned **differential export** of that signal, the important question is:

### What exactly is on that 2-pin header?
There are two very different cases:

### Case 1 — it is the **conditioned low-voltage differential output**
For example:
- diff pair from your FDA / conditioning stage
- low common-mode, intended as an analogue differential signal

Then yes, that is very scope-friendly with:
- a **differential probe**, or
- **CH1 on pin 1, CH2 on pin 2, math CH1−CH2**

This is probably fine.

### Case 2 — it is the **raw tapped OS-related node pair**
If one or both pins are still sitting at high common-mode or not ground-referenced, then:

- **do not** just put a standard ground-referenced probe across it casually

---

## Best practical answer
If it is a **true differential output header from the conditioning path**, then:

**Yes — take it straight to a scope, but measure it differentially.**

### Preferred method
- probe both pins with either:
  - one **differential probe**, or
  - two standard probes and subtract in math mode

### Avoid
- ground clip on one pin unless you are absolutely sure that pin is system ground

## Another practical thought
If it’s only a 2-pin header and meant for measurement, a **3-pin header** is often nicer:
- Diff+
- Diff−
- local reference / shield / ground

Not for the measurement itself necessarily, but for tidy probing and cable management.

## Bottom line
**Yes, it may be scopeable directly — but only as a differential measurement.**  
A normal single-ended probe with a ground clip is only safe if one side is genuinely ground.

If you want, send the exact header connections and I’ll tell you the safest probing method immediately.

[M68] ME (2026-03-06 19:49):
P and n signals come in and go into an op amp each that buffers them either x1 or two. The outputs of those two op amps feed into another op amp to get the single end. It’s between these stages where there is a header 

[M69] AI (2026-03-06 19:49):
Yes — **that header is a very useful place to probe**.

Because it sits **between**:

- the first stage: **P and N each buffered separately**
- and the second stage: **the subtracting / single-ended conversion stage**

that header is effectively giving you access to the **raw differential pair after buffering**, before it gets collapsed into single-ended.

## What that means in practice
At that point you can measure:

- **P to N** as the true differential signal
- **P to ground** and **N to ground** individually
- whether one side is clipping / offset / noisier than the other
- whether the final subtraction stage is the bit causing trouble

That is actually a **better debug point** than the final single-ended output in many cases.

## How to scope it properly

### Best method
Use:

- **2 scope channels**
- one on **P**
- one on **N**
- then math **CH1 - CH2**

That gives you the differential waveform.

### Also useful
Look at each side individually first:
- CH1 = P
- CH2 = N

You’ll often learn a lot just by seeing whether they are:
- equal amplitude
- opposite polarity
- same DC offset
- one-sided distorted

## Important caution
This only works safely with ordinary probes if those buffered P and N outputs are **ground-referenced op-amp outputs within the scope input range**.

From your description, that sounds likely, because they’ve already gone through a buffer stage. So this is **not the same risk** as probing the raw 28 V OS node directly.

Still worth checking:
- op amp supply rails
- expected output common-mode
- whether either output sits outside normal scope range

## Why this header is a good missed opportunity
It gives you a chance to:

- verify the differential buffer stage independently
- bypass suspicion around the final differential-to-single-ended op amp
- inject / pick off signals cleanly
- potentially use that same node as your exported monitor point

So yes — this header may already be the cleanest observation point in the chain.

## One subtle point
If you’re thinking of using this header as the official monitor output, remember:

- it is **after** the first buffer stage
- so it is not the untouched raw signal
- but it is still a very faithful buffered differential version

That is often exactly what you want in real hardware.

## Bottom line
**Yes — that header is a very sensible point to take to a scope.**  
Probe **P and N separately**, then subtract them in the scope. That lets you inspect the buffered differential signal before the final single-ended conversion stage.

If you want, I can help you decide whether that point is good enough to satisfy the “raw OS out” requirement, or whether they’d still argue for tapping earlier.

[M70] ME (2026-03-06 19:52):
Hold on… it is located on the raw differential input 

[M71] AI (2026-03-06 19:52):
That changes it materially.

If the header is on the **raw differential input**, then yes, it is a much more direct observation point — but it is also a **more delicate one**.

## What that means
That header is now sitting **before the buffer op amps**, so probing there can:

- load the signal source
- unbalance the P/N pair
- add capacitance
- change the waveform you’re trying to inspect

So it can still be used for scope access, but you need to be more careful than if it were after the first buffer stage.

## Is it scopeable?
Yes, **provided you measure it differentially and lightly**.

Best order of preference:

### Best
Use a **proper differential probe** across P and N.

That gives:
- minimal loading imbalance
- no accidental grounding of one side
- best fidelity

### Next best
Use **two identical 10x probes**, one on P and one on N, both grounds to the same local reference only if that reference is genuinely circuit ground and both nodes are ground-referenced within allowed range.

Then use:
- **CH1**
- **CH2**
- math **CH1 - CH2**

This can work well, but the probes add capacitance to each side.

### Avoid
Do **not** casually clip a single probe ground onto one side of the raw differential pair unless one side is explicitly intended to be grounded. That can spoil or partially short the differential input.

## Main engineering concern
Because this is the **raw differential input**, the missed opportunity is not just “can I probe it?” but:

> should that header be treated as a proper measurement interface?

If you want it to be genuinely useful, it should ideally have:

- controlled access to **P and N**
- maybe small **series isolation resistors** before the sensitive front end
- perhaps a documented probing method

Otherwise the header is handy, but risky.

## For your OS-monitor idea
If you export the OS-derived signal into that raw differential input path, then this header could be a very nice debug point.

But remember:
- if it is truly upstream of the first buffers, it is **not a free probing point**
- it becomes part of the analogue input environment

## Practical conclusion
Yes, you can use it for a scope, but I would describe it as:

- **valid for careful differential probing**
- **not ideal for casual single-ended probing**
- **susceptible to probe loading because it is on the raw input**

If the goal is regular debug access, a better setup is:
- leave that header for internal routing/debug
- and add or keep a probe point **after the first buffer stage** as the safer observation node

That gives you both:
- true raw access if really needed
- buffered access for routine measurements

## Bottom line
If it’s on the **raw differential input**, then yes, it can be probed, but it is a **sensitive measurement point**, not a carefree one. For normal debug, a buffered downstream point is better.

If you want, I can help you decide whether a small series resistor at each raw input would make that header much safer without compromising the signal.

[M72] ME (2026-03-06 19:56):
Flowing
OS out
Into load 5k and 600r
Single ended tap off 600r
This gives 10:1 representation
Single to diff amplifier x1
Then it goes outside the chamber on diff routing
Arrives on the video conditioning board
Tap off there and present as monitor point for raw os
Use tektronix diff prove 

[M73] AI (2026-03-06 19:56):
Yes — that architecture is sound.

## What you’ve got
**OS out**  
→ **existing load split into 5 k + 600 Ω**  
→ **tap across the 600 Ω**  
→ gives about **10:1 scaled copy of OS**  
→ **single-ended to differential amplifier at ×1**  
→ **send over the chamber differential routing**  
→ **arrive on video conditioning board**  
→ **tap there as the raw OS monitor point**  
→ **measure with a Tek differential probe**

That is a coherent and defensible solution for **bringing out the OS voltage waveform**, not OS current.

## Why it works well
It does a few good things at once:

- keeps the **total OS load about the same** as the original 5.6 kΩ branch
- gives you a **scaled version** of the raw OS waveform
- avoids trying to sample a 500 kHz signal on a **200 kS/s ADC**
- exports it as a **differential signal**, which is much better for leaving the chamber
- lets you probe it safely on the warm side with a **diff probe**

## Important nuance
What you will be monitoring is not literally the untouched 28 V OS node.

It is:

> a **buffered, scaled, transported representation** of OS

That is usually exactly what people really need.

Calling it **“raw OS monitor”** is probably acceptable in conversation, but in design notes I’d phrase it more precisely as:

> **Scaled differential monitor of OS voltage waveform**

That avoids anyone later claiming it was meant to be a direct high-voltage tap.

## One correction to be careful about
Earlier you said “tap off 600 Ω.”

Strictly, you are not just tapping “off the 600 Ω” in a vague sense — you are taking the **midpoint of the 5 k / 600 Ω divider**, referenced to ground through the 600 Ω.

So the monitor voltage is:

\[
V_{MON} = V_{OS}\cdot\frac{600}{5600}
\approx 0.107 \cdot V_{OS}
\]

At 28 V that is about:

\[
28 \cdot 0.107 \approx 3.0\text{ V}
\]

So yes, essentially a **9.3:1** scaling, close enough to call **10:1** in conversation.

## Conditions for it to stay good
There are a few things worth locking down:

### 1) The single-ended to diff amplifier input must be high impedance
Otherwise it will disturb the divider ratio and the original 5.6 k load behaviour.

### 2) Keep capacitance off the divider midpoint
That midpoint is now your measurement node. Too much parasitic capacitance there will start to low-pass the OS waveform.

### 3) The differential link and receiver chain need enough bandwidth
For a 500 kHz signal, you want plenty of analogue margin. Your proposed diff transport approach is sensible for that.

### 4) The monitor point should be on the conditioning-board side
That is the right place for routine probing.

Much better than trying to get a probe into the chamber.

## About current measurement
This scheme does **not** directly measure total OS current in all modes.

What it gives you directly is:
- **OS voltage waveform**, scaled

And in the special state where OS only sees that split load branch, you can infer branch current from:

\[
I = \frac{V_{MON}}{600\ \Omega}
\]

But that is only valid when that branch is the only meaningful OS current path.

## I’d document it like this
Something like:

> OS is monitored by splitting the nominal 5.6 kΩ load into 5.0 kΩ + 600 Ω.  
> The midpoint provides an approximately 10:1 scaled representation of the OS voltage waveform.  
> This node is buffered and converted to a unity-gain differential signal for transmission out of the chamber over the spare differential routing.  
> The signal is made available on the video conditioning board as a monitor point for differential probing.

That is clear and technically tight.

## Bottom line
Yes — this is a good architecture.

It is probably the cleanest solution you’ve discussed so far for the requirement as now interpreted: **get the OS waveform out of the chamber**.

The only thing I’d tighten is the wording: call it a **scaled differential OS monitor**, not a literal raw node export.

[M74] ME (2026-03-06 20:01):
The header is a two way 0.1 inch pitch. What’s the Beatles way to bring this out to a panel 

[M75] AI (2026-03-06 20:02):
Yes — for a **panel bring-out**, I would **not** leave it as a bare 0.1" header on the panel.

The cleanest approach is:

**PCB 2-pin 0.1" header → short twisted pair / shielded pair harness → proper panel connector**

Since you’re planning to view it with a **Tek differential probe**, the best options are:

## Best practical option
**Two insulated coax bulkheads on the panel**  
One for **P**, one for **N**.

Why this is good:
- mechanically solid
- easy to label
- very scope-friendly
- each side stays well controlled
- you can probe with a differential probe or two matched scope channels

At 500 kHz this is comfortably fine.

Use:
- short internal harness from the 0.1" header
- twisted pair or two mini-coaxes
- panel bulkheads such as **SMA** or **SMB**

If this is a lab/debug panel rather than customer-facing hardware, **SMB bulkheads** are a nice sweet spot.

## Neatest single-connector option
**2-pin LEMO / Fischer style panel connector**

That’s the nicest “one hole in the panel” solution if you want something tidy and robust.

Why:
- compact
- locking
- good for repeated use
- easy to make a dedicated diff-probe breakout lead

This is probably the **best professional-looking option**.

## Lowest-effort option
**Keep the 0.1" header internally and bring it to a panel-mounted 2-pin locking wire connector**

For example:
- Harwin / Molex / similar 2.54 mm locking housing internally
- short shielded twisted pair to panel

That is fine electrically, but it is less nice for measurement than coax or LEMO.

Samtec does support **0.100" (2.54 mm) IDC/header systems**, so using the existing header as the board-side handoff is perfectly normal. citeturn1search1turn1search13

## What I would avoid
I would avoid:
- exposing the raw **0.1" pin header directly on the panel**
- long ribbon cable to the panel
- a connector that encourages somebody to clip a standard grounded scope probe onto one side casually

Tektronix notes that ordinary single-ended probe measurements are **ground-referenced**, and floating a grounded oscilloscope is unsafe, so you want the panel interface to naturally support **differential measurement**, not invite grounding one leg by mistake. citeturn1search0turn1search3turn1search6

## My recommendation
For your setup, I’d choose one of these:

**Best engineering/debug choice:**  
**2 × SMA bulkhead** or **2 × SMB bulkhead**, labelled **OS_MON_P** and **OS_MON_N**

**Best neat panel choice:**  
**1 × 2-pin LEMO-style connector**

Then run:
- **short shielded twisted pair** from the board header to the panel
- keep it away from noisy digital stuff
- no 50 Ω termination unless the driver/receiver scheme specifically wants it

Because this is only **500 kHz-ish analogue monitoring**, you do **not** need to overcomplicate it into RF practice. A tidy twisted/shielded differential run to a proper panel connector is enough.

My vote: **two SMB bulkheads** if this is mainly an engineering access panel, or **a 2-pin LEMO** if you want it to look properly integrated.

[M76] ME (2026-03-06 20:07):
Does it need to be shielded? Not sure where I would get the ground connection? Unless it comes from the letter side

[M77] AI (2026-03-06 20:07):
Not necessarily. For **500 kHz differential**, **shielding is nice but not mandatory** if the run is short and the pair is routed properly.

## What matters most
For this signal, priority is:

1. **keep P and N together as a twisted pair**
2. keep the run **short**
3. avoid running it alongside noisy digital / clock / power-switching lines
4. maintain a reasonably balanced path

That often gets you most of the benefit without a shield.

## About the ground
A differential signal does **not** need a ground conductor to function as the measurement pair itself. The receiver or diff probe is looking at:

\[
V_{diff} = V_P - V_N
\]

So the pair can be carried just as:
- **P**
- **N**

### But a shield is different
If you use a **shielded twisted pair**, the shield normally wants to connect to a **chassis or quiet reference**, not become one of the signal returns.

So yes, that ground/shield reference would usually come from the **receiving / panel / conditioning side**, or from the local board 0 V or chassis if available.

## Best practical rule
### If the link is short inside the system
Use just:
- **twisted pair**
- no shield

That is probably fine.

### If the route is longer, messy, or near noise
Use:
- **shielded twisted pair**
- connect shield at **one end only** initially, usually the **receiving / panel side**
- leave the other end unconnected unless testing shows a reason to bond both

That avoids creating a ground loop while still giving electrostatic shielding.

## Important distinction
Do **not** think of the shield as “the missing ground for the signal.”

The signal ground reference is already implicit in the electronics at each end. The shield is just there to reduce pickup.

## For your case
Because this is:
- differential
- only around **500 kHz**
- inside one system
- and not a long external cable

I would start with:

### Recommendation
**Use a twisted pair, no shield, if the run is short.**

If later testing shows pickup:
- move to **shielded twisted pair**
- tie shield to **chassis/0 V at the conditioning-board end only**

## If you bring it to a panel
Then the nicest arrangement is:
- **P and N on the connector**
- optional connector shell or separate braid tied to **panel/chassis**
- Tek diff probe measures **P to N**

So yes: **the shield ground would typically come from the receiving side / panel side**, not because the differential pair needs it to work, but because the shield needs somewhere sensible to terminate.

If you want, I can suggest the simplest cable type and connector arrangement for your exact panel layout.

[M78] ME (2026-03-06 20:09):
Could the then be looked at as ingle end but be a further 50% reduced 

[M79] ME (2026-03-06 20:10):
P

[M80] AI (2026-03-06 20:10):
Yes — **if you look at just one side, P-to-ground, you’ll see about half the differential swing**.

That is the normal relationship for a balanced differential signal:

- \(V_{diff} = V_P - V_N\)
- if it is symmetric, then **P** and **N** each carry **half** the total differential amplitude, opposite in polarity around the common-mode. TI notes that for a given supply, each side of a differential signal is typically half the amplitude of the equivalent single-ended swing. citeturn0search14turn0search17

So in your chain:

- after the **single-ended to differential** stage,
- if the outputs are balanced,
- then probing **P only** single-ended is fine for a quick look,
- but the amplitude will be about **50% of the full differential signal**.

### Example
If the differential output is:

- **2 Vpp differential**

then typically each leg is roughly:

- **1 Vpp single-ended** about its common-mode.

### The catch
Looking at **P only** gives you:

- one half of the signal,
- **plus its common-mode bias**.

So it is useful for a quick sanity check, but it is **not** the same as the true differential waveform.

### Best use
- **Quick debug:** look at **P** single-ended
- **Proper measurement:** use the **Tek differential probe across P and N**

That way you recover the full signal and reject common-mode pickup. Differential signalling is specifically used to improve common-mode rejection and preserve signal fidelity. citeturn0search19turn0search4

### One more caution
Only look at **P** single-ended if that node is safely ground-referenced within your scope input limits. If it is already on the video conditioning board after the driver stage, that is usually fine.

So yes: **you can view P single-ended, and it will be roughly a 50% version of the full differential signal.**

[M81] ME (2026-03-06 20:11):
Howndonininterface the diff probe with this lemo

[M82] AI (2026-03-06 20:11):
Simplest way: **don’t interface the diff probe through the LEMO directly unless you make a tiny breakout lead**.

For a 2-pin LEMO carrying:

- **Pin 1 = P**
- **Pin 2 = N**

the clean setup is:

## Best approach
Make a short **LEMO-to-probe breakout**:

- LEMO plug on one end
- two short tails on the other:
  - **P tail**
  - **N tail**

Then connect:
- diff probe **+** to **P**
- diff probe **−** to **N**

That’s it.

## If the probe has hook clips
Make the breakout end as:
- two short insulated pins or sockets
- or two small turret/test posts
- or two mini grabber-friendly wires

That gives the Tek diff probe something easy to clip onto.

## If the probe has browser tips / square pins
Bring the LEMO out to:
- a tiny 2-pin header
- or two probe loops

That is often the nicest bench setup.

## What not to do
Do not try to use:
- one side of the LEMO as “signal”
- panel/chassis as the return

A differential probe wants to see **P and N directly**.

## Practical pinout
I’d define it clearly:

- **LEMO pin 1 = OS_MON_P**
- **LEMO pin 2 = OS_MON_N**

Optional:
- connector shell to **chassis**, if you have a chassis bond available  
  but **not** as the measurement return

## Easiest lab-friendly implementation
Honestly, the easiest thing is:

**LEMO on panel → short mating LEMO lead → tiny breakout box or heatshrink split to two labelled flying leads**

Labels:
- red = P
- blue/black = N

Then the diff probe clips straight on.

## If you want it really tidy
Use a little adapter lead:
- LEMO plug
- 10–20 cm twinax or twisted pair
- end in either:
  - 2-pin 0.1" female
  - two gold sockets
  - two MMCX/SMA test points if you want a more formal interface

## One subtle point
If you only ever want to use the Tek diff probe, a **2-pin LEMO is fine**.

If you also want occasional single-ended viewing of just **P**, then a **3-pin connector** can be nicer:
- P
- N
- local reference/chassis

But for true differential measurement, 2-pin is enough.

## My recommendation
Use:
- **2-pin LEMO on panel**
- short **LEMO-to-flying-lead breakout**
- Tek diff probe clips to those two leads

That is the cleanest and least troublesome way.

If you know the exact Tek probe model, I can tell you the nicest physical breakout style for that specific tip set.

[M83] ME (2026-03-06 20:17):
[image]
They come with these sorts of connectors 

https://www.farnell.com/datasheets/1759783.pdf?_gl=1*1fakamc*_gcl_au*MTYwMTYyMzg2My4xNzcyNjQ5OTE0
[attached file: B53F570F-92D5-4980-985A-D79A5DDD2307.jpeg]

[M84] AI (2026-03-06 20:17):
Yes — with that Tek probe kit, you probably **don’t need a LEMO at all** just for this monitor point.

Those accessories are meant for exactly this kind of job: clipping onto a **small 2-point differential signal**.

## Easiest interface
Bring your monitor out to something the probe can grab directly, such as:

- a **2-pin 0.1" header**
- two **turret / loop test points**
- two closely spaced probe pins

Then the Tek differential probe’s little accessory leads clip straight onto **P** and **N**.

## Best panel approach with that probe
If this is mainly an **engineering monitor point**, the cleanest panel solution is often:

### Option A — 2-pin header behind a small access hole
- panel label: **OS MON + / −**
- short twisted pair from board to header
- open panel or small service flap
- probe clips straight on

Very simple, very practical.

### Option B — two insulated test sockets / probe loops on panel
- one for **P**
- one for **N**
- spaced to suit the probe accessories

That is probably the nicest “bench friendly” option.

## Less ideal
A **2-pin LEMO** is still fine, but then you need:
- mating plug
- breakout lead
- extra adapter

So unless you specifically want a rugged locked panel connector, it is **more effort than necessary**.

## What I’d recommend for your case
Because this is a **debug / monitor** function, not a production I/O, I’d do one of these:

### Best practical choice
**Two small insulated panel test points** labelled:
- **OS_MON_P**
- **OS_MON_N**

or

### Cheapest / simplest
**2-pin 0.1" header** on the conditioning board, accessible from panel/service side.

Then use the Tek probe accessories directly.

## One thing to avoid
Do not make it something that encourages someone to use:
- one standard passive probe to ground

because this is meant to be viewed **differentially**.

## Bottom line
Given the Tek accessories you showed, the **best interface is probably just two accessible test points or a 2-pin header**, not a LEMO. The probe kit is already designed to connect to small differential nodes directly.

[M85] ME (2026-03-06 20:19):
I’m thinking two panel smb. Then a tiny PCB or overboard that plugs onto them and presents a two pin interface to the probe 

[M86] AI (2026-03-06 20:19):
Yes — that’s a **good solution**.

It gives you:

- a proper **panel interface**
- tidy, robust connection through the panel
- and a **sacrificial / custom little adapter** for the Tek probe, instead of fighting the panel connector every time

## The architecture
**Board diff pair**  
→ short internal twisted pair / twinax  
→ **2 × panel SMB bulkheads**  
→ **small plug-on adapter PCB or overmoulded lead**  
→ **2-pin probe interface for the Tek diff probe**

That is clean.

## Why it’s a strong approach
### SMBs on the panel
Good because they are:

- compact
- more robust than dangling headers
- easy to label P and N
- easy to unplug
- perfectly fine at your bandwidth

### Small adapter PCB
Also good because it lets you:

- define a **probe-friendly geometry**
- add labels
- optionally add protection / damping
- avoid wear on the real hardware

It basically becomes a little **measurement dongle**.

## Best way to implement the adapter
I’d make the adapter as a **tiny differential breakout card** with:

- **2 × SMB jacks/plugs** to mate with the panel
- short controlled/simple routing
- output to either:
  - **2-pin 0.1" header**
  - two **probe loops**
  - two small **gold pins** spaced nicely for the Tek accessory lead

### Best probe-facing format
For that Tek kit, I’d lean toward:

- **two probe loops** or
- **2-pin 0.1" male header**

rather than another fancy connector.

That keeps it simple and field-replaceable.

## Nice extra features on the little PCB
Worth considering:

- silkscreen **P** and **N**
- optional **100 k bleed / bias resistors** only if needed, normally DNI
- optional **small series resistors** like 22–51 Ω in each leg, DNI by default
- maybe one **ground/chassis pad** purely as a convenience reference, not part of the differential measurement

## One thing to watch
If the two SMB bulkheads are separate singles, make sure:

- they’re mounted close together
- the internal wiring from board to panel stays as a **tight pair**
- the tiny adapter doesn’t create a big loop area

At 500 kHz you don’t need RF perfection, but you do want symmetry.

## Even better than a PCB, in some cases
A very simple alternative is:

- two short SMB patch leads
- into a tiny heatshrink breakout with a 2-pin header on the end

That’s mechanically less elegant, but sometimes quicker and more forgiving than a rigid PCB if panel spacing is awkward.

## My recommendation
Your idea is good. I’d do:

- **2 × panel SMB bulkheads**
- a **small removable adapter PCB**
- adapter presents **2-pin 0.1" header or probe loops**
- label everything clearly **OS_MON_P / OS_MON_N**

That gives you a professional panel solution without making the Tek probe interface awkward.

One refinement: make the adapter PCB the “consumable” piece, not the panel hardware. That way if the probing interface changes later, you only redesign the little adapter.

[M87] ME (2026-03-06 20:20):
Would it be best to remove the buffers that the diff pair would have previously driven?

[M88] AI (2026-03-06 20:20):
Probably **yes, for this monitor path** — or at least make them **disconnectable**.

If you now want that diff pair to act as a **transport path for OS monitor**, then leaving the old buffer inputs hanging on the line risks:

- extra loading
- extra capacitance
- possible bias interaction
- uncertainty about what the line is really seeing

And that works directly against your goal of a **clean exported waveform**.

## Best answer
### Ideal
**Remove / isolate the previous receiving buffers from that pair** when it is being repurposed for OS monitor.

That gives you:
- known load
- cleaner bandwidth
- cleaner amplitude
- simpler story in review

## Best implementation
If you might want flexibility later, don’t hard-delete immediately. Instead give yourself a selection method such as:

- **0 Ω links**
- resistor packs
- DNI options
- solder bridges

So you can choose either:
- **legacy buffer destination**, or
- **OS monitor destination**

but not both at once.

That is the cleanest engineering approach.

## Why this matters
Your single-ended-to-diff stage wants to see a reasonably defined load.  
If the old buffers remain connected, even if “high impedance” on paper, they still add:

- input capacitance
- leakage
- ESD structure loading
- possible common-mode constraints

At **500 kHz**, this is not microwave territory, but it is definitely enough for unnecessary loading to start softening things or skewing balance.

## When you might leave them in
Only leave the old buffers connected if all of these are true:

- their input impedance is very high
- their input capacitance is small
- they are powered and biased correctly in this mode
- they do not corrupt the common-mode
- you are happy with the combined loading

Even then, I’d still prefer not to.

## My recommendation
For a repurposed spare diff pair:

- **disconnect the old receiving buffers**
- use the pair solely for the OS monitor path
- keep the option to restore legacy use with **0 Ω links or DNI parts**

That gives you a clean, defensible implementation.

## Practical wording
You could describe it as:

> The spare differential route is repurposed as a dedicated OS monitor transport path. Legacy receiver inputs are isolated to prevent loading and preserve waveform fidelity.

That’s the right design intent.

If you want, I can sketch the neatest strap arrangement for this so you retain future reversibility.

[M89] ME (2026-03-06 20:20):
Can you get insulated smb panel mounts?

[M90] AI (2026-03-06 20:20):
Yes — you can get **insulated / isolated panel-mount SMBs**, but they are **less common than standard grounded bulkheads**, so you may need to search specifically for terms like **isolated ground**, **insulated bulkhead**, or **non-grounding bulkhead** rather than just “SMB panel mount.” Standard SMB families definitely include **bulkhead / panel-mount jacks**, and some RF connector/adaptor lines explicitly offer **isolated-ground varieties**. citeturn0search10turn0search11turn0search1

For your application, though, you probably **do not need insulated SMBs** unless you specifically want the connector shell **not** bonded to panel/chassis. Since you’re carrying a **differential monitor pair** and planning to probe **P-to-N** with a Tek differential probe, the signal itself does not need a panel ground return; insulation only matters if the panel or shell bonding could create an unwanted reference or loop. If the panel is benign and a grounded shell is acceptable, ordinary SMB bulkheads are usually fine. citeturn0search6turn0search11

So the practical decision is:

- If you want the neatest, easiest parts choice: use **standard SMB bulkhead jacks**.
- If you want the panel shell kept electrically separate from the signal environment: look for **isolated-ground / insulated bulkhead SMB** specifically. RF vendors and adaptor lines do make isolated-ground variants in this general connector class. citeturn0search1turn0search10

For your monitor path, I’d start by assuming **standard SMB bulkheads** unless you already know the panel/chassis bond is a problem. That keeps the mechanical side simple.

[M91] ME (2026-03-06 20:22):
Solder cup? Tight twisted pair. Keep them close 

[M92] AI (2026-03-06 20:22):
Yes — **solder-cup panel SMBs with a tight twisted pair kept close together** is a good way to do it.

For your signal, that’s a sensible build.

## What to aim for
- **2 × panel SMB bulkheads**
- **solder-cup termination on the rear**
- run **P and N as a tight twisted pair**
- keep the two SMBs **physically close together** on the panel
- keep the internal run **short**

## Why it works
At your sort of bandwidth, the important thing is not fancy RF practice, it’s mainly:

- preserving the **pair balance**
- minimising loop area
- avoiding picking up rubbish
- keeping the path tidy and repeatable

A **tight twisted pair** does that well.

## Good practice
- Put the two SMBs as close as mechanically practical.
- Twist right up to the solder cups if you can.
- Do not separate P and N into long individual wires near the connector.
- Keep the pair away from noisy digital edges, clocks, switching rails.

## Shielding
For this, I’d start with **just twisted pair**.  
Only move to shielded pair if testing shows pickup.

## One caution
If the SMB shells bond to panel/chassis, just be aware of that mechanically/electrically. It may be totally fine, but it’s worth knowing whether the panel is floating or grounded.

## Bottom line
**Yes — solder-cup SMB bulkheads, wired with a short tight twisted pair and mounted close together, is a sound approach.**

[M93] ME (2026-03-06 20:23):
Is there a snazzy 0.q inch header and socket that can be used as opposed to standard headers. Prob more for aesthetics but nice to recognise it as a respected tap 

[M94] AI (2026-03-06 20:23):
Yes — instead of a plain 0.1" pin header, you can absolutely use something that looks more deliberate and “instrumentation-grade”.

For a respected monitor tap, I’d think in three tiers:

## Best fit for what you mean
### **Harwin M30 / M50 style gold-pin connectors**
These feel much more “serious” than generic 0.1" headers.

Why they work well:
- gold machined contacts
- much nicer mate/unmate feel
- available as pin headers and sockets
- visually read as a deliberate engineering interface, not a random jumper header

They’re a very good choice if you want:
- small 2-pin or 3-pin monitor connectors
- robust repeated use
- a cleaner lab/instrument feel

## Slightly more premium / compact
### **JST GH / SH / Molex PicoBlade / similar**
These look much tidier than 0.1", especially if you want a cable assembly.

Good when:
- you want a keyed compact connector
- you don’t want anyone casually plugging the wrong thing in
- aesthetics and neatness matter

Less good if:
- you want direct probe access at the connector itself

These are more “productised harness connector” than “tap point”.

## Most “special test point” feel
### **Micro-coax / twinax style board connector**
If the point is really a respected differential monitor, you can use:
- a tiny 2-pin coaxial/twinax style interconnect
- or a miniature board connector leading to your little SMB adapter board

That makes it feel very intentional, but it is more effort than you probably need.

---

# My actual recommendation
For your use case, I’d use one of these:

### Option A — best balance
**2-pin Harwin gold-pin header + matching socket**

Why:
- nicer than standard 0.1"
- still easy to hand-build
- probe adapter board can plug on/off cleanly
- looks like an intentional engineering access point

### Option B — if you want it more product-like
**2-pin JST GH**

Why:
- compact
- keyed
- neat
- feels official

But it’s less “scope-friendly” unless you make a dedicated breakout lead.

---

# If this is mainly aesthetics and status
Then the trick is not just the connector — it’s the presentation:

- use a **dedicated footprint**
- label it clearly, e.g. **OS MON DIFF**
- maybe use a different silkscreen box or outline
- gold pins / black housing helps a lot
- put it in a clearly defined instrumentation area of the PCB

That often matters more than the connector family itself.

---

# What I would avoid
I would avoid:
- plain square-post 0.1" headers if you want it to feel special
- Dupont-style loose jumpers
- anything that looks like a temporary bodge/programming link

---

# Best overall answer
If you want it to look like a **proper respected tap**, I’d go with:

**a 2-pin Harwin machined/gold header and mating socket**

It keeps the convenience of a small simple interface, but looks far more intentional than a bog-standard header.

If you want, I can suggest the nicest exact connector style for either:
- **board-to-small adapter PCB**, or
- **board-to-flying lead harness**.

[M95] ME (2026-03-06 20:26):
Remember this board already exists. I’m just using what’s there. Suggest part numbers for Hardin and jst

[M96] AI (2026-03-06 20:26):
Yes — if the board already exists, the key distinction is:

- **Harwin M20** can be a near drop-in if your existing tap is a **plain 2.54 mm / 0.1" 2-pin header footprint**.
- **JST PH/GH/etc.** will need a **different footprint**, so they’re only useful for a little adapter board or cable harness, not as a direct swap on the existing PCB. citeturn1search1turn1search2turn1search9

## Harwin options
For a nicer-looking 0.1" 2-pin through-hole header:

- **Harwin M20-9730245** — 2-position, single-row, vertical, through-board, 2.54 mm pitch, gold finish. This is the cleanest “direct replacement” style part. citeturn1search1
- **Harwin M20-9990245** — also 2-position, single-row, vertical, through-board, 2.54 mm pitch, gold finish, with a slightly different mating pin length. citeturn1search8

If you want tin instead of gold:
- **Harwin M20-9730246** — same basic 2-pin 2.54 mm vertical format, tin finish. citeturn1search3

My pick here is **M20-9730245**.

## JST options
If you decide to use JST on a little breakout or flying-lead adapter:

- **JST PHR-2** — 2-way housing for the PH series, 2.0 mm pitch. citeturn1search15turn1search9
- **JST B2B-PH-K-S** — common 2-way vertical PCB header for PH-series cable mating. The PH series is JST’s 2.0 mm wire-to-board family. citeturn1search2turn1search9

For your situation, JST is better suited to:
- a **small adapter PCB**
- or a **little plug lead**
rather than replacing the existing on-board 0.1" tap.

## Practical recommendation
Because you’re reusing what’s already there, I’d do this:

- On the existing board: **Harwin M20-9730245**
- On any little probe adapter / dongle / harness: JST only if you want a keyed cable interconnect

So the clean answer is: **Harwin for the actual board, JST for any secondary harness if needed.**

[M97] ME (2026-03-06 20:27):
Do Hardin make pig tail interfacing leads?

[M98] AI (2026-03-06 20:27):
Yes — Harwin do make ready-made cable options, but mostly in their **higher-reliability ranges** rather than as simple “Dupont-style 0.1 inch pigtails.”

What Harwin officially offers includes:

- **pre-crimped contacts / pre-wired leads** in the **Datamate** family, including single pre-crimped contacts with wire attached, such as **M80-9220099**. citeturn0search0
- broader **ready-to-use cabled connectors and cable assemblies** in the **Datamate** range. citeturn0search1

For a plain **2.54 mm / 0.1" board header** aesthetic upgrade, Harwin’s M20 headers are a good fit, but Harwin generally is **not** the brand I’d expect to supply off-the-shelf “2-pin 0.1 inch pigtail leads” in the casual jumper-wire sense. Their stronger offering is more “connector system + contacts/cable assembly” than hobby-style loose pigtails. That’s also consistent with Harwin’s own guidance comparing discrete cabling and connector assembly styles. citeturn0search2turn0search1

So for your existing board:

- use a **Harwin M20** part if you want the board connector to look more deliberate
- for the flying lead / pigtail, it is usually easier to use:
  - a custom crimped lead,
  - a small adapter harness,
  - or a different connector family that has ready-made cable assemblies

If you want the neatest practical route, I’d do:
- **Harwin M20 header on the board-side adapter or mating interface**
- and a **custom 2-wire twisted pigtail** made to suit the SMB or probe arrangement

For a true off-the-shelf pigtail ecosystem, JST, Molex, or TE are usually easier than Harwin.

[M99] ME (2026-03-06 20:37):
[image]
[image]
[image]
This will be good 
[attached file: C4765331-53D2-42B3-BDC7-8A6E2BA508F9.jpeg]
[attached file: CD29A135-4C09-4E26-B5FD-BFC3DD17A5DF.jpeg]
[attached file: 6ECA05BF-0DEE-48D3-8245-AFA5B4C4941D.jpeg]

[M100] AI (2026-03-06 20:37):
Yes — **that style is a good fit**.

That Johnson / Cinch flange-mount **panel SMB jack** looks well suited for what you’re doing.

## Why it suits the job
- **Flange mount**: nice and secure on a panel
- **Rear solder pin**: easy to hand-wire with your short twisted pair
- **Compact**: you can get the P and N connectors close together
- **Mechanical quality**: looks like a proper instrumentation bring-out, not a bodge

## What to check before you commit
Just make sure of three things:

### 1) Rear termination style
You want the back end to be something you can sensibly wire to:
- centre pin for signal
- body/shell if needed

From the picture, it looks like a **solder/post style rear**, which is good.

### 2) Shell grounding
Check whether the shell is:
- **bonded to panel/chassis**, or
- isolated by how you mount it

For your differential monitor this is usually fine, but you want to know the behaviour rather than discover it later.

### 3) Panel spacing
Make sure two of them can sit:
- close enough together to keep the pair tidy
- but with enough room to plug/unplug SMBs comfortably

## My view on your plan
For:
- **OS_MON_P**
- **OS_MON_N**

using **two of these on the panel** is a strong solution.

Then inside:
- short twisted pair from board to the two SMBs
- keep the pair tight right up to the rear terminations

Then outside:
- your little SMB-to-probe adapter board/lead

That’s a neat architecture.

## One practical caution
Because this is a **differential analogue monitor**, don’t let the panel connector choice tempt people into treating each SMB like an independent single-ended scope point. Label them clearly as a pair:
- **OS MON +**
- **OS MON −**
- maybe even **DIFF ONLY**

## Bottom line
**Yes — that connector style looks good for the job.**  
I’d be happy using a pair of those for this monitor interface.

[M101] ME (2026-03-06 20:57):
[image]
Is there a male version of this? 
[attached file: 99E31EF6-504B-4F59-853D-F447C73C86BD.jpeg]

[M102] AI (2026-03-06 20:58):
Yes — but **SMB gender naming is a bit backwards-looking**, so it’s easy to get tripped up.

For SMB, the mating face can be described by both:
- **plug / jack**
- and **male pin / female socket**

Those do not always line up the way people expect from everyday language. Digikey’s SMB listings show both **“Jack, Male Pin”** and **“Plug, Female Socket”** as valid SMB part descriptions. citeturn1search7turn1search2

So for the part you showed, the safest way to choose is:

- ignore “male/female” at first
- decide what you want on the **panel mating side**
- then pick the SMB type by **centre contact on the mating face**

## From your screenshot
That Johnson/Cinch **133-3701-621** looks like a **panel flange SMB receptacle/jack style** part with a solder termination on the rear. The visible mating face in your screenshot appears to be a **socket/receptacle-style front**, while the rear protruding pin is just the internal solder/contact tail, not the external mating gender. Your screenshot shows it as a Johnson/Cinch SMB flange-mount connector, and Johnson/Cinch offer SMB connectors in multiple jack/plug and flange styles. citeturn1search2turn1search7

## So: is there a male version?
**Yes, almost certainly in the Johnson/Cinch SMB family**, but the way to search it is:

- **SMB flange mount jack, male pin**
or
- **SMB flange mount plug receptacle**
or
- **panel mount SMB male pin**

not just “male version”.

## Practical advice for your use
If you want the **panel to present a protruding centre pin at the mating face**, then look for:

**SMB panel jack, male pin, flange mount**

If you want the panel to present the more protected **socket-style face**, stay with the type you’ve found.

## My recommendation
For a monitor interface on a panel, I’d usually stay with the **protected receptacle/socket-style face**, not the exposed pin style. It is mechanically safer and less likely to get damaged.

So yes, a male-centre-contact panel alternative should exist, but I suspect the one you already found is actually the better choice for this application.

If you want, send me the mating part you intend to plug into it, and I’ll tell you whether this exact Johnson part is the right gender pairing.

[M103] ME (2026-03-06 20:58):
This is an mcx

[M104] AI (2026-03-06 20:58):
Yes — you’re right, that one is **MCX**, not SMB.

The pictured part number **133-3701-621** is a **flange-mount MCX jack / receptacle**, so the matching “male” counterpart is an **MCX plug**.

A couple of terminology points so it doesn’t get muddled:

- **Panel part shown:** MCX **female jack / receptacle**
- **Cable mating part:** MCX **male plug**

If you want the same style but male on the panel side, that’s usually described as:

- **MCX bulkhead plug**
- **MCX panel-mount plug**
- sometimes **flange-mount MCX plug**

Just be aware that for panel interfaces, the **jack on panel / plug on cable** arrangement is usually the more normal and safer one mechanically.

So for your idea:

- **Panel:** 2 × MCX flange jacks
- **Adapter dongle / little PCB:** 2 × mating MCX plugs
- then break out to your 2-pin probe interface

That is actually a nice solution.

If you want, I can help you find the correct **mating MCX plug style** for either:
- a **tiny PCB adapter**, or
- a **short flying lead adapter**.

[M105] ME (2026-03-06 20:59):
Both 

[M106] AI (2026-03-06 20:59):
Yes — for **both** approaches.

For your panel part **133-3701-621**, the mating side is an **MCX jack, female socket, panel-mount solder**. citeturn0search0turn0search6

## 1) Flying-lead / pigtail adapter
The straightforward mate is a **free-hanging MCX plug, male pin**.

Good Johnson/Cinch options:
- **133-9403-001** — straight, free-hanging, crimp or solder MCX plug, male pin. citeturn0search1turn0search3
- **133-3403-001** — another straight free-hanging MCX plug, male pin, crimp or solder. citeturn0search5
- **133-3403-101** — right-angle free-hanging MCX plug, male pin, solder. citeturn0search9

For your use, I’d pick:
- **straight flying lead:** **133-9403-001**
- **right-angle if space is awkward:** **133-3403-101**

## 2) Tiny PCB adapter
For a little breakout PCB that plugs onto the panel connectors, you want an **MCX board-mount plug**. Johnson explicitly offers **board-mount MCX connectors**, including **surface-mount and end-launch** types in the family. citeturn0search15turn0search13

So the topology would be:
- **2 × panel 133-3701-621**
- mate to **2 × MCX male plugs** on either:
  - short cable pigtails, or
  - a tiny adapter PCB using board-mount MCX plugs

## My practical recommendation
For what you’re doing:

### Best for quick implementation
Use **2 × 133-9403-001** on short twisted pigtails, then break out to:
- 2-pin header
- probe loops
- or a tiny custom dongle

### Best for a neat removable dongle
Use a **small PCB with 2 × board-mount MCX male plugs**, then present:
- a 2-pin 0.1" header
- or dedicated Tek-probe-friendly pads/loops

One caution: before ordering the PCB-plug version, double-check whether you want **vertical / edge-launch / right-angle** mechanical style, because that depends entirely on how your two panel MCXs are spaced and how the dongle will sit.

If you want, I’ll help you choose between **pigtail** and **rigid PCB dongle** based on your panel spacing and whether the two MCXs are side-by-side or stacked.

[M107] ME (2026-03-06 21:03):
On the PCB adaptor, or a separate one. I want a little circuit to convert to single ends what’s the best receiver 

[M108] AI (2026-03-06 21:03):
Yes — for **this specific job**, I’d put the **diff-to-single-ended receiver on a proper little powered PCB**, not in a passive dongle unless the dongle itself can carry power and stay mechanically sane.

For the receiver itself, the cleanest fit is:

## Best fit: **AD8130**
It is explicitly a **differential-to-single-ended receiver amplifier**, intended for signals sent over **twisted pair**, and ADI calls out its high CMRR at high frequency for exactly this kind of conversion. It also has **270 MHz bandwidth at gain = 1**, **1 MΩ differential input impedance**, and a **wide supply range from single +5 V to ±12 V**. citeturn1search0turn1search1turn1search13turn1search14

That matches your use very well because you have:
- a transported **differential analogue monitor**
- only around **500 kHz**
- a desire not to load the line much
- and a need to recover a clean **single-ended monitor point** on the far side.

## Why I’d pick it over a generic op-amp stage
A generic subtractor can work, but the whole point here is **high-frequency CMRR** and clean recovery after a differential run. AD8130 is designed as a **line receiver**, not just “an op-amp you can wire as a subtractor.” ADI also shows it specifically as a high-speed differential line receiver and notes about **70 dB CMRR at 10 MHz** in the application material. citeturn1search0turn1search14

## Second-choice parts
If you want alternatives:

### **AD8129**
Very similar family, also a differential receiver, but **200 MHz** rather than 270 MHz. Still miles beyond what you need for 500 kHz, but if I had the choice I’d still prefer AD8130. citeturn1search1turn1search6

### **AD830**
Also a wideband differencing amplifier and useful at video frequencies, but for your case the **AD8130 is the more direct “twisted-pair receiver” answer**. citeturn1search12

## What I would not use here
I would not use an instrumentation amp type part for this if the goal is to preserve the waveform, because most of those are not the right tool once you care about **500 kHz analogue transport** and decent HF CMRR.

## Practical topology
I’d do:

**MCX pair / diff pair in**  
→ optional light input termination / damping  
→ **AD8130** at **gain = 1**  
→ single-ended monitor output  
→ scope/header/ADC as needed

## A few practical points
- Put the receiver on the **conditioning-board side**, not on a dangling passive adapter, unless you also want to power that adapter.
- Keep the diff pair into the AD8130 tight and symmetrical.
- If your differential driver is low-voltage, check the common-mode and swing so the AD8130 output is centred where you want it.
- If you want both diff and single-ended monitor access, add both:
  - the raw diff tap
  - and the AD8130 single-ended output

## Bottom line
**Best receiver:** **AD8130**.  
It is the most “made for this” answer out of the obvious choices. citeturn1search0turn1search1turn1search14

If you want, I’ll give you a minimal AD8130 gain-of-1 hookup around your MCX pair and tell you what to do with termination.

[M109] ME (2026-03-07 09:40):
What’s the tightest 10:1 network that achieves 5k6

[M110] AI (2026-03-07 09:40):
The nearest neat **10:1 split** that still totals about **5.6 kΩ** is:

- **5.11 kΩ top**
- **562 Ω bottom**

Total:
\[
5.11k + 562 = 5.672k\Omega
\]

Tap ratio:
\[
\frac{562}{5672} = 0.0991
\]

So that gives about **10.09:1**, which is very close.

At **28 V** the tap would be:
\[
28 \times 0.0991 \approx 2.77V
\]

## If you want the mathematically exact target
Exact 10:1 with total **5.6 kΩ** would be:

- **5040 Ω top**
- **560 Ω bottom**

because:
- total = **5600 Ω**
- bottom = **1/10 of total**

But those are not both common preferred values.

## Practical best picks
### Best standard-value choice
- **5.11 kΩ + 562 Ω**

### If you want exact total 5.6 kΩ
- **5.04 kΩ + 560 Ω** if you can source **5.04 kΩ** easily

### If you want easy/common values and don’t mind slightly higher tap
- **4.99 kΩ + 604 Ω**
- total = **5.594 kΩ**
- ratio = **0.108**
- about **9.27:1**

So for your stated ask, the cleanest answer is:

**5.11 kΩ + 562 Ω**  
That’s probably the tightest easy standard network.

[M111] ME (2026-03-07 09:42):
Assume I have 4 footprints available 

[M112] AI (2026-03-07 09:42):
Then you can do better.

If you have **4 resistor footprints available**, the nicest way is to build the values from common precision parts so you hit both:

- **total ≈ 5.6 kΩ**
- **tap ratio ≈ 10:1**

## Exact target
For an exact 10:1 divider with total 5.6 kΩ:

- **Rtop = 5040 Ω**
- **Rbot = 560 Ω**

Because:
- 5040 + 560 = 5600 Ω
- 560 / 5600 = 0.1 exactly

## Easy 4-resistor implementation
A very clean way is:

### Top leg
- **4.99 kΩ + 49.9 Ω** in series = **5039.9 Ω**

### Bottom leg
- **510 Ω + 49.9 Ω** in series = **559.9 Ω**

So you get:

- **Rtop = 5039.9 Ω**
- **Rbot = 559.9 Ω**
- **Total = 5599.8 Ω**

That is essentially perfect.

## Why this is a nice solution
- Uses very standard precision values
- Gets you almost exact **5.6 kΩ**
- Gets you almost exact **10:1**
- Easy to source in 0.1% thin film if you want it tidy

## Result
Tap ratio:

\[
\frac{559.9}{5599.8} \approx 0.09999
\]

So at **28 V**:

\[
V_{tap} \approx 2.80 V
\]

which is exactly where you’d want it.

---

## Alternative slightly simpler set
If you want chunkier, more common values:

### Top
- **4.7 kΩ + 340 Ω = 5.04 kΩ**

### Bottom
- **510 Ω + 49.9 Ω = 559.9 Ω**

Total:
- **5599.9 Ω**

Also excellent, though **340 Ω** is a slightly less “default grab” value than 49.9 Ω.

---

## My pick
I’d use:

- **4.99 kΩ + 49.9 Ω**
- **510 Ω + 49.9 Ω**

That’s probably the cleanest 4-footprint solution.

## Layout note
Put the **bottom pair physically nearest ground**, and take the tap from the junction between the top and bottom networks, as usual. Keep the tap trace short if it goes into the buffer/FDA.

If you want, I can also suggest the best way to split those 4 parts physically so the midpoint tap is tidy and symmetrical on the PCB.

[M113] ME (2026-03-07 09:45):
No parallels?

[M114] AI (2026-03-07 09:45):
Yes — **series only**, no parallels needed.

For **exactly 10:1** and **exactly 5.6 kΩ total**, with **4 footprints**:

## Top leg
- **4.99 kΩ + 49.9 Ω** in series  
= **5039.9 Ω**

## Bottom leg
- **510 Ω + 49.9 Ω** in series  
= **559.9 Ω**

## Result
- Total = **5599.8 Ω**
- Ratio = **559.9 / 5599.8 ≈ 0.1**

So that is essentially perfect:
- **10:1**
- **5.6 kΩ total**
- **all series**
- **4 footprints**
- **no parallels**

At **28 V**, tap is about **2.80 V**.

If you want a slightly simpler BOM, I can also give you a **2-footprint** and **4-footprint** shortlist ranked by neatness.

[M115] ME (2026-03-09 00:49):
[image]
Is this sort of circuit right?
[attached file: IMG_9F8E3FF0-CDFC-4C06-B241-301F203C7A69.jpeg]

[M116] AI (2026-03-09 00:49):
Yes — **conceptually this is the right sort of circuit**.

You’ve now got the architecture we were talking about:

- **OS tapped and attenuated to about 10:1**
- fed into a **single-ended to differential driver**
- then exported as **OS+ / OS-**

That is the right overall idea for getting the waveform out.

A few specific comments from what I can see:

## What looks right
- **LMH6553** is the right class of part for this job.
- **Single-ended in, differential out** using a dedicated diff driver is sensible.
- **±5 V rails** are generous for a ~0 to 3 V input-derived signal.
- The **100 Ω series output resistors** on each leg are a good starting point for isolation / line driving.
- Local **10 µF + 100 nF decoupling** on both rails is right.

## The main thing to check
Your **input side grounding / reference arrangement**.

From the screenshot it looks like one side of the input is referenced to 0 V and the signal comes in single-ended into the other input path through **270 Ω**. That is a normal way to do it, **provided** the gain-setting around the LMH6553 matches the datasheet single-ended-to-differential configuration.

That is the key point: with this part, resistor symmetry matters. You want the input and feedback network to follow one of the recommended topologies fairly closely.

## Things I would review carefully

### 1) Output common-mode
Make sure the **VCM pin** is set to the common-mode you actually want on **OS+ / OS-**.

If the receiving side is just another analogue conditioning stage, this matters a lot.  
Do not leave VCM ambiguous.

### 2) Gain
Check what gain this resistor set is actually giving you.

With FDA-style parts, the gain is not just “input resistor equals feedback resistor, so gain 1” in the casual op-amp sense unless wired exactly as intended.  
You want to confirm:

- single-ended input amplitude in
- differential amplitude out
- common-mode centred correctly

### 3) Load / termination
Your two **100 Ω resistors** on each output leg may be fine as build-out resistors, but the final amplitude at the far end depends on:

- cable / pair impedance
- whether the receiver is terminated
- any additional loading on the conditioning board

So just check you’re not accidentally halving the signal more than expected.

### 4) Input loading on the 10:1 divider node
You want the LMH6553 input network to look **high enough impedance** that it does not noticeably disturb your split 5k6 divider ratio.

A 270 Ω input resistor straight onto the tap would be **far too heavy** if that is the direct load seen by the divider node.  
That is the biggest red flag from the screenshot.

Your divider tap is only coming from about:
- **5.6 k total**
- with a bottom leg around **560 Ω-ish**

So if the amplifier input network presents only a few hundred ohms effectively, it will badly corrupt the 10:1 scaling.

That means one of these must be true:
- there is a preceding buffer not shown, or
- these values are placeholder only, or
- this needs to be increased substantially

## Most important likely issue
### The **270 Ω input resistor values look too low** for a direct tap off the split 5k6 monitor node.

That would be my main challenge point.

If your OS monitor tap is supposed to remain a faithful scaled version of OS, the receive/transmit stage should ideally present **much lighter loading** to that node.

So the topology is right, but I would revisit:
- input resistor values
- whether you need a buffer first
- or whether the divider itself should be driving a higher-impedance stage

## Quick engineering judgement
### Right idea:
- yes

### Right exact resistor values:
- maybe not yet

### Biggest risk:
- **overloading the divider tap**

## What I’d do next
I’d check these three numbers explicitly:

1. **Tap source impedance** from your split 5k6 network  
2. **Effective input impedance** presented by this LMH6553 stage  
3. **Required differential output swing** at the far end

If you want, send a clearer crop or list the actual resistor values around the LMH6553 including feedback, and I’ll work out whether this stage is loading your divider too hard and what values to change.

[M117] ME (2026-03-09 00:52):
The circuit is the same as the output so far that monitors the conditioned os 

[M118] AI (2026-03-09 00:52):
That makes sense — and it changes the answer a bit.

If this stage is **already the proven output-monitor circuit used for the conditioned OS**, then:

## Yes, reusing the same topology is a strong move
Because it means:

- known behaviour
- known layout style
- known receiving-side expectations
- lower design risk
- easier review justification

So from a **system architecture** point of view, using the same LMH6553-style output stage for the new **raw/scaled OS monitor** is a very sensible choice.

## But one thing still matters
Even if the topology is reused, the **source impedance feeding it is now different**.

That is the real issue.

The existing conditioned OS monitor output probably came from a **low-impedance source**.

Your new raw OS monitor tap is coming from a **split 5k6 divider**. That is a much softer source.

So the question is not really:

> “Is this output circuit valid?”

It probably is.

The question is:

> “Can this same circuit be driven directly from the 10:1 divider without corrupting the divider?”

That is where I’d still be cautious.

## The likely concern
If the existing LMH6553 input network uses **270 Ω class resistors**, that is quite a heavy front end for a divider node derived from 5.6 k total.

So even though the topology is proven, the **input values may not be directly reusable** for this new source.

## In plain terms
You can split the judgement into two parts:

### Output-side concept
**Yes, right.**
Reusing the same driver/export arrangement is good.

### Input loading for this specific source
**Needs checking.**
Because the new source is weaker than the original conditioned OS source.

## What I would do
Keep the **same topology and part** if that helps commonality, but re-evaluate:

- input resistor values
- feedback resistor values
- gain
- source loading at the divider midpoint

You may find:
- the same circuit concept is right,
- but the resistor values should be scaled up.

## Quick sanity rule
If your divider is around **5.6 k total**, then the amplifier input should ideally look **much higher impedance** than that, otherwise your 10:1 ratio stops being 10:1.

So if the present conditioned-OS monitor network was happy with **270 Ω / 270 Ω**, I would not blindly reuse those values on the raw tap.

## Best interpretation
So my answer is:

**Yes, the topology is right if it is the same proven monitor-output stage.**  
**No, I would not assume the same resistor values are right without checking divider loading.**

That is probably the key thing not to miss.

If you want, I’ll work through the effective source impedance of your split 5k6 tap and tell you whether the LMH6553 network can be used directly or needs a lighter input network.

[M119] ME (2026-03-09 00:54):
Yes

[M120] AI (2026-03-09 00:54):
Right — let’s check the loading properly.

## 1) Source impedance of your split 5k6 tap

If you do the divider as:

- **Rtop = 5.04 kΩ**
- **Rbot = 560 Ω**

then the tap node Thévenin resistance is:

\[
R_{th} = R_{top} \parallel R_{bot}
\]

\[
R_{th} = \frac{5040 \times 560}{5040 + 560}
\approx 504 \Omega
\]

So your raw OS tap looks like about a **500 Ω source**.

That is not especially stiff.

---

## 2) What happens if you feed that into a 270 Ω input network

From your screenshot, the input resistor into the LMH6553 stage is about **270 Ω**.

If that 270 Ω is effectively the load seen by the tap, then the divider is being loaded by:

- source resistance: **~504 Ω**
- load: **270 Ω**

So the tap gets attenuated further by:

\[
\frac{270}{504+270} \approx 0.349
\]

So you would only get about **35%** of the expected tap voltage at the amplifier input.

### Example
Expected 10:1 tap from 28 V:

\[
V_{tap} \approx 2.8V
\]

Loaded by 270 Ω:

\[
V_{in} \approx 2.8 \times 0.349 \approx 0.98V
\]

So yes — that is a **big error**.

That means the existing conditioned-OS monitor resistor values are **too heavy** for direct use from the split 5k6 tap.

---

## 3) What you want instead

You want the receiver/driver input impedance to be **much higher than ~500 Ω**.

A good rule here is:
- at least **10× higher**
- ideally more

So aim for the input network to look like **5 kΩ minimum**, preferably **10 kΩ+**.

---

## 4) Practical implication for reusing the LMH6553 circuit

### Keep:
- the **same topology**
- the **same part**
- the **same general output arrangement**

### Change:
- **scale the resistor network up**

If the present circuit uses, say:
- **270 Ω input**
- **270 Ω feedback**

then try the same ratios but scaled up by 10:

- **2.7 kΩ**
- **2.7 kΩ**

or even:

- **5.6 kΩ**
- **5.6 kΩ**

depending on what the LMH6553 is happy with and how much bandwidth/noise penalty you can tolerate.

---

## 5) Quick check on loading with 2.7 kΩ

If the tap sees about **2.7 kΩ** load:

\[
\frac{2700}{2700+504} \approx 0.843
\]

So your 2.8 V tap becomes:

\[
2.8 \times 0.843 \approx 2.36V
\]

Still some error, but much better.

## 6) Quick check on loading with 5.6 kΩ

\[
\frac{5600}{5600+504} \approx 0.917
\]

So:

\[
2.8 \times 0.917 \approx 2.57V
\]

Better again.

---

## 7) Best architectural answer

If you want the **10:1 scaling to remain honest**, the best answers are:

### Best
Use a **high input impedance buffer** on the tap first.

### Next best
Keep the LMH6553 stage, but **increase the resistor values substantially**.

Since you want commonality with the existing monitor output circuit, the second option is probably the nicest compromise.

---

## 8) Bottom line

### Yes, the tap source impedance is about:
**500 Ω**

### Yes, the current 270 Ω-style network is too heavy:
it will significantly load and distort the divider ratio.

### So:
- **reuse the topology**
- **do not reuse the low resistor values unchanged**

I’d start by trying the same network scaled up to around **2.7 kΩ to 5.6 kΩ** and checking whether the LMH6553 still gives you the bandwidth and stability you want.

If you want, send the exact resistor designations around the LMH6553 and I’ll suggest a revised value set that preserves roughly the same gain but stops abusing the divider tap.

[M121] ME (2026-03-09 01:25):
[image]
[attached file: IMG_2043E1DB-131D-4324-939D-5F1F59F6DFA4.jpeg]

[M122] AI (2026-03-09 01:25):
Yes — this makes it clearer, and the main concern is still the same:

## The topology is fine
You’ve got:

- **5 k + 560 Ω** split load
- midpoint tap labelled **OS 10:1 (~3 V in)**
- **LMH6553** doing single-ended to differential
- exported as **OSn_P / OSn_N**

That overall concept is sound.

## The likely problem
Your **input network is still too heavy** for that divider tap.

### Why
Your split load is:

- top = **5 kΩ**
- bottom = **560 Ω**

So the tap source impedance is about:

\[
R_{th} = 5k \parallel 560 \approx 504\ \Omega
\]

But you are feeding that into:

- **R35 = 270 Ω**
- **R42 = 270 Ω**
- with the FDA network around it

So the tap is trying to drive a front end of the same order as its own source impedance. That means the “10:1” node is **not really 10:1 anymore once connected**.

## In plain language
The LMH6553 stage is loading your divider too much.

So:

- **circuit type** = right
- **present resistor scale** = probably wrong for this source

---

## What I’d change
Keep the same architecture, but scale the resistor network up.

### First-pass suggestion
Change these:

- **R35: 270 Ω → 2.7 kΩ**
- **R36: 270 Ω → 2.7 kΩ**
- **R40: 270 Ω → 2.7 kΩ**
- **R42: 270 Ω → 2.7 kΩ**

That preserves the same basic ratios/topology, but makes the loading about 10× lighter.

That is the first thing I would try.

### Why 2.7 k is better
With a ~500 Ω source impedance, a few-kΩ input network is much more reasonable than 270 Ω.

It still loads the node somewhat, but not brutally.

If you want to preserve the divider more faithfully, you could even consider **4.7 kΩ to 5.6 kΩ class values**, but **2.7 kΩ** is a good practical first step.

---

## Output side
The output resistors:

- **R37/R38**
- **R39/R41**

at **100 Ω**

look fine as build-out/isolation values for now.

No issue there from what I can see.

---

## Capacitor on OS_CLIP
That **10 nF to ground** on the clip/output side is something to think about.

At 500 kHz, 10 nF is quite a lot of capacitance if you care about waveform fidelity. It may be there intentionally for the existing conditioned monitor path, but for a “raw OS” style export it may start softening things.

So I would question whether **C35 = 10 nF** is wanted for this new path.

That is the second thing I’d review after the input resistor values.

---

## Bottom line
### Right:
- split 5 k / 560 Ω divider
- LMH6553 single-ended to differential concept
- diff export path

### Needs attention:
- **270 Ω network is too low for a ~500 Ω source**
- likely scale those resistor values up by around **10×**
- review whether the **10 nF** is too aggressive for the bandwidth you want

## My practical recommendation
Start with:

- **R35, R36, R40, R42 = 2.7 kΩ**
- leave output 100 Ω as-is
- strongly consider **removing or reducing C35** unless you intentionally want filtering

That would be my next iteration.

If you want, I can also infer the intended LMH6553 configuration from this exact wiring and suggest a cleaner value set rather than just “scale by 10.”

[M123] ME (2026-03-09 01:29):
That is clip voltage is used on the output. Shall I change it to a fixed value

[M124] AI (2026-03-09 01:30):
Yes — for this path, I would make **VCLAMP a fixed defined value**, unless you have a very deliberate reason to drive it dynamically from the legacy **OS_CLIP** net.

On the LMH6553, **VCM sets the output common-mode and must be driven from a low-impedance source and must not float**. The **VCLAMP pin sets the maximum output swing**, and TI states it should be kept in the range **VCM < VCLAMP < VCM + 2.0 V** for proper clamp operation. citeturn0search0

So the design question is really:

## If you want this new path to be a faithful monitor
Then **don’t let an old variable clip-control net dictate the output limit** unless that is part of the requirement.

Because if VCLAMP moves around, your monitor path can:
- change available output swing,
- clip earlier than expected,
- or behave differently between modes. TI explicitly describes VCLAMP as controlling the output limit, including fast recovery from overload. citeturn0search0

## What I would do
Use a **fixed VCLAMP** chosen to be:
- above your expected normal output peak,
- but still inside the allowed clamp range.

With your supplies at **±5 V**, the LMH6553 output itself cannot swing arbitrarily; TI notes output swing is also limited by the output stage, and with split ±5 V rails the outputs saturate before the clamp can act if the clamp is set beyond what the output stage can reach. citeturn0search0

## Practical recommendation
If this is just a transported OS monitor, I’d treat the clamp as a **safety ceiling**, not an active signal-control function.

A sensible approach is:

- set **VCM** to the output common-mode you want for the diff link,
- set **VCLAMP** to a **fixed DC value** that gives enough headroom for your expected monitor amplitude,
- leave it there.

## One important caveat
Do **not** confuse **VCM** and **VCLAMP**.

- **VCM** = where the outputs are centred
- **VCLAMP** = upper clamp reference for output swing

TI’s clamp description means the lower output limit is then forced by symmetry around VCM. citeturn0search0

## My judgement on your schematic
For this new monitor path, **yes, I would change the clip control to a fixed value** unless you specifically need mode-dependent limiting. That will make the monitor behaviour much more deterministic.

If you want, I can help you choose a concrete **VCM** and **VCLAMP** pair from your expected **OSn_P / OSn_N** swing.

[M125] ME (2026-03-09 01:32):
Yes

[M126] AI (2026-03-09 01:32):
Yes. For **this new raw/scaled OS monitor path**, I would make both pins **fixed**, not driven from the old clip net.

## Best default choice
With your **±5 V supplies**, the cleanest starting point is:

- **VCM = 0 V**
- **VCLAMP = +1.5 V** to **+2.0 V**

That is a good default because the LMH6553 requires **VCM** to be driven from a **low-impedance source** and not left floating, and it requires **VCLAMP** to satisfy:

\[
VCM < VCLAMP < VCM + 2.0\text{ V}
\]

For clamp operation, the maximum **single-ended** output swing is:

\[
2 \cdot (VCLAMP - VCM)
\]

and the maximum **differential** output swing is:

\[
4 \cdot (VCLAMP - VCM)
\]

So with **VCM = 0 V**:  
- **VCLAMP = 1.5 V** gives up to **6 Vpp differential**  
- **VCLAMP = 2.0 V** gives up to **8 Vpp differential** citeturn0search0

## What I’d actually use first
I’d start with:

- **VCM = 0 V**
- **VCLAMP = 1.5 V**

That gives you a symmetrical, ground-centered differential output with a decent amount of headroom, but it is a bit less aggressive than pushing straight to the absolute clamp limit. It is also a simpler, cleaner monitor signal for the far-end receiver or a scope. citeturn0search0

## When to use 2.0 V instead
Use:

- **VCM = 0 V**
- **VCLAMP = 2.0 V**

if you want the **maximum available unclipped differential swing** from the clamp relationship. On ±5 V rails, TI notes the output stage itself is still limited by how close it can swing to the rails, so there is no point setting the clamp beyond what the output stage can actually support. citeturn0search0

## Why I would not use the old OS_CLIP net
Because on this path you want a **deterministic monitor**, not a mode-dependent limiter. If VCLAMP moves with some legacy function, the exported waveform can change limit point between modes and become harder to interpret. TI describes VCLAMP specifically as the control for maximum output swing and fast overload recovery. citeturn0search0

## Practical implementation
- Tie **VCM** to a solid **0 V reference** and bypass it with **100 nF** close to the pin. TI explicitly says VCM should be driven from a low-impedance source and bypassed, and must not float. citeturn0search0
- Generate **VCLAMP** as a fixed DC value, for example from a divider/reference/buffer.
- Do **not** leave either pin floating.

## My recommendation
For first spin / first bodge try:

- **VCM = 0 V**
- **VCLAMP = 1.5 V**

Then, if you find the monitor path is too constrained, move to:

- **VCM = 0 V**
- **VCLAMP = 2.0 V**

That is the pair I’d choose for a clean, general-purpose raw OS monitor on ±5 V rails.

If you want, next I’ll turn that into an actual little resistor-divider network from +5 V for the **1.5 V** or **2.0 V** clamp node.

[M127] ME (2026-03-09 01:36):
Explain about bypass capacitor on vcm 

[M128] AI (2026-03-09 01:36):
The **VCM bypass capacitor** is there to keep the output common-mode reference **clean and stiff**.

For the LMH6553, **VCM directly sets the outputs’ common-mode at 1 V/V**, so any noise or ripple on VCM gets copied onto both outputs. TI explicitly says the **VCM pin should be driven by a low-impedance source, bypassed to ground with a 0.1 µF ceramic capacitor, and must not be left floating**. It also notes that unwanted coupling into **VCM** can degrade dynamic range, CMRR, balance, and distortion. citeturn0search0

## What it is doing in practice
Think of VCM as the **reference pedestal** for the differential pair.

If you set:
- **VCM = 0 V**

then the two outputs swing equally around 0 V.

If that VCM node is noisy, high-impedance, or picked up by nearby switching/digital activity, the outputs inherit that movement. The bypass capacitor gives the pin a **low AC impedance to ground**, so high-frequency rubbish is shunted away instead of modulating the output common-mode. citeturn0search0

## Why it matters more here
You’re trying to export a fairly faithful analogue monitor. So you do **not** want extra common-mode wobble added by:
- supply noise,
- clip-control noise,
- long traces,
- or a resistive divider feeding VCM with no local decoupling.

That would not necessarily destroy the differential signal, but it can:
- worsen balance,
- reduce CMRR,
- increase distortion,
- and make probing messier. TI calls these effects out directly in its bypassing guidance. citeturn0search0

## What value to use
For this part, the standard answer is:

- **0.1 µF ceramic** from **VCM to ground**
- placed **very close to the pin**

TI says 0.1 µF on VCM, and elsewhere in the layout/bypass section also shows a **small capacitor on VCM and VCLAMP to ground** because both are high-impedance nodes that can couple external noise into the amplifier. citeturn0search0

## If VCM is generated from a divider
If you create VCM from resistors, the capacitor is even more important.

Why:
- the divider sets the **DC value**
- the capacitor makes it **quiet at AC**

Without the capacitor, the divider may be the right voltage on a meter, but still be too soft/noisy for a fast FDA.

## Practical layout advice
Do this:
- **VCM pin → short trace → 100 nF ceramic → local analogue ground**

Avoid:
- long VCM traces
- sharing that node with noisy logic
- relying on a remote reference without local decoupling

## Bottom line
The VCM bypass capacitor is there to make the **output-centre reference quiet and low-impedance**, so the LMH6553 outputs stay balanced and clean. For your circuit, **100 nF ceramic close to the VCM pin** is the right move. citeturn0search0

[M129] ME (2026-03-09 01:40):
[image]
Like that?
[attached file: IMG_1629CAFE-758B-4033-A3BA-88E38EDC5576.jpeg]

[M130] AI (2026-03-09 01:40):
Yes — **that’s the right idea for the VCM bypass**.

What you’ve now got is:

- **pin 5 (VCM)**  
- a **100 nF cap to 0 V**  
- placed locally

That is exactly the sort of thing you want. TI’s guidance is that **VCM should be driven from a low-impedance source, bypassed with 0.1 µF to ground, and not left floating**. citeturn0search0

A couple of points though:

## What looks right
- **C36 on VCM to 0 V**: yes, good.
- Keeping it **physically close to pin 5**: important.
- Your resistor increase to **2k2** is also a move in the right direction for source loading.

## What I’d still adjust
### 1) Do not leave VCM just hanging off a cap
The cap is only the **AC bypass**.  
VCM still needs a **defined DC source**.

So pin 5 should be:
- tied to a defined **0 V reference** if you want outputs centred on 0 V, or
- tied to some other fixed reference if you want a different output common-mode,

**and** have the 100 nF cap to ground.

So the node should be:

**VCM pin → solid 0 V reference + local 100 nF to 0 V**

not just:
**VCM pin → capacitor only**

### 2) Check VCLAMP separately
You’ve also got **C35 = 10 nF** on the **OS_CLIP / VCLAMP** node. That is fine **if** VCLAMP is now going to be a fixed quiet DC node. TI also recommends bypassing VCLAMP because it is a sensitive control node. citeturn0search0

But if **OS_CLIP** is still some legacy moving signal, then that cap is no longer just “bypass” — it becomes part of a dynamic filter on the clamp control.

For this monitor path, I’d prefer:
- **fixed VCLAMP**
- with a local small bypass cap

## Practical best version
For a clean first pass, I’d do:

- **VCM = hard tied to 0 V**
- **100 nF from VCM to 0 V**, close to the pin
- **VCLAMP = fixed DC value**
- small cap on VCLAMP to 0 V if desired

## Bottom line
**Yes — that VCM capacitor placement is right.**  
Just make sure **pin 5 also has a proper DC reference**, not only the capacitor. The cap stabilises the node; it does not define it.

[M131] ME (2026-03-09 01:45):
[image]
Like that 
[attached file: IMG_CA8790F3-F2BE-4714-9045-DD6D2D18D258.jpeg]

[M132] AI (2026-03-09 01:45):
Yes — **that is much closer**.

You’ve now done the two important things:

- increased the **FDA resistor network** from 270 Ω to **2k7**
- given **VCM** a **100 nF local bypass**

And you’ve added a **fixed divider for VCLAMP**, which is the right direction.

## What looks right
- **R35/R36/R40/R42 at 2k7**: much more sensible for the ~500 Ω source.
- **VCM pin 5 with 100 nF to 0 V close by**: good.
- **VCLAMP pin 7 driven from a resistor divider** instead of the old moving clip net: good.
- **100 Ω output build-out** still looks fine.

## The one thing to check now
Your **VCLAMP divider value**.

From the picture it looks like:

- top resistor = **2k7** to **+5 V**
- bottom resistor = **1k5** to the node feeding **pin 7**

If that bottom resistor really goes to **0 V**, then the clamp node is:

\[
V_{CLAMP} = 5 \times \frac{1.5}{2.7+1.5} \approx 1.79V
\]

That is a **good value**.

So if that lower **1k5** really returns to **ground**, then yes, that part is sensible.

## But from the drawing…
It is not fully obvious from the photo whether the **1k5 lower end** is actually tied to **0 V** or whether it is floating / incomplete.

### It must be:
- **+5 V**
- through **2k7**
- to **VCLAMP node**
- then through **1k5**
- to **0 V**

If the bottom leg is not grounded, the divider does nothing useful.

## VCM node
From the screenshot, **pin 5** appears to have:
- a capacitor to ground

That is correct for bypass.

But if you want **VCM = 0 V**, it also needs to be **electrically tied to 0 V**, not just via the capacitor.

If pin 5 is already on a net that is grounded, fine.  
If not, add a direct connection.

## My judgement
### If:
- **pin 5 is actually tied to 0 V**
- and the **1k5 lower resistor goes to 0 V**

then **yes, this is now basically the right arrangement**.

## Small recommendation
I’d label the clamp node with the intended voltage, something like:
- **VCLAMP ≈ 1.8 V**

That makes review easier later.

## Bottom line
**Yes — like that is right, provided the divider bottom really goes to ground and VCM is truly referenced to ground, not only capacitively bypassed.**

[M133] ME (2026-03-09 01:47):
Draw the vcm config 

[M134] AI (2026-03-09 01:47):
Yes — like this.

For **VCM = 0 V**, the config is just a **hard DC tie to 0 V** plus the **local 100 nF bypass** right at pin 5. TI says the VCM pin sets the output common-mode, should be driven from a low-impedance source, bypassed with 0.1 µF to ground, and must not be left floating. citeturn1search0

```text
                 LMH6553

            pin 5 = VCM
                  |
                  +---- short direct connection to 0V
                  |
                 === 100nF
                  |
                 0V
```

On your schematic, that means:

- **pin 5 goes directly to the 0 V net**
- **a 100 nF ceramic goes from pin 5 to 0 V**
- keep that capacitor **physically very close** to pin 5

If you want the same thing drawn a bit more “schematic-like”:

```text
                 0V
                  |
                  +---------------------> VCM pin 5
                  |
                 Cx
                100n
                  |
                 0V
```

So electrically it is just:
- **VCM node = 0 V**
- with a **local decoupling capacitor** from that node to 0 V

It can feel odd because both ends appear to go to ground, but the point is that the capacitor is a **local HF bypass** at the pin, while the direct net tie is the **DC reference**.

For your circuit, I would make it exactly that simple.

[M135] ME (2026-03-09 01:48):
[image]
[attached file: IMG_6C9D7EC0-66A0-4D3D-B776-CD060CC5A4F1.jpeg]

[M136] AI (2026-03-09 01:48):
Almost — but there’s one mistake there.

You’ve tied **VCM (pin 5)** to the **PAD (pin 9)**.

That is **not** what you want.

## What it should be
- **Pin 5 (VCM)** → directly to **0V**
- **100 nF** from **pin 5 to 0V**, close to the pin
- **Pin 9 (PAD)** → separately to **0V / ground copper** as per package grounding
- **Do not join pin 5 to pin 9 as the signal route**

## So the correction is
Delete the vertical connection between:
- **pin 5**
- **pin 9**

They may both end up at ground, but they should not be shown as the same local node in that way.

## Draw it like this

```text
pin 5 (VCM) ----+---- 0V
                |
               100n
                |
               0V

pin 9 (PAD) -------- 0V
```

Or schematically:

```text
            LMH6553

pin 5 VCM ----------- 0V
      |
     100n
      |
     0V

pin 9 PAD ----------- 0V
```

## Why
- **VCM** is a functional control pin that needs a **solid DC reference** and **local AC bypass**
- **PAD** is the exposed thermal/electrical pad and should be grounded for the package/layout
- They are both grounded, but you do **not** want to imply the pad is the routing node for VCM

## Practical Altium version
Do this cleanly:
- wire **pin 5** to a **0V power port**
- place **100 nF from pin 5 to 0V**
- wire **pin 9** to its own **0V power port**

That is the cleanest schematic representation.

So: **good intent, but remove the direct pin 5 to pin 9 join.**

[M137] ME (2026-03-09 01:50):
[image]
It’s the same bet.
But ok, drawn it separate 
[attached file: IMG_EDC2D3AA-0DBB-4640-993F-3F232F3D1F1F.jpeg]

[M138] AI (2026-03-09 01:50):
Yes — **that’s now drawn properly**.

Electrically it is still the same net, as you say, but **schematically separating it is the cleaner way**:

- **pin 5 (VCM)** shown going to **0V**
- **100 nF from VCM to 0V**
- **pin 9 (PAD)** separately shown to **0V**

That’s the right presentation.

## Why this is better
It makes it obvious that:

- **VCM** is a functional control/reference pin
- **PAD** is the exposed pad / ground connection
- both go to **0V**, but for different reasons

So yes — **keep it like this**.

## One minor tidy-up
The text **“C CLOSE TO PIN”** is fine as a reminder, but if you want it cleaner, make it something like:

- **VCM BYPASS 100N CLOSE TO PIN 5**

That makes the intent explicit when someone else reads it later.

## Quick check of where you are now
At this point you’ve got the important things in place:

- divider tap for OS monitor
- FDA input resistors increased
- fixed **VCLAMP**
- proper **VCM grounding + bypass**
- separate **PAD to 0V**

So this part now looks sensible.

The next thing I’d review is just whether the **VCLAMP divider** is exactly giving the voltage you want.

[M139] ME (2026-03-09 01:51):
Coagulate best values for this 

[M140] AI (2026-03-09 01:51):
Yes — here’s a clean consolidated set of **best-value starting points** for this circuit as it stands.

## 1) OS 10:1 split load
For the load branch that replaces the 5k6 and gives you the tap:

**Best exact-ish 4-footprint solution**
- **Top leg:** 4.99 kΩ + 49.9 Ω = **5039.9 Ω**
- **Bottom leg:** 510 Ω + 49.9 Ω = **559.9 Ω**

Result:
- total = **5599.8 Ω**
- ratio = **559.9 / 5599.8 ≈ 0.1**
- at **28 V OS** → tap ≈ **2.80 V**

That is the neatest set.

### Simpler 2-part version
- **5.11 kΩ**
- **562 Ω**

Result:
- total = **5672 Ω**
- tap ratio ≈ **0.099**
- at 28 V → **2.77 V**

Good if you want less clutter.

---

## 2) LMH6553 input / feedback network
Your original **270 Ω** values were too heavy.

### Best starting point
Use:
- **R35 = 2.7 kΩ**
- **R36 = 2.7 kΩ**
- **R40 = 2.7 kΩ**
- **R42 = 2.7 kΩ**

That preserves the topology and makes the loading much more sensible.

### If you want even lighter loading
You could try:
- **4.7 kΩ** for the same four parts

But I think **2.7 kΩ** is the best first-pass compromise.

---

## 3) Output resistors
Keep these as:

- **R37 = 100 Ω**
- **R38 = 100 Ω**
- **R39 = 100 Ω**
- **R41 = 100 Ω**

That looks fine.

---

## 4) VCM configuration
For this monitor path:

- **VCM = 0 V**
- **100 nF from VCM pin to 0 V**, close to pin 5

No divider needed. Just hard reference plus local bypass.

---

## 5) VCLAMP configuration
Use a fixed divider from **+5 V** to ground.

### Best practical target
Aim for about **1.8 V**.

Use:
- **Top resistor = 2.7 kΩ to +5 V**
- **Bottom resistor = 1.5 kΩ to 0 V**

That gives:

\[
V_{CLAMP} = 5 \times \frac{1.5}{2.7+1.5} \approx 1.79V
\]

That is a good value.

### Optional bypass
- **100 nF from VCLAMP to 0 V**, close to pin 7

I’d do that.

---

## 6) Supply decoupling
Keep:
- **100 nF + 10 µF** on **+5 V**
- **100 nF + 10 µF** on **-5 V**

Close to the part.

---

## 7) Capacitor on OS_CLIP / output node
For the new “raw OS monitor” path:

- **remove C35 initially** or fit **DNI**

That **10 nF** is likely too aggressive if you want to preserve the waveform.

Only add it back later if testing shows you actually want some filtering.

---

# Final recommended value set

## Divider
- 4.99 kΩ
- 49.9 Ω
- 510 Ω
- 49.9 Ω

## LMH6553 resistors
- R35 = 2.7 kΩ
- R36 = 2.7 kΩ
- R40 = 2.7 kΩ
- R42 = 2.7 kΩ

## Output resistors
- R37 = 100 Ω
- R38 = 100 Ω
- R39 = 100 Ω
- R41 = 100 Ω

## VCM
- direct to 0 V
- 100 nF to 0 V

## VCLAMP
- 2.7 kΩ to +5 V
- 1.5 kΩ to 0 V
- optional 100 nF to 0 V

## Capacitors
- C35: DNI initially
- rail decouplers: keep as shown

If you want, I can turn that into a one-shot BOM-style list with exact resistor tolerances as well.

[M141] ME (2026-03-09 01:54):
So vclamp wants to be 1.5 to limit either direction of the max swing 2.8v based on 28v divider input?

[M142] AI (2026-03-09 01:54):
Yes — **that VCM arrangement is now correct**.

You now have:

- **Pin 5 (VCM)** tied directly to **0 V**
- **100 nF from VCM to 0 V**
- **Pin 9 (PAD)** separately to **0 V**

That is exactly the right intent.

A couple of refinements:

## 1) This is the right electrical arrangement
TI says **VCM should be driven from a low-impedance source, bypassed to ground, and not left floating**. It also notes **VCM and VCLAMP are high-impedance nodes**, so local caps help stop noise coupling in. citeturn0search0

So your current VCM setup is good.

## 2) Make the cap physically close to pin 5
Your note “C CLOSE TO PIN” is right.  
That matters more in layout than schematic, but it’s worth keeping on the drawing.

## 3) Value choice
**100 nF** is fine as the default. TI examples show a small cap on VCM and VCLAMP to ground for split-supply bypassing. citeturn0search0

## 4) Same idea applies to VCLAMP
Your fixed VCLAMP divider is sensible, and I’d also give **pin 7** a small local bypass cap to ground.

---

## On your VCLAMP question
You asked whether **1.5 V** is the right number to limit the swing based on the **~2.8 V max input** from the 28 V / 10:1 divider.

The key formula from TI is:

- **max single-ended output swing** = \(2 \cdot (VCLAMP - VCM)\)
- **max differential output swing** = \(4 \cdot (VCLAMP - VCM)\) citeturn0search0

With your current plan:

- **VCM = 0 V**

So:

- if **VCLAMP = 1.5 V**, max **single-ended** output swing is **3.0 Vpp**
- max **differential** output swing is **6.0 Vpp** citeturn0search0

That means **1.5 V does not clip a 2.8 V peak input directly**. It sets the **output swing limit**, not the input limit.

So whether **1.5 V** is right depends on the **closed-loop gain from your 0–2.8 V tap into the FDA outputs**.

### Practical read:
- If your stage is roughly **unity-ish** in the way you intend to use it, **1.5 V VCLAMP is a sensible conservative starting point**.
- If you want more output headroom, use about **1.8 V**.
- If you want the maximum clamp range allowed by the clamp rule, **2.0 V** is the upper practical target from the formula. citeturn0search0

## My recommendation
For first pass:

- **VCM = 0 V**
- **VCLAMP ≈ 1.8 V**
- **100 nF on both VCM and VCLAMP**

That gives a bit more headroom than 1.5 V while still keeping the monitor path controlled.

If you want, I’ll map your exact resistor network to the LMH6553 gain and tell you whether **1.5 V**, **1.8 V**, or **2.0 V** is the best clamp point.

[M143] ME (2026-03-09 01:56):
All 2k7, believe that’s x1

[M144] AI (2026-03-09 01:57):
Yes — if **R35 = R36 = R40 = R42 = 2k7**, then **the stage is still unity-gain in the same way the 270 Ω version was**, because the gain is set by the **ratios**, not the absolute resistor size. Scaling all four together mainly changes loading/noise/stability tradeoffs, not the nominal gain. citeturn0search0

On **VCLAMP**: not quite the way you phrased it.

## What VCLAMP actually limits
With the LMH6553:

- **VCM** sets the output centre point
- **VCLAMP** sets the **maximum output swing around that centre**
- the clamp acts on the **output**, not directly on the input divider voltage. citeturn0search0

So if you have:

- **VCM = 0 V**
- **VCLAMP = 1.5 V**

then the clamp allows roughly:

- **single-ended output swing** up to about **±1.5 V peak** around 0 V
- which is about **3.0 Vpp per leg**
- and about **6.0 Vpp differential** overall. citeturn0search0

## Relating that to your 2.8 V tap
Your divider gives about:

- **28 V in**
- **2.8 V max at the tap**

If the FDA is configured as **x1 single-ended in to differential out**, then each output leg is not simply “2.8 V single-ended copied straight through.” The stage is creating a **balanced differential representation** around **VCM**. So the thing to compare against VCLAMP is the **resulting output-leg swing**, not the raw 2.8 V tap by itself. citeturn0search0

## Practical answer
So:

- **VCLAMP = 1.5 V** is a **reasonable conservative clamp**
- it does **not** mean “limit either direction to the 2.8 V input”
- it means “don’t let either output leg swing beyond about ±1.5 V around VCM”

That is often a good place to start.

## What I’d choose
For your case, I’d set:

- **VCM = 0 V**
- **VCLAMP = 1.5 V** to start

That gives you a controlled output swing and should still be enough for a useful exported monitor signal.

If you later find the far-end signal is smaller than you’d like, move to:

- **VCLAMP ≈ 1.8 V**

That gives a bit more headroom without just opening it up fully.

[M145] ME (2026-03-19 19:35):
Would the differential measurement potentially be a better single than running it around 1m, maybe more single ended 50ohm 

[M146] AI (2026-03-19 19:35):
Yes — over **~1 m or more**, **differential is the better way** in most cases.

For this signal, I would strongly prefer:

- **buffer it**
- **send it as a differential pair**
- recover it at the far end

rather than trying to run the monitor as a **single-ended 50 Ω** line.

## Why differential is better here
You’re carrying a:

- moderate-bandwidth analogue monitor
- through a noisy system
- from inside a chamber / electronics environment
- over a modest but non-trivial distance

Differential buys you:

- much better **noise immunity**
- less sensitivity to ground offsets
- less dependence on a perfect return path
- cleaner probing at the far end
- less risk of the cable itself becoming part of the signal problem

That is exactly what you want.

## Why single-ended 50 Ω is less attractive
A true **50 Ω single-ended** approach only really works nicely if you commit to proper line-driving practice:

- low source impedance
- proper 50 Ω cable
- proper 50 Ω termination at the far end
- enough drive current
- acceptance that the load is now effectively 50 Ω

That can be fine, but for your case it is a bit brute-force and not especially elegant.

### The main downside
A **50 Ω terminated single-ended line** is a **heavy load**.

So unless the buffer/driver is explicitly there to drive it, you end up:

- needing more signal current
- increasing distortion risk
- wasting swing
- making the signal chain more dependent on termination correctness

## Differential over 1 m
At **500 kHz-ish**, 1 m is not RF-black-magic territory, but it is absolutely long enough for:

- pickup
- ground rubbish
- coupling from other harness content

to matter.

So even though 1 m sounds short in human terms, it is plenty long enough for **differential to be worth it**.

## Best practical answer
For your setup, I’d rank the options:

### Best
**Differential buffered transport**
- send **OS+ / OS-**
- use twisted pair
- recover single-ended later if needed

### Second best
**Single-ended buffered transport with local ground reference**
- workable if the environment is clean
- but more fragile

### Least attractive
**Single-ended 50 Ω transport**
- only worth it if you really want a coax-style measurement link and are happy with the loading/termination discipline

## One nuance
If the only goal was:

- “bring a signal to a scope on a bench over a known coax”

then single-ended 50 Ω can be attractive.

But your case is more like:

- in-system analogue monitor
- inside hardware
- likely electrically messy
- likely shared harness environment

That pushes it firmly toward **differential**.

## Bottom line
**Yes — differential is potentially much better than running it 1 m+ as single-ended 50 Ω.**  
For your application, I’d stay with the **differential transport** plan.

[M147] ME (2026-03-19 19:39):
Also, I have a spare gate from an lvds transceiver. I’m using the input as the clamp trigger. The is circuit also has a clip voltage setting. I’m wondering what could use that spare lvds line driver for from single ended. Least I’ll do is place a pad and route it out of the chamber. Just in case something is of interest and it can be used. I was thinking of maybe it looking at the drain current that feeds into the follower. Using that max chip to single end. The single to differential to the system and just stay there if needed.

[M148] AI (2026-03-19 19:39):
Yes — that’s a good instinct. A **spare LVDS channel** is worth treating as a **strategic observation lane**, especially since getting signals out of the chamber later is expensive.

And your thought about using it for the **drain/follower supply current** is one of the better uses.

## Best way to think about the spare LVDS path
Don’t burn it on something trivial. Use it for a signal that is:

- hard to access later
- diagnostically rich
- likely to settle future arguments

That usually means one of these three:

### 1) **Follower drain / ID current monitor** — strongest candidate
This is the best fit from what you described.

Why it’s valuable:
- separates **raw OS voltage behaviour** from **what the follower stage is doing**
- lets you see whether odd behaviour is due to the CCD node or the follower loading/biasing
- complements your raw OS monitor very well
- probably only needs **moderate analogue bandwidth**, not insane fidelity

Architecture:
- small shunt in the **ID / drain / collector feed**
- current-sense amplifier
- then into your **single-ended to differential** export chain
- route onto the spare LVDS/diff path to outside the chamber

That gives you:
- **raw OS voltage monitor**
- **follower current monitor**

Those two together tell a very good story.

## 2) **Raw clip / clamp trigger visibility**
Since you’re already using an LVDS receiver input as the clamp trigger, another valuable use is to expose:

- the actual clamp trigger timing
- or the local analogue clip state / comparator result

Useful because it lets you correlate:
- OS waveform
- follower current
- clamp timing

But this is more digital/event visibility than analogue observability.

## 3) **Pad-only / future utility line**
Also worth doing even if you choose one active use now.

Meaning:
- leave a pad / resistor option / jumper point
- route the spare line to an accessible analogue node region
- maybe with DNI parts

That way you can later hijack it for:
- OD monitor
- another bias rail monitor
- comparator output
- spare chamber diagnostic

That’s smart design hygiene.

---

# On your specific idea: drain current via MAX chip
Yes — that is a **very sensible use**.

Especially because:

- the **drain / follower current** is not the same as raw OS current
- it may be easier to measure cleanly
- it gives you the “second stage” observability you were talking about earlier

## Why it’s a good pairing
You’d then have:

### Channel A
**Scaled raw OS voltage waveform**

### Channel B
**Follower drain / ID current**

That gives you:
- node voltage
- stage current

That is exactly the kind of pair that helps debug:
- clipping
- bias collapse
- unexpected loading
- relay-state behaviour
- noise-cal mode oddness

---

# One caution
You said:

> using that max chip to single end. Then single to differential

That is fine, but only if you actually need the **MAX current-sense chip**.

## Use the MAX chip if:
- you want a **ground-referenced current monitor output**
- you want some gain
- the common-mode conditions suit it
- bandwidth is adequate for what you care about

## Don’t use it if:
- you really want very high-fidelity current waveform export
- or the chip bandwidth/behaviour becomes the limiting factor

For drain current, though, I think the MAX approach is pretty reasonable.

---

# Best architecture for the spare lane
I’d make it flexible.

## Recommended structure
- **Shunt in drain/ID feed**
- footprints/options for:
  - **MAX current-sense amp**
  - output to **single-ended to differential driver**
- route to spare diff lane
- also include:
  - local test pad
  - DNI link / 0R option
  - maybe raw shunt pads too if practical

That way:
- you can populate the full monitor path
- or you can bodge/repurpose later if needed

---

# What I would actually prioritize
If you only get one spare exported analogue diagnostic, I’d rank it:

## 1. Follower drain current
Best overall value.

## 2. Spare generic analogue export pad with routing option
Very smart fallback.

## 3. Another raw voltage monitor
Less useful, since you already have raw OS coming out.

---

# Practical recommendation
Yes — I would absolutely consider using the spare LVDS/diff lane for a **drain current monitor**.

That is probably the **best missed-opportunity catch** in what you’ve described.

And even if you do not fully populate it now, at minimum I would:
- place the shunt location
- place the current-sense amp footprint
- place the single-ended to diff driver option
- route it to the spare lane
- leave pads/links so it can be activated later

That gives you real future-proofing instead of just a dead spare.

If you want, I’ll sketch the cleanest signal chain for that spare lane as a small block diagram with where the shunt and MAX part should sit.

[M149] ME (2026-03-19 19:45):
There’s a spare relay gate also. This could be sweet. The relay switches between os onto follower and noise cal. So when the os is being selected the second pole could be present g the drain current. That was both could be observed at the same time. When it’s looking at noise….???

[M150] AI (2026-03-19 19:45):
Yes — that **is** sweet. That’s a genuinely useful use of the spare relay pole.

## The elegant idea
Use the spare relay pole so the **drain-current monitor is only connected when OS is selected onto the follower**.

Then in that mode you get, at the same time:

- **raw/scaled OS voltage waveform**
- **follower drain current**

That is a very strong paired measurement.

It lets you see:
- what the OS node is doing
- what current the follower stage is drawing because of it

That’s much more valuable than either signal alone.

## Why it’s good
When OS is selected:
- the follower is actually responding to OS
- so drain current is meaningful as the “second-stage” response
- and your raw OS monitor gives the “first-stage” input

So you get direct correlation:
- OS voltage rises/dips
- follower drain current reacts

That is a proper observability win.

---

## What to do in noise-cal mode
That’s the interesting part.

In noise-cal mode the follower input is switched to **OD** instead of **OS**, so you have a few choices for what the spare pole should do.

### Best option
Use the spare pole to switch the same current-monitor channel to observe **the follower drain current in noise-cal mode as well**.

So the current monitor always follows the follower’s operating context:

- **OS mode** → monitor follower drain current while driven by OS
- **Noise-cal mode** → monitor follower drain current while driven by OD

That is probably the best overall use.

Because then the exported current channel becomes:

> **current drawn by the follower stage, whatever source is currently feeding it**

That is a clean concept.

And alongside that, your separate raw OS voltage monitor still tells you what OS itself is doing.

## Why that’s useful
Then you can compare:

### In OS mode
- raw OS voltage
- follower drain current due to OS drive

### In noise-cal mode
- raw OS voltage may still be visible as a bias/reference
- follower drain current now reflects OD-driven behaviour

That gives you mode-dependent insight without wasting the spare pole.

---

## Alternative option
If in noise-cal mode you don’t care about drain current, then use the spare pole to put the current monitor into a **parked / quiet state**.

For example:
- disconnect the current-monitor output
- or connect the monitor input to a known dummy/reference condition

That avoids ambiguity.

But I think that’s less interesting than continuing to observe follower drain current in both modes.

---

## Best conceptual use of the spare relay pole
I’d describe it like this:

> The spare relay pole is used to maintain contextual observability of the follower stage. In OS mode, the exported analogue monitor represents follower drain current under OS drive. In noise-cal mode, the same monitor represents follower drain current under OD drive.

That is a very defensible architecture.

---

## Important implementation thought
Be careful what exactly you switch.

### Best thing to switch
Switch the **selection of which operating state the monitor refers to**, not the raw shunt itself if you can avoid it.

In practice:
- keep the **drain-current shunt permanently in series**
- keep the current-sense amplifier permanently connected if possible
- use the relay pole only to define when/where the resulting signal is routed or enabled

That is cleaner than physically switching the shunt path.

### Why
You do not want relay contacts sitting in the actual current-sense path unless necessary, because that can:
- add contact resistance uncertainty
- inject noise
- complicate calibration

So ideally:
- **shunt always there**
- **MAX/current-sense stage always there**
- relay pole used for **routing/enable/context**

---

## Very nice combined channel concept
You could end up with:

### Channel 1
**Raw OS voltage monitor**

### Channel 2
**Follower drain current monitor**

And the relay state tells you whether Channel 2 corresponds to:
- OS-driven follower operation
- or OD/noise-cal-driven follower operation

That is excellent.

---

## If you want something cleverer in noise-cal mode
A slightly fancier option is:

- in **OS mode**: export **follower drain current**
- in **noise-cal mode**: export **something else useful**, such as:
  - OD-related follower current
  - clamp trigger state
  - comparator output
  - spare analogue node

But unless there’s a very strong alternate need, I’d keep it simple and just let it remain the follower current monitor in both modes.

---

## My recommendation
Use the spare relay pole so that:

- **OS selected** → drain-current monitor is active and interpreted as OS-driven follower current
- **noise-cal selected** → drain-current monitor remains active and interpreted as OD-driven follower current

That gives you simultaneous visibility of:
- **raw OS voltage**
- **stage current response**

which is probably the best use of the spare resources you’ve got.

If you want, I’ll sketch a neat relay truth table for:
**OS mode / noise-cal mode / exported current channel meaning**.

[M151] ME (2026-03-19 19:50):
The other thing is.
There are two os. And i only really have 2 lanes out, not the required 4

[M152] AI (2026-03-19 19:50):
Then the real design problem is now **channel economy**.

You’ve got:

- **2 OS nodes**
- ideally want for each:
  - raw OS voltage
  - follower/drain current
- but only **2 export lanes total**

So you can’t export all four simultaneously.

## Best framing
You need to decide which of these matters more:

- **simultaneous completeness**
- or **practical observability with mode/context**

With only 2 lanes, the best use is usually:

## Best overall allocation
### Lane 1:
**Raw OS monitor**

### Lane 2:
**Follower drain current monitor**

But then use switching / relay context so that each lane corresponds to the **currently selected OS path**.

That gives you:
- one voltage view
- one current view
- for the active channel

That is usually the smartest compromise.

---

## Why this is the sweet spot
If the system only actively presents one OS path into the follower context at a time, then exporting both OS1 and OS2 continuously is often wasteful.

What you really want is:
- the **active OS waveform**
- and the **current response of the active follower path**

That tells the story in real time.

So instead of thinking:
- “I need 4 outputs”

think:
- “I need 2 correlated outputs for whichever path is active”

---

## Good architecture
Use the spare relay pole / selection logic so that:

### Lane 1 switches between:
- **OS1 scaled monitor**
- **OS2 scaled monitor**

### Lane 2 switches between:
- **follower current for path 1**
- **follower current for path 2**

Then the two exported lanes always stay paired.

That is much more useful than, say:
- exporting OS1 and OS2 only,
- or exporting two currents only.

---

## Best use cases
### In OS1 mode
- Lane 1 = **OS1 voltage**
- Lane 2 = **OS1 follower current**

### In OS2 mode
- Lane 1 = **OS2 voltage**
- Lane 2 = **OS2 follower current**

That is a really clean architecture.

---

## If the two OS are active simultaneously
Then you have a genuine multiplexing problem.

In that case you’ve got three realistic options:

### Option 1 — choose one “debug-selected” OS at a time
Best simple answer.

Add links / relay logic / control so you pick:
- monitor channel A set = OS1
or
- monitor channel A set = OS2

This is probably good enough unless both must be observed at once.

### Option 2 — export both OS voltages only
If voltage visibility is the highest priority:
- Lane 1 = OS1 voltage
- Lane 2 = OS2 voltage

Then current is lost.

### Option 3 — export both currents only
Less likely the best choice.

---

## What I would recommend
### If only one OS path is functionally relevant at a time:
Use the 2 lanes as a **context-switched pair**:
- voltage of selected OS
- current of selected OS follower

That is the strongest answer.

### If both OS are genuinely important at once:
Then I would prioritize:
- **OS1 voltage**
- **OS2 voltage**

because those are the harder “raw” signals to reconstruct later, and current can often be inferred or added later more easily.

But from your earlier discussion, it sounds like the real value is in **voltage + current correlation**, which points back to the switched-pair approach.

---

## Missed-opportunity angle
This is where the spare relay pole becomes really valuable:

not just for disconnecting things, but for making the **export lanes follow the active measurement context**.

That turns 2 lanes into:
- not “2 fixed channels”
- but “2 smart contextual diagnostics”

That’s much better.

---

## My concise recommendation
With only **2 lanes**, I’d do this:

- **Lane 1 = selected OS voltage**
- **Lane 2 = selected follower/drain current**

and switch both together so they always refer to the same active OS path.

That is the highest-value use of the available channels.

If you want, I can lay out a simple truth table for **OS1 / OS2 / noise-cal** showing exactly what each lane should carry.

[M153] ME (2026-03-19 19:51):
That’s what I mean… how couple the relay help this?

[M154] AI (2026-03-19 19:51):
It only helps if the relay is already selecting **which OS path is active**.

That is the key.

## What the relay pole can and cannot do
A spare relay pole does **not create extra lanes**.  
It only lets you make the **2 lanes follow the selected path**.

So instead of needing:

- OS1 voltage
- OS1 current
- OS2 voltage
- OS2 current

all at once,

you use the relay to say:

- when **OS1** is selected, export **OS1 voltage + OS1 current**
- when **OS2** is selected, export **OS2 voltage + OS2 current**

That is how the relay helps.

## In plain terms
The relay gives you **context-coupled multiplexing**.

It means your two exported lanes are not fixed as:
- “always OS1”
- “always OS2”

They become:
- **lane A = voltage of whichever OS is currently selected**
- **lane B = current of whichever OS is currently selected**

So the relay does not increase channel count.  
It makes the limited channel count **follow the active channel**.

## When this works well
This works if:
- only **one OS is selected into the follower path at a time**
- or the system meaningfully operates one monitored path at a time

Then the relay is perfect, because you only care about the active one anyway.

## When it does not help much
If:
- both OS1 and OS2 are simultaneously important,
- and you need both at once,

then the relay doesn’t solve that.  
You still only have 2 lanes.

In that case you must choose between:
- both voltages
- both currents
- or one voltage + one current

## The likely best implementation
Use the spare relay pole to switch the **monitor source routing**, not the shunt itself.

For example:

### Main relay contact
selects follower input:
- OS1 or OS2 or noise-cal path

### Spare relay contact
switches monitor lane sources so they track that same choice:
- lane 1 gets selected OS tap
- lane 2 gets selected current monitor for that same path

That way the two monitor lanes stay matched.

## Example truth table

### State 1: OS1 selected
- Lane 1 = OS1 voltage
- Lane 2 = OS1 drain/follower current

### State 2: OS2 selected
- Lane 1 = OS2 voltage
- Lane 2 = OS2 drain/follower current

### State 3: noise-cal
- Lane 1 = selected useful monitor for that mode
- Lane 2 = follower current in noise-cal mode, or park it

That is how the spare pole earns its keep.

## The real value
Without the spare pole, your two export lanes would need to be hard-wired to one path or the other.

With the spare pole, they become **dynamic diagnostic outputs**.

So the relay helps by making the two lanes:
- **relevant**
- **paired**
- **mode-aware**

not by giving you more total observability than physics allows.

## Bottom line
The relay helps only by making your **2 lanes track the currently selected OS path**.  
It does **not** let you observe both OS channels simultaneously.

[M155] ME (2026-03-19 19:55):
I think individual is fine. Just trying to get my head around the config. Two dpdt relay switches. Both operated with the same logic select. So regarding the two separate 

[M156] AI (2026-03-19 19:55):
Yes — that’s the right way to picture it.

If you’re happy with **individual, not simultaneous**, then **two DPDT relays driven by the same select logic** is a clean configuration.

## Mental model
Think of the system as having **one active context at a time**:

- **Select = A**
- or **Select = B**

Both relays move together, so all the monitoring follows that same context.

## Relay 1
This is the **main analogue function switch**.

It decides which signal is being used in the actual circuit, for example:

- **OS path**
- or **noise-cal / OD path**

So Relay 1 is doing the real operational switching.

## Relay 2
This is the **monitor-routing relay**.

It does not change the main function.  
It just makes your exported monitor lanes follow whatever Relay 1 selected.

That is the clean idea.

---

# With two exported lanes
You’ve got two monitor outputs available outside the chamber.

Call them:

- **Lane 1**
- **Lane 2**

Then Relay 2 makes those lanes context-sensitive.

## Example configuration

### Select state 0
Main relay:
- follower input = **OS path**

Monitor relay:
- **Lane 1 = scaled raw OS voltage**
- **Lane 2 = follower drain current**

### Select state 1
Main relay:
- follower input = **noise-cal / OD path**

Monitor relay:
- **Lane 1 = scaled raw OS voltage of whatever path you care about in that state**
- **Lane 2 = follower drain current in that state**

So both monitor lanes always refer to the same selected operating state.

---

# If there are two separate OS channels
If by “two separate” you mean **OS1** and **OS2**, then the exact same idea applies.

## State A
Main relay selects:
- **OS1**

Monitor relay selects:
- **Lane 1 = OS1 voltage**
- **Lane 2 = OS1 current**

## State B
Main relay selects:
- **OS2**

Monitor relay selects:
- **Lane 1 = OS2 voltage**
- **Lane 2 = OS2 current**

That is probably the cleanest use of your two lanes.

---

# Why two DPDT relays works well
Because each DPDT gives you **two poles that switch together**.

So one relay can switch:
- the main signal path(s)

and the second relay can switch:
- the monitor voltage path
- and the monitor current path

all with the same logic select.

That gives you a very tidy “functional path + matching observability path” arrangement.

---

# Best way to think about the poles

## DPDT relay 1
Use its two poles for the **main signal selection**.

For example:
- pole 1 switches the relevant analogue source
- pole 2 switches the complementary related path if needed

## DPDT relay 2
Use its two poles for the **monitor outputs**:

- **Pole 1 → Lane 1 source select**
- **Pole 2 → Lane 2 source select**

So Relay 2 is basically your **monitor multiplexer**.

---

# A clean truth table

| Select | Main function | Lane 1 | Lane 2 |
|---|---|---|---|
| A | OS1 active | OS1 voltage | OS1 current |
| B | OS2 active or noise-cal path | matching voltage | matching current |

That’s the essence.

---

# Important implementation point
Try to switch the **already buffered / conditioned monitor signals**, not the most delicate raw nodes, unless there’s a strong reason otherwise.

So ideally:

- raw OS tap goes into its monitor front end
- current shunt goes into its monitor front end
- relay switches which **monitor outputs** get sent to the two export lanes

That is cleaner than dragging raw high-impedance analogue nodes through relay contacts.

---

# Bottom line
Yes — **two DPDT relays, both driven by the same select logic**, is a very sensible way to do it.

One relay handles the **real circuit selection**.  
The other relay makes the **two exported monitor lanes track that same selection**.

That gives you:
- one active context at a time
- voltage and current for that context
- no need for four export lanes

If you want, I can draw a simple ASCII relay truth diagram for **OS1 / OS2** or **OS / noise-cal** exactly.

[M157] ME (2026-03-19 19:55):
Wait the relays don’t need to be independent logic drives

[M158] ME (2026-03-19 21:13):
[image]
How do I change the background colour in the library editor. Not obvious 
[attached file: IMG_09554406-756E-4689-AB4B-A334D480CEE7.jpeg]

[M159] AI (2026-03-19 21:13):
Yes — in the **library editor** it’s usually the same colour system as the schematic/PCB editors, but it’s hidden behind the **View Configuration** panel.

Try this:

## Schematic library background
In the **SCHLIB** editor:

- press **L**
- or open **Panels / View Configuration**
- look for **System Colors** or **Colors**
- change **Sheet / Workspace / Background** colour there

## If that doesn’t show in SCHLIB
Sometimes the library editor inherits the schematic colours globally. Then do:

- open a normal **schematic sheet**
- press **L**
- change the **sheet background / area colour**
- go back to the library editor

## Another route
Top right gear / preferences can also affect it:

- **Preferences**
- **Schematic**
- **Graphical Editing**
- **Colours** or similar display settings

## If you want the quick dark-to-light fix
In many Altium editors, **L** is the key shortcut that gets you to the display colours fastest.

## On your relay question
Also, no — the relays do **not** need independent logic drives if you always want them to switch together. One control net can drive both coils, provided:
- coil current is supported by the driver
- flyback protection is done properly
- there’s no timing reason to separate them

If you want, send one more screenshot after pressing **L** and I’ll point at the exact setting.

[M160] ME (2026-03-19 21:14):
Schematic 

[M161] AI (2026-03-19 21:14):
For **schematic / schematic library**, change it here:

- open the **SCHLIB** or schematic
- press **L**
- in **View Configuration**, go to **System Colors**
- change the **Sheet Color** / **Document Background**

If **L** doesn’t bring it up:
- use **Panels → View Configuration**

You’re looking for the colour entry for the **sheet/background**, not primitives.

If it still stays dark, check:
- **Preferences → Schematic → Graphical Editing**
- and any **theme / system colour** setting there

And on the relay point: **no, they don’t need independent logic drives** if you want both relays to follow the same select state. One driver can drive both coils if the current budget is OK.

[M162] ME (2026-03-19 21:16):
[image]
Not in here?
[attached file: IMG_8577F828-E3B8-4A16-ABEA-75E35C728B0A.jpeg]

[M163] AI (2026-03-19 21:16):
Right — **not in that window**.

You’re in **Schematic - Defaults**, which is only for **primitive default styles** like line width, colours of objects, etc. It does **not** control the sheet background.

## Where to change the schematic background
Do it from the **editor view**, not Preferences:

- go back to the schematic or SCHLIB sheet
- press **L**
- that should open **View Configuration**
- in there, go to **System Colors**
- change the **Sheet Color / Workspace Color / Background**

## If L doesn’t work
Use:
- **Panels** → **View Configuration**

or sometimes:
- **View** → **Panels** → **View Configuration**

## What to look for
You want the colour entry for things like:
- **Sheet**
- **Area**
- **Workspace**
- **Background**

Not the primitive defaults list.

## Why yours looks dark
It’s probably using a dark **system/view colour theme**, not a primitive colour setting.

So yes: **you’re in the wrong menu for background colour**.  
Back out of Preferences and use **View Configuration** from the actual schematic editor window.

[M164] ME (2026-03-19 21:16):
That L never works in somatic by the way 

[M165] AI (2026-03-19 21:16):
That fits with Altium being inconsistent. In **schematic/schlib**, `L` often does **not** bring up the same thing you expect from PCB.

Use this instead:

## For schematic background colour
From the schematic editor window:

- open **Panels**
- choose **Properties**
- click on a blank area of the sheet so the **sheet/document properties** show
- look for **page options / sheet options / colors**
- change the **sheet colour / background colour** there

## If that still doesn’t show it
Try:

- **View → Panels → View Configuration**
- then look under **System Colors**

## Important distinction
There are three different places people end up by mistake:

- **Preferences / Schematic Defaults** → primitive defaults only
- **Document Options / Sheet Properties** → sheet appearance
- **View Configuration** → editor display colours

You were in the first one.

## Practical Altium reality
In schematic, the quickest route is usually:

- click on **empty sheet space**
- open the **Properties** panel
- edit the sheet appearance there

If you send one screenshot after clicking on a blank part of the schematic with the **Properties** panel open, I can point to the exact field.

[M166] ME (2026-03-19 22:09):
[image]
They use this one further back in the system for the full ID
[attached file: C46D3122-FA12-4693-9333-23B553CBF2E9.jpeg]

[M167] AI (2026-03-19 22:09):
Right — and this actually sharpens the choice.

If they already use the **LT6376** further back for the **full ID** measurement, then it is a very credible candidate for your spare “drain/follower current” monitor path too.

## Why it fits
The LT6376 is a **difference amplifier** with **gain = 10**, a **very wide common-mode range up to ±230 V**, and it is explicitly intended for **high-side or low-side current sensing** and **high-voltage to low-voltage level translation**. Its bandwidth is **300 kHz** with divider ratio 3.1 and **160 kHz** with divider ratio 10.3. It runs from **3.3 V to 50 V** supplies. citeturn977721view0

So for a **drain / follower supply current** monitor, it makes sense if:
- you mainly care about **state / trend / moderate-speed behaviour**, not a pristine 500 kHz waveform, and
- you want a **robust single-ended monitor output** from a potentially awkward common-mode node. citeturn977721view0

## Where it is strong
For this spare lane, LT6376 is attractive because it:
- is already used in the system, so there is **design familiarity**
- is designed for **current-sense / difference measurement**
- handles **high common-mode** comfortably
- gives you a **single-ended output** that you can then send onward or just pad out of the chamber. citeturn977721view0

## Where it is not the best choice
It is **not** the part I’d use for your **raw OS waveform export**.  
For that, you care about preserving a signal around the **hundreds of kHz / 500 kHz region**, and LT6376’s bandwidth is only **160–300 kHz depending on divider setting**, so it is more of a precision monitor than a waveform-faithful transport front end. citeturn977721view0

So I’d split the jobs like this:

### Raw OS voltage out
Use the **divider + LMH6553 differential transport** path.

### Follower drain / ID current
Use the **LT6376** on the shunt, then export that signal if needed.

That pairing is actually very nice:
- **voltage waveform** on one lane
- **stage current monitor** on the other lane

## On the spare LVDS driver lane
Your idea of:
- **LT6376 → single-ended**
- then **single-ended to differential**
- then send it out of chamber

is sound.

And even if you do not fully populate it now, routing it and leaving a pad/test access is a good insurance policy.

## On the relay logic question
Also, no — the relays do **not** need independent logic drives if you always want them to follow the same selection state.

If both relays should always switch together, one control signal can drive both coils, provided:
- the driver can supply the **combined coil current**
- you include proper **flyback suppression**
- and you do not need staggered timing.

That part is just design hygiene, not a functional problem.

## My recommendation
Yes — use the **LT6376** for the spare **drain/follower current** monitor path, not for raw OS. It is a better fit for that job than the raw-waveform path, and the fact it is already used in the wider system makes it an even stronger choice. citeturn977721view0

If you want, I’ll lay out the cleanest two-lane allocation using:
- **Lane 1 = selected raw OS voltage**
- **Lane 2 = selected follower current via LT6376**

[M168] ME (2026-03-19 22:11):
No I was t suggesting it. I’m
Space limited and the max isncompact and really well rated 

[M169] AI (2026-03-19 22:11):
Yep — in that case I’d stay with the **MAX4173** idea.

For your constraints, it actually fits well:

- **small package**
- simple external network
- **0 to 28 V common-mode** fits your rail nicely
- three gain options
- around **1.7 MHz bandwidth** on the family, which is plenty for a follower/drain-current monitor and comfortably more agile than the LT6376 route citeturn612289search1turn612289search15

So if the goal is **compact, easy to place, good-enough bandwidth, and low drama**, the MAX path is the better fit than a bulkier precision difference-amp approach. It is also explicitly positioned as a **simple, compact current-sense solution** in a space-saving package. citeturn612289search1turn612289search0

For this spare exported channel, I’d frame it like this:

- **Raw OS voltage**: use the divider + LMH6553 differential transport
- **Follower drain / ID current**: use the **MAX4173** on a shunt in the drain feed, then either leave it single-ended locally or hand it into the same style of single-ended-to-differential export stage if you want it outside the chamber

That’s a very balanced pair of observability channels.

The only real caution is this: the MAX4173 is a **current monitor**, not a pristine waveform front end. So it’s excellent for **stage current behaviour**, trends, bias movement, and dynamic response, but it is not the thing to use for the “full raw OS waveform on 28 V” job. For that, your voltage-monitor path remains the right one. citeturn612289search1turn612289search0

So yes — given your **space limit**, I think your instinct is right: **the MAX is the sensible choice**.

[M170] ME (2026-03-19 22:13):
What’s the befot of looking at these two together on a scope 

[M171] AI (2026-03-19 22:13):
The benefit is **correlation**.

Looking at the two together lets you see not just **what OS is doing**, but **what the follower stage does in response**.

## The two signals
You’d have:

- **Channel 1:** scaled **raw OS voltage waveform**
- **Channel 2:** **follower drain / collector current**

That gives you **cause and effect** on one screen.

## What that tells you
### 1) Whether the follower is behaving properly
You can see:

- OS moves
- drain current moves as expected

or

- OS moves
- current hardly changes / changes oddly / clips / lags

That tells you whether the second stage is actually following the first.

### 2) Whether a problem is in the node or in the stage
This is probably the biggest value.

#### Case A
- OS waveform looks wrong
- drain current also looks wrong

That points upstream, around:
- the OS source node
- bias network
- relay state
- CCD-side behaviour

#### Case B
- OS waveform looks fine
- drain current looks wrong

That points to:
- follower biasing
- transistor operating point
- clamp interaction
- stage loading / saturation

So it helps you separate:
- **node problem**
from
- **buffer problem**

### 3) Timing relationship
On a scope you can see:

- does current change **at exactly the same moment** as OS?
- is there **delay**?
- does it **overshoot**?
- is there **ringing**?
- does one edge behave differently from the other?

That is very hard to understand from single channels viewed separately.

### 4) Mode comparison
If you can view them in:
- **normal OS mode**
- and **noise-cal / OD mode**

you can compare how the stage behaves in each context.

That can expose:
- hidden loading
- relay feedthrough
- clamp action
- unexpected current draw in one state only

### 5) Confirming whether clipping is real
If you suspect clipping or limiting:

- raw OS channel tells you what the node is trying to do
- current channel tells you whether the follower is being driven into a limit

So you can tell whether clipping is:
- coming from the node itself
- or being introduced by the follower stage / clamp / supply current limit

## In practical engineering terms
On a scope, this pair gives you:

- **voltage stimulus**
- **current response**

That is one of the most informative combinations you can have.

It’s much more useful than:
- voltage + voltage
or
- current + current

when you’re trying to understand behaviour.

## Typical things you’d spot quickly
- follower turning on too hard
- current spikes on edges
- OS droop causing current collapse
- current asymmetry between positive and negative transitions
- stage saturation
- relay switching artefacts
- biasing that looks fine in DC but bad dynamically

## Bottom line
The benefit is that you get a **cause-and-effect view of the stage**:

- **raw OS voltage = what is being asked of the stage**
- **drain current = how the stage actually responds**

That makes debugging far faster and far more conclusive.

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] AI (2026-03-04 18:58):
I get what you mean — you want the **nominal operating point** to sit mid-scale so you get resolution both ways.

But the thing to centre is **the *measured output voltage* (VOUT of MAX4173 / ADC input)**, **not the OS node at 28 V**.

You can’t (and shouldn’t) “bias” OS to mid-rail; OS is the thing you’re observing. What you *can* do is add an offset to the **measurement channel** so the ADC sees mid-rail at nominal current.

## The clean way: offset the measurement output
Let the MAX4173 do high-side sensing as normal, then level-shift **its output**:

### Target
- ADC range: **0–3.3 V**
- Choose mid-rail: **1.65 V**
- Set:  
  \[
  V_{ADC} = 1.65\text{ V} + k\,(V_{MAX4173}-V_{nom})
  \]
or simpler:
  \[
  V_{ADC} = 1.65\text{ V} - V_{MAX4173}
  \]
(if you want droop in one direction)

That gives you “room” for OS current to go up or down without needing a huge shunt.

### Practical implementation (simple)
- Generate a clean **1.65 V reference** (divider + buffer or a proper ref).
- Use a **rail-to-rail op-amp** as a summer/differencer:
  - \(V_{ADC} = 1.65 + (V_{MAX} - V_{nom})\) (shifted), or
  - \(V_{ADC} = 1.65 - V_{MAX}\) (inverted about mid-rail)

This preserves OS biasing and uses ADC range well.

## But do you actually need bidirectional?
With your 5k6 load, current from that path is:
\[
I_{bleed}=\frac{V_{OS}}{5.6k}
\]
So as OS **drops**, bleed current **drops**. That’s a **one-direction** change. Unless there are other paths that increase current when OS droops, your current likely mostly moves one way.

If it’s basically one-sided, the simplest and most robust approach is still:

### My robust recommendation (no extra op-amp)
- **MAX4173H (×100)**
- **RSENSE ≈ 2.0 Ω**
- ADC sees:
  - ~**1.0 V** at 5 mA nominal
  - room up to ~15 mA before you approach 3 V

That gives you lots of resolution without any offset circuitry.

## Key decision

