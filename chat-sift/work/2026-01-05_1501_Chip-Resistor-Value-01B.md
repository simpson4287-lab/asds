# Chip Resistor Value 01B
Date (UTC): 2026-01-05 15:01
Conversation ID: 695bd24d-9f54-832c-8144-0d292c091b41
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-003.json

[M1] ME (2026-01-05 15:01):
What value is chip resistor 01b

[M2] AI (2026-01-05 15:01):
A chip resistor marked **“01B”** is using a **three-character alphanumeric marking**, most commonly found on **precision / thin-film SMD resistors** rather than standard thick-film parts.

### How to interpret **01B**
This follows an **E96-style coding scheme**:

- **“01”** → Base value index in the E96 series  
  - Index **01** corresponds to **100**
- **“B”** → Multiplier  
  - **B = ×10**

### Calculation
100 × 10 = **1,000 Ω**

### Final value
**01B = 1 kΩ**  
Typically **1% tolerance** (sometimes 0.5% or better, depending on series).

### Notes
- Standard low-cost SMD resistors usually use:
  - **3-digit numeric** codes (e.g. 102 = 1 kΩ)
  - **4-digit numeric** codes for 1%
- **Alphanumeric codes** like *01B* are characteristic of **precision thin-film resistors**, often used in:
  - Analog front ends
  - Measurement circuits
  - Gain-setting networks

If you want, you can tell me:
- The **package size** (0402, 0603, etc.)
- The **manufacturer or board context**

and I can confirm the exact series and tolerance.
