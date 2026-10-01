# Negative Feedback Resistors x5
Date (UTC): 2026-03-12 09:50
Conversation ID: 69b28c75-4360-8395-9b8d-1dd93440a462
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-12 09:50):
What’s the best negative feedback resistors for a x5 gain 

[M2] AI (2026-03-12 09:50):
For an **x5 gain**:

- **Non-inverting op-amp:**  
  Gain = 1 + (Rf / Rg)  
  So you want **Rf / Rg = 4**

Good practical pairs are:

- **10k / 40k**
- **2.49k / 10k** for near-exact standard values
- **1k / 4k**
- **4.99k / 20k** if you want tighter E96 values

A very solid default is:

- **Rg = 2.49k**
- **Rf = 10k**

That gives:

- Gain = 1 + 10k / 2.49k = **about 5.02**

If you want it simpler:

- **Rg = 10k**
- **Rf = 40k**
- Gain = **exactly 5** if 40k is available in your series

General rule for “best” choice:
- Stay roughly in the **1k to 20k** region for most op-amp feedback networks
- Too low wastes current
- Too high increases noise and sensitivity to input bias current/parasitics

So for most circuits, I’d pick:

- **2.49k and 10k** for a compact, robust choice
- **10k and 40k** for a nice easy-value choice

If this is actually an **inverting** stage, then it is just:

- Gain = **Rf / Rin = 5**
- Example: **10k in, 50k feedback**

If you want, I can pick the best exact pair for your specific op-amp and bandwidth.

[M3] ME (2026-03-12 09:51):
Separate circuit. Talking like 27r and 120r

[M4] AI (2026-03-12 09:51):
Got you — you mean keeping the **same ratio**, but using **low-value resistors** like **27 Ω** and **120 Ω**.

For a **non-inverting gain of x5**:

\[
Gain = 1 + \frac{R_f}{R_g}
\]

So you need:

\[
\frac{R_f}{R_g} = 4
\]

With your sort of values, a good fit is:

- **30 Ω and 120 Ω** → exactly **x5**
- **27 Ω and 110 Ω** → about **x5.07**
- **33 Ω and 130 Ω** → about **x4.94**

So the neatest answer is:

- **Rg = 30 Ω**
- **Rf = 120 Ω**

But in practice, that is **very low** for an op-amp feedback network.

Why that can be a problem:
- it loads the op-amp output harder
- wastes current
- can reduce output swing capability
- may stress small high-speed amps for no benefit

Example with 30 Ω / 120 Ω:
- total path is very low impedance
- at just **1 V** across the network, current is already several mA

Usually, unless there is a specific RF/high-speed/stability reason, you would scale that up by 10x or 100x:

- **300 Ω / 1.2 kΩ**
- **3 kΩ / 12 kΩ**

Those are much more normal.

So:

- **Best exact low-value pair:** **30 Ω and 120 Ω**
- **Closest to your example:** **27 Ω and 110 Ω**
- **Best practical general choice:** **300 Ω and 1.2 kΩ** or **3 kΩ and 12 kΩ**

If this is for a particular op-amp stage, tell me the device and whether it is **inverting or non-inverting**, because with very low feedback values the op-amp choice starts to matter quite a lot.

[M5] ME (2026-03-12 14:46):
Can you have two symbols that represent the same sheet to keep the block diagram tidier?

[M6] AI (2026-03-12 14:46):
Yes — **you can have multiple sheet symbols pointing to the same child sheet**. In Altium that is a normal way to represent repeated channels, and the official docs explicitly describe “multiple sheet symbols that reference the same child sheet” as one valid multi-channel method. citeturn375380search6turn375380search11

The important bit is this:

- If you place **two separate sheet symbols** that both reference the same `.SchDoc`, Altium generally treats that as **two instances/channels** of that sheet, not just two visual aliases. citeturn375380search6turn375380search11
- For plain hierarchical connectivity, the connection is through the **sheet symbol entries** on the parent and matching **ports** on the child sheet. citeturn375380search8turn375380search12

So for your question, the answer is:

- **Yes, physically you can do it**
- **No, it is usually not a good idea if you only want a tidier block diagram view of one and the same functional block**

Why not:
- You may accidentally create what Altium interprets as **repeated channels**
- That can affect **annotation, compilation, channel naming, and PCB synchronization**
- It can become confusing because both symbols look like “the same block” to you, but to Altium they are often **separate hierarchical instances**

Better options:
- Use **one real sheet symbol** and keep the rest as **graphics/text notes** for clarity
- Or make a dedicated **top-level overview sheet** that is just a non-electrical block diagram
- Or, if you actually want repeated instances, use Altium’s intended multichannel methods such as **multiple sheet symbols referencing the same child sheet** or the **Repeat(...)** keyword on a sheet symbol designator. citeturn375380search1turn375380search6

Practical rule:
- **Same child sheet shown twice for appearance only:** avoid it
- **Same child sheet instantiated twice as two real channels:** fine

For your current design, if you want, I can tell you the **safest tidy way** to show one block in two places on the parent sheet without confusing the compiler.

[M7] ME (2026-03-12 16:36):
My previous multichannel attempt imported the channels directly into rooms. Why is it not doing this anymore?

[M8] AI (2026-03-12 16:36):
Most likely, it has stopped because Altium is no longer seeing that section as a **true multi-channel instance**, or the **class/room generation options** are no longer enabled in the project.

In Altium, PCB rooms for repeated channels are typically created **when the design is transferred from schematic to PCB**, and that depends on the project’s **Class Generation** and **Multi-Channel** settings. Altium’s docs say rooms can be generated automatically for multi-channel sheets, with **a room for each sheet symbol/channel**. citeturn354623search4turn354623search11turn354623search14

The usual reasons it works once and then stops are these:

1. **It is no longer a real multichannel structure**
   - Altium only treats it as multi-channel if you either:
     - use **multiple sheet symbols pointing to the same child sheet**, or
     - use a **single sheet symbol with `Repeat(...)`**. citeturn354623search6turn354623search10
   - If you copied sheets, broke links, changed references, or turned part of it into ordinary hierarchy/reuse blocks, it may compile as normal hierarchy instead of repeated channels.

2. **Project Options → Class Generation changed**
   - Altium’s own material says you need **Component Classes** and **Generate Rooms** enabled for the multichannel sheets, otherwise the ECO will not generate the rooms. citeturn354623search4turn354623search5turn354623search8

3. **The ECO is not including room/class creation**
   - Even if the schematic is right, the PCB update must include the **creation/synchronization of classes and rooms**. Altium explicitly notes those can be generated during **Design » Update PCB**. citeturn354623search8turn354623search11

4. **Component links/UIDs got disturbed**
   - In multi-channel designs, PCB UIDs are derived from the **parent sheet symbol + schematic component UID**. If you have done manual linking, imported blocks, or mixed designs, the PCB may no longer recognise the channel instances the same way. citeturn354623search6

5. **Rooms may exist but not as expected**
   - Altium’s current room documentation notes that rooms depend on inherited member components and their component classes; if a room no longer inherits the expected members, it may not behave the same way. citeturn354623search0turn354623search1turn354623search2

So the practical check sequence is:

- Confirm the repeated block is still made by **one child sheet referenced multiple times** or by **`Repeat(...)`**
- Open **Project Options**
  - **Class Generation**: make sure channel component classes / room generation are enabled
  - **Multi-Channel**: make sure the channel naming/settings are still valid for the repeated sheet structure citeturn354623search4turn354623search5turn354623search10turn354623search13
- Recompile the project
- Run **Design » Update PCB**
- In the ECO, check whether it is actually proposing:
  - **component classes**
  - **rooms**
- If not, Altium is not recognising the design as multichannel at compile time

Based on what you described before, the **most likely cause** is this: your earlier attempt was a **true multichannel sheet-symbol structure**, but the current design has drifted into a **copied/imported hierarchy with manual linking**, so Altium no longer sees those channels as generated channel instances, and therefore it does not auto-create the rooms. That fits the way Altium defines multichannel behaviour and room generation. citeturn354623search6turn354623search14

A good litmus test is simple:

- If the compiler produces **channelised designators / channel instances**, it is still multichannel.
- If it just sees ordinary sheets/components, it will not generate the same channel rooms.

If you show me your **Project Options tabs** for **Class Generation** and **Multi-Channel**, plus the **sheet symbol designator/reference setup**, I can tell you exactly which part has stopped Altium treating it as true multichannel.
