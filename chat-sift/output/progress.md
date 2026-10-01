# chat-sift progress

Updated: 2026-10-01 14:45 UTC

## Setup
- Source: ChatGPT export (`Conversations__…-part-0001/conversations-000..008.json`) at the repo root, read-only. Nothing in it is edited.
- Split into one file per conversation: `chat-sift/work/<date>_<time>_<title>.md` (828 files, UTC timestamps). Script: `chat-sift/tools/split.py`.
- Reading rules for each batch: `chat-sift/work/READER_INSTRUCTIONS.md`. Per-batch results: `chat-sift/work/results/bNN.json`.
- Outputs are built from the results by `chat-sift/tools/build.py` (verbatim text is pulled from the split files by message ID).

## Status
- Batches done: 9 / 98
- Conversations read: 81 / 828
- So far: yes 4, partial 14, no 63

## To resume
Run each batch below that has no `work/results/bNN.json`, following READER_INSTRUCTIONS.md. Then run `tools/build.py` and `tools/progress.py`, and commit.

## Batches done
b01, b02, b03, b04, b05, b06, b07, b08, b09

## Remaining
- b10: 2025-10-18_1148_Incident-statement-assistance.md … 2025-10-19_1204_Summarise-interview-notes.md (4 conversations)
- b11: 2025-10-19_1335_Driving-in-closed-areas.md … 2025-10-20_1227_Guitar-pattern-explanation.md (6 conversations)
- b12: 2025-10-20_1711_Hylands-Park-access-pack.md … 2025-10-26_1243_1-Social-Questions.md (5 conversations)
- b13: 2025-10-26_1249_social.md … 2025-10-31_0429_Tidy-text-request.md (8 conversations)
- b14: 2025-11-01_1447_Viagogo-ticket-benefits.md … 2025-11-02_1400_Journal-entry-transcription.md (5 conversations)
- b15: 2025-11-02_1456_Upload-limits-with-GPT.md … 2025-11-03_1154_Contextual-preface-writing.md (3 conversations)
- b16: 2025-11-03_1325_Final-review-before-submission.md … 2025-11-09_1702_Falstead-circuits-price.md (20 conversations)
- b17: 2025-11-09_1912_Viagogo-order-issue-explained.md … 2025-11-13_1509_Radiohead-2025-tour-songs.md (9 conversations)
- b18: 2025-11-13_1646_Song-rewrite-suggestions.md … 2025-11-13_1646_Song-rewrite-suggestions.md (1 conversations)
- b19: 2025-11-14_1002_Poem-refinement.md … 2025-11-15_2134_Adobe-Audition-vocals-separation.md (7 conversations)
- b20: 2025-11-19_1408_CCD-gain-calibration-explanation.md … 2025-11-22_0825_Portable-2-in-1-laptops.md (7 conversations)
- b21: 2025-11-22_0954_OmniBook-X-vs-5.md … 2025-12-03_2236_Modify-pink-vest.md (20 conversations)
- b22: 2025-12-04_0759_Example-request-clarification.md … 2025-12-05_1401_Colour-block-options.md (20 conversations)
- b23: 2025-12-05_1401_Original-reference-guide.md … 2025-12-09_1652_Power-supply-overcurrent-causes.md (14 conversations)
- b24: 2025-12-10_0341_Improve-my-answers.md … 2025-12-10_0341_Improve-my-answers.md (1 conversations)
- b25: 2025-12-11_0838_Autistic-traits-identified.md … 2025-12-17_1001_Mains-load-estimation.md (18 conversations)
- b26: 2025-12-17_1911_Sharing-psychological-notes.md … 2025-12-17_1911_Sharing-psychological-notes.md (1 conversations)
- b27: 2025-12-17_2157_Reasonable-adjustments-delay.md … 2025-12-18_0852_Altium-AI-usage.md (3 conversations)
- b28: 2025-12-18_1211_Balanced-rewrite-suggestion.md … 2025-12-19_0807_Unanswered-messages-and-politics.md (7 conversations)
- b29: 2025-12-19_1403_Circuit-negative-current-sensing.md … 2025-12-20_0854_Program-details-summary.md (6 conversations)
- b30: 2025-12-20_1034_DSOX1102A-vs-EDUX1002G.md … 2025-12-21_1105_Procreate-vs-Photoshop-benefits.md (7 conversations)
- b31: 2025-12-21_1404_Snap-alignment-fix.md … 2025-12-22_1627_Op-amp-offset-issue.md (9 conversations)
- b32: 2025-12-24_1324_Amusing-Dating-Response-Ideas.md … 2025-12-25_1350_Quality-Log-Building-Benefits.md (7 conversations)
- b33: 2025-12-25_1422_Schaum-Feedback-and-Control.md … 2025-12-25_1540_AoE-vs-Learning-AoE.md (2 conversations)
- b34: 2025-12-25_1729_Psychologist-Session-Mismatch.md … 2025-12-25_1729_Psychologist-Session-Mismatch.md (1 conversations)
- b35: 2025-12-26_0716_Work-Folder-Optimization-Tips.md … 2025-12-26_1729_Under-Siege-2-Streaming.md (4 conversations)
- b36: 2025-12-26_1753_Childhood-Reflection-Analysis.md … 2025-12-27_1524_Gerda-Christian-Biography.md (11 conversations)
- b37: 2025-12-28_0755_Tesco-Sheet.md … 2025-12-29_2005_Scooter-Error-Code-16.md (9 conversations)
- b38: 2025-12-29_2056_Using-ChatGPT-as-Journal.md … 2025-12-30_1652_Project-Reflection-Framework.md (7 conversations)
- b39: 2025-12-30_1709_Clarifying-Boundaries-and-Impact.md … 2025-12-31_0026_ASD-Support-Levels.md (16 conversations)
- b40: 2025-12-31_0034_18-asd-stuff.md … 2025-12-31_1412_0-0-0-Chat-Sandbox.md (10 conversations)
- b41: 2025-12-31_1440_0-1-1-Receipt-Log.md … 2026-01-01_0619_Solar-System-Redraw-Check.md (4 conversations)
- b42: 2026-01-01_0908_Childhood-Info-Request-Process.md … 2026-01-03_1301_A4-Incident-Recall.md (10 conversations)
- b43: 2026-01-03_1303_A1-GPT-History-work.md … 2026-01-03_1414_Polo-Care-Tips.md (12 conversations)
- b44: 2026-01-03_1442_A8-Court-Sandbox.md … 2026-01-03_1522_A10-Project-Output.md (11 conversations)
- b45: 2026-01-03_1534_A6-Voluntary-Interview-Input-Output.md … 2026-01-03_1737_Layer-A7-Defence-Sandbox.md (4 conversations)
- b46: 2026-01-03_1739_Receipt-Acknowledgment.md … 2026-01-03_1739_Receipt-Acknowledgment.md (1 conversations)
- b47: 2026-01-03_1925_Legal-Report-Preparation.md … 2026-01-03_2009_Hylands-Park-Incident-Summary.md (2 conversations)
- b48: 2026-01-03_2041_ASD-Childhood-Reflection.md … 2026-01-05_0959_ICB-Oversight-Request.md (4 conversations)
- b49: 2026-01-05_1315_ASD-Assessment-Deferral-Request.md … 2026-01-05_1829_Document-Tidy-Up.md (6 conversations)
- b50: 2026-01-05_2012_Read-only-Mode-Setup.md … 2026-01-05_2106_Simplified-Document-Overview.md (2 conversations)
- b51: 2026-01-05_2116_ICB-Oversight-Request-Summary.md … 2026-01-05_2220_Cutting-Interlocking-Spurs.md (3 conversations)
- b52: 2026-01-06_0822_Psychologist-Report-Review.md … 2026-01-06_1040_Explaining-Exhaustion-to-HR.md (2 conversations)
- b53: 2026-01-06_1527_Medicash-Proof-of-Purchase.md … 2026-01-08_1121_NHS-Right-to-Choose-Depression.md (6 conversations)
- b54: 2026-01-08_1524_Diode-failure-vs-ADC-issue.md … 2026-01-09_1905_Surviving-Toxic-Workplaces.md (4 conversations)
- b55: 2026-01-09_2131_Z-Pre-Project-PP-chat.md … 2026-01-09_2131_Z-Pre-Project-PP-chat.md (1 conversations)
- b56: 2026-01-10_0514_Shark-CarpetXpert-Model-Identification.md … 2026-01-13_2122_Office-365-Work-Toggle.md (22 conversations)
- b57: 2026-01-13_2142_Test-Electronics-Checklist.md … 2026-01-14_1305_Parent-s-Emotional-Response-Analysis.md (8 conversations)
- b58: 2026-01-14_1453_Appraisal-Chat-Guidance.md … 2026-01-16_0339_Excel-OR-Formula-Explained.md (12 conversations)
- b59: 2026-01-16_0721_Sampling-Rate-Explanation.md … 2026-01-20_1029_Navigating-Work-Challenges.md (8 conversations)
- b60: 2026-01-20_1032_4-Appraisal.md … 2026-01-20_2149_Concrete-Base-and-Timber-Moisture.md (14 conversations)
- b61: 2026-01-21_1226_Cheap-Log-Cabin-Elevation.md … 2026-01-21_1520_Find-Component-by-Designator.md (2 conversations)
- b62: 2026-01-21_2046_SIP-Wall-Installation-Tips.md … 2026-01-21_2046_SIP-Wall-Installation-Tips.md (1 conversations)
- b63: 2026-01-21_2209_Neutron-Radiation-and-Electronics.md … 2026-01-25_1205_Dogs-and-Raw-Pork.md (11 conversations)
- b64: 2026-01-25_1728_Separate-Cabins-for-Acoustics.md … 2026-01-26_1901_Smith-vs-Oracle.md (3 conversations)
- b65: 2026-01-26_2136_Earbud-Repair-Limitations.md … 2026-01-27_1954_Tyvek-Roll-Size-Inquiry.md (4 conversations)
- b66: 2026-01-27_2051_Suspension-or-Resignation.md … 2026-01-27_2051_Suspension-or-Resignation.md (1 conversations)
- b67: 2026-01-28_1653_Soldering-Temp-for-THT.md … 2026-02-03_1143_Debut-Payments-Explained.md (24 conversations)
- b68: 2026-02-04_1318_Document-Comparison-Review.md … 2026-02-06_1346_Process-vs-Engineering-Flow.md (7 conversations)
- b69: 2026-02-07_1606_Autism-Assessment-Cancellation-Reaction.md … 2026-02-07_1606_Autism-Assessment-Cancellation-Reaction.md (1 conversations)
- b70: 2026-02-08_0514_ASD-Assessment-Alternative-Evidence.md … 2026-02-08_0725_3-9.md (36 conversations)
- b71: 2026-02-08_0726_3-10.md … 2026-02-08_0826_Transcript-Request.md (16 conversations)
- b72: 2026-02-08_1226_Managerial-Time-Enforcement-Debate.md … 2026-02-11_0127_DAC-Location-Best-Practices.md (19 conversations)
- b73: 2026-02-11_0246_Mezzanine-Connector-Recommendations.md … 2026-02-14_2158_Voltage-Classification-for-Reset-Restore.md (16 conversations)
- b74: 2026-02-14_2240_Slew-Rate-Control-in-Rameses.md … 2026-02-14_2240_Slew-Rate-Control-in-Rameses.md (1 conversations)
- b75: 2026-02-17_2135_2-Channel-LVDS-Alternatives.md … 2026-02-19_1958_PowerPoint-Crash-Recovery-Tips.md (5 conversations)
- b76: 2026-02-19_2036_Consolidating-Altium-Libraries.md … 2026-02-19_2036_Consolidating-Altium-Libraries.md (1 conversations)
- b77: 2026-02-20_0143_HDMI-to-USB-C-Pinout.md … 2026-02-23_1638_Moving-Pin-Numbers-Altium.md (16 conversations)
- b78: 2026-02-24_0902_ASD-Assessment-Narrative.md … 2026-02-24_0902_ASD-Assessment-Narrative.md (1 conversations)
- b79: 2026-02-24_1641_Autism-Assessment-Reflection.md … 2026-02-27_1531_Missing-connections-in-Altium.md (6 conversations)
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
