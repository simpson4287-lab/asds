# Power Supply Compliance Query
Date (UTC): 2026-05-12 21:27
Conversation ID: 6a039b06-2814-838b-86cf-a205451cc7a9
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-05-12 21:27):
I’m getting resistance from a chief engineer saying we can’t supply a commercial pay tested power supply. No mains leads. Just siting in rack

[M2] AI (2026-05-12 21:27):
I’m treating “pay tested” as **PAT tested**. I’m checking the likely regulatory/safety basis for the chief engineer’s objection, because the answer hinges on whether this is being **supplied as part of your equipment** versus merely used in your own test setup.

[M3] AI (2026-05-12 21:28):
Yes — **I think the chief engineer is probably overstating it**, unless their objection is really about **how** it is being incorporated and documented.

A **commercial enclosed PSU**, already placed on the UK market with the appropriate conformity marking/documentation, can in principle be **supplied with your equipment**. The fact that it has **no mains lead supplied** and is simply **located in the rack** does **not** by itself make it unacceptable. What matters is whether the **overall supplied arrangement is safe, suitable, and correctly defined**. citeturn700436search1turn700436search15turn429088search23

## The key distinction

### What **PAT testing** does — and does not do
A PAT test is essentially a **condition/safety check on an individual appliance**. It is **not** a product conformity route, and it does **not** replace UKCA/CE-related product-supply duties or a proper integration assessment. HSE is explicit that PAT is not itself a blanket legal requirement; the underlying obligation is that electrical equipment is maintained safely. citeturn643186search0turn643186search5

So:

- **“It’s PAT tested, therefore we can supply it”** — weak argument.
- **“It’s a commercially compliant, enclosed, off-the-shelf PSU, suitable for the intended use, and we’ve assessed its integration into the rack”** — much stronger argument.

## Where the chief engineer may have a valid point

If your proposed arrangement is effectively:

> “We’ll buy a desktop / brick PSU, put it loose in the rack, and regard the mains side as not our problem because we don’t supply the IEC lead,”

then I can see why they are resisting.

That approach still leaves legitimate engineering/product-safety questions:

- **Is the PSU mechanically restrained**, or can it shift during transport?
- **Is its cooling/ventilation acceptable** inside the rack?
- **Is it being used within the manufacturer’s intended environment**?
- **Are the DC output leads properly routed and strain-relieved**?
- **Is output protection/fusing adequate** for your downstream wiring?
- **Does the overall rack/system EMC position remain defensible**?
- **Do your system instructions identify the PSU, ratings, mains lead requirement, and permitted replacement part?**

The manufacturer of the **overall supplied product** remains responsible for checking conformity of the product and its incorporated components; using compliant bought-in parts does not automatically make the complete supplied system compliant. citeturn700436search1turn700436search11turn700436search12

## But “we can’t supply one at all” sounds too strong

I would push back on that wording. A more accurate engineering/compliance position would be:

> **We can supply a commercial PSU, but it must be treated as a specified bought-in component/accessory within the delivered system, not waved through on the basis of PAT alone.**

In practice, I’d expect this to be defensible if you do something like:

1. Select a **reputable, fully enclosed, compliant PSU** with proper UK/EU market documentation.
2. Specify it explicitly in the BOM / build standard.
3. Provide a **secure rack retention method** if it travels with the unit.
4. Confirm **thermal suitability** in the rack.
5. Define the **mains inlet/lead position clearly** — e.g. “customer provides standard IEC C13 mains lead” where appropriate.
6. Include it within your **system-level hazard/risk and technical documentation**.
7. Do not present **PAT** as the compliance basis; at most, it is an incoming/pre-delivery inspection record.

## My read

Your chief engineer may be right to reject:

> **“Loose commercial PSU in rack, PAT tested, therefore acceptable.”**

But I do **not** think they are right if the claim is:

> **“A company may not supply an approved commercial mains PSU with rack equipment unless it designs its own internal power solution.”**

That would be an unnecessarily absolute interpretation.

A concise line you could use back to them:

> “I agree PAT alone is not a sufficient basis for supply. However, I don’t believe there is a blanket prohibition on providing a compliant commercial enclosed PSU as part of the delivered rack arrangement. The question is whether we specify, restrain, assess, and document it appropriately within the overall system.”



[M4] ME (2026-05-12 22:00):
Why is it that rf signals can go so long on single ended 

[M5] AI (2026-05-12 22:00):
Because **“single-ended” is not the real problem**. The real problem is usually **an uncontrolled return path**.

A long RF link is typically single-ended **through coax**, which is actually a very well-controlled two-conductor transmission line:

- **Inner conductor** carries the signal.
- **Outer shield** carries the return current.
- Their geometry is fixed, so the line has a controlled impedance, usually **50 Ω or 75 Ω**.
- The shield also keeps external fields out and internal fields in.

So although we call it **single-ended**, electrically it is still a **complete transmission system with a tightly coupled return path**.

## Why it can travel metres — or kilometres

### 1. The impedance is controlled
A coax cable has a known characteristic impedance. If the source and load are matched, the signal propagates cleanly with minimal reflections.

That is very different from running a single-ended logic signal down some arbitrary wire with its return wandering through chassis, ribbon cable ground, or PCB planes.

### 2. The return current knows exactly where to go
At RF, return current wants to flow as close as possible to the outgoing current. In coax, it flows on the **inside surface of the shield**, directly surrounding the centre conductor.

That gives:
- Low loop area
- Low radiation
- Low pickup
- Predictable behaviour

### 3. RF receivers often tolerate low absolute signal levels
A radio link may start with millivolts or microvolts and still be recovered because:
- The receiver is narrowband
- It uses filtering and gain
- It may only care about amplitude/phase/frequency content, not maintaining a pristine DC-referenced waveform

Whereas with digital or analogue video-like signals, you often care about **exact instantaneous voltage shape**, edge timing, baseline, settling, and wideband distortion.

### 4. RF is often AC-coupled and frequency-selective
A lot of long-distance RF transport is around a defined band. You can optimise the whole path for that band.

Your CCD/video monitoring case is harsher:
- You may care about **DC/baseline behaviour**
- You want **fast edges and broad bandwidth**
- You want accurate waveform shape, not just “signal energy arrived”

That makes the link much more sensitive.

---

## So why use differential at all?

Differential is very useful when the cable environment is messy:

- Twisted pair rather than coax
- Multiple grounds that may not be at exactly the same potential
- Strong common-mode noise
- Long cables between boxes
- No desire to dedicate a coax per signal

Differential signalling rejects **common-mode interference** and is less dependent on the two systems sharing a perfectly quiet reference.

But it is not automatically “better” than coax. A properly terminated coax link can be excellent.

## The punchline

> **RF single-ended links work over long distances because they are not “single wire plus hope.” They are controlled-impedance transmission lines with a dedicated, closely coupled return conductor.**

That is why:
- **Single-ended via coax** can be superb.
- **Single-ended via loose wire/ribbon/poor ground reference** can be dreadful.
- **Differential twisted pair** is often chosen when coax is impractical or when ground/common-mode noise is the bigger issue.

[M6] ME (2026-05-12 22:02):
What’s best for digital signals 

[M7] AI (2026-05-12 22:02):
For **digital signals leaving a PCB or travelling any meaningful distance**, **differential is usually best** — typically:

- **LVDS** for fast, point-to-point logic/data/clock links
- **RS-422 / RS-485** for slower, more robust links over longer or noisier cables

Single-ended digital is fine **on-board** or for **short, well-controlled connections**, but it becomes less attractive once you go into a cable.

## Why differential usually wins for digital

Digital receivers care about **threshold crossing and edge timing**. Any noise, ground bounce, ringing, or reference shift can create:

- False switching
- Timing jitter
- Reduced noise margin
- Data errors

A differential receiver looks at the **difference between two wires**, so common noise coupled onto both is largely rejected. It also avoids relying heavily on the remote end having exactly the same “0 V” reference. LVDS was specifically developed for high-speed transmission with low swing, low EMI, and good noise immunity over controlled 100 Ω differential media. citeturn901640search0turn901640search6turn901640search10

## Compared with single-ended coax

A **single-ended digital signal over coax** can work very well, especially for:

- One fast clock
- Trigger pulses
- Timing references
- Very clean point-to-point links

But the receiver still measures the signal **against its local ground**, so ground offset and shield current can matter. Differential is generally more forgiving in a real machine or rack environment. Analog Devices summarises the core weakness well: single-ended runs are more susceptible to external noise because the receiver cannot distinguish interference from intended signal. citeturn901640search1

## Practical rule of thumb

| Situation | Best default |
|---|---|
| PCB trace, short, same board | Single-ended CMOS/LVCMOS |
| Board-to-board over short connector/backplane | Depends on speed; often single-ended is fine if SI is controlled |
| Cable between assemblies | Differential |
| Fast clock/data through a noisy rack or chamber | Differential, usually LVDS |
| Very long, rugged, lower-speed control | RS-422 / RS-485 |
| One ultra-clean timing pulse on a dedicated cable | Coax can be excellent |

## For your kind of setup

For the sort of signals you’ve discussed before — **SPI/control lines over 1–2 m into a chamber or between rack modules** — I would strongly favour:

> **Convert to differential at the source, send over twisted pair or suitable cable, recover to logic at the destination.**

For example:

- **SPI SCLK, MOSI, CS, ENABLE** → differential line drivers/receivers
- Use **LVDS** if you need crisp edges and tens of MHz operation
- Use **RS-422-style drivers** if the speed is lower and robustness matters more than edge rate

TI explicitly frames LVDS as a way to translate a single-ended logic signal into a signalling form “more appropriate for communication over extended distances or in a noisy environment.” citeturn901640search9

## My concise answer

> **Digital inside a PCB: single-ended is normal.  
> Digital over cables: differential is usually the right answer.  
> Coax single-ended is excellent for certain dedicated high-integrity timing links, but differential is the better general-purpose cable strategy.**

[M8] ME (2026-05-12 23:26):
The chief engineer also said that B2B plays not part in it

[M9] AI (2026-05-12 23:27):
On the **core electrical safety / supply argument**, he is **largely right**:

> **Being B2B does not remove the need for the supplied electrical equipment to be compliant and safe.**

The **Electrical Equipment (Safety) Regulations 2016** apply to relevant electrical equipment placed on the GB market; they are **not limited to consumer/B2C sales**. Government guidance is framed around equipment “supplied in or into Great Britain,” and the duties sit with the economic operator placing it on the market. citeturn945384search0turn945384search8

So if his point is:

> “We cannot justify supplying a mains-powered PSU merely by saying it is B2B, not consumer,”

then **yes, that is correct**.

## But B2B is not irrelevant in every sense

I would not say “B2B plays no part in it” as a universal statement. **B2B can matter under some regimes**, for example:

- **WEEE classification/exemptions** can distinguish B2B from B2C, and certain R&D-only equipment available only B2B may be excluded. citeturn945384search1turn945384search18
- Some **consumer-specific product safety duties** are obviously aimed at products intended for consumers rather than professional users.

But for the issue you were discussing — **can we supply a commercial mains PSU as part of a rack system?** — **B2B is not the deciding factor**.

## The stronger, precise position

I’d frame it like this:

> **B2B does not exempt us from electrical product-safety obligations. However, that does not itself mean a commercially compliant external PSU cannot be supplied. The question is whether the overall rack delivery treats that PSU correctly as part of the supplied arrangement and whether the integration is suitably assessed and documented.**

That preserves both points:

1. **He’s right** that “B2B” is not a compliance get-out.
2. **You may still be right** that supplying the PSU is not automatically prohibited.

## My suspicion

It sounds like he may be blending two arguments:

- **Correct:** “B2B does not exempt us.”
- **Possibly overreaching:** “Therefore we cannot supply a commercial PAT-tested PSU sitting in the rack.”

Those are **not the same conclusion**. The first does not automatically prove the second.

[M10] ME (2026-05-13 04:29):
What’s the right pic card for storing data in ram? And then being able to read an “event” within the data over to a hard drive?

[M11] AI (2026-05-13 04:29):
I’m reading “pic card” as **PCIe card** — likely a high-speed acquisition or frame-grabber-style card with onboard RAM, where you continuously capture data, detect/mark an event, then offload the relevant pre/post-event window to disk.

[M12] ME (2026-05-13 04:29):
Pxi 

[M13] AI (2026-05-13 04:30):
You want a **PXI/PXIe high-speed digitiser — effectively a scope card — with deep onboard acquisition memory and hardware triggering**, not just a generic DAQ card.

The operating mode you’re describing is:

1. **Continuously acquire into onboard RAM** as a rolling/circular buffer.
2. **Detect or receive an “event” trigger**.
3. Preserve a defined **pre-trigger and post-trigger window** around that event.
4. **Read that captured record back across PXI/PXIe** to the controller.
5. **Write it to the system SSD/HDD** for later analysis.

That is exactly the behaviour offered by proper PXI digitiser cards with **onboard memory + reference trigger / pretrigger capture**. NI’s PXIe-5114 documentation describes the samples sitting in a **circular onboard buffer until a trigger arrives**, after which it captures the requested post-trigger data; pre/post record depth is limited by onboard memory. citeturn638299search1turn638299search5

## The right class of card

For your wording in a requirement or architecture note, I would call it:

> **PXI/PXIe high-speed digitiser card with deep onboard memory, hardware-triggered pre/post-event capture, and host transfer for persistent storage.**

Or more compactly:

> **PXIe transient capture digitiser / scope card.**

## Features to specify

I would look for these exact capabilities:

| Required feature | Why it matters |
|---|---|
| **Onboard acquisition RAM** | Holds live data at full sampling rate without relying on immediate disk bandwidth |
| **Circular/pretrigger buffer** | Lets you retrieve what happened *before* the event |
| **Hardware event trigger** | Freezes the relevant window deterministically |
| **Post-trigger capture** | Captures the aftermath of the event |
| **Multiple-record / segmented memory mode** | Lets repeated events be captured efficiently without full software intervention |
| **Host transfer to disk** | Offloads records into file storage after capture |

NI SMC-based digitiser families also support **multiple-record acquisition**, where successive triggered records are stored into onboard memory with hardware re-arming between events — useful if there may be more than one event before software drains the data. citeturn638299search13

## Important: RAM is on the digitiser; the hard drive is usually elsewhere

The clean architecture is usually:

> **Digitiser card onboard RAM → PXI/PXIe backplane → embedded controller / PC RAM → SSD or hard drive**

The PXI card itself normally handles **capture and temporary storage**, not the long-term file archive. Long-term retention is handled by the PXI controller’s storage, or by a dedicated PXI/PXIe storage/recording subsystem where data rates are extreme. NI describes PXI data-movement/storage products for very high-throughput systems, while dedicated recorder platforms such as Conduant Cobra combine PXIe, FPGA and high-speed RAM for ultra-high-rate sustained recording. citeturn638299search8turn638299search4

## If this is for the Rameses / OS observation function

Then yes: the requirement is not just “a PXI card that stores data.” It is much more specifically:

> **A PXI/PXIe digitiser with sufficient onboard capture memory to maintain a rolling acquisition of the OS waveform, then preserve and transfer the defined waveform interval associated with a software- or hardware-defined event.**

That wording makes the functional intent clear.

## My recommendation

For the CDR/system description, I would avoid naming a specific card too early unless one is already selected. State the capability as:

> “The digitiser shall provide deep onboard acquisition memory operating as a rolling buffer, permitting event-referenced capture of configurable pre-trigger and post-trigger waveform data. Following the event, the retained acquisition record shall be transferred to host storage for file-based analysis and traceability.”

That is the technically correct description of what you want.

[M14] ME (2026-05-13 04:30):
Signal running at 150khz. Need to capture  a short 2 second window upon request and then store it 

[M15] AI (2026-05-13 04:31):
Yes — for that job you **do not need an exotic high-throughput recorder**. You need a **PXI/PXIe scope/digitiser card with onboard acquisition RAM and triggered finite-record capture**.

For a **150 kHz signal** where you want to capture a **2 second window on demand**, the task is modest from a memory point of view.

## What the card needs to do

> **Acquire continuously or arm for capture, accept a software/hardware trigger, capture a 2 s record, hold it in onboard memory, then transfer it to the PXI controller and save to disk.**

NI PXI digitiser cards are explicitly designed around this pattern: acquisition data is written to **onboard circular memory**, with pre-/post-trigger samples limited by memory depth. citeturn290785search0turn290785search9

---

## Memory requirement — surprisingly small

The key choice is **sample rate**, not the 150 kHz signal frequency itself.

### Example capture sizes per channel

Assuming **16-bit stored samples**:

| Sample rate | Samples in 2 s | Memory per channel |
|---:|---:|---:|
| 1 MS/s | 2 million | ~4 MB |
| 2 MS/s | 4 million | ~8 MB |
| 5 MS/s | 10 million | ~20 MB |
| 10 MS/s | 20 million | ~40 MB |
| 20 MS/s | 40 million | ~80 MB |

So even a card with **32 MB/ch** can capture:
- **2 s at ~8 MS/s** per channel, or
- **2 s at ~4 MS/s** with comfortable margin if storing in a wider format.

Cards with **256 MB/ch** are vast overkill for this specific 2 s/150 kHz requirement, unless you want many channels or much higher sample rate. NI notes that many digitiser families provide onboard memory in the **8, 16, 32 or 256 MB per channel** range. citeturn290785search9

---

## Sensible sample rate

This depends on what “150 kHz signal” means in your context.

### If you only need to record the signal state / amplitude trend
A sample rate of around:

> **1–2 MS/s**

is probably enough.

### If you want a useful view of waveform shape, settling, noise, pixel structure, or transient detail
I would target:

> **5–10 MS/s minimum**

That gives:
- ~33–67 samples per 150 kHz period
- A much better record for later inspection
- Still only **20–40 MB per channel** for the 2 s window

For your kind of analogue/video observability work, I would be more comfortable specifying **at least 5 MS/s**, ideally **10 MS/s** if channel count and card cost permit.

---

## The “right” card category

I would specify:

> **PXI/PXIe oscilloscope or high-speed digitiser, ≥12-bit preferred, with triggered finite-record acquisition, onboard memory sufficient for a 2 s capture at the required sample rate, and software API support for transferring the record to host storage.**

### Very plausible NI-type fit
Something in the class of:

- **NI PXIe-5122** — 2 channels, 14-bit, up to 100 MS/s, data streaming support citeturn290785search5
- **NI PXI/PXIe-5124** class — higher memory variants exist, e.g. 256 MB/ch cited by distributors citeturn290785search16
- **PXIe-5114** / similar deep-memory digitiser family if already available in your ecosystem; NI’s memory/trigger behaviour aligns exactly with the use case. citeturn290785search0

You likely **do not need FlexRIO** or a dedicated recorder for this.

---

## How I would write the requirement

> **The PXI digitiser shall support event-initiated capture of a continuous analogue waveform record of not less than 2 s duration. The captured record shall be retained in onboard acquisition memory and subsequently transferred to host storage for persistent file-based retention. The acquisition sampling rate shall be sufficient to characterise the 150 kHz signal content and associated transient behaviour.**

If you want it firmer:

> **For a single monitored channel, the acquisition system shall support a 2 s capture duration at not less than 10 MS/s, with the resulting record transferred to host storage following completion of the capture.**

At **10 MS/s, 16-bit**, that is only about **40 MB per channel**, which is entirely reasonable.

## My recommendation

For your use case, I’d target:

> **2-channel, 12–14-bit PXIe digitiser, 10 MS/s or greater capture rate for the 2 s event window, with onboard memory of at least 64 MB/ch preferred.**

That gives plenty of engineering headroom without accidentally specifying a far more complex system than required.

[M16] ME (2026-05-13 04:32):
Input will be a digital signal . There are out to 30 channels in parallel doing the same 

[M17] AI (2026-05-13 04:32):
That changes the answer materially: you’re not after a scope/digitiser card at all. You want a **PXI/PXIe digital I/O / logic-capture card** that can sample **~30 parallel digital lines**, buffer a **2 s event window**, then transfer that captured block to host storage.

[M18] AI (2026-05-13 04:32):
Yes — with **up to 30 parallel digital channels at ~150 kHz**, captured for a **2 s requested window** and then saved to disk, the most natural fit is a:

> **32-channel PXIe digital I/O / pattern acquisition card**, not an analogue digitiser.

## My first-choice fit: **NI PXIe-6535**

I’d look first at the **NI PXIe-6535** class:

- **32 digital channels**
- **10 MHz maximum clock rate**
- **40 MB/s throughput**
- Intended for **pattern I/O, change detection, protocol-style acquisition, image-sensor/display-panel interfacing**
- Can stream acquired data over PXIe to host memory, then your software writes the 2 s record to disk. citeturn571292search0turn590409search9

For your use case, it looks very proportionate.

---

## Data volume is tiny

Your 30 channels would normally be captured as a **32-bit digital word per sample**.

### If sampled synchronously at 150 kHz
A 2 second window gives:

- **150,000 samples/s × 2 s = 300,000 samples**
- **300,000 × 4 bytes = ~1.2 MB**

That is negligible.

### Even if you oversample at 1 MHz
- **2,000,000 samples**
- **~8 MB total**

### Even at 10 MHz, the PXIe-6535 maximum
- **20,000,000 samples**
- **~80 MB total**

Still entirely manageable for host RAM and disk transfer. The PXIe-6535 is explicitly designed to stream data over PXI Express rather than hold the whole event in deep onboard RAM. citeturn571292search0turn590409search9

---

# The key architectural choice

## A. If “upon request” means:
> “Software or operator requests a capture; the system grabs the next 2 seconds and saves it.”

Then I would choose:

> **PXIe-6535, 32-channel digital input, finite triggered acquisition, DMA/streaming to host RAM, then disk save.**

That is probably the **right answer**.

The card has start/reference trigger support in its acquisition modes, and the captured block can be transferred to the controller buffer via DMA. citeturn571292search1turn571292search9

---

## B. If you instead mean:
> “The digital activity is already running continuously; when an event happens, I want to preserve the 2 s region around that event, perhaps including pre-trigger history.”

Then I would look instead at an **NI PXIe-6544 / 6545 / 6548 digital waveform instrument** with **deep onboard acquisition memory**.

These provide:

- **32 digital pins**
- **100 or 200 MHz digital acquisition**
- **Onboard acquisition RAM options up to 64 Mbit/channel, i.e. 256 MB total**
- Reference-trigger style acquisition, with pre- and post-trigger samples held in onboard memory before retrieval. citeturn736157search0turn736157search1turn736157search5

For example, at **10 MHz**, your 2 s / 32-bit capture is about **80 MB**, which fits comfortably within the **256 MB total acquisition memory** configuration. citeturn736157search0

---

# Which one would I choose for your description?

Based on:

> “Signal running at 150 kHz. Need to capture a short 2 second window upon request and then store it. Input will be a digital signal. There are up to 30 channels in parallel doing the same.”

I would specify:

> **PXIe-6535 or equivalent 32-channel hardware-timed digital I/O module, configured for finite 2 s triggered digital pattern acquisition, with transfer of the captured record to host storage.**

I would **not** jump to the PXIe-654x deep-memory digital waveform cards unless you specifically need:

- A **continuous circular pre-trigger buffer**
- Much higher timing resolution than your 150 kHz signal needs
- Precise event position relative to a fast free-running internal sampling clock
- More advanced digital test/instrument functionality

---

## One subtle but important point: use an external sample clock if available

If these 30 digital lines are meaningfully valid on a known **150 kHz clock/strobe**, the cleanest capture method is:

> **Sample the 30 channels on that clock edge**, rather than free-running at a much higher arbitrary rate.

That produces a far more compact, semantically clean record: **one 30-bit word per system tick**. The PXIe-6535 family supports externally clocked pattern acquisition via its sample-clock input structure. citeturn590409search0

---

## Requirement wording I’d use

> **The PXI digital acquisition subsystem shall capture up to 30 parallel digital input channels over a configurable 2 s acquisition window initiated on software or hardware request. The acquisition shall be hardware-timed and the resulting digital record shall be transferred to host storage for persistent retention and subsequent event analysis. Where available, acquisition shall be synchronised to the external system sample clock.**

And if you want the architectural selection made explicit:

> **A 32-channel PXIe digital I/O / pattern acquisition module, such as the NI PXIe-6535 class, is considered suitable for this function.**



[M19] ME (2026-05-13 04:34):
What if the signal was purely spi 

[M20] AI (2026-05-13 04:34):
If the data is **purely SPI**, the architecture becomes **much simpler**.

You no longer need a **30-channel parallel digital capture card**. You need to capture and store the **SPI transaction stream**:

- **SCLK**
- **MOSI or MISO** — whichever carries the data of interest
- **CS / frame strobe**
- Possibly one extra **event/request marker** if required

## Best-fit approach

For your requirement:

> **A 150 kHz data source, captured for a 2 s requested window, then saved to disk**

I would use either:

### 1. **PXI FPGA / RIO card implementing an SPI receiver** — best engineered solution
This is the cleanest if the capture function is part of a serious test system.

The FPGA:
- Listens to the SPI bus in real time
- Reconstructs the received words/frames
- Starts logging on command
- Captures **2 s of decoded SPI payload**
- Transfers the stored data to the PXI controller for disk writing

NI’s PXIe R Series / FPGA cards are specifically aimed at **custom protocol communication, precise timing, and onboard processing**, which is exactly this sort of job. Examples include the **PXIe-7820** and **PXIe-7858** families. citeturn622497search14turn622497search2turn622497search7

### 2. **PXIe digital I/O card capturing the raw SPI lines** — simpler procurement, more software work
A card such as the **PXIe-6535** could sample the SPI lines as digital waveforms, then software decodes the clock/data/chip-select relationship afterwards. It supports clocked digital acquisition and host streaming, and NI explicitly positions it for **protocol emulation/custom digital interfacing**. citeturn794966search2turn794966search6

That works, but it is less elegant if the data is already well-formed SPI and you only care about **the data values**, not the analogue edge timing of the SPI bus.

---

# My recommendation

I would recommend:

> **PXIe FPGA/RIO card with a simple SPI slave-receive/logger function.**

That is the right technical answer if this is an intentional system feature rather than a quick lab lash-up.

## Why that is preferable

Instead of storing raw sampled waveforms like:

> SCLK = 0/1, MOSI = 0/1, CS = 0/1 at every acquisition tick

you store meaningful decoded records like:

> Timestamp / frame index / 30-bit or 32-bit payload word

That gives you:
- Far smaller files
- Easier downstream event search
- Lower software processing burden
- Cleaner interpretation
- The option to trigger on **content**, not just time

---

## Data size is trivial

If the SPI payload represents the equivalent of your **30 digital channels** sampled at **150 kHz**, then assuming the payload is packed into a **32-bit word**:

- **150,000 frames/s**
- **2 s**
- **300,000 words**
- **4 bytes/word**
- Total ≈ **1.2 MB**

Even if you add timestamps or overhead, the data is still tiny.

---

## Important decision: capture **decoded SPI** or **raw SPI**

### Capture **decoded SPI** if:
- You trust the bus electrical integrity
- You care about the data content
- You want to find an event inside the 2 s data
- This is a repeatable system function

### Capture **raw SPI waveform** if:
- You need to prove the SPI timing itself
- You want to diagnose malformed transactions
- You suspect clock/data alignment, CS timing, or signal integrity problems

For your described purpose — **store data, then later read an event within it** — I would default to **decoded SPI capture**.

---

# A clean requirement statement

> **The PXI acquisition subsystem shall receive the digital measurement stream presented as SPI-formatted data, capture a configurable 2 s record on software or hardware request, and transfer the decoded record to host storage for subsequent analysis. The acquisition function shall preserve transaction framing and payload ordering sufficient to reconstruct the original time sequence of the measured data.**

If you want the implementation steer:

> **An FPGA-based PXIe acquisition module implementing SPI slave reception and finite-window data logging is considered the preferred architecture.**

## Bottom line

> **If the 30 channels are already serialized into SPI, do not buy a 32-channel digital waveform card merely to recapture them in parallel. Use a PXI FPGA/RIO card to receive and log the SPI stream directly.**

[M21] ME (2026-05-13 04:36):
If it is well formed can’t it just be stored as ram in pxi

[M22] AI (2026-05-13 04:36):
Yes. **If the SPI is already well formed and you only care about the payload data, the 2-second event record can simply be buffered in RAM within the PXI system, then written to disk.**

But one clarification matters:

> **PXI itself is not “RAM.”**  
> The RAM would be either:
> 1. **host RAM in the PXI embedded controller**, or  
> 2. **onboard memory on a PXI FPGA/interface card**.

## The cleanest architecture

For your case I’d envisage:

> **SPI stream → simple PXI SPI receiver/interface → DMA into PXI controller RAM → on request retain 2 s buffer → save to SSD/HDD**

At your data rates, this is very undemanding.

If the serialised SPI carries, say, the equivalent of **30 bits at 150 kHz**, you are in the ballpark of:

- **30 bits × 150,000/s = 4.5 Mbit/s**
- About **0.56 MB/s raw payload**
- A **2 s record = ~1.1 MB**, before any timestamps or packing overhead

That is tiny relative to normal PXI controller RAM capacities, which are typically in the **many GB** range. NI’s PXI embedded-controller RAM guidance shows modern controllers commonly supporting tens of GB of RAM. citeturn472958search1turn472958search5

## Do you need onboard RAM on the acquisition card?

**Probably not**, unless you need one of these:

- **Pre-trigger history** from a continuously running circular buffer that must be protected absolutely deterministically
- Very tight real-time guarantees independent of the host OS
- Capture during periods when the host could be briefly delayed
- Triggering on decoded SPI content inside the acquisition hardware

For a straightforward:

> “Command capture now, collect the next 2 seconds, store it”

then **streaming decoded SPI data straight into controller RAM is perfectly reasonable**. NI FPGA targets commonly use **DMA FIFOs** to move acquired data from the FPGA/interface hardware into host memory efficiently. citeturn472958search2turn472958search10turn472958search12

## What hardware is still required?

You still need **something to receive the SPI electrically and clock it into the PXI system**. The PXI controller will not normally accept raw SPI directly as a high-integrity acquisition stream.

That “something” could be:

- A **small PXI FPGA/RIO card** implementing an SPI receiver, or
- A **suitable digital interface card** if the application/software stack can use it cleanly

Given the stream is well formed, I would lean to a **modest FPGA-based PXI interface** rather than a high-spec digital waveform capture instrument.

## The most sensible functional description

I’d now describe the function as:

> **A PXI-based SPI data receiver shall ingest the serial measurement stream and transfer the decoded payload into controller RAM. Upon acquisition request, a 2 s record shall be retained and written to persistent host storage for subsequent analysis.**

If you want **pre-event history**, phrase it slightly differently:

> **The PXI acquisition function shall maintain a rolling RAM buffer of the decoded SPI stream and, upon event request, preserve a configurable 2 s data window for transfer to persistent storage.**

## Bottom line

> **Yes — for well-formed SPI at this rate, the “event data” can simply live in PXI controller RAM and then be saved to disk.**  
> You do **not** need a large dedicated deep-memory capture card unless you want deterministic pre-trigger capture or more advanced real-time trigger logic.

[M23] ME (2026-05-13 04:37):
Would the embedded controller pxi donit?

[M24] AI (2026-05-13 04:37):
**Not directly, no.**  

The **PXI embedded controller** can absolutely:

- hold the **2 s dataset in its RAM**
- write it to its **internal SSD/HDD**
- manage the capture request, file naming, analysis, etc.

But it generally **cannot receive raw SPI lines itself**. NI PXI embedded controllers are essentially rugged in-chassis PCs; their front-panel I/O is typically USB, Ethernet, serial, DisplayPort, triggers, and sometimes GPIB — **not a native SPI acquisition input**. citeturn932804search14turn932804search9

## What you need

You still need **one PXI/PXIe module to ingest the SPI**, for example:

> **SPI source → PXI digital/FPGA interface card → embedded controller RAM → disk**

The embedded controller then does the easy bit: buffering and storage.

## Could a very simple PXI digital I/O card do it?

**Potentially, yes**, if:
- the SPI is well behaved,
- data rate is modest,
- and the card/software can sample or reconstruct the SPI reliably.

But the most robust architecture is usually:

> **PXI FPGA/RIO or suitable digital protocol interface receives the SPI and passes decoded words to the embedded controller.**

## Why the controller alone is not the right ingestion point

Even though the actual data volume is tiny, the challenge is not memory. It is **real-time edge capture / SPI reception**:

- clocking on the correct SPI edge
- respecting chip-select framing
- guaranteeing no missed words
- handing a continuous data stream off deterministically

A Windows or RT embedded controller is not normally wired for that at logic-pin level. That is the job of an I/O or FPGA card.

## Best concise statement

> **The PXI embedded controller can provide the RAM buffer and hard-drive storage, but a PXI/PXIe acquisition or FPGA I/O module is still required to receive and decode the incoming SPI stream.**

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] AI (2026-05-13 04:29):
For what you describe, the right class of PXI card is a:

> **PXI/PXIe digitizer / oscilloscope card with deep onboard memory, hardware triggering, multi-record acquisition, and stream-to-disk support.**

Not just a generic DAQ card.

## The architecture you want

Something like this:

```text
Signal in
   ↓
PXI/PXIe digitizer
   ↓
Onboard acquisition RAM / circular buffer
   ↓
Trigger / event occurs
   ↓
Capture pre-trigger + post-trigger window
   ↓
Read selected record/event back over PXI/PXIe bus
   ↓
Controller writes it to SSD / hard drive
```

So the key words to search/specify are:

> **deep onboard memory**, **pre-trigger capture**, **post-trigger capture**, **multi-record acquisition**, **hardware trigger rearming**, **streaming to disk**, **segmented memory**.

## NI-style answer

An **NI PXI Oscilloscope / High-Speed Digitizer** is probably the most obvious route. NI describes its PXI oscilloscopes as having **advanced triggering**, **deep onboard memory**, and driver support for **data streaming and signal analysis**. citeturn162536search1

Older but still relevant NI digitizers such as the **PXI-5122 / PXI-5114 / PXI-5922** family explicitly support the sort of behaviour you are describing:

- acquire into onboard memory;
- use triggered / multi-record acquisition;
- capture pre-trigger and post-trigger records;
- stream from onboard memory to host memory or disk. citeturn162536search3turn162536search11turn162536search12

A good example phrase from the NI 5122-type behaviour is **multiple triggered waveforms without software intervention**, which is exactly what you want if the “event” happens faster than Windows/software can react. citeturn162536search11

## PXI or PXIe?

Prefer **PXIe** if this is new or if the data rate is high.

PXI Express uses the PCI Express backplane and is specifically aimed at higher-bandwidth jobs such as **high-speed digitizer streaming to disk**. citeturn162536search0

Plain PXI may still be fine for modest sample rates, but for serious continuous capture or fast digitizers, PXIe is the safer architectural choice.

## What I would specify

I would write the requirement like this:

> The acquisition module shall be a PXIe digitizer/oscilloscope module with onboard acquisition memory capable of circular or segmented acquisition, hardware trigger support, pre-trigger and post-trigger capture, and host transfer/stream-to-disk support. The module shall allow software to retrieve a defined event record from acquisition memory and write the selected data window to local SSD storage without requiring the full continuous capture to be retained.

That avoids saying “store in RAM and then hard drive” too loosely. The formal requirement is really **event-based acquisition with pre/post-trigger record retrieval**.

## Important distinction

There are two different modes:

### 1. Triggered event capture — usually what you want

The card holds data in onboard RAM. When a trigger occurs, it preserves a window around the event.

Best for:

- glitches;
- pulses;
- CCD/video events;
- fault capture;
- rare events;
- waveform inspection.

### 2. Continuous streaming to disk

The card continuously pushes data over the PXI/PXIe bus to the controller and SSD.

Best for:

- long recordings;
- lower sample rate capture;
- data logging;
- when you genuinely need the whole stream.

For very high sample rates, you often cannot stream everything forever unless the PXIe bus, controller, RAID/SSD, and file format are designed for it. That is why onboard memory plus triggered records is usually cleaner.

## Card types to look at

| Use case | Card type |
|---|---|
| Analogue waveform, video, CCD output, transient capture | **PXIe oscilloscope / high-speed digitizer** |
| Digital logic state capture | **PXI/PXIe digital waveform / logic analyser card** |
| Slow sensor logging | **PXI DAQ card** |
| Very fast RF / IF capture | **PXIe wideband digitizer / vector signal analyser** |
| Custom event detection before storing | **FPGA-based PXIe digitizer** |

For your likely case — waveform capture and later reading an event — I would not start with a normal multifunction DAQ. I would start with a **PXIe oscilloscope/digitizer**.

## Practical recommendation

For an NI ecosystem, look at:

- **NI PXIe oscilloscope / digitizer modules**
- NI-SCOPE driver support
- onboard memory depth
- maximum sample rate at your required channel count
- segmented/multi-record acquisition
- pre-trigger/post-trigger capability
- stream-to-disk examples
- controller SSD write bandwidth

For a more custom or high-performance route, also look at **Spectrum Instrumentation** or **Keysight PXIe digitizers**. Some Spectrum cards explicitly support modes like continuous FIFO streaming and event/trigger-related acquisition modes, including storing trigger positions/timestamps. citeturn162536search13 Keysight’s M9203A PXIe digitizer is an example of a high-speed PXIe digitizer family with continuous streaming-to-disk capability. citeturn162536search16

## The simple answer

You want:

> **A PXIe digitizer/oscilloscope card with deep onboard memory and hardware-triggered segmented acquisition.**

Not merely:

> “A PXI card with RAM.”

The event capture is the important feature.
