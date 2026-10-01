# IC Footprint Pad Shape
Date (UTC): 2026-04-06 10:20
Conversation ID: 69d388cc-713c-838e-87af-26a13c0bdfa3
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-06 10:20):
Are ic footprint pads typically rounded?

[M2] AI (2026-04-06 10:20):
Usually yes, or at least **rounded at the corners**.

For IC footprints in PCB CAD:

- **SMD pads** are commonly **rounded-rectangle** pads these days
- Older libraries often use **plain rectangular** pads
- **Through-hole IC pads** are often **round** or **oval**, with **pin 1 sometimes square** for orientation

For most modern assembly work, **rounded-rectangle SMD pads are very normal** and often preferred because they can help with solder paste release and reduce sharp-corner issues. But **rectangular pads are still perfectly common** and not wrong.

In Altium, if you’re looking at a footprint and wondering what’s “normal”:
- gull-wing ICs: usually **rounded-rectangle or rectangle**
- BGAs: **round**
- through-hole DIL/DIP: **round or oval**, often **square pin 1**

So the answer is: **yes, often rounded, but not always**. If you want, send a screenshot of the footprint and I’ll tell you whether it looks sensible.
