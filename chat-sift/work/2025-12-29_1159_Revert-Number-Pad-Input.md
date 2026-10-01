# Revert Number Pad Input
Date (UTC): 2025-12-29 11:59
Conversation ID: 69526cfb-7b2c-8331-b1bd-970680ab17e2
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-002.json

[M1] ME (2025-12-29 11:59):
how do i revert my keyboard to use the number pad. I've lost it when trying to use it for mouse clicking

[M2] AI (2025-12-29 11:59):
This is almost certainly a **Num Lock / Mouse Keys** interaction issue in Windows. When Mouse Keys is enabled, the numeric keypad stops entering numbers and instead controls the mouse pointer.

Below is the clean, deterministic way to revert the number pad to normal numeric input.

---

## Step 1 — Turn **Num Lock** back on
1. Press **Num Lock** once.
2. Test the keypad by typing `1 2 3`.

If that fixes it, stop here. If not, continue.

---

## Step 2 — Disable **Mouse Keys** (this is the usual cause)

### Quick toggle (most common fix)
Press:
```
Left Alt + Left Shift + Num Lock
```
If you see a Windows notification about Mouse Keys, choose **No** or **Disable**.

Test the number pad again.

---

## Step 3 — Disable Mouse Keys permanently (recommended)

1. Press **Windows + I** → **Accessibility**
2. Go to **Mouse**
3. Turn **Mouse keys** **Off**
4. Ensure **“Use Mouse Keys when Num Lock is on”** is **Off**

This prevents it from stealing the keypad again.

---

## Step 4 — Verify no stuck modifier keys
Occasionally one of these is logically “latched”:

- Press **Left Alt**
- Press **Left Shift**
- Press **Ctrl**
- Press **Esc**

Then test the keypad again.

---

## Step 5 — Laptop-specific note (if applicable)
Some laptops require:
```
Fn + Num Lock
```
Especially on compact keyboards without a dedicated numeric cluster.

---

## Prevent this happening again
If you were using the keypad for mouse clicking (e.g. pixel-level Photoshop work):

- Use **AutoHotkey** or **Photoshop keyboard shortcuts** instead of Mouse Keys
- Or enable Mouse Keys only temporarily via the shortcut above

---

If this does **not** resolve it, tell me:
- Desktop or laptop model
- External keyboard yes/no
- Whether numbers appear at all or act as arrows/clicks

I can then give you the exact registry-level or driver-level fix.
