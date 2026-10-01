# Schematic Part Alignment Issue
Date (UTC): 2026-04-02 04:14
Conversation ID: 69cded03-5460-8391-843a-b5573edde1f3
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-02 04:14):
[image]
Why all of a sudden are parts broken?
[attached file: IMG_79FBE29D-45B1-428D-80F2-766913A391DF.jpeg]

[M2] AI (2026-04-02 04:14):
That usually means the **schematic items have gone off-grid or been moved without preserving wire connection points**.

From your photo, the capacitor body is there, but the **top pin is no longer meeting the wire above**, so Altium is drawing it like the part is “broken” when really the **pin end and wire end no longer coincide**.

Most likely causes:

1. **Grid changed**
   - Very common if it has suddenly affected lots of parts.
   - Example: symbols placed on 100 mil grid, then you switch to metric or a finer grid and move things slightly.

2. **Moved with the wrong command**
   - If a part gets moved in a way that does not drag connected wires properly, the wires can stay behind.

3. **Library pin positions or symbol got edited**
   - Less likely if many existing parts suddenly look wrong.
   - More likely if it is only one custom part.

What to check first:

- In the schematic, set the grid back to a normal value like **100mil** or **50mil**.
- Turn **Snap** on.
- Click the part and see whether the **pin ends land on the wire ends**.
- Try nudging the component back onto grid.
- Use **Tools / Align / Align to Grid** if needed.
- Delete and redraw one affected wire segment to see if it snaps correctly to the pin.

A quick test:
- Place a brand new capacitor from the library nearby.
- If the new one connects normally, the old placed item or wires are off-grid.
- If the new one also looks broken, your **grid/snap settings** are the likely culprit.

The image strongly suggests **off-grid connection**, not an actually corrupted part.

Tell me whether this is happening to **all symbols** or just this sheet, and I’ll narrow it down fast.
