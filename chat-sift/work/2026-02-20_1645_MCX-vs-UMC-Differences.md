# MCX vs UMC Differences
Date (UTC): 2026-02-20 16:45
Conversation ID: 69988f9e-3444-8389-a5ef-bf6f5efe2a19
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-02-20 16:45):
What’s the difference between mcx and umc 

[M2] AI (2026-02-20 16:45):
**Short answer:**  
- **MCX** = conventional miniature coax connector (robust, hand-connectable)  
- **UMC** = ultra-micro board connector (very tiny, fragile, usually for internal use)

Now the engineering detail.

---

## Mechanical / Physical

### MCX
image_group{"layout":"carousel","aspect_ratio":"1:1","query":["MCX coaxial connector male female","MCX PCB jack connector","MCX right angle connector","MCX RF connector cable"],"num_per_query":1}

- Snap-on push-pull coupling  
- Outer diameter ≈ **3.6 mm**
- Fairly robust mating cycle (typically **≥500 cycles**)  
- Cable-to-board or cable-to-cable friendly  
- Hand-mateable in production and lab  
- Good strain tolerance

**Typical use:** test gear, RF modules, semi-permanent cabling.

---

### UMC (aka Hirose U.FL / similar class)
image_group{"layout":"carousel","aspect_ratio":"1:1","query":["UMC coaxial connector PCB","Hirose U.FL micro RF connector","U.FL PCB socket close up","ultra micro RF connector board"],"num_per_query":1}

- Ultra-low profile board connector  
- Mated height ≈ **2–3 mm**  
- Extremely small footprint (~2 mm class)  
- Fragile — limited mating cycles (**~30 typical**)  
- Requires vertical snap tool ideally  
- Not designed for repeated manual reconnection  
- Poor cable strain tolerance

**Typical use:** internal antenna leads in phones, Wi-Fi cards, compact modules.

---

## Electrical Performance

| Parameter | MCX | UMC |
|---|---|---|
| Impedance | 50 Ω (also 75 Ω variants) | 50 Ω |
| Frequency range | DC → ~6 GHz typical | DC → ~6 GHz typical |
| Insertion loss | Low | Slightly higher (short path) |
| Power handling | Higher | Low |
| VSWR | Good | Good if layout clean |

**Key insight:** electrically similar at moderate GHz, but mechanically very different.

---

## When to Choose Which (engineering guidance)

### Choose MCX if:
- You need **repeat connect/disconnect**
- There is **any cable movement**
- Lab or field access is required
- Higher mechanical robustness needed
- You may probe/debug frequently
- Cable length is non-trivial

**For PixelBurn-style rigs:** MCX is usually the safer choice.

---

### Choose UMC if:
- Space is extremely constrained
- Connection is **semi-permanent internal**
- Very low profile required
- Cable will be strain-relieved nearby
- Not user-accessible

**Typical:** internal antenna pigtails.

---

## Practical risk notes (important)

**UMC pitfalls:**
- Pads rip off PCB easily
- Side-load kills connector
- Rework is painful
- Needs strict keep-out for mating tool
- Cable pull force is very low

**MCX advantages:**
- Much more forgiving mechanically  
- Easier assembly  
- Better for prototypes and lab work

---

## My recommendation for your typical work

Given your environment (high-reliability test systems, long cables, lab handling):

👉 **Default to MCX**  
👉 Use UMC only when board area is critically constrained and connection is internal.

---

If helpful, I can next produce:

- 📐 MCX vs UMC footprint keep-out comparison  
- 🔧 Best high-temp cable pairings for each  
- 📊 Signal integrity impact at 20–130 MHz (relevant to your LVDS/CCD work)

Just say the word.

[M3] ME (2026-02-20 16:46):
What about mmcx 

[M4] AI (2026-02-20 16:46):
**MMCX** sits neatly between MCX and UMC in both size and robustness.

If MCX is “miniature and rugged” and UMC is “ultra-tiny but fragile,” then **MMCX is the compact, still-serviceable middle ground.**

---

## MMCX — what it is
image_group{"layout":"carousel","aspect_ratio":"1:1","query":["MMCX coaxial connector male female","MMCX PCB jack connector","MMCX right angle RF connector","MMCX snap on connector cable"],"num_per_query":1}

**Key traits**

- Snap-on push coupling (like MCX)  
- 50 Ω characteristic impedance  
- **Outer diameter ≈ 2.4 mm** (smaller than MCX)  
- Supports **360° rotation when mated**  
- Typical mating cycles: **~500**  
- Hand-mateable  
- Reasonably robust for production use  

---

## Size comparison (practical engineering view)

| Connector | OD class | Robustness | Typical cycles | Profile |
|---|---|---|---|---|
| **MCX** | ~3.6 mm | High | ≥500 | Medium |
| **MMCX** | ~2.4 mm | Medium-high | ~500 | Low |
| **UMC (U.FL class)** | ~2.0 mm footprint | Low | ~30 | Ultra-low |

**Mental model:**

- MCX → chunky and forgiving  
- MMCX → compact but still serviceable  
- UMC → tiny and delicate

---

## Electrical performance

For your frequency regime (20–25 MHz video, LVDS clocks, etc.):

✅ All three are electrically excellent  
✅ No meaningful SI difference at these frequencies  
✅ Loss differences only matter in multi-GHz work

MMCX typically rated to **6 GHz+**, so you have huge margin.

---

## Mechanical behaviour (important nuance)

### MMCX strengths

- Much smaller than MCX  
- Still reasonably robust  
- Rotational freedom reduces cable stress  
- Good compromise for dense boards  
- Field-disconnectable

### MMCX weaknesses

- Less pull strength than MCX  
- Can wear faster under heavy lab use  
- Not as forgiving to side-load as MCX  
- Smaller solder anchor area

---

## Where MMCX shines (engineering use cases)

MMCX is excellent when you need:

- Moderate board density  
- Repeated mating capability  
- Cleaner panel packing  
- Coax test access on dense PCBs  
- Compact RF modules  
- Instrumentation front-ends

---

## For your PixelBurn / CCD ecosystem

Based on your typical constraints:

**Best default hierarchy**

- 🟢 Heavy lab / long cables → **MCX**
- 🟡 Dense but still serviceable → **MMCX**
- 🔴 Internal semi-permanent → **UMC**

Given your:

- long coax runs  
- oven environments  
- frequent debug  
- in-house builds  

👉 **MCX still wins for maximum robustness**  
👉 **MMCX is very attractive for high-density mezzanine or front panels**

---

## My candid engineering take for your designs

Use **MMCX** when:

- you’re fighting front-panel density  
- cable strain is controlled  
- connectors are still user-accessible  
- you want a professional compact feel

Stick with **MCX** when:

- cables are long or heavy  
- the environment is rough  
- reliability margin matters most

---

If you want, I can next recommend **specific high-temp MMCX cable assemblies (125 °C capable)** that would fit your burn-in environment.

[M5] ME (2026-02-20 19:22):
[image]
I’m monitoring the fast signal at the output but also want an intermediate monitor where I’ve placed sk5. What resistor shall I put in series?
[attached file: IMG_DD6B35E2-EF87-4C59-B4E6-2613B5E4C068.jpeg]

[M6] AI (2026-02-20 19:23):
For an **intermediate “tap” monitor** like **SK5**, the goal is to **isolate the stub** so it doesn’t ring / distort the main fast net.

### Default recommendation (scope probe / high-Z monitor)
- **33 Ω in series** (at the **branch into SK5**, placed **right at the main net**)  
This is the classic “stub damper”: big enough to tame the stub’s LC, small enough that a 10× probe (≈10 MΩ // a few pF) barely loads the node.

**If you want to be extra safe:** **47 Ω** is also totally fine and often my “sleep at night” value for fast edges.

### If SK5 will sometimes be a 50 Ω coax feed (scope set to 50 Ω)
- Use **49.9 Ω series** into SK5 **and assume 50 Ω termination at the instrument**.  
That makes the SK5 branch behave nicely and prevents the coax stub becoming a nasty resonator.

### Practical notes
- Put the resistor **in series with the SK5 branch**, not in the main signal path.
- Keep the track from the tee-point to SK5 **as short as physically possible**.
- If you’re unsure how it’ll be used, make it **DNP-able** (fit 0 Ω / 33 Ω / 49.9 Ω options).

**So: fit 33 Ω as your default.** If SK5 is definitely a coax-to-50Ω scope point, fit **49.9 Ω**.
