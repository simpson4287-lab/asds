# Library Part Checklist Excel
Date (UTC): 2026-01-13 22:14
Conversation ID: 6966c394-fb44-8327-bfc4-7c0065d3f5d8
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-004.json

[M1] ME (2026-01-13 22:14):
Library checklist. Please transfer this response into an excel spreadsheet of its own. Good — a single-pass checklist means: one row, one sweep, no backtracking. You look at the part once, answer everything, move on. This is exactly right for library hygiene.

Below is a tight, single-pass checklist that fits comfortably on one screen in Excel and still catches the real killers.

⸻

Single-Pass Library Part Checklist

(Schematic Symbol + Footprint + Consistency)

Each item is Yes / No / N/A.
If anything is No, the part is not released. No drama, just physics.

⸻

Identity & Scope
	•	Part number (MPN) correct and unambiguous
	•	Package variant explicitly identified
	•	Datasheet linked and correct revision

⸻

Schematic Symbol (Logical Truth)
	•	Pin count matches datasheet
	•	Pin names and functions match datasheet
	•	Pin numbers exactly correct
	•	Power and ground pins complete (no missing or hidden surprises)
	•	NC / DNU pins clearly identified
	•	Special pins (thermal pad, sense, exposed pad) represented correctly

⸻

Footprint (Physical Truth)
	•	Package type and body size correct
	•	Land pattern dimensions verified
	•	Pin pitch and numbering orientation correct
	•	Pin-1 indicator correct and obvious
	•	Courtyard / assembly outline present
	•	Thermal pad present and sized correctly (if applicable)

⸻

Symbol ↔ Footprint Mapping (Reality Check)
	•	All pins map correctly symbol → footprint
	•	No swapped, mirrored, or rotated pin assignments
	•	Power pins land on correct pads
	•	NC / DNU pins not accidentally bonded
	•	Differential / paired pins mapped correctly (if applicable)

⸻

Parametrics & Metadata (Future-You Test)
	•	Voltage / power / tolerance fields populated where relevant
	•	Approved alternates noted (or explicitly none)
	•	Lifecycle status known (active / NRND / obsolete)
	•	Internal library revision assigned

⸻

Imaging / Test-Electronics Sanity
	•	Absolute max ratings compatible with system rails
	•	Sensitive pins (analog / high-speed / ESD-critical) identified
	•	Known vendor errata or caveats checked
	•	No obvious violation of test-system assumptions

⸻

Release Check
	•	Reviewed by second pass (or same engineer, different day)
	•	Notes recorded if anything is non-obvious

⸻

What this gives you
	•	One sweep
	•	One decision
	•	No ceremonial overhead
	•	No false confidence

If this checklist says “Yes” all the way down, the part is safe enough to build boards with — which is the only bar that matters.

⸻

Next natural step (optional, not required)

When we turn this into the Excel tab, the columns will simply be:
	•	Part Name
	•	MPN
	•	Package
	•	Checklist Result (Pass / Fail)
	•	Notes
	•	Reviewer
	•	Date

Everything else collapses into dropdowns.
No one wants a library checklist that needs a scrollbar.

This is the right level of discipline for serious test electronics.

[M2] AI (2026-01-13 22:14):
Done. I’ve transferred the entire checklist into a clean, single-sheet Excel file with one row per check item and no ceremony.

**What you get**
- Sections preserved (Identity, Symbol, Footprint, Mapping, etc.)
- One decisive field per item: **Response (Yes / No / N/A)**
- Space for **Notes, Reviewer, Date**
- Designed for a single vertical sweep—no scrolling sideways, no backtracking

**Download it here:**  
[Download the Library Part Checklist Excel file](sandbox:/mnt/data/Library_Part_Checklist.xlsx)

This is library hygiene, not bureaucracy. If a single “No” appears, the part simply isn’t real yet. Physics doesn’t negotiate, and neither should your library.
