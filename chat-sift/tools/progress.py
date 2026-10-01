"""Regenerate output/progress.md from work/batches.json and work/results/."""
import json, os, datetime
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = json.load(open(os.path.join(R, 'work', 'batches.json')))
done, todo, cnt = [], [], {'yes': 0, 'partial': 0, 'no': 0}
for b in B:
    p = os.path.join(R, 'work', 'results', b['batch'] + '.json')
    if os.path.exists(p):
        d = json.load(open(p)); done.append(b)
        for x in d: cnt[x['work_related']] += 1
    else: todo.append(b)
n = lambda bs: sum(len(b['files']) for b in bs)
L = ['# chat-sift progress', '', f'Updated: {datetime.datetime.utcnow():%Y-%m-%d %H:%M} UTC', '',
     '## Setup', '- Source: ChatGPT export (`Conversations__…-part-0001/conversations-000..008.json`) at the repo root, read-only. Nothing in it is edited.',
     '- Split into one file per conversation: `chat-sift/work/<date>_<time>_<title>.md` (828 files, UTC timestamps). Script: `chat-sift/tools/split.py`.',
     '- Reading rules for each batch: `chat-sift/work/READER_INSTRUCTIONS.md`. Per-batch results: `chat-sift/work/results/bNN.json`.',
     '- Outputs are built from the results by `chat-sift/tools/build.py` (verbatim text is pulled from the split files by message ID).', '',
     '## Status', f'- Batches done: {len(done)} / {len(B)}', f'- Conversations read: {n(done)} / {n(B)}',
     f"- So far: yes {cnt['yes']}, partial {cnt['partial']}, no {cnt['no']}", '',
     '## To resume', 'Run each batch below that has no `work/results/bNN.json`, following READER_INSTRUCTIONS.md. Then run `tools/build.py` and `tools/progress.py`, and commit.', '',
     '## Batches done', ', '.join(b['batch'] for b in done) or '(none)', '',
     '## Remaining', ]
for b in todo: L.append(f"- {b['batch']}: {b['files'][0]} … {b['files'][-1]} ({len(b['files'])} conversations)")
if not todo: L.append('(none)')
open(os.path.join(R, 'output', 'progress.md'), 'w').write('\n'.join(L) + '\n')
print(f'{len(done)}/{len(B)} batches', cnt)
