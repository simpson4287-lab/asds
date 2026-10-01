# LVDS Twisted Ribbon Shielding
Date (UTC): 2026-06-09 12:40
Conversation ID: 6a2809b0-f514-83eb-86c2-16cb82814d53
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-06-09 12:40):
Using twisted ribbon for a long data run of lvds. It may work on its own but to go one further could it be sandwiched in two grounded sheet of copper foil?

[M2] AI (2026-06-09 12:40):
Yes, **it could be done**, but I would be cautious: sandwiching twisted ribbon LVDS between two grounded copper foils may make the cable **quieter externally**, but it can also make the LVDS link **worse electrically** if it changes the cable impedance too much.

For LVDS, the priorities are:

1. **Controlled-ish differential impedance**
2. **Low skew between + and −**
3. **Good return/reference path**
4. **Low common-mode noise**
5. **Avoiding excessive capacitance over a long run**

A twisted pair ribbon already helps because the two LVDS conductors mostly reference each other. Adding grounded copper foil above and below turns the structure into something closer to a **shielded stripline**, which increases capacitance to ground. That can:

- lower the differential impedance
- slow the edges
- increase driver loading
- increase attenuation over distance
- make the LVDS receiver margin worse

So the foil sandwich is not automatically an upgrade.

### The main risk

If the foil is very close to the twisted pairs, the cable capacitance can go up significantly. LVDS drivers are small-swing current-mode outputs, usually expecting around **100 Ω differential termination** at the receiver. If your cable ends up looking like 60 Ω, 50 Ω, or worse, the link may still “work” at low speed, but reflections and eye margin can become ugly.

For a long run, that matters more than people expect.

### Better approach

A better practical order would be:

**Best:** proper shielded twisted pair cable, ideally around **100 Ω differential**, e.g. Cat5e/Cat6 pair, twinax, or proper LVDS cable.

**Second-best:** twisted ribbon pairs with a nearby ground conductor or ground pair, for example:

```text
GND  LVDS+  LVDS-  GND  GND  LVDS+  LVDS-  GND
```

or if the cable is twisted pair ribbon:

```text
pair, ground, pair, ground, pair, ground
```

**Foil shield:** useful if you wrap or surround the whole cable bundle, but keep it as a **shield**, not as a very close capacitive plate pressed tightly against every pair.

### If you do use copper foil

I would avoid a tight copper-foil sandwich pressed directly onto the ribbon unless you can test it. A safer version is:

```text
copper foil / insulation / twisted ribbon / insulation / copper foil
```

with some spacing, rather than foil directly against the wire insulation.

Also:

- bond the foil to chassis/ground at least at one end
- for high-frequency shielding, bonding at both ends is usually better
- but if there is a ground-potential difference between ends, both-end bonding can create shield current
- avoid using the foil as the actual signal return path
- do not connect foil in a way that lets large DC/supply currents flow through it

### My instinct for your application

For a long LVDS run, I would **not start with the copper sandwich**. I would first use:

```text
proper twisted pairs
100 Ω termination at receiver
ground reference alongside
shield around the cable bundle if needed
```

The foil sandwich is more of an EMC experiment than a guaranteed signal-integrity improvement. It may help radiated noise, but it could easily reduce LVDS margin by loading the line.

If you can scope it, compare the LVDS eye or at least the received waveform with and without the foil. If the edges get noticeably slower or the amplitude collapses, the foil is doing more harm than good.

[M3] ME (2026-06-09 12:42):
It’s for a prototype to see if signals can make it 25m. If it works it gives early confidence, if it doesn’t it flags risk 

[M4] AI (2026-06-09 12:42):
Yes — for that purpose, it is a **reasonable prototype experiment**, as long as you interpret the result correctly.

For a 25 m LVDS run, the question is not “is this the final cable design?” but:

> “Can this signalling approach survive the length with some practical shielding and grounding?”

In that context, a copper-foil sandwich could be useful as a **risk-reduction test**, especially if you build it in a way that does not accidentally make the cable much worse than the final version would be.

### I would test it in three stages

Start simple:

```text
twisted ribbon only
```

Then try:

```text
twisted ribbon + one grounded copper foil sheet
```

Then:

```text
grounded copper foil / insulation / twisted ribbon / insulation / grounded copper foil
```

That gives you useful information:

| Result | Interpretation |
|---|---|
| Works with ribbon only | Very good early confidence |
| Fails with ribbon only, works with foil | Signal may be viable, but EMC/reference/shielding matters |
| Works without foil, fails with foil | Foil is adding too much capacitance/loading |
| Fails both ways | Real risk: cable choice, speed, termination, drive strength, skew, or receiver margin |

### Important: do not press bare foil directly onto the cable

Use insulation between the foil and ribbon. For example:

```text
copper foil
polyester tape / Kapton / plastic sheet
twisted ribbon
polyester tape / Kapton / plastic sheet
copper foil
```

The closer the foil is to the conductors, the more it behaves like a capacitive plate. That can make the test pessimistic compared with a proper shielded twisted-pair cable.

### Grounding approach

For a prototype, I would probably test both:

```text
foil grounded at receiver end only
```

and:

```text
foil grounded at both ends
```

For signal integrity and high-frequency shielding, both ends often performs better. For ground-loop/current concerns, one end can be safer. Testing both tells you which failure mode you are actually fighting.

If the two ends are powered from related lab supplies or the same rack, bonding both ends is probably fine for a bench prototype. If they are physically separate systems with possible ground offset, be more careful.

### Make the test deliberately informative

At 25 m, do not just send a static pattern. Send something aggressive:

```text
10101010...
```

and also pseudo-random data if possible. The alternating pattern stresses edge rate and bandwidth; pseudo-random data exposes baseline wander, jitter, and marginal timing.

Also test at:

- actual intended data rate
- higher than intended data rate, if possible
- worst-case supply voltage
- worst-case expected cable routing
- with nearby noisy equipment switched on, if relevant

### Termination matters more than the foil

Make sure you have the **100 Ω differential termination at the receiver end**. For LVDS that is usually the big one.

Basic topology:

```text
LVDS driver  ───────────── 25 m pair ───────────── 100 Ω ─ LVDS receiver
```

Do not add random termination at both ends unless the driver/interface specifically expects it. Normal point-to-point LVDS is receiver-terminated.

### My practical recommendation

For your prototype, I would do this:

```text
Use the twisted ribbon.
Add a ground conductor or ground pair alongside each LVDS pair if available.
Test without foil first.
Then add foil shield around or either side of the whole ribbon.
Keep insulation between foil and ribbon.
Bond foil to chassis/0V at receiver end first, then try both ends.
```

If it works over 25 m with that setup, I’d take that as **useful early confidence**, but not full design proof.

If it fails, I would not immediately conclude “LVDS cannot do 25 m.” I would conclude:

> “This cable construction may not be good enough; we need controlled 100 Ω shielded twisted pair/twinax, lower edge rate, better grounding, or a repeater.”

So yes — as a prototype confidence test, it is absolutely worth doing. Just test **with and without** the foil, because the foil could either save the link or be the thing that breaks it.
