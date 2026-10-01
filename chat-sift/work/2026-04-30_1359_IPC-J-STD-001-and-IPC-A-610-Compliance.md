# IPC J-STD-001 and IPC-A-610 Compliance
Date (UTC): 2026-04-30 13:59
Conversation ID: 69f35ff9-c960-83eb-93ef-3a51e16394df
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-30 13:59):
If im setting out some ipc requirements is it the case that the supplier adheres to j-std-001 and is as receiver as ipc-610. Or is all ownership for both on supplier 

[M2] AI (2026-04-30 13:59):
I’ll frame this as a procurement/specification ownership question rather than just quoting standards, because the practical split matters: build process, workmanship acceptance, and who signs off nonconformances.

[M3] AI (2026-04-30 13:59):
Yes — broadly, **the supplier should own both compliance to J-STD-001 and delivery to IPC-A-610 acceptance criteria**, but they do different jobs.

The clean way to think about it is:

**J-STD-001 = process/build requirement**  
This defines how the soldered assembly shall be produced: materials, soldering workmanship, process control, cleaning, coating where applicable, inspection/verification criteria, etc. IPC describes it as covering materials, methods, and verification criteria for producing reliable soldered interconnections. citeturn876452search0turn876452search10

**IPC-A-610 = acceptability/inspection requirement**  
This defines how the finished assembly is visually judged: acceptable / process indicator / defect conditions for electronic assemblies. It is widely used as the end-product acceptance standard and is developed in synergy with J-STD-001. citeturn876452search3turn876452search5

So I would **not** write it as:

> Supplier shall build to J-STD-001; customer shall receive to IPC-A-610.

That creates a grey area where the supplier can say, “we built to J-STD-001; your incoming inspection is your issue.”

Better wording is:

> The supplier shall manufacture, inspect, and deliver assemblies in accordance with IPC J-STD-001 and IPC-A-610, Class [2/3], revision [x], unless otherwise stated on the drawing, purchase order, or agreed concession.

Then internally, yes, you as the receiver may use IPC-A-610 for **incoming inspection**, but that does not mean ownership sits only with you. The supplier should use the same acceptance criteria before shipment.

A good ownership split would be:

| Area | Primary owner | Standard |
|---|---:|---|
| Soldering process, materials, workmanship controls | Supplier | J-STD-001 |
| Finished assembly workmanship acceptance before shipment | Supplier | IPC-A-610 |
| Incoming inspection / goods-in acceptance | Customer, using same criteria | IPC-A-610 |
| Design intent, drawings, class, exceptions, special requirements | Customer |
| Concessions/deviations | Customer approval required |

For a supplier requirement, I’d use something like:

> Assemblies shall be manufactured and inspected by the supplier in accordance with IPC J-STD-001 and IPC-A-610, Class 2 unless otherwise specified. The supplier shall be responsible for ensuring delivered assemblies meet the applicable acceptance criteria prior to shipment. IPC-A-610 shall also be used by the purchaser for incoming inspection and dispute resolution, unless superseded by drawing notes, approved deviations, or specific contractual requirements.

For higher-reliability / flight / defence / critical test gear, use **Class 3** if justified. But don’t casually specify Class 3 unless the design, component selection, PCB fabrication, inspection burden, and cost expectations all support it. Class 3 is not just “better soldering”; it is a higher acceptance regime. J-STD-001 also recognises three end-product classes based on intended use and required reliability. citeturn876452search2

One important caveat: **drawing and purchase-order notes override generic IPC wording**. So if you have specific requirements — no-clean flux restrictions, ionic contamination, conformal coating, selective solder masking, hand-solder limits, staking, rework limits, X-ray, first article inspection, cleanliness evidence, certificates of conformity — they need to be explicitly called out. IPC alone won’t capture all project-specific expectations.

My recommendation for your requirement set:

> **Supplier owns compliance to both.**  
> **Customer uses IPC-A-610 as receiving/incoming acceptance.**  
> **J-STD-001 governs the build process.**  
> **IPC-A-610 governs finished assembly acceptability.**  
> **Drawings/PO/project requirements take precedence where more specific.**

[M4] ME (2026-04-30 14:00):
No we are the supplier but we sub contact assembly to another manufacturer 

[M5] AI (2026-04-30 14:00):
Right — in that case the ownership chain is:

**Your company remains the supplier to the customer.**  
**The subcontract assembler is your controlled manufacturing source.**

So contractually, you cannot really pass total ownership of IPC compliance “away” to the subcontractor as far as your customer is concerned. You can flow the requirements down, but **you retain responsibility for what is delivered under your name**.

A clean split would be:

| Layer | Owner |
|---|---|
| Customer requirement compliance | **You** |
| Flow-down of IPC / drawing / PO requirements to assembler | **You** |
| Actual PCB assembly manufacture | Subcontract assembler |
| Process compliance to J-STD-001 | Subcontract assembler, controlled by you |
| Finished assembly workmanship to IPC-A-610 | Subcontract assembler initially; you remain accountable |
| Final acceptance / release to your customer | **You** |
| Concessions / deviations to customer requirements | You, with customer approval where required |

So the subcontractor should be required to build and inspect to:

> **IPC J-STD-001 and IPC-A-610, Class [2/3], revision [x], plus all drawing, BOM, process and purchase order requirements.**

But internally, your position should be:

> We subcontract the physical assembly process, but retain responsibility for ensuring that delivered assemblies meet customer, drawing, IPC and contractual requirements.

The wording I’d use in your subcontract PO / manufacturing requirement would be:

> The subcontract manufacturer shall manufacture, inspect, test where applicable, and release PCB assemblies in accordance with IPC J-STD-001 and IPC-A-610, Class [2/3], revision [x], unless otherwise specified by the drawing, purchase order, build pack, or approved deviation.  
>   
> The subcontract manufacturer shall ensure that assemblies meet the applicable acceptance criteria prior to delivery. Any deviation from IPC, drawing, BOM, approved process, or workmanship requirements shall be formally notified and shall not be shipped without written approval.

Then for your own internal/customer-facing quality position:

> Assembly is performed by an approved subcontract manufacturer under flowed-down IPC and drawing requirements. Final responsibility for conformity of the delivered product remains with [your company].

That is the important distinction.

You can make the subcontractor **responsible for execution**, but you remain **accountable for compliance**.

For a requirements section, I would phrase it like this:

### IPC workmanship and soldering requirements

PCB assemblies shall be manufactured by an approved subcontract assembly provider in accordance with IPC J-STD-001 and IPC-A-610, Class [2/3], unless otherwise specified. These requirements shall be flowed down through the purchase order, drawing pack, BOM, assembly notes and any approved build instructions.

The subcontract assembly provider shall be responsible for process compliance, workmanship inspection and notification of any nonconformance prior to shipment. Final acceptance and customer-facing compliance responsibility shall remain with [your company].

Any deviation from the applicable IPC class, drawing notes, component fit, soldering workmanship, cleanliness, rework limits or agreed process requirements shall require written approval before product release.

[M6] ME (2026-04-30 14:01):
So we would need 610 verification to do it properly 

[M7] AI (2026-04-30 14:01):
Yes — **to do it properly, you need some form of IPC-A-610 verification/acceptance activity under your control**.

Not necessarily **100% reinspection of every joint**, but you need a credible mechanism that proves the subcontract assembler has delivered to the agreed IPC-A-610 class before you release the assembly onward.

A sensible model is:

| Activity | Who does it | Why |
|---|---|---|
| Manufacture to J-STD-001 | Subcontract assembler | Controls how the soldered assembly is produced |
| Workmanship inspection to IPC-A-610 | Subcontract assembler | Confirms the finished assembly meets acceptability requirements before shipment |
| Evidence of inspection / CoC / inspection report | Subcontract assembler provides | Gives you objective evidence |
| Goods-in / sample / risk-based verification to IPC-A-610 | You | Confirms supplier output and protects your customer-facing responsibility |
| Final release to customer/project | You | You remain accountable |

So I’d avoid thinking of it as:

> “The subcontractor says it is IPC compliant, therefore we are done.”

Better:

> “The subcontractor performs IPC-A-610 inspection, and we verify enough of it to maintain control of the outsourced process.”

For your system, that could be:

**Minimum acceptable approach**
- Subcontractor must be IPC-A-610 trained/competent.
- PO/build pack states IPC-A-610 Class 2 or Class 3.
- Subcontractor supplies CoC stating J-STD-001 / IPC-A-610 compliance.
- You perform goods-in visual inspection against IPC-A-610 on a defined sample or risk basis.
- You record inspection results and any escapes/nonconformances.

**Stronger approach**
- First article inspection on new builds.
- Photos of representative workmanship areas.
- Inspection report from subcontractor.
- Your incoming inspection checklist mapped to IPC-A-610.
- Higher sampling on first batch, new subcontractor, new design, high-risk components, hand-soldered areas, BGAs, fine pitch, rework, connectors, high-mass parts.
- Reduced sampling only after demonstrated performance.

The key point is:

> **IPC-A-610 is not only a receiving standard; it is the finished assembly acceptance standard.**

Your subcontractor should inspect to it before shipment, but **you need verification that they have done so effectively**, because you are the supplier of record.

A good internal requirement would be:

> The subcontract assembler shall inspect finished assemblies to IPC-A-610 Class [x] prior to shipment and provide certification of conformity. [Your company] shall perform incoming workmanship verification to IPC-A-610 on a risk-based sampling basis prior to final product release.

Or, slightly more formal:

> IPC-A-610 acceptance verification shall be retained by [your company] as part of the outsourced manufacturing control process. Verification may include review of subcontractor certification, inspection records, first article evidence, photographic evidence, goods-in inspection, or audit of subcontractor inspection competence.

So yes: **you need 610 verification**.  
But no: it does **not automatically mean you must duplicate the subcontractor’s full inspection** every time.

[M8] ME (2026-04-30 14:01):
I meant is as final supplier 

[M9] AI (2026-04-30 14:01):
Yes — **as final supplier, you should have IPC-A-610 acceptance capability or verification evidence before release**.

The important distinction is:

**You do not necessarily need to personally inspect every PCB assembly to IPC-A-610**, but you do need to be able to demonstrate that the assemblies you supply conform to the agreed acceptance standard.

So, as final supplier, “doing it properly” means you need one or more of these under your quality control:

1. **Flow-down requirement**
   
   Your PO/build pack to the subcontract assembler states:

   > Manufacture to IPC J-STD-001 and inspect to IPC-A-610 Class [2/3], plus drawing/build-pack requirements.

2. **Subcontractor declaration/evidence**
   
   The assembler supplies a CoC, inspection record, build traveller, FA report, photos, or other evidence stating the delivered assemblies meet IPC-A-610 Class [x].

3. **Your own release verification**
   
   You perform either:
   
   - incoming visual inspection to IPC-A-610 on a risk/sample basis, or
   - first-article verification, or
   - audit/review of subcontractor inspection records, or
   - targeted inspection of known-risk features.

4. **Competence to judge disputes**
   
   Someone on your side should be competent enough to assess IPC-A-610 accept/reject conditions, especially for customer returns, supplier NCRs, concessions, and goods-in escapes.

So the answer is:

> **Yes, as final supplier you retain responsibility for IPC-A-610 acceptance of the delivered assembly. The subcontractor may perform the inspection, but you need controlled evidence and/or verification before you release the product.**

A good wording for your internal process would be:

> Final assembly acceptance shall be based on IPC-A-610 Class [x], unless superseded by drawing or contract requirements. Where PCB assembly is subcontracted, the subcontractor shall perform IPC-A-610 inspection prior to shipment and provide evidence of conformity. Final supplier release shall include review of this evidence and, where appropriate, incoming or risk-based verification by [your company].

For a customer-facing position:

> PCB assembly is undertaken by an approved subcontract manufacturer under flowed-down IPC J-STD-001 and IPC-A-610 requirements. Final conformity of the supplied product remains the responsibility of [your company].

That is the cleanest model. The subcontractor owns the workmanship activity; **you own final conformity**.
