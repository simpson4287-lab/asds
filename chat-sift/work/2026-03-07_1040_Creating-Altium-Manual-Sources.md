# Creating Altium Manual Sources
Date (UTC): 2026-03-07 10:40
Conversation ID: 69ac0094-9258-838f-aaef-fcf7b9457694
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-07 10:40):
If I wanted to create a manual for altium, where are the best sources 

[M2] AI (2026-03-07 10:40):
For creating an **Altium manual**, I’d build it from **three tiers of sources**:

**1. Official Altium documentation first.**  
This should be your backbone, because it is the most authoritative for commands, menus, workflows, terminology, and current feature behavior. The main technical documentation covers the product broadly, and Altium’s newer docs note that the documentation is no longer versioned in the old way, so you need to be careful to align what you write with the user’s actual installed release. citeturn0search6turn0search9

**2. Official tutorials and walkthroughs second.**  
Use Altium’s complete design walkthrough and quick-start material to structure the manual around real task flow rather than just alphabetic features. That is usually the difference between a reference manual and a usable working guide. Their walkthrough goes from project creation through outputs, which is a good skeleton for chapter order. citeturn0search1turn0search4

**3. Release notes and “What’s New” pages alongside the manual.**  
These are essential if you want the manual to stay accurate. Altium Designer 26 public release notes are current through February 5, 2026, and the “New in Altium Designer” page summarizes recent changes. I would use these to maintain a “version deltas” section so your manual doesn’t quietly drift out of date. citeturn0search2turn0search0

The best source mix, in practice, is this:

- **Primary source:** official Altium technical documentation  
- **Task-flow source:** official tutorials / Learning Hub  
- **Change-control source:** release notes / what’s new  
- **Gap-filling source:** internal screenshots, your own known-good workflows, and team conventions

For your case, I would not rely heavily on random third-party blogs or videos as the foundation. They can be useful for edge-case tricks, but for a manual they often go stale, especially around workspace features, UI changes, release flow, library handling, and manufacturing outputs. Official training also shows Altium’s intended workflow for UI, schematic, PCB layout, documentation, and fabrication outputs, which is better for a formal guide. citeturn0search16turn0search13

A strong manual structure would be:

1. **Environment and setup**  
2. **Projects and file types**  
3. **Libraries and component management**  
4. **Schematic capture**  
5. **Multichannel / reuse blocks / hierarchical design**  
6. **PCB import, rooms, classes, linking, ECO**  
7. **Rules, routing, polygons, planes, stackup**  
8. **Outputs: BOM, drawings, fabrication, assembly**  
9. **Release process / project releaser**  
10. **Troubleshooting and known failure modes**  
11. **Version-specific notes**

That last part matters because Altium’s documentation and release material show ongoing changes in design release, board view behavior, and broader platform capabilities. citeturn0search11turn0search15turn0search0

For a **really good manual**, the best raw material is often:

- official docs for correctness  
- your own screenshots for exact UI state  
- your own “failure / recovery” procedures for real usefulness

That means writing things like:
- “What the tool is”
- “When to use it”
- “Exact click path”
- “Expected result”
- “Common failure mode”
- “How to recover”

That approach tends to work much better than a generic software manual.

If you want, I can draft you a **proper Altium manual outline** next — either as a **general user manual**, or specifically tailored to the areas you keep hitting, like **libraries, multichannel, ECO/component linking, rooms, and PCB sync**.

[M3] ME (2026-03-07 10:41):
I want everything you can find using the structure you have identified 

[M4] AI (2026-03-07 10:42):
Absolutely. I’d build the manual from the structure below and use **official Altium documentation as the primary source base**, then layer in release notes and workflow pages to keep it accurate for current builds. Altium’s current docs are **not versioned the old way anymore**, and the latest public AD 26 release-notes page was updated on **February 5, 2026**, so version-awareness needs to be part of the manual from day one. citeturn0search0turn2search5turn0search11

## 1. Environment and setup

This section should explain what a project is, how to create the core design documents, and how to configure the working environment before doing any real capture or layout. The key official sources are the PCB environment setup page, the schematic capture entry page, and the project options page. Altium’s docs explicitly describe creating a new PCB document, then setting units, origin, grids, color display, and layer visibility early. The schematic docs likewise start from adding a schematic document into the PCB project. Project Options is important because it governs comparator behavior, class generation, rule handling, error reporting, and other project-wide behaviors that affect sync and ECOs later. citeturn1search8turn0search9turn1search6turn2search6

**Best source pages for this chapter**
- PCB Environment Setup. citeturn1search8
- Capturing Your Design Idea as a Schematic. citeturn0search9
- Accessing, Defining & Managing Project Options. citeturn1search6turn2search6

**What to cover in your manual**
Project creation, document types, units, snap/grid philosophy, origins, layer visibility, project options, compiler settings, and the difference between document settings and project settings. citeturn1search8turn0search9turn1search6

## 2. Projects and file types

A proper manual needs a concise model of Altium’s document ecosystem: project file, schematic sheets, PCB document, library documents, OutputJob, Draftsman, ActiveBOM, and release/history artifacts. The most useful sources are the schematic overview, PCB overview, manufacturing/output docs, Draftsman setup, Project History, and release pages. The Project History page is also useful because it reflects the newer solution model and the role of workspace-connected capabilities. citeturn0search9turn1search1turn0search11turn2search2turn1search5turn0search14turn0search7

**Best source pages**
- Capturing Your Design Idea as a Schematic. citeturn0search9
- Laying Out Your PCB. citeturn1search1turn2search8
- Preparing Your Design for Manufacture. citeturn0search11
- Preparing Manufacturing Data with Output Jobs. citeturn2search2
- Setting Up a Draftsman Document. citeturn1search5turn2search0
- Project History. citeturn0search14

**What to cover**
What each file type does, when it is authoritative, and how data flows from schematic to PCB to outputs to release package. citeturn0search11turn2search2turn0search7

## 3. Libraries and component management

This should be one of the biggest chapters. Altium’s official library documentation is strong here. The key page is the components-and-libraries launch page, then file-based libraries, component search, component updating, and footprint creation. The Components panel is explicitly described as the front door for **Workspace, database, and file-based libraries**, which makes it ideal for explaining the user-facing workflow before diving into library methodology. For file-based libraries, Altium also discusses supplier linking; for design maintenance, it documents how library changes are pushed back into live designs. citeturn0search15turn1search15turn1search7turn1search3turn1search11turn0search12

**Best source pages**
- Building & Maintaining Your Components and Libraries. citeturn0search15turn1search15
- File-based Component Libraries. citeturn1search7
- Searching for Components in Database and File-based Libraries. citeturn1search3
- Updating Components from Database and File-based Libraries. citeturn1search11
- Creating a PCB Footprint. citeturn0search12

**What to cover**
Library strategy, file-based vs database vs workspace components, symbol-footprint-model linkage, supplier data, parameter hygiene, library update workflows, footprint conventions, 3D bodies, and mechanical layer allocation. Altium’s footprint page specifically notes using mechanical layers consistently for extra detail such as courtyards, and adding 3D bodies for physical shape representation. citeturn0search12turn1search7turn1search11

## 4. Schematic capture

This chapter should start with basic capture but then quickly move to **connectivity, hierarchy, parameter sets, annotation, and compilation behavior**. The base sources are the schematic overview and the multi-sheet/hierarchical design page. For advanced design governance, project options and the constraints/parameter-set route are also important because schematic-side rules can be pushed through to PCB. citeturn0search9turn0search13turn1search6turn1search10

**Best source pages**
- Capturing Your Design Idea as a Schematic. citeturn0search9
- Multi-sheet & Hierarchical Designs. citeturn0search13
- Defining Design Requirements Using the Constraint Manager. citeturn1search10
- Accessing, Defining & Managing Project Options. citeturn1search6

**What to cover**
Sheet symbols, ports, harnessing as applicable, hierarchy methods, annotation philosophy, compiled view vs source sheets, parameter sets, and how connectivity is resolved across the project. The Navigator panel page is also helpful because it explicitly says navigation can be based on the compiled connective model of the active project. citeturn2search13turn0search13

## 5. Multichannel, repeated circuitry, and hierarchical reuse

For your own use case, this deserves a dedicated chapter. The official multi-channel design page is the core source. It explains the two main creation approaches, how the repeated circuitry is expanded at compile time, how PCB UIDs are formed in each case, and how component links are managed in the PCB editor. It also explicitly discusses the long-designator issue and the option to show logical rather than physical designators on the PCB. citeturn0search1

**Best source page**
- Creating a Multi-channel Design. citeturn0search1

**What to cover**
Repeated-sheet methods, repeat keyword usage, compiled expansion model, UID behavior, logical vs physical designators, component links, naming schemes, and documentation implications for BOM and fabrication outputs. The doc states that logical designators may be displayed on the PCB and outputs, while unique physical designators are still used for BOM generation. citeturn0search1

## 6. PCB import, synchronization, ECOs, component links, rooms, and classes

This is the chapter most people actually need when things go wrong. The synchronization page is the backbone here because it explains that Altium compares schematic and PCB directly using a comparator engine and then generates ECOs; there is no intermediate netlist-like document in the normal flow. Rooms and classes then need their own subsections. Project Options matters again because it controls rule/class generation, and the Component Links references inside the multi-channel page are highly relevant for repeated circuitry. citeturn0search5turn1search0turn2search6turn0search1

**Best source pages**
- Keeping the Schematics & PCB Synchronized. citeturn0search5
- Working with Rooms on a PCB. citeturn1search0turn1search2
- Accessing, Defining & Managing Project Options. citeturn2search6turn1search6
- Creating a Multi-channel Design. citeturn0search1

**What to cover**
Initial import to PCB, update directions, ECO review discipline, how and when to use component links, what rooms are, how classes are generated, when to disable auto-generated classes, and how comparator settings influence change behavior. Altium’s docs note that project options can automatically generate net classes for components, naming them `<ComponentDesignator>_Nets`, which is useful but can also create clutter if unmanaged. citeturn2search6turn0search5

## 7. Board setup, stackup, mechanical layers, rules, routing, polygons, and high-speed features

This should be the core PCB chapter. The PCB overview page is the main hub because it covers board shape, layers, routing, and stackup. The board-shape page, mechanical-layers page, rule-management page, routing page, interactive routing page, routing-rule-types page, high-speed page, and differential-pair page fill in the details. Altium’s PCB docs explicitly say the board is defined as a layer stack in the Layer Stack Manager, with core configuration on the Stackup and Via Types tabs. The routing docs also state that the system includes interactive routing, differential-pair routing, and interactive length tuning. citeturn1search1turn2search8turn1search9turn1search14turn1search4turn2search11turn2search7turn2search3turn1search13turn2search15

**Best source pages**
- Laying Out Your PCB. citeturn1search1turn2search8
- Defining the Board Shape. citeturn1search9
- Working with Mechanical Layers. citeturn1search14
- Defining, Scoping & Managing PCB Design Rules. citeturn1search4turn2search16
- Routing the PCB. citeturn2search11
- Interactive Routing. citeturn2search7
- Routing Rule Types. citeturn2search3
- High Speed Design. citeturn1search13turn2search12
- Differential Pair Routing. citeturn2search15

**What to cover**
Board shape creation, origin policy, stackup definition, via types, mechanical-layer conventions, design-rule scoping and priority, constraints manager, placement techniques, routing modes, diff pairs, matched lengths, and room-based constraints. The rule-management docs also make an important point: default rules that are required for DRC are recreated if deleted, so the correct practice is usually to disable unwanted defaults rather than remove them. citeturn1search4

## 8. Outputs: BOM, Draftsman, fabrication, assembly, and OutputJobs

This should be written as a controlled output workflow, not just a menu tour. Altium’s manufacturing docs say a large variety of outputs can be generated, and that the best way to manage them is with an **Output Job** file. The fabrication-data page then breaks out fabrication outputs, while Draftsman gives the documentation drawing route. For BOMs, Altium’s variants page explicitly says the **recommended approach is ActiveBOM**, even though BOMs can also be generated directly from schematic or OutputJob. citeturn0search11turn2search2turn2search4turn1search5turn2search0turn2search10

**Best source pages**
- Preparing Your Design for Manufacture. citeturn0search11
- Preparing Manufacturing Data with Output Jobs. citeturn2search2
- Preparing Fabrication Data. citeturn2search4
- Setting Up a Draftsman Document. citeturn1search5turn2search0
- Working with Variants in the Design. citeturn2search10

**What to cover**
OutJob architecture, data sources, Gerber/ODB++/drill/fab package generation, assembly drawings, fabrication drawings, Draftsman refresh behavior, BOM generation, and why ActiveBOM should be your master BOM environment. The Draftsman doc also states that it extracts design data directly from copper, component, and mechanical layers, and can be refreshed when PCB data changes. citeturn1search5turn2search0

## 9. Release process, workspace publication, and history

This chapter should explain the difference between simply generating outputs and doing a controlled release. The release pages are the key sources. Altium documents the Project Releaser as the main UI for high-integrity board design release, and it also documents releasing to a Workspace and, where configured, onward publication to PLM using templates. Project History is useful for showing what traceability and review look like after release. citeturn0search7turn0search3turn0search14

**Best source pages**
- Design Project Release. citeturn0search7
- Releasing to a Workspace. citeturn0search3
- Project History. citeturn0search14

**What to cover**
Release view, packaging rules, workspace publication, revision control expectations, release provenance, and how released data differs from ad hoc exports. citeturn0search7turn0search3turn0search14

## 10. Troubleshooting and known failure modes

This chapter should be assembled from multiple official pages rather than one source. The best anchors are sync/ECO, rules, rooms, component updating, project options, Draftsman refresh, and multi-channel documentation. These pages collectively cover the mechanics behind the problems users actually hit: component link mismatches, unwanted class generation, room behavior, PCB-only rules vs schematic-defined rules, long multichannel designators, stale outputs, and library update confusion. citeturn0search5turn1search0turn1search4turn1search11turn1search6turn1search5turn0search1

**Failure modes worth documenting**
ECO removes unexpected items, component links break after reused or repeated circuitry changes, rules reappear after deletion, Draftsman does not reflect board changes until refreshed, classes multiply due to project settings, and multichannel designators become unwieldy or misleading if logical/physical display is not understood. citeturn0search5turn1search4turn1search5turn2search6turn0search1

## 11. Version-specific notes and maintenance plan

This chapter is essential. Altium’s current docs and release pages make clear that the live documentation is current-focused, while older versions are handled through historical release notes and legacy documentation snapshots. That means your manual should include a version banner at the start of every procedure or at least every chapter. For example: “validated on AD 26.x” or “behavior may differ on older 24/25 series.” citeturn2search5turn0search4turn0search11

**Best source pages**
- Public Release Notes. citeturn2search5turn0search0
- New in Altium Designer. citeturn0search6turn2search14
- Historical Public Release Notes. citeturn0search4turn2search18
- Legacy documentation note on the manufacturing overview page. citeturn0search11

## My recommended source hierarchy for the manual

Use this priority order when writing:

**Tier 1 — core truth**
Official Altium technical documentation pages for each topic. citeturn0search9turn1search1turn0search15turn1search4turn2search2

**Tier 2 — current-behavior validation**
Public Release Notes and New in Altium Designer. citeturn2search5turn0search6

**Tier 3 — process and governance**
Project Releaser, Workspace release, Project History, Draftsman, ActiveBOM. citeturn0search7turn0search3turn0search14turn1search5turn2search10

**Tier 4 — your internal working method**
Your own screenshots, company standards, naming conventions, library policy, room policy, ECO review checklist, and failure-recovery playbooks.

## Best way to turn this into a real manual

For each chapter, write the same internal template:

**What it is**  
**When to use it**  
**Exact steps**  
**Expected result**  
**Common failure modes**  
**Recovery steps**  
**Version notes**  
**Linked Altium source pages**

That format works especially well for Altium because the same feature often behaves fine in the happy path but becomes tricky when a project already contains legacy links, multichannel expansion, rooms, generated classes, or PCB-only rules. Those behaviors are all documented, just spread across multiple pages. citeturn0search5turn0search1turn1search0turn1search4turn2search6

For your usage, I’d make the manual **less like a software encyclopedia** and more like this:

1. setup and standards  
2. libraries and components  
3. schematic capture  
4. multichannel and hierarchy  
5. schematic-to-PCB sync  
6. placement, rooms, classes  
7. rules and routing  
8. outputs and release  
9. troubleshooting

That would match the places you actually seem to hit friction. citeturn0search1turn0search5turn1search0turn1search4turn2search2

I can turn this into a full **chapter-by-chapter Altium manual skeleton with headings and subsection text**, ready for Word.

[M5] ME (2026-03-07 20:14):
List as many source links as possible here in a structured manor 

[M6] AI (2026-03-07 20:15):
Below is a **structured source map** for building an Altium manual, using **official Altium documentation** as the source base. I’ve grouped it by the manual structure we identified, and I’ve leaned toward pages that are either core hubs or directly useful for writing procedures. The official docs hub, current release notes, and project history pages are especially useful because they anchor the rest of the material and help you keep the manual aligned to current behavior. citeturn2search6turn1search4turn2search2

## 1. Core documentation hubs

- **Altium Designer Technical Documentation** — master entry point for the doc set. citeturn2search6
- **Public Release Notes** — current release notes for AD 26 family. citeturn1search4
- **Historical Public Release Notes** — older public release notes. citeturn1search7
- **New in Altium Designer** — use alongside release notes for change summaries. Mentioned from the release notes and main docs pages. citeturn1search4turn2search6

## 2. Environment, setup, projects, and documents

- **Creating Projects and Documents** citeturn2search8
- **Opening Projects and Documents** citeturn2search14
- **Managing Project Documents** citeturn2search17
- **Setting Up a Schematic Document** citeturn1search13
- **Data Management Preferences** — useful for local history / recovery behavior. citeturn1search16

## 3. Schematic capture fundamentals

- **Capturing Your Design Idea as a Schematic** citeturn1search0
- **Capturing the Schematic** — tutorial page. citeturn0search8
- **Schematic Placement & Editing Techniques** citeturn1search15
- **Working with Placed Components** citeturn2search12
- **Creating Circuit Connectivity in Your Schematics** citeturn1search11
- **Working with Directives on a Schematic** citeturn1search1

## 4. Multi-sheet, hierarchy, and reuse

- **Multi-sheet & Hierarchical Designs** citeturn1search6
- **Creating a Multi-channel Design** citeturn1search3
- **Working with Managed Schematic Sheets** — useful if you want a reuse / workspace-managed angle. citeturn1search17

## 5. Components, libraries, and part management

- **Building & Maintaining Your Components and Libraries** citeturn2search0
- **Component Types** citeturn2search9
- **File-based Component Libraries** citeturn2search1
- **Integrated Libraries** citeturn2search13
- **Schematic Libraries** citeturn2search10turn2search15
- **PCB Libraries** citeturn2search4
- **Creating & Defining the Database Library** citeturn2search16turn2search18
- **Modifying Symbols & Footprints** citeturn2search19
- **Updating Components from Database and File-based Libraries** citeturn2search3

## 6. PCB setup, board definition, and stackup

- **Defining the Layer Stack** citeturn0search14
- **Working with Rooms on a PCB** — relevant both for placement flow and autogenerated-room behavior. citeturn0search1turn1search9

## 7. Schematic–PCB synchronization, ECOs, rooms, and classes

- **Managing Design Changes between the Schematic & PCB** citeturn0search9turn0search12
- **Working with Rooms on a PCB** citeturn0search1turn1search9
- **Working with Classes on a Schematic & PCB** citeturn0search5turn0search16

## 8. Rules, constraints, routing, and high-speed work

- **Defining, Scoping & Managing PCB Design Rules** citeturn1search8
- **Routing Rule Types** citeturn0search6
- **High Speed Design** citeturn0search2
- **High Speed Rule Types** citeturn0search10

## 9. Outputs, reports, Draftsman, BOM, and manufacturing data

- **Preparing Manufacturing Data with Output Jobs** citeturn0search0turn1search5
- **Preparing Reports** citeturn0search11turn2search11
- **Preparing Outputs and Releasing the Project** — tutorial-style workflow page. citeturn0search7turn1search10
- **Working with Tables** — useful for Draftsman BOM tables and output-driven documentation. citeturn1search12
- **Working with the Variant Manager** — important for variant-aware documentation and BOMs. citeturn0search15

## 10. Release process, workspace release, and traceability

- **Releasing to a Workspace** citeturn0search18turn1search2
- **Project History** citeturn2search2
- **Preparing Outputs and Releasing the Project** citeturn0search7turn1search10

## 11. Good “glue” pages to use between chapters

These are useful when writing a manual because they bridge practical workflow rather than just documenting isolated features:

- **Capturing the Schematic** citeturn0search8
- **Preparing Outputs and Releasing the Project** citeturn0search7turn1search10
- **Creating Projects and Documents** citeturn2search8
- **Managing Design Changes between the Schematic & PCB** citeturn0search9turn0search12
- **Project History** citeturn2search2

## 12. Suggested priority order for writing the manual

For the actual manual build, I’d use this order:

- **Tier 1:** docs hub, schematic, sync, libraries, rules, outputs, release notes. citeturn2search6turn1search0turn0search9turn2search0turn1search8turn1search5turn1search4
- **Tier 2:** multichannel, hierarchy, rooms, classes, variants. citeturn1search3turn1search6turn0search1turn0search5turn0search15
- **Tier 3:** tutorial workflow pages and project-history pages for user-facing procedure flow. citeturn0search8turn0search7turn2search2

## 13. Compact copy-paste source list

You can lift this straight into a planning document:

- Altium Designer Technical Documentation citeturn2search6  
- Public Release Notes citeturn1search4  
- Historical Public Release Notes citeturn1search7  
- Creating Projects and Documents citeturn2search8  
- Opening Projects and Documents citeturn2search14  
- Managing Project Documents citeturn2search17  
- Setting Up a Schematic Document citeturn1search13  
- Capturing Your Design Idea as a Schematic citeturn1search0  
- Capturing the Schematic citeturn0search8  
- Schematic Placement & Editing Techniques citeturn1search15  
- Creating Circuit Connectivity in Your Schematics citeturn1search11  
- Working with Directives on a Schematic citeturn1search1  
- Multi-sheet & Hierarchical Designs citeturn1search6  
- Creating a Multi-channel Design citeturn1search3  
- Working with Managed Schematic Sheets citeturn1search17  
- Building & Maintaining Your Components and Libraries citeturn2search0  
- Component Types citeturn2search9  
- File-based Component Libraries citeturn2search1  
- Integrated Libraries citeturn2search13  
- Schematic Libraries citeturn2search10turn2search15  
- PCB Libraries citeturn2search4  
- Creating & Defining the Database Library citeturn2search16turn2search18  
- Modifying Symbols & Footprints citeturn2search19  
- Updating Components from Database and File-based Libraries citeturn2search3  
- Defining the Layer Stack citeturn0search14  
- Managing Design Changes between the Schematic & PCB citeturn0search9turn0search12  
- Working with Rooms on a PCB citeturn0search1turn1search9  
- Working with Classes on a Schematic & PCB citeturn0search5turn0search16  
- Defining, Scoping & Managing PCB Design Rules citeturn1search8  
- Routing Rule Types citeturn0search6  
- High Speed Design citeturn0search2  
- High Speed Rule Types citeturn0search10  
- Preparing Manufacturing Data with Output Jobs citeturn0search0turn1search5  
- Preparing Reports citeturn0search11turn2search11  
- Working with Tables citeturn1search12  
- Working with the Variant Manager citeturn0search15  
- Releasing to a Workspace citeturn0search18turn1search2  
- Project History citeturn2search2  
- Preparing Outputs and Releasing the Project citeturn0search7turn1search10  

Next, I can turn this into a **numbered manual bibliography** or a **chapter-by-chapter source pack**.

[M7] ME (2026-03-07 20:18):
Can you produce in a table? Or excel sheet?

[M8] AI (2026-03-07 20:21):
Yes — I put it into an Excel workbook with:

- **Sources** sheet: full structured table
- **Summary** sheet: section counts

Download it here: [altium_manual_sources.xlsx](sandbox:/mnt/data/altium_manual_sources.xlsx)

If you want, I can also paste a **markdown table version** directly in chat.
