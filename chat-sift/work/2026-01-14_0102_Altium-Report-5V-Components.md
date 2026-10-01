# Altium Report +5V Components
Date (UTC): 2026-01-14 01:02
Conversation ID: 6966eb04-e96c-8328-b4f8-066db6be2d7e
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-004.json

[M1] ME (2026-01-14 01:02):
Can altium designer run a report that tells
You every component on a supply rail like +5v for example 

[M2] AI (2026-01-14 01:02):
Yes. **entity["company","Altium Designer","pcb design software"]** can absolutely tell you *every component connected to a given supply rail* like **+5V**—and it can do it in a few different ways, depending on whether you want a quick answer or a formal report.

Think of this as asking the schematic a very simple but powerful question: *“Who is drinking from this rail?”* ⚡

---

### The cleanest, engineer-approved way: **Query-based reports**

Altium’s schematic engine understands nets as first-class citizens, so you can query against them.

You can generate a **Component Report** filtered by net connectivity:

- Use a query like:  
  **`HasNet('+5V')`**

This returns *all components with at least one pin connected to +5V*.

From there you can:
- Output it as a **report file**
- Export to **CSV / Excel**
- Sort by designator, footprint, value, etc.

This is the closest thing to a “truth table of power consumption topology.”

---

### Interactive, fast, and visual: **Highlight Net + Selection**

If you want to *see* it rather than list it:

1. Click on the **+5V** net label.
2. Use **Highlight Net**.
3. Then use **Select → All Highlighted Objects**.
4. Open the **SCH Inspector** or **Panels → Components**.

Instant population count. No ceremony. Very satisfying.

This is especially good during design reviews when someone says  
“Wait—*what else is on that rail?*”  
and you want to answer in under five seconds.

---

### Formal documentation style: **Electrical Rules / Netlists**

You can also:
- Generate a **netlist** and post-process it
- Or use **ActiveBOM** to correlate rails with components (especially useful if you later tie this to power budgeting)

ActiveBOM won’t *filter by net directly* in one click, but once you know the component set, it’s excellent for answering the *next* question:
> “Okay, now what does this rail actually cost me in current and risk?”

---

### Subtle but important caveat (this is where designs lie to you)

If your +5V rail is carried through:
- **Power ports**
- **Harness connectors**
- **Net ties**
- **Hierarchical sheets**

Then your answer depends on:
- Correct net naming
- No accidental aliases (`+5V`, `+5VA`, `+5V_A`, etc.)
- Proper sheet symbol wiring

Garbage net discipline = garbage report. Physics is unforgiving, but also fair.

---

### Engineer’s mental model

What you’re really doing is building a *power domain census*.  
Once you have it, you can layer on:
- rail isolation checks
- startup sequencing sanity
- current surge estimation
- “what breaks if this rail sags?” analysis

The report is the easy part. The insight comes from what you do with it.
