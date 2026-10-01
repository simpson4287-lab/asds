# Voltage at Load Current at Source
Date (UTC): 2026-06-23 15:46
Conversation ID: 6a3aaa2d-d164-83eb-985c-34ecf69a2dd1
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-008.json

[M1] ME (2026-06-23 15:46):
Is it acceptable to measure voltage at the load and current at the course of system constraints restrict you? I guess it’s more important to measure the volts at the load?

[M2] AI (2026-06-23 15:46):
Yes — **it is generally acceptable to measure voltage at the load and current at the source**, provided you understand what each measurement is actually telling you.

The usual priority is:

**Voltage: measure at the load.**  
That tells you the voltage the equipment actually receives, after cable drop, connector resistance, fuses, switches, relays, etc. This is normally the most meaningful voltage measurement.

**Current: measuring at the source is usually fine** *if the source feed only supplies that load*.  
In a simple two-wire supply feeding one load, the current leaving the source is the same current entering the load, so measuring current at the PSU/source side is valid.

Where it can become misleading:

- If there are **multiple loads/branches** after the current measurement point, you measure total system current, not just that load.
- If there is **leakage, grounding, chassis return paths, shielding current, or parallel return paths**, source current may not equal load current exactly.
- If the load has **local capacitors**, source current may show charging/inrush behaviour that differs from the instantaneous current used inside the load.
- If the wiring is long, voltage at the source can look fine while the load voltage is low due to cable drop.

For debugging, a good setup is:

```text
PSU/source ─── current measurement ─── cable ─── load
                                      │        │
                              voltage measured at load terminals
```

So yes: **voltage at the load, current at the source** is often the best compromise when access or system constraints limit you.

For power into the load, use:

```text
Pload ≈ Vload × Isource
```

That is a good approximation when the source current only feeds that load. If there are other branches, you need the current in the specific branch feeding the load.
