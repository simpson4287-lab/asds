# Concatenate Cells in Excel
Date (UTC): 2026-01-18 22:11
Conversation ID: 696d5a7d-5884-832a-b9cc-a624fd92186e
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-004.json

[M1] ME (2026-01-18 22:11):
How do I paste contents of two variable cells into 1 cell

[M2] AI (2026-01-18 22:11):
You’re basically asking Excel to **concatenate**—to fuse two cells into one, like a mild-mannered spreadsheet alchemist.

Here are the clean, modern ways to do it, depending on how tidy you want the result.

The simplest formula is:

```
=A1 & B1
```

Whatever text or values are in A1 and B1 will be glued together in the target cell.

If you want a space (or any separator) between them, you insert it explicitly:

```
=A1 & " " & B1
```

That `" "` is just a literal space. You can swap it for a comma, dash, or anything:

```
=A1 & " - " & B1
```

Excel also has a more explicit function, which some people find clearer:

```
=CONCAT(A1, B1)
```

Same result, slightly more verbose. If you want a separator with this one:

```
=CONCAT(A1, " ", B1)
```

Now, if you’re dealing with **variable cells**—meaning sometimes one might be blank—and you don’t want awkward extra spaces, this version behaves nicely:

```
=TEXTJOIN(" ", TRUE, A1, B1)
```

What’s going on there:
- `" "` is the separator
- `TRUE` tells Excel to ignore empty cells
- `A1, B1` are the cells being combined

That one’s gold for dynamic sheets, trackers, and anything where fields may or may not be filled in yet.

One important mental model:  
You’re not “pasting” in the physical sense. You’re **creating a live formula** that always reflects whatever is in those source cells. Change A1 or B1, and the combined cell updates instantly—no manual babysitting required.

If you want to go one step further—locking the result as plain text, auto-filling down rows, or combining whole ranges—that opens up a few more elegant tricks.
