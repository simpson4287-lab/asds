# HDMI to USB-C Pinout
Date (UTC): 2026-02-20 01:43
Conversation ID: 6997bc48-88a8-838b-8d44-8ab5c6a70b43
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-02-20 01:43):
What is the conventional
Pin out from
HDMI to usbc for cables 

[M2] AI (2026-02-20 01:43):
Short answer: **there is no conventional passive pin-to-pin HDMI → USB-C wiring.**  
HDMI and USB-C use fundamentally different physical layers and protocols. Most HDMI↔USB-C cables you see are **active adapters** with conversion silicon inside.

That said, in engineering terms there *is* a conventional **signal mapping architecture** when using **USB-C DisplayPort Alt Mode → HDMI conversion**, which is what almost all legit cables/adapters implement.

Let’s break it down cleanly.

---

# 1) Why there is no simple passive pinout
- **HDMI** carries TMDS video signaling
- **USB-C** natively carries USB, not TMDS
- Video over USB-C is typically **DisplayPort Alt Mode**
- Therefore:  
  ✅ USB-C (DP Alt Mode) → active chip → HDMI TMDS  
  ❌ Not a straight wire conversion

If you ever see a thin HDMI→USB-C cable with no electronics bulge, be suspicious — true HDMI requires conversion.

---

# 2) The de-facto architecture used in real cables

Typical signal path:

```
USB-C (DisplayPort Alt Mode)
        ↓
DP-to-HDMI converter IC
        ↓
HDMI TMDS output
```

Common converter ICs:
- Parade PS176
- MegaChips MCDP29xx
- Lontium LT6711
- Analogix ANX7730

---

# 3) Conventional USB-C → HDMI signal mapping (engineering view)

When USB-C enters **DisplayPort Alt Mode (4-lane)**:

### USB-C high-speed lanes
| USB-C pins | Function in DP Alt Mode |
|-----------|-------------------------|
| TX1± | DP Lane 0 |
| RX1± | DP Lane 1 |
| TX2± | DP Lane 2 |
| RX2± | DP Lane 3 |

These four DP lanes feed the converter IC.

---

### HDMI side (TMDS)
Converter outputs:

| HDMI pin | Signal |
|---------|--------|
| 1 | TMDS Data2+ |
| 2 | TMDS Data2 Shield |
| 3 | TMDS Data2− |
| 4 | TMDS Data1+ |
| 5 | TMDS Data1 Shield |
| 6 | TMDS Data1− |
| 7 | TMDS Data0+ |
| 8 | TMDS Data0 Shield |
| 9 | TMDS Data0− |
| 10 | TMDS Clock+ |
| 11 | TMDS Clock Shield |
| 12 | TMDS Clock− |

---

# 4) Important sideband / control wiring

A proper cable/adapter must also handle:

### USB-C configuration channel
| USB-C pin | Purpose |
|----------|---------|
| CC1 / CC2 | Alt-mode negotiation |
| SBU1/2 | AUX channel (DP) |

These are **mandatory** for DP Alt Mode to enter.

---

### HDMI support signals
| HDMI pin | Function |
|---------|----------|
| 13 | CEC (optional) |
| 15 | DDC SCL |
| 16 | DDC SDA |
| 18 | +5V |
| 19 | HPD |

The converter IC bridges:

```
DP AUX ↔ HDMI DDC/HPD
```

---

# 5) Cable direction matters (VERY important)

There are three fundamentally different products:

### ✅ USB-C → HDMI (most common)
- Source: USB-C laptop/phone
- Sink: HDMI monitor
- Uses DP Alt Mode + converter

### ⚠️ HDMI → USB-C (rare and different)
- Source: HDMI device
- Sink: USB-C display
- Requires completely different silicon
- Much less common

### ❌ Passive cable (almost never valid)
Only works in very niche proprietary cases.

---

# 6) If you are designing PixelBurn hardware

What you normally implement is:

**USB-C source → HDMI output**

Recommended architecture:

```
USB-C receptacle
   ↓
Type-C controller (PD/Alt Mode)
   ↓
DP lanes
   ↓
DP-to-HDMI bridge IC
   ↓
HDMI connector
```

---

# 7) Quick reference pin grouping

## USB-C (video-relevant pins)

**High speed**
- TX1±
- RX1±
- TX2±
- RX2±

**Control**
- CC1 / CC2
- SBU1 / SBU2
- VBUS
- GND

---

## HDMI (video-relevant pins)

**TMDS**
- Data0/1/2 ±
- Clock ±

**Control**
- DDC SDA/SCL
- HPD
- +5V

---

# Bottom line

- There is **no universal passive HDMI↔USB-C pinout**
- Real cables use:
  - USB-C DisplayPort Alt Mode  
  - Active DP→HDMI bridge
- Any proper design must include:
  - CC negotiation
  - AUX/DDC bridging
  - TMDS generation

---

✅ **If helpful**, I can next draw a proper engineering block diagram for a USB-C → HDMI implementation (PixelBurn-grade), including recommended ICs and lane routing rules.

[M3] ME (2026-02-20 01:44):
Just draw the pin to pin typical 

[M4] AI (2026-02-20 01:44):
Yep — I’ll draw the **“typical pin-to-pin”** mapping you see in a *real* USB-C ↔ HDMI cable. Just keep in mind: **this is not a passive wire map**; it’s the **standard interconnect around a DP→HDMI bridge IC** inside the cable/adapter.

Below is the conventional mapping in **USB-C DisplayPort Alt Mode (4-lane)** to **HDMI (Type-A)**.

---

## 1) USB-C (DP Alt Mode) → Bridge IC → HDMI

### USB-C receptacle pins (the ones that matter)

**DisplayPort Main Link lanes (4 lanes):**
- **A2/A3 = TX1+ / TX1−**  → DP Lane0 ±  → Bridge DP Lane0 ±
- **B11/B10 = RX1+ / RX1−** → DP Lane1 ± → Bridge DP Lane1 ±
- **B2/B3 = TX2+ / TX2−**  → DP Lane2 ±  → Bridge DP Lane2 ±
- **A11/A10 = RX2+ / RX2−** → DP Lane3 ± → Bridge DP Lane3 ±

**DP AUX channel (over SBU):**
- **A8 = SBU1** → DP AUX+ (or AUX_P) → Bridge AUX+
- **B8 = SBU2** → DP AUX− (or AUX_N) → Bridge AUX−

**Alt-mode / orientation detection:**
- **A5 = CC1** → Type-C/PD/Alt-mode logic (often in bridge / controller)
- **B5 = CC2** → Type-C/PD/Alt-mode logic

**Power / ground:**
- **A4/A9/B4/B9 = VBUS** (5 V from source; can power bridge)
- **A1/A12/B1/B12 (+ shield) = GND**

> Note: In a plug, the device uses CC1/CC2 to figure out flip orientation and then internally maps the correct lane set to the bridge.

---

## 2) Bridge IC → HDMI Type-A pin map (typical)

Here’s the **standard HDMI pinout** (Type-A) and what the bridge drives.

### HDMI TMDS pairs (video)
- **Pin 1  (TMDS2+)**  ← Bridge TMDS Data2+
- **Pin 3  (TMDS2−)**  ← Bridge TMDS Data2−
- **Pin 4  (TMDS1+)**  ← Bridge TMDS Data1+
- **Pin 6  (TMDS1−)**  ← Bridge TMDS Data1−
- **Pin 7  (TMDS0+)**  ← Bridge TMDS Data0+
- **Pin 9  (TMDS0−)**  ← Bridge TMDS Data0−
- **Pin 10 (TMDS CLK+)** ← Bridge TMDS Clock+
- **Pin 12 (TMDS CLK−)** ← Bridge TMDS Clock−

Shields/returns (usually tied to ground plane/shielding in cable):
- **Pin 2,5,8,11** = TMDS shields
- **Pin 17** = DDC/CEC ground
- **Pin 18** = +5V (from source, typically provided by bridge side or passed through)
- **Pin 19** = HPD (sink → source; handled by bridge)

### HDMI DDC / control (derived via DP AUX in the bridge)
- **Pin 15 (DDC SCL)** ← Bridge “I2C_SCL” (converted from DP AUX transactions)
- **Pin 16 (DDC SDA)** ← Bridge “I2C_SDA”
- **Pin 19 (HPD)**     ← Bridge HPD_OUT (asserted when sink is present/EDID OK)

Optional:
- **Pin 13 (CEC)** is often **NC** in simple adapters (unless the bridge supports it).

---

## 3) One clean “pin-to-pin” diagram

```text
USB-C (DP Alt Mode)                         HDMI Type-A
====================                       ============

A2  TX1+  ── DP Lane0+ ┐
A3  TX1−  ── DP Lane0− ├─>  [ DP → HDMI BRIDGE ] ──>  1  TMDS2+
B11 RX1+  ── DP Lane1+ ┤                               3  TMDS2−
B10 RX1−  ── DP Lane1− ┤                               4  TMDS1+
B2  TX2+  ── DP Lane2+ ┤                               6  TMDS1−
B3  TX2−  ── DP Lane2− ┤                               7  TMDS0+
A11 RX2+  ── DP Lane3+ ┤                               9  TMDS0−
A10 RX2−  ── DP Lane3− ┘                               10 TMDSCLK+
                                                      12 TMDSCLK−

A8  SBU1  ── DP AUX+  ───────────────┐                 15 DDC SCL
B8  SBU2  ── DP AUX−  ───────────────┴─(AUX↔DDC/HPD)→  16 DDC SDA
                                                     → 19 HPD

A5  CC1   ── Alt-mode/orientation detect (with CC2)
B5  CC2   ── Alt-mode/orientation detect (with CC1)

VBUS (A4/A9/B4/B9) ── 5V power ────────────────→ 18 +5V (and/or powers bridge)
GND  (A1/A12/B1/B12 + shield) ────────────────→ 2/5/8/11/17 grounds/shields
```

---

### The one thing you *can’t* do “pin-to-pin”
There is **no fixed, universal mapping** like “USB-C A2 always goes to HDMI pin 1” because:
- USB-C lanes can **swap with plug flip**
- DP lane ordering can be internally remapped
- The bridge decides which TMDS lane is Data0/1/2/Clock

So the *true* “pin-to-pin” is: **USB-C DP lanes → bridge DP inputs; bridge TMDS outputs → HDMI pins** (as above).

---

If you tell me **which direction** you mean (USB-C source → HDMI display *or* HDMI source → USB-C display), I’ll draw the corresponding map — the reverse direction is a different architecture.

[M5] ME (2026-02-20 01:45):
Side by side map 

[M6] AI (2026-02-20 01:45):
Below is the **clean side-by-side “typical” engineering map** for a  
**USB-C (DisplayPort Alt Mode source) → HDMI Type-A (sink)** cable/adapter.

⚠️ Reminder (important):  
- This is **logical signal mapping via a DP→HDMI bridge IC**, not passive wiring.  
- USB-C lane polarity/orientation is handled internally by the bridge/Type-C logic.

---

# USB-C → HDMI Side-by-Side Map (Typical)

## High-Speed Video Path

| USB-C Pin(s) | USB-C Signal (DP Alt Mode) | Bridge Function | HDMI Pin | HDMI Signal |
|---|---|---|---|---|
| A2 / A3 | TX1± → DP Lane 0 | DP RX Lane 0 | 1 / 3 | TMDS Data2 ± |
| B11 / B10 | RX1± → DP Lane 1 | DP RX Lane 1 | 4 / 6 | TMDS Data1 ± |
| B2 / B3 | TX2± → DP Lane 2 | DP RX Lane 2 | 7 / 9 | TMDS Data0 ± |
| A11 / A10 | RX2± → DP Lane 3 | DP RX Lane 3 | 10 / 12 | TMDS Clock ± |

✅ This is the **most common lane mapping** used by bridge ICs  
(though internally the bridge may reorder).

---

## AUX / DDC / Hot-Plug Path

| USB-C Pin | Function | Bridge Role | HDMI Pin | Function |
|---|---|---|---|---|
| A8 | SBU1 → DP AUX+ | AUX ↔ DDC bridge | 15 | DDC SCL |
| B8 | SBU2 → DP AUX− | AUX ↔ DDC bridge | 16 | DDC SDA |
| — | (internal) | HPD generation | 19 | Hot Plug Detect |

✅ The bridge converts **DP AUX transactions → HDMI I²C (DDC)**.

---

## Configuration / Alt-Mode Detection

| USB-C Pin | Purpose | Notes |
|---|---|---|
| A5 | CC1 | Cable orientation + Alt-mode negotiation |
| B5 | CC2 | Cable orientation + Alt-mode negotiation |

These go to:

- Type-C controller inside adapter **or**
- Integrated logic in modern bridge ICs

---

## Power & Ground

| USB-C Pin(s) | Signal | HDMI Pin | Signal |
|---|---|---|---|
| A4, A9, B4, B9 | VBUS (5 V) | 18 | +5 V |
| A1, A12, B1, B12 | GND | 2,5,8,11,17 | Ground / shields |

Notes:

- VBUS usually **powers the bridge IC**
- HDMI +5 V may be:
  - sourced from USB-C side, or  
  - locally regulated in adapter

---

# Visual Block (mental model)

```text
USB-C (DP Alt Mode)
   TX/RX lanes
   SBU (AUX)
   CC pins
   VBUS/GND
        │
        ▼
   [ DP → HDMI Bridge ]
        │
        ▼
HDMI Type-A
   TMDS pairs
   DDC (I²C)
   HPD
   +5V/GND
```

---

# Engineering Notes (PixelBurn-level detail)

**Lane ordering:**  
- Not guaranteed fixed inside silicon  
- Always follow the bridge datasheet routing table

**Impedance targets:**

- DP lanes: ~85 Ω diff  
- HDMI TMDS: 100 Ω diff  
- AUX: 50 Ω single-ended (typical)

**Length matching:**

- TMDS pairs tightly matched  
- DP lanes per datasheet skew budget  
- AUX not length-critical

---

If you want the **reverse direction (HDMI source → USB-C display)** side-by-side, say the word — it’s a different and more specialised mapping.

[M7] ME (2026-02-20 01:47):
Show clearing the pin for pin and differential polarity 

[M8] AI (2026-02-20 01:47):
Understood — below is the **explicit pin-for-pin differential mapping** used in a typical **USB-C (DP Alt Mode source) → HDMI Type-A (sink)** adapter.

This shows:

- exact USB-C pins  
- differential polarity  
- bridge function  
- HDMI pins  
- polarity preservation  

⚠️ This is the **standard logical mapping via a DP→HDMI bridge IC**, not a passive cable.

---

# 🔷 High-Speed Differential Pairs (Fully Expanded)

## DP Lane 0 → HDMI TMDS Data2

| USB-C Pin | USB-C Signal | Polarity | Bridge Input | HDMI Pin | HDMI Signal | Polarity |
|---|---|---|---|---|---|---|
| **A2** | TX1+ | + | DP Lane0+ | **1** | TMDS Data2+ | + |
| **A3** | TX1− | − | DP Lane0− | **3** | TMDS Data2− | − |

✅ Polarity preserved  
✅ 85 Ω diff → bridge → 100 Ω TMDS

---

## DP Lane 1 → HDMI TMDS Data1

| USB-C Pin | USB-C Signal | Polarity | Bridge Input | HDMI Pin | HDMI Signal | Polarity |
|---|---|---|---|---|---|---|
| **B11** | RX1+ | + | DP Lane1+ | **4** | TMDS Data1+ | + |
| **B10** | RX1− | − | DP Lane1− | **6** | TMDS Data1− | − |

---

## DP Lane 2 → HDMI TMDS Data0

| USB-C Pin | USB-C Signal | Polarity | Bridge Input | HDMI Pin | HDMI Signal | Polarity |
|---|---|---|---|---|---|---|
| **B2** | TX2+ | + | DP Lane2+ | **7** | TMDS Data0+ | + |
| **B3** | TX2− | − | DP Lane2− | **9** | TMDS Data0− | − |

---

## DP Lane 3 → HDMI TMDS Clock

| USB-C Pin | USB-C Signal | Polarity | Bridge Input | HDMI Pin | HDMI Signal | Polarity |
|---|---|---|---|---|---|---|
| **A11** | RX2+ | + | DP Lane3+ | **10** | TMDS Clock+ | + |
| **A10** | RX2− | − | DP Lane3− | **12** | TMDS Clock− | − |

---

# 🔷 AUX / Control Channel (Critical)

## DP AUX → HDMI DDC

| USB-C Pin | Signal | Polarity | Bridge | HDMI Pin | Function |
|---|---|---|---|---|---|
| **A8** | SBU1 → AUX+ | + | AUX ↔ I²C | **15** | DDC SCL |
| **B8** | SBU2 → AUX− | − | AUX ↔ I²C | **16** | DDC SDA |

⚠️ Note:  
- AUX is differential but **DDC is single-ended I²C**  
- Bridge performs protocol conversion

---

## Hot Plug Detect

| Source | Bridge | HDMI |
|---|---|---|
| (internal) | HPD out | **Pin 19** |

---

# 🔷 Configuration Channel (orientation & Alt Mode)

| USB-C Pin | Function | Notes |
|---|---|---|
| **A5 (CC1)** | Cable detect / Alt Mode | to Type-C logic |
| **B5 (CC2)** | Cable detect / Alt Mode | to Type-C logic |

These determine:

- plug flip  
- DP Alt Mode entry  
- lane mapping inside bridge  

---

# 🔷 Power & Ground

## Power

| USB-C Pins | Signal | HDMI Pin | Signal |
|---|---|---|---|
| **A4, A9, B4, B9** | VBUS (5 V) | **18** | +5 V |

---

## Grounds / Shields

| USB-C Pins | HDMI Pins | Purpose |
|---|---|---|
| A1, A12, B1, B12 | 2,5,8,11,17 | return / shield |

---

# 🔷 Differential Impedance Targets (for your layout brain 🧠)

| Interface | Target Zdiff |
|---|---|
| USB-C DP lanes | **85 Ω diff** |
| HDMI TMDS | **100 Ω diff** |
| AUX | ~90 Ω diff (typical) |

---

# 🔷 Important PixelBurn-Level Caveats

### 1. Lane swapping
Real bridges often allow:

- lane remap  
- polarity inversion  
- orientation swap  

👉 Always check the specific bridge datasheet.

---

### 2. You cannot passive-wire this
Because you must have:

- DP protocol  
- TMDS encoding  
- AUX ↔ DDC translation  
- HPD handling  
- CC negotiation  

---

### 3. Clock lane assignment
Common but not guaranteed:

```
DP Lane3 → HDMI Clock
```

(Some bridges allow remap.)

---

If you want, I can next produce a **routing-ready PCB constraint checklist** (length match, skew, via limits, etc.) tailored for a tight mezzanine or PixelBurn backplane.

[M9] ME (2026-02-20 01:48):
Ok, now all in one super table 

[M10] AI (2026-02-20 01:48):
Here is the **single consolidated “super table”** for a typical  
**USB-C (DisplayPort Alt Mode source) → HDMI Type-A (sink)** implementation.

This shows true engineering relationships:

- exact USB-C pins  
- differential polarity  
- bridge domain  
- HDMI pins  
- signal purpose  
- impedance targets  

⚠️ Assumes 4-lane DP Alt Mode and a standard DP→HDMI bridge.

---

# 🔷 USB-C → HDMI SUPER PIN MAP

| Domain | USB-C Pin | USB-C Signal | Polarity | Bridge Function | HDMI Pin | HDMI Signal | Polarity | Zdiff Target | Notes |
|---|---|---|---|---|---|---|---|---|---|
| HS Video | **A2** | TX1+ (DP Lane0+) | + | DP RX Lane0+ | **1** | TMDS Data2+ | + | 85→100 Ω | Main video |
| HS Video | **A3** | TX1− (DP Lane0−) | − | DP RX Lane0− | **3** | TMDS Data2− | − | 85→100 Ω |  |
| HS Video | **B11** | RX1+ (DP Lane1+) | + | DP RX Lane1+ | **4** | TMDS Data1+ | + | 85→100 Ω |  |
| HS Video | **B10** | RX1− (DP Lane1−) | − | DP RX Lane1− | **6** | TMDS Data1− | − | 85→100 Ω |  |
| HS Video | **B2** | TX2+ (DP Lane2+) | + | DP RX Lane2+ | **7** | TMDS Data0+ | + | 85→100 Ω |  |
| HS Video | **B3** | TX2− (DP Lane2−) | − | DP RX Lane2− | **9** | TMDS Data0− | − | 85→100 Ω |  |
| HS Video | **A11** | RX2+ (DP Lane3+) | + | DP RX Lane3+ | **10** | TMDS Clock+ | + | 85→100 Ω | Usually clock |
| HS Video | **A10** | RX2− (DP Lane3−) | − | DP RX Lane3− | **12** | TMDS Clock− | − | 85→100 Ω |  |
| AUX | **A8** | SBU1 (AUX+) | + | AUX ↔ DDC bridge | **15** | DDC SCL | — | ~90 Ω diff | Protocol converted |
| AUX | **B8** | SBU2 (AUX−) | − | AUX ↔ DDC bridge | **16** | DDC SDA | — | ~90 Ω diff |  |
| Detect | **A5** | CC1 | — | Type-C/Alt-mode logic | — | — | — | — | Orientation detect |
| Detect | **B5** | CC2 | — | Type-C/Alt-mode logic | — | — | — | — |  |
| Power | **A4, A9, B4, B9** | VBUS (5 V) | — | Bridge power / pass-through | **18** | +5 V | — | — | May be locally regulated |
| Ground | **A1, A12, B1, B12** | GND | — | Common return | **2,5,8,11,17** | TMDS/logic GND | — | — | Stitch to shield |
| Status | — | — | — | HPD generation | **19** | Hot Plug Detect | — | — | From bridge |
| Optional | — | — | — | (optional) | **13** | CEC | — | — | Often NC |

---

# 🔷 Critical Interpretation Notes (worth your time)

## ✅ Lane naming reality
In USB-C DP Alt Mode:

- TX/RX naming is from the USB perspective  
- In DP mode they become **Main Link lanes**  
- Your bridge treats them simply as **DP Lane[0:3]**

---

## ✅ Polarity rules

**Allowed:**
- P/N swap inside many bridge ICs  
- Lane remap inside bridge  

**Not recommended unless supported:**
- passive polarity inversion  
- cross-pair swapping on PCB

---

## ✅ Impedance domains (important for PixelBurn-level SI)

| Segment | Requirement |
|---|---|
| USB-C → bridge | 85 Ω diff |
| Bridge → HDMI | 100 Ω diff |
| AUX pair | ~90 Ω diff |
| Stubs | keep extremely short |

---

## ✅ Orientation handling (often overlooked)

Because USB-C is flippable:

- CC1/CC2 determine orientation  
- Bridge or Type-C controller internally swaps lanes  
- **Do NOT try to hard-wire both orientations externally**

---

## ✅ What is NOT directly wired

These are protocol-translated inside the bridge:

- DP AUX ↔ HDMI DDC  
- HPD generation  
- TMDS encoding  
- Scrambling/clocking  

---

---

If helpful next, I can produce a **layout constraint checklist for a tight FPGA/PixelBurn board** (max skew, via count, return stitching, etc.).

[M11] ME (2026-02-20 02:32):
That’s the circuit. Risks not shown but plus and minus 5v. Driven from the left by a SE

[M12] AI (2026-02-20 02:32):
Got you. If what you’ve got “on the page” is essentially a **pin-mapped differential path** (with **+5 V and −5 V rails present somewhere**) and it’s **being driven single-ended from the left**, then there are some big, non-obvious risks.

I’ll call out the main ones as if I’m reviewing it for a design sign-off.

## 1) A single-ended driver cannot “become” HDMI/DP differential by wiring
HDMI TMDS and DP Main Link are **true high-speed differential serial links** with:

- defined **common-mode voltage windows**
- defined **termination schemes**
- strict **AC coupling / biasing expectations** (especially DP)
- receiver **CDR/equalisation** behaviours that assume a compliant transmitter

If you drive one leg (or drive both legs with an inverted copy created “simply”), you usually end up with:
- wrong common-mode
- wrong swing
- massive deterministic jitter / eye collapse
- reflections (because the output impedance/termination isn’t right)
- a link that might “sort of” do something at low rate and then fails randomly

**Bottom line:** you need a proper **TMDS transmitter** (for HDMI) or proper **DP transmitter** (for DP), not SE logic.

## 2) The ±5 V presence is a red flag around HDMI/USB-C pins
On the connectors:

- **USB-C VBUS is +5 V (or negotiated higher), never −5 V**
- **HDMI has a +5 V pin (pin 18) but the *signals* are not ±5 V tolerant**
- DP/HDMI high-speed pins are typically **ESD-protected for small excursions**, not negative rails

So the main risk isn’t “it won’t work” — it’s **you can hard-damage a port** if −5 V can couple or fault into:
- USB-C high-speed pins
- CC pins (super sensitive)
- SBU pins
- HDMI DDC/HPD pins
- TMDS pins (through ESD structures)

**If −5 V exists anywhere near the connector**, you want:
- clear net naming + segregation
- hard protection (fuse/limit) and **no plausible fault path** to external pins

## 3) Common-mode and biasing mismatch
Even ignoring speed:

- **HDMI TMDS** receivers expect a specific termination/bias scheme (TMDS is a current-mode style interface with receiver-side termination creating the voltage swing).
- **DisplayPort** main link is typically **AC-coupled** with defined common-mode and link training.

A homebrew “differential pair” driven from an SE source won’t land in the receiver’s expected common-mode window, so it can fail silently.

## 4) Termination and impedance discontinuities
Typical targets:
- DP main link: **~85 Ω differential**
- HDMI TMDS: **~100 Ω differential**

If your circuit is literally “pins wired to pins” with some switching/analogue parts in-between, you can easily introduce:
- stubs
- via/connector discontinuities
- wrong pair impedance
- pair-to-pair skew

At multi-Gbps this is usually fatal.

## 5) Orientation / lane swap reality on USB-C
USB-C is flippable. Without a **Type-C/PD + Alt-Mode controller** (or a bridge that integrates it), your “fixed pin map” will only work in one plug orientation (if at all). If you tried to wire both orientations, you typically create **stubs** that kill the eye.

## 6) ESD and latch-up
HDMI and USB-C are both ESD-heavy connectors. If you have ± rails and analogue switches, you also raise:
- latch-up susceptibility
- back-powering paths through protection diodes
- “works on bench, dies in the field” behaviour

## What a “safe” implementation normally looks like
If you need HDMI out from USB-C, the conventional safe path is:

- **USB-C receptacle**
- **Type-C/PD/Alt-Mode controller**
- **DP lanes into a DP→HDMI bridge IC**
- **HDMI connector**
- ESD on all external pins, correct AC coupling/CMC as per the bridge reference design

## Immediate sanity checks you can do on your schematic
1) **Prove** (with nets) that **−5 V cannot reach any external pin under any single fault** (short, misplug, solder bridge).
2) Confirm the “SE driver” is not directly feeding a DP/HDMI pair without the proper PHY.
3) Confirm you have **no DC path** from external high-speed pins into ± rails through protection structures.
4) Confirm **VBUS** is handled correctly (no backfeed, inrush control if needed).

If you paste (or describe) just these three things, I can be very concrete about what’s wrong/right:
- what the SE source actually is (logic family / amplitude / edge rate)
- where the ±5 V rails go in the circuit
- which exact interface you’re targeting (USB-C DP Alt Mode ↔ HDMI, or HDMI ↔ USB-C display)
