# AutoCAD default dimension size
Date (UTC): 2026-01-23 18:46
Conversation ID: 6973c1ef-d388-8325-9791-5320fc1f65c8
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-004.json

[M1] ME (2026-01-23 18:46):
How do you make autocad default measuremewnt size bugger

[M2] AI (2026-01-23 18:46):
To make **AutoCAD’s default measurement (dimension) text and arrows larger**, you must adjust the **Dimension Style**. AutoCAD does not scale dimensions automatically unless you tell it how.

##

[M3] ME (2026-01-23 18:46):
how do you do this

[M4] AI (2026-01-23 18:46):
Follow these steps in **AutoCAD**:

### Method 1 — Change the active Dimension Style (recommended)

1. Type **`DIMSTYLE`** and press **Enter**  
2. Select the dimension style you are using (usually **Standard**)  
3. Click **Modify**

Now adjust the key settings:

**Text size**
- Go to the **Text** tab  
- Set **Text height** to a larger value  
  - Typical values:
    - 2.5 → very small  
    - 3.5 → common for prints  
    - 5–7 → large / clear drawings

**Arrow size**
- Go to the **Symbols and Arrows** tab  
- Increase **Arrow size** (usually match text height)

**Overall scaling (most important)**
- Go to the **Fit** tab  
- Under *Scale for Dimension Features*:
  - Set **Use overall scale of:**  
    - Example:
      - Drawing in **mm, 1:1** → scale = **1**
      - Drawing at **1:10** → scale = **10**
      - Drawing at **1:20** → scale = **20**

4. Click **OK**
5. Click **Set Current**
6. Close the dialog

All new dimensions will now be larger.

---

### Method 2 — If dimensions are still tiny (Annotation scaling)

Check if dimensions are **Annotative**:

1. Open **DIMSTYLE**
2. Select style → **Modify**
3. In the **Fit** tab:
   - Either:
     - ✔ Enable **Annotative**, *or*
     - ✖ Disable it and rely on **Overall scale**

If annotative is ON:
- Select a dimension
- Check **Annotation Scale** in the status bar
- Set it to the scale you are plotting (e.g. 1:10, 1:20)

---

### Quick sanity check (common mistake)
- **Model space in mm** + **paper space layouts** → use **Annotative dimensions**
- **Old-school model-only drawings** → use **Overall scale**

If you want, state:
- Units (mm or inches)
- Drawing scale (1:1, 1:10, etc.)
- Model space vs layout usage  

I can give exact values to use.

[M5] ME (2026-01-23 19:51):
[image]
I'm trying to hatch inside object. I've changed a setting somehow and it no longer works 
[attached file: ecc1fa58-b665-4dc4-ae92-2be28a9d756c.png]

[M6] AI (2026-01-23 19:51):
This is a **classic AutoCAD hatch selection issue**. One (or more) hatch-related system variables has been changed.

Work through these **in order** — this will fix it in almost all cases.

---

## 1. Check **boundary gap tolerance** (most likely cause)

If AutoCAD thinks there are gaps, it won’t hatch.

1. Type **`HPGAPTOL`** → Enter  
2. Set value to:
   ```
   0
   ```
   or try:
   ```
   0.5
   ```

Then try **HATCH** again and click inside the area.

---

## 2. Ensure the boundary is actually closed

Your image suggests **two nearly-parallel lines** — AutoCAD will NOT hatch unless it detects a closed loop.

Quick test:
1. Type **`PEDIT`**
2. Select one boundary line
3. Choose **Join**
4. Select the other edges
5. If it refuses → there is a gap or misalignment

To diagnose gaps:
- Type **`OVERKILL`**
- Select the boundary
- Accept defaults

---

## 3. Reset hatch selection behavior

1. Type **`HATCH`**
2. Look at the command line options
3. Make sure:
   - **Pick Points** is used (not Select Objects)

Then:
- Click **well inside** the region, not near edges

---

## 4. Check hatch associativity (very common)

1. Type **`HPASSOC`** → Enter  
2. Set to:
   ```
   1
   ```

If this is **0**, hatching often behaves unpredictably.

---

## 5. Check if the boundary is on a locked layer

AutoCAD cannot hatch using locked geometry.

- Open **Layer Properties**
- Ensure boundary layer is **not locked**

---

## 6. Check drawing scale / tolerance corruption (fast reset)

Type these **one by one**:

```
HPMAXAREAS 0
HPMAXLINES 0
```

These remove internal limits that silently block hatching.

---

## 7. Absolute reset (nuclear option for the command only)

1. Type **`-HATCH`** (note the dash)
2. Follow prompts
3. Choose:
   - Pattern: SOLID
   - Pick internal point

This bypasses UI state corruption.

---

## Most likely cause (based on your screenshot)

**Slight gap or non-coplanar endpoints** between the two lines.  
AutoCAD is extremely unforgiving here.

### Fast workaround if you just need it filled
- Draw a **temporary rectangle** over the region
- Hatch the rectangle
- Delete rectangle
- Set hatch **Associative = OFF**

---

If you want, tell me:
- Are these **lines, polylines, or offsets**
- Are they **vertical but not parallel**
- Is this **imported DXF/DWG**

I can give you the *exact* fix path.

[M7] ME (2026-01-23 19:52):
I used to be able to clikc inside the pewrimeter i wanted to fill

[M8] AI (2026-01-23 19:52):
Understood. That behavior is controlled by **one specific hatch setting** that has almost certainly been changed.

### The exact fix (this restores “click inside to fill”)

1. Type **`HATCH`** → Enter  
2. Look at the **command line** (not the ribbon)
3. Make sure you are using:
   ```
   Pick Points
   ```
   **NOT**:
   ```
   Select Objects
   ```

If it’s stuck on *Select Objects*, AutoCAD will **never** let you click inside an area.

---

### If it still won’t pick inside (most common hidden toggle)

Type these **exactly**, press Enter after each:

```
HPBOUNDARY
0
```

and

```
HPASSOC
1
```

Then try **HATCH → Pick Points → click inside**.

---

### One more silent killer (very common)

Type:
```
PICKFIRST
1
```

If this is `0`, pick-inside behavior often breaks after certain commands.

---

### Quick sanity test (30 seconds)

1. Draw a **simple rectangle**
2. Type **HATCH**
3. Choose **SOLID**
4. Click inside the rectangle

- If this works → your original geometry has gaps
- If this does **not** work → the setting above was the issue

---

### Summary (what changed)
You didn’t “lose” the feature — AutoCAD switched from:
- **Pick Points (region detection)**  
to  
- **Select Objects (manual boundary selection)**

That’s why clicking inside no longer works.

If you want, say whether this is:
- Imported geometry (DXF)
- Offsets
- Polylines vs lines  

and I’ll give the fastest permanent fix.
