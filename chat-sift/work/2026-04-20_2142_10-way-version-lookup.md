# 10-way version lookup
Date (UTC): 2026-04-20 21:42
Conversation ID: 69e69dce-6d54-8391-8f90-1e1ebaea0faf
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-20 21:42):
[image]
Imnloooking for 10’wY version 
[attached file: IMG_6A39E819-D7C8-43C5-AD52-54176A1D50C3.jpeg]

[M2] AI (2026-04-20 21:43):
The 10-way version looks to be **TE Connectivity 2-1761608-3**. TE lists it as a **10-position, 2.54 mm pitch, vertical, through-hole, low-profile AMP-LATCH header with short eject latch**, which matches the family/style of your 14-way **2-1761608-5**. citeturn694381search0turn967441search2

On Mouser it appears as **Mouser 571-2-1761608-3**, described as **“PIN HEADER 10 POS VERT LOW PROFILE.”** citeturn694381search1

So the likely mapping is:
- **2-1761608-3 = 10 way**
- **2-1761608-5 = 14 way** citeturn694381search0turn967441search2

If you want, I can also find the **matching IDC cable socket/receptacle** for the 10-way version.

[M3] ME (2026-04-20 22:18):
[image]
What’s the Panasonic equivalent of this?
[attached file: IMG_637EE6D7-45E4-48D7-8036-6D859D52B893.jpeg]

[M4] AI (2026-04-20 22:18):
The closest Panasonic equivalent to your **Vishay CRCW12105K60FKEA** is **Panasonic ERJ-14NF5601U**. It matches the key electrical and package attributes: **5.6 kΩ, ±1%, 1210 package, thick film, AEC-Q200**. citeturn209582search0turn209582search7

One thing to watch: Mouser marks **ERJ-14NF5601U** as **NRND**. citeturn209582search7

So in practical terms:
- **Vishay original:** CRCW12105K60FKEA = **1210, 5.6 kΩ, 1%, 0.5 W, thick film, AEC-Q200**. citeturn209582search0
- **Panasonic same-style substitute:** **ERJ-14NF5601U** = **1210, 5.6 kΩ, 1%, thick film, AEC-Q200**. citeturn209582search7

If you need a **currently preferred Panasonic part rather than NRND**, the closest active Panasonic parts I found at Mouser with the same resistance/power/tolerance are in smaller packages, such as **ERJ-P06F5601V** (0805, 0.5 W, 1%, AEC-Q200) and **ERJ-HP6F5601V** (0805, 0.5 W, 1%, up to 175 °C). Those are not footprint-equivalent to your 1210 Vishay part. citeturn209582search7

So the clean answer is: **ERJ-14NF5601U** for the 1210 Panasonic equivalent, but it is **NRND**.

[M5] ME (2026-04-20 22:31):
[image]
I’m trying to consolidate the parts in the library. Not have loads of different manufacturers. I was thinking KEMET for ceramic and ABX FIR TANTALUMS. Can you search through the list on ceramics and provide the owner part numbers? Do them one by one if need to.
[attached file: IMG_DF92F81A-C5C7-419E-8438-2F71F657B3DD.jpeg]

[M6] AI (2026-04-20 22:33):
Yes — I’ve gone through the **ceramic** parts in your screenshot and mapped them to **KEMET owner parts** where there is an evident like-for-like match on **package, capacitance, dielectric, voltage, and tolerance**.

I have **ignored the AVX tantalums** at the bottom, as requested.

### Proposed KEMET owner parts for the ceramic list

| Existing part | Decoded / basis | Proposed KEMET owner part |
|---|---|---|
| **TDK C1005X7R1H104K050BB** | 0402, 0.1 µF, 50 V, X7R, ±10% citeturn144193search8 | **No exact KEMET P/N confirmed yet** |
| **KEMET C0603X102K5RAC3190** | Already KEMET | **Keep as is** |
| **YAGEO CC0603KRX7R7BB105** | 0603, 1 µF, 16 V, X7R, ±10% citeturn648732search1turn144193search5 | **C0603C105K4RACAUTO** citeturn648732search1 |
| **AVX 06035C103KAT2A** | 0603, 0.01 µF, 50 V, X7R, ±10% citeturn144193search2turn144193search10 | **C0603C103K5RACAUTO** citeturn648732search2 |
| **MURATA GRM188R61E106MA73D** | 0603, 10 µF, 25 V, X5R, ±20% citeturn144193search3turn144193search11 | **No KEMET exact match found** |
| **YAGEO CC0603JRNPO9BN390** | 0603, 39 pF, C0G/NP0, 50 V, ±5% inferred from search class and matching families citeturn669658search0 | **C0603H390J5GACTU** citeturn669658search8 |
| **MURATA GRM188R72A104KA35D** | 0603, 0.1 µF, 100 V, X7R, ±10% citeturn999169search4turn999169search12 | **C0603C104K1RACTU** or auto version **C0603C104K1RACAUTO** citeturn669658search5turn669658search1 |
| **KYOCERA 06035C104KAZ2A** | 0603, 0.1 µF, 100 V, X7R, ±10% pattern-equivalent to the Murata line above; this AVX/Kyocera series maps to same electrical class citeturn999169search12turn669658search1 | **C0603C104K1RACTU** / **C0603C104K1RACAUTO** citeturn669658search5turn669658search1 |
| **KEMET C0402C151K5RACTU** | Already KEMET | **Keep as is** |
| **KYOCERA 08053C105KAT2A** | 0805, 1 µF, 50 V, X7R, ±10% citeturn363978search1turn363978search0 | **C0805C105K5RACTU** or auto version **C0805C105K5RACAUTO** citeturn363978search7turn363978search8 |
| **KEMET C0805C475K3PAC** | Already KEMET | **Keep as is** |
| **SAMSUNG CL21B106KOQNNNE** | 0805, 10 µF, 16 V, X7R, ±10% citeturn999169search5turn999169search9 | **No exact KEMET X7R 16 V owner part confirmed yet** |
| **MURATA GRM32ER71E226KE15L** | 1210, 22 µF, 25 V, X7R, ±10% citeturn999169search2turn999169search10 | **C1210C226K3RACAUTO** |
| **MURATA GRM55DR61H106KA88L** | 2220, 10 µF, 50 V, X5R, ±10% citeturn999169search3turn999169search7turn999169search11 | **Closest KEMET found is C2220C106K5RACTU, but this is X7R, not X5R** citeturn277769search3 |

### Cleaned owner list to use
If your aim is a **single ceramic owner family around KEMET**, the parts I’d confidently standardise immediately are:

- **C0603C105K4RACAUTO** for the 0603 1 µF 16 V X7R parts citeturn648732search1  
- **C0603C103K5RACAUTO** for the 0603 10 nF 50 V X7R parts citeturn648732search2  
- **C0603H390J5GACTU** for the 0603 39 pF NP0/C0G parts citeturn669658search8  
- **C0603C104K1RACTU** or **C0603C104K1RACAUTO** for the 0603 100 nF 100 V X7R parts citeturn669658search5turn669658search1  
- **C0805C105K5RACTU** or **C0805C105K5RACAUTO** for the 0805 1 µF 50 V X7R parts citeturn363978search7turn363978search8  
- **C1210C226K3RACAUTO** for the 1210 22 µF 25 V X7R parts citeturn277769search6

### Ones I would treat carefully
A few lines do **not** have a clean exact KEMET replacement from what I could verify quickly:

- **GRM188R61E106MA73D** — 0603, 10 µF, 25 V, X5R, ±20%. I did not verify a KEMET exact equivalent. citeturn144193search3turn144193search11  
- **CL21B106KOQNNNE** — 0805, 10 µF, 16 V, X7R, ±10%. I did not verify the exact KEMET twin yet. citeturn999169search5turn999169search9  
- **GRM55DR61H106KA88L** — KEMET part found was **X7R**, not the same **X5R** dielectric, so I would not auto-substitute that without your sign-off. citeturn999169search7turn277769search3  
- **TDK C1005X7R1H104K050BB** — I confirmed the TDK spec but did not pin an exact KEMET owner P/N from the search results I reviewed. citeturn144193search8

Best next move is for me to do the unresolved ones **one by one** and give you a final **owner-part master list** in a neat table you can paste straight into the library.

[M7] ME (2026-04-20 22:37):
Is there another manufacturer with full coverage?

[M8] AI (2026-04-20 22:38):
Yes. For **ceramics**, the manufacturer I’d pivot to is **Murata**.

Why Murata is the strongest candidate for your owner line:
- Your own list already contains several Murata parts in the harder value/size corners, including **0603 10 µF 25 V X5R**, **1210 22 µF 25 V X7R**, and **2220 10 µF 50 V X5R**, which were exactly the awkward ones where KEMET coverage started to look patchy. citeturn894188search0turn894188search2
- Mouser’s Murata coverage for MLCCs is broad across the general catalogue, and Murata shows up repeatedly in those higher-capacitance, higher-voltage combinations. citeturn894188search0turn894188search1turn894188search2

My practical recommendation:
- **Ceramics owner = Murata**
- **Tantalums owner = AVX / KYOCERA AVX**

That is the cleanest split from a library-governance point of view.

A couple of caveats:
- I would **not** choose KEMET as the sole ceramic owner if your goal is easiest exact replacement coverage across this list, because the difficult MLCC corners were where I could verify Murata parts more readily than KEMET exact matches. citeturn894188search0turn894188search2
- I also would **not yet claim TDK has full exact coverage** for your full set from the evidence I checked. TDK clearly has a very broad MLCC range, but I did not verify exact one-for-one coverage for all of your troublesome entries. citeturn232259search0turn232259search1

So the answer is:
**Yes — Murata is the best bet for near-full, and likely full, ceramic coverage for this list.**

If you want, I’ll take your ceramic rows and convert them into a **Murata owner-part table** next.

[M9] ME (2026-04-20 22:39):
What is the quality like? Out of 10

[M10] AI (2026-04-20 22:39):
For **MLCC ceramics**, I’d rate **Murata about 9/10**.

Why not 10:
- They have a very strong reliability and process story, including broad use in high-reliability sectors and automotive-qualified series such as **GCM/GRT** that are **AEC-Q200 compliant**. citeturn489929search1turn489929search5
- Murata also highlights vertically integrated manufacturing, broad range coverage, and long-standing MLCC production depth, which is exactly what you want for a library owner line. citeturn489929search0
- Their automotive manufacturing base includes **IATF 16949** certification, which is another positive indicator for controlled quality systems. citeturn489929search2turn489929search9

Why I still leave 1 point off:
- No vendor is perfect on **availability, lifecycle stability, and occasional capacitance derating pain** in real designs. That is not unique to Murata; it is just the reality of MLCCs.
- Also, “quality” depends on whether you mean **electrical performance**, **long-term reliability**, **consistency of supply**, or **ease of standardisation**. Murata scores very highly across all four, but I would reserve **10/10** for a case where your exact internal criteria are defined and they clear every one of them.

My practical scoring for library ownership:
- **Murata ceramics:** **9/10**
- **KEMET ceramics:** **7.5–8/10** for this particular consolidation exercise, mainly because coverage looked less complete on your harder-value lines
- **AVX / KYOCERA AVX tantalums:** **9/10** as a sensible tantalum owner family

So if your real question is “would I trust Murata as the ceramic owner manufacturer for a disciplined library?” — **yes, absolutely**.

[M11] ME (2026-04-20 22:44):
Ok, reveal em off 

[M12] AI (2026-04-20 22:44):
Yep — if you mean **“reel them off”**, here’s my **practical library-owner quality score out of 10** for the manufacturers showing up in your list.

For **ceramic capacitors**:

- **Murata — 9/10**  
  Best all-rounder for MLCC breadth, quality reputation, and strong automotive/high-reliability coverage. Murata has broad AEC-Q200-qualified lines and a deep MLCC portfolio. citeturn330559search0turn330559search8turn330559search12

- **TDK — 9/10**  
  Very strong. I’d put them basically shoulder-to-shoulder with Murata for MLCC credibility. Strong automotive coverage and serious breadth, especially in higher-performance and specialised lines. citeturn330559search1turn330559search5turn330559search13

- **KYOCERA AVX — 8.5/10**  
  Strong quality house, very credible for both ceramics and tantalums. Good automotive offering, and they explicitly position QA and improved-reliability ceramic families strongly. citeturn330559search3turn330559search11turn330559search15

- **KEMET — 8/10**  
  Good manufacturer, absolutely usable, and with proper automotive-qualified MLCC families. My only reason for marking them below Murata/TDK here is not “bad quality” — it is that for your consolidation exercise they looked less complete in exact coverage on some awkward corners. citeturn330559search2turn330559search14

- **Samsung Electro-Mechanics — 8/10**  
  Good

[M13] ME (2026-04-20 22:45):
List 

[M14] AI (2026-04-20 22:45):
Ceramics:

- **Murata — 9/10**
- **TDK — 9/10**
- **KYOCERA AVX — 8.5/10**
- **KEMET — 8/10**
- **Samsung Electro-Mechanics — 8/10**
- **Yageo — 7.5/10**

Tantalums:

- **KYOCERA AVX — 9/10**
- **KEMET — 8.5/10**
- **Vishay — 8/10**
- **Panasonic — 7.5/10**

For your library standardisation, I’d go:
- **Ceramics: Murata**
- **Tantalums: KYOCERA AVX**

[M15] ME (2026-04-20 22:47):
[image]
Find Murata alternatives against this list. Not the and parts 
[attached file: B34C304B-9696-453E-A9B2-6C7FF1737193.jpeg]

[M16] AI (2026-04-20 22:49):
Assuming you mean **exclude the existing Murata rows and exclude the AVX tantalum parts at the bottom**, these are the **Murata ceramic equivalents** I’d put against the remaining ceramic lines in your list.

| Current part | Decoded spec | Murata alternative | Confidence |
|---|---|---|---|
| **TDK C1005X7R1H104K050BB** | 0402, 100 nF, 50 V, X7R, ±10% citeturn555462search4turn555462search8 | **GRM155R71H104KE14D** citeturn610377search0turn610377search4 | High |
| **KEMET C0603X102K5RAC3190** | 0603, 1000 pF, 50 V, X7R, ±10% citeturn555462search1turn555462search9 | **GRM188R71H102KA01D** citeturn610377search1turn610377search5 | High |
| **YAGEO CC0603KRX7R7BB105** | 0603, 1 µF, 16 V, X7R, ±10% citeturn555462search2turn555462search6 | **GRM188R71C105KA12D** citeturn610377search2 | High, but obsolete |
| **AVX 06035C103KAT2A** | 0603, 10 nF, 50 V, X7R, ±10% citeturn555462search3turn555462search7 | **GRM188R71H103KA01D** citeturn610377search7 | High |
| **YAGEO CC0603JRNPO9BN390** | 0603, 39 pF, 50 V, C0G/NP0, ±5% citeturn870996search0turn870996search4 | **GRM1885C1H390JA01D** citeturn870996search0turn870996search4 | High |
| **KYOCERA 06035C104KAZ2A** | 0603, 100 nF, 100 V, X7R, ±10%; same class as the Murata line already in your list citeturn870996search1turn870996search5 | **GRM188R72A104KA35D** citeturn870996search1turn870996search5 | High |
| **KEMET C0402C151K5RACTU** | 0402, 150 pF, 50 V, X7R, ±10% implied by KEMET coding and distributor family listings for 0402/50 V/X7R/150 pF citeturn262367search5 | **Likely GRM155R71H151KA01D** citeturn262367search2turn262367search4 | Medium |
| **KYOCERA 08053C105KAT2A** | 0805, 1 µF, 50 V, X7R, ±10% citeturn870996search3turn870996search7 | **GRM21BR71H105KA12L** citeturn870996search3 | High |
| **KEMET C0805C475K3PAC** | 0805, 4.7 µF, 25 V, X5R, ±10% citeturn945956search6 | **GRM219R61E475KA73J** citeturn945956search4 | High |
| **SAMSUNG CL21B106KOQNNNE** | 0805, 10 µF, 16 V, X7R, ±10% citeturn761839search0 | **GRM21BZ71C106KE15L** citeturn690719search7 | High |

A few notes before you bake these into the library:

- **GRM188R71C105KA12D** for the Yageo 1 µF / 16 V / 0603 line is a clean electrical fit, but the distributor page I found marks it **obsolete**. citeturn610377search2
- For **KEMET C0402C151K5RACTU**, the Murata part is the only one I’m not fully happy with yet. The Murata candidate fits the naming pattern and appears on non-primary listings, but I have not verified it on a primary distributor page. citeturn262367search2turn262367search4
- Your **KYOCERA 06035C104KAZ2A** and the existing **Murata GRM188R72A104KA35D** are effectively the same electrical bucket, so that one is straightforward. citeturn870996search1turn870996search5

If you want, I’ll turn this into a **final owner-part list** with just:
**current part → Murata owner part → status (active / obsolete / provisional)**.

[M17] ME (2026-04-20 23:13):
[image]
Right, can you now provide tolerances line by line 
[attached file: IMG_4A8EACB4-9CC4-4310-BE95-462CBC640E90.jpeg]

[M18] AI (2026-04-20 23:14):
Yes — for the **Murata ceramic lines shown**, the tolerances are:

| Part number | Tolerance |
|---|---:|
| **GRM155R71H104KE4D** | **±10%** |
| **GCM188R71H102KA7J** | **±10%** |
| **GCM188R71C105K6Q4D** | **±10%** |
| **GCM188R71H103KA7D** | **±10%** |
| **GRM188R61E106MA73D** | **±20%** |
| **GRM39C390J50** | **±5%** |
| **GRM188R72A104KA35D** | **±10%** |
| **GCJ188R72A104KA1D** | **±10%** |
| **GRM188R72A391MA1J** | **±20%** |
| **GCM21BR71H105KA3K** | **±10%** |
| **GRM219R61E475KA3J** | **±10%** |
| **GRM21BZ71C106KE5L** | **±10%** |
| **GRM31CD71H106KE1L** | **±10%** |
| **GXT31CR6YA106KE1L** | **±10%** |
| **GRM32ER71E226KE15L** | **±10%** |
| **GRM55DR61H106KA88L** | **±10%** |

This lines up with Murata’s tolerance code convention in the part number:
**J = ±5%, K = ±10%, M = ±20%**. citeturn434893search4

A few spot checks from distributor/official pages also match that decoding:
**GRM155R71H104KE14D = ±10%**, **GRM188R61E106MA73D = ±20%**, **GRM32ER71E226KE15L = ±10%**, **GRM55DR61H106KA88L = ±10%**. citeturn821037search0turn821037search2turn434893search6turn434893search3

One note: your first line appears as **GRM155R71H104KE4D** in the sheet, but the standard Murata full part is normally **GRM155R71H104KE14D**. Same tolerance class either way. citeturn821037search0turn821037search12

If you want, I can do the **AVX tantalum tolerances next in the same paste-ready format**.

[M19] ME (2026-04-20 23:15):
And the avx yes 

[M20] AI (2026-04-20 23:15):
Yes — the **AVX / KYOCERA AVX TAJ-series** parts in your sheet decode as follows.

For these part numbers, the tolerance letter is the character after the case size:
- **K = ±10%**
- **M = ±20%** citeturn268132search0

So your lines are:

| Part number | Tolerance |
|---|---:|
| **TAJA106K010RNJ** | **±10%** |
| **TAJE107K025RNJ** | **±10%** |
| **TAJB106K016RNJ** | **±10%** |
| **TAJB156K016RNJ** | **±10%** |
| **TAJC106K010RNJ** | **±10%** |
| **TAJC107K010RNJ** | **±10%** |

All six of the AVX tantalums shown are therefore **±10%** parts. citeturn268132search0

If useful, the same decode also gives you:
- **A/B/C/E** = case size
- **106 / 107 / 156** = capacitance code
- **010 / 016 / 025** = voltage code
- **R** = reel / plating option
- **NJ** = standard suffix. citeturn268132search0

[M21] ME (2026-04-21 01:13):
Is there a way to turn on all “part name “ fields at once 

[M22] AI (2026-04-21 01:13):
Yes — in **Altium** you can usually do it in one go.

If you mean **show all component comment / part name strings on the schematic at once**:

### Schematic
Open the schematic, then use:

**Tools → Parameter Manager**  
or  
**Panels → SCH Inspector**

A quick way is:

1. **Select all components** on the sheet, or across sheets if needed.
2. Open **SCH Inspector**.
3. Find the visibility setting for the relevant string:
   - **Comment Visible**
   - **Designator Visible**
   - sometimes other parameter visibility depending on what you call “part name”
4. Set it to **True** for the whole selection.

If your “part name” is actually stored in the **Comment** field, turning on **Comment Visible** is the one you want.

### Across the whole project
If it is multiple sheets:

1. In the **Projects** panel, select the schematic documents you want.
2. Open **Parameter Manager**.
3. Filter for components.
4. Edit the visibility-related column or component comment handling in bulk.

### Faster method on one sheet
For a single schematic sheet:

1. Click one component with the field visible the way you want.
2. Right-click **Find Similar Objects**
3. Match **Object Kind = Component**
4. Select all matches
5. In **SCH Inspector**, set **Comment Visible = True**

That is often the cleanest mass-edit route.

### Important catch
If by “part name” you mean the **library symbol name** rather than the **comment/value shown on the sheet**, that is different. Normally Altium displays:
- **Designator**
- **Comment**  
not the internal library component name.

So in practice, most people wanting “part name” visible actually want **Comment Visible**.

If you tell me whether this is **schematic** or **PCB**, I’ll give you the exact click path.

[M23] ME (2026-04-21 02:55):
Is wson the same as Dfn?

[M24] AI (2026-04-21 02:55):
Not exactly.

**WSON** is usually a **type of DFN-style package**, but the terms are not always interchangeable.

Practical view:

- **DFN** = broad family name: **Dual Flat No-Lead**
- **WSON** = usually **Very/Thin Small Outline No-lead** style package, often used by some manufacturers for a no-lead plastic package with an exposed pad

So:
- **All WSONs are essentially in the DFN/QFN no-lead world**
- **But not every DFN is a WSON**

What matters for PCB/library use is not the label, but:
- body size
- pin count
- pitch
- pad geometry
- exposed pad size
- package height
- whether pins are on 2 sides only or 4 sides

A useful rule:
- **DFN / SON / WSON** often overlap heavily
- **QFN** normally implies pads on **4 sides**
- **DFN / SON / WSON** often implies pads on **2 sides**

But vendors are inconsistent, so never trust the family name alone.

For library mapping, I would treat **WSON as “DFN-like, verify dimensions”**, not as automatically identical.

If you have a specific part number, I can tell you whether that WSON can safely map onto an existing DFN footprint.

[M25] ME (2026-04-21 02:57):
[image]
This says it’s a dhc package 
[attached file: IMG_EED4AA6E-6C1E-470D-AC14-54ED940B97E4.jpeg]

[M26] AI (2026-04-21 02:57):
Yes — **DHC** here is the **manufacturer’s package code**, not the generic package family.

So in that screenshot:

- **DHC package** = the vendor’s internal code
- **16-lead (5 mm × 3 mm) plastic DFN** = the actual generic package style
- plus **exposed pad, pin 17**

So the correct interpretation is:

**DHC = a specific vendor-coded version of a 16-pin DFN with exposed pad**

That means when doing library/footprint work, do **not** search by “DHC” alone and assume cross-vendor equivalence. Use the actual physical definition:

- **DFN**
- **16 leads**
- **5 mm × 3 mm body**
- **exposed pad**
- then verify:
  - pitch
  - pad length/width
  - exposed pad size
  - overall land pattern recommendation

So this does **not** contradict DFN. It is basically saying:

**Package code: DHC**  
**Package family: DFN**

Very similar to how some vendors say things like:
- **RGE**
- **RTW**
- **MSOP**
- **QFN**
where one is the vendor code and one is the family descriptor.

For library naming, I would call it something like:

**DFN-16_EP_5x3mm_DHC**

That preserves both:
- the real package type
- the vendor code from the datasheet

If you want, I can help you decide whether your footprint should be named **DFN**, **WSON**, or **SON** for consistency.

[M27] ME (2026-04-21 02:58):
[image]
But I have this 16 pin wson…
[attached file: IMG_A615E9DB-E5AF-4B79-A23A-5109990429F5.jpeg]

[M28] AI (2026-04-21 02:58):
Yes — and that is exactly the trap.

Your **TI WSON-16** footprint may well be the **same package class** as that **DHC 16-lead DFN**, but you cannot assume it from the name alone.

What you have on screen is:

- **WSON-16**
- exposed pad
- leads on **2 sides**
- looks very much like a **DFN / SON style** land pattern

So in practical library terms:

- **WSON** and **DFN** are often overlapping descriptions
- **DHC** is just the datasheet’s package code
- the real question is whether the **dimensions match**

For your case, compare these four things against the datasheet mechanical package drawing, not just the pinout figure:

1. **Body size**  
   Your other part says **5 mm × 3 mm**. Check your footprint is also **5 × 3**.

2. **Pitch**  
   Count is 16, but the pitch must match too.

3. **Exposed pad size**  
   This is the big one. Even if the outer pins line up, the centre pad may be different.

4. **Terminal geometry**  
   Pad length, pad width, toe/heel allowance, and overall row span.

So the answer is:

- **A WSON-16 can absolutely be a valid footprint basis for a DFN-16 package**
- but **only if the mechanical dimensions match**
- **DHC** does not mean it is some totally different package family

Looking at your screenshot, it appears to be a **2-sided no-lead package with EP**, so conceptually it is in the right family.

What I would do:
- keep the footprint family under something like **SON/DFN/WSON 2-side no-lead**
- then verify the specific package against the mechanical table
- if it matches, reuse it
- if not, clone and make a variant

A sensible naming convention would be something like:

**SON_DFN_WSON-16_5x3_EP**

or, if you want vendor clarity:

**TI_WSON-16_5x3_EP**  
**DHC_DFN-16_5x3_EP**

If both resolve to the same land pattern, map both symbols to the same footprint.

The **pinout page you showed is not enough on its own** to confirm footprint identity. You need the **package dimensions / recommended land pattern** page. If you send that page, I can tell you whether your current WSON footprint is a safe match.

[M29] ME (2026-04-21 03:12):
How do you change the measurement default to mm

[M30] AI (2026-04-21 03:12):
In **Altium**, to make **mm** the default:

### While editing
Press **Q**  
That toggles between **mil** and **mm**.

### To set it more deliberately
In the PCB or PCB library editor:

- Open **View → Toggle Units** if available, or just use **Q**
- Then go to **Preferences** or the relevant document options and set units to **Metric**

### For PCB editor / PCB library
A reliable route is:

- **Tools / Preferences**
- look for **PCB Editor**
- set default units or display units to **mm**

### Also check grid units
Sometimes the document is in mm but the grid is still awkward. So also set:
- **Grid units = mm**
- choose a sensible grid like **0.05 mm**, **0.1 mm**, or **0.25 mm**

### Important Altium reality
Altium often stores dimensions internally regardless, and **Q** is the quick active-document switch. So for day-to-day use, **Q** is usually the main answer.

If you want, I can give you the exact path for:
**schematic**, **PCB**, or **PCB library**, because they behave slightly differently.

[M31] ME (2026-04-21 03:18):
How do you change the orientation of the dimension from vertical to horizontal 

[M32] AI (2026-04-21 03:18):
In **Altium PCB / PCBLib**, for a placed **dimension object**:

- **Click the dimension**
- Open the **Properties** panel
- Change the **Orientation** setting from **Vertical** to **Horizontal**

If it does not show as a simple orientation field, Altium often determines it from the two points you picked. In that case:

- **Select the dimension**
- **Drag one of its definition points**
- make the measured points run left-to-right for a **horizontal** dimension
- or top-to-bottom for a **vertical** one

If needed, the blunt method is:
- delete it
- place a new dimension
- pick the points in the direction you want

In many Altium versions, for **Linear Dimension**, there is also a right-click or properties option to swap the presentation style after placement, but dragging/replacing is often quicker.

If you want, send a screenshot of the selected dimension with Properties open and I’ll point to the exact field.

[M33] ME (2026-04-21 04:35):
[image]
Remind new me how inimport libraries files. I’m making a PCB library with files I have 
[attached file: IMG_F7FEB4C4-5F7C-49A9-82E2-0274D6EB4EBA.jpeg]

[M34] AI (2026-04-21 04:35):
Yes. If you already have a bunch of **.PcbLib** files and want them brought into your current Altium project/library setup, do this:

### Add existing PCB library files to the project
In the **Projects** panel:

1. Right-click **Libraries** or the project name
2. Choose **Add Existing to Project…**
3. Browse to your folder
4. Select the **.PcbLib** files
5. Click **Open**

That adds them into the project structure. It does **not** merge them into one file yet.

### If you want one master PCB library
Open your target **master .PcbLib**, then for each source library:

1. Open the source **.PcbLib**
2. In the **PCB Library** panel, select the footprint(s)
3. Right-click and **Copy**
4. Go to the master **.PcbLib**
5. **Paste**

That is the cleanest controlled method.

### Faster way if dragging works in your version
Sometimes you can:
- open both libraries
- use the **PCB Library panel**
- drag footprints from one library into the other

But copy/paste is usually safer.

### If they do not show in the open dialog
Check file type filter is set to:
- **PCB Library (*.PcbLib)**
or
- **All files**

### If you want the project to actively use them for components
Adding a **.PcbLib** to the project is one thing.  
Making symbols link to those footprints is another. For that you usually:
- keep the **.PcbLib** in **Libraries**
- then in the **SchLib** or component properties, point the footprint model to the footprint name in that library

### Good practical workflow
Since you are consolidating:
- create one **master PcbLib**
- add all donor libraries to project
- copy only the approved footprints into the master
- then remove the donor libs later

That avoids ending up with loads of scattered libraries again.

If you want, I can give you the exact process for **merging 30 PcbLibs into one master library without losing names**.

[M35] ME (2026-04-21 04:55):
What what’s the keyboard symbol for OR? And is a full stop 

[M36] AI (2026-04-21 04:55):
For Boolean / search / filter style use:

- **OR** is usually written as `|` or sometimes just the word **OR**
- a **full stop** is `.`

If you mean keyboard entry on Windows UK keyboard:

- `|` is the **pipe** symbol
- often on the key with backslash: `\|`
- full stop is the normal `.` key

If you are asking in an **Altium query** specifically, tell me the exact place:
- search
- filter
- query builder
- rule query

because Altium can be picky and often wants the word **OR** rather than a symbol.

=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===

[A1] ME (2026-04-20 22:44):
No the murals just 
