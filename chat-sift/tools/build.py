"""Build output/index.xlsx and output/extracts.docx from work/results/*.json.
All quoted text is pulled verbatim from the split files by message ID (see check.py)."""
import json, os, re, sys
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_BREAK
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check import messages, apply_trim
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, O = os.path.join(R, 'work'), os.path.join(R, 'output')
MAN = {m['file']: m for m in json.load(open(os.path.join(W, 'manifest.json')))}
BAT = json.load(open(os.path.join(W, 'batches.json')))
rows = []
for b in BAT:
    p = os.path.join(W, 'results', b['batch'] + '.json')
    if os.path.exists(p): rows += json.load(open(p, encoding='utf-8'))
rows.sort(key=lambda d: d['file'])  # file names start with date_time
ILLEGAL = re.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f￾￿]')
clean = lambda s: ILLEGAL.sub('', s)
short = lambda src: src.split('/')[-1]

# ---- index.xlsx
wb = Workbook(); ws = wb.active; ws.title = 'Index'
hdr = ['Date', 'Title', 'Source file', 'Split file', 'Work-related', 'Borderline', 'Reason', 'Extracts']
ws.append(hdr)
for c in ws[1]: c.font = Font(bold=True, color='FFFFFF'); c.fill = PatternFill('solid', fgColor='1F3864')
fills = {'yes': 'C6EFCE', 'partial': 'FFEB9C', 'no': 'F2F2F2'}
for d in rows:
    m = MAN[d['file']]
    bl = d.get('borderline') or any(x.get('borderline') for x in d.get('extracts', []))
    ws.append([m['date'], clean(m['title'] or ''), m['source'], d['file'], d['work_related'],
               'borderline' if bl else '', clean(d['reason']), len(d.get('extracts', []))])
    ws.cell(ws.max_row, 5).fill = PatternFill('solid', fgColor=fills[d['work_related']])
for col, w in zip('ABCDEFGH', [12, 45, 40, 50, 13, 12, 80, 9]): ws.column_dimensions[col].width = w
for r in ws.iter_rows(min_row=2):
    for c in r: c.alignment = Alignment(vertical='top', wrap_text=c.column in (2, 7))
ws.freeze_panes = 'A2'; ws.auto_filter.ref = ws.dimensions
cnt = {k: sum(1 for d in rows if d['work_related'] == k) for k in ('yes', 'partial', 'no')}
s = wb.create_sheet('Counts')
for r in [['Conversations read', len(rows)], ['Included (yes)', cnt['yes']], ['Included (partial)', cnt['partial']],
          ['Included total', cnt['yes'] + cnt['partial']], ['Excluded (no)', cnt['no']],
          ['Total in export', len(MAN)]]: s.append(r)
s.column_dimensions['A'].width = 22
wb.save(os.path.join(O, 'index.xlsx'))

# ---- extracts.docx
ME_C, AI_C = RGBColor(0x1F, 0x4E, 0x79), RGBColor(0x59, 0x59, 0x59)
doc = Document()
st = doc.styles['Normal']; st.font.name = 'Calibri'; st.font.size = Pt(10.5)
doc.add_heading('Work-related extracts', 0)
doc.add_paragraph('Verbatim passages from ChatGPT conversations, in date order. The text is copied '
                  'exactly as it appears in the export, including any dictation errors.')
key = [('ME', 'my own words (blue, left bar)'), ('AI', 'ChatGPT’s words (grey, indented)'),
       ('[…]', 'text left out: either non-work messages between quoted ones, or the non-work part of a message'),
       ('BORDERLINE', 'inclusion was uncertain, so it is included under the "if in doubt, include" rule'),
       ('Tags', 'worried / angry / upset / unsettled / speculative, based on my own words in the extract'),
       ('SPECULATIVE', 'my thinking at the time, not established fact')]
for k, v in key:
    p = doc.add_paragraph(style='List Bullet'); r = p.add_run(k + ': '); r.bold = True; p.add_run(v)
doc.add_paragraph('Times are UTC as recorded in the export.')
n = 0
def body(par_fmt_who, text, color, italic=False):
    lines = clean(text).split('\n')
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(4)
    if par_fmt_who == 'ME': p.paragraph_format.left_indent = Cm(0.3)
    else: p.paragraph_format.left_indent = Cm(1.2)
    for i, ln in enumerate(lines):
        r = p.add_run(ln); r.font.color.rgb = color; r.italic = italic
        if i < len(lines) - 1: r.add_break(WD_BREAK.LINE)
    return p
for d in rows:
    if d['work_related'] == 'no': continue
    m = MAN[d['file']]; ms = messages(d['file'])
    for x in d['extracts']:
        n += 1
        doc.add_heading(f"Extract {n} — {m['date']} — {clean(m['title'] or '')}", 2)
        meta = doc.add_paragraph(); meta.paragraph_format.space_after = Pt(2)
        for lab, val in [('Date', m['date']), ('Conversation', clean(m['title'] or '')), ('Source file', m['source']),
                         ('Split file', 'chat-sift/work/' + d['file']), ('Conversation classed as', d['work_related'])]:
            r = meta.add_run(lab + ': '); r.bold = True; meta.add_run(val); meta.add_run().add_break(WD_BREAK.LINE)
        tags = x.get('tags') or []
        r = meta.add_run('Tags: '); r.bold = True; meta.add_run(', '.join(tags) if tags else 'none')
        if x.get('borderline') or d.get('borderline'):
            p = doc.add_paragraph(); r = p.add_run('BORDERLINE'); r.bold = True; r.font.color.rgb = RGBColor(0xC0, 0x50, 0x00)
        if 'speculative' in tags:
            p = doc.add_paragraph(); r = p.add_run('SPECULATIVE — where I speculate in this extract, it is my thinking at the time, not fact.')
            r.bold = True; r.font.color.rgb = RGBColor(0x70, 0x30, 0xA0)
        ids = x['messages']; trims = x.get('trim') or {}
        order = lambda i: (i[0], int(i[1:]))
        prev = None
        for mid in ids:
            if prev and prev[0] == mid[0] and order(mid)[1] != order(prev)[1] + 1:
                p = doc.add_paragraph(); r = p.add_run('[… intervening messages omitted …]'); r.italic = True
            prev = mid
            msg = ms[mid]; who = msg['who']
            h = doc.add_paragraph(); h.paragraph_format.space_after = Pt(0); h.paragraph_format.keep_with_next = True
            h.paragraph_format.left_indent = Cm(0.3 if who == 'ME' else 1.2)
            lab = {'ME': 'ME (my words)', 'AI': 'AI (ChatGPT)'}.get(who, who)
            r = h.add_run(f"{lab} — {mid}" + (f" — {msg['time']} UTC" if msg['time'] else '') + (' — from an edited/regenerated branch' if mid[0] == 'A' else ''))
            r.bold = True; r.font.color.rgb = ME_C if who == 'ME' else AI_C
            text = msg['text']
            if mid in trims:
                t = apply_trim(text, trims[mid])
                pre, post = text.find(t) > 0, text.find(t) + len(t) < len(text.rstrip())
                text = ('[…] ' if pre else '') + t + (' […]' if post else '')
            body(who, text, ME_C if who == 'ME' else AI_C)
doc.save(os.path.join(O, 'extracts.docx'))
print(f"rows {len(rows)} {cnt} extracts {n}")
