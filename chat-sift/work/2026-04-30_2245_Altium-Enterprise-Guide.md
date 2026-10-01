# Altium Enterprise Guide
Date (UTC): 2026-04-30 22:45
Conversation ID: 69f3db85-7314-83eb-9825-d11f402472d1
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-30 22:45):
New chat about altium enterprise user guide 

[M2] AI (2026-04-30 22:45):
I’ll treat this as a fresh thread on getting started with Altium Enterprise/Altium 365 and the available published user guidance, rather than trying to reconstruct the old chat. I’ll check current official Altium material so the links and product names are up to date.

[M3] AI (2026-04-30 22:45):
For the **Altium Enterprise / user guide** topic, the current useful split is:

## 1. If you have Altium 365 / cloud Workspace

Start here:

**Altium 365 technical documentation**  
Altium describes Altium 365 as the cloud platform connecting design, data management, collaboration, procurement, fabrication, and assembly. citeturn891770search7

Also useful:

**Complete Design Walkthrough with Altium Designer + connected Workspace**  
This is probably the best “start from zero” guide because it walks through Altium Designer while connected to a Workspace. citeturn891770search1

## 2. If you have on-prem Altium Enterprise Server

Start here:

**Altium On-Prem Enterprise Server documentation**  
This is the current on-prem product documentation. It covers the managed server model: secure storage, revisions, release management, and integration with Altium Designer. citeturn891770search4

Key admin/startup pages:

**Installation, Licensing & Management**  
Covers install, licensing, updating, backup/restore, and server management. citeturn891770search17

**Enterprise Server FAQs**  
Good for practical setup questions. One useful point: a new installation provides a single Git-based design repository called **Versioned Storage** for Workspace projects. citeturn891770search14

## 3. Concord Pro warning

If your company or old paperwork says **Concord Pro**, note that Altium’s current documentation says Concord Pro has been discontinued and that PCB design, data management, and collaboration are now handled through **Altium Designer + connected Altium 365 Workspace**. citeturn891770search2

So the terminology may have shifted:

| Old / legacy wording | Current likely equivalent |
|---|---|
| Concord Pro | Altium 365 Workspace or On-Prem Enterprise Server |
| Managed Server | Workspace / Enterprise Server |
| Managed Components | Workspace Components |
| Released Components | Component revisions/lifecycle |
| Server libraries | Workspace libraries / managed content |

## Where I’d start in your case

Given what you said previously — server finally up after a year, no clear training package, and you want to avoid being upsold — I’d approach it in this order:

1. **Confirm product type**: Altium 365 cloud Workspace or On-Prem Enterprise Server.
2. **Get login and admin rights clarified**.
3. **Do not migrate the whole library first.**
4. Create a small pilot structure:
   - one component type,
   - one lifecycle scheme,
   - one naming convention,
   - one approved resistor/capacitor/component example,
   - one test PCB project using managed components.
5. Only then define the wider company process.

The main published material is definitely there; it is not some hidden proprietary training-only system. The training hours may help, but the core user/admin guidance is available publicly from Altium.

[M4] ME (2026-04-30 22:48):
It’s an on premise enterprise setup. Create a manual on everything it can do and links 

[M5] AI (2026-04-30 22:49):
Below is a **practical manual / capability map** for an **Altium On-Prem Enterprise Server** setup. It is written as a “what can it do, why would we use it, where is the official guide” document.

---

# Altium On-Prem Enterprise Server Manual  
## Capability Guide for Engineering / Library / IT / Configuration Control

## 1. What the On-Prem Enterprise Server is

Altium On-Prem Enterprise Server is a locally hosted Workspace, managed by your own IT department, that works with Altium Designer to control PCB design data, components, templates, releases, lifecycle states, permissions, collaboration, and manufacturing output packages. Altium describes it as secure local storage with revisioned release management, so design data can be re-released as separate revisions rather than overwritten. citeturn199438search1

Official starting point:  
**Altium On-Prem Enterprise Server documentation** citeturn199438search1

The key point is this: it is **not just a component library server**. It is intended to manage design work-in-progress, released design outputs, managed components, models, templates, permissions, lifecycles, tasks, and process workflows. Altium’s FAQ specifically says you *can* use it only for components, but that this is not recommended because one of its main strengths is managing everyday PCB work-in-progress and creating relationship links such as “Where Used”. citeturn199438search7

---

# 2. Main capability areas

## 2.1 Workspace / browser interface

The Enterprise Server provides a browser-based interface for admin and engineering access. Users can access the local server by entering the server address in a browser, such as `http://<ComputerName>:<PortNumber>` or `http://localhost:<PortNumber>` when on the same machine. citeturn574782search16

Typical browser-side functions include:

| Area | What it is used for |
|---|---|
| Components | Browse managed components and their detailed data |
| Projects | View, create, upload, share, edit, and manage Workspace projects |
| Explorer | Browse Workspace folders, items, releases, templates, models |
| Admin | Configure users, groups, permissions, licences, settings |
| Processes | Manage workflows such as part requests and design/project activities |
| Tasks | Manage assigned activities using a Kanban-style flow |
| PLM Integration | Configure data exchange with enterprise systems |
| Team Configuration Center | Control designer environment settings |

Official guide:  
**Exploring the Browser-Based Interface** citeturn574782search16

---

# 3. Project management

## 3.1 Workspace projects

The Enterprise Server can store and manage Altium PCB projects directly inside the Workspace. This allows projects to be shared, reviewed, commented on, released, and controlled from a central managed environment. The Workspace Projects documentation covers project creation, upload, editing, sharing, and management via the browser interface. citeturn199438search16

Official guide:  
**Workspace Projects** citeturn199438search16

### Practical use

For your company, this means you can move away from loose project folders scattered across network drives and instead have controlled project storage with clearer ownership and traceability.

A sensible starting policy would be:

| Project type | Recommended handling |
|---|---|
| Active product design | Workspace project |
| Legacy design under support | Imported gradually when touched |
| Experimental / throwaway test | Keep outside initially unless needed |
| Released production design | Release through Project Releaser |

---

## 3.2 Versioned storage

A new Enterprise Server installation provides Git-based project storage called **Versioned Storage** for Workspace projects. This gives controlled versioning for design work rather than unmanaged file copying. citeturn199438search7

Official guide:  
**Enterprise Server FAQs** citeturn199438search7

### Practical use

This is valuable for:

| Problem | Enterprise Server benefit |
|---|---|
| “Which version did we build?” | Released project revision |
| “Who changed this?” | Version history |
| “Where is the latest project?” | Workspace project source |
| “Was this output generated from the correct source?” | Project release process |
| “Can we recover an earlier state?” | Versioned project history |

---

# 4. Design release and manufacturing output

## 4.1 Project Releaser

Altium Designer’s **Project Releaser** can release a board design into the connected Workspace. The Workspace hosts the target release repository. The release process uses Output Job files to generate formal outputs such as fabrication files, assembly files, PDFs, reports, and manufacturing packages. citeturn199438search2

Official guides:  
**Design Project Release** citeturn199438search2  
**Releasing to a Workspace** citeturn199438search5  
**Preparing Outputs and Releasing the Project** citeturn199438search11

### What it can produce/control

| Release item | Typical examples |
|---|---|
| Source snapshot | Controlled copy of the exact design source |
| Fabrication data | Gerbers, ODB++, NC drill, fabrication drawings |
| Assembly data | Pick-and-place, assembly drawings, BOM |
| Documentation | Schematic PDFs, PCB prints, reports |
| Generated output package | Formal release package stored in Workspace |
| Release revision | Distinct revision of the released design |

The big advantage is that a release becomes a **controlled product output**, not just a manually zipped folder.

---

## 4.2 Downloading release packages

Released design packages can be downloaded from the Workspace browser interface. Altium’s documentation states that extraction of any and all releases of design projects is done by downloading those release packages from within the Workspace. citeturn199438search17

Official guide:  
**Extracting Data from a Workspace** citeturn199438search17

### Practical use

This is the route for:

| User | Need |
|---|---|
| Engineer | Recover released outputs |
| Manufacturing | Obtain the formal build pack |
| Quality | Check what was released |
| Configuration control | Identify approved release revision |
| Purchasing | Access controlled BOM outputs |

---

# 5. Components and library management

## 5.1 Workspace components

The Enterprise Server can hold managed components in the Workspace. The browser interface allows users to browse components, see how many are available, and view detailed data for each part. citeturn199438search15

Official guides:  
**Workspace Components** citeturn199438search15  
**Building & Maintaining Components and Libraries** citeturn199438search8  
**Working with Component Folders and Items** citeturn199438search14

### What a managed component can include

| Element | Purpose |
|---|---|
| Component symbol | Schematic representation |
| PCB footprint | Physical land pattern |
| 3D model | Mechanical representation |
| Parameters | Value, tolerance, voltage, manufacturer, internal code |
| Datasheet link | Technical reference |
| Part choices | Manufacturer / supplier options |
| Lifecycle state | Draft, prototype, approved, obsolete, etc. |
| Revision | Controlled history of changes |

---

## 5.2 Component folder structure

The Workspace can organise components into structured folders. This is where your company can impose a clean library architecture rather than allowing dozens of overlapping local libraries.

Recommended initial structure:

```text
Components
├── Passives
│   ├── Resistors
│   ├── Capacitors - Ceramic
│   ├── Capacitors - Tantalum
│   ├── Capacitors - Aluminium
│   └── Inductors
├── Semiconductors
│   ├── Diodes
│   ├── Transistors
│   ├── Op-Amps
│   ├── Logic
│   ├── Power Management
│   └── Interfaces
├── Connectors
├── Electromechanical
├── Optoelectronics
├── Mechanical
├── Test Points
└── Company Controlled / Special Parts
```

Do not over-design this on day one. Start with a structure that fits real company usage, not a theoretical taxonomy.

---

## 5.3 Supply chain data

Workspace component supply chain data can be sourced from Octopart. Altium also notes that some organisations instead source supplier data from an internal enterprise system, for example where approved vendors or special pricing structures are required. citeturn574782search3

Official guides:  
**Workspace Components** citeturn574782search3  
**Part Source Configuration** citeturn574782search23

### Practical use

This can help with:

| Capability | Benefit |
|---|---|
| Supplier visibility | See availability and sourcing data |
| Approved part control | Prefer approved suppliers |
| Obsolescence awareness | Identify risky parts earlier |
| Alternate part choices | Link multiple manufacturer parts to one company component |
| Internal part source | Use company-approved data instead of public supply chain only |

---

# 6. Lifecycle management

The Enterprise Server allows administrators to define and manage lifecycle definitions through the browser interface. Altium describes these lifecycle definitions graphically, showing states and transitions. citeturn199438search9

Official guide:  
**Lifecycle Management** citeturn199438search9

### Typical lifecycle examples

For components:

```text
Draft → In Review → Prototype → Approved → Deprecated → Obsolete
```

For projects:

```text
Work In Progress → Review → Released → Superseded → Archived
```

For templates:

```text
Draft → Approved → Retired
```

### Practical use

Lifecycle states answer questions like:

| Question | Lifecycle value |
|---|---|
| Can this component be used in a new design? | Approved / not approved |
| Is this symbol still being checked? | Draft / In Review |
| Is this design output valid for manufacture? | Released |
| Has this part been replaced? | Deprecated / Obsolete |
| Is this template company-approved? | Approved |

For your situation, this is one of the most important areas because it lets you formalise “approved library” behaviour rather than relying on tribal knowledge.

---

# 7. Where-used and traceability

Enterprise Server’s strength is not just storing components; it creates links between library and design content, supporting functions such as **Where Used**. Altium’s FAQ specifically calls this out as a benefit of managing both design work-in-progress and library content in the server. citeturn199438search7

Official guide:  
**Enterprise Server FAQs** citeturn199438search7

### Practical use

Where-used is important when:

| Scenario | Why it matters |
|---|---|
| Component becomes obsolete | Find affected designs |
| Library error found | Identify all designs using affected footprint/symbol |
| Manufacturer part removed | Assess product impact |
| Requirement changes | Locate dependent designs |
| Quality issue found | Trace exposure across projects |

This is why using Enterprise Server only as a fancy component library is underusing it.

---

# 8. Content structure and access control

## 8.1 Folder and item permissions

The Enterprise Server allows managed content to be shared and permissioned. Altium notes that default folder share permissions may allow full write access for Workspace members unless configured otherwise. citeturn574782search4

Official guide:  
**Managing Content Structure & Access** citeturn574782search4

### Practical use

A controlled setup should avoid “everyone can edit everything”.

Suggested permission model:

| Area | Engineers | Librarians | Admins |
|---|---:|---:|---:|
| Approved components | View/use | Edit/release | Full |
| Draft components | View/use selectively | Edit | Full |
| Templates | View/use | Edit/release | Full |
| Released outputs | View/download | Manage | Full |
| Admin settings | No access | Limited | Full |

---

## 8.2 Users and groups

User management is performed by an Administrator through the Admin area of the Workspace browser interface. It uses the Identity Service to define users and groups. citeturn574782search0

Official guide:  
**Managing Users & Groups** citeturn574782search0

### Recommended groups

```text
Administrators
Library Administrators
PCB Designers
Project Leads
Reviewers
Manufacturing / Production Viewers
Quality / Configuration Control
Read Only Users
```

For a company rollout, groups are better than individual permissions. It keeps the system maintainable.

---

# 9. Tasks and collaboration

## 9.1 Tasks

Enterprise Server includes a Tasks feature for creating and managing job activities for Workspace members. Altium describes it as a visual Kanban-board style flow, with statuses such as `ToDo`, `InProgress`, and `Resolved`. citeturn199438search13

Official guide:  
**Working with Tasks** citeturn199438search13

### Practical use

Tasks can be used for:

| Task type | Example |
|---|---|
| Library correction | “Check footprint for connector J12” |
| Design review action | “Resolve clearance issue near mounting hole” |
| Documentation action | “Regenerate assembly PDF” |
| Release action | “Confirm OutJob includes IPC-2581 output” |
| Manufacturing query | “Check alternate part for C104” |

---

## 9.2 Comments, review, and project activities

Processes can include project activities such as design reviews and publishing to PLM. Altium’s process documentation identifies Project Activities as a dedicated area for processes related to Workspace projects. citeturn199438search6

Official guide:  
**Creating & Managing Processes** citeturn199438search6

This is useful if you want design reviews to become a formal workflow rather than ad-hoc Teams messages and marked-up PDFs.

---

# 10. Part requests

Enterprise Server supports formal part request workflows. The documentation covers configuration, starting a request, and viewing a request from the Workspace perspective. citeturn199438search0

Official guide:  
**Part Requests** citeturn199438search0

### Practical use

A part request process can stop uncontrolled library growth.

Example workflow:

```text
Engineer requests part
→ Librarian checks need and duplication
→ Footprint / symbol created or reused
→ Datasheet and parameters checked
→ Lifecycle set to Prototype or Approved
→ Part released to Workspace
```

### Suggested part request fields

| Field | Why it matters |
|---|---|
| Requested manufacturer part number | Identifies requested part |
| Internal part number | Links to company system |
| Reason for request | Avoids unnecessary duplicates |
| Project needing it | Provides priority/context |
| Voltage/current/package constraints | Prevents wrong variant |
| Datasheet link | Source data |
| Preferred supplier | Purchasing alignment |
| Urgency | Workload prioritisation |
| Equivalent existing part checked? | Prevents library bloat |

---

# 11. Process workflows

Enterprise Server supports Workflows, created as part of Process Definitions. These are managed through the browser interface by a Workspace Administrator. citeturn574782search22

Official guide:  
**Creating & Managing Processes** citeturn574782search22

### Useful workflow candidates

| Workflow | Purpose |
|---|---|
| New component request | Control new library entries |
| Component change request | Control edits to existing approved parts |
| Project design review | Formalise review gates |
| Release approval | Confirm output package is acceptable |
| Obsolescence review | Manage impacted designs |
| Template change request | Control company documentation standards |

This area is powerful but should be introduced after the basic library/project structure is working.

---

# 12. Team Configuration Center

Enterprise Server includes **Environment Configuration Management** through the **Team Configuration Center**. Altium describes this as a way to centrally control the environment designers operate in, constraining Altium Designer to use company-ratified design elements such as schematic templates, Output Job files, and Workspace preferences. citeturn574782search12

Official guides:  
**Environment Configuration Management** citeturn574782search12  
**Managing Environment Configurations** citeturn574782search8

### Practical use

This is one of the best company-standardisation features.

It can help enforce:

| Controlled item | Example |
|---|---|
| Schematic templates | Company title block |
| PCB templates | Standard layer stack / rules starter |
| Output Jobs | Approved release output pack |
| Preferences | Company design environment settings |
| Draftsman templates | Standard fabrication/assembly drawings |
| Managed content access | Approved templates and library elements |

For your situation, this could support a proper “Teledyne-style approved design environment” rather than every engineer having their own slightly different setup.

---

# 13. PLM / enterprise system integration

Enterprise Server can integrate with PLM systems. Altium states that it has direct support for Windchill, Arena, Oracle Agile, Aras Innovator, and Siemens Teamcenter, with additional licence and setup. The PLM Integration page allows configuration of interconnection, parameter mapping, and synchronization direction. citeturn574782search2

Official guides:  
**PLM Integration** citeturn574782search2  
**Setup for Teamcenter PLM** citeturn574782search18

### What can be synchronised

| Data type | Example |
|---|---|
| Component data | Parameters, part numbers, lifecycle |
| Project data | Project metadata |
| Supplier data | Approved part/sourcing information |
| Released data | Output packages / release metadata, depending on setup |
| Internal enterprise fields | Company part number, commodity code, approval status |

For a first rollout, I would not start here unless your company already has a mature PLM process. Get the Workspace library and release process under control first.

---

# 14. IT, installation, backup, and maintenance

## 14.1 Installation

The Enterprise Server is installed on-premise and managed locally. Altium’s installation guide covers first-time installation and notes operating system constraints, including that it cannot be installed on a 32-bit OS or unsupported 64-bit Windows editions. citeturn574782search11

Official guide:  
**Installing the Software** citeturn574782search11

---

## 14.2 IT department guide

Altium provides a dedicated IT-focused page covering installation, services, backup, restore, operations, and typical IT questions. citeturn199438search4

Official guide:  
**Information for IT Departments** citeturn199438search4

---

## 14.3 Backup and restore

Backup and restore is done using a command-line Backup & Restore tool. Altium notes that the tool must be run from an administrator command prompt. citeturn574782search1

Official guides:  
**Backing Up & Restoring Your Installation** citeturn574782search1  
**Information for IT Departments** citeturn574782search17

Altium’s IT documentation identifies the tool as `avbackup.exe`, located by default under:

```text
\Program Files (x86)\Altium\Altium365\Tools\BackupTool\
```

citeturn574782search17

Important maintenance note: Altium’s maintenance documentation states that restoring a backup is only possible to the same Enterprise Server version from which the backup was made, and recommends keeping the installer and corresponding licence files with the backup archive. citeturn574782search5

---

## 14.4 Updates and release notes

The release notes page lists current Enterprise Server releases. As of the indexed Altium documentation I found, version **8.0.4 build 2** is dated **1 April 2026** and includes security-related fixes. citeturn574782search15

Official guide:  
**Release Notes** citeturn574782search15

Altium advises making a pre-update backup and testing a new Enterprise Server release on another machine before updating a production instance. citeturn574782search15

---

# 15. Network installation service

Enterprise Server includes a **Network Installation Service** that allows an organisation to perform Altium Designer installations or updates over the local network. citeturn199438search10

Official guide:  
**Advanced Topics** citeturn199438search10

### Practical use

This can help IT manage:

| Area | Benefit |
|---|---|
| Altium Designer deployment | Local network installation |
| Version consistency | Reduce designer version drift |
| Update control | Avoid unmanaged upgrades |
| IT governance | More controlled rollout |

---

# 16. Email notifications

Enterprise Server can send notification emails. The email notification feature is configured from the Workspace browser interface under Admin settings and is available to administrative users. citeturn574782search19

Official guide:  
**Configuration** citeturn574782search19

### Practical use

Useful notifications include:

| Notification | Why useful |
|---|---|
| Part request update | Engineer knows when part is available |
| Task assignment | Reviewer knows action is waiting |
| Workflow transition | Formal process visibility |
| Release activity | Configuration awareness |
| Comment / mention | Design review collaboration |

---

# 17. Local storage and security boundary

Altium’s FAQ states that with On-Prem Enterprise Server, everything is local and behind the firewall. It says the only thing that goes out to the internet is supply chain data, and even that does not necessarily need to be used. citeturn574782search7

Official guide:  
**Enterprise Server FAQs** citeturn574782search7

This is important for organisations with export control, customer confidentiality, defence/aerospace work, or strict internal data policies.

---

# 18. What it can manage

## 18.1 Managed content types

The Enterprise Server Workspace can manage:

| Content | Example |
|---|---|
| PCB projects | Workspace projects |
| Components | Managed components |
| Symbols | Schematic symbols |
| Footprints | PCB land patterns |
| 3D models | STEP models / 3D bodies |
| Simulation models | Where used |
| Schematic templates | Company title blocks |
| PCB templates | Controlled project starters |
| Output Job files | Manufacturing output sets |
| Draftsman templates | Fabrication / assembly drawing templates |
| Released manufacturing packages | Formal build packs |
| Lifecycle definitions | Approved / obsolete / draft states |
| Process workflows | Part requests / project activities |
| Tasks | Assigned actions |
| User/group permissions | Access control |
| Environment configurations | Company-controlled design setup |

---

# 19. Recommended company rollout sequence

Do **not** try to switch everything on at once.

## Phase 1 — Establish server governance

Objectives:

| Task | Owner |
|---|---|
| Confirm version and licence status | IT / CAD admin |
| Confirm backup and restore process | IT |
| Define administrators | Engineering management |
| Define user groups | CAD admin |
| Confirm access route and login method | IT |
| Create basic folder structure | CAD/library owner |

Relevant guides:  
**Managing Users & Groups** citeturn574782search0  
**Backing Up & Restoring Your Installation** citeturn574782search1  
**Managing Content Structure & Access** citeturn574782search4

---

## Phase 2 — Build a pilot component library

Start with a narrow, controlled pilot:

```text
10 resistors
10 ceramic capacitors
5 op-amps
5 connectors
1 company schematic template
1 output job template
1 simple test project
```

Objectives:

| Task | Reason |
|---|---|
| Define component naming | Prevent duplicates |
| Define parameter set | Consistent BOM data |
| Define lifecycle states | Approval control |
| Define footprint review method | Avoid build errors |
| Define ownership | Avoid uncontrolled editing |

Relevant guides:  
**Workspace Components** citeturn199438search15  
**Lifecycle Management** citeturn199438search9  
**Working with Component Folders and Items** citeturn199438search14

---

## Phase 3 — Pilot a Workspace project

Take one non-critical project and run it properly through Workspace project management and Project Releaser.

Objectives:

| Task | Reason |
|---|---|
| Store project in Workspace | Validate project workflow |
| Use managed components | Prove library linkage |
| Use approved OutJob | Prove output repeatability |
| Release to Workspace | Prove manufacturing pack generation |
| Download release package | Prove production handoff |
| Check where-used | Prove traceability |

Relevant guides:  
**Workspace Projects** citeturn199438search16  
**Design Project Release** citeturn199438search2  
**Extracting Data from a Workspace** citeturn199438search17

---

## Phase 4 — Introduce formal part requests

Once the pilot library works, introduce Part Requests.

Objectives:

| Task | Reason |
|---|---|
| Prevent duplicate library creation | Library hygiene |
| Capture engineer need | Better prioritisation |
| Review footprints/symbols | Quality control |
| Approve before general use | Controlled design input |

Relevant guide:  
**Part Requests** citeturn199438search0

---

## Phase 5 — Introduce Team Configuration Center

Once templates and Output Jobs are stable, use Environment Configuration Management to constrain designers to company-approved templates and environment settings. citeturn574782search12

Relevant guide:  
**Environment Configuration Management** citeturn574782search12

---

## Phase 6 — Consider PLM integration

Only do this once the internal Workspace structure is clean.

Relevant guide:  
**PLM Integration** citeturn574782search2

---

# 20. Suggested internal operating model

## 20.1 Roles

| Role | Responsibility |
|---|---|
| Server Administrator | Installation, licences, backup, user access |
| CAD Administrator | Workspace structure, templates, environment configs |
| Library Owner | Component quality, naming, lifecycle |
| Project Lead | Project setup, release approval |
| Designer | Uses managed components/projects correctly |
| Reviewer | Reviews project/component changes |
| Manufacturing/Production | Downloads released packages |
| Quality/Configuration Control | Audits release traceability |

---

## 20.2 Basic rules

Recommended rules for a disciplined setup:

1. **No uncontrolled production library edits.**
2. **No released manufacturing pack outside Project Releaser unless formally justified.**
3. **No new component without checking for existing equivalent.**
4. **Approved components must have symbol, footprint, parameters, lifecycle, and source evidence.**
5. **Output Jobs should be company-controlled.**
6. **Released packages should be downloaded from Workspace, not manually rebuilt later.**
7. **Backups must be tested, not merely scheduled.**
8. **Server upgrades should be trialled before production update.**

---

# 21. Minimum useful internal standards

You probably want these documents internally:

| Document | Purpose |
|---|---|
| Altium Enterprise Server Admin Guide | Who manages what |
| Library Naming Standard | Component naming and parameters |
| Footprint Review Checklist | Prevent PCB manufacturing errors |
| Component Lifecycle Standard | Draft / approved / obsolete rules |
| Project Release Procedure | How to generate formal outputs |
| OutJob Standard | Required manufacturing outputs |
| Workspace Folder Structure | Where things live |
| Permissions Matrix | Who can view/edit/release |
| Backup and Restore Procedure | IT recovery process |
| Part Request Procedure | How engineers request new parts |

---

# 22. “What can it do?” summary

In plain engineering terms, the On-Prem Enterprise Server can:

| Capability | Meaning |
|---|---|
| Store projects centrally | Controlled project source |
| Version project work | Avoid uncontrolled file copies |
| Manage components | Symbols, footprints, parameters, models |
| Control lifecycle | Draft, approved, obsolete, released |
| Support where-used | See where components are used |
| Release designs | Formal output packages |
| Store release history | Previous release packages retained |
| Manage templates | Company schematic / PCB / drawing templates |
| Manage Output Jobs | Standard manufacturing outputs |
| Control users/groups | Permissions and access |
| Support tasks | Action tracking |
| Support comments/reviews | Design collaboration |
| Support part requests | Controlled new component creation |
| Support workflows | Formal engineering processes |
| Integrate with PLM | Sync data with enterprise systems |
| Control designer environment | Team Configuration Center |
| Provide local data control | On-premise storage behind firewall |
| Support backup/restore | IT-managed recovery |
| Support network installation | Local Altium Designer deployment/update support |

---

# 23. Best first move for your situation

Given that your server is finally running after a long delay, I would **not** start by asking Altium for a paid generic training package.

I would start with a small internal pilot:

```text
Pilot name:
Altium Enterprise Server Controlled Library and Release Trial

Scope:
One simple PCB project
One controlled component folder
One schematic template
One Output Job file
One release package
One part request workflow

Success criteria:
- Designer can place managed parts
- Project can be stored in Workspace
- Output pack can be released to Workspace
- Release package can be downloaded
- Component lifecycle can be changed
- Where-used can identify component use
- Backup process is known and documented
```

That gives you a concrete basis for deciding what training, if any, is actually needed.
