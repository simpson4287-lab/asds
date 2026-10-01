# Keysight 61010 Compliance Evidence
Date (UTC): 2026-05-15 08:12
Conversation ID: 6a06d550-73a4-83eb-822e-542285198d75
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-05-15 08:12):
Can you point me to evidence of jeysuhgt mainframe 61010

[M2] AI (2026-05-15 08:12):
Yes — there’s quite a lot of evidence, but it’s scattered through startup guides, regulatory sections, and declarations rather than a single “61010 certificate” page.

For Keysight PXI/PXIe chassis specifically, the strongest direct references are:

- urlKeysight M9018A PXIe Chassis Startup Guideturn0search4  
  This explicitly states the chassis complies with:
  - IEC/EN 61010-1
  - CSA C22.2 No. 61010-1
  - UL 61010-1

  It also references:
  - Installation Category II
  - Pollution Degree 2
  - grounding and disconnect requirements per IEC 61010. citeturn0search4

- urlKeysight PXIe Chassis Family Startup Guideturn0search1  
  This contains the regulatory/safety markings and compliance framework for the PXIe chassis family, including CE/UKCA/CSA style compliance markings associated with IEC 61010 safety certification. citeturn0search1

- urlKeysight TS-8900 PXI-Based Platform Technical Overviewturn0search3  
  This one is useful because it explicitly says:
  > “Complies with European Low Voltage Directive … IEC/EN 61010-1”  
  alongside UL/CSA references. citeturn0search3

The most useful wording for a compliance justification is probably this exact form from the M9018A guide:

> “This product is designed for use in Installation Category II and Pollution Degree 2, per IEC 61010...” citeturn0search4

and:

> “IEC/EN 61010-1” listed under safety compliance. citeturn0search4

If you are building a technical file or customer justification, the usual wording would be something like:

:::writing{variant="document" id="48127"}
The selected PXIe mainframe is a commercially manufactured Keysight Technologies instrument platform designed and certified for laboratory and measurement applications in accordance with IEC/EN 61010-1. Manufacturer documentation for the selected chassis family (e.g. Keysight M9018A PXIe chassis) identifies compliance with IEC/EN 61010-1, CSA C22.2 No. 61010-1, and UL 61010-1 safety standards, including Installation Category II and Pollution Degree 2 operating classifications.

Accordingly, the PXIe chassis is treated as an approved and independently safety-assessed subassembly within the overall system architecture.
:::

If you tell me the exact chassis — for example entity["product","Keysight M9018A PXIe Chassis"], entity["product","Keysight M9037A Embedded Controller"], entity["product","Keysight PXIe 1085 Chassis"] etc — I can probably find the exact declaration wording or DoC reference you can cite directly in your CDR or compliance section.

[M3] ME (2026-05-15 08:12):
Power n supply na nik ngtsm n

[M4] AI (2026-05-15 08:12):
I’m not quite sure what you meant there — could you rephrase it a bit?

If you mean the **Keysight power supplies** and whether they also show IEC/EN 61010 compliance, then yes — most of the bench/lab systems like the entity["company","Keysight Technologies"] N6700, N5700, E36xx, etc. explicitly reference IEC/EN 61010-1 in their manuals and declarations of conformity.

[M5] ME (2026-05-15 08:13):
Power s upoly mainframe 

[M6] AI (2026-05-15 08:13):
Yes — the entity["product","Keysight N6700 Modular Power System"] mainframes are also clearly tied to IEC/EN 61010 compliance.

Typical examples:

- urlKeysight N6700B Modular Power System Data Sheethttps://www.keysight.com/gb/en/assets/7018-02605/data-sheets/5990-6318.pdf  
- urlKeysight N6700 Series User Guidehttps://www.keysight.com/us/en/assets/9018-02607/user-manuals/9018-02607.pdf

The user/safety manuals normally include wording along the lines of:

- IEC/EN 61010-1
- CAN/CSA-C22.2 No. 61010-1
- ANSI/UL 61010-1

and define:
- Measurement Category II
- Pollution Degree 2
- indoor laboratory use

That is generally enough evidence to support statements such as:

:::writing{variant="document" id="51482"}
The Keysight N6700 modular power system utilised within the rack assembly is a commercially manufactured laboratory power platform independently assessed against IEC/EN 61010-1 safety requirements. Manufacturer documentation identifies compliance with IEC/EN 61010-1, UL 61010-1 and CSA 61010-1 standards for laboratory measurement and control equipment.

The power system is therefore treated as an approved safety-assessed subassembly within the overall equipment configuration.
:::

That is usually a much stronger engineering/compliance position than trying to argue bespoke internal mains distribution unless there is a hard system requirement forcing it.
