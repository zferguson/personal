# Copilot Daily Briefing Prompt — v2

**Executive Assistant Style · Full M365 Copilot Required**

-----

## How to Use

1. Start with the **Personalized Version** below — edit it once for your role, then reuse it every day
1. Replace anything in `[brackets]` with your details
1. Delete any `[OPTIONAL]` sections you do not need
1. Save your final version so you can paste it in seconds each morning

> **Use the personalized version by default.** The role and priority context meaningfully improves Copilot’s judgment on what to flag. The generic version is a fallback for teams where roles vary too much to standardize.

### Requirements

|Feature                      |Requirement                                         |
|-----------------------------|----------------------------------------------------|
|Email, Teams, Calendar, Tasks|Microsoft 365 Copilot license (paid)                |
|Jira section                 |Atlassian Jira Cloud connector enabled by M365 admin|
|Weather & Commute            |No setup — works via web automatically              |

-----

## Step 1: Personalized Version *(use this daily)*

*Copy from here, edit the bracketed fields once, then paste each morning.*

-----

You are acting as my executive assistant. I am [your role, e.g., a Manager of Data Analytics at a financial services firm]. My top ongoing priorities are [2–3 things, e.g., delivering reporting projects on time, managing stakeholder communications, and supporting my team]. Anything touching [key people or projects, e.g., my VP or the Q1 board deck] should be flagged as high priority by default.

I want a complete morning briefing. Be direct and specific. No filler, pleasantries, or transitional phrases. If something requires my attention or decision, say so plainly.

Before generating the briefing: check which data sources you have access to. For any source you cannot access — Outlook, Teams, Calendar, Tasks, Jira, or web — state this in one line at the top of that section rather than skipping it or inferring content you cannot verify.

Pull from: Outlook email, Teams messages, calendar, tasks, and Jira. Also check current weather and commute. Cover the period from the end of my last working day through right now.

Structure your briefing exactly as follows:

-----

**SITUATION SUMMARY**
One short paragraph. Lead with the single most important thing I need to know. Surface anything time-sensitive, anything that escalated since yesterday, any thread I am likely to get pulled into, and any context I need before my first meeting. Include a one-line weather and commute note only if conditions are notable enough to affect my day — otherwise omit it here.

-----

**EMAILS REQUIRING ACTION**
List only emails requiring a response, decision, or follow-up. For each:

- Sender and subject
- What they need from me, in one sentence
- Urgency: High / Medium / Low
- Suggested next step, if obvious

Ignore: newsletters, automated notifications, CC-only messages, and anything informational only.

If I appear on the same recurring low-priority thread as in recent briefings with no action taken, deprioritize it unless something has materially changed — note why if you do include it.

*FYI Only (sub-section):* List emails I should be aware of but do not need to act on.

If you cannot access Outlook, state that here.

-----

**TEAMS MESSAGES REQUIRING ACTION**
Same format as email. List only messages where someone is waiting on me. Group by channel or conversation thread. Flag direct @mentions separately from general channel activity.

If you cannot access Teams, state that here.

-----

**JIRA STATUS** *(optional — delete if not using Jira)*

Group results as follows:

*Due Today / This Sprint:* Ticket ID, title, status, priority
*Assigned to Me:* Ticket ID, title, status, priority
*Blockers & High Priority:* Any blocker in my active projects, even if not assigned directly to me
*Mentioned or Tagged:* Any ticket where I was tagged or mentioned since yesterday

If a group has nothing to report, state that in one line. If you cannot access Jira, state that here.

-----

**TODAY’S PRIORITIES**
Synthesize everything above — email, Teams, Jira, tasks, and calendar — into a prioritized list of what I must accomplish today.

Rules:

- Default: 3 to 5 items
- If more than 5 things are genuinely urgent today, list all of them and explicitly flag: *“This is a high-load day — [X] items are time-sensitive”*
- Do not compress or omit urgent items to stay within 5
- For each: what it is, why it is the priority (deadline / dependency / who is waiting), and estimated time if obvious
- Exclude anything low-stakes with no dependencies

-----

**ACTION ITEMS CARRIED FORWARD**
List commitments I made or tasks assigned to me that are not yet complete, drawn from recent email, Teams, and Jira. Include who is waiting and any stated or implied deadline.

-----

**TODAY’S SCHEDULE**
List calendar events in chronological order. For each:

- Time and duration
- Meeting name and attendees (abbreviated if large group)
- One-sentence purpose or expected outcome
- Flag: conflicts, back-to-back meetings with no buffer, meetings I have not accepted

After the schedule: note any gaps of 30 minutes or more suitable for focused work.

If you cannot access Calendar, state that here.

-----

**WEATHER & COMMUTE** *(optional — delete if not needed)*
Weather: Current conditions and forecast for [your city]. Note temperature, precipitation, anything unusual.
Commute: Estimated drive time from [home area] to [office]. Flag delays or incidents. Skip if working from home today.

If web access is unavailable, state that here.

-----

**DECISIONS NEEDED TODAY**
List open decisions I am blocking from any source above. For each: what the decision is, who is waiting, and what information is available to help me decide.

-----

**SUGGESTED FOLLOW-UPS**
Based on today’s briefing content, list the 3 follow-up prompts most relevant to what came up — drawn from the Follow-Up Prompts section below. State each as a ready-to-paste prompt with the relevant details already filled in from the briefing.

-----

END OF BRIEFING. No closing summary or wrap-up paragraph.

-----

## Step 2: Generic Version *(fallback only)*

Use this if distributing to a team where roles differ too much to personalize. Less effective than the personalized version.

> You are acting as my executive assistant. I want a complete morning briefing that helps me walk into the day fully prepared. Be direct and specific. No filler, pleasantries, or transitional phrases. If something requires my attention or decision, say so plainly.
> 
> Before generating the briefing: check which data sources you have access to. For any source you cannot access, state this in one line at the top of that section rather than skipping it or inferring content you cannot verify.
> 
> *Then paste the full briefing structure from Step 1 above, starting from “Pull from: Outlook email…” onward.*

-----

## Follow-Up Prompts

The briefing will automatically suggest the 3 most relevant ones each morning. You can also use any of these manually at any time.

**Deep-dive an email thread**

> Pull up the full thread from [sender] about [subject]. Summarize the history, what has been decided, and what is still unresolved.

**Draft a reply**

> Draft a reply to [sender]’s email about [subject]. My response: [your key point]. Tone: [direct / professional / brief]. No pleasantries.

**Deep-dive a Jira ticket**

> Give me full detail on [ticket ID]. Summarize history, current status, what is blocking it if anything, and what the next action should be.

**Sprint summary**

> Summarize the current sprint for [project]. What is complete, in progress, blocked, and are we on track to finish by the sprint end date?

**Mid-day reprioritization**

> It is now [time]. Based on what has come in since this morning and my remaining schedule, what should I focus on for the rest of the day? Be specific.

**End-of-day close-out**

> Review my tasks, today’s email, Teams, and Jira. What did I commit to today that is not yet done? What carries forward to tomorrow and what can be closed out?

**Meeting prep**

> I have a meeting with [person or group] about [topic] in [X] minutes. Give me: key context, any relevant recent messages between us, and 2–3 things I should accomplish.

**Afternoon commute check**

> What is the current drive time from [office] to [home area]? Any delays I should know about?

-----

## Tips

**Run it before opening your inbox.** Reading email first compromises the objective prioritization the briefing is designed to give you.

**Switch to Think Deeper** in the model selector before pasting. The default model will handle this prompt, but Think Deeper produces noticeably better synthesis and prioritization judgment.

**If Copilot reports it cannot access a source:**

- Missing Outlook / Teams / Calendar: verify your M365 Copilot license is active and you are on the Work tab (shield icon visible in top right)
- Missing Jira: ask your M365 admin to enable the Atlassian Jira Cloud connector under Copilot > Connectors > Gallery in the admin center. You also need to install the Jira Cloud plugin in Teams and toggle it on in the plugin popup.

**If the briefing is too long**, append to the prompt:

> Keep the entire briefing under 500 words. Cut anything not directly actionable or time-sensitive.

**If Copilot misses items**, append:

> Do not limit to the most recent messages. Scan all unread and flagged items from the past 24 hours.

**For a weekly version:** change the time window to “from end of last Friday through right now” and add a final section — *Week Ahead:* “Based on my calendar and open Jira tickets, what are the most important things this week and what do I need to prepare in advance?”

-----

*Last updated: March 2026 · v2*
