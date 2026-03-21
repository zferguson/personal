-----

## name: discovery-call
description: “Use this skill for anything related to prospect discovery calls, scoping calls, intro calls, or sales conversations for Ferguson Insights. Triggers include: preparing for a call with a prospect, debriefing after a call, generating follow-up emails, qualifying a prospect, building a discovery agenda, creating call notes, updating CRM records from call notes, drafting a discovery SOW or proposal based on call findings, analyzing whether a prospect is worth pursuing, or any mention of ‘discovery call’, ‘scoping call’, ‘intro call’, ‘prospect call’, ‘sales call’, or ‘client call’. Also trigger when the user pastes raw call notes and wants them organized, scored, or turned into next steps. Do NOT use for general business strategy, website copy, or marketing content unrelated to a specific prospect interaction.”

# Discovery Call Skill — Ferguson Insights

## Purpose

This skill helps Zach prepare for, execute, and follow up on prospect discovery calls. It enforces a structured process that keeps calls prospect-focused (70/30 listening ratio), surfaces real qualification signals, and converts call outcomes into concrete pipeline actions.

## Context

Ferguson Insights targets COOs, CFOs, and heads of analytics at mid-size RIAs ($500M–$2B AUM), broker-dealers, insurance firms, and fintechs. The core value proposition is senior-level, hands-on analytics execution — “the person who scopes the project builds it” — covering reporting modernization, executive dashboards, data consolidation, and fractional analytics leadership.

Zach has 10+ years of financial services analytics experience (Edward Jones, New York Life, Fisher Investments), is completing an MS in Analytics at Georgia Tech (May 2026), and co-presented at the Databricks Data + AI Summit 2025.

The engagement model is: paid discovery assessment → build phase → handoff/training → optional retainer.

OBA constraints apply: zero work during trading hours (before 7:30 AM and after 5 PM weekdays, plus weekends). This affects scheduling but should never be mentioned to prospects — just work around it.

## Call Structure (30 minutes)

### Pre-Call Prep (5 min before)

Before any call, gather and present:

1. **Firm profile** — AUM, headcount, regulatory filings (ADV Part 2A if RIA), recent news
1. **Contact profile** — Title, LinkedIn summary, tenure, likely pain points for their role
1. **Two or three specific observations** — Something from their ADV brochure, website, or public filings that signals a potential need (e.g., “They mention 15 model portfolios but their tech stack section only lists Excel and Morningstar Direct”)
1. **Hypothesis** — A one-sentence guess at their core pain point, to be tested on the call

When helping with prep, pull from IAPD/ADV data if available. Frame observations as conversation starters, not conclusions.

### Opening (2 min)

The opening sets the frame: this is about them, not a pitch. Two elements:

- **Frame-setter:** “I’ve got about 30 minutes — I’d love to spend most of that understanding what’s going on with your data and reporting, and if it makes sense we can talk about next steps at the end.”
- **One-liner intro:** “I’ve spent the last decade doing analytics and reporting modernization inside firms like Edward Jones and New York Life — now I help firms like yours get the same capability without the full-time headcount.”

Then stop talking. Do not elaborate on credentials unless asked.

### Discovery (18 min)

Four areas to cover. Follow the thread of conversation rather than running through these mechanically — but make sure all four are addressed by minute 20.

**Current state of reporting and data**

- “Walk me through how your team gets the numbers they need for [portfolio reviews / compliance reporting / executive decisions] today.”
- Follow-ups: “What’s manual in that process?” and “Where does it break?”
- Listen for: Excel dependency, copy-paste workflows, reports that take days, numbers that don’t match across systems, single points of failure (one person who knows how it works)

**Impact and urgency**

- “When reporting breaks or is slow, what’s the downstream effect?”
- “How long has this been the situation?”
- “What’s changed recently that’s making you look at this now?”
- Listen for: compliance risk, missed opportunities, executive frustration, staff burnout, trigger events (new regulation, leadership change, growth spurt, failed audit, M&A activity)

**Prior attempts**

- “Have you tried to solve this before — internal project, another vendor, a tool purchase?”
- Listen for: shelfware (bought Tableau but nobody uses it), failed internal projects, bad vendor experiences, political landmines, sunk costs that create anchoring

**Decision process**

- “If we got to a point where an engagement made sense, what would that process look like on your end?”
- Listen for: who decides, budget authority, timeline, other stakeholders, procurement requirements, compliance/vendor due diligence

### Reflect Back (3 min)

Summarize in their language: “So it sounds like the core issue is [X], it’s costing you [Y], and you’ve tried [Z] but it didn’t stick because [reason].”

This confirms understanding and forces corrections. Either outcome is valuable.

### Next Steps (2 min)

Do not pitch a solution on this call. Instead:

- Propose a paid discovery assessment (typically 1–2 weeks) as the next step
- If they’re not ready, offer to send a one-pager or case study and schedule a follow-up
- Always leave with a specific next action and a date

## Qualification Scoring

After every call, score the prospect on five criteria (1–5 each, 25 max):

|Criteria                      |What a 5 looks like                                          |What a 1 looks like                                     |
|------------------------------|-------------------------------------------------------------|--------------------------------------------------------|
|Pain is real and articulated  |They described specific broken workflows with concrete impact|Vague dissatisfaction, can’t name what’s wrong          |
|Urgency / trigger event exists|Clear forcing function (audit, new regulation, exec mandate) |“We’ve been meaning to look at this for a while”        |
|Budget authority on the call  |Decision-maker present, discussed budget range               |Junior contact, no idea how decisions get made          |
|Decision process is clear     |Named the steps, timeline, and stakeholders                  |“I’d have to check with some people”                    |
|Good fit for my skills        |Core reporting/data/analytics problem I’ve solved before     |Needs something outside my lane (app dev, cybersecurity)|

**Score interpretation:**

- 20–25: Qualified — send discovery SOW within 48 hours
- 15–19: Promising — schedule follow-up, send targeted collateral
- 10–14: Nurture — add to drip, check back in 60 days
- Below 10: Not a fit — close out gracefully, ask for referrals

## Red Flags

Watch for these during or after the call. Any one of these should lower the qualification score and inform the follow-up approach:

- They spend the whole call asking about rates without engaging on their problems (price shopping)
- They can’t articulate what’s broken (need may not be real)
- The contact can’t describe how a decision would get made (not the buyer)
- They want a proposal before a discovery call (want free scoping work)
- Unrealistic timelines or budgets relative to the problem described
- They mention they’re talking to five other vendors (RFP mode — low win rate for a solo consultant)

## Post-Call Outputs

When processing call notes or debriefing, always produce:

1. **CRM record** — Structured summary following the Notion template format: firm details, pain points in their words, trigger event, tech stack, decision process, qualification score, pipeline status, and follow-up actions
1. **Follow-up email** — Three sentences max: thank them, restate the core problem you heard, confirm the next step. Send same day.
1. **Honest assessment** — A candid read on likelihood to close, what would need to be true for this to convert, and whether it’s worth the pursuit given current bandwidth

## Follow-Up Email Templates

**Template: Qualified prospect — proposing discovery**

Subject: Following up — [Firm Name] analytics assessment

[Name], thanks for the conversation today. Based on what you described around [one-sentence summary of core problem], I think a structured assessment of your current data and reporting environment would surface some quick wins alongside a longer-term roadmap. I’ll send over a brief scope document for that — happy to walk through it whenever works for you.

**Template: Nurture — not ready yet**

Subject: Good connecting — [Firm Name]

[Name], I appreciated the conversation today. When [trigger event or future milestone they mentioned] comes around, I’d be glad to revisit how I might help on the analytics side. In the meantime, I’ll send over [relevant case study or article] that touches on what we discussed.

**Template: No fit — close gracefully**

Subject: Thanks for the time — [Firm Name]

[Name], thanks for taking the time today. Based on our conversation, it sounds like [brief reason this isn’t a fit right now]. If that changes down the road, don’t hesitate to reach out. And if you know anyone in your network dealing with reporting or data challenges, I’m always happy to have a conversation.

## Engagement Type Mapping

Based on discovery findings, map to the most likely initial engagement:

|What you heard                                          |Likely engagement                        |
|--------------------------------------------------------|-----------------------------------------|
|“Our reports take forever and nobody trusts the numbers”|Reporting modernization                  |
|“We have data in six different systems”                 |Data consolidation                       |
|“Our board wants better dashboards”                     |Executive dashboard build                |
|“We don’t have anyone who can do this internally”       |Fractional analytics leadership          |
|“We just need someone to tell us what to do”            |Paid discovery / data strategy assessment|

## Right-Sizing Guidance

For the $100M–$1B AUM segment, resist the urge to propose enterprise-grade tooling. Common right-sizing decisions:

- Excel + Power Query before recommending a BI tool
- PostgreSQL or SQLite before Snowflake
- Python scripts before Databricks
- Simple dashboards before real-time streaming
- Manual processes with documentation before full automation

The client’s problem is almost always a data organization problem, not a technology problem. Lead with data plumbing, not advanced analytics.