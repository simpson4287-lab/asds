# Push to break switch
Date (UTC): 2026-04-20 06:00
Conversation ID: 69e5c0e7-cb60-83eb-ab71-23f431e24fd0
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-20 06:00):
I need to find a push to break switch 

[M2] AI (2026-04-20 06:00):
I’m checking the correct terminology and a few current UK-available examples so I can point you at the right thing rather than the wrong switch family.

[M3] AI (2026-04-20 06:00):
Yes — what you want is usually called a **momentary normally-closed pushbutton**, or **push-to-break**. RS describes push-to-break switches as the **normally closed (NC)** type, where the circuit is closed until you press the button. citeturn165224search1turn165224search3

A few current UK examples:
- **Multicomp Pro R13-24B-05-BB** — momentary, **SPST-NC**, 7.2 mm, solder terminals. CPC lists it as NC / push-to-break. citeturn165224search2turn165224search4
- **Multicomp Pro R13-24B-05-BR** — same family, also **SPST-NC** / momentary. citeturn165224search4
- **Multicomp “800-027”** — CPC explicitly lists it as **push to break**, NC, panel mount, momentary. citeturn165224search2turn165224search4

When searching, use these terms:
- **momentary NC pushbutton**
- **SPST-NC pushbutton**
- **push-to-break switch**

If this is for an electronics panel rather than mains, the key checks are:
- contact form: **SPST-NC** or **SPDT** if you want both NC and NO available
- mounting hole size
- current/voltage rating
- terminal style: solder, PCB, or quick-connect
- sealing, if it is for outdoor or dusty use

If you want, tell me **panel mount or PCB**, **approx hole size**, and **signal level or current**, and I’ll narrow it to the right exact part.

[M4] ME (2026-04-20 06:01):
Smd*

[M5] AI (2026-04-20 06:01):
I’m narrowing it to SMD tactile or low-profile SMT switch parts with a normally-closed or changeover contact, because plain SMT tact switches are very often push-to-make rather than push-to-break.

[M6] AI (2026-04-20 06:01):
For **SMD**, that gets a bit trickier.

Most standard **SMT tactile switches are push-to-make (SPST-NO)**, not push-to-break. Farnell’s SMD tact listings are overwhelmingly SPST-NO, and RS describes the usual tact action as making contact only while pressed. citeturn673136search1turn673136search7

So for **push-to-break in SMD**, you usually want one of these:

1. **SPDT SMT tactile switch**  
   Use the **NC + common** pins, so pressing it breaks that path.  
   A solid example is **C&K KSC441J DCT 70SH LFS**, which Farnell lists as **SPDT, NC-NO**, tactile, IP67. citeturn417167search8

2. **SMT side-actuated SPDT tactile**  
   Example: **Littelfuse K5V series** SMD side-actuated tactile switches, listed by Farnell as **SPDT** surface-mount parts. citeturn417167search2turn417167search5

3. **Rare true NC SMT momentary switch**  
   These exist, but are much less common than SPDT parts. In practice, **SPDT is usually the safer search path** because you can wire it as push-to-break. RS also notes some pushbutton families support either push-to-make or push-to-break depending on wiring. citeturn673136search3

Best search terms:
- **SMT SPDT tactile switch**
- **SMD tactile switch NC-NO**
- **momentary SMD pushbutton SPDT**

So the practical answer is:

**Don’t look for a plain SMD tact switch labeled “push to break.” Look for an SMD SPDT tactile switch and use the NC contact.**

If you want, I can now find you:
- a **tiny top-actuated** one,
- a **side-actuated** one,
- or a **Farnell / RS / Mouser** part that fits your footprint.

[M7] ME (2026-04-20 06:37):
[image]
Can you verify this circuit 
[attached file: IMG_1E84B292-3124-4AA2-94C3-19F194EE3023.jpeg]

[M8] AI (2026-04-20 06:37):
At a glance: **the basic circuit looks conceptually correct** for a **6 V to 5 V adjustable LT3022 regulator**, but there are **two things I’d want checked carefully before signing it off**.

What looks right:
- The **feedback divider values** appear to be **4.87 kΩ / 200 Ω**, and for the LT3022 the ADJ reference is **200 mV**, so that gives about  
  **Vout ≈ 0.2 × (1 + 4870/200) = 5.07 V**. That is essentially a 5 V setpoint. citeturn285114view0
- The LT3022 adjustable version is intended for **0.2 V to 9.5 V outputs**, so 5 V is well within range. citeturn285114view0
- The datasheet also recommends choosing the divider so it satisfies the device’s **1 mA minimum load current**; using **200 Ω as the lower resistor** gives about **1 mA** through the divider, which matches that recommendation. citeturn285114view0
- With **6 V in and 5 V out**, you have enough headroom above dropout for normal regulation. The LT3022’s dropout is low, and for higher output voltages the input needs to be roughly **VOUT + dropout**. citeturn285114view0

What I would question:
- **SHDN network:** from the photo, **SHDN appears tied high through a 0 Ω link**, with a capacitor to ground. If that 0 Ω really goes straight to the input rail, then the part is basically **always enabled whenever VIN is present**. That is fine if intentional, but it means this is **not really a meaningful delay/threshold network** in its current form. The SHDN threshold note on the schematic is consistent with the pin being logic-controlled, but the **0 Ω link defeats any real RC delay behaviour**. citeturn285114view0
- **Output capacitor implementation:** the LT3022 is specified as stable with **low-ESR output capacitors, 10 µF minimum**, and placement matters. Your schematic seems to show **100 nF + 1 µF + 100 µF**, which may be fine, but I’d want to know **what technology C237 is** and how close the caps are to the regulator pins. If the only local ceramic is 100 nF or 1 µF and the 100 µF is farther away or high-ESR, that is where I’d be cautious. citeturn285114view0

One more practical check:
- At **1 A load**, dropping **6 V to 5 V** means about **1 W dissipation** in the regulator, ignoring small extra terms. That is not outrageous, but it is enough that **package thermal layout and exposed-pad grounding** matter. The datasheet explicitly calls out thermal considerations for continuous operation. citeturn285114view0

So my verdict is:

**Electrically, the setpoint and overall topology look sensible.**  
**Main review points are:**  
1. confirm the **SHDN pin behaviour is really what you want**, and  
2. confirm the **output capacitor type, value at bias, ESR, and placement**.

If you want, I can mark this image up block-by-block and tell you **exactly what each part is doing** and where the weak points are.

[M9] ME (2026-04-20 06:39):
Show calls for the v out

[M10] AI (2026-04-20 06:39):
Yes — for that regulator the **adjustable output equation** is:

\[
V_{OUT} = V_{REF}\left(1+\frac{R_{TOP}}{R_{BOT}}\right) + I_{ADJ}\cdot R_{TOP}
\]

For the **LT3022 adjustable**, the reference is about **200 mV**. citeturn553333view0

From your schematic:
- **R146 = 4.87 kΩ** from **VOUT to ADJ**
- **R147 = 200 Ω** from **ADJ to GND**

So the main calculation is:

\[
V_{OUT} \approx 0.2\left(1+\frac{4870}{200}\right)
\]

\[
\frac{4870}{200} = 24.35
\]

\[
1 + 24.35 = 25.35
\]

\[
V_{OUT} \approx 0.2 \times 25.35 = 5.07V
\]

So your divider is calling for about:

\[
\boxed{V_{OUT} \approx 5.07V}
\]

That is why I said it is basically a **5 V rail**.

The tiny extra term from **ADJ pin current** is usually small, so first-pass design review normally just treats it as about **5.07 V**. The datasheet’s own example also uses the same 200 mV reference and a 200 Ω lower resistor style. citeturn553333view0

If you want, I can also do the **reverse calculation** and tell you what **top resistor gives exactly 5.00 V**.

[M11] ME (2026-04-20 09:56):
[image]
What’s this output resistor doing? Someone said it’s more advised to be 5R. Can you confirm?
[attached file: IMG_309F25FE-C2FB-4EDC-B662-2604739DBE3E.jpeg]

[M12] AI (2026-04-20 09:56):
Yes — that resistor is doing a **real job**, and it is **not just a random output limiter**.

In this ADA4870 stage, the series resistor between the amplifier output pins and the external node is primarily an **output isolation resistor**. When the load has capacitance — which CCD clock lines, cables, probes, connector parasitics, and device input capacitance often do — the amplifier’s output impedance and that capacitance add an extra pole, which can reduce phase margin and cause peaking or oscillation. Analog Devices explicitly says that a **small series resistor \(R_S\)** between the amplifier output and the capacitive load is used to let the ADA4870 drive capacitive loads stably. citeturn919203search0turn919203search1

So what **R7 = 1 Ω** is doing here:
- isolating the ADA4870 from the **capacitive part of the load**
- damping ringing / peaking
- reducing the instantaneous surge current into the load capacitance
- slightly protecting the amplifier from ugly transmission-line or probe-induced behaviour

That means the advice you were given — **“5 Ω is more advised”** — is **plausible in some cases, but not universally correct**. The ADA4870 datasheet does **not** say “always use 5 Ω.” It says to use a **small series resistor**, and that the required value depends on the **capacitive load**; it even provides a curve of **series resistor value vs. load capacitance** for about **1 dB peaking**. citeturn919203search0

So the right conclusion is:

- **1 Ω may be perfectly reasonable** if your effective load capacitance is modest and you are trying to preserve faster edges / lower output loss.
- **5 Ω is a more conservative damping value** and may help if you are seeing ringing, overshoot, or marginal stability.
- But **5 Ω will also cost you more**:
  - more RC slowing with the load capacitance
  - more voltage drop at high output current
  - more dissipation in the resistor

That last point matters here because this is a **clock driver / fast amplifier**, not a slow buffer. If the output current is significant, a bigger resistor starts to hurt. For example, at:
- **100 mA**, 1 Ω drops **0.1 V**, 5 Ω drops **0.5 V**
- **500 mA**, 1 Ω drops **0.5 V**, 5 Ω drops **2.5 V**

So **5 Ω is not a free improvement**.

There is also an Analog Devices forum reply suggesting **about 5 Ω** in one ADA4870 design context, but that is application-specific guidance, not a blanket rule from the datasheet. citeturn919203search2turn919203search0

My view from your schematic:
- **R7 is there for output isolation/damping**
- **1 Ω is not obviously wrong**
- **5 Ω is only “more advised” if your real load is sufficiently capacitive or you have measured ringing/instability**

For your kind of use, the proper way to choose it is:
1. estimate the load capacitance seen at TP49 / the CCD clock net
2. check whether there is cable/probe capacitance
3. simulate or bench-test step response
4. increase R7 only as far as needed to tame peaking

So I would not change it to **5 Ω by default**. I would say:

**Start with 1 Ω if edge speed matters. Move upward only if the waveform tells you to.**

If you want, send the approximate load on that node — CCD input cap, trace length, cable/probe, and target edge rate — and I’ll give you a more defensible resistor range.

[M13] ME (2026-04-20 10:00):
My loads range for 15-60pf. Can you show how the resistor is worked out 

[M14] AI (2026-04-20 10:00):
Yes. For the **ADA4870**, this resistor is **not normally calculated from a clean closed-form formula** from the datasheet. ADI gives it as an **empirical design value** from **Figure 70: \(R_S\) vs. \(C_L\) for maximum 1 dB peaking** for the test circuit in Figure 69. citeturn970975view0turn433220view0

From that graph, for your load range:

- **15 pF** → \(R_S\) is roughly **1 Ω**
- **30 pF** → \(R_S\) is roughly **1.5 Ω**
- **60 pF** → \(R_S\) is roughly **2 to 2.5 Ω**

Those are read off the datasheet curve, so treat them as **engineering estimates**, not exact values. citeturn433220view0

So for your stated **15–60 pF** load range:
- **1 Ω** is believable at the low end.
- A more conservative single-value choice would be around **2.2 Ω**.
- **5 Ω** is not what the graph points to for 15–60 pF. It is more in line with the datasheet’s example table for **300 pF** loads in several standard gain configurations. citeturn970975view0

Why the resistor rises with capacitance:
- the output stage sees the load capacitance as an extra pole,
- that reduces phase margin,
- adding \(R_S\) isolates the amplifier from the capacitor and damps the peaking/instability. citeturn970975view0

A useful first-order intuition is the output node time constant:

\[
\tau \approx R_S \cdot C_L
\]

That is **not** the datasheet design equation, but it explains the tradeoff:
- larger \(R_S\) gives more damping,
- but also slows the edge and increases voltage drop at load current.

For example:
- **1 Ω with 15 pF** → \(\tau \approx 15\ \text{ps}\)
- **2.2 Ω with 60 pF** → \(\tau \approx 132\ \text{ps}\)
- **5 Ω with 60 pF** → \(\tau \approx 300\ \text{ps}\)

So 5 Ω will damp harder, but it is also more intrusive. For a fast CCD clock path, that may be unnecessary if the actual capacitive load is only tens of pF.

Also note the datasheet’s **Table 6** shows **5 Ω with 300 pF**, which is a much heavier capacitive case than yours. citeturn970975view0

My practical recommendation for your range:
- if you want one fitted value for **15–60 pF**, use **2.2 Ω** as a sensible starting point,
- if edge speed is absolutely critical and layout is tight, **1 Ω** may still be fine,
- I would **not jump straight to 5 Ω** unless measurement shows ringing or the real effective capacitance is much higher once trace, connector, cable, probe, and CCD input are all included. citeturn879050search2turn970975view0

If you want, I’ll turn that into a small selection table for **15, 20, 30, 40, 50, 60 pF** with preferred resistor values and the likely tradeoff.

[M15] ME (2026-04-20 10:28):
Which page of data sheet?

[M16] AI (2026-04-20 10:28):
Yes — the **\(R_S\) vs. \(C_L\)** graph I was referring to is on **page 19** of the ADA4870 datasheet, as **Figure 70**. Figure 69 is the test circuit just before it, and Figure 71 is the related bandwidth plot. citeturn857243search0turn857243search1

So the bit to look for is:
- **Page 19**
- **Figure 70**
- title along the lines of **“\(R_S\) vs. \(C_L\) for Maximum 1 dB Peaking”**

That is the page supporting the resistor guidance, not a simple algebraic formula page.

[M17] ME (2026-04-20 10:30):
[image]
So why 2.2?
[attached file: IMG_8E001489-6CF6-4F48-9E94-F3AB56114625.jpeg]

[M18] AI (2026-04-20 10:30):
You’re right to challenge that. **2.2 Ω was not the right recommendation for 15–60 pF.** I mixed up the scale and effectively treated your load as much larger than it is.

From the ADA4870 datasheet:
- Table 6’s **5 Ω** examples are for **300 pF**, not tens of pF. citeturn449365view1
- The capacitive-load section says \(R_S\) is chosen from **Figure 70** for a given \(C_L\), and that this is for about **1 dB peaking** in the Figure 69 test circuit. citeturn449365view1

Looking at your screenshot of Figure 70:
- At **100 pF**, the curve is already only around **~0.3 to 0.5 Ω**
- Below that, in the **15–60 pF** region, the curve is essentially down near the floor, not up at 2.2 Ω

So for **15–60 pF**, the datasheet-based takeaway is:

- **1 Ω is already conservative**
- **2.2 Ω is higher than Figure 70 suggests**
- **5 Ω is for a much heavier capacitive load regime**

Why 1 Ω still makes practical sense even if the graph is near zero:
- the graph is for a **specific test setup**
- your real node may include **trace capacitance, package parasitics, connector, test point, probe, CCD pin structure, and layout inductance**
- using **1 Ω** gives a bit of damping margin without heavily slowing the edge

So the more defensible answer is:

- **Pure datasheet reading for 15–60 pF:** around **sub-ohm to ~1 Ω**
- **Practical fitted value:** **1 Ω** is a sensible starting point
- **5 Ω:** only if your *effective* load is far higher, or bench results show ringing/peaking that 1 Ω does not tame

In other words, for your stated **15–60 pF**, I would now say:

\[
\boxed{R_S \approx 0.5\ \Omega \text{ to } 1\ \Omega}
\]

and **1 Ω is the sensible stock value**.

The datasheet also explicitly notes that for **large capacitive loads**, values **below 0.3 Ω are not recommended**, which implies that once you are in the lighter-load region the required resistor is very small anyway. citeturn449365view1

So the clean conclusion is: **your 1R is believable; 5R is not justified by Figure 70 for 15–60 pF.**

If you want, I’ll convert that graph into a little estimated table for **15, 30, 45, 60 pF** and include what I’d actually fit on a board.

[M19] ME (2026-04-20 10:31):
Why not 0.5

[M20] AI (2026-04-20 10:31):
You **could** use **0.5 Ω**. I would not call it wrong.

The reason I would still lean to **1 Ω as the safer starting value** is that the datasheet curve is for the **Figure 69 test circuit**, not your exact board, and the ADA4870 note is really about **stability margin / peaking**, not just nominal capacitor value. ADI says the output resistor is chosen from Figure 70 for a given capacitive load, because the output resistance and \(C_L\) form a pole that can reduce phase margin. citeturn465082view0

So why not 0.5 Ω?

- **0.5 Ω gives less damping** than 1 Ω. If your real effective load is not just 15–60 pF on paper, but 15–60 pF **plus** pad, trace, package, probe, connector, CCD pin behaviour, and any wiring inductance, then 0.5 Ω may leave you closer to peaking. citeturn465082view0
- The datasheet only gives a hard lower warning for **large capacitive loads**, saying **less than 0.3 Ω is not recommended**. That does not ban 0.5 Ω for your case; it just shows you are already getting into the “very small resistor” region where layout starts to matter a lot. citeturn465082view1turn465082view2
- **1 Ω is more robust** as a default E-series fitted value. It buys some extra damping margin for not much penalty.

The tradeoff is simple:

- **0.5 Ω**: faster, lower drop, less damping
- **1 Ω**: slightly slower, slightly more drop, more stable/forgiving

For your **15–60 pF** load range, my practical view is:

- **0.5 Ω** if the layout is tight, load really is local and known, and edge speed is king
- **1 Ω** if you want a safer first-spin value without overdoing it
- **5 Ω** is still far too conservative for that capacitance range based on Figure 70 and the 300 pF examples in Table 6. citeturn908211view0turn465082view0

So the honest answer is:

\[
\boxed{0.5\ \Omega\ \text{is plausible, but }1\ \Omega\text{ is the safer default}}
\]

If this is a board spin decision, I’d fit **1 Ω** and leave an option for **0.5 Ω / 0 Ω** during bring-up.

[M21] ME (2026-04-20 10:45):
[image]
So does that make sense?
[attached file: IMG_93439E70-2114-4452-A4C8-34C414F4887C.jpeg]

[M22] AI (2026-04-20 10:45):
Mostly **yes, the structure makes sense**, but **two of the equations need tightening**.

What looks right:
- Using **capacitance, swing, and frequency** to estimate switching energy and average power is the right approach.
- Your **R7 power** numbers look consistent with  
  \[
  P = C(\Delta V)^2 f
  \]
  For example, for SØ1:  
  \[
  5.83\times10^{-11}\cdot 9.5^2 \cdot 1 \approx 5.26\times10^{-9}\text{ W}
  \]
  which is **5.26 nW**, not mW.

So the first issue is:

## 1) Your “R7 Power (mW)” heading is wrong
The values shown are actually in **nW**, not mW.

Examples:
- 5.2616 shown as “mW” is really about **5.26 nW**
- 41.1540 shown as “mW” is really about **41.15 nW**

So either:
- change the column heading to **nW**, or
- multiply the displayed values by \(10^{-6}\) if you truly want mW

---

## 2) Your energy-per-cycle note is missing the factor of 1/2
You wrote:

\[
E = C(\Delta V)^2
\]

But the energy stored on a capacitor for one charge from 0 to \(V\) is:

\[
E = \frac{1}{2} C(\Delta V)^2
\]

Now, whether your original form is acceptable depends on what you mean by **“energy per cycle”**:

- if you mean **energy stored in the capacitor on one transition**, use  
  \[
  \frac{1}{2}C(\Delta V)^2
  \]
- if you mean **energy drawn from the driver over a full charge-discharge cycle**, then  
  \[
  C(\Delta V)^2
  \]
  is often used as the total lost per full cycle

So your sheet can be valid, but only if you define it properly.

A better note would be:

\[
E_{\text{cycle}} = C(\Delta V)^2
\]

for a full 0→V→0 cycle, and then

\[
P = C(\Delta V)^2 f
\]

That is standard for dynamic switching loss.

---

## 3) Your \(I_{peak}\) formula is only a resistor-limited approximation
You used:

\[
I_{peak} = \frac{\Delta V}{R_7}
\]

With \(R_7 = 1\Omega\), that gives **9.5 A**, which matches your table.

Mathematically, yes, that follows from Ohm’s law. But physically it is only the **instantaneous theoretical upper bound if the full step initially appears across R7**.

It is **not** the real peak current prediction for the full circuit, because actual current is limited by:
- ADA4870 output current capability
- output slew behaviour
- loop stability
- trace/package inductance
- the fact the load is capacitive, so current is fundamentally tied to  
  \[
  i = C\frac{dV}{dt}
  \]

For a capacitive load, the more physically relevant current estimate is:

\[
i = C\frac{dV}{dt}
\]

So for example, if:
- \(C = 60\text{ pF}\)
- \(\Delta V = 9.5\text{ V}\)
- rise time = 3 ns

then:

\[
i \approx 60\times10^{-12}\cdot \frac{9.5}{3\times10^{-9}}
\approx 0.19\text{ A}
\]

That is **190 mA**, not 9.5 A.

So I would relabel your current column as something like:

**Theoretical resistor-limited instantaneous current ceiling**
or remove it unless you really need that bound.

---

## 4) Important interpretation of the power
The value from:

\[
P = C(\Delta V)^2 f
\]

is mainly the **dynamic charging loss associated with the capacitive load**.

It is **not specifically “R7 power”** in the strict sense unless you are deliberately assigning all dynamic dissipation to that element in a simplified model. In reality, dissipation is shared across:
- output stage
- R7
- parasitics
- discharge path / recovery behaviour

So **“R7 Power”** is too strong a label.

A better heading would be:
- **Capacitive switching power**
- **Dynamic load power**
- **Approx. switched power**

If you want an actual **R7 resistor dissipation** estimate, that needs a more specific waveform/current model.

---

## Recommended corrections

I’d change the notes to:

**Note 3**  
For one full charge-discharge cycle:
\[
E_{\text{cycle}} = C(\Delta V)^2
\]

**Note 4**  
Approximate capacitive load current:
\[
i \approx C\frac{dV}{dt}
\]

**Note 5**  
Average switched power:
\[
P = C(\Delta V)^2 f
\]

And rename the last column from **“R7 Power (mW)”** to:

**Dynamic Switching Power (nW)**

---

## Bottom line
So: **the overall method makes sense**, but:
- the **power units are wrong**
- **R7 power** is mislabelled
- **9.5 A peak** is not a realistic circuit current estimate
- the energy expression needs clearer wording about **per transition vs per full cycle**

The sheet is close, but I would not leave it as-is for review.

If you want, I’ll rewrite the table notes in a clean design-review style so you can paste them straight into the sheet.

[M23] ME (2026-04-20 10:49):
Can you replicate the full table correctly and updated the notes?

[M24] AI (2026-04-20 10:49):
Yes — and there was one key hidden issue:

Your **power numbers were actually fine for mW** **provided** the frequency entries **1** and **24** are really **MHz**, not Hz. So the main fix is:

- change **Frequency f (Hz)** to **Frequency f (MHz)**  
- keep the power values in **mW**
- tighten the notes so they describe **full-cycle switched energy** and the **R7 current figure** properly

Here’s the corrected version.

### Corrected table

| Signal | C to SS (F) | C to SS (pF) | CLK LOW (V) | CLK HIGH (V) | Frequency f (MHz) | Edge Swing ΔV (V) | Damping R (R7) (Ω) | Full-Cycle Switched Energy \(E_{cycle}\) (J) | Theoretical \(I_{R7,max}=\Delta V/R7\) (A) | Dynamic Switched Power \(P=E_{cycle}\cdot f\) (mW) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SØ1  | 5.83E-11 | 58.3 | 0 | 9.5 | 1  | 9.5 | 1 | 5.262E-09 | 9.5 | 5.2616 |
| SØ2  | 5.70E-11 | 57.0 | 0 | 9.5 | 1  | 9.5 | 1 | 5.144E-09 | 9.5 | 5.1443 |
| MTØ1 | 2.62E-11 | 26.2 | 0 | 9.5 | 1  | 9.5 | 1 | 2.365E-09 | 9.5 | 2.3646 |
| MØ3  | 3.67E-11 | 36.7 | 0 | 9.5 | 1  | 9.5 | 1 | 3.312E-09 | 9.5 | 3.3122 |
| MØ2  | 4.05E-11 | 40.5 | 0 | 9.5 | 1  | 9.5 | 1 | 3.655E-09 | 9.5 | 3.6551 |
| IØ2  | 1.74E-11 | 17.4 | 0 | 9.5 | 24 | 9.5 | 1 | 1.570E-09 | 9.5 | 37.6884 |
| IØ1  | 1.90E-11 | 19.0 | 0 | 9.5 | 24 | 9.5 | 1 | 1.715E-09 | 9.5 | 41.1540 |
| IØ3  | 1.78E-11 | 17.8 | 0 | 9.5 | 24 | 9.5 | 1 | 1.606E-09 | 9.5 | 38.5548 |

### Updated notes

**NOTE 1:**  
Values extracted from ICD – AEQ-TN-TE2V-00000029 v5.

**NOTE 2:**  
A common fitted value of **R7 = 1 Ω** has been adopted across all eight clocks based on ADA4870 capacitive-load guidance and expected use-case loading. Final value should be confirmed during bench evaluation from measured overshoot, ringing, settling, and edge-rate performance.

**NOTE 3:**  
For a full charge-discharge cycle of a capacitive load:

\[
E_{cycle}=C\cdot(\Delta V)^2
\]

where:

\[
C = \text{capacitance to SS (F)}
\]

\[
\Delta V = V_{HIGH}-V_{LOW}
\]

This is the **full-cycle switched energy**, not the single-transition stored energy.

**NOTE 4:**  
The column labelled current is a **theoretical resistor-limited instantaneous ceiling** only:

\[
I_{R7,max}=\frac{\Delta V}{R_7}
\]

where:

\[
\Delta V = V_{HIGH}-V_{LOW}
\]

\[
R_7 = 1\ \Omega
\]

This is **not** the expected real driver current into the load. Actual peak current will be influenced by amplifier output capability, edge rate, loop dynamics, and total effective load capacitance.

**NOTE 5:**  
Average dynamic switched power is estimated from:

\[
P=E_{cycle}\cdot f=C\cdot(\Delta V)^2\cdot f
\]

where:

\[
f = \text{clock frequency in Hz}
\]

For this table, the entered frequency values of **1** and **24** are treated as **MHz**, so:

- **1 MHz = 1 × 10^6 Hz**
- **24 MHz = 24 × 10^6 Hz**

This is why the final power values are in **mW**.

### Recommended header fixes
I’d change your sheet headings to these:

- **C to SS (F)** or add a separate **(pF)** display column
- **Frequency f (MHz)**
- **Full-Cycle Switched Energy (J)**
- **Theoretical \(I_{R7,max}\) (A)**
- **Dynamic Switched Power (mW)**

The one thing I would **not** call that last column is **“R7 Power”**, because it is really the **switched capacitive-load power estimate**, not guaranteed resistor dissipation.

If you want, I can turn this into a clean Excel-ready CSV block.

[M25] ME (2026-04-20 10:50):
Yes

[M26] AI (2026-04-20 10:50):
Here it is in **CSV-ready** form.

```csv
Signal,C_to_SS_F,C_to_SS_pF,CLK_LOW_V,CLK_HIGH_V,Frequency_MHz,Edge_Swing_dV_V,Damping_R_R7_Ohm,Full_Cycle_Switched_Energy_J,Theoretical_I_R7_max_A,Dynamic_Switched_Power_mW
SØ1,5.83E-11,58.3,0,9.5,1,9.5,1,5.262E-09,9.5,5.2616
SØ2,5.70E-11,57.0,0,9.5,1,9.5,1,5.144E-09,9.5,5.1443
MTØ1,2.62E-11,26.2,0,9.5,1,9.5,1,2.365E-09,9.5,2.3646
MØ3,3.67E-11,36.7,0,9.5,1,9.5,1,3.312E-09,9.5,3.3122
MØ2,4.05E-11,40.5,0,9.5,1,9.5,1,3.655E-09,9.5,3.6551
IØ2,1.74E-11,17.4,0,9.5,24,9.5,1,1.570E-09,9.5,37.6884
IØ1,1.90E-11,19.0,0,9.5,24,9.5,1,1.715E-09,9.5,41.1540
IØ3,1.78E-11,17.8,0,9.5,24,9.5,1,1.606E-09,9.5,38.5548
```

And the **updated notes** in paste-ready form:

```text
NOTE 1:
Values extracted from ICD – AEQ-TN-TE2V-00000029 v5.

NOTE 2:
A common fitted value of R7 = 1 Ω has been adopted across all eight clocks based on ADA4870 capacitive-load guidance and expected use-case loading. Final value should be confirmed during bench evaluation from measured overshoot, ringing, settling, and edge-rate performance.

NOTE 3:
For a full charge-discharge cycle of a capacitive load:

E_cycle = C × (ΔV)^2

where:
C = capacitance to SS (F)
ΔV = V_HIGH − V_LOW

This is the full-cycle switched energy, not the single-transition stored energy.

NOTE 4:
The column labelled current is a theoretical resistor-limited instantaneous ceiling only:

I_R7,max = ΔV / R7

where:
ΔV = V_HIGH − V_LOW
R7 = 1 Ω

This is not the expected real driver current into the load. Actual peak current will be influenced by amplifier output capability, edge rate, loop dynamics, and total effective load capacitance.

NOTE 5:
Average dynamic switched power is estimated from:

P = E_cycle × f = C × (ΔV)^2 × f

where:
f = clock frequency in Hz

For this table, the entered frequency values of 1 and 24 are treated as MHz, so:
1 MHz = 1 × 10^6 Hz
24 MHz = 24 × 10^6 Hz

This is why the final power values are in mW.
```

One important correction to my earlier wording: the **dynamic switched power values are for the capacitive load energy moved per cycle**, not guaranteed **R7 resistor dissipation**. So the column title should stay as:

**Dynamic Switched Power (mW)**

not **R7 Power**.

[M27] ME (2026-04-20 11:35):
How to start up 4870 on high z? There is an on in and a short down in 

[M28] AI (2026-04-20 11:35):
Yes. To start the **ADA4870** with the output effectively disabled, use the **SD** pin for shutdown, not the **ON** pin alone. The datasheet says **SD is an active-low shutdown input** and **ON is an active-low turn-on/enable input**, both referenced to **VEE**. citeturn150544search0turn150544search1

The practical sequencing is:

- **High-Z / low-power state:** pull **SD low**. That puts the amplifier into shutdown and drops quiescent current to about **750 µA**. The vendor guidance says **do not float SD**. citeturn150544search0turn150544search1
- **Turn-on sequence:** first pull **SD high**, then pull **ON low**. ADI explicitly says this sequence is required when coming out of shutdown. citeturn150544search0turn150544search1
- **After turn-on:** the **ON** pin can then be **floated** if you want the device’s **short-circuit protection** enabled. citeturn150544search0turn150544search1

So if your goal is **“power up in High-Z / disabled, then enable later”**, the clean approach is:

1. Hold **SD = low** at startup.  
2. Keep **ON** in a defined state as needed, but **SD low** is what actually guarantees shutdown.  
3. When ready to enable, drive **SD high** first.  
4. Then drive **ON low**.  
5. Optionally release **ON** afterward if you want short-circuit protection active. citeturn150544search0turn150544search1

One important caution: I would avoid calling it a perfect **“high-Z output”** unless you have confirmed that exact behavior at the load node in your circuit. The official wording is **shutdown** / **low power shutdown**; it does not, in the snippets above, explicitly promise an ideal tri-stated output buffer in every external condition. citeturn150544search0turn150544search1

A simple logic summary relative to **VEE**:

- **SD low** → shutdown  
- **SD high + ON low** → amplifier on  
- **SD must not float**  
- **ON may float after startup** for short-circuit protection behavior citeturn150544search0turn150544search1

If you want, I can sketch a small pull-up / pull-down network so it always comes up disabled and only turns on when your control logic says so.

[M29] ME (2026-04-20 11:42):
[image]
So if that was a p channel. Circles red, that would work?
[attached file: IMG_E2BA108B-C829-4B30-88B0-EC5602ABDA44.jpeg]

[M30] AI (2026-04-20 11:42):
**Not from ordinary 0/3.3 V logic, no.**  
A **P-channel MOSFET there only works if its gate is driven in the same analogue rail domain**.

What that node needs to do is:

- **SD low (near VEE = -13 V)** at power-up → amplifier isolated / shutdown
- **SD high** later → amplifier enabled

And you already have:
- **R6 pulling ON low** → that is fine for enable
- **the SD node pulled up to +19 V through 10 k** → so if nothing pulls it down, the part enables

So the transistor at the red circle is really just a **pull-down clamp for SD**.

## If that device were a P-channel MOSFET
It would only make sense if:

- **source = SD node**
- **drain = -13 V**
- **gate driven low to turn it on**
- **gate driven high, close to source, to turn it off**

That means the gate has to swing roughly in the **-13 V / +19 V world**, or at least close enough to the source to turn it off.

## Why it does **not** work from 0/3.3 V logic
If the SD node is being pulled up toward **+19 V**, then a PMOS gate at:

- **0 V** gives \(V_{GS} \approx -19\text{ V}\) → **hard on**
- **3.3 V** gives \(V_{GS} \approx -15.7\text{ V}\) → **still hard on**

So from normal logic levels, the PMOS would basically **stay on** and keep dragging SD low.

That means:

\[
\boxed{\text{PMOS there is only valid if the gate is driven with rail-shifted control, not plain logic}}
\]

## Same problem for an NMOS there
An **NMOS to -13 V** also does not behave properly from 0/3.3 V gate drive, because with source at **-13 V**:

- gate at **0 V** gives \(V_{GS}=+13\text{ V}\)
- gate at **3.3 V** gives \(V_{GS}=+16.3\text{ V}\)

So it is basically **always on** too.

## So the real answer
If **CLK_ISOLATE** is a normal digital signal, then:

- **No, simply making that part a PMOS does not solve it**

If **CLK_ISOLATE** is already level-shifted into the analogue rail domain, then:

- **Yes, a PMOS could work there as an inverting pull-down element**

## Practical interpretation of your circuit
Your intended logic looks like this:

- **CLK_ISOLATE asserted at startup** → force **SD low** → ADA4870 off
- **CLK_ISOLATE released later** → let **10 k pull SD high** → ADA4870 on

That is a sound intent.  
The issue is just **how you translate the control signal to a node that must move between -13 V and +19 V**.

## What I’d use instead
A more robust way is:

- keep the **10 k pull-up on SD**
- use a **proper level-shift stage** to pull SD to **-13 V**
- for example, a **small transistor pair** or **open-collector/open-drain level shifter** referenced to the analogue rails

So the key point is:

\[
\boxed{\text{The function is right, but a lone PMOS there is not enough unless the gate drive is also shifted.}}
\]

If you want, I can sketch a **clean startup-safe SD control circuit** for **3.3 V logic into ADA4870 SD/ON with +19/-13 rails**.

[M31] ME (2026-04-20 11:45):
I’m not talking about 3.3v at all

[M32] AI (2026-04-20 11:45):
Understood — then the answer is **different**.

If your control signal itself already lives in the **analogue rail domain**, then **yes, a P-channel device there can work** as the pull-down element for **SD**.

What matters is the **gate-to-source voltage**, not whether the control originated from 3.3 V logic.

For the ADA4870:

- **SD low** relative to **VEE** puts it in shutdown.
- **SD high** relative to **VEE** enables it. citeturn447227view0

With your rails of roughly **+19 VA** and **−13 VA**, the SD thresholds are referenced to **VEE = −13 V**, so:
- shutdown is around **−13 V to about −12.1 V**
- enabled is anything above about **−11.9 V** and up toward **VEE + 5 V**. citeturn447227view0

So your transistor’s job is simply:

- **ON at startup** → drag **SD** down near **−13 V** → shutdown
- **OFF later** → let the **10 k** pull-up take **SD** high → enabled

That function is valid.

## If the circled part is a P-channel MOSFET
It can work **provided the terminals and control polarity are right**.

For a PMOS used as a pull-down switch here, the usual idea would be:

- **source to the SD node**
- **drain to −13 VA**
- **pull-up resistor from SD to +19 VA**
- **gate driven close to source to turn it OFF**
- **gate driven sufficiently below source to turn it ON**

That last bit is the key.  
A PMOS turns on when:

\[
V_{GS} = V_G - V_S
\]

is **negative enough**.

So:
- if **SD/source** is sitting high and you pull the **gate lower**, the PMOS turns on and clamps SD downward
- if you bring the **gate up near the source**, it turns off and the 10 k pull-up releases SD high

## The real caveat
The only thing I would check carefully is this:

If the PMOS **source is not fixed**, but attached to the moving **SD node**, then turn-off behaviour depends on the gate being able to track close enough to that source voltage. If your gate drive cannot go high enough, the PMOS may not turn fully off.

So the circuit is viable, but only if your gate control swings far enough that:

- **ON state:** \(V_{GS}\) is comfortably negative
- **OFF state:** \(V_{GS}\) is near 0 V

## In plain terms
So, since you are **not** talking about 3.3 V logic:

- **yes**, a **P-channel MOSFET there could work**
- **yes**, the intended function is sensible
- but only if the **gate drive is referenced correctly to the source/SD node**, so the PMOS can both **turn on hard** and **turn off hard**

## One extra practical point
Because **SD** only needs a logic-level state relative to **VEE**, you do **not** need to switch large current. So in practice, a **small-signal transistor stage** is often easier to reason about than a PMOS with a moving source node.

Your 10 k pull-up plus transistor pull-down concept is fine. The main design check is simply:

\[
\boxed{\text{Can the chosen device and gate drive guarantee both } V_{GS(on)} \text{ and } V_{GS(off)}?}
\]

If you want, I can annotate your exact sketch and tell you whether the **source/drain/gate orientation** you have in mind is the right way round.

[M33] ME (2026-04-20 11:47):
[image]
The input is 3.3v logic yes 
[attached file: IMG_FD1E94B6-09F0-4C24-A328-342A9746B805.jpeg]

[M34] AI (2026-04-20 11:48):
Right — with **3.3 V logic in**, a **single P-channel MOSFET there is not the right solution**.

There are actually **two separate issues**.

First, the **control polarity / gate drive** issue:
- Your note says **CLK_ISOLATE low at power-on = isolate clock**, then **high later = enable clock**.
- For the ADA4870, **SD is active low** and **ON is also active low**. The turn-on sequence from shutdown is: **pull SD high, then pull ON low**. citeturn254653view0turn254653view1
- A lone PMOS used as a pull-down from the SD node to **-13 V** would not be driven properly from **0/3.3 V** when its source is sitting in the analogue domain. It will not give you a clean “off” and “on” over that full node range.

Second, and more important, the **voltage range** issue:
- The ADA4870 **SD pin high level** is specified as **VEE + 1.1 V to VEE + 5 V**.
- The **low level** is **VEE to VEE + 0.9 V**.
- The **ON pin high level** is also only up to **VEE + 5 V**. citeturn254653view0

With **VEE = -13 V**, that means the valid logic window for these pins is roughly:
- **low:** about **-13 V to -12.1 V**
- **high:** about **-11.9 V to -8 V**

So pulling **SD up to +19 V through 10 k** is **not valid** for this pin. It is far above the specified SD/ON input range relative to VEE. The ADI eval board explicitly biases these control pins to about **VEE + 5.2 V**, not to the positive supply rail. citeturn254653view1

So the clean answer is:

## What your circuit should do
For startup-isolated behavior:
- **SD** should be held **low to VEE** at power-up.
- When ready to enable:
  1. drive **SD high** to about **VEE + 5 V**
  2. then drive **ON low** to **VEE**. citeturn254653view0turn254653view1

## What not to do
- Do **not** pull SD or ON to **+19 V**.
- Do **not** try to solve this with a lone PMOS directly driven from **3.3 V logic**.

## What will work
Use a **level-shifted open-collector/open-drain style interface** that creates **VEE-referenced control levels**. In practice:

- create a local **“logic high” for SD/ON** at about **VEE + 5 V**
- use a transistor to pull the pin down to **VEE**
- let **3.3 V logic** drive that transistor through a proper level-shift stage

A very workable pattern is:
- **zener clamp or small regulator** to generate **VEE + 5 V**
- **pull-up resistor** from SD to that **VEE + 5 V** node
- **NPN or NMOS pull-down** to **VEE**
- same idea for **ON**

Then:
- **CLK_ISOLATE = 0** → transistor on → **SD = VEE** → shutdown
- **CLK_ISOLATE = 1** → pull-down released → **SD = VEE + 5 V**
- then separately or by sequencing, force **ON low** after SD is high

So the verdict on your exact question:

\[
\boxed{\text{No — with a 3.3 V control input, just swapping that part to PMOS is not the right fix.}}
\]

The bigger correction is that **SD/ON must be driven in a VEE-referenced ~5 V logic window, not to +19 V**.

If you want, I’ll sketch the exact transistor network for **3.3 V in, +19/-13 rails, default shutdown at power-up, then enable later**.

[M35] ME (2026-04-20 12:11):
But as SD or ON GO TO VCC OR VEE RESEPTICELY. And that’s where they get pulled. Those rails only design are 19 and -13

[M36] AI (2026-04-20 12:12):
That’s the key point: **for ADA4870, “high” on SD or ON does not mean “tie it to VCC.”** It means **drive it to a valid logic-high level referenced to VEE**. The datasheet is explicit:

- **SD high (enabled)**: **VEE + 1.1 V to VEE + 5 V**
- **SD low (power-down)**: **VEE to VEE + 0.9 V**
- **ON high (power-down)**: **VEE + 1.8 V to VEE + 5 V**
- **ON low (enabled)**: **VEE to VEE + 1.3 V** citeturn793791view0

With your rails:
- **VEE = -13 V**
- so a valid control **high** is only about **-11.9 V to -8 V** for SD, and **-11.2 V to -8 V** for ON.  
That is nowhere near **+19 V**. citeturn793791view0

So if you pull SD or ON to **+19 V**, you are taking those pins well outside their specified logic-input range. The datasheet operating examples reinforce this: quiescent current is specified with **SD = VEE + 5 V, ON = VEE**, and the alternate low-power state with **SD = VEE + 5 V, ON = VEE + 5 V**—again, not with either pin at VCC. citeturn793791view0

So the correction is:

- **Do pull SD or ON low to VEE** when you want a logic low.
- **Do not pull them high to VCC.**
- Instead, create a small **VEE-referenced “logic high” rail**, typically around **VEE + 5 V**.  
For your supplies, that would be about **-8 V**. citeturn793791view0

In other words, for your system:
- **SD low** = about **-13 V**
- **SD high** = about **-8 V**
- **ON low** = about **-13 V**
- **ON high** = about **-8 V** citeturn793791view0

So your instinct that they get pulled to rails is only **half right**:
- the **low** state can indeed be **VEE**
- the **high** state is **not VCC**, it is a small offset above **VEE**. citeturn793791view0

That is why your original pull-up to **+19 V** is the thing I’d change first.

A clean implementation is:
- generate **-8 V** from your rails
- use that as the pull-up for **SD** and **ON**
- use transistors to pull each pin down to **-13 V** as needed

And for startup sequencing from shutdown, ADI says: **bring SD high first, then pull ON low**. citeturn793791view0

If you want, I’ll draw the exact resistor/transistor network for **3.3 V logic → SD/ON using -13 V and -8 V control levels**.

[M37] ME (2026-04-20 12:23):
Ok, repeat best method then 

[M38] AI (2026-04-20 12:23):
Best method:

Use **VEE-referenced control levels**, not **+19 V** on **SD** or **ON**. For the ADA4870, valid logic high on those pins is only up to about **VEE + 5 V**. With **VEE = -13 V**, your control “high” should be around **-8 V**, and your control “low” should be **-13 V**. citeturn237801search0turn237801search1turn237801search3

So the clean scheme is:

1. **Create a small control rail at about -8 V**  
   Derive **VEE + 5 V** from your rails, for example with a zener or small regulator referenced to **-13 V**. ADI’s eval material uses this kind of approach rather than pulling the control pins to VCC. citeturn237801search1turn237801search3

2. **Pull SD up to that -8 V rail** with a resistor  
   This makes **SD = high** when released, which is the enabled state for SD. The datasheet defines SD high as approximately **VEE + 1.1 V to VEE + 5 V** and SD low as **VEE to VEE + 0.9 V**. citeturn237801search0

3. **Use a transistor to pull SD down to -13 V**  
   That gives shutdown at power-up. Since your logic input is **3.3 V**, use a proper level-shift stage so the transistor pulls to **VEE**, while the released state lets SD rise only to **-8 V**, not **+19 V**. citeturn237801search0turn237801search1

4. **Treat ON the same way**  
   ON low is the enabled condition; ON high is the low-power/off condition. The valid ON high range is also only up to **VEE + 5 V**. citeturn237801search0

5. **Sequence it correctly**  
   For startup from shutdown:  
   - hold **SD low** at power-up  
   - when ready, let **SD go high** to about **-8 V**  
   - then pull **ON low** to **-13 V**  
   ADI support notes and datasheet guidance match this sequence. citeturn237801search0turn237801search4

So, in plain terms:

- **Do not pull SD or ON to +19 V**
- **Do use -13 V for logic low**
- **Do use about -8 V for logic high**
- **Do level-shift your 3.3 V logic into that window**

A good default behavior for your case is:

- **CLK_ISOLATE = low at power-up** → transistor holds **SD = -13 V** → clock amplifier isolated
- later **CLK_ISOLATE = high** → release **SD** to **-8 V**
- then assert **ON low** to **-13 V** to run the amplifier citeturn237801search0turn237801search1

If you want, I’ll sketch the exact two-transistor network for **3.3 V in, -13 V / -8 V control, default isolated at startup**.

[M39] ME (2026-04-20 12:25):
But I only have 1 bit available 

[M40] AI (2026-04-20 12:25):
Yes — with **only one control bit**, the best method is to use that bit to control **SD only**, and hard-wire **ON** in the enabled state.

That is the simplest clean solution.

## Why this works

For the ADA4870:

- **SD low** = shutdown
- **SD high** = enabled
- **ON low** = enabled
- **ON high** = power-down / short-circuit related control state citeturn173701view0

So with one bit, do this:

- **Tie ON permanently low to VEE** through a resistor
- Use your single logic bit to switch **SD** between:
  - **VEE** for shutdown at startup
  - **VEE + 5 V** for enabled operation

That gives:

- **CLK_ISOLATE = 0** → SD low → amplifier off / clock isolated
- **CLK_ISOLATE = 1** → SD high → amplifier on

## Important constraint

Do **not** pull SD high to **+19 V**.

The datasheet says SD high must be in the range **VEE + 1.1 V to VEE + 5 V**. With **VEE = -13 V**, valid SD high is roughly **-11.9 V to -8 V**. ON high has the same kind of VEE-referenced range, and ON low is the enabled state. citeturn173701view0

So your control levels should be:

- **SD low = -13 V**
- **SD high ≈ -8 V**

## Best one-bit implementation

Use a small **level-shift transistor stage** so your **3.3 V logic** controls **SD**, but the SD pin itself only ever sees:

- **-13 V** or
- **about -8 V**

### Recommended arrangement
- Generate a small rail at **-8 V** = **VEE + 5 V**
- Pull **SD** up to **-8 V** with a resistor
- Use a transistor to pull **SD** down to **-13 V**
- Tie **ON** low to **-13 V** with a resistor

Then your one bit only has to decide whether SD is pulled low or released high.

## Functional truth table

| Control bit | SD | ON | ADA4870 state |
|---|---|---|---|
| 0 | -13 V | -13 V | Shutdown / isolated |
| 1 | -8 V | -13 V | Enabled |

That is fully aligned with the datasheet logic definitions. citeturn173701view0

## Why not use ON as the one bit?

Because ADI says when coming out of shutdown, the sequence is effectively **SD high first, then ON low**. If you only have one bit, the most robust approach is to leave **ON already low** and use **SD** as the master enable. That avoids sequencing headaches. citeturn173701view0

## Bottom line

With one bit available, the cleanest answer is:

\[
\boxed{\text{Hold ON permanently low to VEE, and use the single bit to drive SD between VEE and VEE+5 V}}
\]

If you want, I’ll sketch the exact transistor and resistor values for doing that from your **3.3 V FPGA/CPLD output**.

[M41] ME (2026-04-20 12:26):
Ok, so this but replace 19 with -8. Can’t the -8 be developed using a potential divider 

[M42] ME (2026-04-20 12:26):
[image]
[attached file: 5D31AD41-B69C-4D8D-AB11-1A0D0BB0AC34.jpeg]

[M43] AI (2026-04-20 12:26):
Yes — **the topology is broadly right if you replace the +19 V pull-up with a node around -8 V**. That matches the ADA4870 control-pin requirement, because **SD/ON logic high is only valid up to VEE + 5 V**. With **VEE = -13 V**, that means your “high” should be around **-8 V**, not +19 V. citeturn385304search0turn385304search11

On the **potential divider** question:

**A plain resistor divider is usually not the best way** to generate that **-8 V** control rail.

Why:
- the control high level wants to be reasonably defined relative to **VEE**
- divider voltage moves with supply tolerance and load current
- startup sequencing gets less predictable
- noise coupling into **SD/ON** is not helpful
- ADI’s eval approach uses a **5 V zener referenced to VEE** for this high level, not just a loose divider citeturn385304search11turn385304search13

So the better method is:

- generate **-8 V ≈ VEE + 5 V**
- do that with either a **5 V zener** from the control node to **VEE**, fed by a resistor from a more positive rail, or a small regulator/reference if you want it cleaner
- then use that **-8 V** as the pull-up source for **SD**
- pull **SD** down to **-13 V** for shutdown

For your sketch specifically:
- **R79 pull-up** should go to **-8 V**
- the transistor stage should pull **SD** to **-13 V**
- **ON** can be held permanently low to **VEE** if you only have one control bit, which is how the eval board initially enables the amp as well citeturn385304search1turn385304search11

So the direct answer is:

\[
\boxed{\text{Use }-8\text{ V, yes. Prefer a zener-derived }VEE+5\text{ node, not a bare divider.}}
\]

A divider can work in a rough sense, but for a design you want to trust, I would do:

- resistor from **+19 V** to the control-high node
- **5.1 V zener** from that node to **-13 V**
- that node becomes about **-7.9 V**
- use that as the pull-up rail for **SD/ON**

That is the cleanest one-bit approach.

If you want, I’ll draw the exact small circuit around your screenshot with suggested resistor values.

[M44] ME (2026-04-20 12:27):
So zen we cathode goes to -13

[M45] AI (2026-04-20 12:27):
No — for that scheme the **zener cathode goes to the more positive node**, and the **anode goes to -13 V**.

So:

- **series resistor** from **+19 V** to the new control node
- **zener cathode** to that **control node**
- **zener anode** to **-13 V**

That way the zener clamps the difference between the node and **-13 V** to about **5.1 V**, so:

\[
V_{node} \approx -13V + 5.1V = -7.9V
\]

Which is exactly the kind of **VEE + 5 V** control-high level you want.

If you reversed it:
- cathode to **-13 V**
- anode to node

then it would not zener-clamp the node at **-8 V** in the intended way.

So the correct orientation is:

\[
\boxed{\text{Cathode to the }-8V\text{-ish node, anode to }-13V}
\]

Example:

- **+19 V → 4.7k or 10k → control node**
- **5.1 V zener from control node to -13 V**
- **zener cathode at control node**
- **zener anode at -13 V**

That gives you a local pull-up rail of about **-7.9 V**.

If you want, I’ll size that resistor properly for one or two SD/ON pull-ups.

[M46] ME (2026-04-20 12:29):
What’s the control node?

[M47] AI (2026-04-20 12:29):
The **control node** is just the **new local rail you create for the ADA4870 control-pin “high” level**.

In your sketch, it would be the point that currently goes to **+19VA through the 10k pull-up** above the transistor.

So in your circuit:

- **remove +19VA from the top of that 10k pull-up**
- replace it with a new node, say:
  - **CLK_EN_H**
  - **SD_ON_H**
  - **VEE_PLUS_5**
  - **-8V_CTRL**

That node then does three jobs:
- gets generated from **+19V through a resistor**
- gets clamped to about **-8V** by the zener to **-13V**
- feeds the **10k pull-up** for **SD**

So physically it is the node at:

1. resistor from **+19V**
2. zener cathode
3. top of the **SD pull-up resistor**

### In words
Think of it as a **little logic-high supply rail** for SD/ON.

Not main power.  
Just a **reference pull-up rail**.

### Example
- **+19V → series resistor → control node**
- **zener cathode → control node**
- **zener anode → -13V**
- **10k pull-up to SD → from control node**

That makes the control node sit at about:

\[
-13V + 5.1V \approx -7.9V
\]

### So the answer directly
The **control node** is the **replacement for the +19V point at the top of your 10k pull-up**.

It is the new **~-8V rail**.

A good label would be:

\[
\boxed{\text{VEE\_PLUS\_5 or CTRL\_HI}}
\]

If you want, I can label your exact screenshot node-by-node in plain text.

[M48] ME (2026-04-20 12:31):
[image]
[attached file: FBDC2F36-1B13-461F-91D1-42F73B0D42AD.jpeg]

[M49] AI (2026-04-20 12:31):
Yes — **that red part is the zener arrangement I meant**, and **the yellow part is the pull-up resistor to the SD node**.

Using your colours:

- **green top line** = the more positive rail feeding the zener resistor
- **blue bottom line** = **-13 V / VEE**
- **red branch** = **series resistor + zener clamp** making the new control-high node
- **yellow branch** = pull-up from that control-high node to the **SD** pin

So the important node is the junction of:
- bottom of the **yellow resistor**
- bottom of the **red series resistor**
- **zener cathode**

That junction becomes about:

\[
V_{CTRL\_HI} \approx -13V + 5.1V = -7.9V
\]

## One correction
The **yellow resistor should not go directly to 0 V**.  
It should go to the **SD node**.

So the arrangement is:

- **red network** creates **~ -8 V**
- **yellow resistor** pulls **SD** up to **~ -8 V**
- transistor then pulls **SD** down to **-13 V** when isolate is active

## In text

### Red network
- from a positive source rail through a resistor
- into the new node
- zener from that node down to **-13 V**
- **zener cathode at the node**
- **zener anode at -13 V**

### Yellow resistor
- from that same node
- to **SD**

That means:
- transistor off → SD pulled to **~ -8 V** → enabled
- transistor on → SD pulled to **-13 V** → shutdown

## One practical note
The red network should ideally be fed from **+19 V**, not 0 V, because you need some headroom and zener current. So your sketch is conceptually right, but the top green rail wants to be your positive supply source, not ground.

## So the answer
\[
\boxed{\text{Yes, that is the right idea, provided the yellow resistor goes to SD and the zener cathode is at the created } \sim -8V \text{ node.}}
\]

A clean example would be:
- **+19 V → 4.7k → CTRL_HI node**
- **5.1 V zener from CTRL_HI node to -13 V**
- **10k from CTRL_HI node to SD**
- transistor from **SD to -13 V**

If you want, I’ll now turn your sketch into a proper little schematic in plain text with suggested values.

[M50] ME (2026-04-20 12:34):
No,

Blue - 13v
Green - 0v
Yellow - series limit R and 5v zener
Red - FET with drain connected to -8 and source to -13.

If it’s a p channel then it startup it will be held low until the fet is driven and turned off resulting in -8v

[M51] AI (2026-04-20 12:34):
Not as drawn, no.

If you want a **P-channel MOSFET** to act as the switch between **~−8 V** and **−13 V**, the **source needs to sit at the more positive side**, not at **−13 V**. For a MOSFET, the control variable is **\(V_{GS}\)**, and to turn a PMOS **off** the gate must be brought close to its **source** voltage; to turn it **on** the gate must go sufficiently **below** its source. Also, the source/body are normally tied internally in discrete MOSFETs, which is why source placement matters. citeturn114510view0

So with your proposal:

- **blue = −13 V**
- **green = 0 V**
- **yellow = resistor + 5 V zener making ~−8 V**
- **red FET with drain at −8 V and source at −13 V**

that PMOS orientation is the wrong way round for normal switching use. A PMOS used as a switch wants its **source at the more positive rail**, here **~−8 V**, not at **−13 V**. citeturn114510view0turn279398search4

There is a second issue: with **3.3 V logic** directly on the gate, if the PMOS source is around **−8 V**, then:
- gate at **0 V** gives \(V_{GS} = 0 - (-8) = +8\text{ V}\)
- gate at **3.3 V** gives \(V_{GS} = 3.3 - (-8) = +11.3\text{ V}\)

Those are both **positive**, which does **not** turn a PMOS on. A PMOS needs **negative \(V_{GS}\)** to turn on. So a lone PMOS driven directly from 0/3.3 V will not give the behavior you want. citeturn114510view0

For the ADA4870 itself, the target logic levels are still:
- **SD low** near **VEE** for shutdown
- **SD high** around **VEE + 1.1 V to VEE + 5 V** to enable
- and ADI says when coming out of shutdown, **pull SD high, then pull ON low**. citeturn114510view1

With **VEE = −13 V**, that means:
- **shutdown**: around **−13 V**
- **enabled high**: roughly **−11.9 V to −8 V**, so your **~−8 V zener rail** is fine in principle. citeturn114510view1turn279398search17

So the clean one-bit method is still:

- create **~−8 V** with the zener network
- **pull SD up** to that **~−8 V** through a resistor
- use a transistor to **pull SD down to −13 V** when `CLK_ISOLATE` says isolate
- keep **ON** hard-low to **−13 V** through a resistor if you only have one control bit. citeturn114510view1

The

[M52] ME (2026-04-20 12:35):
Ok I got the source and drain wrong way round 

[M53] AI (2026-04-20 12:35):
Yes — that’s the crux of it.

For a **P-channel MOSFET used as a pull-up switch to the ~-8 V node**, you want:

- **source to -8 V**
- **drain to SD**
- and the pull-down path or resistor arrangement taking **SD to -13 V** when the PMOS is off

So if you had **source and drain swapped**, the body diode and operating behaviour would be wrong for what you want.

The intended behaviour is:

- **startup:** PMOS **off**, SD held **low** at **-13 V**
- **later enable:** PMOS **on**, SD pulled up to about **-8 V**

That part is fine in principle.

The next thing to check is **gate drive**. For a PMOS:

\[
V_{GS} = V_G - V_S
\]

With source at about **-8 V**:
- to turn it **off**, gate needs to be near **-8 V**
- to turn it **on**, gate needs to go sufficiently **below -8 V**

So this is the real question now:

Can your control circuit drive the PMOS gate to:
- about **-8 V** for **off**
- something more negative, say near **-13 V**, for **on**

If not, the PMOS will not switch cleanly.

So yes, your correction on **source/drain orientation** is right, but the design still only works if the **gate drive is in the right voltage domain**.

Also, just to keep the function clear:

- if **SD low at startup = isolate**
- and **SD high later = enable**

then your PMOS arrangement must be such that it is **off by default** and

[M54] ME (2026-04-20 12:35):
Other than that, sound?

[M55] AI (2026-04-20 12:35):
Yes — **other than swapping source and drain, the concept is broadly sound**.

For a **PMOS high-side switch in this negative-domain sense**:

- **source** should go to the **more positive node**, so **~ -8 V**
- **drain** goes to the node you want to pull, i.e. **SD**
- **SD** then also has a path to **-13 V** when you want shutdown, or the PMOS arrangement can be used so the node rises to **-8 V** when released, depending on exactly how you finish the network

The main thing is still this:

- the ADA4870 control pins want a **high level referenced to VEE**, not to +19 V
- so generating about **VEE + 5 V ≈ -8 V** is the right idea
- and using that as the **SD pull-up high level** is the correct direction. ([analog.com](https://www.analog.com/media/en/technical-documentation/data-sheets/ada4870.pdf))

The checks I’d still make are:

1. **Gate drive polarity**  
   Make sure your logic arrangement really gives:
   - **startup:** SD held low near **-13 V**
   - **later:** transistor turns off or releases such that SD rises to **~ -8 V**

2. **Body diode direction**  
   Once source/drain are corrected, check the intrinsic diode is not creating an unwanted path between **SD** and the **-8 V** node.

3. **Gate-source voltage limits**  
   Make sure the PMOS never sees excessive \(|V_{GS}|\) during startup or rail ramping.

4. **Whether PMOS is actually the simplest device**  
   The logic function may still be easier with an **NPN/NMOS pull-down on SD** and a resistor pull-up to **-8 V**. That is usually easier to reason about for “default off, release to enable.”

So the answer is:

\[
\boxed{\text{Yes — with source/drain corrected, the }-8\text{ V control-high concept is sound.}}
\]

But I would still say **the simplest robust implementation is usually:**
- generate **-8 V**
- **10 k pull-up from -8 V to SD**
- transistor pulls **SD to -13 V** for shutdown

That is cleaner than making the PMOS itself do too much.

If you want, I’ll sketch the **simplest final one-bit circuit** from your rails and 3.3 V input.

[M56] ME (2026-04-21 11:36):
I have a 6v8 available 

[M57] AI (2026-04-21 11:36):
I wouldn’t use the **6V8 zener** here.

With **VEE = -13 V**, a 6.8 V zener would make the control-high node about:

\[
-13 + 6.8 \approx -6.2\text{ V}
\]

But the ADA4870 control pins are only specified up to **VEE + 5 V** for a valid high level. With **VEE = -13 V**, that upper limit is **-8 V**. citeturn636746view0

So:

- **SD high valid range**: **-11.9 V to -8 V**
- **ON high valid range**: **-11.2 V to -8 V** citeturn636746view0

A **-6.2 V** pull-up is therefore **too high** for both pins.

So the clean answer is:

- **5.1 V zener**: good choice, gives about **-7.9 V**
- **4.7 V zener**: also fine, gives about **-8.3 V**
- **6.8 V zener**: no, outside the specified input-high range citeturn636746view0

If 6V8 is what you physically have to hand, you could only rescue it by adding extra drop, but that starts getting scrappy. Better to use a **4V7 or 5V1** part.

[M58] ME (2026-04-21 11:48):
What’s the o channel of fdn357

[M59] AI (2026-04-21 11:48):
**FDN357N is N-channel.** onsemi lists its **channel polarity as N-Channel** and describes it as an **“N-Channel Logic Level Enhancement Mode”** MOSFET. citeturn235792search0

If you meant a different suffix, send the exact full part number.

[M60] ME (2026-04-21 11:50):
I want the p channel version 

[M61] AI (2026-04-21 11:50):
The closest **P-channel companion in that family is FDN358P**. onsemi lists it as a **single P-channel logic-level MOSFET, -30 V, -1.5 A** in the same general small-signal SOT-23/SuperSOT style family, while FDN357N is **N-channel, 30 V, 1.9 A**. citeturn661853search1turn661853search2

So, if you just want the **P-channel version to hand**, I’d start with:

- **FDN358P**

One caution: it is the natural family counterpart, but **not a perfect electrical mirror** of FDN357N. The headline differences are:
- **FDN357N:** 30 V, **1.9 A**, **90 mΩ @ 4.5 V**
- **FDN358P:** -30 V, **-1.5 A**, **200 mΩ @ -4.5 V** citeturn661853search1turn661853search2

So if your circuit is sensitive to:
- **RDS(on)**
- **gate charge**
- **current margin**
- **exact pinout/package variant**

then it is worth checking the datasheet before dropping it straight in.

For your SD pull-up switching idea, though, **FDN358P is a sensible candidate** because the current is tiny and low on-resistance is not especially critical. If you want, I can compare **FDN358P pinout vs your current footprint/symbol**.

[M62] ME (2026-04-21 13:37):
My work laptop continues to always be slow. I’m starting to wonder if it could be my networking to profile. I had it before where it got buggered up. Had it for 21!years. Is this a thing? Accumulated baggage?

[M63] AI (2026-04-21 13:37):
Yes — **that is absolutely a thing**.

What you’re describing can come from **accumulated profile baggage**, especially on a long-lived corporate account. Not because the laptop has literally had the same profile files for 21 years unchanged, but because over time you can accumulate:

- oversized **Windows user profile**
- bloated **AppData**
- excessive **login scripts / mapped drives / group policies**
- huge **Outlook OST/cache**
- old **Teams / OneDrive / browser caches**
- stale **credential manager / network shares / printers**
- roaming profile or redirected-folder weirdness
- domain policy objects that hit your account at logon
- inherited permissions / security tooling tied to your user context

So yes, a machine can feel slow because of **user-profile and enterprise environment baggage**, not just bad hardware.

The clue is usually whether the slowness is:

- worst at **login / startup**
- bad when opening **Explorer**, **Office**, **Outlook**, **Teams**
- delayed when accessing **network drives**
- better on a **fresh local admin account**
- better off-site / off VPN / off docking setup

That often points to **profile, domain, or network-linked overhead** rather than raw CPU/RAM.

A good way to think of it is in layers:

**1. Device slowness**
- ageing SSD
- low RAM
- antivirus / EDR
- thermal throttling
- too many startup apps

**2. Profile slowness**
- corrupted or bloated profile
- giant AppData
- bad shell extensions
- broken Office / Teams / OneDrive caches
- slow login/logout due to profile loading

**3. Network/domain slowness**
- login scripts
- GPO processing
- redirected folders
- mapped drives timing out
- Outlook/OneDrive/SharePoint sync
- security agents checking everything

**4. Corporate tooling drag**
- endpoint protection
- DLP
- encryption
- patch agents
- asset management
- monitoring tools

If you’ve “had it before where it got buggered up,” that fits very well with a **corrupt or bloated profile**.

What strongly suggests profile baggage:
- someone else logs onto the same laptop and it’s noticeably better
- your account on another machine is also slow
- a rebuilt profile fixes it
- Safe Mode / clean login behaves better

What strongly suggests machine-only issues:
- all users on that laptop are slow
- boot and app launch are slow even before network login
- disk usage sits at 100%
- fan constantly running

The most useful tests are:

1. **Try another user account on the same laptop**  
If that account feels much snappier, your profile is a prime suspect.

2. **Try your account on another corporate machine**  
If it is still slow, that points to profile/domain baggage.

3. **Check whether slowness is worst just after login**  
That often means GPO, network resources, or profile loading.

4. **Look at Task Manager**
Check:
- disk at 100%
- RAM pressure
- CPU pegged by Teams, Outlook, OneDrive, antivirus, or company agents

5. **Test disconnected from VPN / office network**
If it suddenly feels better, network dependencies are likely involved.

In practice, the usual fixes are:
- **new Windows profile**
- clear/rebuild **Outlook OST**
- clear **Teams cache**
- reduce startup apps
- review **OneDrive sync**
- remove dead mapped drives/printers
- IT rebuild of the machine if needed

So the answer is:

**Yes, accumulated baggage is real.**  
It is often less “21 years of one profile” and more **years of account-level cruft, caches, enterprise policies, and sync/network dependencies** building up.

A sensible way to raise it with IT would be:

> The laptop has persistent slowness that feels profile or domain related rather than just hardware. I’ve seen similar behaviour before when a profile became corrupted or bloated. Can we test with a fresh profile or alternate user login to isolate whether it’s my user context versus the machine itself?

That framing usually gets them looking in the right place.

[M64] ME (2026-04-21 14:04):
We have got Otium enterprise and after one year we finally got the server up and running, but I have no idea where to start with it. I thought it would be a good idea to contact them and see if there was any training or guidance provided in the WORK package contract the last three years but apparently nothing was included so no doubt they’re gonna try and sell us a load of hours whichI’m not too keen about. How complicated can it be and what published information is there or user guide for the system that they may be not so forthcoming with.

[M65] AI (2026-04-21 14:05):
It’s not trivial, but it also should not require a huge paid engagement just to become usable.

The published material is there. Altium has an official **Altium On-Prem Enterprise Server** documentation set, with sections for **installation/licensing/management**, the **browser interface**, **projects**, **components**, **tasks**, **process workflows**, **environment configuration**, **PLM integration**, **configuration**, **maintenance**, and **FAQs**. citeturn250244view0turn475224search12

What the server is really for, in plain terms, is four main things:
- managing **Workspace items and revisions** without overwriting old releases,
- running **managed components/libraries** with lifecycle states,
- hosting **version-controlled projects** in the Workspace,
- enforcing **company design environment standards** through the Team Configuration Center / environment configurations. citeturn250244view0

So the difficulty depends on what you want from it:

- **Easy-ish:** use it first as a **central managed library + project store**.
- **Moderate:** add **lifecycles**, **release discipline**, and **review/commenting**.
- **More involved:** add **process workflows**, **tasks**, **environment control**, and any **PLM integration**. citeturn250244view0

My honest take: if your team just wants to stop scattering symbols/footprints/projects across drives, you can get value without mastering the whole platform. The complicated bit is usually not the software itself, but agreeing your **library model, release rules, lifecycle states, permissions, and naming conventions** before everyone starts using it. That is exactly the territory the platform supports. citeturn250244view0

The best official places to start are:
- the main **On-Prem Enterprise Server** docs landing page,
- **Installing the Enterprise Server** / **Information for IT Departments**,
- **Accessing Your Workspace from Altium Designer**,
- **Building & Maintaining Your Components and Libraries**,
- **Workspace Projects**,
- **Configuration Management**. citeturn250244view0turn475224search10

There is also official Altium material beyond the product docs:
- **Training**
- **Learning Hub**
- **Webinars**
- **Forums**
- **Knowledge Base** citeturn360845view3turn250244view1turn250244view2turn250244view3

So if Altium try to push paid hours, the fair response is that there is already a substantial public documentation trail, and you want to exhaust that first.

A sensible no-nonsense rollout path would be:

1. Get one admin and one librarian account working.
2. Stand up a **single pilot Workspace library** for a narrow set of approved components.
3. Put **one non-critical project** under Workspace control.
4. Define only a minimal lifecycle at first, such as **Draft → Reviewed → Released → Obsolete**.
5. Leave workflows and environment lockdown until the basics feel stable.

That keeps it from turning into a giant “enterprise transformation” project on day one.

If you contact Altium, I’d ask very directly for:
“Please point us to the official public documentation set, recommended first-use workflow for On-Prem Enterprise Server, and any admin/user quick-start guides or webinars relevant to managed libraries and Workspace projects.”

That makes it harder for them to respond with only billable consulting.

If you want, I can turn this into a **practical first-30-days adoption plan** for your team, focused on libraries, projects, and release control rather than the full enterprise stack.

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] ME (2026-04-20 06:01):
Small tactile PCB mount and
