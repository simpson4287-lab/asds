# Power supply overcurrent causes
Date (UTC): 2025-12-09 16:52
Conversation ID: 69385397-d9a4-8333-bde7-9f83b408b9d9
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-002.json

[M1] ME (2025-12-09 16:52):
In what situation would a power supply ocercurrent when operated with sense lines. Nothing that the laid is definitely healthy 

[M2] AI (2025-12-09 16:52):
When a power supply is used with **remote sense lines**, it regulates the output voltage based on the voltage measured at the *sense terminals*, not directly at the power supply output. Even if the load is healthy, **overcurrent can occur under certain conditions** where the sensed voltage becomes inaccurate — causing the PSU to drive more current than intended.

Here are **common situations where overcurrent may occur despite good load**:

---

### **1. Sense leads go open-circuit or have poor/dirty connection**
If the sense line disconnects, the PSU may think output voltage is low (or zero), so it increases drive to compensate → **current rises until overcurrent triggers**.

> Very common failure mode.

---

### **2. Reversed or incorrectly wired sense leads**
If sense polarity is wrong, the PSU sees incorrect feedback and drives output hard → **OC triggered quickly**.

---

### **3. Excessive resistance or long cables without proper sense compensation**
The PSU may try to boost voltage to overcome cable drop. If drop is large enough:

- PSU tries to raise output voltage
- Load draws more current
- Current limit activates

---

### **4. Sense leads picking up noise due to poor shielding / no twisted pair**
Noise injected into sense input can trick the regulator into believing voltage is low → overshoot → **overcurrent condition**.

---

### **5. Local/remote sense not strapped when no sense wiring is present**
On supplies requiring sense links:

- If no jumper present → the supply keeps rising voltage uncontrolled
- Result = **overvoltage attempt → current rises → OCP trips**

---

### **6. Load changes faster than regulation response**
Remote sense adds loop delay. Large step loads can cause momentary:

- **overshoot**
- **surge current**
- **trigger of current protection**

Especially in inductive or capacitive loads.

---

### **7. High capacitance near the load**
Remote sense tries to charge the capacitance as if it's part of line drop → large inrush → **OCP**.

---

### **How to confirm sense line issue**
If the load is healthy, check:

| Check | Expected / fault indication |
|-------|-----------------------------|
| Voltage at PSU output vs load | Large difference = sense compensation problem |
| Resistance of sense leads | > a few ohms can cause problems |
| PSU behaviour without sense (strapped locally) | Works fine = remote sense fault |
| Wiggle sense connector during operation | Change in behaviour = intermittent fault |

---

### Quick isolation test
1. Remove remote sense connections
2. Fit local sense jumpers (short +S to +V, -S to -V at PSU)
3. Power up again

If overcurrent disappears → **fault is in sense wiring or feedback integrity**, not the load.

---

If you want, I can help you step-diagnose the exact failure if you tell me:

1. PSU model + current rating  
2. Load type (resistive, motor, LED driver, analogue circuits etc.)  
3. How sense wires are run (length, twisted pair, shielded?)  
4. What voltage the supply reports vs what you measure at the load  

Reply with any details you have — we can narrow it down quickly.

[M3] ME (2025-12-09 17:44):
[image]
How would a plus and minus 9v supply be witted up. I have two floating supplies modules. They are these type 
[attached file: 1F5F4A0C-8372-4E73-9999-187AF443CA12.jpeg]

[M4] AI (2025-12-09 17:44):
Got it — you’re using **two floating DC outputs** in a Keysight N6700 modular PSU system. Because they are *floating*, you can combine them to create **± rails** (e.g. +9 V and -9 V) as long as the modules aren’t internally earth-referenced.

Here is the correct way to wire **±9 V from two isolated/floating supplies**:

---

## **Wiring for ±9 V dual rail**

```
      Supply A           Supply B
     +9V Output         +9V Output
        |                  |
        |                  |
       +9V              0V (Reference)
        |                  |
        |                  |
   +----+------------------+----+
   |                         |
  +9V Rail (to circuit)     -9V Rail (to circuit)

```

### Step-by-step:

1. **Set each module to 9.00 V output.**
2. Choose one output terminal from each supply to join together ― this becomes **0 V (ground / common).**
   - e.g. connect **Supply A – terminal** to **Supply B + terminal**
3. The two free terminals become your rails:
   - **+9 V comes from Supply A +**
   - **−9 V comes from Supply B −**
4. Your circuit 0V reference is the joined connection.

So final connections look like:

| Terminal | Connection |
|---------|------------|
| PSU A + | **+9 V output** |
| PSU A – | Join to PSU B + (**0 V reference**) |
| PSU B – | **–9 V output** |

---

### **Remote sense lines (important!)**

If you use sense wiring:

```
+Sense → connect to +9V at load  
-Sense → connect to -9V at load  
Common sense reference → to 0V join point
```

Or if sensing each module locally:

```
A +Sense → A +
A -Sense → A -

B +Sense → B +
B -Sense → B -
```

⚠ **Do not leave sense lines floating.**  
If sense lines lose reference, the PSU may overshoot and trigger **OC or OV protection** as discussed earlier.

---

### Things to double-check before powering up

| Check | Why it matters |
|-------|----------------|
| Each output is isolated/floating | Required for stacking supplies |
| Sense lines are strapped or wired to load | Prevents runaway regulation |
| Current limits set correctly | Protects equipment if polarity reversed |
| 0 V join is solid and low resistance | Avoids offset drift/noise/instability |

---

### Quick visual summary

```
      +9V Rail  ────── PSU A +
                      PSU A -
                        │
                        │  ⟵ Join = 0V
                        ▼
                      PSU B +
      -9V Rail  ────── PSU B -
```

---

If you want, I can also:

✔ Draw it specifically with your module connector layout  
✔ Provide recommended sense wiring for long cable runs  
✔ Help you test for stability and current limit behaviour  

Let me know if you want a diagram for **local vs remote sense setup** or if you plan to power **analogue circuitry, op-amps, audio, digital logic, etc.**, as grounding practice changes slightly depending on the load.

[M5] ME (2025-12-09 17:45):
4 are the connections on the back of the module

[M6] AI (2025-12-09 17:45):
Understood — you’re referring to the **4-terminal output arrangement** on the back of each Keysight N67xx module:

### Typical layout per channel:

```
  +S   +V   -V   -S
```

(+Sense, +Output, -Output, -Sense)

So each module has **two power terminals** (+V, -V) and **two sense terminals** (+S, -S).

Because your supplies are floating, you can make ± rails using **two modules** like this:

---

## **How to wire ±9V using the 4 rear terminals on each module**

### MODULE A → will become **+9V rail**
```
  +S ─┐
  +V ─┼────────────── +9V OUT
  -V ─┬────────────── 0V COMMON
  -S ─┘
```

### MODULE B → will become **-9V rail**
```
  +S ─┐
  +V ─┼────────────── 0V COMMON
  -V ─┬────────────── -9V OUT
  -S ─┘
```

Then join the **0V COMMON point together**:

```
MODULE A -V  ─────────┐
                      ├────── 0V Ground reference
MODULE B +V  ─────────┘
```

---

### Complete connection overview

```
             MODULE A (9V)                MODULE B (9V)
          -------------------          -------------------
           +S   +V   -V   -S            +S   +V   -V   -S
            |    |    |    |            |    |    |    |
            |    |    |    |            |    |    |    |
            |    |    |    |            |    |    |    |
            |    |    └────┐            |    └────────┐
            |    |         |            |             |
            |    └──── +9V OUT          └──── 0V COMMON
            |                                |
            └──── Local/remote sense          └──── -9V OUT
```

---

### **If using remote sense correctly**

You must duplicate the connections **at the load end** (not at PSU) for regulation:

```
From MODULE A:
  +V  → +9V load
  +S  → +9V load (same point)
  -V  → 0V join
  -S  → 0V join

From MODULE B:
  +V  → 0V join
  +S  → 0V join (same point)
  -V  → -9V load
  -S  → -9V load (same point)
```

⚠ If you aren’t using remote sense, link them locally:

```
+S to +V
-S to -V
```

(Do this on **each module** or the supply can over-compensate → overcurrent/unstable)

---

### Quick reminder

| Node | Comes from |
|------|-----------|
| **+9V** | Module A +V |
| **0V reference** | Module A –V tied to Module B +V |
| **–9V** | Module B –V |

---

### If you want, reply with:

1. Are you using **remote or local sensing**?  
2. Load type (analogue, digital, motor, op-amp rails etc.)  
3. Cable length between PSU and DUT  

and I’ll draw the **exact wiring diagram** for your scenario so it's bullet-proof and stable.

Send a photo of the rear terminal layout if you want me to annotate it directly.

[M7] ME (2025-12-09 18:00):
Pretty sure I have it wired up as you say. Does the supply need a certain setting in place

[M8] AI (2025-12-09 18:01):
Good question – with the N6700-type modules there *are* a couple of settings that can make life easier / stop weird OCP behaviour, but you don’t need anything exotic just to get ±9 V.

### 1. You **don’t** need a special “±” or “series” mode  
For two **independent, floating** modules wired in series for +9 V / –9 V:

- Set **each module to 9.00 V**.
- Wire them in series as we discussed:
  - CH-A **+V** → **+9 V rail**
  - CH-A **–V** tied to CH-B **+V** → **0 V/common**
  - CH-B **–V** → **–9 V rail**

That alone is fine – no special series-tracking mode needed.

---

### 2. The one thing that *does* matter: **sense configuration**

If you’re using the 4 terminals on the back, the supply needs to “know” whether it’s doing **local** or **remote** sense:

#### Easiest debugging setup
For now, to rule out sense problems:

- On each module **link +S to +V, and –S to –V at the module** (short local sense).
- Or, in the menu, set **Sense = LOCAL** (wording may vary).

Then try your ±9 V setup again:

- If overcurrent **disappears** → the issue was with remote-sense wiring or settings.
- If it still trips → we look at current limit settings / load.

#### When you *do* want remote sense

When you’re confident it’s stable and you want remote regulation:

For +9 V module (A):

- **+V & +S** both to the **+9 V node at the load**
- **–V & –S** both to the **0 V/common node at the load**

For –9 V module (B):

- **+V & +S** both to the **0 V/common node at the load**
- **–V & –S** both to the **–9 V node at the load**

And then enable **Sense = REMOTE** in the settings (if it isn’t automatic on your module).

If any of those sense leads are left floating, or land on the wrong node, the module can “think” the voltage is low and wind itself up → **OCP trips even with a healthy load**.

---

### 3. Double-check these protection settings

On each module:

- **Current limit**: set comfortably *above* the normal load current.
- Check whether **over-current is set to “limit” or “shutdown/trip”**.  
  - For testing, “limit” mode is less confusing: it will go into constant-current instead of tripping off.
- If your load has large input caps, expect a brief inrush – you may need a higher current limit or a slow-start / soft-turn-on mode.

---

### Quick test sequence

1. Strap sense locally (+S→+V, –S→–V) on both modules.
2. Set both to **9 V**, reasonable current limit.
3. Wire in series for ±9 V as before.
4. Connect load and turn outputs on.

If that behaves, we know the **wiring is fine and the issue is in sense config**. Then we can re-introduce remote sense step-by-step.

---

If you tell me:

- whether you see **CC / CV / Protect** on the front panel, and  
- whether you’ve got **Sense = Local or Remote** selected,

I can walk you through the exact setting sequence for your module type.

[M9] ME (2025-12-09 18:02):
So if it was wired up as we have agreed but local sense is selected it can produce fault 

[M10] AI (2025-12-09 18:04):
Short answer: **no – just having “local sense” selected with the series wiring we described will not, by itself, cause an over-current fault.** In fact, local sense is usually the *safest* way to debug a stacked ± supply.

Here’s what’s going on:

- On the N6700 modules, in **local sense** the sense terminals are effectively tied to the output terminals and the supply just regulates the voltage **at its own +V/–V posts**. citeturn2search1turn2search9  
- With two floating modules in series for ±9 V, that’s perfectly fine. Each module only “sees” the voltage between its own + and – terminals, regardless of what the other one is doing.

Over-current / faults appear when **something else** is wrong, for example:

1. **Remote sense is enabled but the sense wiring isn’t right**  
   - Sense leads left open, on the wrong node, or accidentally shorting things → the supply thinks the voltage is low and winds up the output until it hits current limit.

2. **Current limit set too low or big input caps on your DUT**  
   - Inrush at turn-on pushes it into CC or trips OCP even though the steady-state load is fine.

3. **Unexpected ground somewhere on the midpoint**  
   - E.g. the 0 V join is accidentally tied to chassis/scope ground in a way that stresses one module.

So, if you currently:

- have the two outputs wired in series as we discussed, and  
- have **Sense = Local** (or the sense jumpers fitted),

that alone should **not** create a fault. If you’re still getting an over-current or protection event, the next things to check are:

1. **What mode/indicator shows on the front panel?** (CV, CC, OV, OC, Protect, etc.)  
2. **Current limit setting on each module** vs the actual load.  
3. Whether there are any **remote sense wires still connected** out at the DUT from earlier experiments.

If you tell me exactly what the front panel shows when it “faults” (OC? OV? PROT?) and what your load is (e.g. op-amp board, how much current it should draw, any big caps), I can narrow it down a lot further.
