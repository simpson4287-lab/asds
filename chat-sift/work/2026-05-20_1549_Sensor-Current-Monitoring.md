# Sensor Current Monitoring
Date (UTC): 2026-05-20 15:49
Conversation ID: 6a0dd7b6-35a4-83eb-a5d8-b676a44c255a
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-05-20 15:49):
What the should range is useful for monitoring small current supplies to a sensor when undergoing heavy ion testing 

[M2] AI (2026-05-20 15:49):
For small sensor supply rails under heavy ion testing, the “useful” current measurement range is normally dictated by three things:

- **Expected nominal operating current**
- **Transient event magnitude/duration**
- **Whether you care about destructive latch-up detection or subtle degradation**

For imaging sensors and associated front-end electronics, a very typical strategy is:

---

## 1. Split the monitoring into two regimes

### A. Precision low-current monitoring
Used for:
- leakage tracking
- bias drift
- degradation trends
- SEE-induced analogue shifts
- standby/sleep current changes

Typical useful ranges:

| Rail Type | Typical Useful Range |
|---|---|
| Sensor substrate/bias rails | ±100 µA to 10 mA |
| Analogue bias rails | 1 mA to 100 mA |
| Digital core rails | 10 mA to 500 mA |

You generally want:
- **µA resolution**
- bandwidth from DC to maybe a few kHz
- low burden voltage
- stable temperature behaviour

For this:
- precision shunt + instrumentation amp
- or dedicated current monitor IC
- Kelvin sensing
- remote digitisation preferred

---

### B. Fast latch-up / event monitoring
Used for:
- SEL (Single Event Latch-up)
- destructive overcurrent
- rail collapse detection
- transient current spikes

Typical useful range:

| Device Scale | Recommended Full Scale |
|---|---|
| Small sensor die | 0–500 mA |
| Larger FPGA/sensor hybrid | 0–2 A |
| Aggressive protection margin | 0–5 A |

This path needs:
- fast response
- wide dynamic range
- trigger capability
- protection interlock

Heavy ion latch-up events can jump:
- from tens of mA
- to several amps
- in nanoseconds to microseconds

So the protection path is usually:
- separate from the precision telemetry path

---

# Practical Architecture (Very Common)

## Dual-path sensing

### Path 1 — High precision telemetry
Example:
- 0–100 mA FS
- 16–24 bit ADC
- slow filtered output

Tracks:
- degradation
- leakage
- radiation ageing

---

### Path 2 — Fast protection
Example:
- comparator
- FPGA threshold monitor
- digitiser trigger

Trips at:
- 2× to 5× nominal current

Can:
- shut down PSU
- latch fault
- timestamp event
- trigger waveform capture

---

# What matters most in heavy ion work

## Not absolute current range
…but:
- dynamic range
- response speed
- event capture
- rail isolation

A supply that normally draws:
- 18 mA

might suddenly:
- spike to 1.5 A during SEL

before catastrophic damage.

So designing only for “normal current” is dangerous.

---

# Typical recommendation for sensor testing rigs

A very sensible engineering setup is:

| Function | Suggested Range |
|---|---|
| Precision monitoring | ±100 mA |
| Fast event monitor | 0–2 A |
| Hardware trip | Adjustable 50 mA–2 A |
| Logging bandwidth | 10 kHz–1 MHz depending on interest |

---

# For your sort of system specifically

Given your repeated discussion around:
- CCD/imaging chains
- long harnesses
- radiation campaigns
- remote monitoring
- PXI logging

…I’d probably lean toward:

## Analogue rails
- precision ±100 mA monitor
- separate 1–2 A protection monitor

## Clock driver rails
- up to several amps possible during faults
- wider range needed

## Bias rails
- µA resolution genuinely useful
- especially for radiation-induced leakage evolution

---

# One subtle but important point

Heavy ion facilities often care about:
- **integrated event statistics**
- not just catastrophic failure

So being able to see:
- 2 mA → 3.5 mA bias leakage shift

over accumulated fluence can be scientifically valuable.

That pushes you toward:
- high-resolution telemetry
- excellent thermal stability
- careful grounding
- calibrated shunts

rather than only coarse PSU telemetry.

The built-in telemetry on many lab PSUs is often too slow/coarse alone for proper SEE characterisation.

[M3] ME (2026-05-20 15:52):
What about very small currents though. Like 10uA.  Surely seeing a much bigger window would help like x100

[M4] AI (2026-05-20 15:52):
Yes — absolutely. Once you get down into the ~10 µA regime, especially for:
- sensor leakage,
- substrate currents,
- floating diffusion leakage,
- dark current evolution,
- radiation-induced degradation,

then a “normal PSU current readback” becomes almost useless.

You typically want a deliberately amplified measurement path.

---

# Why ×100 (or more) helps

If your actual signal is:

\[
10\,\mu A
\]

and your shunt is too small, the resulting voltage is tiny.

Example:

\[
10\,\mu A \times 1\,\Omega = 10\,\mu V
\]

That is buried in:
- offset drift
- thermals
- EMI
- ground noise
- ADC quantisation

So instead you intentionally increase transimpedance gain.

---

# Typical approaches

## 1. Larger shunt resistor

Example:

\[
10\,\mu A \times 1\,k\Omega = 10\,mV
\]

Now the signal is far more measurable.

But:
- burden voltage rises
- dynamic range shrinks
- latch-up monitoring becomes impossible on same path

So this is usually only for low-current precision paths.

---

## 2. Instrumentation gain stage

Example:
- 100 Ω shunt
- ×100 amplifier

Equivalent transfer:

\[
10\,\mu A \rightarrow 100\,mV
\]

Much easier to digitise.

This is often the sweet spot.

---

# What people actually do in radiation systems

Very commonly:

| Path | Purpose |
|---|---|
| High gain | leakage/degradation |
| Low gain | operational current |
| Protection path | latch-up trip |

Because one range cannot do everything well.

---

# Dynamic range problem

Suppose:

- nominal leakage = 10 µA
- transient SEL = 1 A

That is:

\[
100000\times
\]

dynamic range.

No single clean analogue chain handles that elegantly.

So systems often:
- autorange,
- multiplex gains,
- or run parallel paths.

---

# Your intuition about “seeing the window bigger” is correct

You are basically describing:
- increasing measurement sensitivity
- improving ADC utilisation
- stretching small-signal observability

Exactly what precision electrometer-style systems do.

---

# In practice for 10 µA work

You usually start caring about:

## Input offset voltage

Because:

\[
1\,\mu V
\]

across:
- 100 Ω
= 10 nA error

…and after ×100 gain that becomes very visible.

---

# Noise becomes dominant

You then enter the world of:
- chopper amps
- zero-drift amplifiers
- guarding
- triax
- driven shields
- picoamp leakage
- PCB cleanliness
- humidity effects

At this level:
- fingerprints matter
- flux residue matters
- solder mask leakage matters

especially under radiation and humidity.

---

# Typical useful ranges for true leakage monitoring

| Resolution Goal | Practical Measurement Scale |
|---|---|
| 10 µA visibility | ±100 µA range |
| 100 nA visibility | ±1 µA to ±10 µA range |
| pA-level science | electrometer territory |

---

# For your application

I’d probably seriously consider:

## Dual-stage telemetry

### Fine monitor
- ±100 µA or ±1 mA FS
- high gain
- slower bandwidth
- precision ADC

### Operational monitor
- ±100 mA or ±1 A FS
- moderate gain

### Protection comparator
- independent hardware cutoff

That architecture is very defensible in a radiation campaign review because it clearly separates:
- scientific observability,
- operational telemetry,
- and protection functionality.

For the very small-current path, parts/categories you’d likely end up around are:
- zero-drift instrumentation amps
- transimpedance amplifiers
- electrometer-grade op-amps
- guarded layouts
- Kelvin shunts
- differential digitisation

rather than normal PSU telemetry ICs.

[M5] ME (2026-05-20 15:55):
So a 10-100x variable would provide that flexibility in most cases 

[M6] AI (2026-05-20 15:55):
Yes — **a selectable ×10 / ×100 gain path is a very sensible default** for small sensor-current monitoring.

I’d frame it like this:

| Gain | Best for | Example with 100 Ω shunt |
|---:|---|---:|
| ×10 | wider operating window | 10 µA → 10 mV |
| ×100 | small leakage visibility | 10 µA → 100 mV |

But I would not make it only continuously variable unless you really need that. For test evidence, **switched fixed gains** are usually cleaner:

- ×1 or ×10 = operational range
- ×100 = leakage/degradation range
- maybe ×1000 only if you genuinely need sub-µA visibility

The important bit is to keep a **separate fast overcurrent/latch-up trip path**, because the ×100 path will saturate quickly if a rail jumps during SEE/SEL.

So yes: **10–100× variable/selectable gain gives very useful flexibility in most cases**, provided the shunt value and burden voltage are chosen sensibly.
