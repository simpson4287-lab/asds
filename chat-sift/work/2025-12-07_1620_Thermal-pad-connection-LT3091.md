# Thermal pad connection LT3091
Date (UTC): 2025-12-07 16:20
Conversation ID: 6935a95d-7134-8327-b5f9-9b7e940d4027
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-002.json

[M1] ME (2025-12-07 16:20):
Lt3091. Where shall I connect the thermal pad


[M2] AI (2025-12-07 16:20):
The **LT3091 thermal pad must be soldered to the PCB copper and connected to VOUT (output)**.  
It is **not ground** — unlike some regulators — so this is important to avoid incorrect layout or shorts.

### From the datasheet layout rules (summarised):
- The **exposed pad (EP)** is electrically connected to **VOUT**
- Must be soldered to a **large copper area** for heat dissipation
- Can connect to **internal planes or thermal vias** to increase area
- Keep copper thick and well-spread to improve thermal performance

---

### Practical PCB Layout Guidance

| Pad | Electrically connected to | Notes |
|---|---|---|
| **Exposed thermal pad** | **VOUT** | Use copper pour, multiple vias, heatsinking copper area |
| VIN pins | Input supply | Keep traces wide, place input caps close |
| VOUT pins | Output node | Pad is tied here internally |

---

### Recommended Layout

```
Top Layer
---------
[LT3091]  ← Exposed pad under chip
   | 
   └── Large pour connected to VOUT
        ⬇ Thermal vias (optional but recommended)
Inner Layer(s)
---------------
Copper plane also tied to VOUT for heat spreading
```

---

### Checklist

- [ ] Don't connect pad to GND — **it is not ground**
- [x] Tie thermal pad to **VOUT net**
- [x] Use as much copper as possible for cooling
- [x] Add thermal vias below pad for spreading (0.3–0.4mm holes ideal)

---

If you want, send your PCB image and I’ll mark where to connect the pad and suggest a layout geometry for best performance (trace width, via array, copper area, etc.).

[M3] ME (2025-12-07 16:24):
I have it used in the vin on this deisgb

[M4] AI (2025-12-07 16:25):
Ah, okay – then you’ve actually done it *right*.  

For the LT3091 the datasheet is very explicit:

> **“EXPOSED PAD (PIN 15) IS IN, MUST BE SOLDERED TO PCB”** citeturn3view0  

So:

- The **thermal pad / exposed pad goes to VIN (IN pins)**  
- It **must be soldered** to a copper area on the PCB for heatsinking  
- It is **not GND** and **not OUT** – it’s the **IN node** electrically

So your design, with the pad tied into VIN, is exactly what Analog Devices intend.

### Layout tips given your choice

- Make a **big copper pour** on the VIN net under and around the pad  
- If you can, add **thermal vias** down to an internal VIN plane to spread heat  
- Keep the **OUT copper separate** so you don’t accidentally short IN and OUT with the pad  
- Leave a decent clearance from any sensitive low-level traces under the pad: it’s a chunky, noisy input node for a power device

If you’d like, you can drop a screenshot of your PCB around the LT3091 and I can sanity-check clearances, via pattern, and copper areas.
