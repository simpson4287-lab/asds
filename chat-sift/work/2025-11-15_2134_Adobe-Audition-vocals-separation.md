# Adobe Audition vocals separation
Date (UTC): 2025-11-15 21:34
Conversation ID: 6918f1e2-452c-832e-b6c5-1427a9eccc77
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-001.json

[M1] ME (2025-11-15 21:34):
Tell me about adobe audition. Can you separate vocals out of tracks

[M2] AI (2025-11-15 21:34):
Adobe Audition is a **professional audio editing and restoration suite** used for music production, podcasting, sound design, film post-production, and cleanup/mastering work. It’s powerful, but it works differently from “DJ-style” stem splitters like LALAL, Moises, or iZotope RX Music Rebalance.

Here’s a clean breakdown:

---

# ⭐ **What Adobe Audition Is Best At**
- **Waveform editing** (surgical, destructive editing)
- **Multitrack mixing**
- **Noise reduction & restoration**
- **Spectral editing** (visual editing of frequencies)
- **Mastering tools** (EQ, compression, limiting)
- **Podcast/voice cleanup**
- **Batch processing**

It’s extremely precise, but not particularly “AI-heavy” for modern stem separation.

---

# 🎤 **Can Adobe Audition Separate Vocals From a Full Track?**
**Short answer: Yes — but only in a basic way.**  
It cannot fully isolate vocals like dedicated AI stem-splitting tools.

Audition offers:

## **1. Center Channel Extractor**
Found in:  
**Effects → Stereo Imagery → Center Channel Extractor**

What it does:
- Removes or isolates content panned to the centre (usually vocals).
- Works best for **well-mixed, stereo pop/rock** with vocals dead center.
- Struggles if:
  - Vocals are heavily processed
  - Reverb is wide
  - Instruments share the centre
  - The track is mono

You can choose:
- **Vocal Remove**
- **Vocal Isolation**
- Or tweak manually (frequency ranges, phase settings, etc.)

### ⚠️ Limitations:
- You’ll often get **artifacts**, “phasey” sounds, and leftover reverb.
- Not a true “stem.”

## **2. Spectral Editing**
You *can* manually paint out or isolate frequencies in:
**Spectral Frequency Display**

This is good for:
- Removing coughs in live recordings
- Removing small sections of vocal
- Cleaning noise

But **not** for full-track vocal extraction.

---

# 🚀 **If You Need High-Quality Vocal Isolation**
Use AI-based stem splitters. These outperform Audition dramatically:

### **Best Options**
- **iZotope RX 11 Music Rebalance**  
  (industry standard, extremely clean separations)
- **RipX DeepRemix**
- **LALAL.AI**
- **Moises**
- **Ultimate Vocal Remover (free)**

These give:
- Vocals  
- Drums  
- Bass  
- Other  
- Or up to 8 stems depending on model

Audition can then be used to:
- Clean the isolated vocal
- Mix or master it
- Remove artifacts with spectral editing

---

# 👍 **If you want, I can:**
- Explain exactly how to isolate vocals in Audition step-by-step  
- Recommend the best AI stem splitter for the type of music you’re working with  
- Help you clean up the extracted vocal afterward  
- Compare Audition vs. Logic vs. Pro Tools vs. FL Studio for vocal work

Just tell me what track or purpose you have in mind.

[M3] ME (2025-11-15 21:36):
How much are the best options 

[M4] AI (2025-11-15 21:36):
Here are current pricing examples for some of the best vocal/instrument-separation tools (UK/€ conversions approximate) so you can compare.  

| Tool | Price | Notes |
|------|-------|-------|
| entity["software", "iZotope RX 11", 0] (which includes the “Music Rebalance” module) | • Standard edition ~ **€439 / US$399**. citeturn0search0turn0search9turn0search6 <br>• Elements edition ~ **€109** for basic fewer-tools version. citeturn0search0 <br>• Advanced edition ~ **€1,449** for full suite. citeturn0search0turn0search12 | This is a full audio-repair & production suite, so it’s relatively pricey but very powerful—especially if you already do serious work in audio engineering. |
| entity["software", "Moises AI", 0] (dedicated stem-separation service) | Free plan: basic features. citeturn0search20 <br>Premium plan: for example ~$3.99/month for basic paid tier; ~$24.99/month for “Pro” with Hi-Fi separation. citeturn0search8turn0search2 | Very good value if you only need stem separation regularly and want faster/more fidelity options. |
| entity["software", "LALAL.AI", 0] (pay-as-you-go stem splitting) | One-time packs: e.g. $20 (~90 minutes of audio) for basic. citeturn0search4turn0search28 <br>Other bundles: $54 (~300 minutes), $70 (~500 minutes) etc. citeturn0search28turn0search13 | Very flexible if you only occasionally split tracks and don’t want a recurring subscription. |

---

### ✅ My take for you (given your background)
Since you do a lot of technical/engineering work and might want high-quality separation + clean-up, here’s what I’d suggest:

- If you’re going to do **a lot** of high-fidelity separations and then mix/clean in depth (given your electronics/circuitry mindset, you care about precision), iZotope RX 11 Standard is a strong investment.  
- If you just occasionally want to pull vocals/instruments out for remixing, sampling, or creative journaling/analysis, then a flexible service like LALAL.AI is probably the most cost-efficient.  
- If you want monthly access with evolving features (Hi-Fi stems, plugin support etc.), Moises offers both free trial and subscription tiers, giving good value.

---

If you like, I can pull **UK-specific pricing** (GBP) for each tool (including VAT) and show a breakdown of features vs cost so you can decide which offers the best value for *your workflow*. Would you like me to do that?

[M5] ME (2025-11-15 21:40):
What about platforms they are on

[M6] AI (2025-11-15 21:40):
Here’s a breakdown of the platforms (operating systems/devices) supported by some of the best vocal/instrument-separation tools, and how they compare — important given your detailed creative and technical workflow.  

---

### ✅ Platform Support for Key Tools

#### entity["software", "iZotope RX 11", 0]  
- Available for **Windows (64-bit)** and **macOS (64-bit)**. citeturn0search2turn0search18  
- Works as a standalone application *and* as plug-ins (AU, AAX, VST3) within DAWs. citeturn0search26turn0search9turn0search12  
- Note: No native iOS/Android “app” version for stem-separation; would need desktop or DAW environment.  
- If you’re working on high-resolution stems + clean-up (which your electronics/engineering mindset suggests), this gives you full DAW integration and high fidelity on a professional OS.

#### entity["software", "Moises AI", 0]  
- Has mobile apps: available on **iOS** (App Store) and **Android** (Google Play). citeturn0search16turn0search4  
- Also available as a desktop or web-based platform (so you can upload audio from a laptop/PC). citeturn0search4turn0search20  
- Great if you want flexibility: e.g., do quick separations on tablet/phone, then move to desktop for mixing/mastering.

#### entity["software", "LALAL.AI", 0]  
- Web-based: works in browser on Windows, macOS, Linux. citeturn0search33turn0search21  
- Desktop apps: available for **Windows**, **macOS**, and **Linux (Ubuntu)**. citeturn0search17turn0search11  
- Mobile apps: iOS and Android versions exist. citeturn0search13turn0search32  
- Very versatile platform-wise, which is useful if you switch between devices (desktop studio, laptop, mobile).

---

### 🧭 Which Platform Setup is Best for You?

Given your workflow (journaling, creative remixes, electronics/engineering detail, likely desktop audio work) here are some thoughts:

- If **quality, fidelity, DAW-integration** and deep editing/clean-up matter a lot → iZotope RX 11 is ideal (desktop only).  
- If you want **flexibility** (mobile + desktop + quick separations) → Moises or LALAL.AI give good cross-platform support.  
- If you do some mobile/field work (e.g., quick splits on phone) then work on desktop later → Moises or LALAL.AI shine.

---

If you like, I can **compare a list** of 5 or so separation tools with full platform-compatibility tables (Windows/macOS/iOS/Android/Linux/web) **and** indicate which ones integrate best with your DAW or engineering workflow. Would that be useful?

[M7] ME (2025-11-15 21:46):
Is audio in premiere pro or any other bundles 

[M8] AI (2025-11-15 21:46):
Here’s how audio-separation and audio tools work within the entity["software","Adobe Premiere Pro",0] / entity["software","Adobe Audition",0] / entity["software","Adobe Creative Cloud",0] ecosystem, and the limitations you should be aware of given your goal of separating vocals from tracks.

---

### ✅ What the Adobe bundles **do** include  
- Audition is part of the Creative Cloud audio/video workflow. On the Audition product page: “Mix, edit and create audio content … with a comprehensive tool-set including multitrack, waveform and spectral display for creating, mixing, editing and restoring audio content.” citeturn0search11turn0search13turn0search4  
- Premiere Pro supports audio editing, and via Dynamic Link integrates with Audition. citeturn0search11turn0search4  
- You can import tracks, do cuts/unlink audio from video, manipulate stereo/mono tracks, apply effects, etc in Premiere. citeturn0search7turn0search1  
- In Premiere Pro you can use third-party plug-ins (VST, Audio Units) to enhance audio workflows. citeturn0search8  

---

### ⚠️ What you *can’t* (easily) do in Adobe tools out-of-the-box  
- Despite being powerful, neither Audition nor Premiere Pro include **dedicated AI stem-splitting (vocals/instruments) tools** as a built-in feature at the level of quality that the purpose-built tools provide. For example the “Vocal Isolation” feature being requested in Premiere appears in the forum but not yet as a robust native function. citeturn0search2turn0search0  
- The existing audio tools are more about editing/mixing/restoration + channel-manipulation, rather than fully extracting a vocal stem from a full stereo mix while cleanly separating instruments.  
- If you try to use “center channel extractor” or similar techniques in Audition (which target centre-panned signals) you get *some separation*, but with artefacts and limitations.

---

### 🎯 How this affects **your use case** (given your detailed creative/engineering workflow)  
Since you’re looking to *separate vocals out of tracks* (which implies something like “isolate the vocal stem”, remove the instruments, or extract the instrumental without vocals), you should note:

- If you **already have** separate stems (e.g., multitrack project, or vocal separately recorded) then using Audition/ Premiere is excellent for editing, cleaning, mastering etc.  
- But if you’re starting with **a finished stereo mix** (vocals + instruments blended) and you want the vocal isolated or instrument-only, you’ll likely **need a dedicated stem-separation tool** (as discussed earlier) *in addition to* Audition/Premiere, because Adobe’s native tools aren’t optimised for that task.  
- That said, once you have *some* separation output (even imperfect) you *can* bring it into Audition to: clean it up, reduce artefacts, EQ/delete residual instruments, and integrate with your journal-/creative-workflow.

---

If you like, I can **check the latest Adobe roadmap / beta features** to see if Adobe **plans** to include a high-quality built-in vocal/instrument separator in the next update (so you might be able to do it purely within Adobe in future). Would that be useful?

[M9] ME (2025-11-15 21:46):
Audition 

[M10] AI (2025-11-15 21:46):
## entity["software", "Adobe Audition", 0]  
image_group{"layout":"bento","aspect_ratio":"1:1","query":["Adobe Audition interface screenshot","Adobe Audition spectral frequency display","Adobe Audition multitrack session view"],"num_per_query":1}

### ✅ What Audition Is  
Audition is a full-featured **digital audio workstation (DAW)** and editor developed by entity["organization", "Adobe Inc.", 0]. It’s designed for recording, editing, mixing, restoring, and mastering audio—for music, podcasts, video soundtracks, and post-production. citeturn0search0turn0search3turn0search1  
Key strengths include:  
- Multitrack editing (you can arrange multiple audio tracks together). citeturn0search3turn0search1  
- Waveform + spectral-frequency visual displays, which let you dive deep into precise edits. citeturn0search3turn0search1  
- Strong audio restoration tools: noise reduction, de-hummer, de-esser, etc. citeturn0search1turn0search4  
- Integration with the Adobe Creative Cloud ecosystem (works alongside entity["software", "Adobe Premiere Pro", 0], video timelines, etc). citeturn0search0turn0search4  

### 🎯 Primary Use Cases (Relevant to You)  
Given your background (electronics/engineering + creative writing/journaling + audio work), Audition is useful for:  
- **Post-production cleanup**: If you have audio recordings with hiss, pops, artefacts, Audition’s tools let you restore them.  
- **Multitrack mixing**: For combining voice-over, music, ambience, Foley sounds (e.g., if you create audio diaries, dream-journal snippets, creative voiceovers).  
- **Precision editing**: Because you’re detail-oriented (like circuitry trace analysis), the spectral display lets you zoom into weird artefacts and manipulate them visually.  
- **Video-audio workflows**: If your creative journals or dream-logs ever go into video format (YouTube/streaming), Audition works well with Premiere.  

### ⚠️ What Audition *Isn’t* Ideal For  
- It **doesn’t** include advanced built-in AI stem-separation of vocals/instruments (at least not to the quality of dedicated services).  
- While it offers tools like “center‐channel extractors” and spectral editing, true “isolate the vocal stem from a finished stereo mix” remains difficult and will often leave artefacts.  
- It’s **desktop only** (Windows & macOS) — no full mobile version with the same depth. citeturn0search5turn0search3  
- Because of its depth and professional feature-set, there’s a learning curve.

### 🔧 Key Features (In More Detail)  
Here are some of the standout features:  
- **Multitrack session editing**: You can place many tracks, apply effects to individual clips, automate volume/pan/envelopes. citeturn0search1  
- **Waveform & Spectral Frequency Display**: Enables you to see audio by frequency over time — great for finding weird noises, removing them. citeturn0search3  
- **Audio Restoration / Noise Reduction**: Tools like Adaptive Noise Reduction clean background hiss; spectral editing lets you “paint out” unwanted bits. citeturn0search1turn0search4  
- **Clip stretching / time-pitch tools**: You can change duration without altering pitch, helpful if you’re syncing audio to visual or timing maps. citeturn0search3  
- **Over 50 effects and analysis tools**: From EQ, compression, reverb to loudness metering and mastering environments. citeturn0search4  
- **Essential Sound Panel**: Simplifies many of the complex settings for beginners while still offering power for pros. citeturn0search0turn0search1  

### 🧪 Practical Workflow Example (for Your Use)  
Given your journaling/creative projects + circuit-style precision, you might do something like:  
1. Import a stereo mix (e.g., background music + voice) or recorded voice.  
2. Use the spectral view to locate unwanted noise (e.g., electrical hum, board fan noise, hiss).  
3. Use Adaptive Noise Reduction / Spectral editing to clean those artefacts.  
4. In Multitrack view, layer additional audio (ambient texture, dream-sound design, featured track).  
5. Automate volume/envelopes to fade in/out, duck background under voice, etc.  
6. Export final mix with proper loudness (LUFS) for your target medium (YouTube, podcast, etc). Audition has Match Loudness tools. citeturn0search1  

### 📋 Licensing / Platforms / Integration  
- Runs on **Windows (64-bit)** and **macOS (64-bit)**. citeturn0search5turn0search0  
- It’s part of Adobe’s Creative Cloud subscription model, meaning you get updates, integration with other apps, etc. citeturn0search0  
- Integrates nicely with Premiere Pro — you can send audio clips from Premiere over to Audition for deeper editing, then return them. citeturn0search4turn0search0  

### ✅ Bottom Line  
If you’re working at a professional or near-professional level — especially given your attention to detail and your interest in audio/engineering/creative workflows — Audition is **very strong**. It’s less of a “quick stem-split/one-click vocal extract” tool and more of a precision editor & mixer. If your main goal is to **isolate vocals from full stereo mixes**, it might not be sufficient alone — you’d likely use it *after* a stem-split service for cleanup and further editing.

---

If you like, I can **walk you through exactly how to use Audition to attempt vocal isolation** (with the best available techniques it offers), step-by-step (with screenshots) so you can test whether it meets your needs. Would you like that?

[M11] ME (2025-11-15 21:47):
Is it included in bundles like premiere pro 

[M12] AI (2025-11-15 21:47):
Yes — **Adobe Audition *is* included in some Adobe bundles**, but **not** with a single-app Premiere Pro subscription.

Here’s the clear breakdown:

---

# ✅ **Audition IS included in:**
### **1. Adobe Creative Cloud – All Apps Plan**
This bundle gives you:
- Premiere Pro  
- Audition  
- After Effects  
- Photoshop  
- Illustrator  
- Media Encoder  
- Acrobat  
- + 20+ more apps

💰 **Price:**  
- UK: ~£52.99/month  
- EU: ~€62/month  
- US: ~$59.99/month

If you want both **Premiere Pro + Audition**, this is the bundle.

---

# ❌ **Audition is *NOT* included with:**
### **1. Premiere Pro Single-App Subscription**
When you subscribe to Premiere Pro on its own, you get:
- Premiere Pro  
- Adobe Media Encoder  
- Adobe Fonts  
- Adobe Portfolio  

…but **not Audition**.

You would need to buy Audition separately, or move to the **All Apps** plan.

---

# ✅ **Audition can also be bought as:**
### **2. Adobe Audition Single-App Subscription**
If you only want Audition:
- UK: ~£20.99/month  
- EU: ~€24.19/month  
- US: ~$22.99/month  

---

# ⭐ Best option if you're doing vocals/mixing:
If you plan to do:
- audio extraction  
- editing  
- mixing  
- voice work  
- cleaning vocals for your creative projects  

…then the **All Apps plan** is the best value because you get both Premiere and Audition (and After Effects, Photoshop etc.)

---

If you want, I can compare:
- cost of Audition alone vs All-Apps  
- what comes with each  
- what’s best for your exact workflow (vocals, remixing, dream-journal audio, etc.)

Just tell me your setup (Mac? PC?).
