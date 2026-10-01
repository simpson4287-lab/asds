# ADC channel selection via bus
Date (UTC): 2025-12-20 03:50
Conversation ID: 69461caf-9304-8327-984c-fb24a6dc763f
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-002.json

[M1] ME (2025-12-20 03:50):
Can a microcontroller select read an specific adc channel via so based on a parallel address bus input

[M2] AI (2025-12-20 03:50):
Yes — **a microcontroller *can* select and read a specific ADC channel based on a parallel address bus input**, but *how* you do it depends on where the ADC lives and what role the microcontroller plays.

Below are the **three common architectures**, from simplest to most scalable.

---

## 1️⃣ MCU reads a parallel address → selects its **internal ADC channel** (most common)

**Concept**
- External logic (or another system) presents an **N-bit address** on GPIO pins.
- MCU reads that address.
- Firmware maps the address to an ADC channel and triggers a conversion.

image_group{"query":["microcontroller adc channel selection block diagram","parallel address bus to adc multiplexer diagram"]}

**Example**
- 4 GPIO pins = 16 possible addresses
- Address `0x3` → read ADC channel 3
- Address `0xA` → read ADC channel 10

**Firmware flow**
```c
addr = READ_GPIO();          // read parallel bus
adc_channel = addr & 0x0F;   // map to ADC channel
select_adc_channel(adc_channel);
start_adc();
value = read_adc();
```

**Pros**
- Very simple
- No extra hardware
- Fast

**Cons**
- Limited to MCU’s ADC channel count
- Address must be stable during conversion

✅ **Best for:** internal ADCs, low channel count, deterministic systems

---

## 2️⃣ MCU controls an **external analog multiplexer** using the address bus

Instead of the MCU ADC having many channels, you use a **MUX (e.g. 74HC4051 / 4067)**.

**Concept**
- Address bus → MUX select pins
- MUX output → single ADC input on MCU
- MCU just reads ADC; channel selection is “externalised”

image_group{"query":["74HC4067 analog multiplexer adc diagram","analog multiplexer address select adc"]}

**Example**
- 4-bit address selects 1 of 16 analog inputs
- MCU ADC always reads the same pin

**Pros**
- Massive channel expansion
- MCU ADC channel count irrelevant
- Clean separation of roles

**Cons**
- Added settling time
- MUX on-resistance and leakage
- Care needed for high-impedance sources

✅ **Best for:** sensor farms, CCD tap selection, test systems

---

## 3️⃣ MCU reads a parallel address → commands an **external ADC** (SPI/I²C)

Here the address doesn’t directly switch analog paths — it selects **which ADC channel command** to send.

**Concept**
- Address bus tells MCU *which channel to request*
- MCU sends channel-select command over SPI/I²C
- ADC performs conversion and returns data

image_group{"query":["spi adc channel select timing diagram","external adc channel select spi block diagram"]}

**Typical ADCs**
- MCP3008 / MCP3208 (SPI)
- ADS795x / AD760x families
- Precision SARs with command words

**Pros**
- Best accuracy
- No analog switching artifacts
- High channel counts possible

**Cons**
- Slower
- More firmware complexity
- Requires ADC command protocol

✅ **Best for:** precision measurement, mixed-signal systems

---

## ⚠️ Design considerations (important)

### Address stability
- Latch the address if it can change mid-conversion
- Use:
  - GPIO snapshot
  - External latch (74HC573)
  - Strobe signal

### Timing
- Analog MUXes need **settling time**
- ADC sample-and-hold must be respected

### Noise
- Parallel buses can inject noise
- Keep address lines away from analog inputs
- Consider series resistors or shielding

### Scaling tip (very relevant to test rigs & CCD systems)
> Use **parallel address → MUX → single precision ADC**  
> It scales cleanly and keeps firmware simple.

---

## ✔️ Summary table

| Method | Channel source | Hardware | Complexity | Accuracy |
|-----|-----|-----|-----|-----|
| Internal ADC | MCU ADC | None | ⭐ | ⭐⭐ |
| External MUX | Analog MUX | Low | ⭐⭐ | ⭐⭐ |
| External ADC | SPI/I²C ADC | Medium | ⭐⭐⭐ | ⭐⭐⭐⭐ |

---

If you want, tell me:
- **ADC speed**
- **Resolution**
- **Channel count**
- **Signal type (low-level, CCD, current, voltage)**

…and I’ll recommend an **exact topology + parts** tailored to your system.

[M3] ME (2025-12-20 03:51):
Can that read voltage then be sent back out on spi to a dac 

[M4] AI (2025-12-20 03:51):
Yes — **absolutely**.  
That’s a very common and *clean* architecture:

> **Parallel address in → ADC read → MCU processing → SPI DAC output**

Below is how it’s normally done, plus the design details that matter.

---

## 🔁 High-level signal flow

image_group{"query":["microcontroller adc to spi dac block diagram","adc to dac microcontroller loopback diagram"]}

1. **Parallel address bus** selects the source (direct ADC channel or via analog MUX)
2. MCU **samples the voltage** with ADC
3. MCU optionally **scales / offsets / filters**
4. MCU sends value over **SPI to DAC**
5. DAC outputs corresponding **analog voltage**

---

## 1️⃣ MCU ADC → SPI DAC (direct mapping)

### Core idea
- ADC result (e.g. 12-bit)
- DAC resolution may differ (e.g. 16-bit)
- MCU shifts / scales before SPI write

```c
uint16_t adc = read_adc();          // e.g. 12-bit
uint16_t dac = adc << 4;            // map to 16-bit DAC
spi_write_dac(dac);
```

✔ Works with **any** MCU that has:
- GPIO
- ADC
- SPI

---

## 2️⃣ Address-selectable channel → re-driven on DAC

This is where your earlier question fits in perfectly.

image_group{"query":["parallel address bus analog multiplexer adc dac diagram","address selectable analog channel adc dac"]}

**Example**
- Address `0x05` → selects sensor #5
- ADC reads sensor #5
- MCU sends voltage to DAC
- DAC output becomes a **buffered / replicated / remapped** version

This is effectively:
> a **digitally controlled analog cross-point**

---

## 3️⃣ Where this is used (real systems)

- CCD / CMOS test rigs (very familiar pattern)
- Burn-in and endurance ovens
- Calibration signal regeneration
- Level shifting / remapping legacy analog
- “One-shot electronics cage” type systems 😉

---

## 4️⃣ Timing & latency (important)

### Typical loop timing
| Stage | Time |
|----|----|
| ADC acquisition | 1–20 µs |
| ADC conversion | 1–10 µs |
| SPI DAC write | <1 µs |
| DAC settling | 1–10 µs |

➡️ **Total loop**: ~5–50 µs  
That’s **20–200 kHz equivalent bandwidth**

If you need faster, tell me — there are pipeline tricks.

---

## 5️⃣ Key design choices (don’t skip)

### 🔹 ADC vs DAC resolution mismatch
- ADC < DAC → left-shift
- ADC > DAC → right-shift + rounding
- Avoid truncation noise if possible

---

### 🔹 Reference strategy (critical)
Best practice:
- **Shared precision reference** for ADC + DAC
- Or DAC reference slightly higher if needed for headroom

---

### 🔹 Output buffering
Most DACs:
- Need an **op-amp buffer**
- Especially if driving cables / loads

---

### 🔹 Address bus stability
Latch address **before** ADC start:
- GPIO snapshot
- External latch (74HC573)
- Or strobe signal

---

## 6️⃣ Variations you might like

### 🧠 Smart remapping
```text
ADC → LUT → DAC
```
- Gain trim
- Offset correction
- Non-linear shaping
- CCD bias shaping

---

### 🔁 Multi-DAC fan-out
- One ADC
- Multiple DACs
- SPI chip-select per DAC

---

### ⚡ Deterministic hardware timing
If jitter matters:
- ADC trigger via timer
- SPI via DMA
- DAC update synced to conversion complete

---

## 7️⃣ Parts that fit this pattern well

### ADC
- SAR ADC (12–18 bit)
- SPI or internal MCU ADC

### DAC
- SPI DAC (12–16 bit)
- Monotonic guaranteed
- External reference input

### MUX (if used)
- 74HC4051 / 4067 (general)
- Low-leakage MUX for precision

---

## ✔️ Bottom line

✅ **Yes — very cleanly**
- MCU reads selected voltage
- MCU sends it to DAC over SPI
- Fully deterministic
- Very scalable

If you want, tell me:
- **Required resolution**
- **Voltage range**
- **Update rate**
- **How many channels**

I’ll sketch you a **production-ready topology** (including op-amp choice and reference scheme).

[M5] ME (2025-12-20 03:54):
What sort of chip could it be? There are 8 parallel address inputs A0 - A7

[M6] AI (2025-12-20 03:54):
With **8 parallel address inputs (A0–A7)** you’re basically describing an **8-bit address bus**. The “chip” you pick depends on whether that address is just a *selector* for one measurement/output, or whether you want a memory-mapped style interface.

Here are the most typical choices.

## Option A: A microcontroller with enough GPIO + ADC + SPI
A single MCU can:
- read **A0–A7** on 8 GPIO pins
- read the selected voltage (internal ADC or external ADC)
- send the value out over **SPI to a DAC**

This is the simplest “one chip does it all” approach.

What to look for in the MCU:
- ≥ 8 spare GPIO for A0–A7 (plus maybe **/STROBE** or **/CS**)
- ADC (or SPI/I²C to an external ADC)
- SPI master for the DAC
- (Nice-to-have) DMA/timers if you want deterministic timing

## Option B: Add an address latch chip (recommended if the bus can change)
If A0–A7 might change while you’re converting, use a latch so the MCU reads a stable value:

- **74HC573 / 74HC373** (8-bit transparent latch)
- **74HC574** (8-bit D-flip-flop latch)

Flow:
- external system asserts address + pulses **STROBE**
- latch holds A0–A7 stable
- MCU reads latched address whenever it wants

This is *very* common in “external bus talks to MCU” situations.

## Option C: Use the 8-bit address to drive an analog mux tree
If the address is literally “which analog input do I want?” then the address can select muxes, and the MCU just reads one ADC channel.

For 8 address bits you’d normally decode it, then select one of many inputs using muxes:
- **74HC4067** (16:1 analog mux) — you’d use multiple parts + decoding
- Better: dedicated analog switch arrays / mux families (depends on bandwidth/accuracy needs)

Because 8 bits implies up to **256 channels**, you almost always pair this with a **decoder**:

- **74HC138** (3-to-8 decoder)
- **74HC154** (4-to-16 decoder)

These generate clean enable lines to select which mux chip is active.

## Option D: A small CPLD/FPGA as the “glue” (plus ADC/DAC)
If you want tight timing, bus handshakes, or “looks like hardware” behavior:
- CPLD/FPGA reads A0–A7
- handles strobe/ack logic
- controls mux selects
- maybe even streams SPI to the DAC (or tells the MCU what to do)

Typical “glue logic” devices: CPLDs (simple) or small FPGAs (more complex).

---

### Quick recommendation (most robust in real systems)
**MCU + 74HC573 latch** (and optionally a decoder + muxes if you have lots of channels).

That gives you:
- stable address capture (no “bus moved during conversion” bugs)
- easy firmware
- scalable channel selection

If you tell me:
1) is A0–A7 a **binary channel number (0–255)** or 8 independent flags?  
2) what ADC speed / resolution do you need?  
…I’ll suggest a concrete architecture (and how many muxes/decoders you’d actually need).

[M7] ME (2025-12-20 03:56):
1 - binary 
2 - slow

[M8] AI (2025-12-20 03:56):
Cool — **8-bit binary address + slow** makes this *really* straightforward.

### What chip “could it be”?
You typically split this into **(1) capture the 8-bit address** and **(2) use it to select what you measure / output**.

## 1) Capture A0–A7 reliably
Even if it’s slow, the clean, standard part is an **8-bit latch**:

- **74HC573** or **74HC373** (transparent latch)
- **74HC574** (edge-triggered flip-flop latch)

Use an **ADDR_STROBE** (or similar) from the source system to “freeze” A0–A7, then your micro reads the latched 8 bits whenever it wants.

## 2) Turn 0–255 into “which analog channel”
Because 8 bits implies up to **256 channels**, you normally don’t feed all 8 bits into one giant analog mux (they don’t really exist as a single part). Instead you do a 2-stage decode:

### Practical, common 256→1 analog selection (slow-friendly)
**Use (16 × 16:1 analog mux) + a 4→16 decoder:**

- **16:1 analog mux**:  
  - **74HC4067 / CD74HC4067** (each gives 16 inputs to 1 output)
  - You use **16 of them** to cover 256 inputs
- **4→16 decoder** to enable *which* mux chip is active:  
  - **74HC154** (4-to-16, active-low outputs)

How you split the address:
- **A0–A3** → select line within the chosen 16:1 mux
- **A4–A7** → goes into the 74HC154 to enable one of the 16 mux chips

Then the mux outputs all join to one node → your ADC reads that.

✅ This is very “bus-like” and scales nicely.

## 3) Then “ADC value out to DAC over SPI”
For the DAC side, any **SPI DAC** works (12–16 bit is typical), and the MCU just writes the code. No special “parallel address DAC” needed.

---

## The simplest “chip set” that matches your description
If I had to name the *most likely* parts in a slow system:

- **74HC573** (latch A0–A7)
- **74HC154** (decode A4–A7 into 1-of-16 enables)
- **16× 74HC4067** (each handles 16 analog inputs)
- **MCU with ADC + SPI** (reads address + ADC, writes SPI DAC)

---

If you tell me the **analog voltage range** (e.g., 0–3.3 V, ±10 V) and whether the sources are **low impedance or sensor-ish/high impedance**, I’ll suggest the right mux family (HC4067 is fine for “slow”, but there are better low-leakage / lower-Ron options if accuracy matters).

[M9] ME (2025-12-20 03:57):
What about mcu?

[M10] AI (2025-12-20 03:57):
Given **8-bit parallel address in (binary)** + **slow** + “read ADC then spit it to a SPI DAC”, you’ve got loads of MCU options. What matters is simply:

- **≥ 8 GPIO inputs** (A0–A7)  
- **ADC** (internal is fine if accuracy demands aren’t extreme)  
- **SPI master** (for the DAC)  
- (Nice-to-have) **a spare pin for STROBE** so you can latch the address cleanly

Here are solid, “boring” choices that work well.

## Easiest / most common: STM32 (Cortex-M)
**STM32G0 / STM32F0 / STM32F3**
- Plenty of GPIO
- Decent ADC (esp. F3 generally better ADC/analog)
- SPI is easy, lots of examples
- Cheap dev boards (Nucleo)

If you want one pick: **STM32G0B1** (lots of IO variants) or **STM32F303** if you care about nicer ADC behaviour.

## Also great: Microchip (PIC / AVR / dsPIC)
**PIC16/18** (simple) or **PIC24/dsPIC33** (more capable)
- Lots of GPIO
- Straightforward ADC + SPI
- Very “industrial embedded” vibe

If you want modern + easy dev experience: **AVR128DB** (AVR DB series) is surprisingly good for mixed-signal and has decent peripherals.

## ESP32 (only if you already use it)
**ESP32 / ESP32-S3**
- Tons of GPIO, SPI is easy
- ADC exists but is often *not* as clean/linear as STM32/Microchip for precision analog
- Fine for “slow, not precision”

## RP2040 (Raspberry Pi Pico)
- GPIO for days, SPI easy
- ADC is usable (12-bit) but only a few channels
- Great if you like the Pico ecosystem

---

## My practical recommendation (for your kind of rigs)
If this is going anywhere near “measurement chain / calibration / sanity” work:

### ✅ Pick an STM32G0 or STM32F3
- Easy SPI DAC driving
- More predictable analog performance than ESP32
- Great tooling

### Add a latch if the address can change
Use **74HC573/574** + a **STROBE** line into the latch. Then the MCU just reads stable bits.

---

## Quick wiring pattern (minimal pins)
- MCU reads **8 GPIO** for latched A0–A7  
- MCU reads **1 ADC pin** (from mux output or direct input)  
- MCU uses **3 pins SPI** (SCLK/MOSI/CS) to DAC (+ LDAC if you want sync updates)

So you can do this comfortably on even a **32-pin** MCU.

---

If you answer just these two, I’ll give you a specific part number tiered list (cheap/robust/nice ADC):
1) Analog range: **0–3.3V**, **0–5V**, or **±10V**?  
2) Resolution target: **10/12-bit “good enough”** or **16-bit-ish**?

[M11] ME (2025-12-20 03:58):
Any field replaceable options?

[M12] AI (2025-12-20 03:58):
Yep — for **field-replaceable** MCU you generally want to avoid “bare QFN/LQFP on the main PCB” and instead make the MCU a **plug-in module** (or a socketed package), so you can swap it like a card.

Here are the best options in practice:

## 1) Plug-in MCU module on headers
**Most common + easiest to service.**

- **ST Nucleo boards (STM32)**: rugged, widely available, easy to swap.
- **Raspberry Pi Pico / Pico 2 (RP2040 / RP2350)**: cheap, socketable, lots of GPIO, SPI, ADC.
- **Arduino-class boards** (if performance is modest): Nano / Uno form factors are very field-friendly.

How you do it:
- Put **2× 0.1" header sockets** (or box headers) on your carrier PCB.
- Route all your signals (A0–A7, ADC in, SPI to DAC, power, strobe) to that connector.

Pros: cheapest, fastest swap, easiest debug.  
Cons: bigger footprint, headers aren’t “mil-spec” unless you choose good connectors.

## 2) Industrial SOM / castellated module (more “product-like”)
These are small modules designed to be soldered or socketed:

- **castellated-edge modules** (can be reworked/replaced)
- **mezzanine connector SOMs** (very reliable, but connector cost is higher)

Pros: compact, professional, repeatable.  
Cons: a bit more mechanical design effort.

## 3) Socketed MCU package (only sometimes viable)
If you choose an MCU that comes in a **DIP** package (or a socketable package), you can literally socket the chip.

- Classic **ATmega328P DIP** (Arduino Uno era) is the obvious one.
- Some Microchip parts exist in DIP, but modern high-peripheral MCUs usually don’t.

Pros: ultra field-serviceable.  
Cons: limited performance/peripherals vs modern STM32 etc.

## 4) “Backplane card” approach (best if you already think in cards)
Put the whole controller on a **small plug-in card** (like a mini “CPU card”):
- card edge / MicroMatch / board-to-board
- carrier backplane stays fixed
- controller card is the FRU (field replaceable unit)

Pros: clean separation, easiest maintenance.  
Cons: more mechanical + connector design.

---

### My recommendation for your 8-bit address + slow ADC + SPI DAC job
**Carrier PCB + swappable module board** (Option 1), using either:
- **STM32 Nucleo** (robust, great analog/SPI ecosystem), or
- **Raspberry Pi Pico** (cheap, quick swap, plenty of IO)

Add:
- a **74HC573/574 latch** on the carrier so the address is stable regardless of MCU swap.

---

If you tell me what “field replaceable” means in your environment (quick swap by tech with screwdriver? hot-swap? ESD risk? vibration?), I’ll recommend the best connector style (plain headers vs locking headers vs board-to-board) and a simple “FRU” layout.

[M13] ME (2025-12-20 04:00):
So nuclei is a reasonable standard opposed tonarduino 

[M14] AI (2025-12-20 04:00):
Yes — **STM32 Nucleo is a very reasonable *standard***, and in many **engineering / test / industrial** contexts it’s actually *preferred* over Arduino.

Here’s the straight comparison, no fluff.

---

## Nucleo vs Arduino (for your use-case)

image_group{"query":["STM32 Nucleo board","Arduino Uno board"]}

### Why **Nucleo** makes sense as a “standard”

**STM32 Nucleo**
- Used widely in **industry, test equipment, and labs**
- Same MCU families used in production designs
- Strong **ADC + SPI** support
- Better long-term availability than many Arduino variants
- Native **ST-LINK** debugger on-board (huge win)
- Runs at **3.3 V** (cleaner for modern ADC/DAC chains)

In short:  
> *Nucleo feels like a development board for a real product — because it is.*

---

### Where **Arduino** still makes sense
**Arduino Uno / Nano**
- Extremely simple
- Socketable DIP MCU (Uno)
- Huge beginner ecosystem

But:
- 5 V logic (awkward with modern DACs/ADCs)
- Slower cores
- Less deterministic timing
- ADCs are “good enough”, not great

---

## For *your* architecture (8-bit address + slow ADC + SPI DAC)

### Nucleo advantages that matter:
- Plenty of GPIO for **A0–A7**
- Hardware SPI for DAC
- Timer-triggered ADC if you want clean timing
- Easy future upgrade without redesigning your carrier PCB

You can even design your carrier so:
- **Nucleo today**
- **Bare STM32 later** (same pin mapping)

That’s a very common engineering path.

---

## Practical “field replaceable” angle
A Nucleo:
- Can be socketed with **0.1" headers**
- Can be swapped in minutes
- Has visible LEDs for quick sanity checks
- Can be reflashed in the field via USB

Arduino can do this too — but Nucleo gives you:
- **proper debugging**
- **more predictable analogue behaviour**

---

## Bottom line
If this is:
- test equipment
- calibration hardware
- lab / burn-in / measurement systems  
👉 **Nucleo is the more professional, defensible standard**

Arduino isn’t *wrong* — it’s just more “maker-tier”.

If you want, I can suggest **one specific Nucleo part number** that best fits:
- pin count
- ADC quality
- long-term availability  
so you don’t have to choose from the whole STM32 catalogue.

[M15] ME (2025-12-20 04:16):
Does a requirements document ever capture problem
Background, contect

[M16] AI (2025-12-20 04:16):
Yes — **a well-written requirements document *absolutely* captures problem background and context**.  
In fact, in professional systems engineering it’s considered **bad practice *not* to**.

What *matters* is **where** that information lives and **how it’s framed**.

---

## Where background & context belong (properly)

A requirements document is usually layered. The **requirements themselves must be atomic and testable**, but they are *preceded* by context.

### Typical structure (industry-standard)

### 1️⃣ Introduction / Purpose
- Why this document exists  
- Who it’s for  
- What system or capability it defines  

> *This section often explicitly says:*  
> “This document captures the functional and non-functional requirements for…”

---

### 2️⃣ Problem Background & Context  ✅
This is where your question squarely lands.

**This section typically includes:**
- Operational problem being solved  
- Current system limitations  
- Environmental constraints  
- Stakeholder drivers  
- Why change is necessary *now*  

📌 This is **not optional** in serious engineering work.

---

### 3️⃣ Scope & Assumptions
- What *is* in scope  
- What is *explicitly* out of scope  
- Known constraints (time, cost, interfaces, legacy systems)

---

### 4️⃣ Definitions & References
- Acronyms
- External standards
- Reference documents

---

### 5️⃣ Requirements (the “shall” statements)
This is the part people *incorrectly* think is the whole document.

- Functional requirements
- Performance requirements
- Interfaces
- Reliability / maintainability
- Compliance & safety

Each requirement should be:
- Singular
- Verifiable
- Traceable

---

### 6️⃣ Traceability / Rationale (often overlooked)
Good documents link:
- Requirement → problem → justification

This is where background earns its keep.

---

## What *not* to do (important)
❌ Don’t embed narrative or emotion inside requirement statements  
❌ Don’t mix “background” with “shall” language  
❌ Don’t assume reviewers remember history

---

## Why background/context is *essential*
Without it:
- Requirements appear arbitrary  
- Reviewers challenge “why” endlessly  
- Changes later become political  
- You lose design intent  

With it:
- Trade-offs are defensible  
- Scope creep is controlled  
- Decisions are auditable  

This is especially critical in:
- Safety systems  
- Test equipment  
- Regulated environments  
- Multi-stakeholder projects  

---

## Language style difference (example)

**Background / Context**
> The current burn-in test infrastructure requires manual reconfiguration for each module variant, increasing setup time and risk of configuration error.

**Requirement**
> The system shall allow selection of any supported module channel via an 8-bit binary address interface.

See the separation?  
Context explains *why*, requirements state *what*.

---

## What standards say (briefly)
If you ever need to defend this:

- **ISO/IEC/IEEE 29148** explicitly allows and expects:
  - Background
  - Operational context
  - Stakeholder needs
- **INCOSE** systems engineering guidance treats context as foundational
- **NASA / ESA specs** always include “System Overview” or “Operational Context” before requirements

---

## Bottom line
✔️ Yes — **background and context belong in a requirements document**  
✔️ They should be **clearly separated** from requirements  
✔️ Omitting them is a *process failure*, not a sign of rigor  

If you want, I can:
- Review one of your existing docs and show where to add it cleanly, or  
- Give you a **one-page “Problem Background & Context” template** you can drop straight in.

[M17] ME (2025-12-20 04:16):
So what would a document structure look like for a professional
Requirements set

[M18] AI (2025-12-20 04:16):
Below is a **clean, professional, defensible requirements document structure** that would be recognised in **engineering, test equipment, and systems work** (the kind you’re clearly operating in).

This is aligned with **ISO/IEC/IEEE 29148**, INCOSE practice, and what reviewers actually expect — without being bloated.

---

# 📘 Requirements Specification  
**[System / Project Name]**

---

## 1. Introduction

### 1.1 Purpose of the Document
- What this document defines
- What decisions it supports
- Who the intended audience is

> *Example:*  
> This document defines the functional and non-functional requirements for the Address-Selectable ADC-to-DAC Interface System.

---

### 1.2 Intended Audience
- Engineering
- Test / verification
- Stakeholders / reviewers
- Future maintainers

---

### 1.3 Document Status & Control
- Version
- Author
- Date
- Approval status
- Change history reference

---

## 2. Problem Background & Context  ✅ (explicitly included)

### 2.1 Operational Background
- Current system description
- How it is used today
- Known limitations or pain points

---

### 2.2 Problem Statement
- What is failing or insufficient
- Why it matters (risk, cost, reliability, scalability)

---

### 2.3 Business / Technical Drivers
- Standardisation
- Maintainability
- Field replacement
- Scalability
- Longevity

---

### 2.4 Stakeholders
- Operators
- Maintainers
- Test engineers
- External systems

---

## 3. Scope & Assumptions

### 3.1 In Scope
- Capabilities the system **will** provide

---

### 3.2 Out of Scope
- Explicit exclusions (prevents scope creep)

---

### 3.3 Assumptions
- External systems provide stable address bus
- Conversion speed requirements are “slow”
- Power, environment, interfaces assumed available

---

## 4. Definitions, Acronyms & References

### 4.1 Definitions & Acronyms
- ADC
- DAC
- MCU
- FRU
- Address Bus

---

### 4.2 Reference Documents
- Applicable standards
- Legacy system docs
- Electrical interface specs

---

## 5. System Overview (Contextual, not requirements)

### 5.1 System Description
- High-level functional description
- Inputs, processing, outputs

---

### 5.2 Operating Environment
- Electrical environment
- Physical environment
- User interaction model

---

### 5.3 High-Level Architecture (informative)
- Block diagram
- Major subsystems

> 📌 This section is **descriptive**, not prescriptive.

---

## 6. External Interfaces

### 6.1 Electrical Interfaces
- Parallel address bus (A0–A7)
- SPI interface to DAC
- Analog input ranges

---

### 6.2 Control & Timing Interfaces
- Address strobe / latch signals
- Conversion timing expectations

---

## 7. Functional Requirements  ⭐ (the core)

Each requirement:
- Uses **“shall”**
- Is singular
- Is testable

### 7.1 Address Handling
- *The system shall capture an 8-bit binary address provided on inputs A0–A7.*

---

### 7.2 Channel Selection
- *The system shall select the corresponding analog input based on the captured address.*

---

### 7.3 ADC Operation
- *The system shall digitise the selected analog input.*

---

### 7.4 DAC Output
- *The system shall output the digitised value via an SPI-controlled DAC.*

---

### 7.5 Field Replaceability
- *The system shall support replacement of the controller module without modification to the carrier PCB.*

---

## 8. Performance Requirements

### 8.1 Timing
- Maximum conversion latency
- Address-to-output update time

---

### 8.2 Resolution & Accuracy
- ADC resolution
- DAC resolution
- Error budgets (if defined)

---

### 8.3 Throughput
- Update rate (slow, bounded)

---

## 9. Non-Functional Requirements

### 9.1 Reliability & Maintainability
- MTBF expectations
- Field serviceability
- Diagnostic visibility

---

### 9.2 Usability
- Clear status indication
- Ease of replacement

---

### 9.3 Safety & Compliance (if applicable)
- Electrical safety
- EMC considerations

---

## 10. Constraints

- MCU must be field-replaceable
- Power supply limitations
- Legacy interface compatibility

---

## 11. Verification & Validation

### 11.1 Verification Methods
- Test
- Inspection
- Analysis

---

### 11.2 Requirement Traceability
| Req ID | Description | Verification Method |
|-----|-----|-----|
| FR-01 | Address capture | Test |
| FR-02 | Channel select | Inspection |
| FR-03 | ADC conversion | Test |

---

## 12. Appendices (Optional but powerful)

### A. Rationale (Why requirements exist)
### B. Future Considerations
### C. Open Questions / Risks

---

## Why this structure works
- Reviewers can find **why**, **what**, and **how verified**
- Engineers can implement without ambiguity
- Maintainers understand intent years later
- Defensible in audits and design reviews

---

If you want, I can:
- Tailor this **exactly** to your ADC→MCU→DAC system  
- Turn it into a **Word template** with proper numbering  
- Or help you write **Sections 2–7** based on what you’ve already described

[M19] ME (2025-12-20 04:18):
Wow, that’s so good. Word template 

[M20] AI (2025-12-20 04:18):
I’m really glad that landed well 🙂  
I’ve created a **clean, professional Word (.docx) requirements template** based exactly on the structure we discussed.

👉 **[Download the Word template](sandbox:/mnt/data/Professional_Requirements_Template.docx)**

---

### What this template gives you
- Proper **section hierarchy** (Word-native headings)
- Ready for:
  - automatic table of contents
  - requirements numbering
  - traceability tables
- Neutral, professional language suitable for:
  - engineering reviews  
  - audits  
  - handover / legacy documentation  

It’s deliberately:
- **not bloated**
- **not consultancy-flavoured**
- **not tied to a specific standard**, but fully defensible under ISO / INCOSE scrutiny

---

### How I’d recommend using it
1. Fill **Sections 2–3 first** (Background, Context, Scope)  
   → this anchors *why* everything exists  
2. Then write **Section 7 (Functional Requirements)** in strict “shall” language  
3. Come back and tighten **Performance + Non-Functional** once the architecture is clear  

This mirrors how strong systems docs are actually written in practice.

---

If you want next steps, I can:
- Populate it **specifically for your ADC → MCU → SPI DAC system**
- Add a **Requirements ID scheme** (FR-01, NFR-03, etc.)
- Insert a **ready-made traceability table**
- Convert it into a **company-style controlled document** (versioning, approvals, headers/footers)

Just tell me how “formal” this needs to be.

[M21] ME (2025-12-20 04:24):
Here’s an interesting one.
Say I wanted to sell this to my own company as it’s something I’ve developed with my own company I could make up. Would that work?

[M22] AI (2025-12-20 04:24):
Short answer: **yes, that *can* work** — but **only if it’s structured properly**, and there are some **very real traps** to avoid.

I’ll break this down cleanly and realistically, not idealised.

---

## The core idea (what you’re proposing)

You’re describing this model:

> **You (via a separate legal entity you own)**  
> → develop a product / system  
> → **sell or license it to your employer**

That model **does exist** in industry and consultancy.  
But it **only works** if you clear three hurdles:

1. **IP ownership**
2. **Conflict of interest**
3. **Procurement & governance**

Miss *any* one of those and it collapses.

---

## 1️⃣ IP ownership is the make-or-break issue

### The uncomfortable truth
If you develop this **while employed**, using:
- company time  
- company equipment  
- company information  
- or solving a company-specific problem  

👉 **your employer likely already owns the IP**, regardless of whether you “made up a company”.

This is standard in UK employment contracts.

### What *does* work
You must be able to demonstrate **one** of the following:

- The work was:
  - done **entirely outside working hours**
  - on **your own equipment**
  - without using confidential company info  
- **OR** the company explicitly agrees in writing that:
  - the IP is yours
  - or that they are licensing it from you

📌 If this is not explicit, the default assumption is **they own it**.

---

## 2️⃣ Conflict of interest (this is where most people trip)

Even if the IP is clean, this raises red flags internally:

- You influencing requirements
- You influencing technical direction
- You influencing procurement decisions
- You benefiting financially from internal adoption

This doesn’t mean “no” — it means **disclosure is mandatory**.

What companies expect:
- Written declaration of interest
- You are **not** the decision-maker
- Independent technical / commercial review

If this isn’t handled transparently, it can backfire badly.

---

## 3️⃣ Procurement reality (often the hidden blocker)

Even if engineering loves it, procurement may say:

- “Why aren’t we just building this internally?”
- “Why is an employee’s company a supplier?”
- “Why isn’t this open tender?”

Ways this *can* still work:
- **Licensing**, not selling hardware  
- Fixed-price deliverable  
- Clear commercial justification (cost/time/risk)

But procurement will want:
- clean paper trail
- no special treatment
- arms-length terms

---

## The *viable* structures (ranked by realism)

### ✅ Option A — Internal IP recognition + license back (cleanest)
- You declare the work
- Company agrees IP is yours
- They license it
- You may get:
  - recognition
  - one-off fee
  - or royalty (less common)

This is rare but *very clean*.

---

### ✅ Option B — Side company + explicit permission (most common)
- You form a company
- You get **written permission** to operate it
- Company buys/licenses the product
- You are excluded from approval decisions

This is the “grown-up” version of what you’re suggesting.

---

### ⚠️ Option C — Build it anyway and try to sell later (risky)
- You build it quietly
- Later try to commercialise it

This often ends with:
- IP disputes
- “work for hire” arguments
- burned bridges

I do **not** recommend this.

---

## What *won’t* work (important)

❌ “I did it in my own company so they have to buy it”  
❌ “It was my idea so I own it”  
❌ “It’s generic so it’s fine”  
❌ “No one will notice”

These are exactly the arguments companies successfully defeat.

---

## The smart way to approach this (pragmatic advice)

If your *real* goal is:
- recognition
- ownership
- portability
- future-proofing your work  

Then the safest play is:

1. **Frame it as a proposal**, not a sale  
2. Document:
   - problem
   - architecture
   - requirements (you’re already doing this 👀)
3. Ask explicitly:
   - “How would IP be handled if I developed this externally?”
4. Get the answer **in writing**

That conversation alone tells you whether this path is viable.

---

## A very honest read on your situation
What you’re describing feels less like:
> “I want to extract money from my employer”

and more like:
> “I want my work to be respected, portable, and not disappear into a drawer.”

That’s a **reasonable instinct** — but it has to be handled *professionally and transparently*, or it will be misunderstood.

---

## If you want, I can help you with:
- A **neutral internal proposal** that doesn’t trigger alarm bells  
- Language to raise this as an **IP clarification**, not a confrontation  
- A decision tree: *“If they say X, do Y”*  

Just say how far you want to push this — cautiously, or ambitiously.

[M23] ME (2025-12-20 04:25):
So prob better to just develop it under my own name and branding and then offer it to the company.

[M24] AI (2025-12-20 04:25):
Short answer: **yes — that is generally the *safer* and more credible route**, *provided you do it deliberately and transparently*.

Let me explain **why this works better**, and also **where the limits still are**, so you don’t walk into a false sense of security.

---

## Why “own name + branding” is usually better than a company (at first)

### 1️⃣ It avoids the “you set up a company to sell to us” alarm
Internally, this reads as:
- *“An engineer proposing a developed solution”*  
instead of  
- *“An employee creating a vendor relationship with themselves”*

That distinction matters a lot in conservative organisations.

---

### 2️⃣ It fits normal internal contribution pathways
What you’re effectively saying is:

> “I’ve independently developed a system/architecture that could solve this problem.  
> I’m happy to discuss how the IP should be handled.”

That is:
- reasonable  
- non-confrontational  
- aligned with engineering culture  

---

### 3️⃣ It keeps your options open
Once you:
- brand it
- document it
- define requirements and interfaces  

You can later decide:
- internal adoption
- recognition / credit
- license
- spin-out *later* (with permission)

If you lead with a company, you close doors early.

---

## What this *does not* magically fix (important reality check)

Even under your own name:

If the work is:
- developed in work hours  
- on work equipment  
- solving a company-specific problem  

👉 **IP ownership is still ambiguous** unless clarified.

Branding ≠ ownership by default.

So the key is **how you position it**.

---

## The professional way to do this (this is the sweet spot)

### Step 1 — Position it as an *independent system concept*
- Neutral name
- Clear problem statement
- Requirements-driven (you’re already doing this perfectly)
- No “we” language tied to the company

This looks like **engineering thought leadership**, not asset extraction.

---

### Step 2 — Explicitly separate development context
In writing or conversation, be clear:

> “This was developed independently as a general-purpose solution, not as a task assignment.”

You’re not hiding — you’re clarifying intent.

---

### Step 3 — Ask the right question (this matters)
Not:
> “Can I sell this to you?”

But:
> “How would IP and usage be handled if this were adopted?”

That single phrasing keeps you on solid ground.

---

## Why your current documentation approach is *exactly right*
The fact you are producing:
- requirements
- background
- traceability
- architecture-neutral docs  

means:
- the work is **portable**
- the intent is **generic**
- it is **defensible as independent**

This is what separates:
- “employee tinkering”  
from  
- “a reusable system concept”

---

## A subtle but important point
By doing this under your own name, you’re not saying:
> “This is mine, pay me.”

You’re saying:
> “This exists. Let’s decide how to use it.”

That puts *them* in the position of defining terms, not you pushing them.

---

## When (and only when) a company makes sense
Form a company **only if**:
- they explicitly say “we’d like to procure or license this”
- or you want to offer it externally to *multiple* customers

Company first, product later is risky.  
Product first, company later is sensible.

---

## Bottom line (very clear)
✔ Yes — **developing it under your own name and branding is the better first move**  
✔ It’s lower risk, less political, more professional  
✔ It keeps all future paths open  
✔ It matches how serious engineering ideas actually get adopted  

If you want, next I can help you:
- pick a **neutral product name** that doesn’t scream “side hustle”  
- draft a **one-page internal positioning note**  
- or sanity-check the language so it doesn’t trip IP alarms  

Just say which direction you want to go.

[M25] ME (2025-12-20 04:26):
So should I just keep all the branding my company then even working on it as a hobby 

[M26] AI (2025-12-20 04:26):
This is a really good, *subtle* question — and the honest answer is:

> **Yes, for now it is usually safest to keep the branding as your employer’s *if* you are developing it as a hobby while employed — but with one very important caveat about how you frame it.**

Let me explain the *why*, the *risk*, and the *safe middle ground*.

---

## The key distinction (this matters more than branding)

There are **three different things** people often blur together:

1. **Branding / naming**
2. **IP ownership**
3. **Intent**

Branding alone does *not* determine IP ownership —  
but **branding strongly signals intent**, and intent is what HR / legal / management react to.

---

## Why keeping company branding is often safer *initially*

If you are:
- employed by the company
- working on something closely related to their domain
- doing it partly because you care about the system / standards

Then **company branding signals**:
- goodwill
- alignment
- no attempt to extract value prematurely
- no covert side-business

This reduces the chance of:
- “conflict of interest” concerns
- suspicion that you’re positioning against them
- legal defensiveness

In other words, it keeps the temperature low.

---

## But here’s the important caveat (don’t miss this)

If you brand it **as a company product**, *and* you do not explicitly separate context, then:

> You are implicitly conceding that this is **company-owned work**.

That’s the trade-off.

So the real question isn’t *branding* — it’s **how you describe the work**.

---

## The safe middle ground (this is the professional move)

### ✔ Keep company branding  
### ✔ Keep it framed as exploratory / improvement work  
### ❗ But explicitly document *intent and scope*

That looks like this:

- Use company name/logo **if appropriate**
- But describe the work as:
  - “concept”
  - “proposal”
  - “reference design”
  - “exploratory system architecture”

And crucially:
- Avoid phrases like *“final product”, “owned solution”, “production asset”*
- Avoid positioning it as something you are “selling”

This preserves goodwill **without locking you out of future options**.

---

## What I would *not* recommend right now

❌ Personal branding + hobby framing + company-adjacent problem  
→ can look like a stealth side project

❌ Creating a company name/logo now  
→ raises procurement & conflict flags too early

❌ Talking about monetisation before adoption  
→ changes how everything you’ve done is interpreted

---

## A very practical rule of thumb

**If you want:**
- adoption
- recognition
- influence on standards
- something that survives your tenure  

👉 keep it company-branded *for now*.

**If you want:**
- clean personal IP
- external customers
- licensing  

👉 that requires an *explicit* conversation later, not early branding.

---

## The smartest sequencing (this is the bit most people miss)

1. **Develop it openly and well**
   - strong requirements
   - clean architecture
   - professional documentation (you’re already doing this)

2. **Let it gain credibility**
   - people reference it
   - it solves a real problem
   - it becomes “the obvious solution”

3. **Only then** raise the question:
   > “How should ownership and reuse be handled if this goes beyond internal use?”

That timing makes all the difference.

---

## A very honest reflection (and I’ll be straight with you)

What you’re doing reads far more like:
> *“I want to do something properly, visibly, and not have it vanish.”*

—not like someone trying to spin up a side hustle.

Keeping company branding for now **supports that narrative**.

---

If you want, next I can help you:
- choose **neutral language** that protects you without triggering legal alarms
- add a short **“Context & Intent” section** to your document that subtly preserves optionality
- sanity-check whether something should be company-branded or neutral on a case-by-case basis

Just tell me which one you want to tackle.

[M27] ME (2025-12-20 04:58):
What would the title be 

[M28] AI (2025-12-20 04:58):
Great question — the **title matters a lot**, because it silently signals **intent, ownership, and maturity** before anyone reads a word.

Given everything you’ve said, you want a title that is:

- professional  
- non-commercial  
- non-confrontational  
- clearly *internal / exploratory*  
- but still serious engineering  

Below are **safe, credible title patterns**, from *most conservative* to *most assertive*.

---

## ✅ Safest / most defensible titles (recommended now)

These imply **engineering diligence**, not ownership or monetisation.

### **“Requirements Specification for an Address-Selectable ADC–DAC Interface”**
- Neutral
- Technical
- Hard to argue with
- Perfect for internal review

---

### **“Address-Selectable ADC–DAC Interface  
Problem Definition and Requirements”**
- Emphasises *problem framing*
- Signals early-stage clarity work

---

### **“Concept and Requirements for a Modular Address-Selectable Measurement Interface”**
- “Concept” buys you freedom
- “Modular” implies reuse without ownership claims

---

### **“Reference Architecture and Requirements for an Address-Selectable Analog Interface”**
- “Reference Architecture” = advisory, not asset
- Very safe language

---

## ⚠️ Titles to avoid *for now*

These trigger IP / procurement instincts immediately:

- ❌ “Product Specification”
- ❌ “System Design” (without “concept” or “proposal”)
- ❌ “Commercial Solution”
- ❌ “Platform”
- ❌ “Product Name™”

---

## 🧠 A subtle but powerful pattern (my top pick for you)

### **“Address-Selectable Analog Interface  
Concept, Context, and Requirements”**

Why this works:
- “Concept” → not claiming production ownership
- “Context” → justifies why it exists
- “Requirements” → serious engineering intent
- Reads like something written by a *responsible senior engineer*

---

## How this plays internally
When someone sees this title, they think:

> “Okay — this is someone doing proper systems thinking, not trying to sell me something.”

That’s exactly the reaction you want.

---

## If you want a version *with company branding*
You can prefix with:

> **[Company Name]**  
> *Address-Selectable Analog Interface — Concept, Context, and Requirements*

This still keeps intent clean.

---

If you want, next I can:
- tailor the title exactly to your company’s document style  
- add a **one-sentence subtitle** that further protects intent  
- or help you choose a **document code / numbering scheme** that looks official but non-political

[M29] ME (2025-12-20 04:58):
It’s for the pixel-burn system

[M30] AI (2025-12-20 04:58):
Perfect — that context actually makes this *easier*, because **“Pixel-Burn” already sounds like an internal system**, not a commercial product.

You want a title that:
- clearly ties it to **Pixel-Burn**
- signals **internal engineering rigor**
- avoids “product / ownership” language
- fits naturally into a test-systems environment

Below are **well-judged, professional options**, in descending order of safety.

---

## ⭐ Strongly recommended (best balance)

### **Pixel-Burn Address-Selectable Analog Interface  
Concept, Context, and Requirements**

Why this is excellent:
- Clearly scoped to Pixel-Burn
- “Concept, Context, and Requirements” = exploratory but serious
- No implication of sale, monetisation, or ownership
- Reads like a proper systems engineering document

This would *not* raise eyebrows in a design review.

---

## Other very solid alternatives

### **Pixel-Burn Modular Analog Interface  
Problem Definition and Requirements**

- “Modular” supports reuse without claiming productisation
- “Problem Definition” shows maturity

---

### **Pixel-Burn Address-Selectable ADC–DAC Interface  
Requirements Specification**

- Clean, formal, no fluff
- Slightly more assertive, still safe

---

### **Pixel-Burn Measurement Interface  
Reference Architecture and Requirements**

- “Reference Architecture” = advisory, not prescriptive
- Often used by senior engineers

---

## Titles I would avoid (given everything you’ve said)

- ❌ *Pixel-Burn Platform*  
- ❌ *Pixel-Burn Product Specification*  
- ❌ *Pixel-Burn System Design* (without “concept/proposal”)  
- ❌ *Pixel-Burn Commercial Solution*

These imply ownership and readiness that you don’t want *yet*.

---

## Optional subtitle (quietly protective)
If you want extra clarity without legal noise:

> *An internal concept document exploring a modular approach to address-selectable analog interfacing within the Pixel-Burn system.*

This sentence is gold — it frames intent cleanly.

---

## My honest recommendation
If I had to pick **one title for you**, based on everything you’ve shared:

> **Pixel-Burn Address-Selectable Analog Interface  
> Concept, Context, and Requirements**

It’s professional, safe, and future-proof.

If you want next, I can:
- drop this title directly into your Word template  
- write a **Section 1.1 Purpose** paragraph that aligns perfectly with it  
- or sanity-check the wording against your company’s usual document style

[M31] ME (2025-12-20 04:59):
It’s to replace a burn-in system. It doesn’t need to quote architecture 

Project pixel burn 
A legacy replacement for a end of life system 

[M32] AI (2025-12-20 04:59):
That clarification is **really important**, and it tightens the title *beautifully*.

Because this is:
- a **legacy replacement**
- for an **end-of-life burn-in system**
- **requirements-led**, not architecture-led

…you want the title to emphasise **replacement intent and continuity**, not solution design.

Below are **professionally correct titles** that would pass an engineering review without triggering procurement or IP alarms.

---

## ⭐ Best-fit title (very strong, very safe)

### **Project Pixel-Burn  
Legacy Burn-In System Replacement — Requirements Specification**

Why this works:
- “Project” → internal initiative
- “Legacy … Replacement” → clear business driver
- “Requirements Specification” → you’re defining *what*, not *how*
- No architectural commitment implied

This is exactly how serious internal replacement projects are titled.

---

## Other excellent options (slightly different tone)

### **Project Pixel-Burn  
Requirements for Replacement of the Legacy Burn-In System**

- Reads like a formal systems document
- Very hard to challenge

---

### **Project Pixel-Burn  
Problem Definition and Requirements for Legacy Burn-In Replacement**

- Slightly earlier-phase framing
- Useful if discovery is still ongoing

---

### **Project Pixel-Burn  
Operational Requirements for a Legacy Burn-In System Replacement**

- “Operational” keeps focus on use, not design
- Popular in test and manufacturing environments

---

## Titles I would avoid (given your goals)

- ❌ *System Architecture*  
- ❌ *Design Specification*  
- ❌ *Product Specification*  
- ❌ *Platform*

These all prematurely lock intent.

---

## Suggested subtitle (optional but powerful)

> *Defining functional and non-functional requirements to enable replacement of an end-of-life Pixel-Burn test system.*

This sentence does quiet, defensive work for you.

---

## How this positions you internally
This framing says:

> “We have an operational risk (EOL system).  
> This document defines what the replacement must do.  
> Architecture comes later.”

That’s **exactly** the right sequencing.

---

## My clear recommendation
If you want one **gold-standard** choice:

> **Project Pixel-Burn  
> Legacy Burn-In System Replacement — Requirements Specification**

If you want, next I can:
- rewrite your **Section 2 (Problem Background & Context)** specifically for “EOL risk”  
- help you draft a **one-paragraph executive summary**  
- or align this wording to your company’s existing document conventions

[M33] ME (2025-12-20 05:00):
So what did the document header. I may be able to fit all that in

[M34] AI (2025-12-20 05:00):
Good instinct — this is exactly what a **professional document header** is for:  
it carries the *context* so the title itself can stay clean.

Below is a **compact, realistic header layout** that would look completely at home in an engineering organisation and fits everything you’ve described.

---

## ✅ Recommended document header (clean & professional)

**Project:** Pixel-Burn  
**Document Title:** Legacy Burn-In System Replacement — Requirements Specification  
**Document Type:** System Requirements Specification (SRS)  
**Document ID:** PB-REQ-001  
**Version:** 0.1 (Draft)  
**Author:** Chris Simpson  
**Date:** 20 Dec 2025  
**Status:** Internal Draft  

---

### Optional subtitle (one line, highly effective)

*Defining functional and non-functional requirements to replace an end-of-life Pixel-Burn burn-in system.*

This line does a lot of quiet work.

---

## Why this header works
- **Project** carries the name (Pixel-Burn)  
- **Title** carries the intent (legacy replacement)  
- **Type** anchors it to standard practice  
- **ID / Version / Status** make it “real” and reviewable  
- **Author** gives ownership without ownership claims  

Nothing here implies:
- commercial sale
- side business
- architecture commitment

---

## Slightly more compact variant (if space is tight)

**Project Pixel-Burn — Legacy Burn-In System Replacement**  
**Requirements Specification (PB-REQ-001, v0.1, Internal Draft)**  

*Defining requirements to replace an end-of-life burn-in system.*

---

## What I would avoid in the header
- ❌ “Product”  
- ❌ “Platform”  
- ❌ “Architecture”  
- ❌ Company-external branding  

---

## Pro tip (this is senior-engineer polish)
Put this header:
- on the **cover page**
- repeated in the **header/footer** with:
  - Document ID
  - Version
  - Page X of Y

That alone makes it look established and controlled.

---

If you want next, I can:
- drop this header into your Word template exactly  
- create a **revision history table**  
- or align the wording to how your company normally labels documents

[M35] ME (2026-02-11 09:57):
Can y👌 u produce a professional
Guide to the requirements capture 

[M36] AI (2026-02-11 09:57):
Absolutely. I’ll give you something properly structured — the kind of guide you could actually use, or even circulate internally without embarrassment.

Below is a **Professional Guide to Requirements Capture**, written for engineering environments (test systems, hardware, mixed-signal projects like Pixel-Burn).

---

# Professional Guide to Requirements Capture  
*(For Engineering & Technical Systems Projects)*

---

## 1. Purpose of Requirements Capture

Requirements capture exists to answer three fundamental questions:

1. **What problem are we solving?**
2. **What must the solution do?**
3. **How will we know when it is acceptable?**

It is **not**:
- design work  
- architecture selection  
- solution selling  
- feature brainstorming  

It is structured clarification.

---

## 2. The Golden Sequence (Always Follow This Order)

Many engineers skip steps and go straight to design. Don’t.

### Step 1 — Define the Problem (Before Writing Any Requirements)

Capture:

- What system exists today?
- Why is it insufficient?
- What risks are emerging (e.g., end-of-life, obsolescence, maintenance burden)?
- What operational pain points exist?
- Who is affected?

This is the **anchor**. Without this, requirements drift.

---

### Step 2 — Define Scope and Boundaries

Clarify:

- What is included?
- What is explicitly excluded?
- What interfaces are fixed?
- What constraints are non-negotiable?

If scope is unclear, requirements multiply uncontrollably.

---

### Step 3 — Identify Stakeholders

List:
- Operators
- Maintainers
- Test engineers
- Manufacturing
- Quality / compliance
- Management

Each stakeholder typically introduces a class of requirements:
- usability
- maintainability
- reliability
- compliance

---

### Step 4 — Capture High-Level Capabilities

Before writing detailed “shall” statements, describe:

- What major capabilities the replacement must provide
- At system level (not implementation detail)

Example:
- The system must allow address-based channel selection.
- The system must support legacy burn-in operating modes.

Only once this is clear do you write formal requirements.

---

## 3. Writing Good Requirements

Every requirement should be:

- **Atomic** (one idea only)
- **Clear**
- **Unambiguous**
- **Verifiable**
- Written using **“shall”**

---

### Correct Structure

> The system shall [perform function] under [condition], within [constraint].

Example:

✔  
> The system shall capture an 8-bit binary address presented on inputs A0–A7.

✔  
> The system shall digitise the selected analog input within 50 ms of address capture.

---

### What to Avoid

❌ “The system should ideally…”  
❌ “The system will…”  
❌ “The system might…”  
❌ “The system shall be user-friendly.”  
❌ “The system shall be flexible.”  

If it cannot be tested or inspected, it is not a requirement.

---

## 4. Categories of Requirements

A professional specification separates requirement types.

---

### 4.1 Functional Requirements  
What the system must do.

Examples:
- Address handling
- Channel selection
- ADC acquisition
- DAC output
- Status indication

---

### 4.2 Performance Requirements  
How well it must do it.

Examples:
- Timing
- Resolution
- Throughput
- Accuracy

---

### 4.3 Interface Requirements  
How it connects to other systems.

Examples:
- Electrical interfaces
- Voltage levels
- SPI protocol
- Address bus timing

---

### 4.4 Non-Functional Requirements  
Quality attributes.

Examples:
- Field replaceability
- Maintainability
- Reliability
- Environmental tolerance

---

### 4.5 Constraints  
External limits imposed on the system.

Examples:
- Must fit within existing rack footprint
- Must operate from existing power supply
- Must use replaceable MCU module

---

## 5. Capturing Requirements Properly (Practical Method)

Here’s a clean workflow you can actually use.

---

### Phase 1 — Elicit

Talk to stakeholders and ask:

- What currently fails?
- What is painful?
- What must not change?
- What would break operations?

Write everything down informally.

---

### Phase 2 — Structure

Group the notes into:

- Functional
- Performance
- Interface
- Non-functional

Remove duplicates.

---

### Phase 3 — Formalise

Convert each into a “shall” statement.

Assign IDs:

- FR-01
- PR-01
- NFR-01
- IF-01

---

### Phase 4 — Validate

Ask:

- Can this be tested?
- Is it solution-neutral?
- Does it accidentally prescribe architecture?
- Does it contradict anything else?

---

## 6. What Requirements Capture Is Not

It is not:

- A design document
- A procurement justification
- A commercial pitch
- A personal branding vehicle

It is a **clarity instrument**.

---

## 7. Common Mistakes in Engineering Teams

### 1. Writing design instead of requirement
“The system shall use an STM32 MCU.”

That is architecture.  
The requirement should state capability, not component.

---

### 2. Over-specifying prematurely
If speed is “slow”, don’t write:
“≤ 10 ms response time”  
unless justified.

Only specify what is necessary.

---

### 3. Mixing background and requirement
Narrative belongs in Sections 2–3.  
“Shall” belongs in Section 7.

---

### 4. No traceability
Each requirement should trace back to:
- Problem
- Risk
- Stakeholder need

---

## 8. Verification Planning (Often Forgotten)

For every requirement, decide:

- Test
- Inspection
- Analysis
- Demonstration

If you cannot verify it, reword it.

---

## 9. When to Stop Capturing Requirements

You are done when:

- The problem is clearly defined.
- The system boundaries are stable.
- All stakeholder concerns are represented.
- Requirements are testable.
- No design decisions are embedded.

At that point, architecture can begin.

---

## 10. Why This Matters (Strategically)

Strong requirements:

- Prevent architecture debates based on opinion.
- Reduce rework.
- Protect against scope creep.
- Provide defensible decisions.
- Enable clean handover.

Weak requirements:

- Create political arguments.
- Invite feature creep.
- Undermine credibility.
- Blur ownership.

---

## 11. Applied to Pixel-Burn (Brief Illustration)

For your case:

Problem:
- End-of-life burn-in system.
- Operational risk.
- Replacement required.

Requirements capture should define:
- What burn-in modes must exist.
- What channel addressing must support.
- What analog performance is required.
- What maintainability improvements are necessary.

It should **not** define:
- Which MCU.
- Which mux topology.
- Which PCB layout.
- Which supplier.

That comes later.

---

If you’d like, I can next:

- Turn this into a **formal Word guide** you can reuse internally  
- Create a **requirements capture checklist** (one-page printable)  
- Or tailor this specifically to the Pixel-Burn replacement project  

You’re thinking about this at exactly the right level, by the way.
