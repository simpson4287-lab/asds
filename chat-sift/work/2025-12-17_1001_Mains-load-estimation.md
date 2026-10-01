# Mains load estimation
Date (UTC): 2025-12-17 10:01
Conversation ID: 69427f11-b604-8330-9e24-315f62b9878b
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-002.json

[M1] ME (2025-12-17 10:01):
If my key sight main frame draws 10A from a pair of plus and minus 7.5v and I have two of them resulting in 20A Dc. Do you know what the mains load would be from a 230v supply powering both mainframes 

[M2] AI (2025-12-17 10:01):
We can estimate it fairly cleanly, but the key is that **the exact mains load depends on efficiency and power factor**. I’ll walk it step-by-step and give you a realistic range.

---

## 1. DC power drawn by the mainframes

Each mainframe:
- +7.5 V at 10 A  
- −7.5 V at 10 A  

That’s effectively **15 V rail-to-rail at 10 A**.

**Power per mainframe:**
\[
P = V \times I = 15\,\text{V} \times 10\,\text{A} = 150\,\text{W}
\]

Two mainframes:
\[
150\,\text{W} \times 2 = \boxed{300\,\text{W DC}}
\]

---

## 2. Allow for PSU efficiency

Keysight mainframes typically use high-quality switch-mode PSUs. Realistic efficiency figures:

- **Conservative:** 80%
- **Typical:** 85–90%

Let’s calculate both ends.

### At 80% efficiency
\[
P_{AC} = \frac{300}{0.80} = 375\,\text{W}
\]

### At 90% efficiency
\[
P_{AC} = \frac{300}{0.90} = 333\,\text{W}
\]

So expect:
\[
\boxed{330–380\,\text{W from the mains}}
\]

---

## 3. Mains current at 230 V

Ignoring power factor for the moment:

### Best case (333 W)
\[
I = \frac{333}{230} = 1.45\,\text{A}
\]

### Worst case (375 W)
\[
I = \frac{375}{230} = 1.63\,\text{A}
\]

---

## 4. Power factor (important but not dramatic)

Keysight gear normally has **active PFC**, so power factor is usually **0.95–0.99**.

Including PF:

\[
I_{real} = \frac{P}{V \times PF}
\]

Worst-case realistic draw:
\[
\frac{375}{230 \times 0.95} \approx 1.72\,\text{A}
\]

---

## ✅ Final realistic answer

For **two Keysight mainframes**, each drawing ±7.5 V at 10 A:

- **Mains power:** ~**330–380 W**
- **Mains current @ 230 V:** ~**1.5–1.7 A**
- **Well within** a standard UK 13 A socket
- Thermal and wiring load are modest

---

If you want, I can:
- sanity-check against **Keysight datasheet max VA ratings**
- estimate **startup inrush current**
- or help you size a **bench isolation transformer / UPS** for this setup

[M3] ME (2025-12-17 10:36):
Which keysight module is specified for 8v 6.25a

[M4] AI (2025-12-17 10:36):
The **Keysight module specified for 8 V at 6.25 A** is the **entity["turn0product0","Agilent/Keysight N6732B DC Power Module",0]** (also sold as **entity["turn0product1","Keysight Technologies Bench Power Supply, 50W, 1 Output, 0 → 8 V/6.25 A"]** in some listings). It’s a **50 W DC power module** designed for use in Keysight’s modular power systems such as the N6700 series or the N6705 DC Power Analyzer. citeturn0search1

### Key specifications
- **Output voltage:** 8 V  
- **Output current:** 6.25 A  
- **Output power:** ~50 W  
- Designed as a plug-in power module for modular mainframes (e.g., N6700, N6705). citeturn0search1

If you’re matching power ratings to a specific instrument or mainframe, this is the standard Keysight module at that 8 V/6.25 A output point. citeturn0search1

Would you like help comparing this to other Keysight DC power modules with higher current at similar voltages? (Useful if you need more than 6.25 A per rail.)

[M5] ME (2025-12-17 10:42):
20v 5a module?

[M6] AI (2025-12-17 10:43):
Yes — the **standard Keysight DC power module rated for 20 V at 5 A** in their modular system is:

### 🔌 **entity["turn0product0","Keysight N6743B DC Power Module",1]**
- **Output:** 0 → 20 V  
- **Max Current:** 5 A  
- **Max Power:** 100 W  
- Designed for use in **N6700 Series Modular Power Systems** or the **N6705 DC Power Analyzer** mainframes. citeturn0search0

This classic module gives you a programmable 20 V output with up to 5 A current — ideal if your DUT needs up to 100 W from a single slot in a modular mainframe. citeturn0search1

✅ **Notes**
- It’s a versatile, general-purpose DC supply within the Keysight modular ecosystem. citeturn0search0  
- If you need *higher current* at ~20 V you’d look at other modules (e.g., up to 15 A versions exist in the wider N67xx lineup, though then the current rating and power differ). citeturn0search7

If you want, I can list **other Keysight modules with similar voltage ranges but different current/power ratings** too (e.g., 20 V at higher current limits).
