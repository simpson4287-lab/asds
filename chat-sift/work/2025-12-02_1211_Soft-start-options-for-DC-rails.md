# Soft-start options for DC rails
Date (UTC): 2025-12-02 12:11
Conversation ID: 692ed75b-33b0-8325-a203-1e9215480a9a
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-001.json

[M1] ME (2025-12-02 12:11):
I need to soft start some dc rails. Whats the best option? Varistor?

[M2] AI (2025-12-02 12:11):
Short answer: **don’t use a varistor for soft-start.** That’s for surge protection, not ramping rails. There are a few “good” ways to soft-start DC rails, and the right one depends on voltage/current and how fancy you want it.

---

## Why a varistor is the wrong tool

A varistor (MOV) or TVS:

- Is basically **open-circuit** at normal voltage  
- Suddenly becomes **low-impedance** when the voltage gets too high  
- Purpose: **clamp transients / surges**, not shape the startup ramp

It won’t control inrush into your caps or make the rail come up gently; it only reacts if the voltage spikes above its threshold.

---

## Better options for soft-starting DC rails

### 1. Use the regulator’s built-in soft-start (if available)
Most modern DC-DC converters and some LDOs have **soft-start pins**:

- You connect a **capacitor to SS/Soft-Start pin**
- The chip internally ramps the reference / duty cycle so the **output rises in a controlled way**
- Very clean, no extra active parts, protects against inrush into big output caps

If your rail is from a switch-mode regulator, check the datasheet first – this is often the best and simplest option.

---

### 2. Series MOSFET with an RC ramp (classic soft-start)

Great if you’ve got a fixed DC source (e.g. already-regulated 5 V / 12 V / 24 V rail) and want to **slowly connect it to the load**.

Basic idea:

- Put a **P-channel MOSFET (for high-side)** or **N-channel (for low-side)** in series with the rail  
- Drive the gate with an **RC network** so the gate voltage changes slowly  
- As the gate ramps, the MOSFET goes from off → partially on → fully on, so the **output rail ramps up instead of slamming on**

Key points:
- Add a **gate resistor** to control dV/dt and avoid oscillations.
- Check **SOA (safe operating area)** of the MOSFET – during startup it’s in the linear region and can dissipate significant power if the load is heavy.
- Often you also add:
  - A **bleed resistor** so it turns off properly
  - A **small series resistor** or current sense if you want basic over-current limiting

This is usually the best DIY “generic” soft-start for medium-power stuff.

---

### 3. Inrush limiter / pre-charge (resistor or NTC + bypass)

If the main problem is **charging big bulk capacitors** (e.g. big input caps on a board or module), you can **pre-charge**:

- Put a **series resistor or NTC thermistor** in line with the rail
- After a short time (caps mostly charged), **short it out** with a relay or MOSFET

Variants:
- **NTC inrush limiter**:
  - High resistance when cold → limits initial current
  - Heats up → resistance drops, so normal operation has lower loss
  - Simple and cheap, but ramp shape isn’t precise, and if you power-cycle quickly (still hot) it barely limits anything.
- **Fixed resistor + MOSFET bypass**:
  - Predictable pre-charge current (I ≈ V/R)
  - After a delay, drive MOSFET on to bypass resistor
  - Good when you want a more controlled limit than an NTC

This is nice for higher-voltage/higher-energy rails where the main issue is that first cap-charge spike.

---

### 4. Hot-swap / ideal-diode / power-path controllers

For more serious / high-current or multi-board stuff (e.g. plugging into a backplane, or 12–48 V systems):

- Use a **dedicated hot-swap controller IC** (e.g. LTC/ADI, TI, etc.)
- They:
  - Control a series MOSFET
  - Limit inrush current very precisely
  - Often provide **over-current**, **short-circuit**, and **UV/OV protection**
  - Sometimes handle **fault retry**, **power-good**, etc.

If your rail is more than just a small bench circuit, this is often the most robust and safest option.

---

### 5. Multi-rail sequencing / enable pin tricks

If your real goal is **“power this rail first, then that rail, and avoid glitches”**, you can:

- Use the **enable pin** of each regulator with RC delays
- Or use a **power-sequencer IC**

That doesn’t do inrush limiting by itself, but it *does* control **when** things turn on and can avoid situations where one rail tries to back-feed through protection diodes.

---

## Rough guidance

If you tell me (next message) roughly:

- Voltage(s)
- Max current / power
- Whether it’s one rail or several, and if it’s from a DC-DC / bench / battery

…I can sketch an exact little soft-start topology and ballpark component values (MOSFET type, R/C values, etc.) for your case. But in general:

- **Small/medium load, board-level rail** → Regulator soft-start or MOSFET+RC
- **Big caps / higher energy** → Pre-charge resistor/NTC + bypass MOSFET/relay
- **Serious / high-current or “hot-plug”** → Dedicated hot-swap controller
- **Never**: varistor as the soft-start element 🙂

[M3] ME (2025-12-02 12:13):
What’s an ntc

[M4] AI (2025-12-02 12:13):
An **NTC** is a type of thermistor used for **inrush-current limiting**. Full name:

> **NTC = Negative Temperature Coefficient thermistor**

### What that actually means
Its resistance **drops when it gets hot**:

- When it’s cold (at power-up): resistance is **high**
  → limits the first big surge of current into caps, motors, switch-mode supplies, etc.

- After a fraction of a second: current heats the part, resistance **drops low**
  → normal operating losses become small

So it kind of “auto soft-starts” the circuit.

---

## Why NTCs get used for soft-start
Typical application:

When you plug in a supply with big capacitors, you get a huge instant current spike.  
Put an NTC in series → it limits that spike.

It’s cheap, passive, and zero control signals needed.

---

## The catch
NTCs are not perfect:

### Pros
- Very cheap
- No control circuitry
- Simple for high-voltage AC/DC loads or big cap banks

### Cons
- Ramp shape is **not controlled** (depends on temperature)
- If you restart while still hot → resistance is low → **no inrush limiting**
- Causes some heat loss in steady state
- Not a precision soft-start element

---

## What one looks like
They are usually disc-shaped like this:

```
   ----/
  ( NTC )
   ----\
```

Often labelled something like: **NTC 5D-11**, **NTC 10R-9**, etc.

Example meaning:

- “10R” = ~10 Ω cold resistance
- “9” = size in mm

---

## When not to use an NTC
If you want a **controlled voltage ramp or multi-rail sequencing**, use:

- MOSFET soft-start
- Hot-swap controller
- Regulator’s soft-start pin

NTCs are mainly for **inrush current into capacitors or power supplies**, less for precision ramp.

---

## If you want, tell me your rails:
Just send:

- Voltage
- Max current
- Load type (supply? ICs? motors?)
- Why you want soft-start

and I’ll tell you whether an NTC is appropriate — or recommend a better option for your case.

[M5] ME (2025-12-02 12:13):
Rails are 32v / +- 18v

[M6] AI (2025-12-02 12:14):
Nice, that’s enough to start being concrete.

You’ve basically got:

- One **+32 V rail**
- One **±18 V pair**

I’ll assume the ±18 V comes from the 32 V (or same source) and that your main worries are inrush into caps and not slamming sensitive analogue stuff.

---

## 1. When an NTC makes sense here

If the issue is mainly **“big caps on 32 V / ±18 V” → huge inrush when you power up**, then:

- Put **one NTC in series with the main 32 V input**  
- Let the ±18 V regulators and local caps hang off that

That gives you:

- First few ms: NTC is cold → several ohms → **limits inrush**
- After a short time: NTC heats → drops to < 1 Ω → negligible drop at normal current

This is fine if:

- You don’t need a **nice controlled ramp shape**, just “don’t blow fuses or stress rectifiers / connectors”
- You’re not doing **rapid on/off cycles** (because if it’s still hot, its resistance is low → no inrush protection)
- You’re okay with a bit of extra dissipation in the NTC

Very rough example (totally generic):

- 32 V rail, you’d like inrush limited to, say, ~5 A into your bulk caps
- Need **R_cold ≈ V / I ≈ 32 / 5 ≈ 6.4 Ω**
- You’d pick something in that ballpark, but also rated for your **steady-state current** and energy

So: **for a simple, cheap solution just to tame inrush, an NTC on the 32 V input is reasonable.**

---

## 2. When you’re better off with MOSFET soft-start

Use a **MOSFET-based soft-start** if ANY of these are true:

- You want a **controlled ramp** on the ±18 V rails (e.g. to avoid pops, op-amp latch-up, DAC/ADC weirdness)
- You need the system to withstand **rapid power cycling**
- You care about **minimising dissipation** and having predictable behaviour

Typical approach:

### On the 32 V rail

- Put a **P-channel MOSFET high-side** in series with the 32 V
- Gate network:
  - Gate tied to source via a resistor (keeps it **off** initially)
  - An **RC to ground** that slowly pulls the gate down, turning the MOSFET on gradually
  - Optionally a **zener between gate and source** to keep |Vgs| below its maximum, since 32 V is near or above a lot of FET Vgs ratings

So the 32 V line at the board input becomes:

> 32 V in → P-FET → board bulk caps / regulators

As the gate ramps, the FET gradually enters conduction → your 32 V rail ramps instead of jumping.

### For ±18 V rails

Options:

1. **Let them be derived from the soft-started 32 V**  
   If your ±18 V regulators (or DC-DCs) have their own **soft-start pins**, use those – that’s the cleanest.

2. Or put **small MOSFET soft-starts on each ±18 V** rail individually  
   - One P-FET for +18 V  
   - One N-FET or P-FET arrangement for –18 V (often back-to-back FETs for symmetry, if you want truly clean disconnect)

This is what you’d do if you care about **rail sequencing** (e.g. +18 then –18) or avoiding any weird current paths during startup.

---

## 3. So what’s “best” for your case?

Given just “32 V / ±18 V rails” and no more constraints, I’d summarise like this:

- **If the main problem is big capacitor inrush and you don’t care about exact ramp shape or fast restart:**
  - 👉 **NTC in series with the 32 V input** is OK and simple.
- **If you care about clean analogue behaviour, sequencing, repeatable startup, or you might power-cycle quickly:**
  - 👉 Use a **MOSFET soft-start on the 32 V** and, if needed, **soft-start / soft-enable on the ±18 V** rails too.
- **If currents are high (amps) and you’re plugging this into a live bus (like 24–32 V system):**
  - 👉 Consider a **hot-swap controller IC + external MOSFET** instead of a bare RC/FET hack.

---

If you tell me roughly how much current each rail draws and what’s supplying them (bench supply / SMPS / transformer+rectifier), I can sketch a very concrete soft-start scheme for your setup with example MOSFET types and RC values.

[M7] ME (2025-12-02 12:15):
No more than an amp

[M8] AI (2025-12-02 12:15):
Cool, that’s nice and gentle currents then 👍

At **≤1 A** on **32 V / ±18 V**, you’ve basically got two realistic “simple but decent” options:

---

## Option 1 – Easiest: NTC in series with the 32 V input

If your main concern is **“don’t slam my caps / rectifiers / connectors with inrush”** and you’re not doing rapid power-cycling, an **NTC on the 32 V input** is absolutely fine.

### How to do it

Put an NTC thermistor in series with the **32 V feed** before everything else:

> 32 V in → **NTC** → bulk caps / ±18 V regulators → rest of circuit

### What to look for

For your case (max 1 A):

- **Cold resistance**: something in the **5–10 Ω** range  
  - At turn-on, limits inrush roughly to:
    - 32 V / 10 Ω ≈ **3.2 A**
    - 32 V / 5 Ω ≈ **6.4 A**
- **Current rating**: at least **1 A continuous**, preferably a bit more for margin (2–3 A parts are common)
- **Steady-state drop**:  
  When hot, NTC might drop to ~0.3–0.8 Ω:
  - At 1 A → 0.3–0.8 V drop, 0.3–0.8 W dissipation  
  - That’s acceptable but it will run warm, so don’t jam it against heat-sensitive stuff.

### Pros / cons for you

- ✅ Super simple, 2 solder joints
- ✅ Cheap
- ✅ Good enough for “tame the inrush”
- ❌ No precise voltage ramp shape
- ❌ **Fast off/on** (while it’s hot) = almost no inrush limiting

If your rails feed general analogue/digital stuff that doesn’t care about exact ramp timing, this is probably all you need.

---

## Option 2 – Nicer: P-MOSFET soft-start on the 32 V

If you want something a bit more controlled and **repeatable** than an NTC, a **P-channel MOSFET high-side with an RC on the gate** is a good sweet spot.

### Concept

> 32 V in → **P-MOSFET** → bulk caps / ±18 V regs

- The MOSFET is initially off.
- An RC on the gate slowly pulls the gate down relative to the source, making the MOSFET conduct gradually.
- Your 32 V rail at the board then **ramps** instead of stepping.

### Rough example (numbers you can tweak)

- Use a **P-MOSFET** rated:
  - **Vds ≥ 40 V**
  - **Id ≥ 3–5 A** (overkill but gives margin)
  - **Logic-ish gate** is a bonus but not essential.
- Gate network (simple version):

  - **Rgs** (gate–source): ~100 kΩ  
    - Keeps the FET **off** at power-up (gate = source initially).
  - **Cgate** (gate to ground): e.g. 100 nF
  - Optional: **small series resistor in gate** (like 100–220 Ω) to prevent ringing.
  - Optional but recommended: a **zener (e.g. 12–15 V) between gate and source** to clamp Vgs, because with 32 V rails you don’t want to exceed the FET’s ±20 V gate rating.

  Time constant ≈ Rgs × Cgate  
  - 100 kΩ × 100 nF ≈ 10 ms  
  - For a slower ramp, you can go 470 kΩ / 100 nF ≈ 47 ms, etc.

So at power-up:

1. Source jumps to 32 V, gate is initially also at 32 V → FET off.
2. Cgate starts pulling the gate toward 0 V through its connections.
3. As **Vgs** becomes more negative (down to the zener clamp limit), the MOSFET gradually turns on → your 32 V rail downstream ramps up.

Your **±18 V regulators** then ride on that ramp and come up smoothly too.

### Pros / cons

- ✅ Way less dissipation than an NTC in steady-state
- ✅ Behaviour is **repeatable**, even for quick off/on cycles
- ✅ Gives a reasonably controlled ramp (better for some analogue circuits)
- ❌ A few more parts and a bit of layout thought (heat, SOA)

At ≤1 A, a decent P-MOSFET won’t even break a sweat.

---

## Which would *I* pick at 1 A?

- If you just want **“don’t hammer the caps / supply”** and don’t care about ramp shape:
  - 👉 **Single NTC on the 32 V input** is absolutely fine.
- If this feeds **sensitive analogue stages** or you care about **repeatable start-up / fast power-cycling**:
  - 👉 **P-MOSFET soft-start on 32 V** is a better long-term choice.

If you tell me whether this is, say, an audio front-end, CCD stuff, op-amp rails, etc., I can nudge you toward the one that matches that use-case – but either way, **varistor is still firmly “no”** for soft-start 🙂

[M9] ME (2025-12-02 12:16):
Next is fine, suggest part?

[M10] AI (2025-12-02 12:16):
Nice, NTC it is then 👍

At **≤1 A, 32 V** you don’t need anything exotic. Something in the **5–10 Ω cold, 2 A rated** class is spot on.

Here are a couple of concrete examples you can look up:

- **Generic “10D-9, 10 Ω, 2 A” inrush NTC**  
  e.g. parts sold as *“NTC Thermistor 10D-9, 10 Ω, 2 A Inrush Current Limiter”* – disc about 9 mm, 10 Ω cold, 2 A continuous. citeturn0product3  
  - Cold ≈ 10 Ω → first-hit inrush ≈ 32 V / 10 Ω ≈ **3.2 A**  
  - Hot resistance ≈ 0.5–1 Ω → at 1 A you lose maybe 0.5–1 V and 0.5–1 W in the part.

- **Amphenol CL-120, 10 Ω NTC** (more “proper brand” distributor part) citeturn0product2  
  - Around 10 Ω cold, disc type, specified for inrush limiting.
  - This class of part is fine at your current levels; just check the exact continuous current rating and energy rating in the datasheet.

If you’d prefer **less voltage drop** in steady state and can tolerate a bit more inrush, you can go for roughly **5 Ω cold** instead of 10 Ω:

- Target:  
  - 32 V / 5 Ω ≈ **6.4 A** max inrush  
  - Hot maybe ~0.3–0.6 Ω → **0.3–0.6 V** drop at 1 A

Look for descriptions like:

> “NTC inrush current limiter, 5 Ω, 2–3 A, disc 9–13 mm”

and you’re in the right territory.

### How to drop it in

On your 32 V feed:

> 32 V input → **NTC** → all your bulk caps / ±18 V regs → rest of circuit

- Make sure it has **a bit of airflow** and isn’t crammed against plastic.
- Don’t expect protection if you **flick it off and back on quickly** – while hot, the NTC is basically a small resistor.

If you tell me your rough bulk capacitance on the 32 V line (µF) I can sanity-check energy vs. the NTC so you know you’re not abusing it, but with 1 A rails you’re very likely in a comfortable zone.

[M11] ME (2025-12-02 12:17):
Gonna link?

[M12] AI (2025-12-02 12:17):
Sure — here are a few NTC-thermistor inrush limiters you could buy for your ≤1 A, 32 V rails. These are all cheap, disc-style “inrush limiters,” suitable for small DC rails like yours.

## ✅ Sample NTC thermistors you can order

products{"selections":[["turn0product2","NTC 5D-7 5 Ω Inrush Current Limiter"],["turn0product18","Vishay Ametherm ICL NTC 5 Ω Inrush Thermistor"],["turn0product0","uxcell NTC Thermistor 10 Ω 2 A Inrush Current Limiter"],["turn0product1","NTC 5D-25 Inrush Suppression Thermistor"],["turn0product11","Generic Disc-Type NTC Inrush Current Limiter (5–10 Ω)"],["turn0product5","TKS SCK-10502MS 50 Ω 2 A NTC Inrush Limiter"],["turn0product16","TDK B57153S0100M000 NTC Inrush Current Limiter"],["turn0product19","Amphenol 5 Ω 6 A NTC Inrush Current Limiter"]],"tags":["Low-Ω 5 Ω – gentle limit","Brand 5 Ω","Common 10 Ω 2 A","Low-Ω 5 Ω","Generic 5–10 Ω","High-Ω 50 Ω","TDK 10 Ω","Robust 5 Ω"]}

### Quick notes on some picks

- **product_entity["turn0product2","NTC 5D-7 5 Ω Inrush Current Limiter"]** — a low-Ω NTC, useful if you want minimal steady-state drop but modest inrush limiting (for up to a few amps).  
- **product_entity["turn0product18","Vishay Ametherm ICL NTC 5 Ω Inrush Thermistor"]** — from a reputable manufacturer, a good “drop-in” NTC if you want reliability and known datasheet specs.  
- **product_entity["turn0product0","uxcell NTC Thermistor 10 Ω 2 A Inrush Current Limiter"]** — a common “10 Ω / 2 A” NTC disc, decent if you expect higher initial inrush (good if you have larger capacitors).  
- **product_entity["turn0product1","NTC 5D-25 Inrush Suppression Thermistor"]** — alternative disc NTC, useful if you want something between “gentle” and “strong” inrush limit.  
- **product_entity["turn0product11","Generic Disc-Type NTC Inrush Current Limiter (5–10 Ω)"]** — a generic option (not brand-name), fine for simple bench / hobby builds.  
- **product_entity["turn0product5","TKS SCK-10502MS 50 Ω 2 A NTC Inrush Limiter"]** — high-Ω part: this would strongly limit startup current — maybe overkill for a 1 A rail, but useful if you have very large bulk caps.  
- **product_entity["turn0product16","TDK B57153S0100M000 NTC Inrush Current Limiter"]** — from a major manufacturer, good if you prefer industrial-grade components for reliability or long-term use.  
- **product_entity["turn0product19","Amphenol 5 Ω 6 A NTC Inrush Current Limiter"]** — over-spec for your current, but nice if you want margin or plan future upgrades.

---

### ⚠️ What to check when you buy

- **Cold resistance**: generally 5–10 Ω works well for a 1 A rail.  
- **Rated continuous current**: at least **1–2 A**. Prefer a bit higher to give margin (many above are 2–4 A). citeturn0search11turn0search6turn0search0  
- **Physical size & disc rating**: ensure the thermistor disc isn’t so small it overheats or so large it’s hard to fit. citeturn0search11turn0search4  

---

If you like — I can **build a short BOM (Bill of Materials)** for your 32 V/±18 V rail (with 1 A current) including **2 or 3 alternative NTCs** — so you have ready-to-order part numbers + footprint suggestions for PCB or prototyping. Do you want me to go ahead and build that BOM for you now?
