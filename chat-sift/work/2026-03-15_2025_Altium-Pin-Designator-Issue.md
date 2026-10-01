# Altium Pin Designator Issue
Date (UTC): 2026-03-15 20:25
Conversation ID: 69b7158f-6908-8393-82f6-c958d8ef913a
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-15 20:25):
[image]
[image]
I’ve coded a part alphanumeric. But the layout says purely numeric 
[attached file: IMG_F08661D7-AAE6-479E-9127-17E3CF88A410.jpeg]
[attached file: IMG_2B238009-7D6F-4B38-B91C-D701015F5558.jpeg]

[M2] AI (2026-03-15 20:25):
That is normal in Altium: the **schematic pin designator** and the **PCB pad designator** must match if they are meant to be the same pin.

What you’ve got now looks like this:

- **Schematic symbol pin** = `E1`, `E2`, `E3`
- **PCB footprint pad** = `1`, `41`, `81`, `121`, `161` etc.

So the layout is not “changing” it — it is showing the **pad designator from the footprint**.

### The key point
In Altium, the PCB side does **not care about the pin name you want conceptually**. It maps by:

**symbol pin designator ↔ footprint pad designator**

So if the symbol says `E1` but the footprint says `161`, they are different pins as far as Altium is concerned.

### What to do
You have two valid approaches.

#### Option 1 — Make them match exactly
If you want the PCB to show `E1`, then edit the **footprint pad designators** to `E1`, `E2`, `E3`, etc.

That means in the PCB library footprint:
- change pad `161` to `E1`
- change pad `162` to `E2`
- and so on

Then the schematic symbol pin designators must also be `E1`, `E2`, `E3`.

This works fine in Altium as long as the package genuinely uses alphanumeric cavity IDs.

#### Option 2 — Keep numeric pad numbers, use names separately
This is often the better method for connectors.

Use:
- **Pin Designator** = actual physical pad number, like `161`
- **Pin Name** = logical label, like `E1` or `CB0_FAST_CLOCK_0_P`

That way:
- symbol-to-footprint mapping stays robust
- PCB keeps real pin numbers
- the schematic can still show useful functional labels

### Why yours is confusing right now
Your top screenshot shows the **Pin Designator** field set to `E1`.  
Your bottom screenshot shows the footprint pad **Designator** is `161`.

So they do not correspond.

### Best practice for connectors
Usually:

- **Designator** = manufacturer’s actual contact/pin number
- **Name** = signal or cavity label

For example:
- Designator: `161`
- Name: `E1`
- Net label: `CB0_FAST_CLOCK_0_P`

That is normally cleaner than making the physical pin number alphanumeric unless the connector documentation itself uses `E1`, `E2`, etc as the true contact IDs.

### In your case
Because this looks like a PoGo / connector style interface, I’d check the connector drawing:

- If the manufacturer calls the contacts `E1`, `E2`, `E3`, then rename the **PCB pads** to those values too.
- If the manufacturer numbers them `161`, `162`, etc, then keep PCB numeric and move `E1` into the **pin name** instead, not the designator.

### Practical fix
Open the symbol and footprint side by side and decide which field is the true physical mapping field:

- **Symbol pin Designator** must equal **Footprint pad Designator**
- Any friendlier text should go in **Pin Name** or as overlay text

If you want, send one screenshot of the **schematic symbol pin properties** and one of the **footprint pad properties** for the same contact and I’ll tell you exactly which field to put `E1` into.
