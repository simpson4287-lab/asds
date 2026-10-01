# Power Net Component Report
Date (UTC): 2026-03-25 15:44
Conversation ID: 69c402bc-1174-8388-9049-d0a3e2eaa4ea
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-25 15:44):
Can altium run a report to tell you all the components touching a power net?

[M2] AI (2026-03-25 15:44):
Yes — not as a single nicely named “show me everything touching this power net” report, but you can get it a few ways.

Best methods in Altium:

**1. PCB panel / Nets**
If you want **all physical copper-connected components** on a power net:
- Open the **PCB editor**
- Open **Panels**
- Choose **PCB**
- Switch the panel mode to **Nets**
- Select the power net, for example `+5V`, `3V3`, `AVDD`

That will highlight the whole net on the board, and you can inspect every pad/via/track on it. Good visually, but not a clean export by itself.

**2. Schematic cross probe / compiled design**
If you want **all schematic components with pins on that net**:
- In the schematic, use **Project > Compile**
- Then use **Panels > Navigator** or **SCH List**
- Search/filter by the net name

You can often filter objects by net, then see which component pins belong to it.

**3. Generate a net report**
You can produce a report that includes net connectivity:
- In PCB editor go to **Reports**
- Look for **Netlist**, **Net Status**, or **Board Information** style reports depending on version
- Some report outputs list each net and the pads/components attached

This is usually the closest thing to a formal report.

**4. Query-based selection**
A very useful way:
- Use **Find Similar Objects** on a pad belonging to that net, or
- Use a **PCB Filter** query

Typical idea:
```text
InNet('3V3')
```

That selects all objects on the net. Then you can refine to pads/components. For components specifically, a common workflow is:
- select pads on the net
- then use **Tools / Reports / selection-based commands** or inspect associated components

**5. From the schematic BOM/netlist side**
If your real goal is:
“Which components have at least one pin connected to this rail?”
then the schematic/netlist route is better than PCB copper inspection.

You want a **compiled netlist** view, because that reflects logical connectivity, not just placed copper.

Practical answer:
- **Yes, Altium can tell you**
- **No, it is not usually one single one-click ‘power net component report’**
- The cleanest route is usually:
  - **compile project**
  - inspect **net connectivity**
  - optionally export a **netlist/net report**

If you want, I can give you the exact quickest workflow for either:
**schematic side** “which components are on 3V3?”
or
**PCB side** “which placed parts physically touch 3V3 copper?”
