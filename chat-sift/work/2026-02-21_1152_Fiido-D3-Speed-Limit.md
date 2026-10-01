# Fiido D3 Speed Limit
Date (UTC): 2026-02-21 11:52
Conversation ID: 69999c6e-ae98-8393-b3e4-8f8bc21b4f28
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-02-21 11:52):
Fiido d3 off public road max speed is 18.5mph, I was expecting 22

[M2] AI (2026-02-21 11:52):
18.5 mph is ~30 km/h. 22 mph is ~35 km/h. So what you’re seeing is basically: **your D3 is “part-unlocked” to ~30 km/h, but not to the full ~35 km/h**.

A few realities to anchor expectations:

- **Most Fiido D3 / D3 Pro units are sold as 25 km/h (15.5 mph) assist-limited** by design. That’s explicitly stated in D3 Pro documentation/spec pages. citeturn0search35turn0search0turn0search1turn0search2  
- In the UK, anything that provides motor assistance above **15.5 mph** on public roads **stops being an EAPC** and is treated as a motor vehicle (moped/motorcycle rules). citeturn1search0turn1search1

Why you might be topping out at ~18.5 mph (30 km/h) instead of ~22 mph (35 km/h):

1. **Controller / firmware variant**  
   Some controller versions cap “off-road” at ~30 km/h, others allow higher (and some are region-locked). There are enough reports of “doesn’t reach expected speed” that Fiido sometimes swaps controllers after troubleshooting. citeturn0reddit34

2. **Speed sensor / wheel-size calibration**  
   If the wheel size setting is wrong, the display speed and the cut-off behaviour can be off. (On small wheels like the D3’s, this matters more.)

3. **Battery voltage sag / state of charge**  
   On a 36 V system, you’ll typically only see “best speed” right off a full charge. Under load, voltage drops and the controller may not deliver enough power to keep pushing up to the next speed step.

4. **Power limit + drag**  
   The D3 is a compact bike; rider weight, tyre pressure, wind, gradient, and rolling resistance can easily be the difference between ~30 km/h and ~35 km/h.

What I’d do (safe + practical checks):

- **Confirm the limit setting** in the display/app (if your variant has it) and ensure any “speed limit” isn’t set to 30 km/h.
- **Verify wheel size / P-setting** matches the actual wheel size.
- **Check speed sensor alignment** (magnet gap, secure mounting) and that the speed reading is stable.
- **Test on full charge**, flat road, tyres properly inflated.
- If everything is correct and it still hard-stops at ~30 km/h, **it’s very likely your controller/firmware is the limiting factor** — at that point, it’s worth **asking Fiido support which controller version you have** and whether a replacement is available for your model/region. citeturn0reddit34

If you tell me **whether it’s D3 or D3 Pro**, and what method you’re using to measure speed (display vs GPS), I can narrow down which of the above is most likely.

[M3] ME (2026-02-21 11:54):
D3 pro brought this week. On bike display. Firmware version 40

[M4] AI (2026-02-21 11:55):
Got it — **Fiido D3 Pro, bought this week, display shows FW v40**.

Two key points:

1) **A D3 Pro is normally specced/limited to 25 km/h (15.5 mph)** from the factory (that’s what Fiido and multiple manuals/spec pages state). citeturn0search3turn0search38turn0search2turn1search5  
So **22 mph (~35 km/h) isn’t the “expected” stock behaviour** for a D3 Pro.

2) **18.5 mph on the bike display is already ~30 km/h**, i.e. *above* the stated 25 km/h spec. That usually means one of these is happening:
- **The display is mis-calibrated** (wheel size parameter wrong, so speed is over-reported), *or*
- The bike/controller is genuinely allowing ~30 km/h (some region/controller variants do odd things).

### What to do (fast, definitive)
**Step 1 — verify real speed with GPS**
Use a phone GPS speed app and do a steady run on flat ground.
- If GPS shows **~15–16 mph** while the display shows **18.5 mph**, your **wheel size / speed calibration is wrong** (very common on small-wheel e-bikes).
- If GPS also shows **~18–19 mph**, then the bike is actually doing ~30 km/h.

**Step 2 — if it’s a calibration issue**
On many e-bike displays there’s a wheel-size setting (sometimes called “wheel diameter” or a P-setting). For the D3 Pro it should correspond to **14-inch wheels** (D3 Pro is commonly listed with **14×2.125** tyres). citeturn0search1turn1search2turn1search4  
Your manual explicitly warns not to change background parameters casually, so if the menu isn’t obvious, it’s safer to have **Fiido support tell you the correct parameter path for your exact display/firmware**. citeturn1search0turn1search7

**Step 3 — if it’s genuinely capped at ~30 km/h and you “expected 35”**
That expectation usually comes from other models, aftermarket controller behaviour, or internet chatter — **it’s not the normal published D3 Pro spec**. citeturn0search3turn0search38turn1search5  
Also, in the UK, anything assisting above **15.5 mph** on public roads isn’t an EAPC. citeturn0search2

If you want, tell me **your GPS-measured top speed** (one number) and whether the display is set to **mph or km/h** — then I can say confidently whether you’re looking at *miscalibration* vs a *true controller limit*.

[M5] ME (2026-02-21 14:37):
How easy is it to concerns bike to an ebike. I have a canondale  quick 2

[M6] AI (2026-02-21 14:37):
Pretty doable on a **Cannondale Quick 2** — it’s a sensible donor bike (strong hybrid frame, disc brakes, 700c wheels). The “ease” mainly depends on *which* conversion route you choose.

## First: keep it UK-legal (if you’ll ride on public roads)
To stay an EAPC in Great Britain, the motor must be **≤250 W continuous** and assistance must cut off at **15.5 mph (25 km/h)**. Anything assisting beyond that becomes a motor vehicle (registration/insurance/helmet, etc.). citeturn0search0turn0search2

## Your Quick 2’s key compatibility bits (good news)
Cannondale’s Quick 2 uses:
- **700c wheels**
- **Hydraulic disc brakes**
- **Rear hub: QR 135×9 mm** (common and conversion-friendly)
- **Front hub: 12×100 mm thru-axle** (possible, but fewer hub-motor options) citeturn1search1turn1search3

That means: **rear hub motor kits are usually the easiest “clean” fit** on this bike.

---

## Option A — Rear hub motor kit (usually easiest on your bike)
**Difficulty:** medium (DIY-able with basic tools)  
**Pros:** straightforward fit (QR 135×9), good reliability, keeps your drivetrain stock  
**Cons:** adds weight at rear wheel; needs careful cable routing + torque arm

What’s involved:
- Swap rear wheel for a motor wheel (or lace a motor into your rim)
- Fit **pedal assist sensor** (and optionally a road-legal “walk assist”)
- Mount battery (downtube or rear rack)
- Install controller + wiring harness
- Check brake cutoffs (many kits include levers; with hydraulics you often skip lever swap and rely on PAS-only control)

---

## Option B — Front hub motor kit (possible, but your fork is thru-axle)
**Difficulty:** medium–hard  
Your fork is **12×100 thru-axle** citeturn1search1turn1search3, and lots of generic front hub kits assume a QR fork. There *are* thru-axle compatible options, but selection is narrower and fitment is fussier.

---

## Option C — Mid-drive kit (best “ride feel”, most fiddly)
**Difficulty:** medium–hard (more mechanical work)  
**Pros:** climbs well, efficient, keeps wheels standard  
**Cons:** more wear on chain/cassette, more setup complexity, bottom bracket standards matter

Your Quick line commonly uses a **68 mm threaded/BSA-type BB on some models**, but I wouldn’t assume it for your exact Quick 2/year without checking (Cannondale varies by model/year). A quick look at the BB area (threaded cups visible vs press-fit) confirms.

---

## Option D — “Minimal hassle” kits (e.g., Swytch-style front wheel + bar battery)
**Difficulty:** easy–medium  
These are designed to be universal and quick to install, but again: your **front thru-axle fork** means you must confirm they offer a matching front motor/wheel format for your exact fork. Swytch’s own pitch is “universal conversion kit including motor wheel + battery”, and their UK throttle behaviour is designed around UK rules. citeturn0search1turn0search3

---

## Practical reality: cost + effort
- **DIY rear hub conversion:** commonly the best balance of ease, cost, and compatibility for the Quick 2.
- Expect a few hours of install time if you’re comfortable with bike wrenching, plus a proper safety check (axle retention, torque arm, cable strain relief, brake test).

## Two questions that let me steer you to the “right” route immediately
1) **What year is your Quick 2?** (or a photo of the drivetrain/BB area)  
2) Do you want it **strictly road-legal assist** (15.5 mph), or is this **private land only**?

If you answer those, I’ll recommend the best conversion type for *your exact* Quick 2 and list the key measurements/specs to confirm before buying anything.

[M7] ME (2026-02-21 14:44):
2014, off road 

[M8] AI (2026-02-21 14:45):
2014 Quick 2 is a *very* workable donor for a conversion. The “how easy” mostly comes down to **which drive type you choose** and whether you’re happy doing basic bike-mechanics.

A quick legal note (UK): if you ever ride it on public roads, the EAPC rules are **250 W continuous** and **assist cut-off at 15.5 mph**. Anything beyond that is treated as a motor vehicle. citeturn4search0turn4search2turn4search4

## Easiest conversion route for a 2014 Quick 2
### 1) Rear hub motor kit (usually the least hassle)
**Why it’s easiest:** it avoids bottom-bracket compatibility questions and keeps your drivetrain unchanged.

What to check on your bike (5 minutes with a tape measure):
- **Rear dropout spacing** (most hybrids are **135 mm** QR, but measure to be sure).
- **Brake type**: rim brakes vs disc.  
  - Rim-brake bikes are straightforward (no rotor alignment issues).
  - Disc bikes are still fine, just pick a motor wheel that matches your rotor mount and spacing.

Must-do safety item:
- **Torque arm(s)** on the rear dropout. Hub motors apply axle torque that can chew dropouts if you skip this.

### 2) Mid-drive (best climbing feel, more fiddly)
This is the “proper e-MTB feel” option because it drives through the chain, but it demands **bottom bracket compatibility** and tends to increase chain/cassette wear.

Typical Bafang-style mid drives (BBS02 etc.) commonly fit **68–73 mm** bottom brackets *if* your frame uses a compatible BB standard. citeturn4search1turn4search3  
So you need to identify whether your 2014 Quick 2 has a **threaded BB shell vs BB30 / press-fit** before you buy.

## For “off-road” use: what power/speed should you aim for?
On private land you can go higher than EAPC limits, but practically:
- **500–750 W** feels like the sweet spot for “fast hybrid” without becoming a heat/brake/handling headache.
- Above that, you’re into “everything else becomes the limiting factor” (braking, tyres, frame stress, battery current, controller heat).

## The fastest way to get you to a correct parts list
Reply with:
1) **Rim brakes or disc brakes?** (photo of the rear wheel area is enough)  
2) **Rear dropout spacing** you measure (usually 135 mm)  
3) Do you want **throttle**, or **PAS only**?

And I’ll tell you which of the two (rear hub vs mid-drive) is the cleanest fit for your exact Quick 2, plus a sanity-checked shopping list (motor type, battery voltage/capacity range, controller current range, torque arms, and any special tools).

[M9] ME (2026-02-21 14:47):
Hydraulic disk brakes. Yes 135mm. Not fussed with throttle.

[M10] AI (2026-02-21 14:47):
Nice — **hydraulic discs + 135 mm rear spacing** makes your 2014 Quick 2 a *very* friendly donor for a conversion.

### The cleanest build for your bike (given your constraints)
**Rear hub motor, 700c, 135 mm** + PAS (no throttle).  
This avoids bottom-bracket standard headaches and keeps your drivetrain/chainline mostly stock.

A very common spec in the conversion world is a **Bafang G020 rear hub kit** that’s explicitly sold in **135 mm dropout spacing** and available in **700c** builds. citeturn1search5

---

## What to buy (practical shopping list)
### 1) Motor / controller
Because you said “off-road”:
- **48 V rear hub kit**, nominal **500–750 W** range (controller current typically 20–25 A for 500 W feel, 25–30 A for 750 W feel).
- Choose a **700c rear wheel** build *or* a bare motor to lace into your rim.

### 2) Disc brake compatibility (don’t guess this bit)
Your hub motor wheel must match your rotor interface:
- **6-bolt rotor mount** *or* **Centerlock**.

Quick way: look at your current rear rotor.
- 6 Torx bolts = **6-bolt**
- Big lockring = **Centerlock**

(Some hub motors are 6-bolt only; some are centerlock; adapters exist but I’d rather match native where possible.)

### 3) Battery
- **48 V battery** (13S lithium). Capacity depends on range; typical is 10–20 Ah.
- Mounting: **downtube** (best handling) if your frame has bosses and clearance; otherwise **rear rack**.

### 4) Torque arm(s) (non-optional)
A hub motor can rotate the axle in the dropout and damage it if you don’t restrain it.
- Fit **at least one torque arm**, two if you go 750 W / higher current.

### 5) Hydraulic brake cut-off (optional but recommended)
Since you have hydraulic levers, many kits’ “replacement e-brake levers” aren’t ideal.
- Use **stick-on hydraulic brake sensors** (magnet + reed/Hall sensor) so motor cuts when you brake.

### 6) PAS sensor
- **Bottom-bracket PAS ring** + sensor is fine if you’re not fussed about throttle.
- If you want nicer feel later: consider a **torque-sensing BB** option, but that’s more money/fitment work.

---

## Installation difficulty (realistic)
If you’re comfortable swapping a wheel and doing tidy cable routing:
- **Rear hub build:** medium (very doable DIY in an afternoon)
- The two “gotchas” are **torque arm fitment** and **disc rotor alignment**.

---

## Performance expectations (off-road)
With 48 V + 500–750 W:
- You’ll get a *meaningful* jump over a stock legal 250 W bike, especially in acceleration and hills.
- Top speed depends on controller limit + wheel RPM + load; hub kits are usually configured by the controller/display settings.

(If you ever plan to ride it on UK public roads, remember the EAPC limit is 15.5 mph assist and 250 W continuous. citeturn0search0)

---

## Quick confirmation questions (so I can be precise and stop you buying the wrong interface)
1) Is your **rear rotor 6-bolt or centerlock**?  
2) What tyre size are you running (e.g., **700×32c**, **700×35c**)?  
3) Any preference: **quiet/stealthy** vs **max shove**?

Answer those and I’ll pin down a sensible target spec (voltage, power, controller amps) and the exact compatibility checklist for your Quick 2.

[M11] ME (2026-02-21 15:07):
Candondale quick cx2 2014

[M12] AI (2026-02-21 15:07):
Perfect — **2014 Cannondale Quick CX 2** with **hydraulic discs** and **135 mm rear spacing** is one of the easier “real bike → e-bike” donors.

A couple of specs that matter for conversion on *your exact model*:

- The 2014 Quick CX 2 runs **700×35c tyres** (so you’re in standard 700c land for wheel kits). citeturn1view0  
- It uses a **Tange cartridge bottom bracket**, i.e. the common “cartridge BB” style rather than Cannondale’s BB30 system (which is great news for mid-drive compatibility). citeturn2search1  

## Easiest, least-faff route: 700c rear hub motor kit (PAS only)
Given you’re **not fussed about throttle**, this is the cleanest build:

**Why this is easiest**
- No chainline/drivetrain re-engineering.
- No bottom-bracket extraction headaches beyond a simple PAS sensor ring.
- Works very nicely with a hybrid like the Quick CX (especially on mixed paths).

**Must-haves**
- **Torque arm(s)** (non-optional at “off-road” power levels).
- A hub wheel that matches your **disc rotor interface** (6-bolt vs centerlock).

## “Best ride feel” route: mid-drive kit
If you want stronger climbing + a more “natural” drive feel, mid-drive is great on this bike because the **cartridge BB** typically means a straightforward 68–73 mm shell. citeturn2search1  
Tradeoffs:
- More drivetrain wear (chain/cassette).
- More setup time (chainline, motor clearance, gearing choices).

## Power/battery guidance (off-road)
On private land you can go higher than EAPC limits, but practically for a hybrid frame:
- **48 V + 500–750 W class** is the “fast but still sensible” zone.
- Battery: **48 V, 10–20 Ah** depending on range and how hard you push.

## What I need from you to lock the exact kit choice (no guesswork)
1) Rear brake rotor: **6-bolt or centerlock?** (quick photo works)  
2) Do you want **stealth/quiet** or **max shove**?  
3) Preferred battery mount: **downtube** (best handling) vs **rear rack** (easier fit)

Answer those and I’ll give you a nailed-down shopping list (hub/mid choice, controller current, battery spec, torque arms, brake cut-off sensors for hydraulics, and the “don’t-get-caught-out” install checklist).

[M13] ME (2026-02-21 15:42):
6 yes, best shove, downtube 

[M14] AI (2026-02-21 15:43):
Great — with **6-bolt discs**, **135 mm rear**, **“best shove”**, and **downtube battery**, you’re basically describing the most common “strong but still tidy” hybrid conversion.

## Best-fit build for your 2014 Quick CX 2
### Rear hub motor (48 V, ~750 W class), 700c, cassette/freehub, 6-bolt
Look for a kit explicitly stating:
- **700c / 29er wheel compatible**
- **rear dropout 135–142 mm**
- **disc brake compatible**
- **cassette/freehub** (so you keep your gears)

Example of the typical compatibility language you want to see: “wheel sizes up to 700c” + “dropout spacing 135–142 mm”. citeturn0search5

That spec will give you the “shove” you want without the extra drivetrain wear/chainline fuss of a mid-drive.

## Battery (downtube)
- **48 V (13S) downtube pack**.
- For “best shove” that doesn’t sag instantly: I’d target **~15–20 Ah** and a pack/BMS rated for the controller current you choose (often 25–30 A on 750 W-ish kits).

## Two safety/quality items I’d treat as non-negotiable
### 1) Torque arm (or ideally two)
Hub motors can rotate the axle in the dropout if you don’t restrain it. A proper clamp-style torque arm is the standard fix, and Grin’s torque arms are well regarded and heavily tested in their own documentation. citeturn0search0turn0search2

### 2) Hydraulic brake cut-off sensor (stick-on)
Since you’ve got hydraulic levers, use **magnet + sensor** add-ons so the motor cuts when you brake (no need to swap levers). This is exactly what “ebrake sensors” are for. citeturn1search0turn1search1

## Key compatibility checks (so you don’t buy the wrong kit)
1) **Cassette speeds:** how many gears on the back now (8/9/10)?  
   Buy a motor wheel/freehub that matches (or plan to replace cassette/chain together).
2) **Axle type:** most rear hub kits assume **QR** dropouts (you already said 135 mm, so likely QR — just confirm it isn’t a thru-axle rear).
3) **Rotor size + caliper alignment:** keep your same rotor size; you may need minor caliper adjustment after wheel swap (normal).

## Recommended “best shove” tuning (practical)
- **48 V + 25–30 A controller** is where it starts to feel properly punchy on a hybrid.
- PAS-only is fine; just choose a controller/display that lets you set assist levels sensibly.

If you tell me **rear cassette speed (e.g., 9-speed?)** and **rear axle type (QR vs thru-axle)**, I’ll pin this down to an exact spec (motor winding choice, controller amps, battery minimum discharge/BMS, and whether you should run 1 or 2 torque arms on your frame).

[M15] ME (2026-02-21 15:44):
What’s the rear dropout again?

[M16] AI (2026-02-21 15:44):
The **rear dropout** is the **pair of slots (or holes) at the very back of the frame** where the **rear wheel axle** mounts.

- On a **quick-release (QR)** bike, the dropouts are usually **open-ended slots** you slide the axle into, then clamp with the QR skewer.
- On a **thru-axle** bike, the “dropouts” are more like **closed holes** you line up and pass a thru-axle through.

### What you care about for conversions
1) **Spacing (OLD – over-locknut dimension):**  
   The inside-to-inside distance between the dropouts. You said yours is **135 mm** — that’s the common QR MTB/hybrid rear standard and is ideal for rear hub kits.

2) **Axle style:**  
   - **QR 135×9** (most likely on a 2014 hybrid): open slots + a thin 5 mm skewer.
   - **Thru-axle 142×12**: closed holes + a chunky axle.

### How to check in 10 seconds
- If you see a **little lever** on one side of the rear wheel (QR lever) → **QR dropouts**.  
- If you see a **big bolt/axle head** (often 5–8 mm hex) going through the frame → **thru-axle**.

If you want, snap a quick photo of the rear axle area and I’ll tell you immediately which type you’ve got.

[M17] ME (2026-02-21 15:45):
How much will the kit cost 

[M18] AI (2026-02-21 15:46):
For your **2014 Cannondale Quick CX 2** build (rear hub, 6-bolt disc, downtube battery, “best shove”), you’re typically looking at **~£450 to ~£900 DIY**, depending on kit quality and battery size.

Here’s a realistic breakdown with UK-ish reference prices:

### Core parts
- **Rear hub motor conversion kit (wheel + controller + display + PAS loom):**  
  Budget kits can be ~**£160** (example: Voilamart 48V 1000W rear wheel kit listed at **£159.99**). citeturn4view1  
  Better, more complete / branded kits commonly land **~£250–£450** (varies a lot by motor type, display, waterproof cabling, etc.).

- **Downtube battery (48V):**  
  A common 48V **15Ah Hailong**-style pack is around **£194** (Battery King listing **£194.00**). citeturn1view1  
  Bigger / higher-quality packs (e.g., 17–20Ah, better cells/BMS) are often more.

### Safety / integration bits (don’t skip)
- **Torque arms:** ~**£20+** for a pair is a normal budget line item (example: steel torque arms advertised at **£19.99**). citeturn8search0  
- **Hydraulic brake cut-off sensors (optional but recommended):** typically **~£15–£40** depending on brand/connector style. (Many listings hide price behind scripts, but that’s the usual bracket.)

### What that totals in practice
- **Budget “it moves” build:**  
  £160 (kit) + £194 (battery) + £20 (torque arms) + £20–£40 (odds/sensors) ⇒ **~£400–£450**. citeturn4view1turn1view1turn8search0  
- **More robust “best shove” build (what you’re aiming for):**  
  £300–£450 (better kit) + £250–£450 (bigger/better battery) + £20–£60 (torque arms/sensors/mounting) ⇒ **~£600–£900**.

### If you don’t want DIY
Some UK conversion services quote **~£600** for a “750W / 48V conversion service” including installation (their page shows £600). citeturn4view0  
(Just note: that particular listing text is a bit inconsistent on motor rating in its “what’s included”, so you’d want to confirm exactly what motor/battery you’re getting. citeturn4view0)

If you tell me the **cassette speed (8/9/10)** and the **rotor diameter (160/180)**, I’ll sanity-check which kits will fit cleanly (freehub/cassette, rotor spacing, etc.) and what budget tier actually makes sense for “best shove” without buying twice.

[M19] ME (2026-02-21 15:57):
[image]
[image]
[image]
So you mean the distance between the dropouts? Depends where the measurement is taken. External faces is about 150mm. Internal about 140mm. Some pictures of the bike  
[attached file: 240EF352-1456-41EB-ACF5-79503F8A2B84.jpeg]
[attached file: 72BF025C-49B5-4D82-93B5-3585641BFF3E.jpeg]
[attached file: EF875E05-CE5C-4D81-8F0B-3B7355D1D588.jpeg]

[M20] AI (2026-02-21 15:57):
Yes — **it’s the distance *between the inner faces* of the rear dropouts**, specifically the faces the hub locknuts/end-caps press against. That dimension is commonly called **O.L.D. (Over-Locknut Dimension)** and it’s meant to match your hub’s O.L.D. citeturn0search3turn0search0

### Why your numbers look “too big”
If you’re seeing **~140 mm internal** and **~150 mm external**, you’re almost certainly measuring **at a slight angle**, measuring **outside the actual contact faces**, or the frame is **sprung slightly open** with the wheel out. On a QR hybrid like yours, the *functional* standard is typically **135 mm O.L.D.** for the rear hub/frame interface. citeturn0search0turn0search3

### The most reliable way to confirm (easier than measuring the frame)
Measure the **existing rear wheel hub O.L.D.**:

1) Take the rear wheel out.  
2) Measure **across the hub** from the **outer face of one locknut/end-cap** to the **outer face of the other** (i.e., the faces that sit *inside* the frame dropouts).  
3) That number is the hub O.L.D. — and your frame spacing will match it when clamped. citeturn0search3turn0search0

If your bike is truly 135-QR (as expected), you’ll read **~135 mm** on the hub.

### If you want to measure the frame properly
- Remove wheel.
- Measure **between the inner dropout faces**, **right where the axle sits** (the flat “seat” surfaces).
- Don’t pull the stays apart to get the ruler in — just touch the ruler to the faces lightly. citeturn0search1turn0search2

### What I can see from your photos
- You’ve got a **quick-release rear wheel** (not thru-axle) and **6-bolt rotor**, which fits the “standard” rear hub conversion ecosystem nicely.

If you tell me how many speeds your cassette is (looks like **9-speed-ish** from the stack, but I won’t guess), I’ll tell you exactly what freehub compatibility to buy (8/9/10-speed HG, etc.).

[M21] ME (2026-02-21 16:02):
[image]
What’s cassette speed?
[attached file: 435A64C3-6601-4474-845B-B0328584FBCC.jpeg]

[M22] AI (2026-02-21 16:03):
“Cassette speed” just means **how many sprockets (cogs) are on the cassette** — e.g. **9-speed = 9 cogs** on the back wheel.

### How to tell on your bike (quick + foolproof)
1) Look at the rear cassette.
2) **Count the cogs** (easiest if you rotate the wheel slowly and count each distinct sprocket).
3) That number is your “speed”.

### For your 2014 Cannondale Quick CX 2
Your model is commonly specced with a **Shimano 9-speed cassette** (e.g., Shimano HG200 11–34 9-speed on retailer spec sheets, and Shimano HG30 9-speed on BikeIndex entries for the 2014 Quick CX 2). citeturn0search2turn0search4

So: **very likely 9-speed**.

### Why it matters for an e-bike hub kit
You want a rear hub motor wheel with a **Shimano HG-compatible freehub** that will take a **9-speed cassette** (most do). If you accidentally bought a freewheel-type motor, you’d be fighting compatibility.

If you want, take a quick photo of the cassette from the **right-hand side** (no spokes blocking) and I’ll confirm the count instantly.

[M23] ME (2026-02-21 16:04):
What’s the rotor?

[M24] AI (2026-02-21 16:04):
On your bike, the **rotor** is the **round metal disc** bolted to the wheel hub that your **disc brake caliper clamps onto** to slow/stop the wheel.

In your photos, that shiny circular plate next to the rear hub is the **brake rotor**.

### Two rotor details that matter for an e-bike hub kit

**1) Mount type**
- You have a **6-bolt rotor** (you can see the 6 small bolts around the rotor’s centre).

**2) Rotor diameter (size)**
Common sizes are **160 mm**, **180 mm**, **203 mm**.

How to measure it properly:
- Measure **straight across the disc** from outer edge to outer edge.
- If you only have a ruler: measure radius (centre to edge) and **double it**.

Rule of thumb visually:
- 160 mm looks “medium” and is the most common on hybrids.
- 180 mm looks noticeably larger and closer to the caliper mount.

If you tell me the diameter (or show a close-up with a ruler against the disc), I’ll tell you whether you can reuse your existing rotor as-is on the new motor wheel (almost always yes if it’s 6-bolt and same diameter).

[M25] ME (2026-02-21 16:06):
11 speed, disc brake 150mm. Single Flywheel cog 130mm

[M26] AI (2026-02-21 16:06):
I think you’ve got **three different standards mixed together** there — totally normal when you’re eyeballing it the first time.

## 1) “11 speed”
If you truly have **11 cogs on the back**, that’s an **11-speed cassette**.

But on a **2014 Cannondale Quick CX 2**, 11-speed is *unlikely* as original spec (those were typically 8/9/10-speed era). What often happens is people count:
- cogs **+ a spacer**
- or miscount because the smallest cogs blend together

**How to confirm properly:** count the cogs, but also look for markings on the biggest sprocket or lockring (often says something like “11-34T” and sometimes “9S / 10S / 11S”).

## 2) “Disc brake 150mm”
**150 mm rotors are very uncommon** on bikes. The standard common sizes are **160 / 180 / 203 mm**.

What *is* common is measuring **from near the caliper to the far edge** (not true diameter) or measuring at an angle.

**Correct rotor measurement:** measure **outer edge to outer edge straight across the disc**.  
Chances are you’ll find it’s **160 mm**.

## 3) “Single flywheel cog 130mm”
A **single “flywheel cog”** describes a **freewheel** (screws on) or a **single-speed** setup.

But your photos clearly show a **multi-sprocket stack** (a cassette) and a derailleur — so you’re not on a single cog system.

The **130 mm** number is also a classic **road rear dropout spacing**. Your frame/wheel style looks far more like **135 mm QR** (which you said earlier), and your “internal 140 / external 150” measurement suggests you weren’t on the true inner faces.

## What matters for your hub-motor kit (practical)
For a rear hub motor wheel you want:
- **135 mm QR rear hub motor**
- **6-bolt disc mount**
- **cassette/freehub type (HG)** (not a screw-on freewheel motor)

Most rear hub kits use a Shimano **HG** freehub that happily takes **8/9/10-speed** and *some* 11-speed (depends on which 11-speed cassette you have).

## Do this and you’ll know for sure in 2 minutes
1) **Rotor diameter:** put a ruler across the rotor and read the diameter (likely 160).  
2) **Cassette speed:** count cogs again, then look for “9S/10S/11S” marking on cassette/lockring if present.  
3) **Hub OLD:** measure the **existing rear hub** end-to-end across the locknuts/end caps — if it’s ~135 mm, buy 135 mm.

If you can send one clear photo of the cassette from the **right-hand side** (no spokes blocking) and one of the rotor with a ruler across it, I’ll call all three (cassette speed, rotor size, and hub spacing) with high confidence.

[M27] ME (2026-02-21 17:10):
[image]
[image]
[image]
[image]
[image]
[image]
11 cigs at the rear
1 cog at pedal crank 
Ruler shown 
[attached file: F8D11377-6295-49D0-AA29-5C39345D8D04.jpeg]
[attached file: 9FBB8045-B94D-45D1-842C-01BD7A65C854.jpeg]
[attached file: 3FAF53E9-0652-4FDB-9033-47274AE33C92.jpeg]
[attached file: 9E8A2E1C-002A-411B-9715-3ACB5702473D.jpeg]
[attached file: BB23D50F-CF51-4D92-BA6D-61CE702D5476.jpeg]
[attached file: A1B63C15-C4A0-44BD-9863-EDCCFD2D5EEE.jpeg]

[M28] AI (2026-02-21 17:14):
Yep — you’ve got a **1× drivetrain**: **1 chainring at the crank** (your SRAM X-Sync ring) and you’re saying **11 cogs at the rear**, i.e. **1×11**.

### Rotor size: why you’re reading ~150 mm
Your ruler photo is sitting *near* the rotor edge, but it isn’t measuring **true diameter edge-to-edge across the centre**. Also, **150 mm isn’t a common MTB/hybrid rotor size**; the usual “close” standard is **160 mm** (and then 180/203 etc.). citeturn1search4turn1search1

So in practice: **treat your rotor as almost certainly 160 mm** unless you measure it properly.

**How to measure rotor diameter correctly (10 seconds):**
- Put the ruler straight across the disc **through the hub centre** and read **outer edge to outer edge**.
- Or measure **centre → edge** (radius) and double it.

### 11-speed cassette compatibility with hub-motor kits
Most rear hub motor wheels come with a **Shimano HG-type freehub**. Good news: many **11-speed MTB cassettes that start with an 11-tooth** sprocket fit HG bodies just fine. citeturn0search0turn0search1turn0search4

The only “gotcha”:
- If your cassette is an **XD driver** type (often **10T smallest cog**), it **won’t** fit a normal HG freehub.

**Quick check:** look at the **smallest rear sprocket**:
- If it’s **11T** → you’re almost certainly **HG**, which is what you want.
- If it’s **10T** → you’re likely **XD**, and you’ll need a different plan.

### Where this leaves your conversion spec (still the right path)
For your bike: **rear hub motor wheel, 135 mm QR, 6-bolt disc, HG freehub** + downtube battery + torque arm(s).

If you can snap one more photo of the cassette where I can see the **smallest cog tooth count (10T vs 11T)**, I’ll tell you definitively whether a standard HG hub-motor wheel will take your exact cassette.

[M29] ME (2026-02-21 17:25):
11t

[M30] AI (2026-02-21 17:25):
Perfect — **11T smallest cog** means your cassette is almost certainly **HG-compatible** (not XD). So you can buy a rear hub motor wheel with a **standard Shimano HG freehub** and either:

- **move your existing 11-speed cassette across**, or  
- fit a new HG 11-speed cassette if you fancy fresh drivetrain parts.

### What to buy (now we can be specific)
For your Cannondale Quick CX (QR rear):
- **Rear hub motor wheel:** **700c**, **135 mm QR**, **6-bolt disc**, **HG freehub**
- **Battery:** **48 V downtube** (for “best shove”)
- **Controller:** typically **25–30 A** if you want punch (and battery/BMS must support that)
- **Torque arm(s):** at least one, ideally two at higher torque

### Small note on “11-speed fit”
HG freehubs generally take **8/9/10** and most **11-speed MTB (11–xx)** cassettes. If yours is an 11-speed MTB cassette (it is, given 1×11 + 11T), you’re in the safe zone.

### Rotor
Assume your rotor is **160 mm** unless you measure edge-to-edge across centre and prove otherwise. The practical point: you can reuse your existing **6-bolt rotor** on the new motor wheel, as long as the diameter matches.

If you tell me your rear cassette’s **largest sprocket tooth count** (e.g. 42T/46T/50T — it’s usually printed on it), I can suggest whether you’d be better with a hub motor or a mid-drive for “best shove” on hills, and what controller current is sensible before it starts eating chains/cassettes.

[M31] ME (2026-02-21 17:29):
42t

[M32] AI (2026-02-21 17:29):
42T largest + 11T smallest means you’re running a **1×11 “11–42” MTB cassette**, which is a very normal range.

### What it implies for the e-hub kit (good news)
- **11–42 cassettes commonly fit a standard Shimano HG freehub** (i.e., the freehub most rear hub-motor wheels come with). citeturn1search4turn1search1  
- So your earlier plan still stands: **rear hub motor wheel, 135 mm QR, 6-bolt rotor mount, HG freehub**.

### What it implies for “best shove”
- With **11–42**, you already have a decent low gear for hills (42T bailout), so a **rear hub motor** will feel punchy without you needing to rework gearing immediately.
- If you go **48 V + ~750 W class + 25–30 A controller**, that’s typically the “proper shove” zone on a hybrid/MTB drivetrain (battery/BMS must support the current).

### Rotor sanity check
Your rotor almost certainly isn’t “150 mm” as a standard size; common sizes you’ll see listed are **160/180/203 mm** (among others). citeturn0search1  
So assume **160 mm** unless you measure edge-to-edge through the hub centre.

### Bottom line shopping spec (based on everything you’ve confirmed)
- **Rear hub motor wheel:** 700c, **135 mm QR**, **6-bolt**, **HG freehub**
- **Battery:** 48 V **downtube**
- **Extras:** torque arm(s) + hydraulic brake cut-off sensor (recommended)

If you tell me **rear rotor diameter (likely 160)** and whether your rear axle is definitely **QR** (it looks QR in your photos), I can point you at the exact kit descriptors to look for so you don’t accidentally buy a **freewheel** motor wheel or the wrong rotor interface.

[M33] ME (2026-02-21 23:22):
Yes 160 and qr 

[M34] AI (2026-02-21 23:24):
Nice — with **QR rear + 135 mm + 6-bolt + 160 mm rotor + HG cassette (11–42, 11T smallest)** you’re in the “easy path” for rear hub kits.

### Typical DIY cost for your exact setup (UK prices I can actually see)
**Core kit (rear hub motor wheel + controller/display/PAS)**
- **~£160** for a budget rear-hub kit (Voilamart example shows **£159.99** for a 48V 1000W rear wheel kit on their site; their 700c version is typically the same ballpark when in stock). citeturn4view0  
- **~£350** for a more “branded / tidy harness / nicer display choices” rear hub kit (ElectroCity’s Bafang 48V rear hub *cassette* kit shows **£349.99**). citeturn10view2  

**Battery (48V downtube)**
- A common Hailong-style **48V 15Ah downtube** pack is **£189** (Battery King). citeturn9view1  
(Go bigger capacity and/or higher current BMS and you’ll pay more, but £189 is a good reference point.)

**Must-have safety item**
- **Torque arms**: **£19.99** for a pair (Lively E-Bike listing). citeturn11view0  

**Recommended with hydraulic discs**
- **Brake cut-off sensors**: I can see **£11.66 each** on an eBay UK listing (so ~£23 for a pair). citeturn4view3  

### What that totals in practice
- **Budget “it rips” build:**  
  £160 (kit) + £189 (battery) + £20 (torque arms) + £23 (brake sensors) + ~£20–£50 misc (cable wrap, mounts, connectors)  
  **≈ £410–£440** citeturn4view0turn9view1turn11view0turn4view3

- **Nicer kit / better integration build:**  
  £350 (kit) + £189 (battery) + £20 + £23 + misc  
  **≈ £580–£630** citeturn10view2turn9view1turn11view0turn4view3

### Quick buying checklist (so you don’t get the wrong rear wheel)
Look for these exact phrases/specs:
- **Rear hub motor, 700c**
- **135 mm QR**
- **Cassette / HG freehub** (not “freewheel”)
- **6-bolt disc mount**
- Controller current **25–30A** if you really want “best shove” (and ensure the battery/BMS supports it)

If you tell me whether you’d prefer **500–750W “strong but sensible”** or **1000W “maximum shove”**, I’ll steer you to the safest current/battery/BMS pairing so you don’t end up with a battery that sags or a dropout that gets abused.

[M35] ME (2026-02-22 09:24):
1000w

[M36] AI (2026-02-22 09:25):
1000 W is doable on your Quick CX (QR/135 mm/6-bolt/160 mm/HG 11-42), but it moves you into the zone where **current, torque reaction, and heat** matter more than the “headline watts”.

## What “1000 W” usually means electrically
Most 48 V “1000 W” kits are paired with controllers around **35 A** (48 V × 35 A ≈ 1680 W peak electrical; continuous is lower). You’ll see 48 V 1000–1500 W controllers sold as **35 A** units. citeturn0search0turn0search3

## Battery spec you should target (so it actually *shoves*)
For a 35 A controller, pick a 48 V downtube battery with:
- **BMS continuous discharge ≥ 30 A** *minimum* (better: 35–40 A if available)
- decent cells (sag is what makes “1000 W” feel like “meh”)

It’s common to see 48 V Hailong packs marketed for 1000 W with a **30 A BMS**. citeturn0search1

## Dropout / torque arm is non-negotiable at 1000 W
At these torque levels, a hub motor can try to **spread/chew the dropouts** if the axle rotates even slightly. Grin quantify the forces: e.g. **40 N·m at a 12 mm axle can translate to ~1000 lb spreading force on each dropout**. That’s why a proper torque arm (ideally **two**) is the right mindset for a 1 kW hub build. citeturn1search2

## Your confirmed fitment checklist (you’re in good shape)
You want a rear hub kit described as:
- **Rear hub motor wheel, 700c**
- **135 mm QR**
- **6-bolt disc**
- **HG/freehub for cassette** (NOT “freewheel”)
- Works with **11-speed MTB 11–42** (your 11T smallest makes HG compatibility likely)

## Practical cautions (worth taking seriously)
- **Braking:** 160 mm rotors work, but with 1 kW you’ll be glad of excellent pads/rotors and perfect caliper alignment.
- **Wheel build:** hub motors stress spokes; avoid bargain “mystery” wheels if you’ll ride hard.
- **Heat:** long climbs at low speed are where hub motors cook; mid-drives handle that better (but eat drivetrains).

## UK note (because it bites people)
If you ever use it on public roads, UK EAPC rules are **250 W continuous** and **assist cut-off 15.5 mph**; anything beyond is treated as a motor vehicle. citeturn1search0turn1search1

If you tell me whether you want **48 V 35 A** (typical “1 kW kit feel”) or you’d rather cap it to **30 A** for battery/frame sympathy, I’ll translate that into a clean “buy this spec” list (battery Ah + BMS current, controller current, torque arm count, and the exact wording to look for on listings).

[M37] ME (2026-02-22 09:26):
30a

[M38] AI (2026-02-22 09:26):
30 A is a sensible call for **“strong shove”** without going full dropout-abuse / battery-sag territory.

## What 30 A means in practice (48 V system)
- **Peak electrical input** ≈ 48 V × 30 A = **~1440 W** (real-world peak; “1000 W” is usually the *nominal* marketing label).
- You’ll still get a big jump in punch vs legal 250 W, but with less heat and less axle torque than 35–40 A setups.

## The spec to buy for your bike (now fully defined)
Given your confirmed hardware: **QR rear, 135 mm, 6-bolt, 160 mm rotor, HG 11-speed (11–42)**:

### Controller
- Look for a **KT-series 48 V 30 A controller** (commonly 12-MOSFET) sold as suitable for **1000–1500 W motors**. citeturn0search3turn0search4

### Battery
Minimum you want:
- **48 V downtube battery with a 30 A BMS** (continuous).  
Example: Battery King’s 48 V 15Ah Hailong downtube pack explicitly states a **smart 30A BMS** and is marketed for 1000 W. citeturn0search1turn0search2

Capacity guidance:
- **15 Ah** = decent, cost-effective baseline
- **17.5–20 Ah** = noticeably less voltage sag, better sustained shove

### Motor wheel
- **Rear hub motor wheel**: **700c**, **135 mm QR**, **6-bolt**, **HG cassette freehub** (so your 11-speed 11–42 moves over cleanly).

### Torque arms
At 30 A, treat torque arms as mandatory:
- **At least one**, and if you ride hard / off-road lots, **two** is the conservative engineering choice.

## Budget expectation (with 30 A controller)
- Kit + controller/display/PAS: often **~£250–£450** depending on brand/harness quality.
- 48 V 15Ah downtube (30A BMS): **~£189–£200** range is common from UK sellers. citeturn0search1turn0search2
- Torque arms + brake sensors + misc: **~£40–£80**.

So you’re typically **~£500–£750 DIY** for a “30 A, properly done” build (battery quality and kit tier drive the range).

## One last detail to avoid an expensive mismatch
Your kit and battery must match connector “ecosystem”:
- KT controllers often use specific waterproof harnesses and display connectors.
- Batteries vary (XT60/Anderson/bullet, etc.). Plan either matched connectors or a proper adapter.

If you tell me whether you want a **simple PAS bike (no throttle)** with a **basic display**, or you want **programmable KT display settings**, I’ll give you a tight “buy these keywords” list so every connector and part standard lines up first time.
