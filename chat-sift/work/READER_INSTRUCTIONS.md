# Reader instructions (one batch)

You are reading a batch of ChatGPT conversations that were split from an export into
`chat-sift/work/*.md`. In each file, `ME` is the account owner and `AI` is ChatGPT. Messages
on the final thread are numbered `[M1]`, `[M2]`, and so on. Messages from edited or
regenerated branches appear after the line `=== ALTERNATE BRANCHES ===` and are numbered
`[A1]`, `[A2]`, and so on.

## What to do
Read EVERY file in your batch IN FULL. Read every message, including long AI messages and
alternate branches. Use the Read tool with offset/limit for long files until you have
covered every line. Do not skim, and do not decide from the title.

For each conversation, decide whether it is **work-related**:
- **yes**: the conversation is substantially about the owner's work.
- **partial**: some passages are work-related and the rest is not.
- **no**: there is no work-related content.

"Work" means the owner's employment and working life. This includes the employer, the
job/role and duties, managers, colleagues, HR, occupational health, reasonable adjustments,
sickness absence or return to work, workload, performance, appraisals/reviews, workplace
meetings, emails or incidents, grievances, disciplinaries, tribunals and employment law as it
applies to them. It also includes the effect of work on their health or wellbeing, job
applications and interviews, and professional projects they do as work. The owner's own
ventures or proposals (for example a business or community project they are setting up) and
anything else you are unsure about count as work-related but are marked
`"borderline": true`. **If in doubt, include it and mark it borderline.**

## Output
Write ONE JSON file to the path you are given. It must be a list with one object per
conversation, in the batch order:
```json
{
  "file": "2025-12-17_2157_Reasonable-adjustments-delay.md",
  "work_related": "yes" | "no" | "partial",
  "borderline": false,
  "reason": "one line",
  "extracts": [
    {
      "messages": ["M3", "M4", "M5"],
      "trim": {"M4": {"start": "exact first words of kept part", "end": "exact last words of kept part"}},
      "tags": ["worried", "speculative"],
      "borderline": false
    }
  ]
}
```
Rules:
- `reason`:
  - For **no**, write exactly `No work-related content.` Do NOT describe or summarise
    personal, non-work content in any way.
  - For yes/partial, write one neutral line that says only what work matter is discussed.
    No conclusions, no judgements, and no mention of the non-work parts.
- `extracts` must be empty for **no**. For yes/partial, list every work-related passage. Each
  extract is a run of messages on one work topic, normally ME's message(s) together with the
  AI reply(ies) that belong to them. Do not leave out work content. If a whole conversation
  is work, its extracts cover the whole conversation.
- Use `messages` to list message IDs. Leave out any non-work messages that fall inside the
  run. A gap in the IDs will be shown as an omission.
- Use `trim` ONLY when a single message mixes work and non-work content, or when a very long
  AI message has only a part that is work-related. `start` and `end` MUST be copied EXACTLY,
  character-for-character, from that message (about 6-15 words each, and unique within the
  message). The kept text runs from `start` to the end of `end`. A script checks them. If
  unsure, do not trim.
- Never paraphrase, correct or rewrite any text. The final document quotes the source
  directly by message ID. Dictation errors stay as they are.
- `tags`: include any that apply, based on **ME's own words** in the extract:
  - `worried`
  - `angry`
  - `upset`
  - `unsettled`
  - `speculative`: ME guesses, suspects, theorises or assumes something about people,
    motives, causes or what will happen, rather than stating a known fact.

  Tag only what ME's words actually show. Do not infer or interpret beyond that. Use an empty
  list if none apply.
- `borderline: true` on an extract or conversation whenever inclusion is doubtful.
- Non-work personal content (health unrelated to work, family, legal matters unrelated to
  work, hobbies, etc.) is left out entirely. Do not quote, list or summarise it anywhere.

When you have written the file, validate it with
`python3 chat-sift/tools/check.py <your json>` and fix any error it reports. Then reply with
only: the batch id, conversations read, and the yes/partial/no counts. Do not echo any content
in your reply.
