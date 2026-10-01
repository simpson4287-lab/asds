# Single-ended to LVDS Conversion
Date (UTC): 2026-01-14 12:05
Conversation ID: 69678668-57ac-8326-b36f-1db142965d7c
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-004.json

[M1] ME (2026-01-14 12:05):
What’s needed to drive an lvds signal from a single ended input. Part example?

[M2] AI (2026-01-14 12:05):
To go **single-ended → LVDS**, you need a **differential line driver** (often called an *LVDS transmitter*). It takes a CMOS/TTL input (or a clock) and generates a low-swing **balanced pair** (OUT+ / OUT−) suitable for a 100 Ω differential link.

### What you typically need (minimum viable stack)
- **An LVDS driver IC** (single-channel or multi-channel, depending how many signals)
- **100 Ω termination at the receiver** (either internal on the receiver or an external 100 Ω across the pair)
- **Decent routing/cabling** (twisted pair / diff pair, controlled impedance if on PCB)
- Optional but common:
  - **Series damping resistors** (e.g., 10–33 Ω) right at the driver if you see edge-ringing/EMI
  - **Fail-safe biasing** at the receiver if the link can be unplugged (many modern receivers include this)

### Part examples (good “grab and go” options)
**For a logic signal (GPIO / data line):**
- **SN65LVDS1** (Texas Instruments) – single LVDS line driver, TTL/CMOS input → LVDS pair  
- **SN65LVDS2** (TI) – dual driver (2 channels)

**For a clock specifically (low jitter emphasis):**
- **DS90LV011A** (TI) – LVDS line driver commonly used for clocks/data
- **NB3L553 / NB3L553D** (onsemi family) – logic fanout/clock-ish use cases (depends on exact variant)

**If you actually mean “video-ish ADC data buses” (multi-bit):**
- Look at **multi-channel LVDS serializers/drivers** or **LVDS buffer families** depending on rate and interface (the right pick depends heavily on Mbps, voltage, and whether you need SERDES).

### Quick wiring sketch (conceptual)
- Single-ended input → **DIN** of driver  
- Driver outputs → **OUT+ / OUT−** → differential pair / twisted pair  
- At receiver end: **100 Ω across OUT+ and OUT−** (unless receiver has internal termination)

### Two gotchas that bite people
- **Voltage standards:** Some “LVDS” parts are actually **LVDS-like** (sub-LVDS, M-LVDS, SLVS, etc.). Make sure the receiver expects real LVDS levels.
- **Data rate / edge speed:** Pick a driver rated comfortably above your toggle rate; edge rates matter for signal integrity even at “low” frequencies.

If you tell me (1) your single-ended logic level (3.3 V? 1.8 V?), (2) approx bit rate / clock rate, and (3) cable length, I can point to the most appropriate exact part and whether you’ll want series resistors or any biasing.
