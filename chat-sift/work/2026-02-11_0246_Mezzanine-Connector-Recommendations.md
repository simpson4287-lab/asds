# Mezzanine Connector Recommendations
Date (UTC): 2026-02-11 02:46
Conversation ID: 698bed5e-1708-8388-80e8-5f5ddbdcdb6f
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-005.json

[M1] ME (2026-02-11 02:46):
Looking for mezzanine connectors that fairly high density bending in 25mm gap

[M2] AI (2026-02-11 02:46):
For a **25 mm board-to-board gap** *and* **fairly high density**, you’re basically in “tall stacking / mezzanine system” territory (not the ultra-low SlimStack stuff). A few solid connector families to look at:

### 1) Samtec “Q” families (high density + available up to 25 mm stack)
- **Samtec Q Strip® / Q Pairs®** are specifically called out with **stack heights 5–25 mm** and high I/O counts / good SI options. citeturn0search0  
**Why it fits:** good density, mature ecosystem, lots of variations (ground plane options, retention, etc.).  
**When to pick:** if you care about signal integrity and want a clean mezzanine stack at exactly ~25 mm.

### 2) TE Connectivity STRADA Mesa (25 mm stack option)
- TE’s STRADA Mesa modelling list explicitly includes a **25 mm stack height** variant. citeturn0search3  
**Why it fits:** very “backplane/mezzanine system” vibe, scalable pin counts, robust mechanical platform.  
**When to pick:** if this is more like a mini-backplane / multi-board architecture than a tiny embedded stack.

### 3) Hirose FX23LH / related (floating, 8–30 mm stacking heights)
- Hirose’s own series listing describes a **0.5 mm pitch floating board-to-board**, **stacking height 8–30 mm**, with decent floating range to tolerate misalignment. citeturn0search5turn0search9  
**Why it fits:** if by “bending” you mean the assembly isn’t perfectly rigid and you need compliance/tolerance.

---

## About “bending in a 25 mm gap”
If you literally mean **the interconnect needs to flex** (boards moving relative to each other), a rigid mezzanine connector is usually the *wrong* tool. In that case, typical approaches are:
- **Board-to-board + compliance (floating connector family)** (e.g., Hirose floating style above). citeturn0search5  
- Or go to **cabled mezzanine** (micro-coax / twinax / IDC) and use stiffeners/spacers for mechanical.

---

## Quick shortlist recommendation
- **Best “straight shot” 25 mm mezzanine, high density:** **Samtec Q Strip / Q Pairs** citeturn0search0  
- **Best if you need tolerance/compliance:** **Hirose FX23LH floating (8–30 mm)** citeturn0search5turn0search9  
- **Best if it’s a more formal backplane/mezz system:** **TE STRADA Mesa 25 mm stack** citeturn0search3  

If you tell me **(a)** approximate pin count, **(b)** whether it’s high-speed (LVDS/SerDes) or mostly DC/slow IO, and **(c)** whether you need **right-angle** or **vertical stack**, I can narrow to 2–3 exact series/part-number patterns that are actually practical to route and assemble.
