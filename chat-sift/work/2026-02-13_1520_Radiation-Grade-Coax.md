# Radiation Grade Coax
Date (UTC): 2026-02-13 15:20
Conversation ID: 698f4144-e6ec-838a-9376-a6eaf2300208
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-02-13 15:20):
What is some typical radiation grade coax 

[M2] AI (2026-02-13 15:20):
Radiation-grade coaxial cable is specified for environments where **total ionising dose (TID), displacement damage, vacuum, and temperature extremes** would rapidly degrade standard polymer-dielectric RF cable.

Given your background in sensor / vacuum / burn-in systems, I’ll frame this in terms of materials science and failure mechanisms rather than catalogue parts.

---

# 1️⃣ What Makes a Coax “Radiation Grade”?

Radiation primarily attacks:

- **Polymer dielectrics** (cross-linking, embrittlement, dielectric constant drift)
- **Jacket materials** (cracking, outgassing)
- **Adhesives**
- **Foamed dielectrics** (collapse under dose)

Radiation-tolerant designs therefore use:

| Element | Radiation-tolerant choice | Why |
|---------|--------------------------|-----|
| Dielectric | Solid PTFE, PFA, FEP | Excellent TID resistance |
| Conductor | Silver-plated copper, copper-nickel | Stable, low activation |
| Shield | Braided silver-plated copper | Mechanical robustness |
| Jacket | PFA / ETFE / Kapton | Radiation + vacuum stability |
| No foams | Solid dielectric only | Foams trap gas & degrade |

---

# 2️⃣ Common Radiation-Tolerant Coax Types

## 🔹 PTFE Semi-Rigid Coax (Most Common)

image_group{"layout":"carousel","aspect_ratio":"1:1","query":["semi rigid coax cable PTFE dielectric","semi rigid coax stainless steel outer conductor","RG405 semi rigid coax","semi rigid coax cut cross section PTFE"],"num_per_query":1}

**Typical examples:**
- RG405 (.086")
- RG402 (.141")
- Custom semi-rigid assemblies

**Why it’s used:**
- Solid PTFE dielectric
- No trapped gas
- Excellent radiation tolerance
- Excellent vacuum compatibility
- Stable impedance

**Dose capability:**  
Often >10⁶ rad (10 kGy) and beyond depending on application.

Used extensively in:
- Particle accelerators
- Space systems
- Nuclear instrumentation

---

## 🔹 Mineral Insulated (MI) Coax (Extreme Environments)

image_group{"layout":"carousel","aspect_ratio":"1:1","query":["mineral insulated coax cable","magnesium oxide insulated coax cable","nuclear instrumentation coax cable mineral insulated","MI coax cable cross section magnesium oxide"],"num_per_query":1}

**Construction:**
- Copper or stainless outer
- Magnesium oxide dielectric
- Solid metal sheath

**Radiation performance:**  
Essentially immune to ionising radiation damage.

**Used in:**
- Reactor cores
- High-dose gamma fields
- Severe temperature + radiation combined

Trade-off:
- Expensive
- Hard to terminate
- Limited flexibility

---

## 🔹 Space-Grade PTFE / ETFE Coax

image_group{"layout":"carousel","aspect_ratio":"1:1","query":["space grade coax cable ETFE jacket","radiation resistant coax cable aerospace","silver plated copper PTFE coax aerospace","NASA radiation tolerant coax cable"],"num_per_query":1}

Often custom assemblies using:

- ETFE jacket
- Solid PTFE dielectric
- Silver-plated conductors
- Low outgassing qualification

Radiation tolerance varies, but commonly qualified for:
- GEO mission doses
- Proton / heavy ion exposure

---

# 3️⃣ Typical Radiation Ratings (Order of Magnitude)

| Cable Type | TID Capability |
|------------|----------------|
| Standard PVC coax | <10⁴ rad |
| PE dielectric coax | 10⁴–10⁵ rad |
| Solid PTFE coax | 10⁶+ rad |
| Mineral insulated | Effectively radiation immune |

(Actual spec always manufacturer-specific.)

---

# 4️⃣ For Your Use Case (Sensor / 125 °C / Long Runs?)

Given your recent high-temp and sensor discussions:

If you need:
- 125 °C rating
- 50 MHz range
- Possibly vacuum compatible
- Potential radiation exposure

The sensible baseline choice is:

✔ **Solid PTFE semi-rigid (.086" or .141")**
✔ Silver plated copper
✔ Stainless outer if mechanical robustness needed

Avoid:
- Foamed dielectric
- PVC jacket
- Consumer RG58 variants

---

# 5️⃣ Manufacturers Known for Radiation-Tolerant Coax

- entity["company","Times Microwave Systems","us rf cable manufacturer"]
- entity["company","Huber+Suhner","swiss connectivity manufacturer"]
- entity["company","Gore","w l gore company"]
- entity["company","Thermocoax","france mineral insulated cables"]
- entity["company","Habia Cable","swedish specialty cable manufacturer"]

These all supply aerospace / nuclear / accelerator-grade options.

---

If you want to narrow this properly, tell me:

- Expected total ionising dose?
- Neutron flux or gamma only?
- Vacuum or air?
- Required bend radius?
- Frequency / impedance?
- Cable length?

We can then converge on something realistic rather than generic catalogue advice.

[M3] ME (2026-02-13 15:22):
Is there any commercially available options 

[M4] AI (2026-02-13 15:22):
For **commercially available radiation-tolerant / radiation-resistant coax options**, the market isn’t like standard RG-58 or LMR cables you can buy off the shelf — you’re looking at specialised products designed for aerospace, nuclear, and research environments. These *can* be ordered in reasonable quantities, though often through specialist distributors rather than consumer-grade catalogues. citeturn0search3turn0search6turn0search1

### 📦 Examples You Can Source

#### 🧪 1. **PTFE & Kapton Radiation-Resistant Coax**
These are semi-rigid / flexible coax cable types with **solid PTFE dielectric** and in some cases **Kapton insulation**, rated for high doses (e.g., >1×10^9 rad). citeturn0search3turn0search6  
- These are sold by specialised technical suppliers (example product lines seen on European cable supplier sites). citeturn0search3  
- They’re suitable for **UHV, high temperature, and radiation environments**.

✔ Typical specs:  
- Solid PTFE or Kapton dielectric  
- Silver-plated copper conductors  
- OD ~1.4 mm (depending on type)  
- Radiation tolerance >10^9 rad (model dependent)  
- Often used in vacuum chambers, accelerator instrumentation, space harnesses. citeturn0search3turn0search6

To order, suppliers like Allectra sell these as “312-PTFE-COAX-SR” and similar lines, which you can purchase in fixed lengths or reels. citeturn0search3

#### 🪐 2. **Space / Aerospace Grade Coax Assemblies**
Several manufacturers produce **space-qualified coax assemblies** that are engineered to withstand radiation, thermal cycling, vibration and vacuum outgassing — not glue/foam coax like typical consumer cables. citeturn0search12turn0search17

These aren’t usually “off-the-shelf” reels but are sold as assemblies or cables with connectors, and often documented for NASA/ESA compatibility:
- ETFE jacketed coax series (e.g., SpaceNXT™ QT Series) with radiation-resistant materials. citeturn0search12  
- Space flight coax assemblies from specialist RF cable makers intended for commercial satellites. citeturn0search17

You order these from specialist distributors or directly from manufacturers like Smiths Interconnect, Axon’ Cable, or Times Microwave Systems — often to spec.

#### 🛠 3. **Radiation-Resistant Cable Manufacturers**
Companies that engineer cables for nuclear reactors, particle accelerators, and fusion experiments offer coax categories on request. citeturn0search1turn0search5

Examples of environments they serve:
- Nuclear power instrumentation  
- Aerospace harnesses  
- Medical accelerator facilities  
- Research labs (e.g., CERN) citeturn0search1

They commonly use advanced materials (Kapton, polyimide, mineral insulation, high-temp fluoropolymers) to ensure long life under ionising radiation, extreme heat, and vacuum. citeturn0search1

---

### 📌 Where *Not* to Buy Just Yet

Consumer-grade coaxial cables such as typical RG-58, RG-6, LMR, etc. (e.g., entity["turn0product1","HRG58 High-Voltage RF Coaxial Cable",0], entity["turn0product12","LMR-240-DB Coaxial Cable",0]) are **not rated for radiation environments** and will degrade rapidly under significant ionising dose. These are fine for lab RF but *not* for radiation tolerance.

---

### 🛒 Summary of Commercially Available Options

- **Radiation-resistant PTFE/Kapton coax** — available in reels/lengths from specialised suppliers. citeturn0search3  
- **Space / aerospace grade coax assemblies** — ready-to-use with connectors, radiation-tolerant materials. citeturn0search12  
- **Custom/engineered specialist cables** from radiation cable manufacturers — can cover coax needs on request. citeturn0search1

---

### 💡 Ordering Tips

If you want something you can *buy without custom engineering*:

1. Contact precision cable suppliers that list PTFE/Kapton coax products (e.g., Allectra or similar) and request part numbers for the cable you need with:
   - impedance (typically 50 Ω),
   - radiation spec (e.g., >10⁶ or >10⁹ rad),
   - temperature/vacuum requirements.

2. For assemblies with connectors included, look at space-grade coax series from RF cable specialists — they often have priced catalog parts with standard connectors.

If you’d like, tell me your **frequency range, radiation dose requirement, and environment (vacuum/air/temperature)** and I’ll narrow down specific product references you could order.

[M5] ME (2026-02-13 15:22):
Non vacuum 

[M6] AI (2026-02-13 15:23):
Absolutely — if your application **doesn’t involve vacuum** (i.e., just air or controlled gas environments) but **does involve radiation exposure**, you still have commercially available coax options that are **rad-tolerant without needing ultra-high-vacuum materials**.

Here’s a clear breakdown of practical, off-the-shelf coax you can source:

---

## 🧪 1. **Radiation-Tolerant PTFE Coax**

These are the most common **commercially available** radiation-hard coax cables that will work in **non-vacuum air environments**.

### Typical Construction
- **Solid PTFE dielectric** (not foam)
- Silver-plated copper conductors
- PTFE or fluoropolymer jacket (e.g., FEP, ETFE)
- 50 Ω / 75 Ω versions exist

### Why They’re Good for Radiation
- PTFE resists ionising dose far better than polyethylene/foam dielectrics
- Jacket materials like ETFE and FEP tolerate radiation without embrittling quickly
- No trapped gas pockets (like in foam cables) that degrade under dose

### Commercially Available Examples
You can purchase these from specialized cable suppliers — often by part number or cut-to-length.

- **RG-405** — Solid PTFE, semi-rigid, 50 Ω  
- **Custom PTFE flexible coax** with ETFE jacket  
- **PTFE insulated coax from RF cable houses** that specify high radiation tolerance

*Note:* Radiation tolerance will vary by spec sheet, but solid PTFE cables are routinely rated for **10⁶ rad and higher** (depending on vendor). This is suitable for many electronic test environments and moderate radiation chambers.

---

## 🔄 2. **Space / Aerospace-Grade PTFE Coax (Non-Vacuum Use)**

There are many aerospace coax products that are **qualified for temperature cycling, humidity, and radiation**, but they don’t require vacuum compatibility.

These are often sold as assemblies with connectors, but you can usually request custom lengths.

Examples of materials used:
- PTFE dielectric
- ETFE jacket
- Silver-plated conductors
- Low outgassing based on aerospace standards (even though vacuum isn’t needed, the materials are robust)

You can find these from:
- OEM RF cable houses
- Space cable distributors

They’re priced higher than consumer coax but **commercially orderable in modest quantities**.

---

## 🔌 3. **High-Temperature Fluoropolymer Coax**

If your environment also has elevated temperature in addition to radiation (e.g., up to ~125 °C), look for:
- **FEP- or ETFE-jacketed coax**
- Solid PTFE dielectric
- Rated temperature up to ~150 °C

These are often available in catalog form (e.g., PTFE-FEP cables) and are used in industrial RF and nuclear gauge instrumentation.

---

## ⚠️ What *Not* to Use

Avoid these for radiation environments even in air:
- Foam dielectric cables (e.g., typical RG-58/6 variants)
- PVC jackets
- Gel-filled cables
- Standard consumer LMR cables (low radiation tolerance)

These degrade quickly under even moderate ionising dose.

---

## 📌 How to Order Today

### Step 1 — Define Key Specs
You’ll want the following minimal spec to get a good commercial part:
- **Impedance:** usually 50 Ω (common choice)
- **Frequency range:** define (e.g., DC–500 MHz, 1 GHz, etc.)
- **Radiation tolerance requirement:** e.g., **≥10⁶ rad**
- **Temperature range:** e.g., up to 125 °C
- **Mechanical form:** flexible vs semi-rigid

### Step 2 — Choose a Supplier
Many RF cable houses sell PTFE cables in stock or with short lead times in batches:

| Supplier Type | What They Offer |
| ------------- | ---------------- |
| Precision RF cable houses | PTFE coax in cut-to-length / reels |
| Space / aerospace distributors | Radiation-tolerant assemblies |
| Specialist industrial cable stock | High temp PTFE / ETFE cable |

You can order by part number or request a quote based on your spec.

---

## 🧠 In Practice

For an environment that’s **non-vacuum but radiation exposed**, a typical **solid PTFE coax with an ETFE or FEP jacket** hits the best balance of:
- Radiation tolerance
- Flexibility
- Temperature capability
- Commercial availability

It’s the default choice for:
- Radiation test stands
- Sensor instrumentation in irradiated areas
- Nuclear gauge cabling in air environments

---

If you want, you can share a couple specifics like **frequency range, required bend radius, and estimated radiation dose** and I’ll recommend a few precise parts you can order from suppliers today.

[M7] ME (2026-02-13 15:26):
Would this be any good for twisted pairs in radiation? https://itm-components.co.uk/products/shielded-cat-5e-plenum-cable-rj45-rj45-1500-ft

[M8] AI (2026-02-13 15:26):
Here’s a clear assessment of whether standard twisted-pair Ethernet cable like **entity["turn0product3","Cat5e F/UTP Shielded Foil Twisted Pair Data Cable",0]** or similar shielded Cat 5e options (from your link) would be suitable in a radiation environment:

### 🚫 **Standard Ethernet Twisted Pair Is *Not Radiation-Tolerant***

**Cat5e/Cat6 Ethernet cable**, even when shielded and plenum-rated for building code:
- Uses **polyolefin/PE insulation and PVC/FEP jackets**
- Is specified for **electromagnetic interference (EMI) performance** in communications — not for radiation environments  
- Has **no meaningful specification for ionising radiation** resistance in datasheets

Standard networking cables are designed for signal integrity in office/data-centre environments, *not* for exposure to gamma, neutron, or other ionising fields. Typical insulation materials in Cat5e will degrade (embrittle, crack, change dielectric properties) at relatively low radiation doses compared to specialised radiation-tolerant cable materials. citeturn0search11

> In other words: shielding in Cat5e is *for EMI/RFI*, not for protection against radiation effects on the cable materials. citeturn0search12

### ✔ **What “Shielding” Actually Does in Cat5e**
Shielded twisted pair means there’s a foil or braid around the pairs to reduce:
- Crosstalk and electromagnetic interference  
- External noise coupling into the cable

This helps with network performance near motors, RF sources, or power electronics — *but does not protect insulation from ionising radiation damage*. citeturn0search4

### ❗ Performance Under Radiation
Radiation affects cables by:
- Breaking polymer chains in insulation/jacket materials  
- Causing embrittlement and cracking  
- Changing dielectric constant (affects signal quality)  
- Accelerating chemical degradation

Commercial networking cables aren’t tested or specified for these effects — they’ll degrade quickly under even moderate total ionising dose (TID) relative to specialised cables. citeturn0search0

### 🧠 When Standard Twisted Pair *Might* Be Okay
If your use case has extremely low dose rates or very limited radiation exposure (like incidental scatter in a lab far from sources), Cat5e might survive *short-term* — but this is an **unreliable** strategy unless the dose is quantified and proven very low.

### ✅ Radi-Tolerant Alternatives for Twisted Pairs
For electrical signal pairs in a radiation field, look for cables with insulation and jacket materials that are known to withstand ionising dose, such as:
- **PTFE / PFA / ETFE insulated twisted pairs**
- Radiation-qualified telecom/mil-spec data cables from aerospace suppliers
- Specialty polyimide or mineral insulated pairs (for high dose)

These are *designed* for radiation environments and will endure far higher accumulated dose than consumer Cat5e.

---

## 🧾 Bottom Line

| Cable Type | Designed for Radiation? | Suitable as a Twisted Pair in Rad Field? |
|------------|------------------------|-----------------------------------------|
| Standard Cat5e shielded (e.g., your example) | ❌ No | ❌ Not recommended without qualification |
| Custom high-rad tolerance twisted pair (PTFE/ETFE) | ✅ Yes | ✅ What you want for reliability |

If you can share the **approximate radiation level (total dose)** and **frequency / signal type** you intend to carry over the pairs, I can point you at specific **radiation-qualified twisted-pair cable part numbers** that you could source commercially.
