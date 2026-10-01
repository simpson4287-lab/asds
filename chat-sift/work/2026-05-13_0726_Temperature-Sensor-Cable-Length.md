# Temperature Sensor Cable Length
Date (UTC): 2026-05-13 07:26
Conversation ID: 6a04279c-3d48-83eb-9d01-c0d3474d52aa
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-05-13 07:26):
When measuring a temperature sensor down to 25 m cable using a Lakeshore is that sufficient?

[M2] AI (2026-05-13 07:26):
Yes — **25 m can be perfectly sufficient with a Lake Shore**, but only if the wiring method and sensor type are appropriate.

For a **resistive sensor** such as Pt100/Pt1000/Cernox/RuO₂:

- Use **4-wire/Kelvin measurement**.  
  This largely removes cable resistance error.
- Use **twisted, shielded pairs**, ideally one pair for excitation and one pair for sense.
- Ground the shield at **one end only**, usually the instrument end.
- Keep the cable away from mains, heaters, motors, relay wiring, and fast digital signals.
- Check that the Lake Shore input supports the sensor resistance range and excitation current without self-heating.

For a **diode temperature sensor**:

- Cable resistance is usually less of a direct accuracy issue than with 2-wire RTDs, but noise pickup and leakage matter.
- Use shielded twisted pair.
- Avoid thermoelectric junctions and poor connectors if measuring small voltage changes accurately.

The main risks over **25 m** are not usually “can it measure”, but:

1. **Noise pickup**
2. **Ground loops**
3. **Cable capacitance causing unstable/noisy readings**
4. **2-wire resistance error**, if not using 4-wire
5. **Thermal EMFs at connectors**, especially for precision/cryogenic work

Rule of thumb:  
**25 m is fine for a Lake Shore if wired as 4-wire with decent screened twisted cable.**  
I would not trust a **2-wire resistive sensor** over 25 m unless the required accuracy is very loose.
