# Find Component by Designator
Date (UTC): 2026-01-21 15:20
Conversation ID: 6970eec1-5288-8331-a8c3-9cba58cc0668
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-004.json

[M1] ME (2026-01-21 15:20):
What’s the easiest way to find a component by designator in altium desigber 

[M2] AI (2026-01-21 15:20):
Altium hides this in plain sight, like a smug little goblin guarding a lever you actually need.

The **fastest, least-ceremony way** to find a component by designator in **Altium Designer** is this:

### The one you want (muscle-memory friendly)
Press **`Ctrl + F`** → type the **designator** (for example `R68` or `U12`) → press **Enter**.

Altium will jump straight to it and highlight it. No panels, no rituals.

### If you want it *locked-on* and obvious
Open the **PCB panel** (bottom-right by default), set the dropdown to **Components**, then type the designator in the filter box. Double-click the result and the view snaps to it. This is slower, but excellent when you’re dealing with stacked misery or dense BGAs.

### Cross-probing sanity trick
If you’re in the **schematic**:
- Click the component
- Hit **`Ctrl + Alt + Click`** (or just `Ctrl`-click if cross-probing is enabled)

The PCB zooms to the exact part like it’s been summoned.

### When Altium “finds” it but you still can’t see it
Two common gotchas:
- The component is on a **hidden layer** (check View Configuration → Layers).
- It’s inside a **room / variant / assembly view** filter.

Clear filters with **`Shift + C`** if things feel haunted.

Once this is in your fingers, you’ll never scroll a PCB like a lost Victorian explorer again.
