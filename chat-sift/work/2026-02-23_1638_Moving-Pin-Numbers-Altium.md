# Moving Pin Numbers Altium
Date (UTC): 2026-02-23 16:38
Conversation ID: 699c8289-1bec-8396-86ff-19d5a930a1ec
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-02-23 16:38):
[image]
Why can’t I move these PIN numbers in altium 
[attached file: IMG_0F5F7CE4-E847-43A0-87D8-C74B2F97CE68.jpeg]

[M2] AI (2026-02-23 16:39):
Because in Altium the **pin number isn’t a separate “text object” you can drag around**. It’s the **Pin Designator** that’s *owned by the pin*, so it only moves when you change the **pin’s designator/name position/offset** (or the pin itself).

### Do this in the **SchLib** (symbol) editor
1. **Click the actual pin** (the black stub), not the component background.  
   - If you’re accidentally selecting the component, use **View ▸ Panels ▸ Selection Filter** and tick **Pins** only.
2. With the pin selected, look in **Properties** for **Pin** settings (not “Component”).
3. Adjust one (names vary slightly by version):
   - **Designator / Number ▸ Position** (Inside/Outside/Top/Bottom/Left/Right)
   - **Designator / Number ▸ X/Y Offset** (or “Location”)
   - **Pin Length** (often fixes “number floating miles away” issues)
4. Repeat or multi-select pins and change the same field once to apply to all.

### If it’s still refusing to move
- Check the pin (or component) **Locked** flag in Properties and **untick Locked**.
- Make sure you’re not in a read-only/managed state (less likely in a local SchLib, but if it’s from a managed component/workspace item you may need to “Edit” it in the right context).

If you tell me whether you’re editing a **SchLib** symbol or a **schematic placed component**, I’ll give the exact click-path for that case (they’re slightly different).
