# chat-sift progress

Updated: 2026-10-01 15:07 UTC

## Setup
- Source: ChatGPT export (`Conversations__…-part-0001/conversations-000..008.json`) at the repo root, read-only. Nothing in it is edited.
- Split into one file per conversation: `chat-sift/work/<date>_<time>_<title>.md` (828 files, UTC timestamps). Script: `chat-sift/tools/split.py`.
- Reading rules for each batch: `chat-sift/work/READER_INSTRUCTIONS.md`. Per-batch results: `chat-sift/work/results/bNN.json`.
- Outputs are built from the results by `chat-sift/tools/build.py` (verbatim text is pulled from the split files by message ID).

## Status
- Batches done: 98 / 98
- Conversations read: 828 / 828
- So far: yes 251, partial 83, no 494

## To resume
Run each batch below that has no `work/results/bNN.json`, following READER_INSTRUCTIONS.md. Then run `tools/build.py` and `tools/progress.py`, and commit.

## Batches done
b01, b02, b03, b04, b05, b06, b07, b08, b09, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36, b37, b38, b39, b40, b41, b42, b43, b44, b45, b46, b47, b48, b49, b50, b51, b52, b53, b54, b55, b56, b57, b58, b59, b60, b61, b62, b63, b64, b65, b66, b67, b68, b69, b70, b71, b72, b73, b74, b75, b76, b77, b78, b79, b80, b81, b82, b83, b84, b85, b86, b87, b88, b89, b90, b91, b92, b93, b94, b95, b96, b97, b98

## Remaining
(none)
