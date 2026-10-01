# ADC Output Sampling Issue
Date (UTC): 2026-01-13 09:57
Conversation ID: 696616ed-7a30-832b-8fba-5e6f5e42b76d
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-004.json

[M1] ME (2026-01-13 09:57):
[image]
I have this adc bit an issue with the outputs. One of the outputs is reduced in its sampling rate. It only samples every 64 counts
[attached file: DCB90AB9-96A3-440B-B113-0192F7FC868E.jpeg]

[M2] AI (2026-01-13 09:58):
That “every 64 counts” symptom has a *very* common, very sneaky explanation:

### The boring-but-likely truth: you’re looking at a higher-order bit, not a slower sampler
If your ADC data is a **ramp** (either from a test pattern, or a slowly changing analogue input that your digital chain turns into a count-up), then **each bit toggles at a power-of-two rate**:

- Bit 0 (LSB) toggles every 1 count  
- Bit 1 toggles every 2 counts  
- Bit 2 toggles every 4 counts  
- …  
- **Bit 6 toggles every 64 counts**  
- Bit 7 toggles every 128 counts  
- etc.

So if you probe **one LVDS pair / one logic line** that corresponds (directly or after your FPGA mapping) to **bit 6**, it will *look* like it “only updates every 64 samples”, even though the ADC is sampling every clock.

This fits your wording *exactly*.

### How to prove it in 2 minutes
1. **Force a test pattern** in the AD9978 (or your ADC) that toggles *every sample*, e.g.:
   - `0xAAAA` / `0x5555` (checkerboard)
   - or “alternating” pattern if the part supports it  
   If that “slow” lane suddenly toggles fast → it wasn’t slow, it was just a higher bit.

2. **Look at the data clock / strobe** (DCO / DCLK_OUT / frame marker if present).  
   That’s the true sample cadence. Data bits can be “quiet” for long stretches depending on value.

3. In your FPGA, temporarily **reconstruct the full word** and check whether the *word* increments every sample (even if one constituent bit doesn’t).

### If it’s *not* that (less likely), the real “/64” causes to check
If you truly get *repeated samples* (word held constant for 64 sample clocks), then it’s usually one of these:

- **FPGA clock-enable / decimation accidentally set to /64** (a counter gating your capture enable)
- **Deserializer word-alignment mistake** where you’re only latching one word per 64 bit-clocks
- **You’re probing a “word boundary / sync” signal** (some AFEs can output markers that pulse at a programmable interval)

### Quick sanity check thought
If the “problem output” is *the only one* doing /64, ask: is it also the only one that corresponds to a specific **bit position** in your mapping? If yes → it’s almost certainly the “bit 6 toggles every 64” effect.

If you tell me what stimulus you’re feeding (test ramp? real video? constant input?) and **which exact AD9978 output pair** you’re watching (DOUTxP/N?), I can pin it down to “bit significance” vs “capture/formatting bug” with pretty high confidence.
