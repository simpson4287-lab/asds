"""Validate a batch result JSON against the split files (anchors must match verbatim)."""
import json, re, sys, os
W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'work')
HDR = re.compile(r'^\[([MA]\d+)\] (ME|AI|[A-Z]+)(?: \(([^)]*)\))?:$', re.M)
def messages(fn):
    t = open(os.path.join(W, fn), encoding='utf-8').read()
    hs = list(HDR.finditer(t)); out = {}
    for i, h in enumerate(hs):
        end = hs[i+1].start() if i+1 < len(hs) else len(t)
        body = t[h.end()+1:end]
        body = body.split('\n=== ALTERNATE BRANCHES')[0]
        out[h.group(1)] = {'who': h.group(2), 'time': h.group(3), 'text': body.rstrip('\n')}
    return out
def apply_trim(text, tr):
    s = text.find(tr['start']); e = text.find(tr['end'], max(s, 0))
    if s < 0 or e < 0: return None
    return text[s:e+len(tr['end'])]
def check(path, batch_files=None):
    errs = []; data = json.load(open(path, encoding='utf-8'))
    if batch_files is not None and [d['file'] for d in data] != batch_files:
        errs.append('file list does not match batch')
    for d in data:
        try: ms = messages(d['file'])
        except Exception as ex: errs.append(f"{d.get('file')}: {ex}"); continue
        if d.get('work_related') not in ('yes', 'no', 'partial'): errs.append(f"{d['file']}: bad work_related")
        if d['work_related'] == 'no' and (d.get('extracts') or d.get('reason') != 'No work-related content.'):
            errs.append(f"{d['file']}: 'no' must have no extracts and the fixed reason")
        if d['work_related'] != 'no' and not d.get('extracts'): errs.append(f"{d['file']}: yes/partial without extracts")
        for x in d.get('extracts', []):
            for mid in x.get('messages', []):
                if mid not in ms: errs.append(f"{d['file']}: unknown message {mid}")
            for mid, tr in (x.get('trim') or {}).items():
                if mid not in ms or apply_trim(ms[mid]['text'], tr) is None:
                    errs.append(f"{d['file']}: trim anchors for {mid} not found verbatim")
            bad = set(x.get('tags', [])) - {'worried', 'angry', 'upset', 'unsettled', 'speculative'}
            if bad: errs.append(f"{d['file']}: bad tags {bad}")
    return errs
if __name__ == '__main__':
    b = None
    bid = os.path.basename(sys.argv[1]).split('.')[0]
    for x in json.load(open(os.path.join(W, 'batches.json'))):
        if x['batch'] == bid: b = x['files']
    e = check(sys.argv[1], b)
    print('\n'.join(e) if e else 'OK')
    sys.exit(1 if e else 0)
