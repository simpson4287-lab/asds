# Harwell Radiation Facility Info
Date (UTC): 2026-05-15 08:18
Conversation ID: 6a06d6cc-dfd4-83eb-8eb9-51723bea8027
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-05-15 08:18):
Lookup harwell radiation facility 

[M2] AI (2026-05-15 08:18):
The main modern “Harwell radiation facility” people usually mean today is the radiation-effects and irradiation capability based at the entity["organization","Harwell Campus"] in Oxfordshire, particularly the work done by entity["company","Radtest Ltd"] (formerly Cobham RAD Europe).

A few key links:

- urlHarwell Irradiation Facility overviewturn0search0
- urlRadtest Ltd official siteturn0search1
- urlHarwell Campus listing for Radtestturn0search2

What they actually provide:

- Cobalt-60 gamma irradiation
- Total ionising dose (TID) testing
- Single event effects (SEE) support
- Electron beam irradiation
- Ion beam and neutron test coordination via partner facilities
- Radiation testing for:
  - space electronics
  - nuclear industry hardware
  - medical systems
  - high-energy physics instrumentation
  - defence systems

The Harwell site historically was the UK’s main atomic research establishment, the old entity["organization","Atomic Energy Research Establishment"]. citeturn0search4turn0search5

For your sort of interests (CCD systems, fibre links, electronics survival, neutron/gamma effects), the important distinction is:

- Harwell/Radtest itself is especially known for **gamma total dose** and general radiation-effects expertise.
- For heavy neutron or proton SEE campaigns, they often broker or coordinate testing at accelerator facilities elsewhere in Europe. citeturn0search1turn0search8

The capability summary from the Harwell irradiation page is actually pretty strong technically:
- temperature-controlled irradiation
- vacuum/gas environments
- powered/biased electronics during exposure
- long-duration endurance testing
- 24/7 irradiation campaigns citeturn0search0

For space-style electronics qualification, that combination is genuinely valuable because you can run:
- powered FPGA boards
- fibre transmitters
- CCD support electronics
- bias supplies
- long cable harnesses

…while logging drift/failure behaviour live during dose accumulation.

If you want, I can also dig into:
- what facilities they use for neutron SEE specifically
- typical pricing/order-of-magnitude costs
- how a real radiation campaign is structured
- what kinds of electronics usually fail first under gamma vs neutron
- whether they have published data on optical transceivers/fibre links/ADCs/FPGAs.

[M3] ME (2026-05-15 08:20):
If I a cnosnimaging sensor and I wanted togice it the max they can do what would my plan kiik kike 

[M4] AI (2026-05-15 08:20):
I’ll treat this as: “If I had a CMOS imaging sensor and wanted to give it the maximum irradiation Harwell can provide, what would the test plan look like?” I’ll check current facility details rather than relying on memory, then map that into a practical campaign.

[M5] AI (2026-05-15 08:20):
Yes — for a **CMOS imaging sensor**, your “maximum Harwell/Radtest” plan would look like a **powered Co-60 gamma TID campaign to failure**, not just a passive soak.

Radtest state Co-60 total dose testing from ELDRS low dose rates up to high dose rates, with in-situ monitoring and temperature control; their brochure quotes dose rates from background to **several kGy/hour**. citeturn293587search0turn293587search2

## Practical test plan

**1. Define the aim**

> “Expose the CMOS imaging sensor and representative readout electronics to the maximum practical Co-60 gamma total ionising dose available, under powered operating conditions, while monitoring image performance until parametric failure or functional loss.”

**2. Test articles**

Use at least:

| Item | Purpose |
|---|---|
| 1 unirradiated control sensor | Baseline/reference |
| 1 biased/static sensor | Powered but not imaging |
| 1 live imaging sensor | Best real-use case |
| optional spare | Continue beyond first failure |

**3. Pre-test characterisation**

Before irradiation, record:

- dark current vs exposure time
- bias current consumption
- full-frame image quality
- stuck/hot pixel count
- read noise
- offset/baseline drift
- gain/linearity
- ADC/readout stability
- temperature dependence if relevant

**4. Irradiation mode**

For “maximum they can do”, ask for:

- **Co-60 gamma**
- **highest available dose rate compatible with your fixture**
- sensor **powered during exposure**
- continuous or periodic readout
- temperature-controlled chamber if possible
- cables/feedthroughs for bias, clocks, trigger, data and monitoring

**5. Dose stepping**

Do not just blast it once. Step it so you learn where it degrades.

Example:

| Step | Cumulative dose |
|---|---:|
| Baseline | 0 |
| Step 1 | 100 Gy |
| Step 2 | 300 Gy |
| Step 3 | 1 kGy |
| Step 4 | 3 kGy |
| Step 5 | 10 kGy |
| Step 6 | 30 kGy |
| Step 7 | 100 kGy |
| Continue | until failure / facility limit / project limit |

For a brutal exploratory campaign, you could say: **continue to functional failure or maximum achievable booked dose**.

**6. Live monitoring**

During irradiation, log:

- sensor supply currents
- bias rail currents
- frame output
- dark frames
- fixed pattern noise
- hot pixel growth
- readout errors
- latch-up/current excursions
- temperature
- cumulative dose and dose rate

**7. Failure criteria**

Define failure before test:

- no image output
- supply current exceeds safe limit
- dark current unusable
- hot pixels above threshold
- read noise above threshold
- image artefacts unacceptable
- communication/readout failure
- latch-up or non-recoverable reset event

**8. Post-irradiation**

After each major dose step, repeat full characterisation. Then check annealing:

- immediately after exposure
- after 24 hours
- after 1 week
- optionally after elevated-temperature anneal

## What to ask Harwell/Radtest

Send something like:

:::writing{variant="email" id="58420" subject="CMOS imaging sensor Co-60 TID test enquiry"}
Hello,

We are interested in irradiating a CMOS imaging sensor using Co-60 gamma exposure at the highest practical total dose and dose rate available.

The intent is a powered, in-situ total ionising dose test, ideally with the sensor biased and operating during exposure while we monitor image output, supply currents, temperature, and cumulative dose.

We would like to understand:

1. The maximum available Co-60 dose rate for a small electronics/sensor test article.
2. The maximum practical total dose achievable during a campaign.
3. Available feedthroughs for power, clocks, bias, trigger and data cabling.
4. Whether temperature-controlled irradiation is available.
5. Whether in-situ image/data monitoring is practical.
6. Recommended dosimetry method and sensor mounting arrangement.
7. Any constraints on powered electronics, cables, or support equipment near the irradiation position.

The proposed test article is a CMOS imaging sensor with representative readout electronics. We are initially interested in a step-stress campaign to characterise degradation up to failure or facility limit.

Kind regards,
Chris
:::

The key phrase is **“powered in-situ Co-60 TID test to failure”**. That tells them you do not just want a passive dose certificate; you want degradation data.

[M6] ME (2026-05-15 08:22):
What's the unit?

[M7] AI (2026-05-15 08:22):
For radiation testing like this, the main unit is the **Gray**.

genui{"math_block_widget_always_prefetch_v2":{"content":"1\\ \\mathrm{Gy} = 1\\ \\mathrm{J/kg}"}}

That means:
- **1 Gray (Gy)** = 1 joule of absorbed radiation energy per kilogram of material.

For electronics and imaging sensors you will commonly see:

| Unit | Meaning |
|---|---|
| Gy | Gray |
| kGy | kilogray = 1000 Gy |
| MGy | megagray = 1,000,000 Gy |

Older papers often use:
- **rad**
- **krad**
- **Mrad**

Conversion:

genui{"math_block_widget_always_prefetch_v2":{"content":"100\\ \\mathrm{rad} = 1\\ \\mathrm{Gy}"}}

So:

| Old | Modern |
|---|---|
| 1 krad | 10 Gy |
| 100 krad | 1 kGy |
| 1 Mrad | 10 kGy |

Space/electronics people still very often talk in:
- “100 krad”
- “1 Mrad TID”

even though SI units are technically Gy now.

For CMOS sensors specifically:
- a few Gy → often negligible
- tens to hundreds of Gy → dark current/hot pixels start becoming noticeable
- kGy range → serious degradation
- tens of kGy+ → many commercial sensors become heavily impaired or fail

The *rate* of exposure is separate:
- Gy/hour
- krad/hour
- etc.

So a facility might say:
- “dose rate = 5 kGy/hr”
- “total dose = 30 kGy”

meaning:
- it accumulates at 5 kGy every hour
- until the part has absorbed 30 kGy total.
