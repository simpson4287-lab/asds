# Altium CircuitStudio Overview
Date (UTC): 2026-02-23 10:25
Conversation ID: 699c2b07-5eb4-8384-98ae-e4518fab6c77
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-02-23 10:25):
What’s Latium circuit studio?

[M2] AI (2026-02-23 10:25):
**Altium CircuitStudio** (sometimes mis-typed as “Latium”) is Altium’s **mid-tier PCB CAD** package: a professional schematic + PCB layout tool positioned between the free/hobby tools and the full Altium Designer / Altium NEXUS stack. citeturn0search1turn0search0

What it’s for (in plain terms):

- **Schematic capture + PCB layout** in one environment (Altium-style workflow). citeturn0search1turn0search0  
- Aimed at **individual engineers / small teams** who want a “proper” PCB tool without the enterprise collaboration/management overhead. citeturn0search1turn0search0  
- Sold as a **perpetual license** with an optional subscription year for updates; licensing can be done via an offline-style license file (*.alf). citeturn0search2turn0search5  

If you tell me what you’re comparing it to (Altium Designer, CircuitMaker, KiCad, EasyEDA), I’ll map the *practical* differences—libraries, managed content, 3D/MCAD, constraints, output job/ODB++, etc.

[M3] ME (2026-02-23 10:26):
Is it included with enterprise?

[M4] AI (2026-02-23 10:26):
Usually **no** — **CircuitStudio isn’t automatically “included” just because you have an Altium *Enterprise* (Altium Designer / Altium 365) subscription**.

CircuitStudio has historically been sold as its **own product/license** (perpetual, with its own subscription/updates model). citeturn0search0 And Altium later positioned it as being **renamed/upgraded into “CircuitMaker Pro”** rather than being folded into Altium Designer tiers. citeturn0search4

What *can* make it “included” in practice:
- Your company’s **enterprise agreement** may have purchased **separate CircuitStudio/CircuitMaker Pro seats** as part of a bundle or add-on (that’s a commercial decision, not automatic).

Fast way to verify (no guesswork):
- Have your Altium license admin check **license entitlements** in your Altium account / licensing portal (or ask your reseller to list what products are covered). If you can tell me whether you’re on **Altium Designer Standard/Pro/Enterprise** and whether you see **CircuitStudio or CircuitMaker Pro** listed in entitlements, I’ll tell you exactly what that implies.

[M5] ME (2026-02-23 10:26):
What about circuit maker?

[M6] AI (2026-02-23 10:27):
**CircuitMaker** is Altium’s **free** PCB design tool (schematic + layout) built on **Altium Designer technology**. citeturn0search0turn0search2

Key points that matter in practice:

- **Separate product, not a “module” of Altium Designer Enterprise.** You can use CircuitMaker because it’s offered as a free tool, independently of your Designer/Enterprise licensing. citeturn0search0turn0search2  
- **Project/privacy model:** CircuitMaker 2.0 introduced **up to 5 private projects**; beyond that, projects are generally expected to be shareable (community/public). citeturn0search4  
- **Positioning:** It’s often described as an “Altium Designer Lite” experience—solid capture/layout/routing, but without the heavier enterprise-grade capabilities (advanced management/integrations/etc.). citeturn0search5  

Related nuance (because you asked about CircuitStudio earlier):
- Altium stated that **CircuitStudio was upgraded and renamed as “CircuitMaker Pro”** (i.e., the paid/pro tier concept). citeturn0search1turn2search0  

If you tell me what you’re trying to achieve (e.g., “I need unlimited private projects,” “I need managed components/365 workspace,” “I need full draftsmans/ODB++/rigid-flex rules”), I’ll point you to the least-painful option inside your Enterprise stack.
