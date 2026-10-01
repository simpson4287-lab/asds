# 2-Channel LVDS Alternatives
Date (UTC): 2026-02-17 21:35
Conversation ID: 6994def9-f040-8395-b002-436b4c8a9176
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-02-17 21:35):
Is there a 2 channel equivalent of ds90lv032

[M2] AI (2026-02-17 21:35):
Here are some common **2-channel LVDS (differential) receiver ICs** that serve as smaller-channel-count alternatives to the quad-channel entity["turn0product0","Texas Instruments DS90LV032ATM",1] (a 4-channel LVDS receiver supporting up to ~400 Mb/s and ANSI/TIA/EIA-644 compatibility) — i.e., options with two LVDS receiver channels instead of four:citeturn0search0

products{"selections":[
["turn1product10","Texas Instruments SN65LVDS1050PW Dual LVDS Receiver"],
["turn1product5","onsemi FIN1002M5X LVDS Differential Receiver"],
["turn1product19","onsemi FIN1019MTCX LVDS Differential Receiver"],
["turn1product6","Texas Instruments SN65LVDS2DBVR LVDS Receiver"],
["turn1product2","Analog Devices LVDS Receiver"],
["turn1product12","Analog Devices ADN4680EBCPZ LVDS Interface IC"],
["turn1product14","Analog Devices MAX9172EKA+T Dual LVDS Receiver"],
["turn1product20","Texas Instruments SN65LVDS2D LVDS Interface IC"]
]}

### 👍 Good 2-Channel LVDS Receiver IC Options
- **entity["turn1product10","Texas Instruments SN65LVDS1050PW",0]** – Dual LVDS receiver that integrates two LVDS input pairs and outputs compatible logic; compact footprint and typical data rates suitable for many point-to-point links.  
- **entity["turn1product5","onsemi FIN1002M5X",0]** – Simple LVDS differential receiver; low cost with two differential inputs.  
- **entity["turn1product19","onsemi FIN1019MTCX",0]** – Another 2-channel LVDS receiver option with typical ~400 Mb/s capability.  
- **entity["turn1product6","Texas Instruments SN65LVDS2DBVR",0]** – Very low-pin-count 2-channel receiver, useful for tight board space.  

### Additional Compatible LVDS Devices
These parts also provide LVDS input reception with two channels, though feature sets (e.g., integrated line receivers, logic levels, output formats) may vary:  
- **entity["turn1product2","Analog Devices LVDS Receiver",0]** – A general dual LVDS receiver IC.  
- **entity["turn1product12","Analog Devices ADN4680EBCPZ",0]** – LVDS interface receiver with robust analog front end.  
- **entity["turn1product14","Analog Devices MAX9172EKA+T",0]** – Dual high-speed LVDS receiver up to ~500 Mb/s.  
- **entity["turn1product20","Texas Instruments SN65LVDS2D",0]** – Another 2-channel LVDS interface part with flexible logic outputs.

### What to Watch When Choosing
* **Data rate and skew:** Match or exceed the ~400 Mb/s (≈200 MHz differential) capability of the original DS90LV032. citeturn0search0  
* **Common-mode range:** Ensure the device accepts your LVDS transmitter’s common-mode voltage.  
* **Fail-safe behavior:** The DS90LV032 has internal fail-safe biasing — lower-channel parts may not; you might need external bias if receivers see open or terminated conditions. citeturn0search0  
* **Package and I/O level:** Check supply voltage, output logic levels (LVTTL/CMOS), and package size against your board constraints.

If you want a direct drop-in replacement with **identical pin-out** and quad-channel, there isn’t a 2× version from TI’s DS90LV family — the DS90LV032 itself is only in 4-channel variants — so dual receivers like the SN65LVDS1050PW are the practical alternative. Let me know if you’d like cross-reference suggestions (same pin count/pin-compatible) or part comparisons at specific data-rates!

[M3] ME (2026-02-17 22:31):
Dual receiver in a ssop package 

[M4] AI (2026-02-17 22:31):
Here are **dual-channel LVDS receiver ICs in SSOP (or SSOP-like small outline) packages** that are suitable as a smaller-channel alternative to a DS90LV032:

### ✅ Dual-Channel LVDS Receivers (SSOP / Small Packages)
**1. entity["turn1product4","Texas Instruments SN65LVDS1050PW",1]** – Dual LVDS receiver (two differential inputs) with LVDS-to-LVTTL outputs in a 16-pin TSSOP package.  
- Compact SSOP-type package.  
- Typical LVDS data compatibility (~400 Mb/s).  
- Common in board-level LVDS links with point-to-point signalling.

**2. entity["turn1product12","Texas Instruments SN65LVDS049PWR",0]** – Dual LVDS differential drivers/receivers in a 16-pin SSOP/TSSOP package.  
- Useful if you need paired driver + receiver channels.  
- Complies with TIA/EIA-644-A LVDS signalling. citeturn0search10

**3. entity["turn1product1","Analog Devices LVDS Receiver",0]** – LVDS receiver in a small SSOP/SSOP-like package (exact part depends on variant identifier; check the datasheet for pin-count and package details).  
- Good general alternative with differential LVDS to logic outputs.

**4. entity["turn1product2","Texas Instruments DS90CR286AMTD/NOPB, LVDS Receiver, TSSOP-56",0]** – LVDS receiver in a TSSOP package (check pin count vs your footprint).  
- While a bit larger, it’s still a thin SSOP format.

---

### 📌 Notes / Selection Tips
- **Package pitch & footprint:** SSOP/TSSOP pins are typically 0.65 mm pitch; ensure your board can support the pitch and pad spacing.  
- **Fail-safe behaviour:** The DS90LV032 has internal fail-safe biasing; many smaller dual receivers may *not* — so if you expect open/idle lines, you might need external bias/terminations. citeturn0search26  
- **Data rate:** Verify the receiver’s maximum differential rate if you’re targeting speeds similar to or above 400 Mb/s.  
- **Driver/receiver vs receiver-only:** Some parts (like SN65LVDS049) include drivers along with receivers, which may or may not suit your use case.

---

If you’d like, I can narrow this down further based on **exact data-rate requirements (e.g., ≥ 500 Mb/s)** or **desired output logic (LVTTL/CMOS)**!

[M5] ME (2026-02-17 22:40):
[image]
Trying to find dual receiver in this package 
[attached file: 0E45ACAF-35BE-4C33-928E-87B83A5CA2B4.jpeg]

[M6] AI (2026-02-17 22:40):
You’re showing **entity["company","Renesas Electronics","semiconductor manufacturer"] ISL32433EIUZ-T7A** — that’s an **RS-485/RS-422 transceiver**, not LVDS. It’s also **single-channel**, even though it’s in MSOP-10.

If you’re specifically looking for:

> **Dual LVDS receiver**  
> **MSOP-10 or SSOP-10 class package (≈3 mm body)**

That combination is unfortunately rare. Most LVDS dual receivers jump to **TSSOP-16** because you need:

- 4 LVDS inputs  
- 2 CMOS outputs  
- Vcc  
- GND  
- (often) Enable or fail-safe bias pins  

That typically pushes you past 10 pins.

---

## Realistic Options

### 1️⃣ 16-pin TSSOP (Most Practical)

**entity["product","SN65LVDS2","texas instruments dual lvds receiver"]** (TI)  
- Dual LVDS receiver  
- 16-TSSOP  
- 400+ Mbps  
- Very close functional match to DS90LV032 (just 2 channels)

This is usually the cleanest engineering choice.

---

### 2️⃣ Tiny Package but Single Channel (Use Two)

If board area is the real constraint:

**entity["product","FIN1002","onsemi lvds receiver"]**  
- SOT-23 / small MSOP  
- Single LVDS receiver  
- Use two devices  
- Often *smaller total footprint* than one TSSOP-16

In dense CCD clock boards (like what you’re building), two SOT-23s sometimes route cleaner than a 0.65 mm 16-pin.

---

### 3️⃣ If You Truly Meant RS-485 (Like the ISL32433)

If this is actually for slower differential control lines and not LVDS video/clocking, then dual RS-485 receivers in MSOP-10 *do* exist.

But for true LVDS (350 mV swing, 100 Ω termination, 6 MHz+ clean edge):

You won’t realistically find a proper **dual LVDS receiver in 10-pin MSOP**.

---

## Quick Question

Is this for:

- LVDS clock distribution (6 MHz CCD clocks)?
- Long cable reception?
- Or low-speed differential control?

If this is for your PixelBurn clock chains, I’d strongly lean toward:

> Dual TSSOP-16 LVDS receiver  
> or two tiny single-channel receivers for layout control.

Tell me the exact signalling level and speed and I’ll narrow it precisely.

[M7] ME (2026-02-17 22:46):
 Is there a version of this, quad receiver 

[M8] ME (2026-02-17 22:46):
[image]
[attached file: 94CB329D-D599-4951-BFC5-557A515B9752.jpeg]

[M9] AI (2026-02-17 22:46):
You’re looking at **entity["product","SN65LVDS1050","texas instruments dual lvds transceiver"]** — which is:

- 2 × LVDS drivers  
- 2 × LVDS receivers  
- 16-pin TSSOP  

If you’re asking:

> Is there a quad-receiver version of this (receiver-only)?

Yes — but it won’t be in the same 16-pin footprint.

---

## Direct Quad Receiver Equivalent

### ✔️ **entity["product","DS90LV032A","texas instruments quad lvds receiver"]**

- 4 LVDS receivers
- ANSI/TIA-644 compliant
- Fail-safe biasing
- 400 Mbps class
- 16-pin SOIC or TSSOP

This is essentially the receiver-only version of what the 1050 does on its RX side.

---

## If You Need Driver + Receiver (Quad Total Channels)

Closest TI family parts would be:

- **entity["product","SN65LVDS348","texas instruments quad lvds transceiver"]**
- Or multi-channel LVDS transceiver families

But those move into 28+ pins quickly.

---

## Important Package Reality

Quad LVDS receiver cannot fit into MSOP-10.  
You need:

- 8 differential inputs  
- 4 CMOS outputs  
- Vcc  
- GND  
- Possibly enable  

That’s already > 14 pins minimum.

So realistically:

- **Dual → 16-pin**
- **Quad → 16–20+ pin**
- **MSOP-10 → Single channel only**

---

## Engineering Perspective (Given Your PixelBurn Context)

For dense clock blocks:

- Quad device = fewer ICs, cleaner biasing, matched propagation delay.
- Dual devices = better placement flexibility per clock chain.
- Singles = tightest routing but more components.

If this is for 6 MHz CCD clock reception over 14 m LVDS lines, the **DS90LV032A** is honestly the cleanest quad solution.

If you tell me:
- Required supply (3.3 V?)
- Whether you need fail-safe open detection
- Edge symmetry sensitivity

I’ll narrow to the most layout-sane part for your architecture.

[M10] ME (2026-02-17 22:49):
What’s the dual device equivalent 

[M11] AI (2026-02-17 22:49):
Yes — for a **dual LVDS receiver** that’s the “2-channel equivalent” of the **DS90LV032A (quad receiver)**, the clean match is:

## Best direct equivalent (2-channel receiver-only)
**entity["product","DS90LV028A","Texas Instruments"]**  
- **Dual** CMOS LVDS differential line receiver  
- **>400 Mbps (200 MHz)** class  
- Includes **fail-safe for open/short/terminated inputs** citeturn1search2  
- Available in **SOIC** and **WSON** packages citeturn1search2

If you’re staying in the classic TI/National “DS90LV0xx” family, this is the closest “half of a 032A”.

---

## If you only need 1 channel (for completeness)
**entity["product","DS90LV012A","Texas Instruments"]** – single LVDS receiver, also **>400 Mbps**, and it even has **integrated termination** (102 Ω typ). citeturn0search1turn0search5

---

## One nuance to check (important for your use-case)
The **DS90LV028A** gives you **two channels in one package**, but **package options won’t be MSOP-10** (pin-count reality: 2 channels needs more than 10 pins). If you tell me your *must-have footprint* (TSSOP-16 OK? SOIC-8/10? WSON?), I’ll give you the tightest package that still behaves like your DS90LV032A links.

Do you need **3.3 V CMOS outputs** like the 032A, or **1.8 V** acceptable too?

[M12] ME (2026-02-17 22:52):
What about the 32? Is that in a ssop package?

[M13] AI (2026-02-17 22:52):
Short answer: **No — the DS90LV032 (quad LVDS receiver) is *not* offered in a 10-pin SSOP/MSOP form factor.**

Here’s the detail:

### 📌 **DS90LV032A Packaging**
The true quad LVDS receiver from TI — **entity["product","DS90LV032A","quad lvds receiver"]** — is available in packages like:

- **TSSOP-16**
- **SOIC-16**
- (sometimes) **WQFN** / similar

But there is **no SSOP-10 / MSOP-10 offering for the 032A**. That’s simply not enough pins for:

- 4 differential inputs (×2 pins each = 8)
- 4 CMOS output pairs (×1 each = 4)
- Vcc / GND
- Enable / failsafe logic

So you *must* go to a ≥14-pin class package for quad.

### 📌 Why 10-pin Isn’t Possible for Quad LVDS
Let’s count minimum pins:

| Signal              | Pins |
|--------------------|------|
| 4 LVDS pairs (inputs) | 8 |
| 4 CMOS outputs       | 4 |
| Vcc & GND            | 2 |
| Control / Enable / Bias | 1+ |
| **Total**            | **≥15** |

Even with pin sharing, 10 is too few.

### 📌 What You *Can* Do
| Need | Suitable Package |
|------|------------------|
| 1 LVDS receiver | MSOP/SOT23 (single channel) |
| 2 LVDS receivers | TSSOP-16 minimum |
| 4 LVDS receivers | TSSOP-16 / SOIC-16 |

So:

- **DS90LV012A** — single LVDS receiver, available in tiny packages (closer to MSOP-8).
- **DS90LV028A** — dual LVDS receiver → requires a **TSSOP-14/16** (more pins).
- **DS90LV032A** — quad LVDS receiver → *only* in 16-pin class.

### 📌 If You’re Trying to Minimize Footprint
Your options to keep size small are:

**Option A — Packaged Quad (one chip)**  
- *DS90LV032A* in **TSSOP-16**  
- Best matched fail-safe/established.

**Option B — Two Dual Receivers**  
- Two **DS90LV028A** or two **SN65LVDS1050 receivers**  
- Physically splits ties, routing optimized where needed.

**Option C — Four Narrow Single Receivers**  
- 4 × tiny SOT23/SC70 LVDS receivers  
- Lowest individual footprint but more devices.

---

## If footprint constraint is critical
Tell me:

1. **Max body size** you can tolerate (e.g., ≤5 mm wide)?  
2. **Supply voltage** (3.3 V or 1.8 V)?  
3. **Required data rate** (e.g., ≥100 MHz diff, ≥200 MHz diff frame clocks)?

With that info I can give you a concise shortlist best for your board constraints.

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] AI (2026-02-17 22:40):
You’re looking at **MSOP-10 (3 × 3 mm class)** in that Renesas part — so the constraint is:

- **Dual LVDS receiver**
- **MSOP-10 (or very close equivalent)**
- Similar behaviour to **DS90LV032** (LVDS → CMOS/LVTTL)

Here’s the important reality:

👉 **Most dual LVDS receivers are 8-pin packages.**  
MSOP-10 is uncommon for receiver-only dual parts because you only need:
- 2 × differential inputs (4 pins)
- 2 × outputs (2 pins)
- VCC, GND (2 pins)
- Optional enable/failsafe (1–2 pins)

That typically fits in **MSOP-8**.

---

## 🔎 Clean, Practical Options

### 1️⃣ **Texas Instruments SN65LVDS2**
- Dual LVDS receiver
- Available in **VSSOP-8** (very similar footprint class)
- ~400 Mbps capability
- CMOS outputs

If your board can tolerate 8-pin instead of 10-pin, this is the cleanest solution.

---

### 2️⃣ **ON Semiconductor FIN1002**
- Dual LVDS receiver
- **MSOP-8**
- Up to ~400 Mbps
- Very compact

---

### 3️⃣ **TI SN65LVDS1050**
- Dual LVDS receiver
- **TSSOP-16**
- Larger, but closer to DS90LV032 electrical behaviour

---

## ⚠️ Important Clarification

The part in your screenshot:

> **ISL32433EIUZ-T7A**

is **RS-485/RS-422**, not LVDS.

It:
- Has ±7V common-mode range
- 5V differential swing
- Is NOT LVDS-level compatible

So if this is for your PixelBurn clock distribution or 14 m LVDS runs, this part is not the correct signalling class.

---

## 💡 If You Absolutely Need MSOP-10

Then you're likely forced into:
- Dual **transceiver** (driver + receiver)
- Or a multiprotocol part

Pure receiver-only dual LVDS in MSOP-10 is rare.

---

## Quick Engineering Question

For your application:
- Data rate?
- 3.3 V supply?
- Need fail-safe biasing internal?
- CMOS output required or current-mode?

Given your CCD clock architecture and tight layout constraints, I suspect **MSOP-8 dual receiver is electrically optimal**, unless you're trying to footprint-match something.

If you confirm speed + supply, I’ll narrow this to the most robust option for your architecture.
