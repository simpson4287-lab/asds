# High slew-rate OP amps
Date (UTC): 2026-04-02 11:33
Conversation ID: 69ce540c-8c44-8389-8f13-aadbf9fd7558
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-02 11:33):
Are there any OP parts with good slew?

[M2] AI (2026-04-02 11:33):
I’m checking a few current high-slew op-amp families so I can give you parts that are actually worth looking at, not just generic names.

[M3] AI (2026-04-02 11:34):
I’ve got a decent spread now: one ultra-fast small-signal part, one heavy-drive high-voltage part, and one strong older workhorse. I’m adding one or two practical alternatives so the list is more useful.

[M4] AI (2026-04-02 11:34):
Yes — quite a few, but the good ones are usually **current-feedback** or **power/high-speed video amps**, not ordinary general-purpose voltage-feedback op-amps.

A few solid examples:

- **THS3491** — about **8000 V/µs**, high-power, wide supply range, strong output drive. Very serious part if you need large swing and speed. citeturn168834search3turn168834search7
- **THS3091** — about **6000 V/µs**, ±5 V to ±16 V supplies, around **±310 mA** output drive. Good when you want fast edges with decent muscle. citeturn194587search2turn194587search5
- **AD8009** — about **5500 V/µs**, extremely fast small-signal amp, around **1 GHz** class. More of a pulse / RF-ish gain block than a “normal op-amp.” citeturn168834search0turn168834search4
- **OPA695** — about **5000 V/µs**, high-speed current-feedback amp, useful for instrumentation / gain stages / digitiser front ends. citeturn194587search1turn194587search4
- **ADA4870** — about **2500 V/µs**, but importantly it can deliver **1 A output current** from a **40 V supply**, so it is very relevant when the load is harder to drive. citeturn168834search1turn168834search9
- **AD811** — also **>2500 V/µs**, older but still a very respectable high-speed workhorse. citeturn168834search2turn168834search6
- **AD8001** — slower than the above at about **1200 V/µs**, but still fast and often easier to live with in practical circuits. citeturn194587search0turn194587search3

For your sort of use, the real split is:

- **Need raw slew only / very fast small signals:** AD8009, OPA695
- **Need fast slew plus stronger output drive:** THS3091, THS3491
- **Need fast slew at higher voltage / heavier load:** ADA4870
- **Need something familiar and proven:** AD811

The catch is that these parts are often **touchy on layout, gain setting, feedback values, supply decoupling, and capacitive load**. A “faster” op-amp can easily look worse on the bench if the surrounding network is not right. TI also notes that current-feedback amplifier slew behaviour is not simply a gain-setting issue in the same way people often assume. citeturn194587search14

For your CCD-clock / pulse-shaping direction, I’d say the first parts worth comparing are:
**AD811 vs OPA695 vs THS3091 vs ADA4870**.

If the goal is specifically **taking something like a 12 ns input edge and preserving or sharpening it into a higher-voltage stage**, **THS3091** and **OPA695** are the most interesting adds to your current shortlist, while **ADA4870** stays attractive when load drive matters more than headline slew. citeturn194587search1turn194587search2turn168834search1

Tell me your **supply voltage, target output swing, and load/capacitance**, and I’ll narrow it to the 2 or 3 best candidates.
