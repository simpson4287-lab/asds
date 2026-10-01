# Cimembt Stucjnon Issue
Date (UTC): 2026-03-19 12:01
Conversation ID: 69bbe569-a684-8387-a487-0e3f10495ba5
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-19 12:01):
[image]
[image]
Why is the cimembt stucjnon an old parameter?
[attached file: IMG_168668D8-9DE4-4684-9328-8F86C79FFB61.jpeg]
[attached file: IMG_F01D8C0A-F0EE-49B5-8B6B-F900C2BF7A37.jpeg]

[M2] AI (2026-03-19 12:01):
Because in Altium the **Comment** you edit in the component properties and the **text object shown on the symbol** are only linked if that visible item is the actual **Comment parameter object**.

From your screenshots, the likely causes are:

1. **The visible text is not the real Comment parameter**
   Someone may have replaced it with plain text, or with another parameter object.
   In that case, changing the component’s Comment field will not update what you see on the symbol.

2. **The Comment parameter object has been manually edited / detached**
   If the text object on the symbol was copied, converted, or overridden, it can behave like old static text.

3. **Database/library sync is involved**
   I can see **“Allow Synchronization with Database”** ticked.
   If this part is tied to a database or managed component source, the comment/value can be pushed back from there and appear “stuck” on an older value.

What to check:

- Click the text on the symbol.
- In Properties, confirm the object type is a **Parameter** and its **Name = Comment**.
- If it is just **Text**, it is not live-linked.
- If unsure, delete that visible text and place a fresh **Comment** parameter on the symbol.

Best fix:
- Delete the current visible comment text.
- Re-place the proper **Comment** string for the SCHLIB component.
- Then edit the component Comment again and see if it follows.

Also, because your screenshot shows **Allow Synchronization with Database** enabled, I would try unticking that temporarily to see whether the database is forcing the old value back in.

So the core answer is: **it’s usually “stuck” because the thing on the symbol is not the live Comment parameter anymore, or database sync is overwriting it.**

Send me one more screenshot of the **selected text object’s full Properties panel**, especially the very top where it says the object type, and I’ll tell you exactly which of the two it is.

[M3] ME (2026-03-19 12:02):
It won't let me delete it 

[M4] AI (2026-03-19 12:02):
That points to it not being a normal free text item.

Most likely it is one of these:

**1. It is the component’s built-in Comment parameter object**
That object is owned by the symbol definition, so it behaves differently from ordinary placed text.

**2. It is locked**
Less likely, but possible.

**3. You are editing the parameter entry, not the drawable object properly**
In SCHLIB, the visible comment string can be a managed parameter object tied to the component body.

Try this in order:

**First check what object it actually is**
- Click directly on the text.
- Open **Properties**.
- Look at the object type at the top.
- If it says **Parameter**, check whether the parameter name is **Comment**.

If it is the real **Comment** parameter, do not try to delete it like plain text. Instead:

**To reset it properly**
- In the SCH Library, select the component body, not just the text.
- In the Properties panel, find **Comment**.
- Change the text there.
- Then look for options like visibility / autopoistion / unlock.
- If the displayed text still does not update, the displayed object may be overridden.

**Try unlocking it**
In the text/parameter properties, look for:
- **Locked**
- **Location locked**
- anything similar

Untick those if present.

**If it still will not delete**
Use the SCH List panel:
- Open **View → Panels → SCH List**
- Filter for text/parameter objects on that component
- Select the suspect object from the list
- Check whether it is a **Comment parameter** or some other parameter
- Delete it from there if allowed

**Very likely fix in your case**
Because I can see **Allow Synchronization with Database** ticked, the library/database linkage may be protecting or reasserting that field. Try:
- untick **Allow Synchronization with Database**
- apply
- then edit the comment again

One important detail from your screenshot:
the visible text looks like random text, but the main component property above shows a different proper part description. That strongly suggests the visible item is a **parameter object with stale display content or database-driven mapping**, not normal text.

Try this exact test:
- select the text
- in Properties, change **Name** to see whether it says `Comment`
- if yes, do **not** delete yet
- just change its **Value** field and see if it updates on-screen

If the **Value** field changes but the text on the schematic stays old, then it is a display/render sync issue.
If the **Value** field immediately snaps back, then database sync is overriding it.

Show me a close-up of the **top half of the selected object’s Properties panel** and I’ll pinpoint it.

[M5] ME (2026-03-19 12:03):
[image]
Yes but comment greyed out 
[attached file: IMG_91EC3A5F-27AD-48E0-A0B5-D211A8449238.jpeg]

[M6] AI (2026-03-19 12:03):
Yes — this confirms it.

That object is the **special built-in Comment parameter**, not ordinary text. That is why:

- **Name = Comment** is greyed out
- you **can’t rename** it
- you often **can’t treat it like normal deletable text**

So nothing is “wrong” there. Altium is protecting the parameter identity.

What matters is the **Value** field. In your screenshot the Comment parameter’s value is now:

`fgdfgdfg`

So if the text shown on the symbol is still the old value, the problem is not that the parameter is wrong — it is that the **display has not refreshed / the component record is still holding another comment value / database sync is involved**.

Do this next, in this order:

### 1. Untick database sync on that parameter
In your screenshot, **Allow Synchronization with Database** is ticked.

Untick it.

That is the first suspect for why it keeps behaving like an old parameter value is stuck.

### 2. Force a redraw / refresh
After unticking:
- click away
- save the SCHLIB
- close and reopen the component or library
- if needed use **View → Refresh** or just reopen Altium

Sometimes the graphical text does not update immediately.

### 3. Check the component-level Comment field
Important distinction:

- the **selected text object** is the Comment parameter object
- but the **component itself** also has a **Comment field**

Select the **component body / symbol**, not the text.
Then in the component properties, set the component’s **Comment** there.

That is often the master source.  
The visible Comment parameter object then displays that master value.

So:
- clicking text edits the parameter display object
- clicking the component edits the component’s actual Comment field

If those get out of step, weirdness happens.

### 4. Turn on Autoposition
Not essential, but worth trying:
- tick **Autoposition**

This can help Altium regenerate the parameter placement properly.

### 5. If still stuck, remove and recreate the built-in comment object
Since it is a special parameter object, don’t try to rename it. Instead:
- select the component in SCHLIB
- use the menu to **hide/remove comment display** if available
- then **re-enable/show comment**
- or place a fresh parameter display object for Comment

Depending on library mode/version, this is sometimes done through the SCHLIB component display controls rather than deleting the text directly.

### What I think is most likely in your case
Most likely order of probability:

1. **Database synchronization is overriding or confusing the displayed Comment**
2. You are editing the **parameter object**, but the real component **Comment** is still different
3. The display just has not refreshed properly

### The key test
Do this exact test:

- untick **Allow Synchronization with Database**
- click the **component body**
- change the component **Comment** field to something very obvious like `TEST_COMMENT_123`
- save library
- reopen component

If the text then changes, the issue was database sync and/or editing the wrong level.

If it still does not change, then we need to inspect whether the symbol has a duplicated comment display object or a library corruption quirk.

From what you’ve shown, though, the greyed-out **Comment** name is normal. The problem is almost certainly the **sync/master-value path**, not the fact that it is greyed out.
