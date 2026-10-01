# Ethernet connector temp rating
Date (UTC): 2026-04-17 08:28
Conversation ID: 69e1ef26-9408-83eb-883c-e1748dc7907b
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-17 08:28):
Can you find a ra PCB mount Ethernet connector rated to 150 def c

[M2] AI (2026-04-17 08:28):
I’ll check current distributor/manufacturer listings for a right-angle PCB-mount Ethernet/RJ45 connector with a 150 °C temperature rating, then separate “true 150 °C rated” parts from parts that only survive reflow.

[M3] AI (2026-04-17 08:29):
I found **one family that gets close, but not an exact match**:

### Best match found — but only **+105 °C**, not +150 °C

**Amphenol MRJ / MRJR rugged RJ45, right-angle PCB-tail**

Examples:

| Part | Type | Mount | Temp rating |
|---|---|---:|---:|
| **MRJ-5381-01** | Rugged RJ45, Cat5/Cat5e style | Right-angle PCB tail / through-hole | likely **–40 to +105 °C** |
| **MRJ5381M1** | 8P8C RJ45 | 90° right-angle PCB | likely **–40 to +105 °C** |
| **MRJR5580M1** | Gen 2 rugged RJ45 | Right-angle PCB tail | **–40 to +105 °C** |

Farnell lists **MRJ-5381-01** as a right-angle PCB-tail RJ45 rugged connector, and DigiKey lists **MRJ5381M1** as an 8P8C RJ45 Ethernet connector with **90° right-angle** orientation. TTI’s Amphenol MRJ/MRJR search result shows the right-angle PCB-tail versions at **–40 °C to +105 °C**, not +150 °C. citeturn257889search19turn257889search15turn257889search3turn257889search11

### The only +150 °C RJ45 parts I found

The **Amphenol MRJR5480BF / MRJR5481BF** parts show **–40 °C to +150 °C**, but they are **not right-angle PCB mount** in the usual sense:

| Part | Mount / orientation | Temp |
|---|---|---:|
| **MRJR5480BF** | Flange mount, straight | –40 to +150 °C |
| **MRJR5481BF** | Panel mount / vertical solder | –40 to +150 °C |

Mouser’s filtered result for **+150 °C shielded Ethernet/modular connectors** only returned those two Amphenol MRJR parts, and the mounting-angle filters available there were **Straight** and **Vertical**, not right-angle. citeturn570744view0

### Bottom line

I **did not find a true right-angle PCB-mount RJ45/Ethernet connector rated to +150 °C**. The practical options appear to be:

1. Use **Amphenol MRJ/MRJR right-angle PCB-tail** and accept **+105 °C max**.
2. Use **Amphenol MRJR5480BF / MRJR5481BF** if **+150 °C is mandatory**, but adapt the mechanical arrangement because they are not the normal RA PCB jack.
3. If this is for an oven/endurance setup, mount the RJ45 connector **outside the hot zone** and run high-temp wiring/coax/twisted pair internally. That is usually cleaner than forcing a standard Ethernet jack into +150 °C operation.

[M4] ME (2026-04-17 09:10):
Is there anyway to recover a battery like trickle charge? Or use a car charger with a specific mode?

[M5] AI (2026-04-17 09:10):
Yes, **sometimes**, but it depends heavily on the battery chemistry and how far it has collapsed. For cordless drill/impact batteries, it is almost certainly a **lithium-ion pack**, and that changes the advice quite a lot.

## First: do **not** use a normal car battery charger on a lithium tool battery

A car charger is usually designed for **12 V lead-acid**, not lithium-ion packs. Even if it has “repair”, “recondition”, “pulse”, or “trickle” modes, that is generally for **lead-acid batteries**. Using it directly on a lithium tool battery can overcharge cells, bypass protection electronics, cause heating, venting, or fire.

So for a MacAllister-style drill battery: **do not connect a car charger directly to the battery terminals.**

## What may have happened

From what you described earlier — batteries show charged, LED comes on, tool twitches/intermittently runs — likely causes are:

1. **Battery pack voltage sagging under load**
   - The pack looks okay with no load, but collapses when the motor asks for current.

2. **One weak lithium cell group**
   - The charger may think the pack is charged, but one internal cell group is low or damaged.

3. **Battery protection board tripping**
   - The pack briefly powers the tool, then the BMS cuts out.

4. **Tool fault**
   - Since both drill and impact seem affected, battery/charger is likely, but not guaranteed.

## Can a lithium tool battery be “woken up”?

Sometimes, yes — but the safe way is usually:

### Safe recovery method

Put the battery on its **proper manufacturer charger** and leave it for a while.

Some chargers do a very low-current pre-charge automatically if the pack is below normal voltage. That is the correct “trickle” equivalent for lithium packs.

Try:

1. Let the battery reach room temperature.
2. Clean the battery contacts.
3. Put it on the correct charger.
4. Leave it for a few hours.
5. Remove it, let it rest 10 minutes, then test it.
6. Try a second known-good charger/battery if available.

## The slightly hacky method people use — but I would be very cautious

Some people “jump” a lithium pack briefly from another same-voltage pack to raise its voltage enough for the charger to recognise it. I would **not recommend doing this** unless you can measure pack voltage, understand polarity, and know the pack chemistry.

It can work, but it can also turn a damaged lithium pack into a fire risk. For a cheap power-tool battery, it usually is not worth the risk.

## What to measure with a multimeter

Check the pack voltage across the main + and – terminals.

Typical expected voltages:

| Battery label | Likely pack type | Normal charged voltage | Concerning if below |
|---:|---:|---:|---:|
| 12 V lithium | 3-cell pack | ~12.6 V full | below ~9 V |
| 18 V lithium | 5-cell pack | ~20–21 V full | below ~15 V |
| 20 V max lithium | 5-cell pack | ~20–21 V full | below ~15 V |

Then measure it again while pulling the trigger, if you can do so safely. If it collapses hard, the pack is probably tired or has a bad cell group.

## My practical recommendation

For your symptoms, I would not try a car charger. I would do this order:

1. **Clean battery and tool contacts** with contact cleaner or IPA.
2. **Measure battery voltage** fully charged.
3. Test with a **known-good battery** if you can borrow one.
4. If both batteries behave the same, suspect charger/tool contacts or the tool.
5. If one battery collapses under load, replace the battery.

If the battery is swollen, smells odd, gets hot on charge, clicks/cuts repeatedly, or has been left flat for ages, treat it as unsafe and recycle it. Lithium packs are not worth nursing back if they have genuinely failed.

[M6] ME (2026-04-17 09:12):
I have bench power supplies where I can control the current and voltage 

[M7] AI (2026-04-17 09:12):
Yes — a bench PSU is **much safer than a car charger** because you can current-limit it, but you still need to be careful. For a lithium tool battery, the bench supply should only be used as a **gentle pre-charge / wake-up**, not as a full charger.

## The safe principle

Use the bench supply to lift the pack voltage just enough that the **proper battery charger recognises it again**.

Do **not** fully charge the pack from the bench PSU unless you know the cell count, chemistry, BMS behaviour, and have individual cell monitoring.

## First identify the battery voltage

Most cordless tool packs are:

| Label on battery | Likely cell count | Full pack voltage | “Too low” region |
|---:|---:|---:|---:|
| 12 V Li-ion | 3S | 12.6 V | below ~9 V |
| 18 V Li-ion | 5S | 21.0 V | below ~15 V |
| 20 V max Li-ion | 5S | 21.0 V | below ~15 V |

If it is an **18 V / 20 V max** pack, do **not** set the PSU above about **20–21 V**.  
For recovery, you usually only need to get it to around **15–16 V** so the charger wakes up.

## Gentle bench PSU wake-up method

Assuming an **18 V / 20 V max lithium pack**:

1. Set PSU voltage to about **15.0 V to 16.0 V**.
2. Set current limit very low: **50 mA to 100 mA** to start.
3. Connect PSU positive to battery positive, negative to battery negative.
4. Watch the current and battery temperature.
5. Let it rise slowly for **5–15 minutes**.
6. Disconnect and try the proper charger again.

If the charger then accepts it, let the **proper charger** do the rest.

For a **12 V lithium pack**, use roughly:

- PSU voltage: **9.0 V to 10.5 V**
- Current limit: **50 mA to 100 mA**

## Do not force it if it behaves badly

Stop immediately if:

- the pack gets warm
- current does not taper or behaves erratically
- voltage refuses to rise
- the pack smells odd
- there is swelling, clicking, or hissing
- the PSU instantly current-limits hard
- the proper charger still refuses it after a short pre-charge

That usually means one cell group is badly discharged or damaged. At that point it is not worth rescuing.

## Important caution about the pack terminals

Some tool batteries have more than just + and – terminals. The extra pins may be thermistor, ID, balance, comms, or enable pins. For bench pre-charge, only use the **main pack + and –** terminals. Do not apply voltage to the smaller sense pins.

## My suggested settings for your likely case

For a MacAllister-style **18 V tool battery**, I’d try:

- **Voltage:** 15.5 V  
- **Current limit:** 50 mA initially  
- **Max time:** 10 minutes  
- Then try the proper charger.

If the pack voltage rises and the charger accepts it, good. If not, you can try once more at **100 mA**, but I would not push beyond that without opening the pack and checking individual cell groups.

The key thing: **bench PSU only to wake it, proper charger to charge it.**

[M8] ME (2026-04-17 09:14):
When you say accept it. The charger currently just shows it’s fully charged 

[M9] AI (2026-04-17 09:14):
That changes the diagnosis: the charger is **not “refusing” the pack as flat** — it is likely seeing the pack as **already at/near charged voltage**, or the battery electronics are reporting “charged”, while the pack still cannot deliver current.

So a bench PSU “wake-up” is probably **not the right fix** here.

## What “fully charged” but tool barely runs usually means

For an 18 V / 20 V lithium tool battery:

- Charger sees pack voltage around **20–21 V** → says full.
- Tool asks for high current → one weak cell group collapses.
- Battery BMS cuts out → tool runs for a second, LED flickers, then stops.

That is classic **high internal resistance / weak cell group**, not a simple under-voltage lockout.

## Check it with your bench supply / multimeter

Measure the battery main terminals:

### 1. No-load voltage

Fresh off charger:

- **18 V lithium pack:** should be about **20.0–21.0 V**
- **12 V lithium pack:** should be about **12.0–12.6 V**

If it shows around full voltage, the charger’s behaviour makes sense.

### 2. Voltage under load

Put the battery in the tool and measure across the battery terminals while pulling the trigger, or use a sensible dummy load if you have one.

For an **18 V pack**:

| Result under load | Meaning |
|---|---|
| Drops from ~20 V to maybe 17–19 V | Probably okay |
| Drops sharply to 10–15 V | Weak cell group / high resistance |
| Drops to near 0 V then recovers | BMS is tripping |
| Stays high but tool stops | Tool/contact/switch fault more likely |

## Can the bench PSU help now?

Only for testing, not really recovery.

You can use the bench PSU to test the tool **without the battery**, if your PSU can supply enough current. But most bench PSUs cannot supply the startup current of an impact driver or drill, which can be tens of amps.

For a cautious tool test:

- Set PSU to the battery’s nominal voltage:
  - 18 V tool → **18 V**, maybe up to **20 V max**
- Current limit:
  - start at **1–2 A**
  - expect the tool may not run properly
- Do not stall the motor.
- Use short trigger taps only.

If the tool tries to run normally from PSU but current-limits, that at least suggests the tool is alive.

## What I would not do

I would **not trickle-charge a pack that the charger already thinks is full**. That risks overcharging the better cell groups while the weak group remains the problem.

A lithium pack that says full but collapses under load usually needs:

- cell group diagnosis,
- cell replacement/rebuild,
- BMS/contact repair,
- or replacement battery.

## Most likely conclusion

Given your earlier symptom — **both drill and impact driver only twitch intermittently, LEDs come on, batteries charge fine** — I’d suspect either:

1. **Both batteries are tired/failed**, especially if same age and usage pattern, or  
2. **Charger is incorrectly terminating**, less likely if pack voltage is genuinely full, or  
3. **Battery/tool contact issue**, especially if both tools behave similarly.

Best next measurement: tell me the battery label voltage and the **actual voltage across +/– fresh off the charger**, then the **voltage while pulling the trigger**. That will separate weak battery from tool/contact fault very quickly.

[M10] ME (2026-04-17 09:16):
There does seem to be corrosion on contacts 

[M11] AI (2026-04-17 09:16):
Yes — **corroded contacts could absolutely cause your exact symptoms**:

- charger says battery is full
- LED comes on
- tool twitches briefly
- impact/driver works intermittently
- both tools affected

A high-resistance contact can pass enough current for electronics/LEDs, but not enough for the motor surge.

## What to do first

Remove the battery and clean **both sides**:

1. **Battery terminals**
2. **Tool contacts**
3. **Charger contacts**

Use:

- **IPA / isopropyl alcohol**, or electrical contact cleaner
- cotton bud, toothbrush, or small nylon brush
- for heavier corrosion: very light rub with a fibreglass pen, fine abrasive pad, or folded fine wet-and-dry paper

Then wipe clean and let it dry fully.

## Avoid

Do **not** use WD-40 as the main cleaner on electrical contacts. It can leave residue. If you already have, clean it off afterwards with IPA/contact cleaner.

Do **not** aggressively scrape plated contacts unless you have to. Once the plating is damaged, corrosion comes back faster.

## Best quick test

After cleaning, insert/remove the battery several times to help wipe the contacts. Then try the tool.

Also try pressing the battery firmly into the tool while pulling the trigger. If it runs better when pushed or wiggled, that strongly points to contact pressure/corrosion rather than dead cells.

## If the corrosion is green/blue/white

That suggests oxidation or leakage/contamination. Clean it thoroughly and inspect for pitting. If the contacts are badly pitted or loose, cleaning may only partly fix it.

## Bench PSU relevance

Before trying any recovery charge, I’d fix the contacts first. With corroded contacts, the battery may be fine but unable to deliver motor current. A bench PSU or trickle charge would not solve that.

Best next diagnostic is: clean the contacts, then measure voltage at the battery terminals while the tool trigger is pulled. If voltage stays high but the tool cuts, suspect contact/switch/tool path. If voltage collapses, suspect the battery internally.

[M12] ME (2026-04-17 09:18):
Isn’t it unlikely that all 4 batteries fail.. and it’s more environmental/corrosion 

[M13] AI (2026-04-17 09:18):
Yes — **if all 4 batteries show similar symptoms, simultaneous cell failure is much less likely**. It starts to look much more like a **common environmental/contact issue**, especially now you’ve seen corrosion.

The most likely common faults are:

1. **Corroded battery/tool contacts**
   - Enough conductivity for LEDs/control electronics.
   - Not enough for motor surge current.
   - Impact driver may twitch because the voltage collapses at the contact under load.

2. **Corroded charger contacts**
   - Charger may misread pack state or only make contact through sense/ID pins.
   - It may show “full” without properly interacting with the pack.

3. **Oxidation on the tool-side spring contacts**
   - If both drill and impact were stored in the same damp place, the internal contact rails/springs may both be affected.

4. **Damp/contamination inside the battery slide rail**
   - Dust, moisture, cement dust, shed condensation, etc. can create high-resistance paths or poor mechanical seating.

## So yes: I’d treat this as a contact/current-delivery problem first

A battery can look fine at no-load voltage, and the charger can say full, but a dirty contact only has to add a tiny resistance to kill a cordless tool.

Example: at **20 A**, just **0.1 Ω** of bad contact resistance drops:

**V = I × R = 20 × 0.1 = 2 V**

and dissipates:

**P = I² × R = 20² × 0.1 = 40 W**

That is enough to cause cut-outs, twitching, heat, arcing, and BMS trips.

## What I’d do now

Clean every current-carrying contact:

- battery main + and –
- tool + and –
- charger + and –
- any obvious sense/temperature contacts

Use **contact cleaner or IPA**, then a light mechanical clean if needed.

For stubborn corrosion, use:

- fibreglass pencil
- very fine abrasive paper
- small brass brush
- small flat screwdriver only very gently, as a last resort

Then insert/remove each battery into the tool and charger **10–20 times** to wipe the mating contacts.

## Key diagnostic

After cleaning, try this:

1. Put battery in tool.
2. Hold the battery pushed firmly into the tool.
3. Pull trigger.
4. Wiggle battery slightly while holding trigger.

If the tool changes behaviour — cuts in/out, runs briefly, or speeds up — that is almost certainly **contact seating/corrosion**, not four dead batteries.

Also check whether the contacts look **dull, blackened, green, blue, white, or pitted**. Green/blue especially points to corrosion rather than normal wear.

[M14] ME (2026-04-17 09:22):
What about carberetta spray 

[M15] AI (2026-04-17 09:22):
I’d **avoid carburettor spray** for the battery/tool contacts.

It will probably remove grime, but it is often quite aggressive: it can attack plastics, soften rubber seals, strip protective films, and leave the contacts very “dry” and prone to rapid re-oxidising. Around battery housings, trigger plastics, and charger slots, it is a bit of a blunt instrument.

Better options:

1. **Electrical contact cleaner** — best choice. Ideally plastic-safe and residue-free.
2. **IPA / isopropyl alcohol** — safe, cheap, decent for light oxidation and contamination.
3. **Fibreglass pencil or very fine abrasive** — only for visible corrosion on metal contacts, then clean again with IPA/contact cleaner.

For your case, I’d do:

- Remove battery.
- Spray/contact-clean the **battery terminals**, **tool contacts**, and **charger contacts**.
- Gently scrub with toothbrush/cotton bud.
- If green/white corrosion remains, very lightly abrade just the metal.
- Let it fully dry.
- Insert/remove the battery 10–20 times to wipe the mating faces.

Do **not** soak the battery pack or charger. Keep liquid out of the casing as much as possible.
