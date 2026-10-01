# Symbol Meaning in Altium
Date (UTC): 2026-02-27 21:16
Conversation ID: 69a209b8-4224-8388-869c-ec24c5615797
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-02-27 21:16):
[image]
[attached file: IMG_8FDD1328-8A62-44BD-9D97-43117C9A765A.jpeg]

[M2] ME (2026-02-27 21:16):
What does the little symbol mean

[M3] AI (2026-02-27 21:18):
That little **square “button” icon next to IC6** is the **Locate / Zoom-to-object** control.

- Click it and Altium will **pan/zoom the PCB editor to that component** (and usually select/highlight it), so you can quickly find it on the board.

If you actually meant the **yellow triangle icons** on the right: those are **warnings** that the source/target items **don’t match cleanly** (e.g., footprint / parameters / design item mapping), so replication may be partial until the mismatch is resolved.

[M4] ME (2026-02-27 21:23):
[image]
They be all worked partially with the placement. Now the rooms is still not happy 
[attached file: IMG_D812BAA1-CA49-48ED-BC86-0E25A6BD5443.jpeg]

[M5] AI (2026-02-27 21:23):
Yep — that dialog is the key:

**“18 Channel-Offset Errors Found” = Altium can’t line up the *net/channel mapping* between the source room and the target room(s), so it can’t safely replicate routed nets.**  
Placement can “mostly work” because footprints/designators match, but routing replication depends on the **channel offsets** being consistent.

### What causes “Sequence Errors” / “Failed Offset Matches”
Common causes in multi-channel / rooms workflows:

1. **Different designator sequences between rooms**  
   e.g. Source has `R23,R24,R25…` but target has `R34,R36,R38…` (or missing parts / extra parts).

2. **Room contents not identical**  
   Any extra/missing component, different footprint, or different variant fitted/not-fitted breaks the offset solve.

3. **Nets differ between channels**  
   If the copied block has net names that aren’t channelized the same way (or were renamed after), Altium can’t map them.

4. **Room definition not coming from the same PCB snippet / schematic channel instance**  
   If one room was created manually or via a different snippet instance, the “channel identity” isn’t consistent.

---

## Fastest way to get it working (practical sequence)

### A) If you want **routing replicated**
1. **Make sure both rooms come from the same “pattern”**
   - Ideally: both placed from the same **PCB Snippet / Reuse block** (or at least identical component set).

2. In PCB, open **PCB Layout Replication**
   - **Untick** “Copy routed nets” for one test run.
   - Replicate **placement only** and confirm you get *zero* offset errors.
   - If you still get offset errors even with routing off, your room/component mapping is inconsistent.

3. Fix the mapping:
   - Ensure the **target room has the same components** as the source room (same footprints).
   - Make the **designators align by channel** (see note below).

4. Then re-run with **Copy routed nets** enabled.

### B) If you only need placement copied (and will route manually)
- In PCB Layout Replication:
  - ✅ Copy Designator & Comment formatting (fine)
  - ❌ Copy routed nets (disable)
  - ✅ Copy unrouted objects (optional, depends if you want tracks from un-routed primitives)
This avoids the channel-offset solver entirely.

---

## The designator/channel alignment bit (the thing that usually fixes it)
For routed replication to work reliably, each room needs the *same logical component list* in the same order **within the channel**.

**Best practice:**
- Get the schematic multi-channel to generate consistent per-channel designators (or at least stable Unique IDs).
- Push an ECO so PCB rooms are re-instantiated correctly.
- Don’t manually “swap” or delete items inside one room unless you do the same to all.

---

## Quick check you can do right now
In your screenshot, the two rooms clearly have **different designators** (IC1/J1 vs IC8/J8, resistors are different numbers). That’s normal — **but** the *set* must match 1:1.

So: in the replication panel, expand the warnings and see **which components are flagged** (it’ll list mismatched pairs). Those are the ones breaking the offset.

---

If you paste a screenshot of the **expanded error list** in the PCB Layout Replication panel (the rows with warning triangles), I can tell you exactly which mismatch is causing the offset failure and the quickest correction (rename, re-room, re-snippet, or re-ECO).

[M6] ME (2026-02-27 21:27):
Can you remember a component selection?

[M7] ME (2026-02-27 21:27):
Renumber

[M8] AI (2026-02-27 21:27):
Yes — in Altium you can “remember” a selection in a couple of solid ways, and then **renumber** just that set.

## Remember a component selection (so you can reselect it later)

### Option A (best for components): **Component Class**
1. Select the components.
2. **Design → Classes…**
3. Under **Component Classes**, click **Add**, then **Add Selected** (wording varies slightly by version).
4. Name it e.g. `ROOM1_SET`.

Later you can reselect via **PCB Panel → Components → Classes** (or use it in rules/queries).

### Option B (quick + flexible): **Union**
1. Select the objects (components + tracks + anything).
2. **Tools → Component Placement → Create Union from Selected Objects** *(or right-click → Unions → Create Union, depending on UI)*.
3. Name the union.

Later: open **PCB Panel → Unions**, click it to reselect.

*(If you only need components, Class is usually cleaner.)*

---

## Renumber (renumber just the selection / class)

### In the PCB editor
1. Select the components you want renumbered (or select the class/union).
2. **Tools → Renumber Components…**
3. In the dialog:
   - **Scope**: choose **Selected Components** (or equivalent).
   - Set **Start number** (e.g. 1 or 23).
   - Set **Increment** (usually 1).
   - Choose ordering (e.g. **Left-to-Right, Top-to-Bottom**).
4. Apply/OK.

**Tip:** If this design is multi-channel/rooms based and you want replication to behave, try to keep numbering consistent per channel (same “pattern” per room), otherwise mapping/routing replication gets cranky.

If you tell me whether you want **room 2 to match room 1’s numbering pattern** (offset style), or you just want “nice sequential numbers by position,” I’ll give you the exact safest settings to pick in that Renumber dialog.

[M9] ME (2026-02-27 21:32):
[image]
Why has this one got lots of x in it
[attached file: IMG_83EE4F22-1042-4923-8545-18971CBE3653.jpeg]

[M10] AI (2026-02-27 21:32):
Those **lots of little green/red “X” marks** are Altium showing that the **pads/vias in that area are “unconnected / not matching their net” (or are being flagged by a display mode)** — it’s essentially a **connectivity marker overlay**, not “damage” to the footprint.

In practice, you usually see that pattern for one of these reasons:

### 1) You’ve got a **polygon pour / plane** there that’s **not repoured** or is **on the wrong net**
- Typical after room replication / ECO changes.
- Fix: **Tools → Polygon Pours → Repour All** (or right-click polygon → Repour).

### 2) Those pads are in a **BGA/DFN footprint**, but the **ratlines are hidden** and Altium is showing **unrouted connections** as “X” markers
- If this one room didn’t copy routing cleanly, you’ll see a “bed of X’s” on the un-routed pad connections.

### 3) **Net assignment mismatch** (most common in multi-channel replication issues)
- The footprint pads are still on e.g. `NetC82/NetC23` but the replicated channel expects different nets, so Altium marks a ton of “this copper doesn’t belong here / not connected”.

### 4) It’s a **DRC/Violated rule display** mode
- Some view configs show violations as X’s across pads/tracks.

---

## Quick way to identify exactly what it is (30 seconds)
1. **Click one of the X-marked pads/vias**.
2. Look at the **Properties** panel:
   - **Net:** what net is it on?
   - Any message like **Un-Routed Net**, **Violation**, **Unconnected**?
3. Then run:
   - **Tools → Design Rule Check** (or open the **PCB Rules and Violations** panel) and see what category lights up.

## Fast “likely fix” given your room/replication situation
Do these in order:
1. **Repour all polygons** (Repour All).
2. **Recompile + ECO update** from schematic (so nets are re-associated correctly).
3. If still there: open **PCB Panel → Nets**, highlight the net for one of those pads and see if it belongs to that channel.

If you send a close-up showing the **Properties panel for one of those pads** (net name + any violation text), I can tell you precisely which of the four it is and the exact corrective clicks.

[M11] ME (2026-02-27 22:07):
Could a schematic being off grid cause issue with rooms

[M12] AI (2026-02-27 22:07):
Off-grid schematic objects **won’t directly break Rooms** in the way you’re seeing. Rooms/replication problems almost always come from **connectivity + channel identity + component identity**, not whether a wire end is sitting exactly on a grid point.

That said, an “off-grid” schematic **can indirectly cause room pain** if it leads to any of these:

## When off-grid *can* cause issues
1. **Wires not actually connected**
   - Visually touching but not electrically connected (wire ends/junctions not snapped).
   - Result: nets get split/renamed, ERC warnings, and the PCB ends up with different netlists per channel → rooms can’t map routing (“channel-offset” errors).

2. **Net labels / ports not truly attached**
   - A net label or port placed near a wire but not snapped onto it.
   - Result: that channel gets `NetCxx` auto-nets instead of the intended named net → replication mismatch.

3. **Harness connectors / sheet entries / ports misaligned**
   - Similar “looks connected” issue.
   - Result: different connectivity between channels.

## What *doesn’t* matter much
- A resistor symbol slightly off grid
- Text/comments off grid
- Even the physical placement of the channel circuitry on the schematic page

## Quick sanity checks (worth doing once)
- In the schematic: **Project → Validate / Compile**
  - Look for **“Net has no driver”, “Unconnected pin”, “Net label not connected”** type messages.
- Turn on **View → Connections** (ratsnest) and make sure nets behave as expected.
- If you have copies of the channel: compare one channel instance vs the other for **unexpected NetCxx nets**.

## If your issue is PCB Layout Replication “Channel-Offset Errors”
That’s usually because the two rooms aren’t the same **component set / unique IDs / net naming** per channel.
So the highest value fix is:
- Ensure both channels come from the **same multi-channel sheet** (same compiled channel structure)
- Push ECO so PCB gets clean consistent channel mapping
- Then replicate placement/routing

If you show me the schematic compile messages (or a screenshot of the Messages panel showing any warnings), I’ll tell you which ones are actually capable of breaking rooms.

[M13] ME (2026-02-27 22:46):
[image]
[image]
Why is it dragging that other circuit when I selected the room just for that one alone 
[attached file: IMG_8306604D-F897-4967-9CA7-FB435C532A92.jpeg]
[attached file: IMG_4E2F409A-8C8D-417C-9F07-21732B7EA0EC.jpeg]

[M14] AI (2026-02-27 22:46):
That only happens for **one of two reasons** in Altium:

## 1) The “other circuit” components are **actually assigned to the same Room**
Even if they’re visually outside the pink rectangle, they can still have their **Room** property set to that room (common after ECO / replication / deleting rooms).

**Quick proof (10 seconds):**
- Click a component in the “other circuit” (the one being dragged).
- Look in **Properties** → find **Room** / **Component Room**.
- If it says the same room name as the one you’re moving (e.g. *RoomDefinition_1*), that’s why it moves.

**Fix:**
- **Design → Rooms → Recreate Rooms** (or *Update Rooms* from schematic, wording varies)
- Or delete rooms and re-push from schematic: **Design → Update PCB Document** (ECO) with “Rooms” enabled.
- Worst-case quick fix: select the wrongly-assigned components → Properties → **Room = No Room** (then reassign properly).

---

## 2) You’ve accidentally got a **Union / Group** tying both circuits together
Unions/groups make multiple objects move as one.

**How to check / fix:**
- Open **PCB Panel → Unions** (or Panels → PCB → Unions).
- If there’s a union containing both sets, select it and **Remove / Break Union**.
- Or right-click one of the dragged components → **Unions → Remove from Union** (or **Break Union**).

---

### What I think is most likely from your screenshots
Because you’re moving a **Room** (pink room selection handles) and another “block” moves too, it’s most often **mis-assigned Room membership** (reason #1), typically triggered by the multi-channel / offset mismatch issues you’ve been fighting.

If you tell me what the **Room** field says for one component in the “other circuit” (e.g., NetC18_2 capacitor or the IC), I’ll tell you the exact cleanest way to rebind rooms in your current state (without breaking placement).

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] ME (2026-02-27 21:27):
Debunker 

[A2] ME (2026-02-27 21:27):
Reminder 
