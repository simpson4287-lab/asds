# Temp Rated Coax Options
Date (UTC): 2026-02-13 09:08
Conversation ID: 698ee9f0-40fc-8390-a3fe-54549b21b148
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-02-13 09:08):
I’m looking for a temp rated coax. Similar tonight part number ACX1567-ND.
The part needs to be rated for 125 deg c

[M2] AI (2026-02-13 09:09):
ACX1567-ND is **Amphenol RF 135101-01-06.00**, an **SMA-to-SMA 6" assembly built on RG-316/U**. citeturn1view0turn2view0

If your key requirement is **125 °C**, the simplest “like-for-like but temp-safe” move is to stay with **PTFE/FEP coax families** (RG-316/U, RG-178, etc.). **RG-316/U is commonly specified to ~200 °C operating temp** (so 125 °C is comfortably inside spec). citeturn3search2turn3search4turn3search0

### Practical options (what to buy)
- **Direct drop-in (same as your reference):**  
  **Amphenol 135101-01-06.00 (ACX1567-ND)** — SMA-M to SMA-M, RG-316/U, 6". citeturn1view0turn2view0  
  *Note:* Digi-Key’s listing doesn’t state operating temp for the assembly, so for 125 °C work I’d treat the **cable spec + connector/boots/heatshrink spec** as the real limit.

- **Same idea, different geometries/lengths:**  
  The same Amphenol family has multiple lengths (12", 24", 36", etc.) on **RG-316/U**. citeturn1view0turn2view0

- **Smaller / more flexible than RG-316:**  
  **RG-178 (PTFE family)** is thinner than RG-316 and is also used for high-temp harnessing (check the exact jacket material/spec on the part you pick). Example stock parts exist at Digi-Key/Mouser. citeturn0product3turn0product7turn0product11

- **Bulk cable for building your own assemblies (guarantee the 125 °C spec):**  
  Buy **RG-316/U** from a vendor that explicitly states **-65…200 °C**, then terminate with SMA/MCX etc using **high-temp heatshrink/boots**. citeturn3search2turn3search4

products{"selections":[["turn0product2","Amphenol RF 135103-03-06.00 RG-316 assembly (Farnell UK)"],["turn0product1","Amphenol 135103-02-06.00 cable assembly (Mouser UK)"],["turn0product3","HUBER+SUHNER ENVIROFLEX_178 RG-178 cable (DigiKey UK)"],["turn0product11","HUBER+SUHNER RG_178_B/U cable (DigiKey UK)"],["turn0product7","HUBER+SUHNER RG_178_B/U cable (Mouser UK)"],["turn0product9","RS PRO SMA Series 1 m cable assembly (RS UK)"],["turn0product10","Amphenol RF 135104-03-12.00 RG-316 assembly 12in (Farnell UK)"],["turn0product6","RG316 RF Coaxial Cable (Amazon UK)"]],"tags":["RG-316 assembly","RG-316 assembly","Thin high-temp coax","Thin high-temp coax","Thin high-temp coax","Ready-made 1 m","RG-316 longer lead","Budget bulk RG316"]}

### Quick “don’t get bitten later” checklist for 125 °C
- Confirm **jacket material** (FEP/PTFE preferred) and the **published operating temperature** for the *specific cable* (not just “RG-316” generically). citeturn3search2turn3search4  
- Confirm the **connector + any overmold/boot/heatshrink** temperature rating (often the hidden limiter).
- If this is in an oven/hot zone: consider **strain relief** and **repeated flex** at temperature (FEP can creep).

If you tell me the **connector ends** you need (SMA–SMA like ACX1567-ND, or SMA–MCX/MMCX, U.FL, etc.) and **length**, I’ll narrow this to a tight short-list of exact orderable parts that explicitly clear **≥125 °C**.
