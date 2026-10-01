# 40-Core Cable Search
Date (UTC): 2026-04-30 08:27
Conversation ID: 69f31257-4310-83eb-abfd-470e0383d039
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-30 08:27):
I’m oooking for a 40 core cable 16/0.2

[M2] AI (2026-04-30 08:27):
I’ll treat this as a UK parts-sourcing question for **40-core multicore cable, 16/0.2 mm conductors**. I’ll check what’s actually available rather than guessing equivalents.

[M3] AI (2026-04-30 08:27):
For **40-core at 16/0.2**, the key thing is that **16/0.2 mm is normally treated as ~0.5 mm² conductor area**. So useful search terms are:

**“40 core 0.5mm² multicore cable”**  
**“40 x 0.5mm² control cable”**  
**“LAPP UNITRONIC LiYY 40x0.5”**  
**“ÖLFLEX 40 core 0.5mm² YY cable”**

A direct match I found is:

**LAPP UNITRONIC® LiYY 40 x 0.5 mm² — part 0028540**  
This is a **40-core, stranded copper, unshielded data/control cable**, grey PVC, OD about **15.8 mm**, rated **0.5 kV**. TME lists it as **LAPP 0028540**. citeturn579413search1

That is probably the closest off-the-shelf equivalent to “40 core 16/0.2”.

One caveat: if you specifically need **Def Stan 61-12 Part 5 16/0.2**, 40-core does **not** appear to be a normal standard size. The published Permanoid Def Stan table shows 16/0.2 Part 5 up to **25 cores unscreened**, and up to **32 cores collectively screened**, but not 40 cores. It also confirms 16/0.2 is rated around **2.5 A** in that Def Stan family. citeturn186801view0

So I’d choose based on what matters:

| Need | Best search/spec |
|---|---|
| Exactly 40 cores | **40 x 0.5 mm² control / LiYY / YY cable** |
| Exactly 16/0.2 Def Stan style | You may need **25-core + extra cores**, **32-core screened**, or a **bespoke cable** |
| Screened cable | Search **40 x 0.5 mm² CY / screened control cable** |
| Flexible industrial cable | Search **LAPP ÖLFLEX 40G0.5** or **40 x 0.5 YY cable** |

For your use, I’d probably search/buy it as **“40 x 0.5 mm² multicore control cable”**, not “16/0.2”, because suppliers are much more likely to index it by CSA.

[M4] ME (2026-04-30 08:30):
What mm2 is a 7/0.2

[M5] AI (2026-04-30 08:30):
A **7/0.2** conductor means:

**7 strands**, each **0.2 mm diameter**.

Area per strand:

\[
A = \pi r^2 = \pi \times 0.1^2 = 0.0314 \text{ mm}^2
\]

Total area:

\[
7 \times 0.0314 = 0.22 \text{ mm}^2
\]

So **7/0.2 ≈ 0.22 mm²**.

In practical cable terms, it’s often treated as roughly equivalent to **0.22 mm²**, sometimes rounded near **0.2 mm²**, depending on the cable standard.
