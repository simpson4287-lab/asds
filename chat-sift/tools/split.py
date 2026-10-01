"""Split the ChatGPT export into one text file per conversation.
Reads the export read-only; writes chat-sift/work/<date>_<time>_<title>.md and work/manifest.json.
Messages on the visible thread are numbered M1..Mn. Edited/regenerated branches that are not
on the visible thread are appended at the end as A1..An so nothing is lost."""
import json, glob, os, re, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORK = os.path.join(ROOT, 'chat-sift', 'work')
def ts(t): return datetime.datetime.fromtimestamp(t, datetime.timezone.utc) if t else None
def slug(s): return (re.sub(r'[^A-Za-z0-9]+', '-', s or 'untitled').strip('-')[:60] or 'untitled')
def text_of(m):
    out = []
    for p in m['content'].get('parts', []) or []:
        if isinstance(p, str): out.append(p)
        elif isinstance(p, dict):
            ct = p.get('content_type', 'attachment')
            out.append(p.get('text', '') if ct == 'audio_transcription' else ('[voice]' if 'audio' in ct else ('[image]' if 'image' in ct else f'[{ct}]')))
    for a in (m.get('metadata') or {}).get('attachments', []) or []:
        out.append(f"[attached file: {a.get('name','?')}]")
    return '\n'.join(x for x in out if x)
def who(m):
    r = m['author']['role']
    return {'user': 'ME', 'assistant': 'AI'}.get(r, r.upper())
manifest = []; used = set()
for f in sorted(glob.glob(os.path.join(ROOT, 'Conversations__*-part-0001', 'conversations-*.json'))):
    src = os.path.relpath(f, ROOT)
    for c in json.load(open(f, encoding='utf-8')):
        mp = c['mapping']; path = []; n = c.get('current_node')
        while n: path.append(n); n = mp[n].get('parent')
        path.reverse(); onpath = set(path)
        d = ts(c.get('create_time'))
        base = f"{d:%Y-%m-%d_%H%M}_{slug(c.get('title'))}"; name = base; i = 2
        while name in used: name = f'{base}-{i}'; i += 1
        used.add(name)
        lines = [f"# {c.get('title')}", f"Date (UTC): {d:%Y-%m-%d %H:%M}", f"Conversation ID: {c.get('conversation_id') or c.get('id')}", f"Source file: {src}", '']
        k = 0
        def emit(nid, label):
            m = mp[nid].get('message')
            if not m: return False
            if m['author']['role'] in ('system',) : return False
            t = text_of(m)
            if not t.strip() or (m.get('metadata') or {}).get('is_visually_hidden_from_conversation'): return False
            mt = ts(m.get('create_time'))
            lines.append(f"[{label}] {who(m)}" + (f" ({mt:%Y-%m-%d %H:%M})" if mt else '') + ':')
            lines.append(t); lines.append('')
            return True
        for nid in path:
            if emit(nid, f'M{k+1}'): k += 1
        alt = [nid for nid in mp if nid not in onpath]
        a = 0
        if alt:
            alt.sort(key=lambda x: (mp[x].get('message') or {}).get('create_time') or 0)
            hdr = len(lines); lines.append('=== ALTERNATE BRANCHES (edited/regenerated messages not on the final thread) ===\n')
            for nid in alt:
                if emit(nid, f'A{a+1}'): a += 1
            if not a: del lines[hdr:]
        body = '\n'.join(lines)
        open(os.path.join(WORK, name + '.md'), 'w', encoding='utf-8').write(body)
        manifest.append({'file': name + '.md', 'title': c.get('title'), 'date': f'{d:%Y-%m-%d}', 'source': src,
                         'id': c.get('conversation_id') or c.get('id'), 'messages': k, 'alt': a, 'chars': len(body)})
manifest.sort(key=lambda x: x['file'])
json.dump(manifest, open(os.path.join(WORK, 'manifest.json'), 'w'), indent=1, ensure_ascii=False)
print(len(manifest), sum(x['chars'] for x in manifest))
