# Key sight n6743b current
Date (UTC): 2025-12-15 10:28
Conversation ID: 693fe26b-e2d4-8330-9070-2692f20469cd
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-002.json

[M1] ME (2025-12-15 10:28):
Can a key sight n6743b run at higher than 5 A

[M2] AI (2025-12-15 10:28):
No — the **entity["turn0product0","Keysight N6743B",1]** (often sold as a module for the Keysight N6700 system or as the bench unit variant **entity["turn0product2","Keysight Technologies Bench Power Supply",0]**) is **rated for a maximum of 5 A** output. Its official specifications list:

- **Output voltage:** up to 20 V DC  
- **Maximum output current:** **5 A**  
- **Maximum power:** 100 W  

Those limits are set by the internal design (power semiconductor, heat dissipation, and protection circuitry) and the module’s safety/current-limit settings. citeturn0search0

Because the manufacturer specifies **5 A max**, you cannot reliably draw more than that (e.g., 6 A or higher) without exceeding the device’s specifications. Attempting to do so would either:

- trigger the module’s over-current protection and shut down the output, **or**
- potentially overheat/damage the unit if protections fail.

So **you should not run it above 5 A** — doing so is outside the specified operating range and risks reliability or safety issues. citeturn0search0

If you need higher current than 5 A, you’d want a different module in the N6700/N6705 family with a higher current rating (e.g., 10 A or 15 A variants) or a separate power supply rated for your required current. citeturn0search6

[M3] ME (2025-12-15 10:34):
Negative 

[M4] AI (2025-12-15 10:34):
Got it — let’s reset and be precise 👍  

**Short answer:**  
**No, an N6743B cannot source more than 5 A from a single output.**  
If you think it can, the *only* ways that might look true are edge-cases or configuration misunderstandings.

---

## What the N6743B actually is
**Keysight N6743B DC Power Module**
- **20 V max**
- **5 A max**
- **100 W max**
- Linear / high-performance module (not a high-current brute)

Those three limits are *hard limits* enforced by hardware and protection.

---

## Common reasons this gets confusing (and why they don’t apply)

### 1. **Parallel outputs**
If you parallel **two N6743B modules**, you can get **~10 A total**, **but**:
- Each module is still capped at **5 A**
- Current sharing must be configured correctly
- This is **not** one module running above 5 A

✔ Valid system-level solution  
✘ Not a single-module capability

---

### 2. **Constant-power misunderstanding**
Some supplies allow higher current at lower voltage *within power limits*.  
The N6743B **does not** exceed 5 A even at low voltage.

Example:
- 5 V × 5 A = 25 W → still capped at 5 A
- You **do not** get 10 A just because you’re under 100 W

---

### 3. **Transient / peak current**
The N6743B is **not** a pulsed or peak-current supply.
- No sanctioned “burst above 5 A”
- Over-current protection will trip very fast

---

### 4. **Sense lead or measurement illusion**
Sometimes people *see* >5 A on:
- An external meter
- A load transient
- A wiring fault or inductive kick

That does **not** mean the supply is sourcing it continuously or safely.

---

## If you need >5 A (cleanly)
Within the N6700 ecosystem, look at:
- **10 V / 10 A modules**  
- **Higher-power SMU or switching modules**
- **Parallel-capable higher-current supplies**

If you want, tell me:
- Required **voltage**
- Required **current**
- Whether this is **analog / low-noise** (which I suspect, given your past work)

…and I’ll point you to the *correct* Keysight module or a better alternative.

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] ME (2025-12-15 10:34):
Is there a way to share currents. I have two
Modules powering plus and minus 7.5v. The narrative uses hardly anything 
