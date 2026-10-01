# Formatting Mac Drive HFS
Date (UTC): 2026-04-24 13:29
Conversation ID: 69eb7032-b0c4-83eb-95ed-3a533dff4216
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-04-24 13:29):
how can i format a drive used for mac system using HFS explorer

[M2] AI (2026-04-24 13:29):
HFSExplorer **cannot format a Mac system drive**. It is mainly for **reading HFS/HFS+ Mac drives from Windows** and copying files off them.

To format the drive, use one of these:

### Best option: on a Mac

1. Open **Disk Utility**
2. Select **View → Show All Devices**
3. Select the **physical drive**, not just the volume underneath
4. Click **Erase**
5. Choose format:
   - **APFS** — for modern macOS system drives
   - **Mac OS Extended (Journaled)** / HFS+ — for older Macs
   - **exFAT** — if you want Windows and Mac compatibility
6. Choose scheme:
   - **GUID Partition Map** for Mac boot/system drives
7. Click **Erase**

### On Windows

You can only really **wipe/partition** it in Windows, not properly format it as HFS+ using HFSExplorer.

Use **Disk Management** or `diskpart` to delete the Mac partitions, then format as **exFAT** or **NTFS**.

For `diskpart`:

```text
diskpart
list disk
select disk X
clean
create partition primary
format fs=exfat quick
assign
exit
```

Replace `X` with the correct disk number. Be very careful — `clean` wipes the selected drive.

### If your aim is to reinstall macOS

Boot into **macOS Recovery**, then use **Disk Utility** there and erase as:

```text
APFS + GUID Partition Map
```

Then reinstall macOS.
