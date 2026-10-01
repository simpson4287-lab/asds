# Differential amplifier gain
Date (UTC): 2025-10-12 17:50
Conversation ID: 68ebea77-ac58-832e-bd8d-db436d6568b9
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-000.json

[M1] ME (2025-10-12 17:50):
How to work out gain of differential amplifier


[M2] AI (2025-10-12 17:51):
Here are the common cases and the quick formulas you’ll actually use.

# 1) Op-amp differential amplifier (the 4-resistor diff amp)

```
     R2                  R4
V2 ──/\/\/─+──(–)   (+)──/\/\/── V1
           |    \   /              (ideal op-amp)
           +----[OP-AMP]---- Vout
           |    /   \
     R1    |          |
GND ─/\/\/─+          +─ GND via R3
```

If the resistor **ratios are matched**:  
**R2/R1 = R4/R3 = K**, then the **differential gain** is

\[
V_{out} = K\,(V_2 - V_1) \quad \Rightarrow \quad A_d = K = \frac{R_2}{R_1}
\]

That’s the classic result. The common-mode gain is ~0 (set by mismatch and the op-amp’s CMRR).

If ratios **aren’t** matched, use:

\[
V_{out} = \left(\frac{R_2}{R_1}\right) V_2 - \left(\frac{R_4}{R_3}\right) V_1
\]
plus a small common-mode term due to the mismatch. In practice, trim or use 0.1% resistors.

**Example:** R1=10 k, R2=100 k, R3=10 k, R4=100 k → \(A_d=100k/10k=10\).  
With \(V_2=120\,\text{mV}\), \(V_1=100\,\text{mV}\): \(V_{out}=10\cdot(20\,\text{mV})=0.2\,\text{V}\).

---

# 2) Instrumentation amplifier (3-op-amp INA)

For the common INA topology (two buffers + diff stage), the **gain-set resistor \(R_G\)** sets the first stage gain:

\[
A_{stage1} = 1 + \frac{2R}{R_G}
\]

The second (diff) stage usually has gain \(R_2/R_1\).  
Total gain:

\[
A_{total} = \left(1 + \frac{2R}{R_G}\right)\left(\frac{R_2}{R_1}\right)
\]

(Vendors often fix \(R_2=R_1\) so the second factor is 1.)

---

# 3) BJT/MOS differential pair (long-tailed pair)

Small-signal **per-side (single-ended) gain** for a BJT pair with collector resistor \(R_C\):

- Each base sees ±\(v_d/2\) where \(v_d = v_2 - v_1\) (differential input).
- With transconductance \(g_m \approx 1/r_e\) (and \(r_e \approx 25\,\text{mV}/I_C\) at room temp):

\[
A_{single} \equiv \frac{v_{out}}{v_d} \approx -\frac{g_m R_C}{2} \;=\; -\frac{R_C}{2r_e}
\]

**Differential output** (taking the difference of both collectors) doubles it:

\[
A_{diff\text{-}out} \equiv \frac{(v_{o2}-v_{o1})}{v_d} \approx -g_m R_C \;=\; -\frac{R_C}{r_e}
\]

Include emitter degeneration \(R_E\) by replacing \(g_m\) with \(g_m/(1+g_m R_E)\).

**Example:** Tail gives \(I_C \approx 0.5\,\text{mA}\) per side → \(r_e \approx 25\,\text{mV}/0.5\,\text{mA}=50\,\Omega\).  
With \(R_C=5\,\text{k}\Omega\):  
Single-ended \(A \approx -5000/(2\cdot 50) = -50\).  
Differential-out \(A \approx -5000/50 = -100\).

---

## Practical steps to “work it out” on your circuit

1) **Identify the topology** (op-amp 4-resistor diff, INA, or transistor pair).  
2) **Write the gain from the right formula above.**  
3) **Include real-world effects** if needed:
   - **Resistor mismatch/CMRR:** use 0.1% parts or laser-trim; mismatch creates common-mode gain.
   - **Op-amp limits:** input common-mode range, open-loop gain/GBW, output swing, input bias currents.
   - **Source impedance:** for the 4-resistor diff amp, keep source impedances low/equal or add matching resistors.
   - **Bandwidth/noise:** gain trades against bandwidth and noise (especially in INAs).

---

## Extra: using a CCD dummy output
When you use a **dummy output** to cancel clock feedthrough, you typically feed **signal** to \(V_2\) and **dummy** to \(V_1\) (or vice-versa) into the diff stage. The **gain is exactly the same** formulas as above; the dummy just improves common-mode rejection by making the unwanted feedthrough appear on both inputs so it cancels. Ensure your resistor **ratios** (or INA gain set) are tight to preserve CMRR at the CCD clock frequencies.

---

If you tell me your exact resistor values (or tail current/RC for a transistor pair), I’ll calculate the numeric gain for your specific build.

[M3] ME (2025-10-12 17:51):
Give me more detail on the op amp option . Use schematic symbols

[M4] AI (2025-10-12 17:52):
Got it—let’s zoom in on the classic **4-resistor op-amp differential amplifier** and do it properly, with symbols, formulas, matching rules, and a worked example.

# Schematic (ASCII symbols)

```
          R2                           R4
V2 ────/\/\/\───┐               ┌───/\/\/\─── V1
                │               │
               (–)             (+)
                │   ┌──────────┴──────────┐
                └──▶│        OP-AMP       │
                    │                    ▷│── Vout
                ┌───┴──────────┬──────────┘
                │              │
               GND            / \
                              R3
                              \ /
                              GND

Inverting leg:    V2 → R2 → (–) node, feedback R1 from Vout to (–)
Non-inverting leg: V1 → R4 → (+) node, divider R3 from (+) to GND
```

(For clarity: the feedback resistor **R1** goes from **Vout** back to the (–) input; I drew it implicitly in the op-amp block. Many people redraw with R1 shown explicitly: Vout ─/\/\/\─ to the (–) node.)

# Exact gain (ideal op-amp)

General case (no assumption of matching):

\[
V_{out} \;=\; \underbrace{\left(\frac{R_2}{R_1}\right)}_{\text{inverting gain}}\,V_2\;-\;\underbrace{\left(\frac{R_4}{R_3}\right)}_{\text{non-inverting gain}}\,V_1
\]

If you **ratio-match** the network so that
\[
\frac{R_2}{R_1}=\frac{R_4}{R_3}=K,
\]
then
\[
\boxed{V_{out}=K\,(V_2 - V_1)} \quad\Rightarrow\quad A_d=K.
\]

# Where that comes from (quick derivation)

1) Non-inverting side acts as a divider: \(V_{+}=V_1\cdot\frac{R_3}{R_3+R_4}\).  
2) Op-amp forces \(V_{-}\approx V_{+}\) (ideal, with negative feedback).  
3) Inverting network is a standard inverting amp referenced to \(V_{-}\):

\[
V_{out} = V_{-} - \frac{R_2}{R_1}\,(V_2 - V_{-}).
\]

Substitute \(V_{-}=V_{+}\) and the divider expression, rearrange → the general formula above. With matched ratios, terms collapse to \(K(V_2-V_1)\).

# Input impedances (what each source “sees”)

- **V2 (inverting input):** sees approximately **\(R_2\)** (node is a virtual ground).  
- **V1 (non-inverting input):** sees **\(R_4\) in series with \(R_3\)** (op-amp input ≈ open), so ≈ **\(R_4 + R_3\)**.

If you need high input Z on both, use an **instrumentation amplifier** topology instead.

# Common-mode rejection & resistor matching

Let the intended ratio be \(K\). Suppose small fractional mismatch ±ε between the two ratio pairs:
\[
\frac{R_2}{R_1}=K(1+\varepsilon), \qquad \frac{R_4}{R_3}=K(1-\varepsilon).
\]

Then, writing inputs as **diff** and **CM**:
\[
V_d = V_2 - V_1,\qquad V_{cm}=\frac{V_2+V_1}{2},
\]
you get (to first order):
\[
V_{out} \approx K\,V_d \;+\; K\,\varepsilon\,V_{cm}.
\]

So the **common-mode gain** is \(\approx K\varepsilon\), and the **CMRR** (ratio) is
\[
\text{CMRR} \approx \frac{A_d}{A_{cm}} \approx \frac{K}{K\varepsilon}=\frac{1}{\varepsilon}.
\]
In dB: \(\text{CMRR}_{dB}\approx 20\log_{10}(1/\varepsilon)\).  
With **0.1%** ratio matching (ε≈0.001): CMRR ≈ **60 dB**. With 0.01%: ≈ **80 dB**.  
Use **matched resistor networks** or laser-trim for good CMRR.

# Bias currents & offset (simple fix)

Op-amp input bias currents create an offset if the **DC resistances** seen by the (+) and (–) inputs differ. Rule of thumb:

\[
R_{\text{seen at }(+)} \; \approx \; R_3 \parallel \infty \;+\; R_4 \approx R_3 + R_4
\]
\[
R_{\text{seen at }(-)} \; \approx \; R_1 \parallel R_2.
\]

Try to **equalize** them:
\[
R_1 \parallel R_2 \;\approx\; R_3 + R_4.
\]
If not feasible, add a small **balance resistor** in series with the non-inverting node to equalize DC resistance.

# Frequency response & stability

- Keep resistor values **moderate** (e.g., 2 k–100 k) to limit noise/offset yet not overload the op-amp with capacitances.  
- For wideband/fast parts, add **matching capacitors** \(C_1\) across \(R_1\) and \(C_4\) across \(R_4\) so the **two ratio networks track with frequency**:
  \[
  \frac{R_2 \parallel \frac{1}{sC_1}}{R_1 \parallel \frac{1}{sC_1}} \;=\;
  \frac{R_4 \parallel \frac{1}{sC_4}}{R_3 \parallel \frac{1}{sC_4}} = K.
  \]
- Ensure your op-amp’s **GBW** exceeds \(A_{noise}\times f_{-3dB}\) (noise gain here is roughly \(1+R_2/R_1\) around the inverting loop).

# Noise (quick sense-check)

- Inverting leg contributes \(e_n\) shaped by the inverting gain and **\(R_2\)** thermal noise; non-inverting leg contributes via the divider (\(R_3\|R_4\)).  
- If low noise matters, use **lower resistor values** and a **low-noise op-amp**; keep the two networks symmetric so CM noise cancels well.

# Design recipe (step-by-step)

1) Choose desired **differential gain** \(K\).  
2) Pick comfortable resistor magnitudes (e.g., **R1 = R3 = 10 kΩ**).  
3) Set **R2 = K·R1**, **R4 = K·R3**.  
4) Make **\(R_1\parallel R_2 \approx R_3+R_4\)** (tweak values or add a small series resistor on the + side to balance bias currents).  
5) Use **0.1% (or better) matched** resistors, preferably from the **same network** package.  
6) If bandwidth/CMRR at high frequency matters, add **matching caps** across R1 and R4.  
7) Check op-amp: **input common-mode range** must include your \(V_1,V_2\) span; **output swing** must cover \(K(V_2-V_1)\).

# Worked example

**Goal:** \(A_d = 20\). Inputs around mid-supply; modest bandwidth.

- Choose \(R_1 = R_3 = 4.99\,\text{k}\Omega\) (1%).  
- Then \(R_2 = R_4 = 20 \times 4.99\,\text{k} \approx 100\,\text{k}\Omega\) (use 0.1% for R2/R1 and R4/R3 ratio matching).
- Input impedances: \(Z_{in}(V_2)\approx 100\,\text{k}\Omega\), \(Z_{in}(V_1)\approx 100\,\text{k}+4.99\,\text{k}\approx 105\,\text{k}\Omega\).
- Bias balance: \(R_1\parallel R_2 \approx 4.75\,\text{k}\Omega\). Non-inverting DC resistance ≈ \(R_3+R_4 \approx 105\,\text{k}\Omega\) → very unequal.  
  Add a **series resistor \(R_B\)** between the op-amp **(+)** pin and the R3/R4 junction so the op-amp “sees” \(R_B \parallel \infty\). Choose \(R_B \approx R_1\parallel R_2 \approx 4.7–4.75\,\text{k}\Omega\). This reduces input-bias-current-induced offset.
- If HF CMRR matters, place ~**10 pF** across **R1** and the **same** across **R4** (tune as needed).

**Result:** \(V_{out}\approx 20\,(V_2 - V_1)\) with strong common-mode rejection, provided the two **ratios** track.

# Practical tips

- Layout: route the two input legs **symmetrically**, keep them short, guard the + input if very high impedance, and keep clock lines (e.g., from CCD systems) away from the diff nodes.  
- Power & headroom: for single-supply parts, shift inputs so they sit well inside the valid **input common-mode** window; rail-to-rail parts are helpful but still check datasheets.  
- When CM range is large or source impedances are high/unequal, an **instrumentation amplifier** (3-op-amp INA) is often a safer choice.

If you want, tell me your **target gain** and any **resistor constraints** (range, noise, input Z), and I’ll spit out a ready-to-build value set (including a bias-balance resistor and optional HF caps).

[M5] ME (2025-10-12 17:55):
Why would a capacitor be across r2 Inc.


￼
￼







[M6] AI (2025-10-12 17:55):
Excellent question — this one goes right to the heart of **stability and frequency balance** in op-amp differential amplifiers.  
Let’s unpack it properly, because it’s not just a “throw-in-a-cap” trick — it has a real engineering purpose.

---

## 🧩 Context

We’re talking about a **resistor \( R_2 \)** (the feedback resistor in the *inverting* path of a differential amplifier).

```
            R2
 V2 ────/\/\/\───┐
                 │
                (–)
                 │\
                 │ \
                 │  \____ Vout
                 │  /
                 │ /
                 │/
                 │
                GND
```

Sometimes, you’ll see a small **capacitor placed in parallel with \( R_2 \)** — i.e.

```
            R2
 V2 ────/\/\/\───┬─────┐
                 │     │
                 │    === C2
                 │     │
                (–)    │
                 │\    │
                 │ \   │
                 │  \__┘
                 │  /
                 │ /
                 │/
                 │
                GND
```

That little capacitor \( C_2 \) (sometimes called a **“feedback capacitor”** or **“compensation capacitor”**) changes how the op-amp responds at higher frequencies.

---

## ⚙️ 1. The main purpose — *stability & phase compensation*

The op-amp’s open-loop gain falls with frequency, and there’s always some phase lag.  
At high frequency, the feedback network (formed by \( R_1, R_2 \)) can add **extra phase shift** if the input or stray capacitances interact with those resistors.  
If the phase shift approaches 180° while there’s still loop gain, you get **oscillation** or ringing.

Adding a capacitor across \( R_2 \):

- **Reduces the feedback impedance** as frequency increases (the cap starts to short R2).  
- This increases the **amount of feedback** at high frequencies.  
- That, in turn, **reduces closed-loop gain** at HF and **improves stability** (more phase margin).

Essentially, it **rolls off** the amplifier’s response slightly to tame high-frequency noise or instability.

---

## ⚖️ 2. When used in *differential amplifiers*

In a 4-resistor differential amplifier, there are *two ratio networks*:

```
Inverting:      R1 (to output) and R2 (to V–)
Non-inverting:  R3 (to ground) and R4 (to V1)
```

To preserve **good common-mode rejection** across the frequency band, both sides must have **matching impedance vs. frequency**.

So:

> ✅ If you put a capacitor across R2,  
> you should put an **equal capacitor across R4**.

That way, both ratio pairs \( R_2/R_1 \) and \( R_4/R_3 \) track not just in DC value, but in their **frequency-dependent impedance**, so the CMRR stays high across frequency.

---

## 📉 3. The effect on frequency response

At low frequencies, \( C_2 \) is effectively open → no effect.  
At higher frequencies, its reactance \( X_C = \frac{1}{2\pi f C_2} \) becomes smaller → it shunts R2.

That creates a **pole** in the closed-loop transfer function around

\[
f_p \approx \frac{1}{2\pi R_2 C_2}.
\]

Above \( f_p \), gain falls at roughly −20 dB/decade.

So \( C_2 \) defines the **high-frequency roll-off** (a low-pass filter).  
Engineers often pick \( f_p \) well above the signal band but below the region where op-amp phase shift becomes troublesome.

---

## 💡 4. Other secondary reasons

- **Noise reduction:** It filters out high-frequency noise pickup (e.g. EMI from switching signals, CCD clocks, digital logic).  
- **Charge injection control:** In circuits reading sensors (like CCDs or photodiodes), it smooths fast transients.  
- **Differentiator tamer:** If the circuit around the inverting input behaves like a differentiator, this capacitor “tames” it so it doesn’t amplify noise like crazy.

---

## 🧮 5. How to choose the value

Rough design guide:

1. Estimate your signal bandwidth \( f_{signal,max} \).
2. Choose \( f_p \) about **5–10× above** that (so it doesn’t hurt your desired band).  
   \( f_p = \dfrac{1}{2\pi R_2 C_2} \)
3. Solve for \( C_2 \).

Example:

- \( R_2 = 100\text{kΩ} \)
- Want \( f_p = 100\,\text{kHz} \)
\[
C_2 = \frac{1}{2\pi R_2 f_p} \approx \frac{1}{2\pi \times 100k \times 100k} = 15.9\text{ pF}.
\]
→ Pick a 15 pF or 18 pF NP0 ceramic.

---

## 📊 6. Summary table

| Function | Effect of C across R2 |
|-----------|----------------------|
| Stability | Adds HF negative feedback, improves phase margin |
| CMRR (HF) | Keeps both resistor networks tracking if same C on R4 |
| Noise     | Filters high-frequency noise & pickup |
| Bandwidth | Creates low-pass roll-off at \( f_p = 1/(2πR_2C_2) \) |
| Trade-off | Too large → loss of bandwidth; too small → no effect |

---

## 🧠 Rule of thumb
> A capacitor across R2 is **not for DC gain**, but for **AC behaviour** — it stabilises, filters, and ensures matched frequency response.

---

If you’d like, I can show you the **Bode plot** and **phase margin effect** with and without that capacitor (using example R2, op-amp GBW, etc.), to see exactly how it stabilises the loop.  
Would you like me to plot that?

[M7] ME (2025-10-12 17:55):
[image]
[attached file: 53CE20AC-13C6-4D13-94A7-4A59F53FEB4D.jpeg]

[M8] AI (2025-10-12 17:55):
Perfect — yes, that image you’ve shared shows the **classic four-resistor op-amp differential amplifier**.  

Let’s break *that exact circuit* down carefully, then explain where and why a **capacitor across R₂** might be added in that version.

---

## 🧩 Circuit anatomy (matching your image)

```
          R2
Vout ◄──/\/\/──┐
               │
              (–)
Vin1 ──/\/\/───┘
       R1

Vin2 ──/\/\/───┐
       R3       │(+)
                 │
                / \
               /   \
              /_____\
                |
               / \
               R4
               \ /
                |
               GND
```

- **R1 and R2** form the **inverting network**  
- **R3 and R4** form the **non-inverting divider**
- The op-amp amplifies the **difference** between Vin2 and Vin1.

When:
\[
R1 = R3, \quad R2 = R4,
\]
the **differential gain** is:
\[
V_{out} = \frac{R2}{R1} (V_{in2} - V_{in1})
\]
and ideally all common-mode voltage (anything equal on both inputs) is rejected.

---

## ⚡ Where the capacitor goes

Now, that optional capacitor is connected **in parallel with R2** — like this:

```
          R2
Vout ◄──/\/\/──┬───────┐
               │       │
               │      === C2
               │       │
              (–)      │
Vin1 ──/\/\/───┘       │
       R1               │
                        │
Vin2 ──/\/\/───┐        │
       R3       │(+)
                 │
                / \
               /   \
              /_____\
                |
               / \
               R4
               \ /
                |
               GND
```

---

## 🧠 Why that capacitor is added

### 1️⃣ Stability improvement
At high frequencies, parasitic capacitances on the inputs and feedback network can cause the op-amp to lose phase margin (risk of oscillation).  
Adding \( C_2 \) across \( R_2 \) lowers the **feedback impedance** at high frequency — giving the op-amp **more negative feedback** in that region and **smoothing the response**.

Result → less ringing, less overshoot, and stable operation.

---

### 2️⃣ Common-mode tracking (for high-frequency CMRR)
In the differential amplifier, both the inverting and non-inverting networks should have the *same impedance ratio versus frequency*.

So if you add \( C_2 \) across \( R_2 \), you should also add an identical capacitor \( C_4 \) across \( R_4 \).

That keeps both sides frequency-balanced → the differential gain stays constant, and the common-mode rejection stays high across the frequency band.

---

### 3️⃣ High-frequency noise filtering
\( C_2 \) and \( R_2 \) form a **low-pass filter**.  
Above the cutoff frequency \( f_c = 1/(2\pi R_2 C_2) \), the op-amp’s closed-loop gain rolls off.

This is useful to:
- filter out RF or switching noise from the inputs
- reduce the gain for unwanted high-frequency signals (e.g., EMI from digital logic or CCD clocks)

---

### 4️⃣ Typical values and design rule

You choose \( C_2 \) so that its cutoff is **above the signal bandwidth** but **below the instability or noise region**.

Example:

| Parameter | Value |
|------------|-------|
| R2         | 100 kΩ |
| Desired corner \( f_c \) | 100 kHz |
| \( C_2 = 1/(2π·R_2·f_c) \) | ≈ 16 pF |

Use a small NP0/C0G ceramic capacitor (very stable, low loss).

If you also match it with one across R4, use the same 16 pF part.

---

## ⚙️ Summary of purpose

| Reason | Effect of capacitor across R2 |
|--------|-------------------------------|
| Stability | Improves phase margin, prevents oscillation |
| HF CMRR | Keeps both ratio networks matched vs. frequency |
| Noise | Filters high-frequency noise and spikes |
| Bandwidth control | Sets upper cutoff frequency |
| Limitation | Too large a cap will reduce signal bandwidth |

---

If you’d like, I can calculate the **exact cutoff and Bode-plot behaviour** for your chosen resistor values (R1–R4) and show how adding that capacitor changes the gain/phase curves.  

Would you like me to do that next?

[M9] ME (2025-10-12 17:57):
What about in terms of a ccd output amplifier

[M10] AI (2025-10-12 17:58):
Great question. With a **CCD output chain**, the little capacitors around the 4-resistor differential amp aren’t just “nice to have”—they’re doing real work against the CCD’s fast clocks, big parasitic caps, and reset/feedthrough spikes.

Here’s how to think about it.

# What a CCD output looks like
- The CCD usually drives a **source follower** with **several pF–tens of pF** at the node.
- You see **clock feedthrough** and **reset transients** riding as a **common-mode** burst on both the signal and the dummy output.
- Your diff amp is there to **subtract the dummy from the signal** and give gain, while keeping **CMRR** high at the clock rates.

# Where the capacitors go—and why

## 1) Small caps across the *ratio resistors* (R2 and R4)
Place a capacitor **in parallel with R2** (inverting leg) and **an equal capacitor across R4** (non-inverting leg):

- Purpose: **HF symmetry + stability**. These caps make the two resistor *ratios* track with frequency so CMRR stays high even at the CCD clock edges.  
- Side effect: creates a **low-pass** in the closed-loop gain:
  \[
  f_{p,R2} \approx \frac{1}{2\pi R_2 C_{R2}},\qquad
  f_{p,R4} \approx \frac{1}{2\pi R_4 C_{R4}}
  \]
  Choose \(C_{R2}=C_{R4}\) so both corners match.
- Why it helps CCDs: you intentionally **reduce HF gain** for out-of-band junk (clock feedthrough/RF) while preserving in-band video.

**Rule of thumb:** set these poles **above** your video band but **below** the region where the op-amp’s phase margin gets marginal—typically **3–10× your required signal bandwidth**.

---

## 2) (Often more important) a small cap across the **feedback resistor** R1
Many CCDs present **large input capacitance** to the inverting node. That cap + R2 makes a pole that adds phase lag; a small cap across **R1** introduces a **zero** that cancels it (classic lead compensation).

- Choose \(C_{R1}\) so the **zero** roughly cancels the input-cap pole:
  \[
  f_{z} \approx \frac{1}{2\pi R_1 C_{R1}} \;\;\approx\;\; \frac{1}{2\pi R_{source\to(-)}\,C_{in}}
  \]
  where \(R_{source\to(-)}\) is the resistance from your CCD/dummy source into the inverting node (usually \(R_2\)) and \(C_{in}\) is the sum of CCD node + op-amp input + stray.
- Why it helps: restores **phase margin** (avoids peaking/oscillation) without crushing bandwidth.

If you use this R1 capacitor, keep the **R4 branch frequency behavior similar** (e.g., a small cap across R4 or a matching RC from the non-inverting input to ground) so the two legs remain frequency-balanced for **HF CMRR**.

---

## 3) Optional tiny series resistors at each input
Put **20–200 Ω** in series with each input right at the op-amp pins. With the input capacitances, they form a mild RC that **damps ringing** and helps with **EMI/clock edges**. Use the **same value on both inputs** to protect CMRR.

---

# Picking the numbers (CCD-oriented recipe)

1) **Define the video bandwidth.**  
   For pixel rate \(f_{pix}\), a practical signal bandwidth target is \(B \approx 0.2\!-\!0.3\,f_{pix}\) (exact value depends on your CDS window and required rise time).

2) **Choose the gain \(K\).**  
   Make \(R_1=R_3\) in the **2–10 kΩ** range (noise vs. drive trade-off), and set \(R_2=R_4=K\cdot R_1\). Use **0.1% (or better)** ratio matching.

3) **Stability (lead) compensation:**  
   Estimate total input cap on the inverting node \(C_{in}\) (CCD node + op-amp + layout), often **5–50 pF**.  
   Set \(C_{R1}\) so \(f_z \approx 1/(2\pi R_1 C_{R1}) \approx 1/(2\pi R_2 C_{in})\).  
   (This aligns the zero with the pole made by \(R_2\) and \(C_{in}\).)

4) **HF roll-off / CMRR tracking:**  
   Add **equal** caps across **R2 and R4** to create matched poles at
   \[
   f_p = \frac{1}{2\pi R_2 C_{R2}} = \frac{1}{2\pi R_4 C_{R4}}
   \]
   Place \(f_p\) about **3–10×** your video bandwidth so you trim clock feedthrough without dulling video detail.

5) **(Optional) Input series resistors:**  
   Add 50–100 Ω in series with both inputs, identical values.

6) **Check the op-amp**: input common-mode range (the non-inverting leg sees actual CCD bias), output swing for \(K(V_{sig}-V_{dum})\), and **GBW** ≥ ~\(10\times\) your closed-loop bandwidth (more if you see peaking).

---

# Quick numeric example
- \(f_{pix}=1\,\text{MHz}\) → choose \(B \approx 250\,\text{kHz}\).  
- Gain \(K=10\). Pick \(R_1=R_3=4.99\,\text{kΩ}\), \(R_2=R_4=49.9\,\text{kΩ}\).  
- Assume \(C_{in}=15\,\text{pF}\) on the inverting node.  
  - Input pole from \(R_2\|source\) with \(C_{in}\) is near \(f_{p,in}\approx 1/(2\pi\cdot 49.9k \cdot 15pF)\approx 212\,\text{kHz}\).  
  - Choose \(C_{R1}\) so \(f_z\approx 212\,\text{kHz}\):  
    \(C_{R1} \approx 1/(2\pi\cdot 4.99k \cdot 212k)\approx 150\,\text{pF}\).  
- Set **matched** caps across R2 and R4 to gently cut HF at, say, \(f_p=2.5\,\text{MHz}\):  
  \(C_{R2}=C_{R4}\approx 1/(2\pi\cdot 49.9k \cdot 2.5M)\approx 1.3\,\text{pF}\) (use 1–1.5 pF NP0).  
- Add 68 Ω series on both inputs.

Result: stable loop, preserved CMRR up through the pixel clock harmonics, and reduced sensitivity to feedthrough.

---

# One more thing: CDS vs. “just caps”
Caps across R2/R4 **won’t remove kTC/reset noise**; they just limit/shape HF and help stability/CMRR.  
For true baseline removal you still want **Correlated Double Sampling (CDS)** (switched-capacitor or S/H-and-subtract), ideally feeding your diff stage (signal vs. dummy) or following it.

---

If you share your pixel rate, estimated input capacitance, and target gain, I’ll plug in values for \(C_{R1}, C_{R2}=C_{R4}\), and the input series resistors so you can drop them straight into your schematic.
