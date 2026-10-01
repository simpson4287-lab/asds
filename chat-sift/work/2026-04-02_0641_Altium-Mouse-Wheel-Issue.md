# Altium Mouse Wheel Issue
Date (UTC): 2026-04-02 06:41
Conversation ID: 69ce0f86-8ad0-8396-a2f1-2bddf66ade2c
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-02 06:41):
Why has altium decided to pan whilst using mouse wheel without shift. It’s like someone’s holding down shift key

[M2] AI (2026-04-02 06:41):
That usually means Altium thinks a modifier key state has changed, or the mouse-wheel action got remapped.

Most likely causes, in order:

1. **Shift key is effectively stuck**
   Even if the keyboard looks fine, Altium can behave as if Shift is latched.
   Try:
   - Tap **Shift** a few times
   - Tap **both Shift keys**
   - Click into another app, press/release Shift there, then return to Altium
   - Disconnect/reconnect any external keyboard if one is attached

2. **Middle-mouse / wheel mode got altered**
   In some views, Altium can end up behaving oddly if navigation preferences changed.
   Check:
   - **Preferences / System Preferences → View** or **PCB Editor / Schematic → General / Mouse Wheel Configuration**
   - Look for options related to **Mouse Wheel pans/zooms**
   - Set wheel back to **Zoom**

3. **Windows sticky/filter keys type issue**
   If Windows thinks a modifier is held, Altium will too.
   Check OS keyboard settings and turn off:
   - Sticky Keys
   - Filter Keys

4. **A utility is intercepting input**
   Mouse software, keyboard macro tools, remote desktop sessions, or CAD helpers can fake modifier input.
   Common culprits:
   - Logitech Options / G Hub
   - Corsair / Razer tools
   - AutoHotkey
   - Remote desktop / VM input glitches

5. **Temporary Altium input glitch**
   Altium does sometimes get “stuck” in a strange navigation state.
   Try:
   - Save
   - Close and reopen Altium
   - If that fails, reboot the PC

A quick test to confirm it is “fake Shift”:
- Open **Notepad**
- Spin wheel there, then press **Shift** and spin
- Also type a capital using Shift and see whether Shift feels normal
- In Altium, try **wheel over schematic/PCB** and compare whether it always pans

The fastest fix is usually:
- tap both Shift keys a few times,
- click out of Altium and back in,
- then restart Altium.

If you want, I can walk you through exactly where to check the wheel-pan/zoom setting in **your editor view** — schematic or PCB.
