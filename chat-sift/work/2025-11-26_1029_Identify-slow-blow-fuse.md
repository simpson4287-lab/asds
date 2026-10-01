# Identify slow-blow fuse
Date (UTC): 2025-11-26 10:29
Conversation ID: 6926d695-1764-832f-9e4d-2dfd659e0008
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-001.json

[M1] ME (2025-11-26 10:29):
How to identify a slow blow fuse

[M2] AI (2025-11-26 10:29):
You can identify a **slow-blow fuse** in a few reliable ways. Here’s the quick engineer’s checklist:

---

# ✅ Ways to Identify a Slow-Blow Fuse

## 1. **Markings on the fuse**
Manufacturers almost always mark them.

Look for letters such as:

### ● Slow-blow markings
- **T** (most common – stands for Time-lag)
- **S**
- **SB** (Slow-Blow)
- **MDL / MDQ** on glass fuses (common Bussmann types)
- **FUSE-TR** / **Time Delay** on panel fuses

### Examples:
- **T3.15A** = 3.15-amp slow blow
- **T250mA** = 250-mA slow blow

### Fast-blow markings (for comparison)
- **F** or **FF** = fast or super-fast

---

## 2. **The look of the element**
If it’s a glass fuse:

### Slow-blow:
- Thicker wire inside
- Often coiled wire
- Sometimes a spring inside
- Sometimes looks like a blob or soldered part

### Fast-blow:
- Very thin straight wire

---

## 3. **Packaging or datasheet**
If it's in a holder or PCB:
- Often printed as **T** on the PCB silk
- Part numbers usually tell you:
  - Example: **Littelfuse 021701.6MXP** = slow-blow

---

## 4. **Typical uses (good indicator)**
Slow-blow fuses are normally found where inrush current happens:
- switching power supplies
- transformers
- motors
- audio amplifiers
- relay coils

If your circuit has an inrush surge (capacitors, motors etc.) then the fuse is **very likely slow-blow**.

---

## 5. Can you tell electrically?
Sort of, but it’s destructive:
- A fast-blow pops instantly on slight surge
- A slow-blow tolerates a short overload

But visually + markings are usually enough.

---

# ❗ Tip you’ll find really useful:
If the fuse body is ceramic (not see-through), markings are the only guaranteed way. Ceramic slow-blows are very common in mains circuits.

---

# If you want, take a photo
I can identify it for you quickly:
- Tell me any markings
- or show a picture

I’ll confirm exactly what type it is and whether it’s compatible with your circuit.
