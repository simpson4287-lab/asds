# Dragon vs Microsoft Dictation
Date (UTC): 2026-03-17 17:11
Conversation ID: 69b98b3f-da88-8391-8fc6-2e2f053419bd
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-17 17:11):
So dragon speaking software worth it anymore? Is Microsoft’s built in version on par?

[M2] AI (2026-03-17 17:12):
Yes — **Dragon is still worth it for some people, but it’s no longer the automatic choice**.

For most general users on Windows 11, **Microsoft’s built-in tools have caught up enough that Dragon is not obviously worth paying for** just for casual dictation. Microsoft now has:
- **Voice typing** for speech-to-text, which uses Azure speech recognition. citeturn124008search1
- **Voice Access** for full PC control plus text authoring, and it works **offline** on Windows 11. citeturn124008search5turn124008search17

Where **Dragon still tends to justify itself** is when you need more than “good enough” dictation:
- very heavy daily dictation
- lots of **custom vocabulary**
- repeated **boilerplate/macros/templates**
- accessibility use where reliability and hands-free workflow matter a lot
- specialist domains like legal/medical/technical language

Nuance still positions Dragon Professional around **high accuracy, professional workflows, and customization**, including claims of up to **99% recognition accuracy** and strong productivity features. citeturn124008search0turn124008search3

My practical take:

**Choose Microsoft built-in** if:
- you want free
- you mainly dictate emails, notes, Teams chats, Word docs
- you only occasionally need voice control
- you’re happy with “pretty good” rather than finely tuned

**Choose Dragon** if:
- you want voice to be a core workflow, not just an occasional convenience
- you need dependable command/control across apps
- you use unusual terminology, names, part numbers, or technical jargon
- RSI, fatigue, ADHD friction, or accessibility needs make voice input a serious productivity tool

Given the kinds of things you do — engineering, long technical notes, odd component names, acronyms, structured documentation — **Dragon probably still has an edge for your use case** because custom terms and reusable commands matter more than raw dictation alone. Microsoft’s built-in option is likely “on par” only for **basic dictation**, not for a fully optimized professional workflow. citeturn124008search0turn124008search1turn124008search5

A good real-world approach would be:
1. Try **Windows Voice Typing + Voice Access** first, since you already have it.
2. Test it with your actual vocabulary: part numbers, acronyms, project names, structured notes.
3. If it feels flaky, slow, or annoying after a few days, that’s where Dragon still earns its keep.

If you want, I can give you a **straight engineering-style comparison table** of Dragon vs Windows built-in for your specific use case: technical writing, CAD/Office use, and low-friction note capture.

[M3] ME (2026-03-17 17:12):
Is there a way to train the azure?

[M4] AI (2026-03-17 17:12):
Not really in the **consumer Windows built-in dictation** sense.

For **Windows Voice Typing / Voice Access**, there isn’t a normal user-facing “train it to my voice” workflow like the old speech-recognition era. Microsoft’s current voice typing uses **Azure Speech services**, and the older **Windows Speech Recognition** path is deprecated in favor of Voice Access. citeturn668073search1turn668073search12turn668073search16

What you *can* do on Windows is:
- make sure the **speech language/locale** matches your accent
- use it consistently so Microsoft’s broader cloud model does its thing
- benefit from **inking and typing personalization**, which builds a custom word list from what you type/write — but that is not the same as explicitly training speech dictation to your voice. citeturn668073search3turn668073search1

If you mean **Azure Speech as a developer/product feature**, then **yes** — Microsoft does support **Custom Speech**. You can upload domain-specific text/audio, train a custom model, test it, and deploy it to improve recognition for specialist vocabulary or accents in your own app/workflow. citeturn668073search0turn668073search4turn668073search11turn668073search13

So the practical answer is:

- **Windows built-in for personal use:** no proper manual training in the old Dragon-style sense.  
- **Azure platform for developers/business use:** yes, but that’s a separate custom-model workflow, not a simple “train my PC dictation” button. citeturn668073search0turn668073search1

For your use case, that usually means:
- if you want **free built-in dictation**, use Windows as-is and optimize mic + language settings
- if you want **serious adaptation to technical jargon**, Dragon still has an advantage unless you’re willing to build around Azure Custom Speech yourself. citeturn668073search0turn668073search4

A useful rule of thumb: **Microsoft built-in is easier; Dragon is more tunable.**
