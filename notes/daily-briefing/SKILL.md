---
name: copilot-daily-briefing
description: >
  Generates a complete, ready-to-paste Microsoft Copilot Chat prompt for a daily
  executive assistant-style morning briefing. Use this skill whenever a user asks
  to improve their Copilot experience, build a daily briefing, create a morning
  standup prompt, automate their daily agenda, or get an AI assistant to summarize
  their email, Teams, calendar, Jira, or work activities. Also trigger when a user
  asks how to use Copilot as an executive assistant, how to start their day with AI,
  or how to consolidate their daily work context into a single prompt. Produces a
  personalized, versioned prompt with failure handling, source-aware sections, and
  contextual follow-up suggestions — significantly better than a generic summary
  prompt. Covers Outlook, Teams, Calendar, Tasks, Jira (optional), and
  weather/commute (optional).
---

# Copilot Daily Briefing Skill

Produces a complete, paste-ready Microsoft 365 Copilot Chat prompt that acts as a
daily executive assistant briefing. Output is personalized to the user's role,
includes failure handling for disconnected sources, and generates contextual
follow-up prompts based on what came up that morning.

## When to Use This Skill

Trigger whenever a user wants to:
- Build or improve a Copilot morning briefing prompt
- Use Copilot to summarize email, Teams, calendar, or Jira
- Automate their daily agenda or work prioritization
- Set up Copilot as an executive assistant

## Output

Deliver two files:
1. `copilot-daily-briefing.txt` — plain text, easy to paste into Copilot
2. `copilot-daily-briefing.md` — formatted markdown for wikis, SharePoint, Confluence

If the user only needs one format, produce that one only.

---

## Step 1: Gather User Context

Before generating, collect:

| Field | Purpose | Default if not provided |
|---|---|---|
| Role / job title | Personalizes priority judgment | Generic version (less effective) |
| Top 2–3 priorities | Tells Copilot what to flag high | Omitted |
| Key stakeholders / projects | Escalation triggers | Omitted |
| City / location | Weather section | Prompt user to fill in |
| Office location | Commute section | Prompt user to fill in |
| Uses Jira? | Include/exclude Jira section | Include with [OPTIONAL] label |
| Works in office or remote? | Include/exclude commute | Include with [OPTIONAL] label |
| Team distribution? | Single user vs. team handout | Single user personalized version |

If generating for a team rather than an individual, produce the generic version
(Step 2 in the prompt) as the primary output, with a note explaining the
personalized version is more effective for individual use.

---

## Step 2: Generate the Prompt

Use the template below. Substitute collected context into `[brackets]`. Remove
`[OPTIONAL]` markers and their sections if user confirmed they are not needed.
If context was not provided for a bracketed field, leave the bracket in so the
user knows to fill it in.

---

### PROMPT TEMPLATE — TXT FORMAT

```
========================================================
  COPILOT DAILY BRIEFING PROMPT  v2
  Executive Assistant Style — Full M365 Copilot Required

  HOW TO USE:
  1. Open Copilot Chat — Work tab (shield icon visible)
  2. Paste the PERSONALIZED VERSION each morning, before
     opening email or Teams
  3. Fill in [brackets] once, then remove them
  4. Delete OPTIONAL sections you do not need
  5. Save your version for fast daily reuse

  REQUIREMENTS:
  - M365 Copilot license (paid): email, Teams, calendar,
    tasks
  - Atlassian Jira Cloud connector (admin-enabled): Jira
  - Weather & commute: no setup, works via web
========================================================

You are acting as my executive assistant. I am [ROLE].
My top priorities are [PRIORITY_1], [PRIORITY_2], and
[PRIORITY_3]. Anything touching [KEY_STAKEHOLDERS_OR_
PROJECTS] should be flagged high priority by default.

Be direct and specific. No filler or pleasantries. If
something requires my attention or decision, say so plainly.

Before generating: check which sources you can access.
For any source you cannot reach — Outlook, Teams, Calendar,
Tasks, Jira, or web — state this in one line at the top of
that section. Do not skip or infer content you cannot verify.

Pull from: Outlook, Teams, calendar, tasks, Jira. Check
weather and commute. Cover end of last working day to now.

---

SITUATION SUMMARY
One paragraph. Lead with the single most important thing
I need to know. Surface anything time-sensitive, escalated
since yesterday, or needed before my first meeting. Include
weather/commute only if conditions are notable — otherwise
omit here.

---

EMAILS REQUIRING ACTION
List only emails needing response, decision, or follow-up.
For each:
- Sender and subject
- What they need, in one sentence
- Urgency: High / Medium / Low
- Suggested next step, if obvious

Exclude: newsletters, auto-notifications, CC-only,
informational-only messages.

If I appear on the same recurring low-priority thread as
in recent briefings with no action taken, deprioritize it
unless something has materially changed — note why if
including it.

FYI ONLY: List emails I should know about but not act on.

If you cannot access Outlook, state that here.

---

TEAMS MESSAGES REQUIRING ACTION
Same format as email. Only messages where someone is waiting
on me. Group by channel or thread. Flag direct @mentions
separately from general channel activity.

If you cannot access Teams, state that here.

---

JIRA STATUS [OPTIONAL — DELETE IF NOT USING JIRA]
Group as:
DUE TODAY / THIS SPRINT: ticket ID, title, status, priority
ASSIGNED TO ME: ticket ID, title, status, priority
BLOCKERS & HIGH PRIORITY: any blocker in active projects,
  even if not assigned to me
MENTIONED OR TAGGED: tagged or mentioned since yesterday

If a group has nothing to report, say so in one line.
If you cannot access Jira, state that here.

---

TODAY'S PRIORITIES
Synthesize email, Teams, Jira, tasks, and calendar into
what I must accomplish today.

Rules:
- Default: 3–5 items
- If more than 5 things are genuinely urgent, list all
  and flag: "High-load day — [X] items are time-sensitive"
- Do not compress urgent items to stay within 5
- For each: what it is, why it is the priority, estimated
  time if obvious
- Omit anything low-stakes with no dependencies

---

ACTION ITEMS CARRIED FORWARD
Commitments I made or tasks assigned to me not yet complete,
from recent email, Teams, and Jira. Include who is waiting
and any deadline.

---

TODAY'S SCHEDULE
Calendar events in chronological order. For each:
- Time and duration
- Meeting name and attendees (abbreviated if large group)
- One-sentence purpose or expected outcome
- Flag: conflicts, back-to-back with no buffer, not accepted

After schedule: note gaps of 30+ minutes for focused work.
If you cannot access Calendar, state that here.

---

WEATHER & COMMUTE [OPTIONAL — DELETE IF NOT NEEDED]
Weather: Conditions and forecast for [CITY].
Commute: Drive time from [HOME_AREA] to [OFFICE]. Flag
delays. Skip if WFH today.
If web is unavailable, state that here.

---

DECISIONS NEEDED TODAY
Open decisions I am blocking from any source above.
For each: what it is, who is waiting, what info is available.

---

SUGGESTED FOLLOW-UPS
Based on today's briefing, list the 3 most relevant
follow-up prompts from the list below, with details already
filled in from this briefing. State each as a ready-to-paste
prompt.

---

END OF BRIEFING. No closing summary or wrap-up.
```

---

### FOLLOW-UP PROMPTS (include in both output files)

```
Deep-dive an email thread:
"Pull up the full thread from [sender] about [subject].
Summarize history, what was decided, and what is unresolved."

Draft a reply:
"Draft a reply to [sender]'s email about [subject].
My response: [key point]. Tone: [direct/professional/brief].
No pleasantries."

Deep-dive a Jira ticket:
"Full detail on [ticket ID]: history, current status,
blockers, and next action."

Sprint summary:
"Summarize the current sprint for [project]. Complete,
in progress, blocked, and on track?"

Mid-day reprioritization:
"It is [time]. Based on what has come in and my remaining
schedule, what should I focus on? Be specific."

End-of-day close-out:
"Tasks, email, Teams, Jira today: what did I commit to
that is not done? What carries forward, what can close?"

Meeting prep:
"Meeting with [person/group] about [topic] in [X] min.
Key context, recent messages between us, 2–3 goals."

Afternoon commute:
"Drive time from [office] to [home area] right now?
Any delays?"
```

---

### TIPS SECTION (include in both output files)

```
Run before opening your inbox — reading email first
undermines objective prioritization.

Switch to Think Deeper in the model selector before
pasting — noticeably better synthesis and prioritization.

If a source is missing:
- Outlook/Teams/Calendar: verify M365 Copilot license,
  confirm Work tab is active (shield icon visible)
- Jira: ask admin to enable Atlassian Jira Cloud connector
  in M365 admin center > Copilot > Connectors > Gallery.
  Also install Jira Cloud plugin in Teams and toggle on.

If briefing is too long, append:
"Keep under 500 words. Cut anything not directly
actionable or time-sensitive."

If Copilot misses items, append:
"Scan all unread and flagged items from the past 24 hours."

For a weekly version: change time window to "end of last
Friday through now" and add WEEK AHEAD section: "Based on
calendar and open Jira, what are the most important things
this week and what do I need to prepare?"
```

---

## Step 3: Format and Deliver

**TXT file:** Use the template exactly as structured above —
ASCII section dividers, plain text throughout, all-caps
section headers. No markdown syntax. Paste-ready.

**MD file:** Convert to markdown — `#`/`##`/`###` headers,
blockquotes for the pasteable prompt blocks, tables for
requirements, clean section breaks. Suitable for SharePoint,
Confluence, or wiki pages.

**File naming:**
- `copilot-daily-briefing.txt`
- `copilot-daily-briefing.md`

---

## Step 4: Personalization Notes to Include

At the top of the output, briefly note:
- Which sections were removed as not applicable
- Which bracketed fields still need the user to fill in
- Whether this is the personalized or generic version and why

Example:
> Generated personalized version for a data analytics manager.
> Jira and weather/commute sections included — remove if not
> needed. Still needs: [KEY_STAKEHOLDERS_OR_PROJECTS] and
> [CITY] / [HOME_AREA] / [OFFICE] filled in.

---

## Known Limitations

- Copilot cannot run this prompt on a schedule — it must be
  triggered manually each morning.
- Jira section requires admin enablement of the Atlassian
  connector; individual users cannot self-serve this.
- Quality of prioritization degrades on days with very high
  volume (20+ action items) — the high-load flag in the
  priorities section partially mitigates this.
- Copilot may drift from the briefing structure in later
  turns of a long session; the prompt should be re-pasted
  if the session has been running for a while.
- The suggested follow-ups section depends on Copilot's
  ability to self-reference its own output — this works
  reliably in Think Deeper mode, less so in Quick Response.
