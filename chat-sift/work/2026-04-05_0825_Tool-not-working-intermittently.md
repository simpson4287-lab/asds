# Tool not working intermittently
Date (UTC): 2026-04-05 08:25
Conversation ID: 69d21c46-2ffc-838f-8f72-a6fc28df4b34
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-05 08:25):
My mcalister drill and impact driver are jonlonger working. The batteries charge fine and thenimpsct driver turns for a second here and there intermittently. The led also comrsninnbothbif then when the trigger is pulled. Whatbcouod be the issues

[M2] AI (2026-04-05 08:25):
Most likely it’s **not the batteries** if they charge normally and **both tools show the same fault**. The strongest suspects are:

1. **Battery-to-tool contact problem**
   If the battery terminals or tool contacts are dirty, tarnished, bent, or loose, you can get enough power for the LED but not enough for the motor. The LED draws very little current; the motor needs a lot more.

2. **Battery pack can show “charged” but collapse under load**
   A weak cell inside the battery can still let the charger say “full,” and still light the LED, but as soon as the motor tries to draw current the voltage drops and the tool cuts in and out.

3. **Trigger / speed controller fault**
   On modern drills and impact drivers, the trigger usually contains the electronic speed control. If that starts failing, you can get intermittent motor operation, flickering, brief spins, and LED behaviour.

4. **Motor brushes or commutator issue**  
   If these are brushed motors, worn brushes, dirty commutator segments, or a dead spot on the armature can cause exactly this “works for a second here and there” behaviour.

5. **Protection circuit tripping**
   A shorted motor winding, failing trigger electronics, or a bad battery can make the protection kick in immediately.

Because **both drill and impact driver are doing it**, I would rank them like this:

- **Most likely:** battery issue under load, or dirty/poor contacts
- **Next:** both tools exposed to damp/dust causing contact or trigger faults
- **Less likely but possible:** both tools independently failed internally

What to check first:

**A. Inspect and clean all contacts**
- Battery terminals
- Tool battery contacts
- Look for blackening, green corrosion, bent tabs, looseness

Use a dry cloth first. If needed, use electrical contact cleaner. Let it dry fully.

**B. Try each battery in each tool**
Make a little matrix:

- Battery 1 + drill
- Battery 1 + impact
- Battery 2 + drill
- Battery 2 + impact

If **all combinations fail the same way**, that points more to the tools or the contact interface.
If **one battery is bad in both tools**, that battery is the culprit.

**C. Watch for behaviour under trigger**
- LED bright but motor barely twitches = likely high resistance / weak battery / trigger fault
- Motor sparks or smells burnt = motor/brush issue
- Only works if you wiggle the battery = contact problem

**D. Check whether the battery latches tightly**
If the pack has even slight movement, the connection can break under vibration or trigger pull.

**E. Listen closely**
- single click = protection or trigger electronics
- rough crackle = brushes/commutator/contact issue
- absolutely nothing but LED = trigger/controller likely

A very useful clue:
If the tool sometimes runs when you **tap the body lightly** or rotate the chuck by hand a little first, that strongly suggests **brush/commutator dead spot** in the drill motor.

For the impact driver:
If it gives only a tiny twitch and stops, that can be:
- motor/controller fault
- poor battery current delivery
- seized gearbox or internal damage, though that is less likely if the LED is fine and it tries to start

My best diagnosis from your symptoms:
**Start with battery/contact fault first, especially a battery that charges but cannot deliver current.** The fact the LED comes on in both tools but the motor only briefly turns is classic for **“enough voltage for the light, not enough current for the motor.”**

If you want, describe:
- how many batteries you have,
- whether both tools fail with all batteries,
- whether they’ve been stored somewhere damp or cold,
- and whether the drill chuck can still be turned by hand,

and I’ll narrow it down properly.
