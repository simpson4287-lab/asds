# Multiple Top-Level Documents
Date (UTC): 2026-03-11 14:41
Conversation ID: 69b17f1d-ccb8-838e-aab3-3833abab8442
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-006.json

[M1] ME (2026-03-11 14:41):
[image]
What does altium mean by multiple
Top
Level documents  
[attached file: IMG_4DB58494-AE07-4137-B9EC-51F0B9013116.jpeg]

[M2] AI (2026-03-11 14:41):
It means Altium thinks the same schematic sheet is being treated as a **top-level sheet in more than one place** in the project hierarchy.

In your case the key message is:

**“Multiple top level documents: CCD38x_Interface.SchDoc has been used”**

That usually happens when **the sheet is not only being called by a Sheet Symbol, but is also included as its own standalone root sheet** during compilation.

What Altium expects is:

- a **top-level document** = the root sheet of the design
- lower sheets = brought in **through sheet symbols / entries** from that root

You get this error when the same child sheet ends up with **more than one parent path**, or Altium can’t determine a single clean root.

Common causes:

1. **The child sheet is open in the project as an ordinary schematic, but also referenced by a sheet symbol**
   - So `CCD38x_Interface.SchDoc` is both:
     - a standalone schematic in the project hierarchy
     - and a sub-sheet called from another sheet

2. **Two different top sheets both point to the same child sheet**
   - for example both a CCD381 sheet and a CCD385 sheet reference `CCD38x_Interface.SchDoc`

3. **A sheet filename is reused in more than one branch of hierarchy**
   - especially easy to do when copying channels / variants

4. **Project options / hierarchy mode are confused by extra sheets in the project**
   - Altium sometimes treats unreferenced schematic documents as roots

Why that matters here:
Because if Altium sees the same sheet in multiple top-level contexts, net resolution gets messy. That can lead to exactly the sort of weirdness you’ve been seeing:
- duplicate net issues
- nets with only one pin
- ports not resolving as expected
- floating objects
- unexpected compile results

What to check now:

**First check the project tree**
- Identify your true root sheet
- Ask: is `CCD38x_Interface.SchDoc` supposed to be:
  - the top sheet, or
  - a child sheet only?

It must be one or the other, not both.

**Then check every sheet symbol**
- Search all schematics for references to `CCD38x_Interface.SchDoc`
- Make sure only the intended parent sheet calls it

**Then check for orphan sheets**
- If a schematic is sitting in the project but not meant to be compiled as a separate root, either:
  - remove it from project temporarily, or
  - ensure it is only reached through hierarchy

**Then check sheet symbols / filenames**
- Make sure two separate sheet symbols are not both pointing at the same physical `.SchDoc` unless that is genuinely intended and supported by your design structure

Practical interpretation for your design:
I suspect `CCD38x_Interface.SchDoc` is being used as a shared interface sheet in more than one branch, or Altium is seeing extra variant sheets as additional roots. That would fit with your earlier comment about **extra sheets in the hierarchy**.

Fastest diagnostic:
1. Open the project panel  
2. Find your intended master top sheet  
3. Search for every reference to `CCD38x_Interface.SchDoc`  
4. Confirm whether more than one sheet symbol points to it  
5. Temporarily remove or exclude any duplicate parent sheets and recompile

If you want, send a screenshot of:
- the **project tree**
- the **sheet symbols that point to `CCD38x_Interface.SchDoc`**
- and **Project Options → Error Reporting / Connectivity / Multi-Channel tabs**

and I’ll tell you exactly which sheet Altium is treating as the extra top-level path.
