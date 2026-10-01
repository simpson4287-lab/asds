# Relay Contact Configuration
Date (UTC): 2026-03-24 21:47
Conversation ID: 69c30627-705c-838d-acc3-4273fd0b518d
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-24 21:47):
[image]
[attached file: IMG_F7437A31-9984-40D2-9D51-C0A66C4089A0.jpeg]

[M2] ME (2026-03-24 21:47):
One on the left 

[M3] AI (2026-03-24 21:47):
If you mean the relay contact on the left-middle of the sheet, the one labelled **RL1C**, then as drawn:

- the **common** is the moving wiper, coming from the left/lower-left path
- in the **rest / de-energised** state it appears to be touching the **upper contact**
- when the relay is **energised**, it will switch to the **lower contact**

So the real question is whether that default state matches your intent.

From what I can see, that means:

- **default path** goes up toward the **R34 / IC14 raw ODI sample** route
- **energised path** goes down toward the **IC7 / raw differential OSV sample** route

So:

- if you want **ODI/raw monitor as the normal state**, it looks right
- if you want **the lower path as the normal state**, it is backwards

The main trap here is not the drawing style, but whether the symbol’s **NC/NO mapping matches the actual relay pinout/footprint**. That is the bit I would verify carefully, because relay symbols often look “right” while the footprint pins are swapped.

Best check:
1. identify the relay datasheet **COM / NC / NO**
2. confirm the schematic symbol pins map to those correctly
3. confirm what state your transistor drive leaves the relay in at power-up

If you want, I can mark on your image exactly which node is COM, which is NC, and which is NO.

[M4] AI (2026-03-24 21:48):
Looks **basically right**, assuming your intent is:

- **relay de-energised:** the blade sits on the contact it’s drawn touching
- **relay energised:** it flips to the other throw

From your schematic, **RL1C is currently drawn in the lower position**, so in its normal state it will connect the **left/common node down into the lower path** going toward the diff/sample circuitry, **not** the upper path.

So the key check is this:

- If you want **normal operation = lower path selected**, it looks right.
- If you want **normal operation = upper/raw direct path selected**, then it is the wrong way round and the throws need swapping.

The usual gotcha here is not the relay itself, but **which pin you’ve called COM / NC / NO in the footprint and symbol mapping**. That is worth double-checking against the datasheet, because schematically it can look right while the PCB pins end up reversed.

Also, one design sanity point: for this kind of measurement switching, it is usually safer that the **default unpowered state** lands in the **least intrusive / safest measurement mode**, so the system does not accidentally load or reroute OS when the relay drive is absent.

If you want, I can mark up on your screenshot exactly which node is **COM**, **NC**, and **NO** for RL1C.

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] ME (2026-03-24 21:48):
No I mean should that single snooker take its input before the follower

[A2] AI (2026-03-24 21:48):
Ah — yes, I think you mean the **single-ended sampler/buffer on the right**.

In general: **yes, taking it before the follower is usually the cleaner choice** if your aim is to observe the **true raw OS node**.

Why:

- the **follower stage is already loading / conditioning** the node, even if lightly
- once you take it **after** the follower, you are no longer looking at the genuine detector output node, you are looking at the **buffered interpretation** of it
- if the purpose of that single-ended path is **diagnostic/raw access**, then it really wants to come from the **same raw node** as early as possible

So the usual rule is:

- **before follower** = best for **authentic raw node observation**
- **after follower** = best for **stable, low-impedance, easier-to-export version**

For your schematic specifically, I’d separate the intent like this:

- **RAW DIFF OSV SAMPLE**: can reasonably be after the follower/conditioning stage, because that path is about making the signal measurable and transportable
- **RAW (SE) OSV SAMPLE / probe point**: if you want this to mean *raw*, it really ought to be taken **before the follower**

The caution is this:
if you tap before the follower, that single-ended monitor must be **very light loading**. Otherwise it starts defeating the point of having a raw observation node in the first place.

So I would only do that if the single-ended stage is:

- very high input impedance
- low capacitance
- physically close
- optionally isolated/switched out when not in use

That last point matters a lot for CCD-style nodes. A “raw” monitor that is always hanging on the node can subtly spoil exactly what you were trying to inspect.

My recommendation here:

- if the right-hand single-ended route is meant as a **true debug/raw access point**, take it **before the follower**
- if it is meant as a **practical exported monitor signal**, take it **after the follower**
- best arrangement of all: keep the **diff/export path after the follower**, and keep the **single-ended raw probe path before it**, ideally through a resistor / switch / relay isolation arrangement

So conceptually:

**OS_RAW node**
→ optional high-Z raw SE monitor  
→ follower / conditioning  
→ exported diff or robust monitor path

That is the more defensible architecture.

If you want, I can sketch exactly where I’d move that pickup on your shown circuit.
