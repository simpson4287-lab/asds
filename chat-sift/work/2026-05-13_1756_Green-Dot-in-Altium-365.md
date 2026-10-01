# Green Dot in Altium 365
Date (UTC): 2026-05-13 17:56
Conversation ID: 6a04bb42-4c68-83eb-a661-bd6103ed4337
Source file: Conversations__7c20a96482f3aa11fccee3586429b7a503a5350734f19c55cb3e538cc195527e-chatgpt-0001-part-0001/conversations-007.json

[M1] ME (2026-05-13 17:56):
What does the green dot next to a name mean for altium 365?

[M2] AI (2026-05-13 17:56):
In urlAltium 365https://www.altium.com/altium-365 the little green dot next to someone’s name typically means they are currently online / active in the workspace or document session.

You’ll often see it:

- In the collaboration panel
- Next to comments
- In shared document sessions
- In the workspace member list

It’s basically a presence indicator — similar to Teams or Slack. If they’re actively viewing the design/document, sometimes you’ll also see:
- their cursor
- viewport tracking
- what document they have open
- live editing presence

If the dot is:
- Green → online/active
- Grey/off → offline or inactive
- Sometimes hollow/faded → idle/background

In live co-design sessions Altium can also show coloured avatars/cursors for simultaneous users editing/viewing the same project.

There’s also a separate concept in Altium Designer itself where green markers/dots/Xs can indicate DRC or placement/routing states, so context matters a bit. citeturn0search1turn0search3turn0search5

[M3] ME (2026-05-13 17:57):
It’s strange how it’s two people who have left the business only 

[M4] AI (2026-05-13 17:57):
That can happen for a few fairly mundane reasons in urlAltium 365https://www.altium.com/altium-365 — the presence/status system is not always tightly coupled to HR reality or account deactivation.

Common causes:

- Their Altium accounts still exist in the workspace
  - If IT never removed/deactivated them from the workspace, their profiles remain visible.

- Cached/lingering presence
  - Sometimes the green indicator can persist incorrectly due to browser sessions, stale auth tokens, or background services.

- Shared/generic logins
  - Occasionally old accounts remain signed in on a lab PC, build machine, or VM.

- Workspace sync lag
  - Especially with on-prem or hybrid enterprise setups, identity sync can lag behind actual employment status.

- Automated/background access
  - Some integrations or services can appear “online” if the account token is still valid.

Given your setup is relatively newly deployed enterprise/on-prem from what you described before, I honestly wouldn’t treat the green dot as authoritative evidence someone is actively using the system. Early-stage enterprise rollouts often have messy user/admin hygiene for a while.

A quick check:
- Open the workspace members/users area
- See whether their accounts are still enabled
- Check last login / last activity if available
- Verify whether those accounts are tied to SSO/AD sync

That usually explains it pretty quickly.
