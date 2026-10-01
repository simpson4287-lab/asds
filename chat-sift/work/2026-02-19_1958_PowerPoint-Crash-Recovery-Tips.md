# PowerPoint Crash Recovery Tips
Date (UTC): 2026-02-19 19:58
Conversation ID: 69976b52-08e8-8388-a2ba-6925a6149a61
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-02-19 19:58):
I had a PowerPoint crash on me and lost a load of work. It’s not in recovered files. Is it gone?

[M2] AI (2026-02-19 19:58):
Not necessarily gone — PowerPoint often leaves recoverable traces even when the obvious recovery pane is empty. Work through this **in order**, because success probability drops as you go.

---

## 1️⃣ Check AutoRecover folder (highest chance)

PowerPoint AutoRecover files don’t always appear in the UI.

**Windows path (most common):**

```
C:\Users\<your-username>\AppData\Local\Microsoft\Office\UnsavedFiles
```

**Also check:**

```
C:\Users\<your-username>\AppData\Roaming\Microsoft\PowerPoint\
```

Look for files ending in:

- `.pptx`
- `.ppt`
- `.tmp`
- `.asd`

👉 Sort by **Date Modified**.

---

## 2️⃣ Inside PowerPoint: Recover Unsaved Presentations

Open PowerPoint fresh:

**File → Info → Manage Presentation → Recover Unsaved Presentations**

Even if you checked earlier, try again after restarting PowerPoint.

---

## 3️⃣ Search your whole PC (often works)

In Windows search box:

```
*.pptx
```

Then sort by **Date modified**.

Also try:

```
*.tmp
```

Sometimes the crash leaves a temp file with a random name.

---

## 4️⃣ Check OneDrive / SharePoint version history (if applicable)

If the file was ever saved to cloud storage:

- Open OneDrive online
- Find the file
- Check **Version history**

This rescues many “lost” edits.

---

## 5️⃣ Check temporary folder (last-ditch but worth it)

Press **Win + R**, paste:

```
%temp%
```

Sort by date and look for large recent files.

---

## ⚠️ Important reality check

If:

- The file was **never saved once**, and  
- AutoRecover interval hadn’t triggered yet, and  
- Nothing exists in UnsavedFiles…

…then unfortunately the work can be unrecoverable.

But in practice, **AutoRecover saves every 10 minutes by default**, so there is still a decent chance.

---

## 🧭 Quick triage question (helps me target the right path)

Tell me:

- Windows or Mac?
- Had you saved the file at least once?
- Roughly how long you were working before the crash?
- Is AutoSave (top-left toggle) usually on for you?

Reply with that and I’ll give you the **highest-probability recovery path** for your exact case.

[M3] ME (2026-02-20 12:22):
[image]
[image]
[attached file: IMG_51E48AA7-F8B6-4562-AD0C-39DA5EAAB6CE.jpeg]
[attached file: IMG_4E1A67E6-C44B-40B2-8C58-E14DB4B868A3.jpeg]

[M4] AI (2026-02-20 12:22):
I’m sorry — losing PowerPoint work is brutal. The good news is: **most crashes still leave something recoverable**, even when the recovery pane is empty.

Based on your photos you’re on **Windows + Office desktop**, so do this exact high-probability sweep:

---

# 🔴 Step 1 — Check the real AutoRecover cache (MOST IMPORTANT)

Press **Win + R** and paste:

```
%localappdata%\Microsoft\Office\UnsavedFiles
```

Then:

- Sort by **Date modified**
- Look for:
  - `.pptx`
  - `.tmp`
  - `.asd`

👉 If you find one, **copy it to Desktop first**, then try opening.

**This is where PowerPoint usually hides crash saves.**

---

# 🔴 Step 2 — Secondary PowerPoint cache

Press **Win + R** again:

```
%appdata%\Microsoft\PowerPoint
```

Same drill — sort by date.

---

# 🔴 Step 3 — Full machine search (surprisingly effective)

In File Explorer search box:

```
*.tmp
```

Then sort by **Date modified**.

You’re looking for:

- recent large files
- random names like `pptXXXX.tmp`

---

# 🔴 Step 4 — Inside PowerPoint (one more time)

Open PowerPoint fresh:

**File → Info → Manage Presentation → Recover Unsaved Presentations**

Even if you checked earlier — crashes sometimes register on second launch.

---

# ⚠️ Reality check (important but not doom)

Recovery depends mainly on two things:

✅ Had the file ever been saved once  
✅ Whether AutoRecover interval fired before crash

---

## 🎯 Quick diagnostic — answer these

Reply with:

1. Had you saved the PPT at least once?
2. Roughly how long were you working before the crash?
3. Was AutoSave (top-left toggle) ON or OFF?
4. Did PowerPoint say “not responding” or hard crash?

With those, I can tell you **the actual probability of recovery** and the next forensic steps if needed (there are a couple deeper ones we can try).

You still have a decent shot at this.
