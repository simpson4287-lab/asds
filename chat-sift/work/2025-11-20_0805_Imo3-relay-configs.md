# Imo3 relay configs
Date (UTC): 2025-11-20 08:05
Conversation ID: 691ecbc9-864c-832a-bb38-83e41f7e4a73
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-001.json

[M1] ME (2025-11-20 08:05):
Does the imo3 relay come in alternative configs?

[M2] AI (2025-11-20 08:05):
Yes — the product_entity["turn0product4","TE Connectivity IM03JR (IM03) relay"] and the wider “IM” series from entity["brand", "AXICOM", 0] / entity["organization", "TE Connectivity", 0] does indeed come in multiple configurations. Here’s a breakdown of how they vary based on the datasheet and product listings:

---

### ✅ Evidence of alternative configurations  
From the datasheet for the IM series:  
- “The relays are available in **non-latching or latching** configurations …” citeturn0search6turn0search3turn0search7  
- Also: “Available as through-hole and surface-mount type (J-Legs and Gull Wings) …” citeturn0search3turn0search7  
- The product code table shows variants: e.g., IM03GR, IM03JR, IM03NS, IM03TS etc, noting differences in coil voltage, mounting style, “performance type” (standard, high dielectric, high current, high contact stability) etc. citeturn0search7turn0search3  
- Example spec sheet for the IM03GR shows: 5 V coil, DPDT (“2 Form C”) contact arrangement, surface-mount gull wing terminals. citeturn0search1turn0search4  

---

### 🛠 What variations you can select / specify  
Here are the typical configurable parameters for the IM03 / IM series:  

- **Coil voltage**: e.g. 1.5 V, 3 V, 4.5 V, 5 V, 6 V, 9 V, 12 V, 24 V etc. citeturn0search7turn0search3  
- **Mounting style / terminal style**: surface-mount gull-wing (SMT), J-leg SMT, through-hole standard, through-hole narrow version. citeturn0search7turn0search3  
- **Performance type / special features**: standard, “high dielectric” version, “high current” version, “high contact stability” version etc. citeturn0search7turn0search0  
- **Contact arrangement / poles**: The IM03 version is 2 form C (i.e., DPDT) for the standard case. But the broader IM series has various contact configurations. citeturn0search3turn0search7  
- **Latching vs Non-latching (and/or bistable)**: Some variants are latching (single coil bistable) or non-latching (monostable). citeturn0search6turn0search7  

---

### 🔍 Practical implications for your design  
Given your engineering background (electronics, PCB design etc), here’s what you should check/decide when picking an IM03-series (or variant):  
- Choose the correct **coil voltage** for your drive circuit.  
- Decide whether you need **latching** (if power off must hold state) vs classic non-latching.  
- Select appropriate **mounting/terminal style** based on your PCB layout (SMT vs through-hole) and mechanical constraints (height, pad layout).  
- Decide whether you need any special performance version: if you expect high surge, high voltage isolation, higher current than standard.  
- Confirm contact arrangement (for IM03: DPDT) matches your switching needs.  
- Double check part number suffix to ensure you’re getting the exact variant (e.g., “GR” vs “JR” vs “TS” etc). The datasheet shows how suffix maps to voltage, terminals, package style. citeturn0search7turn0search3  

---

If you like, I can pull together **a table of all the IM03 variants** (coil voltages, mounting styles, part numbers) so you can pick the best one for your PCB design. Would you like me to do that?

[M3] ME (2025-11-20 08:06):
So what would be the safe replacement version so that in normal deenrgised state in is connected to gain cal and not charging the capacitor via od

[M4] AI (2025-11-20 08:07):
Short answer: there isn’t an IM03 “reverse-logic” version – the contact layout and which side is NC/NO is fixed for all IM03s. So you can’t get a drop-in part that magically makes the de-energised state connect to gain-cal instead of the 25 V/cap path.  

But you *can* make the behaviour you want – it just has to be done in wiring / PCB, not by choosing a different IM03 code.

---

### How the IM03 behaves (all variants)

For the non-latching IM03:

- **De-energised (normal) state**:  
  COM → **NC**  
- **Energised state**:  
  COM → **NO**

That’s true regardless of coil voltage, mounting style, etc. The suffix (GR, JR, etc.) changes things like coil voltage and package style, not which pins are NC vs NO.

So if right now, in the de-energised state, the node is connected to **25 V + C4** and *not* to the gain-cal staircase, it means:

- Your **COM** is that shared node, and  
- You’ve put **25 V/C4** on the **NC** pin, and  
- The **gain-cal** node on the **NO** pin.

Hence: relay off → node sees 25 V/C4, and when you switch, that charged 25 V on C4 gets dumped toward the gain-cal circuitry.

---

### What you actually want

> “in normal de-energised state [the node] is connected to gain cal and not charging the capacitor via 25 V/OD”

Electrically, that means:

- **De-energised (normal) state**: COM → **gain-cal**  
- **Energised state**: COM → **25 V/C4** (or CCD, depending how you’re using the second pole)

So the “safe” configuration is:

- Put **gain-cal** on **NC**  
- Put **25 V/C4** on **NO**  

Then:
- If the relay loses power or at power-up default, the node is safely tied to gain-cal and *not* to a pre-charged 25 V capacitor.
- The 25 V/C4 only connects when you actively energise the coil.

---

### What this means for you in practice

1. **If you can still change wiring / PCB:**
   - Keep using the **same IM03** type (no special variant needed).
   - Swap which pads/nets go to NC and NO so that:
     - NC = gain-cal
     - NO = 25 V/C4
   - Do the same logic for the second pole if it’s also involved in that 25 V charging path.

2. **If the PCB is already built and you can’t change the layout:**
   - There is **no IM03 variant** that simply flips NC/NO on the existing footprint.
   - Options then are:
     - **Track cuts + jumpers** to effectively swap gain-cal and 25 V between NC/NO.
     - Or add a **small daughter relay / MOSFET** just to control the 25 V charge into C4 so it can’t ever be connected to the gain-cal node when the relay switches.

3. **Safety / transient aspect:**
   - Even with the “safe” default, if C4 is ever charged to 25 V and then switched onto the gain-cal node, you’ll still get a transient dump.
   - Ideally:
     - Only *charge* C4 when that side is isolated from gain-cal, and/or
     - Add series resistance / clamping between the relay and the sensitive op-amp inputs so a charged cap can’t slam them directly.

---

If you want, you can paste the exact pin labels you used for the IM03 on your schematic (which nets are on COM/NC/NO for each pole), and I can spell out *exactly* how to reassign them so de-energised = gain-cal, energised = 25 V, with minimal surgery.
