# Circuit fault analysis
Date (UTC): 2025-11-12 05:13
Conversation ID: 69141739-10e0-832e-a1be-52e5cbc281f1
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-001.json

[M1] ME (2025-11-12 05:13):
[image]
I have a circuit fault I need help with. The pink box is typically a negative input and -9 V in this case. A fault occurred where it was reverse polarity 2+9 V as a consequence the circled capacitor has got charge and been sacrificed which may be a good thing for the regulators survival but also the blue circle is a P and Moss vet so did that help save the day as well if that was on
[attached file: IMG_1933ED97-9BB9-4124-93F4-B58DDCD3D3E5.jpeg]

[M2] AI (2025-11-12 05:15):
Short answer: the cap took the hit; the P-MOSFET probably didn’t “save the day.”

What I can read in your shot:

- The negative rail is **-9V_DUT_1** (pink).
- The big input cap **C56 100 µ/16 V** (red) is from the –9 V rail to 0 V (its **positive** plate should be at 0 V because it’s a negative supply).
- There’s a **10 Ω/0.5 W** series resistor **R112** in that rail.
- The blue device **TR11 = BSS308PE** is a **P-MOSFET**, but it is not in the power path of the –9 V rail; it’s tied around the **IVS_COMP**/supervisor area (a clamp/discharge function), i.e., a housekeeping transistor.

### What happened with +9 V applied by mistake
- **C56 was reverse-biased** (its negative plate was driven positive). Electrolytics hate that: they heat, gas, and either vent open or short briefly then go open. That’s why it “sacrificed” itself.
- **R112** limited the fault current into the rest of the –9 V network while the cap was mis-biased. If anything helped the regulator to survive, it was R112 plus the cap failing early.
- **TR11 (P-MOSFET)** in blue is not positioned to block reverse polarity on the –9 V rail. It’s a clamp/switch for a logic/supervisory node; it wouldn’t have protected the LT3091 negative LDO from a polarity reversal on the rail.

### Likely damage / what to check
1. **Replace C56** with a fresh 100 µF/16 V (or higher-voltage) electrolytic **oriented for a negative rail** (positive to 0 V, negative to –9 V).  
2. **Inspect/measure R112**. If it looks dark or measures high, replace it.  
3. **Check the LT3091** (the negative LDO shown at left). With power off, measure resistance from its –IN pins to 0 V—shouldn’t be a dead short.  
4. **Power-up carefully** with a bench supply current-limited to ~50–100 mA. Sweep from 0 V down to –9 V and watch input current. Verify the regulator output rails come up normally and no part heats.  
5. **Supervisor/MOSFET (TR11)** is probably fine. You can quickly sanity-check its body diode with a DMM (it should conduct one way only) and confirm the gate isn’t shorted to source/drain.

### If you want a bit more protection next time
- Add a **reverse-polarity protection MOSFET** in the *negative* rail (P-MOS or N-MOS arranged as an ideal diode in the correct orientation for a negative supply), or a **Schottky diode** if you can tolerate the drop.  
- Use a **bi-polar electrolytic** or add a **back-to-back electrolytic pair** on rails that might be exposed to polarity mistakes, and keep the **series resistor** (it clearly helped).  
- A **TVS diode** for the negative rail (correct polarity) can clamp transients without reverse-biasing the electrolytic.

Bottom line: replace the cap (and R112 if needed), then bring the rail up gently. The P-MOSFET in blue is supervisory, not a reverse-polarity guard for the –9 V input.

[M3] ME (2025-11-12 05:19):
[image]
So there are tvd diodes on the input. When the fault occurred it was using a bench supply with current limit which would have hopefully suppressed any major surge before it stepped in. The board powers up ok now, and the 7.5 v rails + and - are healthy. 
[attached file: IMG_898E7004-AEF7-4A12-B652-4110F630B24C.jpeg]

[M4] AI (2025-11-12 05:20):
Good news that it powers up and both ±7.5 V rails look healthy. The TVS parts on the input help with *surges* and *over-voltage*, but they don’t really save you from the specific mistake you had (+9 V applied to the –9 V pin).

Why:
- In your schematic the TVSs are 12 V parts from each rail to 0 V. For the +9 V rail the TVS is **cathode to +9, anode to 0 V**; for the –9 V rail it’s **anode to –9, cathode to 0 V**.  
- If you put **+9 V on the –9 V input**, that TVS is **reverse-biased** and won’t conduct until ~12 V in reverse—so it doesn’t clamp.  
- The electrolytic on the –9 V rail *does* get reverse-biased (its negative lead was driven positive), which is why it vented. The series resistor in that rail also limited stress on the rest of the circuit. Your bench supply current-limit helped keep it from getting catastrophic.

So: the TVSs likely didn’t conduct in this event and are probably fine; the sacrificed cap and series resistor are what spared the regulator.

What I’d do now (quick checklist):
1. **Replace the reversed electrolytic** (use ≥16 V, orient for a negative rail: positive to 0 V). Inspect/ohm-check the series resistor and replace if it drifted.  
2. **Sanity-check the TVSs**: with power off, diode-test each to 0 V—you should see ~0.6–0.8 V one way (forward) and open the other (unidirectional parts). Any near-short = replace.  
3. **Power up with current-limit** and watch input current on ±9 V.  
4. **Scope ripple** on the ±7.5 V rails (AC-coupled, 20 MHz BW). Excess ripple ⇒ the input cap or LDO took damage.  
5. **Touch-test** the LDOs and nearby parts—no hotspots.

If you want true reverse-polarity protection next time:
- Add an **ideal-diode MOSFET** in each input rail (there’s a standard P-MOS arrangement for the negative rail), or a **Schottky** if a small drop is acceptable.  
- Keep the **series resistor**; it clearly helped.  
- TVSs are still useful for ESD and plug-in transients.

Bottom line: replace the cap, verify the resistor, and do the quick checks above. The regulators likely survived because the TVS didn’t turn on in this scenario, the cap took the abuse, and your current limit kept energy low.

[M5] ME (2025-11-12 05:22):
Explain further why tvs not conducting helped the regulator 

[M6] AI (2025-11-12 05:22):
Excellent question — and this is subtle but very important to understand.  

Let’s unpack what happened and **why the TVS *not* conducting actually saved the regulator**, step by step.

---

### ⚙️ 1. What the TVS is meant to do
A **TVS diode (Transient Voltage Suppressor)** — like your SMAJ12A — is designed for **brief, high-voltage spikes** (ESD, surge).  
It’s **not** a polarity-protection device — it clamps *overvoltage* between the rail and ground, not *reverse voltage*.

So, in normal use:
- The –9 V TVS sits between the –9 V rail (anode) and 0 V (cathode).
- It will only conduct if the rail goes **more negative** than about –12 V (because it’s a 12 V part).  
- If the rail goes **positive**, it remains *reverse-biased* — i.e. open circuit.

---

### ⚡ 2. What happened in your reverse-polarity fault
You accidentally applied **+9 V** to the **–9 V input**.

So, relative to ground:
- The “–9 V” node was actually at **+9 V**.
- The TVS diode’s anode was at +9 V, and its cathode at 0 V → it was **reverse-biased**, so **no conduction**.
- The regulator’s input pin, however, saw a **positive voltage instead of a negative one**.

Now here’s the key point:
If the TVS had conducted, it would have **dumped that +9 V straight to ground**, creating a **massive current surge** through your supply and tracks, because TVSs are almost like short circuits when they fire.  
That surge current would have:
- Pulled the “–9 V” line violently towards 0 V.
- Potentially **driven current backwards through the LDO**, through internal ESD diodes or body diodes.
- Very likely **blown the regulator instantly** or lifted PCB copper.

---

### 🔥 3. Why *not* conducting was beneficial
Because the TVS stayed off:
- There was **no large, low-impedance current path** from +9 V to ground.
- The only current path was through the **series resistor (R112)** and the **reversed electrolytic cap (C56)**.
- That resistor **limited current** and slowed the fault transient — acting as a “fuse-and-snubber” combination.
- The cap heated, vented, and opened up — **sacrificing itself as a harmless failure** rather than turning the board into a short circuit.

This “gentle” failure meant:
- The regulator’s internal structures weren’t forced to conduct large reverse currents.
- Your bench supply never went into a hard short, and the voltage never slammed the sensitive internal nodes of the regulator.

Essentially, the energy was **absorbed and dissipated locally** (in the cap + resistor) instead of **being dumped through the LDO and the TVS**.

---

### 🧠 4. If the TVS *had* conducted
Let’s imagine it did:

| Scenario | Result |
|-----------|---------|
| +9 V applied to –9 V node | TVS clamps to ≈ 0 V via avalanche |
| Current path | +9 V → TVS → ground |
| Current magnitude | Limited only by PSU and wiring (tens of amps) |
| Regulator input | Rapidly pulled through 18 V differential swing |
| Consequence | Regulator body diodes conduct backwards → internal ESD damage or latch-up, likely fatal |

So ironically, the **TVS staying open** spared both the **power supply** and the **downstream ICs**.

---

### ✅ 5. Why the board survived
1. **Bench supply current limit** restricted fault current.  
2. **Series resistor (R112)** absorbed and dropped much of the reversed voltage.  
3. **Electrolytic capacitor (C56)** failed open, not short — effectively isolating the reversed rail.  
4. **TVS diode didn’t clamp**, so no destructive surge current.  
5. Therefore, the **LDO saw only a modest reverse bias**, not a destructive current injection.

---

### 🧩 Summary Analogy
Think of it like a car crash:
- The **TVS firing** would have been like slamming into a brick wall (huge current impact).
- The **TVS staying off** meant you slid into a soft barrier (resistor + cap) that absorbed energy gradually.

The “soft barrier” approach saved your expensive components.

---

Would you like me to draw a simple annotated diagram showing the current paths for the “TVS conducts” vs. “TVS doesn’t conduct” cases? It makes the current flow and protection logic visually clear.

[M7] ME (2025-11-12 05:26):
But if 9v was on the anode and of on cathode doesn’t the diode conduct like a conventional one?

[M8] AI (2025-11-12 05:26):
Excellent — that’s the *right instinct* to question it.  
Let’s go carefully through the polarity and the actual behaviour, because this part trips up even experienced engineers.  

---

### 🧭 First — recall what the TVS actually *is*
Your device (e.g. **SMAJ12A**) is a **unidirectional TVS diode**.  
It behaves like a **normal diode** in the forward direction, and like a **Zener diode** in the reverse direction (avalanche mode).  

So we have two possible conduction cases:

| TVS direction | Symbol meaning | Conducts when… | Typical drop |
|----------------|----------------|----------------|---------------|
| **Forward direction** (like a normal diode) | Anode → Cathode | Anode ≈ 0.7 V higher than cathode | ≈ 0.7 V |
| **Reverse direction (avalanche)** | Cathode → Anode | Cathode ≈ breakdown voltage (≈12 V) higher than anode | ≈ 12 V clamp |

---

### ⚡ The way yours is wired (negative rail protection)
In your schematic:

- The **negative rail** is at –9 V.  
- The **TVS** has **anode connected to –9 V**, **cathode to 0 V**.

In *normal operation*:
- The anode (–9 V) is **9 V lower** than the cathode (0 V).  
- That means it is **forward biased** — but only by 9 V? Wait, here’s the subtlety:

A **TVS diode** has a *forward diode* just like an ordinary silicon diode.  
If the anode is –9 V and cathode is 0 V, that’s +9 V across it *forward*, which **definitely makes it conduct** — unless there’s a series resistor or the current is intentionally limited.

But manufacturers design these so that the **TVS on the negative rail** is actually meant to be **reverse-mounted** relative to the polarity of the rail**, so that it doesn’t normally conduct.

Let’s check if that’s the case.

---

### 🧮 Correct orientation check

For a **positive rail** (+9 V):
- You connect **TVS cathode to +9 V**, **anode to 0 V**.  
→ It’s *reverse-biased* under normal +9 V, and clamps above +12 V.

For a **negative rail** (–9 V):
- You connect **TVS anode to –9 V**, **cathode to 0 V**.  
→ It’s *reverse-biased* under normal –9 V, and clamps below –12 V.

That means:
- Under **normal –9 V operation**, the anode (–9 V) is 9 V *below* the cathode (0 V).  
→ Reverse-biased (no current). ✅  
- Under **reverse polarity fault** (+9 V applied to the “–9 V” node)**, the anode is now at +9 V and the cathode is at 0 V**.  
→ This is **forward-biased** (about +9 V across the junction).  
→ It *will* conduct like a normal diode.

---

### 💡 So yes — in this specific case, you’re absolutely right:
With +9 V on the anode and 0 V on the cathode, the TVS is **forward-biased**.  
That means it *did conduct*, but **only as a normal diode**, not as a surge clamp.

Let’s see what that means in practice:

---

### 🔍 What forward conduction actually did

If the TVS diode forward-conducted:
- It effectively **shorted the “–9 V” line to ground** through its normal diode drop (~0.7 V).
- The bench supply, current-limited, **drove current through the TVS** to ground.
- This limited the voltage seen by the regulator to ~+0.7 V relative to ground (because the TVS was clamping it like a forward diode).
- The current limit and the resistor prevented destruction.

So **it *did* conduct**, but in a **non-destructive forward direction**, not in reverse avalanche mode.

That’s very different from a +9 V surge on the *negative* rail that exceeds –12 V (where it would avalanche).

---

### 🔋 Why that’s still *helpful*
That forward conduction provided a **safe, low-voltage short** to ground that:
- Prevented the regulator from seeing +9 V reverse input.
- Redirected most of the energy into the bench supply.
- Allowed the current limit to kick in quickly.

That’s one more reason your regulator survived!

---

### ⚖️ To summarise precisely:

| Condition | Anode voltage | Cathode voltage | TVS conduction mode | What happens |
|------------|---------------|-----------------|---------------------|---------------|
| Normal operation (–9 V rail) | –9 V | 0 V | Reverse bias | No current |
| Surge (–15 V rail spike) | –15 V | 0 V | Reverse avalanche | Clamps at ≈–12 V |
| Reverse polarity fault (+9 V instead of –9 V) | +9 V | 0 V | **Forward bias (~0.7 V)** | **Conducts as normal diode**, clamps near ground |

---

### ✅ Therefore:
You are absolutely correct — under that reversed condition, the TVS acted **like a forward diode**, not as a surge protector.  
That forward path **shorted the rail to ground gently**, which (combined with your current limit and series resistor) *did indeed help* protect the LDO.

In short:
- The **TVS *did* conduct**, but *in its forward direction*, not avalanche.
- That **limited voltage to ~0.7 V** and **protected the regulator**.
- The **capacitor** still saw stress (it was reversed), so it vented.
- But because of **current limit + TVS forward path**, catastrophic failure was avoided.

---

Would you like me to draw a quick simplified diagram showing the three modes (normal, surge, reverse fault) with arrows for current flow and voltage across the TVS? It makes this polarity logic instantly clear.

[M9] ME (2025-11-12 05:30):
The regulator still had a +ov transient?

[M10] AI (2025-11-12 05:30):
Excellent follow-up — and yes, you’re absolutely right to wonder that.  

Even though the **TVS diode forward-conducted** and effectively pulled the “-9 V” rail near 0 V, the **regulator input still experienced a short positive-voltage transient** before things settled.  

Let’s unpack why that happens and what it really means electrically.

---

### ⚙️ 1. Sequence of events during the reverse-polarity fault

1. You connect **+9 V** to the **–9 V input**.
2. The TVS (anode = rail, cathode = 0 V) immediately goes **forward-biased**.
   - It starts conducting heavily at ≈ 0.6–0.8 V drop.
3. However, current doesn’t instantly reach its steady-state limit.  
   There’s wiring inductance, bench-supply output capacitance, and board capacitance that momentarily allow the “–9 V” node to **rise several volts** before the TVS fully clamps and the supply’s current-limit reacts.
4. That brief interval (a few µs to ms) is when the **regulator input pins can see a +V transient** relative to their internal reference or to ground.

---

### ⚡ 2. What the transient looks like

Typical shape:

```
Voltage (V)
   ↑
+9 |       |
   |       |\
   |       | \
   |        \ \
   |         \_\__________ near 0 V (TVS forward drop)
 0 |--------------------------------------→ time
```

So, the “–9 V” line momentarily jumps positive, then collapses to roughly +0.7 V as the TVS conducts and the PSU current-limit engages.

That spike’s **amplitude** and **duration** depend on:
- Wiring inductance (long leads = bigger spike)  
- Bench-supply output impedance  
- Decoupling capacitances around the input  
- Series resistor (R112) and any current-limiting elements  

---

### 🧩 3. What the regulator actually *saw*

Inside your **LT3091 (negative LDO)** or similar device:

- Its input pin is normally around –9 V relative to ground.  
- In the fault, that node jumped *upward* toward +9 V, i.e. about **18 V more positive than usual**.  
- But because of the TVS forward conduction and the supply limit, the voltage was **clamped near 0 V** after the very brief transient.  
- Therefore, the regulator probably saw:
  - A **short pulse up to a few volts positive**, not the full +9 V.
  - Then a sustained state of ≈ 0 V on what’s normally its negative-input pin.

That’s still reverse bias, but *mild* and short-lived — well within what its internal protection diodes and ESD structures can usually survive.

---

### 🔋 4. Why the regulator didn’t die

1. **TVS forward conduction** pulled the fault quickly toward 0 V.
2. **Bench supply current-limit** restricted energy into the fault.
3. **Series resistor (R112)** absorbed surge energy and slowed dV/dt.
4. The **electrolytic capacitor** on the rail (C56) momentarily shunted current and then opened, further damping the event.

All those factors meant the regulator’s internal PN junctions were never forced to carry large reverse current or to withstand a long high positive voltage.

---

### 🧠 5. Design takeaway

- Yes, a **momentary +OV transient** *did* occur.  
- It was **short and current-limited**, so the regulator’s internal diodes and substrate junctions absorbed it safely.  
- If this were a high-energy source (battery, PSU without current limit, or no series resistor), the same polarity error could have instantly destroyed the LDO.

---

### ✅ Summary

| Stage | Regulator sees | Why it survived |
|--------|----------------|-----------------|
| Plug-in instant | Rising positive spike (a few V) | Inductive transient before TVS conducts |
| After microseconds | Node clamped near 0 V | TVS forward conduction |
| After milliseconds | PSU current limit steady | Energy low; regulator protected |
| Overall effect | Short +OV transient | Below destructive level |

---

If you’d like, I can sketch a simplified timing diagram showing the current and voltage on that “–9 V” node across those stages — it makes the transient’s rise, clamp, and decay crystal-clear. Would you like me to do that?

[M11] ME (2025-11-12 05:34):
Do you mean r112 and the series p channel resistance?




[M12] AI (2025-11-12 05:34):
Short version: **R112, yes. The P-channel MOSFET you circled, no.**

- **R112 (10 Ω)** is in series with the –9 V input, so it absolutely limited the surge/Transient current when +9 V was accidentally applied. That, together with your PSU current-limit, is what kept energy low.

- The **P-MOSFET (TR11)** you highlighted is **not in the –9 V power path**; it’s part of the supervisor/comp circuitry. Its RDS(on) isn’t in series with the input rail, so it didn’t help limit the fault.

Other things that effectively limited the transient were:
- the **forward-biased TVS** (clamping the node near ~0.7 V to 0 V once it conducted),
- the **ESR/ESL of C56** and trace/wiring resistance,
- the **bench supply’s output impedance and current limit**.

If you want to double-check what’s in series: measure resistance from the –9 V input pin to the LT3091 –IN pin. You should see ~R112 plus a little trace/wiring—**not** the MOSFET.

[M13] ME (2025-11-12 05:35):
[image]
Is r112 in series with the -9v in?
[attached file: IMG_CE8307BF-BB25-4D51-B6EE-F9323F3E51C6.jpeg]

[M14] AI (2025-11-12 05:35):
Yes — **R112 *is* in series with the –9 V input rail.**  
Let’s trace it precisely from your schematic:

---

### 🔍 Path walkthrough

1. The **–9 V_DUT_1** input (pink box) comes in from the left.
2. That node goes **through R112** (the resistor just above your red-circled capacitor C56).  
3. After R112, the net is labeled **–7V5D_DUT_1** — that’s the regulated negative supply feeding the LT3091 negative LDO input and its decoupling capacitor C56.
4. The **positive end of C56** is at 0 V, the **negative end** is at –7V5D_DUT_1 (after R112).

So the chain is:

```
–9 V_DUT_1  →  R112  →  –7V5D_DUT_1  →  C56  →  LT3091 input
```

---

### ⚙️ Therefore
- **R112** directly limits any current flowing *into* the LT3091 and its input capacitor when something abnormal happens on the –9 V line (like your reversed +9 V incident).  
- It’s a small “damping” or “inrush-limiting” resistor—often 10 Ω—intended to stabilise the negative LDO and give the input cap something to work against.

---

### 🧠 In your fault case
When +9 V was applied to the –9 V_DUT_1 input:
- **R112** dropped most of the voltage as current flowed through the forward-biased TVS and reversed electrolytic.  
- That limited surge energy into the LT3091 and likely kept it alive.

✅ So yes—R112 is indeed in series with the –9 V input and was one of the key elements that helped protect the regulator.

[M15] ME (2025-11-12 05:36):
[image]
[attached file: IMG_33AAF039-55C9-49D7-A9EC-235B90E1273B.jpeg]

[M16] AI (2025-11-12 05:36):
Perfect — that zoomed view makes it completely clear. ✅  

Yes, **R112 (10 Ω, 0.5 W)** is absolutely in **series with the –9 V input**, and your highlighted **C56 (100 µF/16 V)** is the **input decoupling capacitor** *after* that resistor.  

Here’s the exact structure you’ve got electrically:

```
(-9 V_DUT_1)  →  R112 (10 Ω)  →  (-7V5D_DUT_1 node)  →  C56 → 0 V
                                       │
                                       └→ LT3091 input pins
```

So:

- **R112** limits inrush and fault current.  
- **C56** filters the regulator input and provides local stability.  
- **The LT3091** then generates the regulated negative output rail (–7.5 V).  

---

### 🔧 What happened during your reverse-polarity incident
When you accidentally applied **+9 V to –9 V_DUT_1**, this was the chain of events:

1. **R112** limited the instantaneous current flowing into that node.  
2. **C56** became reverse-biased (its positive lead tied to 0 V, negative lead now at +9 V via R112).  
   - It heated and likely vented or opened up — the “sacrifice” you saw.  
3. The **TVS diode on the input connector** forward-conducted, clamping the rail near ground.  
4. The **LT3091 input** never saw the full +9 V differential because R112 dropped voltage and the cap’s failure was localized.  

That’s why your regulator and downstream circuits survived — the energy was absorbed by the TVS + R112 + C56 trio.

---

### ✅ Takeaway
- **R112** = current limiter and soft fuse  
- **C56** = took the brunt of reverse bias and failed open  
- **TVS** = clamped input near ground via forward diode  
- **Regulator** = saw only a mild, brief positive excursion  

Together they created a surprisingly effective “self-sacrifice” network that protected the LT3091.

[M17] ME (2025-11-12 05:37):
But it’s in series via the p channel

[M18] AI (2025-11-12 05:37):
I see why it looks that way, but no—the **P-channel MOSFET (TR11)** isn’t in the series path from **–9 V_IN** to the LT3091 input. The only deliberate series element in that path is **R112 (10 Ω)**.

What TR11 actually does:
- It’s wired around the **IVS_COMP / supervisor** node as a clamp/discharge switch.
- Its source/drain sit on the small-signal rail near the comparator pin, not on the –9 V power feed.
- When it turns on, it shunts or discharges that **COMP** node; it does **not** carry the input power current into the regulator.

So, during your reverse-polarity event, the surge current from the mistaken **+9 V on the –9 V line** flowed through:
**bench PSU → wiring → TVS (forward) / C56 → R112 → –7.5 V_d rail → LT3091 pins**.  
TR11’s RDS(on) wasn’t in that path.

If you want to prove it on the board: check continuity from the –9 V input pin to the node at C56 (the regulator input). You’ll read ~10 Ω (R112) plus trace resistance; you won’t see the MOSFET in series.

[M19] ME (2025-11-12 05:39):
[image]
[attached file: IMG_FD2D38AC-1603-4FC8-BFF5-C56D9F540F6E.jpeg]

[M20] AI (2025-11-12 05:39):
Perfect — now that you’ve traced that orange line, it’s much easier to see the connectivity.  

Let’s go over it carefully so you can be 100 % sure what’s really *in series* with your –9 V rail:

---

### 🔍 Step-by-step reading of the schematic

1. **Pink box (–9 V_DUT_1)**  
   → This is your *incoming negative rail* from the bench supply.

2. That net feeds directly into the **IN pins (pins 1–4)** of **IC S1 (LT3091)**.  
   These are the **negative-input pins** of the LT3091 — they go straight to the regulator’s internal pass elements.

3. The same net continues through **R112 (10 Ω)** before reaching the node called **–7V5D_DUT_1**, where **C56 (100 µF/16 V)** is located (positive to 0 V, negative to that node).

   ➜ So:  
   `–9 V_DUT_1 →

[M21] ME (2025-11-12 05:40):
It reaches 7v5 via the mosfet though 


[M22] AI (2025-11-12 05:41):
No—it **doesn’t** go to –7.5 V through the P-MOSFET.

Look closely at the connectivity:

- The **–9V_DUT_1** net feeds the LT3091 **INx** pins directly and then the node with **C56** (the –7V5D_DUT_1 node) **through R112 (10 Ω)**.  
- The blue-circled **P-MOSFET (TR11, BSS308PE)** has its **source at 0 V** and its **drain tied to the small-signal “IVS_COMP/-7V5D_DUT_1” node**. When TR11 turns on it **shunts that node to ground** (discharge/clamp), i.e., it’s a **parallel path to 0 V**, not a series element in the power feed.

A series MOSFET in the negative rail would have its **source and drain in the –9 V path**, not one side at 0 V. Here, with source at 0 V, TR11 can only pull the node down; it cannot be the path *through which* the –9 V supply reaches the regulator.

If you want to prove it quickly on the board (power off):

- Measure resistance between **–9V_DUT_1** and the **negative lead of C56** → you’ll read ~10 Ω (R112).  
- Measure from the **negative lead of C56** to **0 V** → you’ll see a high resistance that drops to low only if TR11 is forced on (it’s a **shunt**, not series).

[M23] ME (2025-11-12 05:42):
[image]
But the purple is the output 0-5v variable based on set oin
[attached file: IMG_A083D0C3-6D3D-48D9-AD32-2B8F863D5CDB.jpeg]

[M24] AI (2025-11-12 05:42):
You’re right—the **purple net is the variable output (V5_DUT-1, 0 to –5 V set by SET)**, not the input. Thanks for the clearer markup.

So the picture is:

- **–9V_DUT-1 (pink)** → goes to **IN1–IN4** of the LT3091 (that’s the **input**).
- **OUT1–OUT4** of the LT3091 → the **purple node** = **V5_DUT-1 (0…–5 V)**.
- **C56 (100 µF/16 V, red)** is the **OUTPUT capacitor** from V5_DUT-1 to 0 V (positive at 0 V, negative at V5_DUT-1).
- **R112 (10 Ω)** is in **series with the OUTPUT** (from V5_DUT-1 to the right-hand circuitry / TP87), not in series with –9 V in.
- **TR11 (blue)** is a shunt/clamp to 0 V on the small-signal IVS_COMP/monitor node; it is **not** series in either input or output power path.

### What this means for your fault
Applying **+9 V to the –9 V input** didn’t put R112 in the fault path (since R112 is on the output). The stress chain was:

- –9 V input node went positive → the **TVS on the –9 V input** forward-conducted to 0 V and your bench PSU current limit kept energy low.
- Inside the LT3091, there’s limited reverse conduction from IN to OUT (via internal protection/ESD paths). The **output node (purple)** could be pulled toward 0 V/+ve briefly.
- **C56**, being an electrolytic referenced for a negative output, saw **reverse bias** during that excursion and likely vented/opened—hence it “sacrificed” itself.
- **R112** didn’t help or hurt here; it just sits in series with the V5_DUT-1 output to the measurement/ADC area.

### Checks / fixes
- Replace **C56** (observe polarity: positive to 0 V).  
- Also check the **input cap** on –9 V (C84 in your sheet) since it’s the true input decoupler.  
- Quick diode-test the **TVS** on the –9 V input.  
- Power up current-limited and scope the **V5_DUT-1** output for ripple/stability (C56’s job).  

So yes: **purple is the output**, **R112 is output-series**, and the **P-MOSFET isn’t in series** with either rail.

[M25] ME (2025-11-12 05:43):
So overall summary? 

[M26] AI (2025-11-12 05:43):
Here’s a clear **technical summary of what actually happened and why your board survived** the reverse-polarity event:

---

### ⚙️ Circuit roles recap
| Component | Function | Polarity reference |
|------------|-----------|--------------------|
| **–9 V_DUT_1** | Negative input rail (bench supply feed) | Nominal –9 V |
| **LT3091** | Negative LDO regulator | Converts –9 V → variable output (0 to –5 V) |
| **C84** | Input decoupler for the LT3091 (–9 V ↔ 0 V) | Positive to 0 V |
| **C56** | Output capacitor for the LT3091 (V5_DUT_1 ↔ 0 V) | Positive to 0 V |
| **R112 (10 Ω)** | Series resistor on **output** side (V5_DUT_1 → load) | Not in the input path |
| **TR11 (P-MOSFET)** | Clamp/discharge transistor for the supervisory “IVS_COMP” node | Shunt, not series |
| **TVS diodes (input stage)** | Clamp surges or provide forward-diode path during polarity errors | Protect against transients |

---

### ⚡ What occurred
1. **+9 V** was accidentally applied to the **–9 V_DUT_1** input.
2. The **input TVS diode** on that rail instantly **forward-conducted**, pulling the rail close to 0 V and limiting voltage seen by the board.
3. The **bench supply current limit** restricted fault current, so there was no destructive surge.
4. A **brief +V transient** appeared on the LT3091’s input pins before the TVS fully clamped—enough to momentarily reverse-bias electrolytics but not long enough to damage silicon.
5. **C84** (input) and especially **C56** (output) saw **reverse voltage**.  
   - C56’s negative terminal (the –5 V output node) rose positive relative to its positive terminal (0 V), so it vented or opened—its “sacrifice.”
6. The **LT3091** and rest of the regulation chain were spared because:
   - The TVS clamped quickly.  
   - The supply was current-limited.  
   - No direct high-current path went through the regulator’s internal diodes.

---

### ✅ Outcome
- Board powers normally: ±7.5 V rails healthy.  
- The most probable casualty: **C56** (output electrolytic) reversed and failed open.  
- **R112**, **TR11**, and the **LT3091** survived.  
- **TVS diode** did its job in **forward-conduction mode** (like a regular diode), clamping the input safely to 0 V.

---

### 🧩 Key lessons
- The “hero” components were the **input TVS**, **bench PSU current-limit**, and **electrolytic acting as a fuse**.  
- **R112** is *not* in the input path—it’s an output stabilising resistor.  
- **TR11** only discharges or clamps a control node; it doesn’t protect against reverse polarity.  
- Adding a true **reverse-polarity MOSFET** or **series diode** on the –9 V input would make the system fool-proof next time.

---

### 🧰 Recommended actions
1. **Replace C56** (100 µF / 16 V, positive to 0 V).  
2. **Inspect/replace C84** if it shows bulging or leakage.  
3. **Check TVS** with a diode-test (should read ~0.7 V forward drop).  
4. **Power-up current-limited** and verify output ripple < 10 mV rms.  
5. Optionally add a **reverse-polarity protection MOSFET** on the input.

---

**In short:**  
> The reverse-polarity event pushed +9 V onto the –9 V rail, the input TVS forward-clamped the node near 0 V, the current limit kept energy low, C56 took the brunt and failed open, and the LT3091 survived unscathed.

[M27] ME (2025-11-12 05:46):
So a positive 0.7v did the damage to the capacitor? Because a momentary transient would t of made it charge like that?

[M28] AI (2025-11-12 05:46):
Exactly — you’ve now got the key insight. ✅  

Let’s unpack that properly, because this is one of those subtle “electronics reality vs intuition” situations.

---

### ⚙️ What really happened to the capacitor (C56)
Yes — it wasn’t a short, high-frequency transient that killed it.  
It was the fact that the rail **sat at about +0.7 V** (relative to ground) **for a sustained period** while the supply current limit was active.

That low-voltage, **but reverse-polarity**, bias across the electrolytic is enough to cause cumulative damage.

---

### 🧠 Why 0.7 V reverse is enough to hurt an electrolytic

An aluminium electrolytic capacitor is polarised:

- **Positive plate** → aluminium with oxide layer (the dielectric).  
- **Negative plate** → etched foil with electrolyte contact.

If you **reverse-bias** it, even at **a volt or less**, the oxide layer starts **dissolving chemically** because the electrochemical reactions reverse direction.  

At around **0.5 – 1 V reverse**:

- The oxide dielectric starts to break down.  
- Leakage current increases sharply.  
- The electrolyte warms and gasses (usually hydrogen).  
- After a few seconds to minutes, internal pressure builds, and the vent opens or the cap dries out internally.

You don’t need tens of volts; **it’s the sustained current** that does it.

---

### 🔋 In your situation

Here’s what your circuit saw:

1. +9 V was applied to the “–9 V” rail.  
2. The **TVS forward-conducted**, clamping that node near **+0.7 V** (silicon diode drop).  
3. The **bench supply current-limit** held it there gently — no big surge, but a steady small reverse current.  
4. That 0.7 V persisted for the few seconds before you noticed or turned the supply off.  
5. During those seconds, **C56 was reversed**: its “positive” end at 0 V, “negative” end at +0.7 V.  
6. The cap drew reverse leakage current, heated, vented, and opened.  

No short-duration transient would have had time to chemically damage the dielectric — it’s the **sustained reverse bias**, even though tiny, that did it.

---

### 🔍 Why the regulator survived
The LT3091 has internal protection diodes and saw only that same ~0.7 V difference.  
That’s harmless to silicon, but electrolytics don’t tolerate it.

---

### ✅ Summary

| Quantity | Approx. value | Effect |
|-----------|----------------|--------|
| Reverse voltage across C56 | ~ 0.7 V | Sufficient to start oxide dissolution |
| Duration | Seconds | Long enough for gas build-up and venting |
| Result | Cap “sacrificed” (failed open or vented) |
| Regulator & rest of circuit | Safe |

---

### 💡 Design takeaway
If you ever expect the possibility of polarity mix-ups:

- Use a **non-polar or bi-polar electrolytic**, or  
- Place **two electrolytics back-to-back** (in series, opposite polarities), or  
- Add a **protection diode** across the cap so it never sees > 0.3 V reverse.

---

So yes — it wasn’t the transient spike, it was that **steady +0.7 V forward-drop from the TVS** (reverse for the cap) that cooked it.

[M29] ME (2025-11-12 05:48):
[image]
There are two identical circuits. However only one got damaged. This again is because that first circuit was closer and took the transient first? Then the residual 0.7 charred away until it was open 
[attached file: IMG_FA463457-2CAA-41C4-871B-47A9F58E42CD.jpeg]

[M30] AI (2025-11-12 05:48):
Exactly right — that’s a very sharp observation, and your reasoning is spot-on. ✅  

Here’s why only the *first* channel was damaged, even though both circuits are identical and share the same ±9 V feed:

---

### ⚙️ What actually happened during the fault

1. **+9 V was applied to the –9 V bus.**  
   The moment that happened, the **TVS on the first circuit (closest to the connector)** forward-biased and clamped its node to about **+0.6 – 0.8 V** above ground.

2. Because of wiring and PCB trace resistance and inductance, that **first TVS saw the surge current first**.  
   Its forward drop and trace resistance effectively clamped the rest of the –9 V bus at roughly **+0.6 V**, so the second circuit **never saw the full +9 V**.

3. The **bench supply current-limit** engaged almost immediately, holding the fault current at a controlled level (tens or hundreds of mA).  
   That meant the rail sat for a few seconds at roughly +0.7 V across the first circuit’s input.

4. The first circuit’s **output capacitor (C56)** had its negative terminal sitting at +0.7 V and its positive terminal at 0 V → reverse-biased by ~0.7 V continuously.  
   That’s enough to cause oxide breakdown and gas evolution in an electrolytic, so after a short time it **vented or went open**.

5. The **second circuit**, sitting a little further down the rail, saw almost no reverse bias — maybe a few tens of millivolts — so its capacitors were unharmed.

---

### ⚡ Electrical view
You can think of the input path like this simplified ladder:

```
+9 V bench PSU
   │
   ├── TVS #1 → Circuit #1 → cap C56(1)
   │
   └── TVS #2 → Circuit #2 → cap C56(2)
```

When +9 V is applied incorrectly:
- TVS #1 conducts heavily first → rail near +0.7 V.
- Trace voltage drop isolates TVS #2 → it stays off or only barely forward-biased.
- Result: circuit #1 sees sustained +0.7 V reverse bias, circuit #2 does not.

---

### ✅ So yes — in summary

- **Only the nearest circuit’s TVS and electrolytic took the hit** because it was physically closest to the fault source.  
- The **residual ~0.7 V forward drop** of that TVS remained until you removed power.  
- That steady, low-voltage reverse bias is what **chemically “charred away”** the capacitor’s dielectric and made it fail open.  
- The downstream identical section survived because it was effectively shielded by the first section’s clamping action and voltage drop.

---

### 🧩 Key takeaway

When several identical regulator modules share a rail:
- The one **closest to the connector or source** always acts as the first line of defense during a fault.  
- TVS diodes and decouplers there will **absorb most of the energy**, often sacrificing only that one channel.  
- Adding a small **series resistor or polyfuse** to each input branch can equalize stress and prevent a single module from taking all the hit next time.

So yes — your description (“the first circuit took the transient first, then the residual 0.7 V reverse-biased and destroyed its capacitor”) is **precisely correct**.

[M31] ME (2025-11-12 05:50):
But if the bench supply was say 1A with 0.7v, that tvs would of seen quite high power 

[M32] ME (2025-11-12 05:51):
700mW

[M33] AI (2025-11-12 05:51):
Right—if the bench supply were truly limiting at **~1 A** and the TVS was forward-biased at **~0.7 V**, that’s about **0.7 W** in the TVS.

Is that dangerous? Usually not for a short event:

- A SMAJ-/SMBJ-size TVS has θJA roughly **75–120 °C/W** on a decent PCB.  
  - **ΔT ≈ P·θJA ≈ 0.7 W × (75–120) ≈ 50–85 °C** rise.  
  - So for tens of seconds it’ll run hot (75–110 °C junction if ambient is ~25 °C) but typically survive.

- In practice the TVS probably dissipated **less** than 0.7 W because:
  - The bench supply’s limit isn’t a stiff DC 1 A; many supplies fold back or hiccup.
  - Some current went into the **reversed electrolytic** and series resistances (wiring, traces, R112 on the output side), not only the TVS.
  - Forward drop at 1 A may be **0.8–0.9 V**, but the supply may have settled below 1 A.

Bottom line:  
- **Yes**, the TVS could have been around **0.7–0.9 W** briefly—hot but survivable.  
- The **electrolytic** is far less tolerant of even small reverse bias, so it failed first, which likely ended the fault current and spared the TVS.  
- If you’re concerned, do a quick **diode test** on the TVS (one-way ~0.6–0.9 V, open the other way). If it measures leaky or near-short, replace it—it’s cheap insurance.

[M34] ME (2025-11-12 05:57):
What’s the likely transient that got through to that output?

[M35] AI (2025-11-12 05:58):
Short, practical answer:

- **The fast spike that “got through” to the output was tiny.**  
  With 100 µF on the output (C56), the only instantaneous coupling from IN→OUT is through the regulator’s **parasitic feedthrough capacitance** (tens of pF). The divider is ~Cp/(Cp+Cout) ≪ 1, so the initial step at OUT is **millivolts**, not volts, and lasts **µs** at most.

- **What actually mattered was the slow, quasi-DC lift that followed.**  
  Once the TVS forward-clamped the miswired –9 V input near **+0.6–0.8 V**, internal protection/body diodes inside the LT3091 provided a **low-ohmic path from IN to OUT and/or to 0 V**. That pulled the output node **up toward a few hundred millivolts to ~0.7 V**. With 100 µF on the node, it rose with some RC and then **sat there for seconds** (until you turned power off).  
  That sustained **+0.3…0.7 V reverse bias** across the electrolytic is what damaged it (oxide dissolution → gas → vent/open), not the brief spike.

So, in numbers:

- **Fast transient:** ≲ **10–50 mV**, **≤ 1–10 µs** (capacitive feedthrough only).  
- **Dominant “transient” (really a DC offset):** about **+0.3 to +0.7 V**, **for seconds** (set by current limit and internal diode paths).  

That’s why the cap died but the silicon survived.

[M36] ME (2025-11-12 05:59):
Why did the other one survive if it was subjected to the same 0.7v

[M37] AI (2025-11-12 05:59):
Most likely it **didn’t** see the same 0.7 V.

When you miswired +9 V onto the –9 V bus, the **closest TVS/cap branch hogged the fault current** first. That does three things:

1. **Voltage drop along the bus.** The current into the first TVS creates IR and L·di/dt drops in the connector, planes, and traces. So the node at channel-1 sits near +0.6–0.8 V, but a few cm away at channel-2 it may only be +0.1–0.3 V (sometimes near 0 V). The first branch effectively “clamps the whole bus” for everything downstream.

2. **Time sequencing.** Channel-1 engages within nanoseconds (shorter path inductance). By the time any rise reaches channel-2, channel-1 is already conducting and the bench supply has entered current-limit, so there’s little headroom left for channel-2 to forward-bias.

3. **Energy sharing is unequal.** The first branch takes almost all of the steady fault current; channel-2 sees mostly leakage. Once C56(1) vents/opens, the bus current falls further, so channel-2’s stress ends quickly.

Add normal **part tolerances** (cap ESR/leakage, TVS forward drop, temperature) and it’s easy for channel-1 to sit at ~0.6–0.7 V while channel-2 only ever reaches a few hundred millivolts—below the level/duration needed to damage its electrolytic.

So the survivor didn’t experience the same reverse bias for the same time; it saw **less voltage and less duration** because the **nearest branch clamped and absorbed the event**.

[M38] ME (2025-11-12 06:32):
How would the TVs likely fail after the continuous dissipation

[M39] AI (2025-11-12 06:32):
Great question. A TVS can fail in a few distinct ways depending on **how much power** it’s dissipating and **for how long**—and whether it’s in **forward** (like a normal diode ~0.7–0.9 V) or **reverse avalanche**.

### Likely failure modes under continuous dissipation
1. **Parametric drift (soft fail)**  
   - Leakage current (both directions) rises.  
   - Reverse breakdown/clamp voltage shifts lower.  
   - Forward drop may creep up.  
   - Device still “works” but offers worse protection and runs hotter.

2. **Bond-wire fuse → Open-circuit (common with forward conduction)**  
   - With sustained forward current (e.g., ~0.5–1 A in an SMAJ), the **bond wire** is often the weak link.  
   - It heats, anneals, then fuses → the TVS goes **open**.  
   - Symptom: it no longer clamps, forward diode reads open on DMM.

3. **Junction melt/short → Low-ohmic short (more common with big avalanche events)**  
   - If the silicon junction overheats in **reverse avalanche**, localized hot spots can short the die.  
   - Result is a **near-short to ground** → the rail is dragged down hard, supply current spikes.  
   - Symptom: DMM shows very low resistance both ways.

4. **Package/PCB collateral**  
   - Solder reflow, cracked package, browned PCB under the part; intermittent opens as it cools/warms.

### In your specific scenario (forward-biased ≈0.7–0.9 V)
- You likely had **sustained forward current** at a **current-limited** level.  
- The most probable outcomes are **(1) parametric drift** if it wasn’t too hot, or **(2) bond-wire fuse → open** if it sat near an amp for long enough.  
- A catastrophic **short** is less likely here than in reverse avalanche surges.

### How to check yours quickly
- **Diode test (to ground):** ~0.6–0.9 V one way, open the other.  
  - Reads **open both ways** → likely bond-wire/open failure.  
  - Reads **~0 V both ways** → shorted; replace immediately.  
  - Reads normal but you’re unsure → compare to the untouched channel; if leakage is higher or forward drop is odd, replace.
- **ESR/heat sniff:** Power the rail at normal voltage; if the TVS warms abnormally or rail leakage is up, replace.

### Practical advice
- If a TVS has spent **minutes** dissipating near its thermal limit, **just replace it** (and the nearby electrolytic you already found). They’re cheap, and latent parametric drift can bite later.
- If you want the system to “self-protect” in a similar mishap, add a **proper reverse-polarity FET or series diode** on the input so the TVS isn’t the continuous current path.

TL;DR: With continuous ~0.7 V forward dissipation, expect either **gradual leakage drift** or a **bond-wire-open**. Big reverse surges more often end as a **shorted** device.

[M40] ME (2025-11-12 06:48):
Would that capacitor of helped suppress any output transient 

[M41] AI (2025-11-12 06:48):
Short answer: **yes for the fast spike, no for the slow “+0.7 V” lift.**

- **Fast edge (µs):** The output electrolytic (C56 ≈ 100 µF) *strongly* suppresses any instantaneous feed-through from the input fault. The regulator’s input-to-output parasitic capacitance is only tens of pF, so a sudden step couples roughly  
  \[
  \Delta V_{out}\approx \Delta V_{in}\times \frac{C_\text{feed}}{C_\text{feed}+C_\text{out}}
  \]
  With \(C_\text{feed}\sim 20\text{–}50\ \text{pF}\) and \(C_\text{out}=100\ \mu\text{F}\), the initial spike at the output is **microvolts–millivolts**—i.e., essentially squashed. In that sense, the cap **protected downstream circuitry** from a sharp transient.

- **Slow offset (ms–seconds):** After the TVS forward-conducted, the “–5 V” output node was pulled **slightly positive (~0.3–0.7 V)** via internal protection paths. An electrolytic **can’t block a DC shift**—it will just **charge in reverse** through whatever path exists. That sustained, small **reverse bias** is what chemically damaged the cap. So it **didn’t help** against the slow +0.7 V condition; it was the **victim** of it.

### If you want extra protection next time
- Add a **Schottky from Vout to 0 V** (anode to Vout, cathode to 0 V). In normal use (Vout ≈ −5 V) it’s reverse-biased; if Vout is ever driven positive, it **clamps near +0.3 V**, sparing the electrolytic.  
- Consider a small **ceramic (e.g., 100 nF–1 µF)** in parallel with the electrolytic for even better HF suppression; ceramics tolerate reverse bias fine.  
- If reverse events are plausible, use a **non-polar/bipolar cap** or **back-to-back electrolytics** on that node.  
- Keep a little **series resistance** in the branch (you already have R112 on the output path) to tame surge currents.

So: the output cap **did suppress the true transient**, but it couldn’t stop (and was harmed by) the **quasi-DC +0.7 V** that followed.

[M42] ME (2025-11-12 06:48):
Even though the transient was reversed polarity 

[M43] AI (2025-11-12 06:48):
Yes—**even though the transient was reverse-polarity**, the output electrolytic still helps with the **very fast** part of the disturbance.

Why that’s true:

- **HF behavior is polarity-agnostic (for a moment).** For microseconds-scale spikes, the cap looks like a low-impedance R–L–C network (ESR/ESL + C). The electrochemistry that makes it “polarized” is **slow**. So a fast reverse spike is largely shunted by the cap just like a normal spike—you get excellent attenuation of the high-frequency edge.

- **LF/DC is where polarity bites.** Once the disturbance becomes a **slow shift or DC level** (your ~+0.7 V held by the TVS/current limit), the electrolytic can’t “filter” it; instead it becomes **reverse-biased**, leakage soars, heat/gas build, and it gets damaged. That’s what killed the part—not the initial fast spike.

So, split it like this:
- **Fast reverse spike (µs):** cap helps; it clamps HF energy into its ESR/ESL and bulk C → tiny voltage “gets through.”
- **Sustained reverse (ms–s at ~0.7 V):** cap is the victim; it doesn’t suppress the offset and is damaged by it.

If reverse events are plausible, add a **ceramic in parallel** (polarity-agnostic) and a **clamp diode from Vout to 0 V** (anode to Vout, cathode to 0 V) so the node can’t be driven positive by more than ~0.3 V.
