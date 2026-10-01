# Telephone wire vs twisted pair
Date (UTC): 2026-06-04 10:55
Conversation ID: 6a215976-7378-83eb-b7f8-3e5c4f0080ad
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-06-04 10:55):
I’ve used some telephone wire as differential cable. It was 4 core but not worsted. Labelled telephone wire. The cores were super tight together. Is this better than some twisted pairs 

[M2] AI (2026-06-04 10:55):
It **can be better than random loose wires**, but it is usually **not better than proper twisted pair** for a differential signal.

The key point is not just “cores close together”; it is whether the **two conductors of each differential pair stay close together with consistent geometry** along the whole cable.

For differential signalling, the best order is usually:

**Proper twisted pair cable**  
Best for controlled coupling, noise rejection, consistent impedance, low loop area.

**Telephone cable with all cores tightly bundled but not twisted into pairs**  
Often acceptable for low-speed or forgiving signals, especially over short runs, because the cores are close together. But the pair geometry changes along the cable, so impedance and noise pickup are less controlled.

**Loose multicore / random hookup wire**  
Worst, because the loop area can be large and inconsistent.

Where telephone cable can actually do okay is with **slow-ish differential standards** like RS-422/RS-485 over modest distances, especially if the signal edges are not too fast. But for **LVDS, clocks, fast digital edges, SPI-ish fast logic, or anything where signal integrity matters**, I would strongly prefer proper twisted pair, ideally screened twisted pair or CAT5/CAT6.

A subtle issue with untwisted 4-core telephone wire is that each conductor may couple slightly differently to external noise. With a twisted pair, both wires repeatedly swap physical position, so external interference tends to affect both conductors equally. That is what helps the receiver reject it as common-mode noise. In a tight but untwisted 4-core, one core might sit consistently nearer a noisy cable or ground reference, so the noise can become **differential**, which the receiver cannot reject as well.

Also, if you used two adjacent cores for `+` and `-`, that is better than using opposite/far-apart cores. If the four cores are arranged like a square, pair adjacent conductors rather than diagonal ones.

For your kind of setup, I’d put it like this:

For **temporary bench use, short distance, low frequency**: probably fine.

For **20–30 m cable runs**: I would not trust plain telephone wire unless the signalling is slow and robust.

For **RS-422/RS-485 at modest rates**: likely workable, but use proper twisted pair if available.

For **LVDS / clocks / precise timing / radiation test harnesses**: use proper twisted pair, preferably known impedance cable.

The “super tight together” part is good because it reduces loop area, but it doesn’t fully replace twisting. Twisting gives you **symmetry along the length**, not just closeness.
