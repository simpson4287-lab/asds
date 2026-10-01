# Voltage Classification for Reset Restore
Date (UTC): 2026-02-14 21:58
Conversation ID: 6990efe1-fec8-838e-8bbf-c7178bf00ba3
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-02-14 21:58):
What voltage would a restore restore come under. We usually use OD, RD, OG, AMD, DD, OG, IG ETC

[M2] AI (2026-02-14 21:58):
In CCD clocking terminology, a **Reset Restore** level sits in the **output stage domain**, not the image clock domain.

Given your shorthand (OD, RD, OG, AMD, DD, IG, etc.), here’s how it maps structurally:

---

### Where “Reset Restore” Lives

A reset/restore pulse is used to:

- Reset the floating diffusion (FD)
- Restore the output node to a defined reference before charge transfer
- Establish the baseline for CDS (correlated double sampling)

That function is performed by the **reset transistor** in the output amplifier block.

So electrically it is:

> **RD domain (Reset Drain / Reset Drive domain)**

Not OD, not OG, not IG.

---

### Typical Voltage Classification

Depending on the device family, reset/restore typically sits:

- **High-level RD**: ~10–15 V (many full-frame and line-scan CCDs)
- **Lower-voltage CMOS-like CCD variants**: 5–8 V
- Sometimes slightly above OD (but referenced to OD bias)

So in your shorthand taxonomy:

| Signal | Domain | Nature |
|---------|--------|--------|
| Reset Restore | **RD** | Pulsed high-level clock |
| OD | Output Drain | DC bias |
| OG | Output Gate | DC bias |
| IG | Image Gate | Clock domain |
| AMD | Anti-bloom drain | Bias |
| DD | Dump Drain | Bias or pulse |

---

### Important Distinction

Be careful not to confuse:

- **RD (Reset Drive / Reset Drain)** → clocked pulse
- **OD (Output Drain)** → static bias
- **Restore level** → the *high* phase of RD

So "Restore" is not a new domain — it's the **high state of RD**.

---

### In Your Pixel-Burn Context

For fast CCD clocking (you mentioned 6 MHz earlier):

- Reset pulse edges must be clean
- Timing relative to charge transfer gate is critical
- Jitter on restore directly impacts noise floor

So it absolutely belongs in your **high-voltage clock domain**, not in static bias rails.

---

If you want, tell me:
- CCD type (line scan? frame transfer?)
- OD bias level
- Target pixel rate

And I’ll sanity-check expected RD amplitude and edge rate.
