# Radiation Effects on Fibres
Date (UTC): 2026-05-14 15:43
Conversation ID: 6a05eda7-788c-83eb-be1c-0a59db7f1a4b
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-05-14 15:43):
[attached file: UKAEA-CCFE-CP2512.PDF]

[M2] AI (2026-05-14 15:43):
Yes — that paper is predominantly about the fibre behaviour itself, not the optoelectronic transceiver electronics. fileciteturn0file0L5-L13

The experiment was essentially:

- place a 60 m silica fibre coil near the JET fusion machine,
- expose it to intense neutron + gamma fields,
- remotely monitor optical transmission and induced emission during DT plasma shots. fileciteturn0file0L6-L13

The actual optical transmitter/receiver arrangement was comparatively conventional and mostly outside the biological shield. They specifically mention:

- broadband light source,
- compact spectrometer,
- remote measurement via transfer fibres outside shielding. fileciteturn0file0L6-L13

The radiation study focus is therefore:

- radiation-induced attenuation (RIA),
- Cherenkov/radiation-induced emission (RIE),
- wavelength dependence,
- self-annealing behaviour,
- neutron/gamma dose effects on transmission. fileciteturn0file0L8-L13

It is not really a study of:
- VCSEL survivability,
- laser diode degradation,
- photodiode damage,
- SERDES/LVDS optical modules,
- FPGA optical links,
- COTS transceiver failure modes.

That distinction matters for your application.

For your earlier question — “is this just about the fibre tube itself?” — the answer is essentially:
- yes, mainly the glass fibre medium and its optical attenuation behaviour under fusion radiation,
- not the active electro-optic conversion electronics.

What the paper *does* give you, though, is an important systems insight:

- the fibre itself may survive surprisingly well at longer wavelengths (>800 nm),
- especially if you can tolerate some attenuation,
- whereas active optoelectronics are often the weaker radiation point in the chain.

They explicitly conclude that even unheated low-OH SiO₂ fibre showed “remarkable resistance” above 800 nm. fileciteturn0file0L13-L13

That aligns with why many harsh-environment architectures do this:

1. Put only a minimal optical transmitter near the radiation zone.
2. Get onto fibre immediately.
3. Move all intelligent electronics outside shielding.

For your disposable-module concept, that’s probably the right direction architecturally.

A few practical implications from the paper for your case:

- 850 nm / 1064 nm style links are preferable versus blue-visible wavelengths.
- Pure silica core fibres can be very robust.
- Neutron damage recovery/self-annealing is real and significant (~95% transient recovery reported). fileciteturn0file0L11-L13
- The fibre may not be your dominant lifetime limiter.
- The transmitter laser and receiver TIA/SERDES likely become the dominant risk items.

So if you are designing a “sacrificial” radiation campaign link, the likely hierarchy is:

LVDS → simple serializer (optional) → rad-tolerant laser driver/VCSEL → fibre → normal receiver outside shield.

Not:
- full Ethernet PHYs,
- complex optical networking stacks,
- standard datacentre optics sitting in-core.

Also important: neutron environments are usually much harder on active semiconductor junctions than gammas alone. Your earlier instinct about “the tube itself” being comparatively durable is directionally correct. The fibre glass is often surprisingly resilient compared with the active silicon/III-V devices attached to it.

[M3] ME (2026-05-14 15:44):
Is there a paper anywhere about transmit534s?

[M4] AI (2026-05-14 15:44):
I think you may mean “transceivers” generally rather than a specific “Transmit534” device — I can’t find a recognised radiation/space/fusion optical part with that exact name.

What I *can* find is:
- generic SFP-534 commercial fibre modules (ordinary telecom/datacentre optics), which are not radiation-focused, citeturn0search0turn0search3
- and a number of papers on radiation-tolerant or space optical transceivers more broadly. citeturn0search6turn0search5

For your application, the most relevant direction is probably:
- radiation-tolerant optical links,
- space photonics,
- fusion diagnostics fibre systems,
- or rad-hard SERDES/optical transceiver architectures.

A particularly relevant recent paper is:

- “Reconfigurable Silicon Photonic Transceiver for Space-Based …” — which discusses integrated photonic transmitter/receiver structures for harsh environments and high-speed optical links. citeturn0search6

That’s much closer to:
- what survives radiation,
- how optical modulation is implemented,
- BER behaviour,
- optical carrier wavelengths,
- receiver sensitivity,
than the JET fibre paper.

Your earlier instinct is still broadly correct:
- passive fibre is often comparatively robust,
- active electro-optic conversion is usually the fragile part.

The weak points are typically:
- laser threshold drift,
- VCSEL degradation,
- photodiode dark current rise,
- TIA noise increase,
- PLL/SERDES upset,
- SEU/SEL in digital logic.

Not the silica fibre itself.

If you want, I can also search specifically for:
- rad-hard VCSEL papers,
- CERN optical links,
- ESA/NASA space transceivers,
- fusion diagnostic optical links,
- neutron-tested SFPs,
- or “minimal LVDS-to-fibre transmitter” architectures suitable for disposable irradiation modules.

[M5] ME (2026-05-14 15:44):
Transmitters

[M6] AI (2026-05-14 15:44):
Yes — there are quite a few papers specifically on radiation-tolerant optical transmitters and VCSEL-based links.

The main keyword space you want is:

- VCSEL radiation hardness
- optical link radiation tolerance
- rad-hard optical transceiver
- ATLAS optical links
- space optical interconnects
- neutron irradiation of VCSELs

The CERN / particle physics world is actually one of the best sources because they run optical transmitters inside intense neutron/proton environments continuously.

Some particularly relevant papers:

1. “Neutron and gamma irradiation studies of packaged VCSEL emitters…”  
This is very close to what you were asking. It tested VCSEL optical transmitters under neutron and gamma exposure for the ATLAS detector. citeturn0search0turn0search1

Key findings:
- only ~10–15% attenuation after neutron exposure,
- threshold current barely changed,
- partial recovery/annealing occurred after drive current conditioning. citeturn0search0

2. “Radiation-Hard Opto-Link for the Atlas Pixel Detector”  
Discusses complete optical transmitter/receiver chains using:
- VCSEL arrays,
- PIN receivers,
- rad-hard driver ASICs,
- optical fibre links. citeturn0academia11turn0academia13

This is probably the closest architectural analogue to your “disposable module near radiation source” concept.

3. “VCSEL-based Array Optical Transmitter (ATx)”  
Modern radiation-tolerant multi-channel optical transmitter modules for collider detectors. citeturn0search2turn0academia10

These are:
- compact,
- high-density,
- explicitly designed for hostile radiation environments.

4. “112 Gb/s Radiation-Hardened Optical Transceiver”  
More space-focused, but useful because it discusses:
- RHBD techniques,
- VCSEL drivers,
- TIA hardening,
- SEE mitigation. citeturn0search9

For your application specifically, the important thing is this:

The optical transmitter itself is not usually “just a bright photodiode”.

A transmitter chain normally contains:
- serializer,
- PLL/clocking,
- laser driver,
- VCSEL/laser,
- monitoring photodiode,
- bias control loops.

The actual laser junction may survive surprisingly well.
Often the supporting electronics fail first.

That is why minimal architectures are attractive in fusion/radiation work:
- LVDS directly into simple laser driver,
- no Ethernet PHY,
- no packet stack,
- minimal digital complexity,
- move recovery/deserialization outside shielding.

The CERN designs strongly follow that philosophy. citeturn0search1turn0academia11

The other interesting point from the papers:
- VCSELs often degrade gracefully rather than catastrophically.
- Optical power drops,
- threshold current rises,
- BER worsens,
- but the device may still function long after spec degradation. citeturn0search0turn0search4

That makes them very suitable for:
- sacrificial campaigns,
- calibration rigs,
- temporary irradiation instrumentation,
- fusion diagnostics near-vessel links.

[M7] ME (2026-05-14 15:51):
Can you find these in the market?

[M8] AI (2026-05-14 15:51):
Yes — but there’s an important split between:

1. **true rad-hard / rad-tolerant optical transmitters**  
2. ordinary commercial fibre modules that people experimentally use in radiation environments.

The genuinely radiation-qualified parts are mostly aerospace, CERN, defence, or satellite market devices — not normal DigiKey/Amazon parts.

For your kind of fusion instrumentation work, the most realistic route is often:
- use reasonably robust COTS optics,
- keep them close to shielding boundaries,
- accept they are sacrificial/replaceable.

The “fully rad-hard” parts become very expensive very quickly.

The most relevant commercially obtainable families I found are:

### Space / rad-tolerant optical transceivers

- urlSmiths Interconnect SpaceABLE optical transceiversturn0search0  
These are genuine space-oriented radiation-tolerant parallel optical transceivers. citeturn0search0

- urlReflex Photonics / SpaceABLE platformturn0search0  
Used in satellites and harsh-environment optical interconnects. Multi-lane VCSEL architecture. citeturn0search0

### CERN / detector style architectures

- urlATLAS radiation-hard opto-link paperturn0academia14  
Not a shop listing, but this is one of the canonical examples of real deployed radiation optical transmitters. citeturn0academia14

These systems used:
- VCSEL arrays,
- PIN receivers,
- rad-hard ASIC drivers,
- hybrid optical boards.

That architecture is probably closer to what you actually want than a normal SFP.

### Practical “engineering compromise” options

These are *not* radiation hardened, but are cheap enough to treat as disposable:

| Type | Typical Use | Approx Cost | Comment |
|---|---|---:|---|
| entity["turn0product19","Cisco SFP-10G-SR-S= Transceiver Module"] | 10G VCSEL MMF | ~£20–40 refurb | Common, robust, easy to source |
| entity["turn0product3","10G SFP+ SR Multimode Transceiver"] | Generic VCSEL SFP+ | ~£15 | Good for experimentation |
| entity["turn0product14","TP-Link SM311LS Fiber Module"] | 1G optical module | ~£20 | Very cheap sacrificial testing |
| entity["turn0product23","XZSNET 1000BASE-LX SFP Transceiver"] | 1310 nm SMF | ~£16 | Longer wavelength advantage |

For your stated “disposable module” idea, this may actually be the sweet spot:
- £15–50 optics,
- mounted near shield penetration,
- fibre immediately exits hostile zone,
- everything intelligent stays outside.

That is often far more economically sensible than:
- £5k–£50k true rad-hard space photonics.

The important thing is that you do *not* need Ethernet necessarily.

You can use:
- serializer/deserializer,
- Aurora,
- custom LVDS framing,
- even raw encoded data streams,
and simply transport over optical hardware.

The other key observation from the papers:
- VCSEL emitters themselves often survive better than expected,
- especially for cumulative dose,
- while support electronics degrade first. citeturn0search1turn0academia14

So if you minimise:
- PLLs,
- DSP,
- protocol stacks,
- management ICs,
you improve survivability dramatically.

The most robust architecture for your kind of instrumentation is probably something like:

FPGA LVDS  
→ simple serializer  
→ laser driver  
→ VCSEL/SFP cage  
→ fibre  
→ everything else remote.

Not:
- Ethernet PHY,
- Linux endpoint,
- managed optical networking.

The CERN detector world repeatedly converged on that same philosophy. citeturn0academia14turn0search1

[M9] ME (2026-05-14 15:53):
Looking for that Honeywell part

[M10] AI (2026-05-14 15:53):
I think the Honeywell part you were probably remembering is not a complete optical SFP-style transceiver, but one of Honeywell’s radiation-hardened SERDES/link IC families.

The closest genuine Honeywell rad-hard comms part I could find is:

urlHoneywell HXSRD01 Trivor SERDES Datasheetturn0search0

This is:
- radiation-hardened,
- SOI CMOS,
- intended for radiation-sensitive environments,
- multi-Gb/s serial links,
- serializer/deserializer architecture. citeturn0search0turn0search2

Key specs:
- 1–3.1875 Gb/s per lane,
- redundant lanes,
- −55 °C to +125 °C,
- Honeywell 150 nm SOI rad-hard process. citeturn0search0turn0search4

This is important:
it is *not* the optical emitter itself.

You would pair this sort of device with:
- external laser driver,
- VCSEL,
- fibre interface.

That actually aligns very well with your “minimal sacrificial optical module” thinking.

Honeywell appear to focus more on:
- rad-hard serializers,
- ASICs,
- space link electronics,
rather than selling commodity optical pluggable modules. citeturn0search1turn0search5

The likely architecture in aerospace/space systems is:

FPGA/LVDS  
→ Honeywell rad-hard SERDES  
→ laser driver  
→ VCSEL/fibre.

Rather than:
- integrated Ethernet SFP modules.

Also worth noting:
true Honeywell rad-hard parts are usually:
- export-controlled,
- aerospace supply-chain items,
- long lead time,
- extremely expensive.

You generally don’t “buy one from Mouser”.

For your application, I still suspect the best engineering trade may be:

- commercial cheap optical emitter module near radiation zone,
- fibre immediately out of shield,
- all expensive logic remote,
- treat the local optical head as consumable.

Because once you step into genuine rad-hard aerospace silicon, costs escalate very rapidly.

[M11] ME (2026-05-14 16:08):
Is was this one 

[M12] AI (2026-05-14 16:08):
The one you were probably thinking of is very likely the entity["company","Honeywell","Aerospace microelectronics division"] HXSRD01 “Trivor” SERDES. It is a genuine radiation-hardened high-speed serial transceiver IC. citeturn0search0turn0search2

Key specs that match what you were describing:

- Quad redundant SERDES
- 1–3.1875 Gb/s per lane
- Supports Fibre Channel / XAUI
- Radiation hardened SOI CMOS
- Neutron tolerance ≥ 1×10¹⁴ cm⁻²
- Total dose up to 1 Mrad(Si)
- No latch-up
- Space / harsh environment intended. citeturn0search0turn0search2

This is the datasheet:

urlHoneywell HXSRD01 Trivor SERDES Datasheetturn0search0

But importantly:

this is **not** an optical SFP module.

It is the electronic high-speed serial transceiver portion. You would still need:
- laser driver,
- VCSEL or laser,
- optical subassembly,
- fibre.

So the architecture becomes:

FPGA/LVDS  
→ Honeywell rad-hard SERDES  
→ optical driver  
→ VCSEL  
→ fibre.

That’s why earlier the terminology got blurred between:
- “transceiver IC”,
- and “optical transceiver module”.

Honeywell mainly sell the former. citeturn0search1turn0search5

There *was* also an older Honeywell rad-hard fibre optic LED module family — example “Honeywell 2066 Fiber Optic Rad-Hard LED” — but that looks like legacy aerospace hardware rather than modern high-speed data optics. citeturn0search7

If your use case is:
- moderate speed,
- LVDS transport,
- fusion instrumentation,
- disposable near-vessel modules,

then honestly the Honeywell device may be overkill unless:
- you need guaranteed SEE performance,
- very high cumulative dose,
- or mission-critical survivability.

The CERN-style approach using:
- simpler VCSEL drivers,
- modest protocol complexity,
- sacrificial optical heads,
often ends up much more practical and affordable. citeturn0academia12turn0academia13

[M13] ME (2026-05-14 16:09):
Well my speed isn’t that high . 100Mhz

[M14] AI (2026-05-14 16:09):
At **100 MHz**, the Honeywell SERDES route is probably **massive overkill**.

For your case, think simpler:

**100 MHz digital / LVDS signal**  
→ **LVDS receiver or buffer**  
→ **simple optical transmitter / laser driver / VCSEL**  
→ fibre  
→ **remote receiver outside radiation area**

You likely do **not** need:
- multi-Gb/s SERDES,
- XAUI,
- Fibre Channel,
- Ethernet,
- protocol stacks,
- embedded controller near the radiation zone.

The key distinction is:

- **100 MHz clock-like or logic signal**: can be sent as a raw optical digital channel.
- **100 Mbit/s encoded data**: still modest; a simple optical link can handle it.
- **100 MHz parallel bus / many channels**: then you need either one optical channel per signal, or a serializer/mux.

For a radiation campaign, the sensible hierarchy is probably:

### Best practical option

Use a **simple 850 nm VCSEL transmitter** or **fibre-optic logic transmitter** as close to the source as needed, with the expensive receiver/electronics outside.

Something in the style of:

**LVDS in → optical Tx → fibre → optical Rx → LVDS/TTL out**

That is much more aligned with a disposable module.

### If you want robust rather than fancy

Prefer:
- 850 nm or 1310 nm fibre link,
- minimal IC count,
- no SFP management electronics,
- no Ethernet PHY,
- direct optical modulation,
- radiation test it as a consumable item.

### Honeywell only makes sense if

You need:
- guaranteed rad-hard qualification,
- high neutron fluence survivability,
- formally controlled space-grade part pedigree,
- many years operation in-radiation,
- or failure is unacceptable.

For **100 MHz**, I’d be looking first at:

- Broadcom/Avago HFBR-style fibre optic transmitters/receivers,
- simple industrial fibre optic logic links,
- VCSEL + laser driver,
- or a cheap SFP used only as a physical optical head if sacrificial.

The cleanest argument to the customer is:

> At the required 100 MHz signalling rate, a complex rad-hard SERDES solution is not technically necessary. A simpler directly modulated optical transmitter with remote receiving electronics is likely to reduce complexity, cost, and radiation-sensitive silicon in the exposed area.

That is probably the right engineering line.

[M15] ME (2026-05-14 16:10):
Yes but what part has had some xharatxerisat8! For neutron testing 

[M16] AI (2026-05-14 16:10):
Yes — now we’re in the right territory. The parts with the strongest neutron-characterisation pedigree are mostly **VCSELs and VCSEL arrays** from the CERN / ATLAS ecosystem, rather than generic telecom SFPs.

The most directly characterised devices I found are:

- **Truelight VCSELs** irradiated at the Ljubljana TRIGA reactor. citeturn0search9turn0search6
- **Commercial VCSEL arrays** used in ATLAS optical links. citeturn0search2turn0academia11
- **Custom ATLAS VCSEL optical links** designed for hostile neutron fields. citeturn0search6turn0academia10

The important thing is the neutron levels they survived are *extremely high*:

- up to ~\(8\times10^{14}\) neq/cm² in earlier studies, citeturn0search2turn0search6
- and later studies pushed toward \(10^{16}\) neq/cm². citeturn0search9

That is well beyond most fusion diagnostic instrumentation exposures unless you are very near plasma-facing regions.

The key practical findings:

- VCSEL optical power degrades gradually,
- threshold current rises,
- annealing helps,
- many devices continue functioning after huge neutron fluence. citeturn0search9turn0search7

For your ~100 MHz requirement, that is encouraging because:
- you do not need high optical margin,
- you do not need multi-Gb SERDES recovery,
- you can tolerate some optical degradation.

The actual vendors/parts historically seen in papers include:

| Type | Notes |
|---|---|
| Truelight VCSEL arrays | Explicit neutron irradiation data from ATLAS studies |
| Fujikura fibre + VCSEL systems | CERN optical link ecosystem |
| Honeywell rad-hard SERDES + external VCSEL | Aerospace approach |
| Avago/Broadcom VCSELs | Commonly evaluated in detector systems |
| CERN MTx/MTRx optical modules | Modern HL-LHC approach |

The problem is:
many of the exact historical VCSEL parts are now obsolete or semi-custom.

So the better engineering question becomes:

> “Which *modern* VCSEL families are descendants of the characterised ATLAS/CERN style devices?”

That usually points toward:
- Broadcom/Avago VCSEL arrays,
- Finisar optical engines,
- Firecomms industrial fibre devices,
- CERN MTx ecosystem.

The most useful paper for your exact thought process is probably:

“VCSEL-based Custom Radiation Tolerant Optical Data Links” citeturn0search6

because it specifically discusses:
- neutron irradiation,
- annealing,
- commercial VCSEL qualification,
- optical link architecture,
- detector readout,
- low-mass/simple optical links.

And importantly:
they were running around **40–80 Mbit/s** range in many cases. citeturn0academia10turn0academia12

That is extremely close to your own bandwidth territory.

So your idea is actually quite aligned with proven architectures:
- modest speed,
- simple optical transport,
- minimal in-radiation electronics,
- sacrificial/replaceable optical heads,
- fibre immediately escaping hostile region.

[M17] ME (2026-05-14 16:11):
Can you link me to a part supply. Do they show costs 

[M18] AI (2026-05-14 16:11):
For your ~100 MHz case, I would focus on the simpler industrial/VCSEL-style optical transmitters rather than aerospace SERDES parts.

The good news is:
- these are cheap,
- available now,
- and architecturally very similar to what CERN historically used before custom ASIC integration.

The most interesting currently-buyable parts I found are:

### Broadcom / Avago HFBR family
These are old-school but very robust industrial fibre-optic transmitter modules.

product["turn0product8","Broadcom HFBR-1414PTZ",{"render_as":"hero","description":"160 MBd industrial fibre-optic transmitter module using 820 nm optics; simple architecture and suitable for experimental radiation testing."}]

Typical cost:
- ~£20–25 each from Farnell/RS. citeturn0product8turn0product11

These are attractive because:
- 160 MBd rating comfortably covers your 100 MHz territory,
- very low complexity,
- no Ethernet stack,
- no management EEPROM,
- no DSP,
- essentially direct electrical-to-optical conversion.

That simplicity is exactly what tends to survive radiation better.

Other closely related variants:

products{"selections":[["turn0product2","HFBR-1414T AGILENT transmitter"],["turn0product20","Broadcom HFBR-1412PTZ"],["turn0product14","Broadcom HFBR-1415PMZ"]]}

These are all in roughly the:
- £13–30 range,
- industrial fibre-link category,
- easy-to-prototype territory. citeturn0product2turn0product14turn0product20

## Why these are interesting for neutron environments

These exact parts are not formally sold as “rad-hard”, BUT:
- Broadcom/Avago style VCSELs are extremely similar to the commercial devices used in CERN ATLAS optical-link neutron campaigns. citeturn0search0turn0search3turn0academia14
- The ATLAS studies repeatedly showed commercial VCSEL arrays surviving neutron/proton exposure with graceful degradation rather than catastrophic failure. citeturn0search0turn0search3
- The tested systems were often around 40–80 Mbit/s class links, very close to your application. citeturn0academia13turn0academia15

## Practical recommendation

I’d probably prototype in this order:

| Attribute | entity["turn0product8","Broadcom HFBR-1414PTZ"] | entity["turn0product20","Broadcom HFBR-1412PTZ"] | entity["turn0product1","FS 10G LR SFP+"] |
|---|---:|---:|---:|
| Complexity | Very low | Very low | High |
| Protocol overhead | None | None | Significant |
| Radiation-sensitive silicon | Minimal | Minimal | Much higher |
| Speed capability | 160 MBd | 160 MBd | Massive overkill |
| Ease of prototyping | Excellent | Excellent | Moderate |
| Cost | ~£20–25 | ~£20–25 | ~£28 |
| Likely neutron robustness | Potentially good | Potentially good | Uncertain |
| Repair/disposable suitability | Excellent | Excellent | Moderate |

The HFBR approach feels much more aligned with your:
- disposable module idea,
- fusion instrumentation mindset,
- moderate bandwidth,
- desire to minimise active silicon in-radiation.

Whereas an SFP:
- contains SERDES,
- clock recovery,
- management interfaces,
- DSP/limiting amplifiers,
- often far more delicate support circuitry.

[M19] ME (2026-05-14 16:12):
So what’s the best documented part for survival and characteristics 

[M20] AI (2026-05-14 16:12):
If the question is:

> “Which currently obtainable optical transmitter family has the best documented neutron/radiation survivability pedigree?”

then the answer is probably:

## Broadcom / Avago VCSEL-based devices
especially the families historically used in CERN ATLAS optical-link work.

The exact historic CERN-tested parts are often obsolete now (Truelight VCSELs etc.), but the *best-documented lineage* is still:

- Avago / Broadcom VCSEL transmitters,
- simple optical link architectures,
- low-complexity optical heads.

For your actual use case (~100 MHz, fusion instrumentation), I think the strongest practical candidate is:

# Best overall

product["turn0product0","Broadcom HFBR-1414PTZ",{"render_as":"hero","description":"Simple 160 MBd industrial fibre-optic transmitter with minimal internal complexity and architecture closely aligned with historically radiation-tested VCSEL link approaches."}]

Why this wins:
- very low internal complexity,
- no SERDES,
- no Ethernet PHY,
- no DSP,
- cheap enough to sacrificially irradiate,
- available today,
- comfortably above your required speed,
- architecture similar to CERN low-level optical links.

And importantly:
the *Broadcom/Avago VCSEL ecosystem* is the one with the deepest published neutron-characterisation heritage from CERN ATLAS. citeturn0search0turn0search1turn0search6

## Most strongly documented pedigree

The actual best-documented *specific* devices in literature were:

- Truelight VCSELs,
- Fujikura fibre systems,
- ATLAS custom VCSEL optical links. citeturn0search0turn0search1

Those papers tested:
- neutron fluence up to ~\(10^{15}\) neq/cm²,
- gradual optical degradation,
- annealing recovery,
- long-term operation in collider environments. citeturn0search0turn0search1turn0search6

The problem:
those exact parts are difficult or impossible to buy now.

So the engineering decision becomes:
> “What modern commercially obtainable family is closest to the historically characterised CERN ecosystem?”

That points directly back to Broadcom/Avago industrial optical transmitters.

## Shortlist comparison

| Attribute | entity["turn0product0","Broadcom HFBR-1414PTZ"] | entity["turn0product1","Broadcom HFBR-1412PTZ"] | entity["turn0product3","Finisar FTLF8519P3BNL"] |
|---|---:|---:|---:|
| Architecture complexity | Very low | Very low | High |
| Ethernet/SFP management | No | No | Yes |
| Internal SERDES | No | No | Yes |
| Speed class | 160 MBd | 160 MBd | Multi-Gb |
| Suitability for 100 MHz | Excellent | Excellent | Overkill |
| Radiation-sensitive silicon count | Minimal | Minimal | Much higher |
| Similarity to CERN low-level links | High | High | Moderate |
| Ease of sacrificial deployment | Excellent | Excellent | Moderate |
| Cost | ~£17–25 | ~£18–25 | ~£20–35 |

The Finisar-style SFPs are interesting because:
- CERN *does* use SFP-like architectures in some newer systems,
- but they contain far more delicate electronics.

At your bandwidth, simpler is probably better.

## The important insight

At 100 MHz, survivability is usually improved more by:
- reducing silicon complexity,
- minimising PLLs and DSP,
- keeping the optical head dumb/simple,
than by chasing formally “rad-hard” telecom modules.

That is exactly why the CERN detector world historically converged on:
- VCSEL,
- simple drivers,
- custom lightweight optical heads,
- remote electronics. citeturn0search1turn0academia12

[M21] ME (2026-05-15 07:17):
A battery 

[M22] AI (2026-05-15 07:17):
If you mean:

> “What battery chemistry/part is best characterised for neutron/radiation survival?”

then that becomes a very different problem from the optical links.

For radiation environments, the usual hierarchy is roughly:

| Chemistry | Radiation Robustness | Notes |
|---|---|---|
| Primary lithium thionyl chloride (Li-SOCl₂) | Very good | Common in nuclear/space instrumentation |
| Lithium metal primary | Good | Simple chemistry helps |
| NiCd | Historically robust | Old aerospace/nuclear favourite |
| Lead acid | Surprisingly tolerant | But bulky |
| Li-ion commercial cells | Variable / often poor | Protection electronics become issue |
| Supercaps | Often quite robust | Good for ride-through |

The important thing:
for batteries, the weak point is often *not the cell chemistry* but:
- protection ICs,
- gas generation,
- separator degradation,
- electrolyte radiolysis,
- BMS electronics.

For your kind of fusion instrumentation, many systems avoid placing:
- smart BMS,
- switching regulators,
- microcontrollers,
inside high neutron regions.

Instead they:
- place passive cells locally,
- keep charging/control remote,
- or avoid batteries entirely.

If you are asking for:
- a battery that can sit near neutron exposure during campaigns,
- modest runtime,
- disposable or semi-sacrificial use,

then the most defensible engineering choice is often:

## Lithium thionyl chloride primary cells

Examples:
- Saft LS series
- Tadiran SL series

These have:
- excellent shelf life,
- simple chemistry,
- industrial/nuclear pedigree,
- fewer active electronics required.

Or:

## Simple sealed lead acid
if size/mass are acceptable.

Because:
- extremely well understood,
- little sensitive silicon,
- graceful failure behaviour.

What I would *not* trust near significant neutron exposure:
- consumer USB power banks,
- smart Li-ion packs,
- integrated BMS systems,
- cheap boost converters.

Those are full of:
- MOSFETs,
- controllers,
- flash,
- protection ICs,
which are much more neutron sensitive than the battery chemistry itself.

If you want, I can also look specifically for:
- neutron-tested battery papers,
- fusion/space battery studies,
- rad-hard power systems,
- or practical buyable battery parts for instrumentation modules.

[M23] ME (2026-05-15 07:19):
Wild that heavy ant oros or cins of powering optics?

[M24] AI (2026-05-15 07:19):
I think you’re asking something close to:

> “Would heavy anti-protons / ions / radiation conditions cause issues powering the optics?”

or possibly:

> “What’s the main concern when powering optics in heavy radiation?”

The answer is: yes — but usually the *power/control electronics* fail before the optical fibre itself.

For optical transmitters in neutron/heavy-ion environments, the vulnerable areas are typically:

- laser driver ICs,
- VCSEL bias circuitry,
- PLLs/clock recovery,
- DC/DC converters,
- EEPROM/configuration devices,
- protection MOSFETs.

Not usually:
- the fibre glass,
- or even the VCSEL junction initially.

Heavy ions are especially nasty because they can cause:

- SEU — single event upset,
- SEL — single event latch-up,
- burnout,
- transient glitches,
- regulator collapse.

A commercial optical module powered in-radiation can fail simply because:
- a tiny switching regulator latches,
- bias current drifts,
- or the control IC crashes.

That’s why the simplest architecture tends to survive best.

For your 100 MHz application, a very robust philosophy is:

Battery / remote supply  
→ simple linear regulation  
→ LVDS buffer  
→ optical transmitter  
→ fibre out.

Avoid:
- switching converters locally if possible,
- smart management ICs,
- complex digital logic,
- Ethernet PHYs,
- Linux/SFP management.

The funny thing is:
the actual optical power needed at 100 MHz is tiny. So you can often get away with:
- very low current,
- simple biasing,
- even crude architectures.

That simplicity helps radiation tolerance enormously.

Also, if you are genuinely in a heavy neutron environment:
- don’t underestimate power-supply transients,
- cable-induced ground shifts,
- induced currents,
- and intermittent latch behaviour.

A lot of “optics failures” in radiation systems are actually:
- power integrity failures,
- not optical failures.

So your instinct about keeping things:
- simple,
- sacrificial,
- low component count,
is probably exactly right.

[M25] ME (2026-05-15 07:22):
Wiuid powering the optics wth Nica battery we good?

[M26] AI (2026-05-15 07:22):
I’ll separate this into two risks: whether the NiCd cell chemistry will tolerate the environment, and whether the optical electronics it powers will behave cleanly under radiation.

[M27] AI (2026-05-15 07:22):
Yes — **NiCd is a good candidate** for powering a small optical head in a radiation area.

Better than a consumer Li-ion pack, mainly because it can be very simple: **cells + fuse + linear regulator + optics**. Avoid putting a smart charger/BMS/DC-DC converter in the radiation zone.

NiCd has historic space/nuclear use, and older radiation studies found short-term voltage/current behaviour was not strongly affected by gamma irradiation, though capacity can degrade with cycling/exposure. citeturn842395search0turn842395search2

For your optical module I’d do:

**NiCd pack → fuse/PTC → LC/RC filtering → simple LDO/linear regulator → LVDS/optical transmitter**

Avoid locally:
- switch-mode converters,
- microcontrollers,
- smart BMS,
- EEPROM/configured modules,
- anything needing software.

Main caveat: NiCd cells are bulky, self-discharge, and cadmium is nasty from a handling/disposal standpoint. But electrically and radiation-wise, for a **sacrificial 100 MHz optical transmitter module**, it is a very sensible direction.

[M28] ME (2026-05-15 07:23):
Or just use a bench shoot disn a iibg thick cable?

[M29] AI (2026-05-15 07:23):
Yes — **a bench supply down a big thick cable is probably better** than a local battery, provided you design the feed properly.

For your case I’d favour:

**remote bench/linear supply → thick 2-core feed → local fuse → local bulk capacitance → local LDO/regulator → optics**

Why it’s better:
- no battery chemistry in the radiation area
- no charging/BMS problem
- easier to switch off/reset remotely
- easier to current-limit and monitor
- less maintenance before/after campaigns

Use the thick cable to minimise voltage drop, but still regulate locally at the optical head. Don’t feed the optics directly from 20 m away without local decoupling/regulation.

I’d include at the head:
- fuse or resettable PTC
- reverse-polarity protection
- TVS diode
- bulk cap, e.g. 100–1000 µF
- ceramic caps close to transmitter
- linear regulator/LDO
- maybe common-mode choke/feedthrough filtering if the environment is noisy

So the practical architecture becomes:

**12 V bench supply at rack → thick cable → local 5 V or 3.3 V clean rail → optical Tx**

That is probably the neatest option. Battery only really wins if you need full galvanic isolation or there is no trustworthy supply path.

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] ME (2026-05-15 07:17):
The oxide cowoikd a battedybget upet?

[A2] AI (2026-05-15 07:17):
Yes — if by “optics” you mean the optical transmitter/receiver electronics near the radiation area, then a battery-powered module absolutely could get upset by radiation depending on:

- neutron flux,
- gamma dose,
- chemistry of the battery,
- and what electronics are attached to it.

But the battery itself is usually *not* the first thing to fail.

The more likely upset points are:
- regulators,
- DC/DC converters,
- PLLs,
- serializers,
- laser drivers,
- microcontrollers,
- EEPROM/configuration memory.

A simple battery feeding a simple VCSEL driver can actually be fairly robust.

For fusion/neutron environments specifically:

## What neutrons tend to upset most

### Very sensitive
- SRAM
- FPGAs
- flash memory
- Ethernet PHYs
- SERDES
- switching regulators
- DSPs
- clock recovery

### Moderately sensitive
- laser drivers
- op-amps
- ADCs
- MCUs

### Often surprisingly robust
- passive fibre
- simple BJTs/FETs
- linear regulators
- LEDs/VCSELs
- batteries

So your instinct toward:
> “keep the near-radiation end extremely simple”

is exactly right.

For example, this architecture is pretty sensible:

Battery  
→ linear regulator  
→ LVDS buffer  
→ simple optical transmitter  
→ fibre out.

Much better than:

Battery  
→ FPGA  
→ Ethernet PHY  
→ managed SFP  
→ Linux SOM.

## Battery chemistry

Different chemistries behave differently:

| Chemistry | Radiation Behaviour |
|---|---|
| Li-ion | Usually usable but capacity degrades over dose/time |
| LiFePO₄ | Generally more stable/safe |
| Alkaline | Simple, often surprisingly tolerant |
| Lead acid | Quite robust physically |
| Coin cells | Can suffer leakage/de
