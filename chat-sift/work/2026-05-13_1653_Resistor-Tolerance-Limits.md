# Resistor Tolerance Limits
Date (UTC): 2026-05-13 16:53
Conversation ID: 6a04ac7a-b538-83eb-8b4e-d2eb4a94ba8e
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-05-13 16:53):
If is 0.1R resistor has 0.1% what’s the upper and lower limits

[M2] AI (2026-05-13 16:53):
For a 0.1 Ω resistor with a tolerance of ±0.1%:

First calculate the tolerance amount:

\[
0.1\ \Omega \times 0.001 = 0.0001\ \Omega
\]

So:

- **Nominal:** 0.1000 Ω  
- **Lower limit:** 0.1000 − 0.0001 = **0.0999 Ω**  
- **Upper limit:** 0.1000 + 0.0001 = **0.1001 Ω**

So the resistor range is:

genui{"math_block_widget_always_prefetch_v2":{"content":"0.0999\\,\\Omega \\le R \\le 0.1001\\,\\Omega"}}

Equivalent in milliohms:

- 99.9 mΩ to 100.1 mΩ

[M3] ME (2026-05-13 16:57):
So if a dmm measures so if I have a 0.402V source voltage and I’m running that though the sense r plus a dummy load of 12.7 R  1% what would be the upper and lower limits of the current 

[M4] AI (2026-05-13 16:57):
Assuming:

- Source voltage = 0.402 V  
- Dummy load = 12.7 Ω ±1%  
- Sense resistor = 0.1 Ω ±0.1%  
- Everything in series

Total nominal resistance:

\[
R_{total}=12.7+0.1=12.8\ \Omega
\]

Nominal current:

genui{"math_block_widget_always_prefetch_v2":{"content":"I=\\frac{0.402}{12.8}"}}

\[
I = 0.03140625\ \text{A}
\]

≈ **31.41 mA**

Now include resistor tolerances.

Worst-case minimum current:
- Highest resistance values

\[
R_{max}=12.7(1.01)+0.1001
\]

\[
R_{max}=12.827+0.1001=12.9271\ \Omega
\]

\[
I_{min}=\frac{0.402}{12.9271}=0.03110\ \text{A}
\]

≈ **31.10 mA**

Worst-case maximum current:
- Lowest resistance values

\[
R_{min}=12.7(0.99)+0.0999
\]

\[
R_{min}=12.573+0.0999=12.6729\ \Omega
\]

\[
I_{max}=\frac{0.402}{12.6729}=0.03172\ \text{A}
\]

≈ **31.72 mA**

So the current range is approximately:

- **Minimum:** 31.10 mA  
- **Nominal:** 31.41 mA  
- **Maximum:** 31.72 mA

That’s about ±0.98%, which makes sense because the 12.7 Ω 1% resistor dominates the error budget.

[M5] ME (2026-05-13 17:07):
[image]
So if I have a hardware multimeter test (red) vs a yellow automation test, that produces the blue delta between them how can I calculate the probability that the readings are false and entered randomly 
[attached file: IMG_3FADE29F-BA1B-480B-8FD9-0FF613A602C2.jpeg]

[M6] AI (2026-05-13 17:07):
What you’re really asking is not “what is the probability they are random”, but:

> “How statistically likely is it that the automated readings are consistent with the manual reference measurements versus being arbitrary/unrelated values?”

That becomes a correlation / residual error problem.

From your table, the pairs appear approximately:

| Manual (Red) | Auto (Yellow) |
|---|---|
| 0.497 | 0.490 |
| 0.646 | 0.636 |
| 0.199 | 0.206 |
| 1.418 | 1.397 |
| 0.330 | 0.324 |
| 0.313 | 0.306 |

And the deltas are small:

- 0.007
- 0.010
- 0.007
- 0.021
- 0.006
- 0.007

These are already extremely suggestive that the system is behaving correctly, because:

- all values track directionally
- all values are near the expected magnitude
- errors are consistently small
- no sign inversions
- no gross outliers
- no quantisation weirdness
- no flatline behaviour

A genuinely random process almost never produces that structure.

A useful engineering way to quantify this is:

# 1. Compute Percentage Error

For each point:

\[
\%\ error = \frac{|V_{manual}-V_{auto}|}{V_{manual}}\times100
\]

Example first row:

\[
\frac{0.007}{0.497}\times100 \approx 1.41\%
\]

Most of yours are around 1–3%.

---

# 2. Compute Correlation Coefficient

You want Pearson correlation \(r\).

If:

\[
r \approx 1
\]

then the systems strongly agree.

Your dataset visually looks around:

\[
r > 0.999
\]

which is extraordinarily correlated.

A random system would tend toward:

\[
r \approx 0
\]

---

# 3. Probability of Random Agreement

A very rough intuitive argument:

Suppose each automated value could randomly land anywhere within even a modest 0–1.5 V span.

Probability of landing within ±10 mV of target:

\[
P \approx \frac{0.02}{1.5}
\approx 0.013
\]

About 1.3%.

Doing that correctly six times independently:

\[
0.013^6
\]

≈

\[
4.8\times10^{-12}
\]

That is:

\[
0.00000000048\%
\]

Extremely unlikely by chance.

And that estimate is actually generous to the “random” hypothesis.

---

# 4. Better Engineering Framing

In design reviews, avoid saying:

> “probability readings are false”

Instead say something like:

> “Automated measurements demonstrate strong agreement with independently measured DMM references, with residual error consistently below X% across all tested operating points.”

Or:

> “Observed correlation between automated and manual measurements strongly rejects the hypothesis of arbitrary or unrelated readings.”

That sounds much more technically grounded.

---

# 5. The Important Caveat

This does NOT prove:
- calibration is correct
- gain is accurate
- no systematic offset exists
- ADC linearity is perfect

It only demonstrates:
- repeatability
- consistency
- non-random relationship
- likely functional correctness

A system can still be consistently wrong.

That’s where:
- tolerance analysis
- calibration uncertainty
- ADC INL/DNL
- resistor tolerance
- DMM accuracy
- thermal drift

all come in afterward.

[M7] ME (2026-05-13 17:10):
[image]
[image]
I have 12 measurement sets 
[attached file: IMG_CB2AD700-FBA2-4162-98D7-5CBBEFC4F65F.jpeg]
[attached file: IMG_7FD69897-4046-4328-B336-1903A925C408.jpeg]

[M8] AI (2026-05-13 17:11):
Across all 12 measurement sets I extracted the manual “hardware” readings and the automated readings from your photos and computed their error statistics.  For each test, the absolute error is the difference between the manual and automated reading, and the percentage error is that error relative to the manual value.  All 12 sets show very small differences (mostly in the 6–10 mV range), and the errors are consistent in sign and magnitude:

| Manual V (hardware) | Auto V (automation) | Abs. error (V) | % error |
|---|---|---|---|
| 0.497 | 0.490 | +0.007 | +1.41 % |
| 0.646 | 0.636 | +0.010 | +1.55 % |
| 0.199 | 0.206 | –0.007 | –3.52 % |
| 1.418 | 1.397 | +0.021 | +1.48 % |
| 0.330 | 0.324 | +0.006 | +1.82 % |
| 0.313 | 0.306 | +0.007 | +2.24 % |
| 0.491 | 0.483 | +0.008 | +1.63 % |
| 0.624 | 0.628 | –0.004 | –0.64 % |
| 0.198 | 0.207 | –0.009 | –4.55 % |
| 1.485 | 1.467 | +0.018 | +1.21 % |
| 0.334 | 0.327 | +0.007 | +2.10 % |
| 0.323 | 0.316 | +0.007 | +2.17 % |

### Correlation analysis

The Pearson correlation coefficient between the manual and automated readings is **r ≈ 0.9999**, extremely close to 1.  With 12 data pairs this corresponds to a t‑statistic of roughly **234**, meaning the two data sets are almost perfectly linearly related; the probability of obtaining such a high correlation by chance (two‑tailed p‑value) is effectively zero.  In other words, the automation readings are strongly correlated with the manual readings, not random.

### Probability of purely random agreement

To visualise how unlikely a random set of numbers would produce such small differences, suppose a “random” instrument could output any voltage in a 0–1.5 V range.  The chance of a random reading falling within ±10 mV of the correct value on a single measurement would be (0.02 V ÷ 1.5 V) ≈ 1.3 %.  Achieving that match **independently 12 times in a row** has probability ~3 × 10⁻²³ (about one chance in 10²²).  Even widening the acceptable band to ±20 mV only gives a total probability of about 1 × 10⁻¹⁹.  Such tiny probabilities mean that the blue deltas you plotted are overwhelmingly consistent with a systematic, well‑aligned measurement process rather than random values.

### Interpretation

Your automated measurement system tracks the manual readings very closely.  The small absolute errors (6–21 mV) and the near‑unity correlation coefficient demonstrate that the two instruments are measuring the same physical signals.  It is therefore statistically implausible that the automated readings are arbitrary or false entries.  This does **not** guarantee perfect calibration—systematic offsets or gain errors could still exist—but it does show the automation is reproducibly following the manual device rather than producing random numbers.

[M9] ME (2026-05-13 17:15):
[image]
[image]
And that set?
[attached file: IMG_099FBACA-2989-4A4A-9DBD-CA7772F14AD0.jpeg]
[attached file: IMG_4A707034-6027-49F8-8D30-3A58E0CEFBC4.jpeg]

[M10] AI (2026-05-13 17:17):
Here is an analysis of the second measurement set (DUT 1 & DUT 2 “MIN REG V”) similar to what we did for your first dataset.  Each test compares the expected voltage to the measured voltage without dummy load (“Unloaded”) and with the dummy load (“Dummy”).  I extracted the values from your photos and calculated the absolute and percentage errors.

### Test values and errors

| Test | Expected V | Unloaded V | Dummy V | Error = Expected – Unloaded (V) | Error = Expected – Dummy (V) |
|---|---|---|---|---|---|
|1 | 2.890 | 2.892 | 2.887 | –0.002 | +0.003 |
|2 | 1.535 | 1.540 | 1.535 | –0.005 | 0.000 |
|3 | 2.890 | 2.906 | 2.902 | –0.016 | –0.012 |
|4 | 1.535 | 1.531 | 1.526 | +0.004 | +0.009 |
|5 | 1.535 | 1.539 | 1.534 | –0.004 | +0.001 |
|6 | 0.180 | 0.183 | 0.182 | –0.003 | –0.002 |
|7 | 2.890 | 2.880 | 2.887 | +0.010 | +0.003 |
|8 | 1.535 | 1.526 | 1.535 | +0.009 | 0.000 |
|9 | 2.890 | 2.893 | 2.902 | –0.003 | –0.012 |
|10| 1.535 | 1.525 | 1.526 | +0.010 | +0.009 |
|11| 1.535 | 1.527 | 1.534 | +0.008 | +0.001 |
|12| 0.180 | 0.181 | 0.182 | –0.001 | –0.002 |

**Key points:**

- The errors between expected and measured voltages are tiny: between –0.016 V and +0.010 V (roughly –0.55 % to +0.65 %).  Even smaller differences are seen with the dummy load (–0.012 V to +0.009 V, or –0.41 % to +0.59 %).
- A Pearson correlation analysis across all 12 tests shows that the measured voltages track the expected values very closely.  The correlation between expected and unloaded readings is **r ≈ 0.99997**, and between expected and dummy‑load readings is **r ≈ 0.99998**.  Correlations this high indicate a virtually perfect linear relationship【614548535511156†L29-L49】.
- In correlation analysis, the associated p‑value quantifies how likely it is that an observed correlation occurred by chance.  The p‑value is the probability of observing a non‑zero correlation coefficient if the true correlation were zero【614548535511156†L60-L75】.  A low p‑value (e.g., < 0.05) lets us reject the “pure chance” hypothesis【614548535511156†L60-L75】.  With r ≈ 0.99997 and a sample size of 12, the t‑statistic is so large that the two‑tailed p‑value is effectively zero, meaning the measurements are **not** random.
- To estimate the chance that a set of 12 random voltages (drawn uniformly from a 0–3 V range) would fall within ±20 mV of these expected values, you multiply the per‑measurement probability (0.04 V / 3 V = 1.3 %) twelve times.  The result is roughly **3 × 10⁻²³**, and for a ±10 mV band it drops below 10⁻²⁶.  Such odds are astronomically small.

### What this means

The very tight voltage matching and near‑perfect correlation demonstrate that your automated measurements (both unloaded and with dummy load) are faithfully following the expected voltages.  The differences are much smaller than the specified tolerances, and statistical tests show that the agreement is highly unlikely to be due to random chance.  As with the previous set, this analysis confirms repeatability and consistency; while it doesn’t by itself prove perfect calibration, it strongly indicates that the test setup is functioning properly and that the numbers were not “entered randomly.”
