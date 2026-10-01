# Cable Distance with LVDS
Date (UTC): 2026-02-09 18:57
Conversation ID: 698a2df4-4754-8393-82ef-f80c00d1852d
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-005.json

[M1] ME (2026-02-09 18:57):
[image]
How far could this sensibly drive a line with good quality cable 
[attached file: 39572194-7DD3-453F-90F5-B634080EC18E.jpeg]

[M2] AI (2026-02-09 18:57):
You’re looking at the **Texas Instruments DS90LV047A** — a quad LVDS line driver. Solid, old-school, robust part. Let’s talk realistically about distance rather than datasheet optimism.

---

## 1️⃣ What the device is designed for

The **DS90LV047A** is a **4-channel LVDS transmitter**:

- ~350 mV differential swing  
- ~1.2 V common mode  
- Intended for **100 Ω differential termination**
- Typical data rates: up to ~200–400 Mbps (depending on variant and layout quality)

It’s not a long-haul cable driver — it’s a board-to-board / short-to-medium cable interconnect device.

---

## 2️⃣ Sensible distance expectations

With **good quality 100 Ω differential cable** (e.g. Cat5e twisted pair or shielded twisted pair), here’s what is realistic:

### 🔹 At lower speeds (≤ 50–100 Mbps)
You can typically achieve:

**10–20 metres** reliably  
Possibly up to **30 m** if:
- Proper 100 Ω termination at receiver  
- Clean routing  
- Controlled impedance cable  
- Good ground reference  
- No heavy EMI environment  

Beyond that, margin starts collapsing unless you slow edges or reduce data rate.

---

### 🔹 At 200+ Mbps
Realistically:

**3–10 metres**

After ~10 m:
- Eye closure increases
- Jitter margin collapses
- Common-mode noise becomes dominant
- Reflections become visible if termination isn’t perfect

---

### 🔹 On PCB only (no cable)
You can route **tens of cm** with excellent signal integrity at full rate.

---

## 3️⃣ What actually limits the distance

It’s not voltage swing — it’s:

- Cable attenuation at high frequency  
- Rise time degradation  
- Reflections from impedance mismatch  
- Skew between pairs  
- Common-mode noise pickup  

LVDS doesn’t have pre-emphasis or adaptive equalisation. So once the high-frequency components die, the eye dies.

---

## 4️⃣ Practical Engineering Rule of Thumb

If this is for your Pixel-Burn or sensor rig context:

- For lab setups: **<10 m at 200 Mbps = safe**
- For industrial environments: stay **<5 m** unless tested
- For slow control signals (clock <20 MHz): **20–30 m is realistic**

If you need:

- 50+ metres  
- 100+ metres  
- No performance degradation  

You move to:
- LVDS with line drivers designed for long haul  
- RS-485  
- CML + equalisation  
- Or SerDes with pre-emphasis

---

## 5️⃣ The real question

The answer changes dramatically depending on:

- What data rate?
- Continuous clock or burst?
- Cable type?
- Is this point-to-point or multi-drop?
- Industrial EMI environment?

If you tell me:
- Bit rate  
- Cable type  
- Environment  
- Required BER  

I’ll give you a proper engineering limit rather than a generic range.

You’re asking the right question before committing layout — that’s exactly where signal integrity problems get expensive.
