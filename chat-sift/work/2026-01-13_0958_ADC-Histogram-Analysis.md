# ADC Histogram Analysis
Date (UTC): 2026-01-13 09:58
Conversation ID: 6966171b-2f2c-832b-868d-713cfac5fc52
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-004.json

[M1] ME (2026-01-13 09:58):
See here from the histogram spread. Left is the 64 counts when it should be like the right 

[M2] AI (2026-01-13 09:58):
Got it — that histogram tells a very specific, very nerdy story, and it’s a familiar one.

image_group{"query":["ADC histogram missing codes","ADC histogram every 64 codes","ADC histogram decimation artifact","ADC histogram quantization error"]}

On the **left**, the ADC output is only landing on **every 64th code**. On the **right**, you have the healthy case: contiguous codes populated, noise doing its honest work, entropy everywhere it should be.

This is not “noise got worse” or “gain is wrong.” This is **bit-level starvation**.

### What the histogram is actually saying
If an N-bit ADC only ever produces codes spaced by 64, that means:

- 64 = 2⁶  
- You have effectively **lost the bottom 6 bits**
- Your ADC is behaving like **(N − 6) bits**, with the LSBs stuck at zero or ignored

So instead of:
```
xxxx xxxx xxxx
```
you’re getting:
```
xxxx xxxx 000000
```

The histogram doesn’t lie. It never does.

### The usual culprits (in descending order of likelihood)

**1. Digital truncation or bit misalignment**
- Bits [5:0] dropped in FPGA logic
- AXI / LVDS / JESD lane alignment off
- Wrong bit slicing after deserialization
- Signed/unsigned conversion done before scaling

This is *by far* the most common cause.

**2. Decimation or downsampling without dithering**
- CIC / FIR decimator with an output shift of 6 bits
- Averaging 64 samples and discarding the remainder
- “Optimization” that quietly murdered your LSBs

If the decimation factor is 64, the symptom matches *perfectly*.

**3. Test mode or reduced-resolution mode enabled**
Some ADCs have:
- 8-bit / 10-bit / 12-bit modes
- Fast mode that internally drops LSBs

If the ADC is configured for a lower effective resolution but still padded to full width, you’ll see exactly this.

**4. Input signal is quantized upstream**
Less common, but possible:
- DAC feeding the ADC is only 6 bits effective
- Pattern generator or gain-cal block stepping in 64-LSB chunks

Easy to rule out by probing analog noise directly at the ADC pin.

### Why the right-hand histogram looks “correct”
The right side shows:
- Code-to-code continuity
- Noise spreading energy across adjacent bins
- No regular spacing

That means:
- LSBs are alive
- Thermal + quantization noise is being preserved
- Digital path is correctly aligned

Noise is not the enemy here — it’s your witness.

### How to prove the root cause in minutes
Do these in order:

1. **Force DC input + inject analog noise**
   - If histogram *still* has 64-LSB spacing → digital problem
2. **Right-shift your captured word by 6 bits**
   - If histogram suddenly looks normal → you dropped bits earlier
3. **Check exact bit mapping from ADC → FPGA register**
   - One off-by-6 error will do this
4. **Disable all decimation / averaging**
   - Raw samples only, no “helpful” processing

### The key insight
This failure mode is **binary-clean**. That regular spacing means the system is behaving *exactly as instructed* — just not as intended.

When histograms become picket fences, the crime scene is digital.

If you want, we can walk the signal path end-to-end and mark exactly where the 6 bits vanish — ADC config register, JESD lane, FPGA slice, or post-processing.

[M3] ME (2026-01-13 10:00):
[image]
[attached file: 0015911E-440C-471F-8C37-23CDADCDBDD8.jpeg]

[M4] AI (2026-01-13 10:00):
Right — seeing the actual capture locks this down. That image is textbook.

Let me describe what the eye should notice, because it matters more than any register dump.

Top histogram (the “bad” one):
You’ve got a comb. Tall, evenly spaced bars. Big empty gaps between them. The bars are razor-thin and land at perfectly periodic code values. That periodicity is exactly **64 codes**.

Bottom histogram (the “good” one):
It’s a fat, continuous mound. Adjacent bins are populated. Noise is smearing energy sideways. No regular spacing. This is what a living ADC looks like.

Now the key point:

This is not an analog problem.

If this were:
• bandwidth limiting  
• sample clock jitter  
• front-end gain  
• reference noise  

you would still see **adjacent codes being hit**. You’d get a blur, not a picket fence.

What you are seeing in the top plot means:

> The digital word arriving at the histogrammer has its bottom **6 bits effectively frozen at zero**.

That can only happen in a few very specific ways.

First, the smoking gun visible in your screenshot:
The *range* and *mean* look sane. The distribution width is sane. Only the **granularity** is wrong.

That means:
• MSBs are intact  
• scaling is intact  
• timing is intact  
• only resolution is broken

Which narrows it to **bit handling**, not sampling.

The most likely causes, in order, given this exact appearance:

1. Bit slicing / alignment error  
Somewhere between ADC output and histogram input, you are doing something equivalent to:
```
sample_out <= adc_data[13:6];
```
and then padding it back up.

This often happens accidentally when:
• deserialiser lane mapping is off by 6  
• a sign extension is applied after a shift  
• someone “normalised” the data path earlier

2. Decimation or accumulation with an implicit >>6  
If you average or accumulate 64 samples and then truncate instead of rounding, you *create* this pattern perfectly.

This includes:
• CIC filters
• boxcar averages
• “noise reduction” blocks
• calibration modes

The regularity in your histogram screams “power-of-two math happened here”.

3. ADC mode / test configuration  
Some ADCs will:
• output fewer effective bits in certain modes
• left-justify data in a wider word
• drop LSBs in high-speed or test modes

But the reason this is *less* likely is that your **good channel** exists. Same silicon, different behavior. That points upstream or downstream logic, not the converter core.

Here’s the fastest way to prove where the fault is:

Do one capture where you:
• take the raw ADC word
• before *any* processing
• and histogram **only bits [5:0]**

If those bits are always zero → digital path fault.
If those bits contain noise → you’re killing them later.

Second killer test:
Right-shift the bad channel by 6 bits *in software* and histogram it.
If it suddenly looks like the bottom plot, you’ve found the exact magnitude of the damage.

One final subtle but important clue from your image:
The bad histogram bars are tall and consistent in height.

That means the system is *deterministic*. No metastability, no marginal timing, no analog weirdness. The FPGA is doing exactly what it’s told. It’s just been told something slightly stupid.

This is one of those bugs where the hardware is innocent and the math is guilty.

If you want, next step is to walk the data path **stage by stage** (ADC → deserialiser → formatter → filter → histogram) and I’ll help you pinpoint the precise line of logic where the six bits fall off a cliff.

[M5] ME (2026-01-13 10:16):
So this is in so config of adc?

[M6] AI (2026-01-13 10:16):
It *could* be, but odds-on it’s **not the ADC itself** — it’s the **digital path / processing after it**.

That 64-code “comb” means the **bottom 6 bits are being zeroed or ignored** somewhere. An ADC mis-config that *can* cause that usually looks like “left-justified” data or a reduced-resolution mode, but with one channel behaving and another not, it screams “per-channel digital handling.”

Here’s how to tell in minutes:

### 1) Bypass everything and grab RAW samples
If you can tap the bus right at the ADC interface (before any decimation/filter/averaging/scaling), histogram that.
- **RAW looks comb-like** → could be ADC config *or* interface bit alignment.
- **RAW looks normal but later looks comb-like** → definitely your downstream logic.

### 2) Check for left-justified / right-justified formatting
Classic mistake: ADC outputs (say) 14-bit data left-justified in 16 bits:
- Bits [15:2] = data, bits [1:0] = 0
That would give steps of 4, not 64.
Steps of **64** implies a **6-bit shift** (or dropping 6 LSBs).

So ask: is anything doing `>> 6`, or selecting `[N:6]`?

### 3) Look for decimation/averaging factor = 64
If there’s a block that averages 64 samples and then truncates, you get exactly this.
Search your design for:
- “decim”, “cic”, “avg”, “accum”, “boxcar”
- shifts like `>> 6`
- parameters equal to 64

### 4) Quick “software sanity test”
Take a captured bad sample stream and do:
- `y = x >> 6`
Histogram `y`.
If that suddenly becomes “normal-looking,” you’ve basically proven you’re losing 6 LSBs somewhere.

### When it *is* ADC config
You’re looking for things like:
- reduced-resolution mode / power-saving mode
- digital output formatting (offset binary vs two’s complement won’t do this; justification can)
- per-channel digital downscalers / digital gain blocks (some ADCs have per-channel DDC/decimation)

But again: the *exact* factor of 64 is such a “FPGA shift/decimate” number that I’d hunt there first.

If you tell me the ADC part number (and how you’re interfacing it: parallel LVDS, JESD204B/C, etc.), I can point at the exact register fields that could plausibly cause a 6-bit loss — and the exact FPGA failure modes that mimic it.

[M7] ME (2026-01-13 10:17):
It’s common across two systems with know hardware correct 

[M8] AI (2026-01-13 10:17):
If it happens on **two separate systems that you trust hardware-wise**, that’s a huge hint: the *ADC silicon is probably fine*, and you’re looking at something that’s **common to both builds**:

- the **same FPGA image / RTL block**
- the **same ADC register init sequence**
- the **same capture / formatting software**
- the **same “mode” setting** (decimation/averaging, test path, debug packer, etc.)

And the symptom is still very “digital”: **bottom 6 bits gone**.

What that points to, most likely:

### 1) A shared processing step is shifting/truncating
Somewhere, there’s effectively a `>> 6`, a `[N:6]` slice, or an accumulator/decimator that’s dividing by 64 and truncating.

This could be:
- a decimation/averaging block enabled by default
- a “reduce noise” / “moving average” mode
- a “histogram input select” mux that’s grabbing the wrong bus
- a word packer that is dropping the lower byte/halfword lanes

### 2) A shared ADC init script is enabling a per-channel digital path
Some ADCs have per-channel digital downconversion/decimation or “HP/LP” paths. If the same register map is used across both systems, a single bitfield can quietly enable a /64 path.

### 3) Your histogram tool is being fed the wrong bits
This is sneaky and common: the plotted value isn’t the raw sample; it’s an internal bus that already had scaling applied. If the same GUI/firmware feeds that histogram on both systems, it’ll reproduce perfectly.

---

## The fastest “no guessing” proof
Pick the “bad” channel and do these two checks:

**A) Compute `x & 0x3F` (bottom 6 bits) across a chunk of samples**
- If it’s **always 0** → those 6 bits are zero *at the point you captured them* (formatting/alignment/truncation upstream of capture)
- If it varies but histogram still shows comb → your histogrammer is using a shifted/scaled version

**B) Compare `x` vs `(x >> 6) << 6`**
- If `x` equals that expression almost always, then the data really is quantized to 64-code steps.

These can be done in firmware, Python, whatever—super quick.

---

## Practical place to look first (because it’s common to both)
1. **FPGA block that writes to the histogram FIFO / memory**
   - verify the exact bit slice going into the histogram
2. **Any decimator/averager enable**
   - anything with factor=64, or a shift=6
3. **ADC init register dump**
   - dump all registers from a “good” vs “bad” condition and diff them
   - if there’s no difference, it’s almost certainly *not* ADC config

---

One extra nerdy clue: **“sampling every 64 counts”** is usually *not* a sample-rate issue at all — it’s **code-step quantization**. Your sample rate can be perfect while your *code resolution* is wrecked.

If you can tell me where the histogram input comes from (raw ADC stream, post-filter, post-cal, DMA buffer, etc.), I’ll tell you the single most likely block doing the murder.
