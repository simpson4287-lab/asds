# Soldering Temp for THT
Date (UTC): 2026-01-28 16:53
Conversation ID: 697a3ef8-cb64-8325-99f4-b3c437ecf394
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-004.json

[M1] ME (2026-01-28 16:53):
[image]
What temp should be used with this solder and through hole soldering 
[attached file: IMG_CE24DFE2-CA40-4F1B-B742-D475092B8506.jpeg]

[M2] AI (2026-01-28 16:53):
From the label, this is **Loctite 362**, **99C / 5C alloy**, **Ø0.5 mm**. That alloy is **Sn99.3 / Cu0.7 (lead-free SAC-type, no silver)**.

### Melting characteristics
- **Solidus / liquidus:** ~**227 °C**  
  (sharper melt than SAC305, but slightly higher wetting temp)

### Recommended iron temperatures (through-hole)
For hand soldering with a temperature-controlled iron:

- **Standard through-hole:** **350–370 °C**
- **Large pads / ground planes / thick leads:** **370–390 °C**
- **Fine pins, light copper:** **340–350 °C**

### Practical guidance
- Use the **lowest temperature that gives a 1–2 s wetting time**.
- If joints look dull or take >3 s to flow → increase temperature or improve flux.
- If pads discolor or flux burns instantly → temperature too high.

### Tips specific to Sn99Cu
- Wetting is **slower than leaded** and slightly slower than SAC305 → temperature matters.
- Extra **flux** (no-clean or RMA) helps significantly for THT.
- Keep tip well-tinned; Sn99Cu is less forgiving of oxidised tips.

### Quick recommendation
If you want a single safe setting for most through-hole work:

**Set the iron to ~370 °C**, adjust ±20 °C depending on joint size and thermal mass.

[M3] ME (2026-01-28 16:54):
Flux needed?

[M4] AI (2026-01-28 16:54):
**Yes — flux is recommended**, even though this wire contains a flux core.

### Why additional flux helps (Sn99Cu / 99C)
- **Slower wetting** than leaded solder
- **Higher surface oxidation** sensitivity
- Through-hole pins and plated barrels often have oxide or contamination

The core flux alone is often **marginal** for clean, fast joints.

### When you can skip extra flux
- Brand-new PCB
- Bright, clean component leads
- Small thermal mass
- Iron ≥ 360 °C and good tip condition

Even then, results are usually better *with* flux.

### What flux to use
For through-hole electronics:

- **No-clean flux (preferred)**  
  - ROL0 / ROL1 type
  - Liquid pen or syringe
- **RMA flux** (acceptable, but clean after)

Avoid:
- Plumbing / acid flux (corrosive, destructive)
- Water-soluble unless you will wash thoroughly

### How to apply
- Light **pre-wet** of the pad and lead
- Do not flood — a thin film is enough
- Re-flux if reworking a joint

### Rule of thumb
If the joint does not fully wet in **≤2 seconds**, add flux before raising temperature.

For Sn99Cu, **extra flux improves joint quality more than extra heat**.
