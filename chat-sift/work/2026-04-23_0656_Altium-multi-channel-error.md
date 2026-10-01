# Altium multi-channel error
Date (UTC): 2026-04-23 06:56
Conversation ID: 69e9c269-f074-83eb-bc9f-77e14fccff9d
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-23 06:56):
Altium is annoying me. It says can't gave the same port name but then can't have multiple names?? Using multi channel hierarchy 

[M2] ME (2026-04-23 06:56):
[image]
[attached file: AE26B016-A778-4E24-926D-E3FB8FBE48B5.jpeg]

[M3] AI (2026-04-23 06:56):
I’m checking the exact Altium rule behind that message and how it interacts with multi-channel sheets, then I’ll tie it back to your screenshot so you can fix this without tearing the hierarchy apart.

[M4] AI (2026-04-23 06:56):
Yes — this is Altium being fussy, but there is a logic to it.

From your screenshot, the error is:

> **Port name duplicated among sheet entries**

That usually means **on the parent sheet symbol**, Altium sees **more than one sheet entry with the same name on what it thinks is the same channel block**, and it does not allow that. At the same time, inside a proper **multi-channel repeated child sheet**, you are absolutely allowed to reuse the same port names, because the channel index disambiguates them after compilation. Multi-channel design is normally created by reusing the **same child sheet** via multiple sheet symbols or with the **Repeat** keyword in the sheet symbol designator. citeturn388529search1turn388529search12

What that means in practice:

- **Inside one child sheet**: use the same port names for each repeated channel, such as `IN`, `OUT`, `GAIN`, `FB`, etc. That is normal for multi-channel. citeturn388529search1turn388529search12
- **On one sheet symbol instance**: each **sheet entry** must match a unique child-sheet port by **name and I/O type**. If you accidentally create two sheet entries both called `P0` on the same sheet symbol, Altium complains exactly like this. citeturn388529search7turn388529search14
- If the project’s **Net Identifier Scope** is wrong, especially `Flat` or `Global`, same-named ports across sheets can also create confusing duplicate/continuity issues because Altium may treat same-named ports on different sheets as connected. For hierarchical multi-channel work, that setting often needs checking. citeturn388529search11turn388529search16

Looking at your image, the likely issue is one of these:

1. You have **duplicate sheet entries on the parent symbol** for the same child connection.
2. You copied a sheet symbol or entries manually and now the **sheet entries are no longer synchronized** with the child ports.
3. The child sheet has been edited, but the parent sheet symbol was not re-synced.
4. The project connectivity scope is set in a way that is fighting the hierarchical intent. citeturn388529search5turn388529search7turn388529search11

The clean fix is usually this:

1. Open the **child sheet** and make sure each port is uniquely defined there once.
2. Go back to the **parent sheet symbol**.
3. Right-click the sheet symbol and run **Sheet Symbol Actions → Synchronize Sheet Entries and Ports**.
4. Delete any manually duplicated entries that should not be there.
5. Check **Project Options → Options → Net Identifier Scope** and make sure it matches a proper hierarchical/multi-channel setup rather than a flat one. Altium notes that the relationship between ports and sheet symbols depends on that setting. citeturn388529search14turn388529search7turn388529search11

The key distinction is:

- **Same port name across repeated channels** = fine.
- **Same sheet entry name duplicated on one parent sheet symbol** = not fine.

So Altium is not really saying “you can’t reuse names in multi-channel.” It is saying “on this one sheet symbol, I’ve found multiple entries that collide.”

Your screenshot strongly suggests the parent sheet symbol / sheet-entry side is where it has gone wrong, not the concept of multi-channel itself.

A good rule for Altium is: **never hand-edit sheet entries unless you have to**. Let the **child ports drive the parent entries** using synchronize. That avoids exactly this class of mess. citeturn388529search5turn388529search7turn388529search14

If you want, send a zoomed-out shot showing:
- the parent sheet symbol,
- the child sheet’s ports,
- and your Repeat syntax/designators,

and I’ll tell you exactly which object is wrong.

[M5] ME (2026-04-23 11:14):
I was talk in g about the multi name. It moans when the same names, it moans when there's multi names.

[M6] AI (2026-04-23 11:14):
Yep — I get you now. This is the classic Altium connectivity trap:

It complains if you use the **same names** in the wrong context, and it complains about **multiple names** when you mix naming methods on the same wire. In Altium, a single wire/net can only end up with one effective name; if that same wire touches, say, a **net label** and a **port/sheet entry** with a different interpreted name, it reports **“Wire … has multiple names.”** citeturn584035search0turn584035search7turn584035search12

From your screenshot, that is exactly what is happening. For example, entries like:

- `Wire SC0 has multiple names (Net Label SC0, Port …)`
- `Wire SC_CH5 has multiple names (Net Label SC_CH5, Port SC_5_SCLK5, Sheet Entry …)`

mean Altium sees one physical wire, but more than one naming source attached to it, and those names do not resolve cleanly to one name. citeturn584035search0turn584035search14

## What the rule actually is

In hierarchical designs, **sheet entries connect to child-sheet ports**. Ports are for inter-sheet connectivity, while net labels are for naming nets on a sheet. Altium’s project options also control whether ports are allowed to name nets. citeturn584035search3turn584035search5turn584035search15

So the safe rule is:

- **Inside a child sheet:** use **ports** to define what goes up to the parent.
- **On the parent sheet symbol:** use **sheet entries** matching those child ports.
- **On the same wire segment:** do **not** also stick a separate net label on there unless you are sure it resolves to exactly the same intended compiled name. Altium explicitly warns against multiple net identifiers producing conflicting names on one net. citeturn584035search7turn584035search12turn584035search17turn584035search18

## Why multi-channel makes it feel contradictory

In a proper multi-channel design, you often reuse the **same child-sheet port names** across repeated channels, and Altium then compiles unique channelized names behind the scenes. That is normal. The trouble starts when you manually decorate those same signals with extra net labels on the parent or child, so Altium now sees both:

- the hierarchical name coming from the **port/sheet entry path**, and
- your manual **net label** name on the same wire. citeturn584035search1turn584035search3turn584035search5

That is why it feels like:

- “same names are bad”
- “different names are bad”
- “multiple names are bad”

What Altium really wants is:

- **one connectivity method per signal path**, used consistently.

## For your case, the fix is usually this

For those hierarchical multi-channel signals, remove the extra naming clutter and let hierarchy do the work.

### Best practice
On hierarchical/multi-channel connections:

- child sheet: **Port**
- parent sheet symbol: **Sheet Entry**
- parent wiring: optional wire, but avoid extra net labels unless essential
- avoid putting **Port + Net Label + Sheet Entry** all into the same logical path unless the naming is deliberate and consistent

That should stop the “multiple names” messages. This matches Altium’s guidance that ports/sheet entries are the hierarchical connection mechanism, while net identifiers define connectivity and can conflict when mixed improperly. citeturn584035search3turn584035search5turn584035search7turn584035search12

## The likely direct cause in your screenshot

This line is the giveaway:

`SC_CH5 has multiple names (Net Label SC_CH5, Port SC_5_SCLK5, Sheet Entry …)`

So that wire probably has:

- a **net label** called `SC_CH5`
- a **port** called `SC_5_SCLK5`
- and a **sheet entry** tying into that same path

That is not one naming system anymore — it is three. Altium is right to moan there. citeturn584035search0turn584035search14

## What I’d do immediately

1. Pick one test signal that errors, like `SC_CH5`.
2. Trace it from parent to child.
3. Remove the **net label** first.
4. Leave only the **sheet entry / child port** relationship.
5. Recompile.

If the error disappears, that confirms the issue is mixed naming, not multi-channel itself.

## The simplest mental model

- **Net labels** = name wires on a sheet.
- **Ports / sheet entries** = connect sheets hierarchically.
- **Do not use both to fight over the same wire name.** citeturn584035search5turn584035search7turn584035search15

If you send one clear crop of a single failing parent/child connection, I’ll tell you exactly which object to delete and which to keep.
