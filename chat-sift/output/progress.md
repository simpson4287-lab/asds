# chat-sift progress

Updated: 2026-10-01 15:00 UTC

## Setup
- Source: ChatGPT export (`Conversations__…-part-0001/conversations-000..008.json`) at the repo root, read-only. Nothing in it is edited.
- Split into one file per conversation: `chat-sift/work/<date>_<time>_<title>.md` (828 files, UTC timestamps). Script: `chat-sift/tools/split.py`.
- Reading rules for each batch: `chat-sift/work/READER_INSTRUCTIONS.md`. Per-batch results: `chat-sift/work/results/bNN.json`.
- Outputs are built from the results by `chat-sift/tools/build.py` (verbatim text is pulled from the split files by message ID).

## Status
- Batches done: 79 / 98
- Conversations read: 636 / 828
- So far: yes 154, partial 68, no 414

## To resume
Run each batch below that has no `work/results/bNN.json`, following READER_INSTRUCTIONS.md. Then run `tools/build.py` and `tools/progress.py`, and commit.

## Batches done
b01, b02, b03, b04, b05, b06, b07, b08, b09, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36, b37, b38, b39, b40, b41, b42, b43, b44, b45, b46, b47, b48, b49, b50, b51, b52, b53, b54, b55, b56, b57, b58, b59, b60, b61, b62, b63, b64, b65, b66, b67, b68, b69, b70, b71, b72, b73, b74, b75, b76, b77, b78, b79

## Remaining
- b80: 2026-02-27_2116_Symbol-Meaning-in-Altium.md … 2026-03-04_1009_Unclear-Explanation.md (7 conversations)
- b81: 2026-03-04_1651_OS-Current-Measurement.md … 2026-03-06_0943_Perplexity-AI-Usage.md (6 conversations)
- b82: 2026-03-06_0950_CDR-Report-Rewrite.md … 2026-03-11_1441_Multiple-Top-Level-Documents.md (9 conversations)
- b83: 2026-03-12_0950_Negative-Feedback-Resistors-x5.md … 2026-03-21_0641_E-bike-storage-canopy.md (21 conversations)
- b84: 2026-03-21_1000_Front-Wheel-Motor-Setup.md … 2026-03-21_1542_Cabin-Studio-Rental-Pricing.md (2 conversations)
- b85: 2026-03-21_2101_Cement-board-packing-uses.md … 2026-03-22_1545_Text-Positioning-Issues.md (4 conversations)
- b86: 2026-03-23_0026_x5-Signal-Weighting-Differences.md … 2026-03-23_0026_x5-Signal-Weighting-Differences.md (1 conversations)
- b87: 2026-03-23_2313_Graphic-Enhancement-Request.md … 2026-03-28_1403_Angle-Calculation-for-Slope.md (12 conversations)
- b88: 2026-03-28_1521_Wall-Insulation-Plan-Review.md … 2026-04-06_1020_IC-Footprint-Pad-Shape.md (15 conversations)
- b89: 2026-04-13_1622_PIP-and-Autism-Support.md … 2026-04-17_2129_Lean-to-Conservatory-Roof-Conversion.md (6 conversations)
- b90: 2026-04-18_0424_AI-Economy-Financial-Planning.md … 2026-04-18_1702_Shark-Carpet-Cleaner-Tips.md (4 conversations)
- b91: 2026-04-18_1953_Curved-Monitors-for-Work.md … 2026-05-05_2038_Counselling-Course-Application-Help.md (24 conversations)
- b92: 2026-05-12_2127_Power-Supply-Compliance-Query.md … 2026-05-14_1726_Oxide-Controllers-Benefits.md (11 conversations)
- b93: 2026-05-14_1727_PXI-Embedded-Controllers-Benefits.md … 2026-05-14_2259_HR-Cliques-and-Dysfunction.md (3 conversations)
- b94: 2026-05-15_0430_PXI-4-Wire-Sense-Options.md … 2026-05-26_1459_Clarification-Request.md (18 conversations)
- b95: 2026-05-28_1009_Log-cabin-work-summary.md … 2026-06-22_1703_Radiation-Suited-Cables.md (30 conversations)
- b96: 2026-06-23_1546_Voltage-at-Load-Current-at-Source.md … 2026-06-29_1135_Rise-time-measurement-tweak.md (8 conversations)
- b97: 2026-07-03_0922_Retrospective-IEC-61010-Uplift.md … 2026-08-06_0719_Broadfix-Shim-Feature.md (6 conversations)
- b98: 2026-08-06_1641_djay-Pro-2-Crash.md … 2026-08-17_1510_Max-Voltage-Inputs-LM1086-MAX604.md (5 conversations)
