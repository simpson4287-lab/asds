# Removing U_ Prefix in Altium
Date (UTC): 2026-03-20 05:48
Conversation ID: 69bcdf95-3cfc-8389-b0c4-fecb37444092
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-20 05:48):
[image]
Is it going to get fussy if I remove the U it puts on the start of sheets?
[attached file: IMG_D620E2D6-A6A1-4FE9-A4E0-F618A12FBE1C.jpeg]

[M2] AI (2026-03-20 05:48):
No — generally Altium will not care if you remove the `U_` prefix from a **sheet symbol designator/name** like `U_OS0`, **provided you are only changing the sheet symbol’s displayed designator/comment and not breaking any managed references or parameter-driven naming you rely on**.

In your case, changing `U_OS0` to just `OS0` is usually fine.

What matters is this:

- **Ports / sheet entries / net names** are what drive connectivity.
- The **sheet symbol name/designator** is mostly an identifier for the block in the hierarchy.
- Altium does **not** require sheet symbols to begin with `U_`. That is more a convention than a rule.

Where it can get fussy:

1. **If you already reference that exact sheet symbol name elsewhere**
   - Cross-references, harnessing, scripts, or generated docs might expect `U_OS0`.

2. **If this came from a repeated-sheet or multichannel naming convention**
   - Sometimes people use `U_` to visually distinguish hierarchical blocks from nets or channels.
   - Removing it won’t usually break compile, but it can make the hierarchy a bit less explicit.

3. **If it is actually a parameter being used somewhere**
   - For example, if `U_OS0` is tied to a compiled channel identifier, variant script, or custom output naming.

Best way to judge:
- Rename **one** sheet symbol from `U_OS0` to `OS0`
- Compile
- Check for:
  - sheet entry mismatches
  - duplicate identifiers
  - broken cross references
  - any script/output naming issues

My expectation from what you’ve shown: **it should be fine**.

A sensible convention would be:
- Sheet symbol/block name: `OS0`
- Actual components inside keep normal designators like `Uxx`, `Rxx`, etc.

That tends to read cleaner on block diagrams.

One caution: if you have several blocks with similar names, make sure `OS0`, `OS1`, etc. stay unique at that hierarchy level.

If you want, I can also tell you the cleanest distinction in Altium between:
- sheet symbol name
- sheet file name
- sheet title
- designator/comment  
because those get mixed up a lot and are often the source of this sort of confusion.

[M3] ME (2026-03-22 04:17):
Some guys at works in forever moaning about having a tidy and standard library. I finally stepped forwards and he’s already trying to steer me towards his product standardgot tv

[M4] AI (2026-03-22 04:17):
That sounds very predictable.

What often happens is:
you step up to solve a genuine **library governance** problem, and someone immediately tries to reframe it as **their preferred product standard**, because that gives them influence over the outcome.

Those are not the same thing.

A **tidy, standard library** should usually mean things like:
- consistent naming
- controlled metadata fields
- clear symbol/footprint/3D ownership
- defined approval/release states
- duplication reduction
- sensible parameter standards
- predictable schematic and PCB representation
- auditable change control

It should **not automatically mean**:
- “everything must follow my preferred component philosophy”
- “all parts must be built in the style I like”
- “my product team’s way becomes the company-wide rule”
- “library cleanup becomes a stealth design-standard takeover”

So the key move is to separate:

**1. Library hygiene / governance**  
from  
**2. Product design standards / engineering policy**

That gives you a defensible boundary.

A good line to hold is something like:

> I’m happy to define a consistent library standard for symbol quality, footprint quality, metadata, lifecycle state, and naming. Product-specific design rules are a related but separate discussion and shouldn’t be conflated with core library governance.

That is the cleanest position because it sounds collaborative, but it stops the scope-creep.

You could frame your library effort around a few neutral pillars:

**Library standard should cover**
- naming convention
- revision control
- approved metadata fields
- symbol drawing rules
- footprint creation rules
- 3D model policy
- supplier/manufacturer link policy
- status model: draft / review / released / obsolete
- duplicate prevention
- ownership and change approval
- migration/legacy handling

**Separate design standard should cover**
- preferred resistor package sizes
- default derating rules
- grounding philosophy
- connector choices
- EMC layout preferences
- bias rail conventions
- test point policy
- product-family specific conventions

That way, if he pushes “product standard,” you can calmly say:
“Useful input, but that belongs in the engineering design standard, not the base library standard.”

Also, politically, be careful not to become the person who “owns every opinion.”  
Better to become the person who owns the **framework**.

So instead of arguing specific preferences, say:
- “Let’s define what is mandatory at library level.”
- “Let’s classify what is optional, preferred, and product-specific.”
- “Let’s separate CAD quality from circuit design philosophy.”
- “Let’s avoid hard-coding one team’s preferences into the global library.”

That keeps you in the stronger systems role.

A very practical way to structure it is with three layers:

**Level 1 — Mandatory library rules**  
Non-negotiable CAD/data quality rules.

**Level 2 — Recommended engineering conventions**  
Common good practice, but not always mandatory.

**Level 3 — Product/program-specific rules**  
Only apply where relevant.

That prevents endless arguments because not everything has to be forced into one bucket.

Honestly, if you want credibility here, I’d avoid making it sound like “my standard versus his.”  
Make it sound like:
**scope control, governance, and classification**.

That is much harder to argue with.

A strong sentence for meetings would be:

> My aim is to standardise the library so it is clean, reusable, and governed. I’m not trying to turn the central library into a proxy for one product team’s design preferences.

That lands well because it is firm without being confrontational.

You are probably in a good position here, because the person who frames the categories usually controls the conversation more than the person arguing the preferences.

If you want, I can draft you a one-page **Library Governance Charter** that draws this boundary very clearly and professionally.

[M5] ME (2026-03-22 04:22):
A weird example is he wants to do it all
Properly but is using the comment field for showing and finding part numbers which I feel is sloppy and wrong

[M6] AI (2026-03-22 04:22):
Yes — that is exactly the kind of thing worth pushing back on.

Using the **Comment** field to hold or drive **part numbers** is usually bad library architecture.

Why it is sloppy:

**1. Comment is presentation-oriented, not identity-oriented**  
The Comment field is typically for what you want to **see on the schematic**:
- value
- functional description
- human-readable label

It is not a clean master identifier.

**2. Part number is a controlled data attribute**  
Manufacturer part number, internal company part number, supplier part number, and library item ID are all different things. Those should live in **dedicated parameters/fields**, not be stuffed into Comment.

**3. It creates ambiguity**  
If Comment says `10k 1% 0402` on one part and `RC0402FR-0710KL` on another, you’ve mixed:
- engineering description
- purchasing identity
- manufacturer identity

That gets messy very fast.

**4. Searchability becomes crude and brittle**  
He may be thinking:
“if I put the part number in Comment, I can find it quickly.”

That works in a primitive way, but it’s a workaround for not having a proper searchable parameter structure.

Better is:
- `Company_PN`
- `Manufacturer`
- `Manufacturer_PN`
- `Description`
- `Value`
- `Package`
- `Tolerance`
- `Voltage`
- `Lifecycle State`

Then you can search properly and consistently.

**5. Schematic readability suffers**  
The Comment field is often what gets shown to designers. If it is overloaded with procurement identifiers, the schematic becomes less readable and more admin-heavy.

**6. It causes maintenance pain**  
If the part number changes, alternates are added, or a company numbering scheme evolves, now the displayed schematic text is tangled up with your database logic.

A much cleaner principle is:

> **Comment = what the designer should see**  
> **Parameters = what the system should know**

That is probably the sharpest way to state it.

For example:

**Good split**
- **Comment:** `10k 1%`
- **Description:** `RES 10k OHM 1% 0.1W 0402`
- **Company_PN:** `RES-0402-10K-1`
- **Manufacturer_PN:** `RC0402FR-0710KL`
- **Manufacturer:** `Yageo`

Or for ICs:
- **Comment:** `Low Noise Op Amp`
- **Description:** `Dual low-noise JFET input op amp`
- **Company_PN:** internal code
- **Manufacturer_PN:** actual orderable device

Now, to be fair, some teams do abuse Comment because:
- legacy CAD tools were limited
- old libraries evolved informally
- people want quick search from the schematic side

But that does not make it good practice. It just means it became a habit.

The deeper issue is this:
he may be treating the library as a **visual filing cabinet**, whereas you are thinking of it as a **controlled engineering data model**.

Your approach is the stronger one.

A calm way to challenge it would be:

> I think we should keep Comment reserved for the human-readable schematic display and use dedicated parameters for internal or manufacturer part numbers. Otherwise we blur presentation with identity, which makes the library harder to govern and maintain.

Or slightly firmer:

> Using Comment as the primary carrier for part numbers may work as a convenience shortcut, but it is poor separation of concerns for a governed library.

That phrase “separation of concerns” is useful here. It makes the objection sound architectural rather than personal.

You could even propose a simple rule:

**Library field intent**
- **Designator** = instance identity
- **Comment** = displayed engineering label/value
- **Description** = fuller functional text
- **Parameters** = searchable controlled attributes
- **Part choice / MPN fields** = procurement identity

That is a very defensible standard.

Honestly, this is the exact sort of thing that distinguishes:
- a library built for short-term convenience
from
- a library built for scale, reuse, auditability, and migration.

You are not being awkward here — you are spotting a real data-model problem.

I can help you turn this into a concise **library field usage policy** with “shall / should / shall not” wording, which would give you something much more solid than just arguing opinions.

[M7] ME (2026-03-22 04:25):
See I’ve been using value and tolerance as parameters displayed and left comment to be purely superset info.

[M8] AI (2026-03-22 04:25):
That is a much cleaner model.

What you’re doing is closer to proper **attribute separation**:

- **Value** = electrical identity
- **Tolerance** = performance attribute
- **Displayed parameters** = explicit engineered data
- **Comment** = broader descriptive/superset information

That is far more disciplined than stuffing everything into Comment.

Why your approach is strong:

**Displayed parameters are deliberate**  
If you show `10k` and `1%` as parameters, the schematic is saying exactly what matters electrically. It is explicit and structured, not just a blob of text.

**Comment stays flexible**  
Leaving Comment for broader descriptor text means it can carry a generic part-family description without becoming the master source of truth for identity.

**It scales better**  
Once you start needing filters, automation, database linking, BoM handling, alternates, or auditability, parameterised fields hold up much better than Comment-driven conventions.

**It avoids text parsing nonsense**  
A library becomes fragile when people must infer meaning from a free-text comment like:
`10k 1% 0402 thick film`
instead of just reading discrete fields.

So architecturally, your instinct is sound.

The only thing I’d tighten is this:

If by “superset info” you mean Comment contains a broad descriptor like:
`RESISTOR CHIP GENERAL PURPOSE`
or
`OP AMP LOW NOISE DUAL`

then that’s reasonable.

But if Comment starts becoming a catch-all for:
- value
- tolerance
- package
- voltage
- MPN
- internal code

then it drifts back into the same mess.

A very robust model is:

- **Comment** = concise human-readable description or family label
- **Value** = electrical nominal value
- **Tolerance** = tolerance
- **Package / Case** = package attribute
- **Voltage / Power / Tempco** = explicit parameters
- **MPN / company PN** = controlled identity fields
- **Description** = fuller text for reports/BOMs/library search

For resistors, for example:

- Comment: `Chip Resistor`
- Value: `10k`
- Tolerance: `1%`
- Package: `0402`
- Power: `0.063W`
- Manufacturer_PN: actual orderable code

Or, if you want the schematic to read more naturally, Comment could be:
`10k`
while tolerance is separately displayed. That can also work well.

The key principle is:
**displayed text should be assembled from structured fields, not used as a substitute for them.**

So yes — your method is more defensible than his.

The tradeoff is that some people like Comment because it is quick and visually familiar. But that is really a convenience habit, not a good governance model.

A good line to use with him would be:

> I’d rather keep the electrically meaningful attributes as discrete parameters and display those directly, instead of encoding them into Comment. That preserves searchability, consistency, and downstream data quality.

Or even more crisply:

> Comment should not be doing the job of structured data.

That is probably the heart of it.

One extra thought: if you are trying to standardise this across a team, don’t frame your method as “my preference.” Frame it as:

- **free text fields are weakly governed**
- **structured parameters are strongly governed**
- therefore **critical engineering attributes should live in structured parameters**

That turns it from taste into engineering logic.

I can help you define a proper field map for passives, ICs, connectors, and electromechanical parts so you’ve got a concrete standard rather than just an argument.
