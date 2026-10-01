# Make links visible CADSTAR
Date (UTC): 2026-01-29 18:22
Conversation ID: 697ba544-02bc-8327-bf17-3706af450d3f
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-004.json

[M1] ME (2026-01-29 18:22):
How do you make links visible on Cadar classic?

[M2] AI (2026-01-29 18:22):
In **CADSTAR Classic**, “links” (net connectivity lines / ratsnest) are controlled from the **Connectivity** display settings.

Use one of the following methods.

---

### Method 1: Menu path (most reliable)
1. Go to **View → Connectivity → Show Links**
2. Ensure **Links** is **ticked / enabled**
3. If nothing appears, also check:
   - **View → Connectivity → Show Ratsnest** (older terminology in some installs)

---

### Method 2: Display Control (layers & items)
1. Open **View → Display Control**
2. In the **Items** or **Connectivity** section, enable:
   - **Links**
   - **Connectivity / Nets**
3. Apply and close

---

### Method 3: Hotkey (if configured)
Some installations map a toggle key:
- Try **Ctrl + L** or **Shift + L**
- If it does nothing, check **Tools → Customise → Keyboard**

---

### Common reasons links still don’t show
- **No netlist loaded**  
  → You must have imported or forward-annotated the schematic netlist.
- **Board not updated from schematic**  
  → Run **Design → Update PCB from Schematic**
- **Wrong colour / visibility**  
  → Links may exist but are same colour as background  
  → Adjust in **Settings → Colours → Connectivity / Links**

---

### Quick diagnostic check
- Select a component  
- If **nothing highlights**, connectivity is not present
- If pads highlight but no lines appear → display issue, not netlist

---

If you want, tell me:
- **CADSTAR version**
- **Schematic → PCB workflow used (import vs ECO)**
- Whether this is **blank board vs routed board**

I can give an exact step-by-step for your setup.
