# Fluctuate pulse on rail
Date (UTC): 2025-10-14 12:36
Conversation ID: 68ee43cf-bc1c-832c-88de-ee929b6cf6c3
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-000.json

[M1] ME (2025-10-14 12:36):
[image]
How can I get the function generators pulse to fluctuate on the 12v rail
[attached file: A429CBD1-269A-4B8F-A730-238DEFF11E01.jpeg]

[M2] AI (2025-10-14 12:37):
You’re trying to “ride” a pulse on top of a stiff 12 V DC rail. In the simulator the 12 V source is **ideal (zero output impedance)**, so if you just tie the function-generator output to the same node, the 12 V source clamps the node and your pulse can’t move it.

Two easy ways to make the rail fluctuate:

### A) Inject ripple into the 12 V rail (keep the 12 V source)
1. Break the +12 V line and insert a small series resistor (e.g., 0.5–5 Ω) between the supply and the rail node you want to disturb.  
2. AC-couple the function generator into that rail node with a capacitor: FG OUT → series capacitor (e.g., 1–100 µF depending on frequency) → rail node. FG GND → circuit GND.  
3. Set the FG **offset = 0 V** and choose the pulse **amplitude** you want for the ripple.  
4. Pick C so its reactance at the pulse’s fundamental is **≪ the series resistor** (|Xc| ≪ Rs) to inject most of the FG voltage onto the rail.  
   - \(X_C = \frac{1}{2\pi f C}\)

This gives a 12 V rail plus a small superimposed pulse/ripple.

### B) Make the pulse itself sit at 12 V (don’t keep the DC source on that node)
Use the function generator **instead of** the DC source and add a **DC offset**:
- Set FG **DC Offset = 12 V**.  
- Set pulse **amplitude** to the ripple you want (e.g., 1 Vpp → 11.5–12.5 V).  
- Leave FG ground at circuit ground.

If you keep the 12 V source connected while doing this, they’ll fight—so disconnect the DC source on that node for method B.

**Typical quick setup (method A):**
- Rs = 1 Ω in series with the 12 V source.  
- C = 10 µF–100 µF for kHz-range pulses.  
- FG: 0 V offset, 0.5–1 V amplitude pulse.  

Scope the rail node after Rs—you’ll see the 12 V line “wiggle” by the injected amount.
