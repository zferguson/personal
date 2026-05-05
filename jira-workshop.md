# ERM Jira Training — Facilitator Outline & Talking Points

**Format:** 2-part series, 45 minutes each, recorded | **Audience:** ERM team, basic technical skills

-----

## Pre-Session Checklist (Before Either Session)

- All attendees have working Jira logins with access to the ERM project
- Demo screen is projected and readable from the back of the room
- ERM Jira project is pre-populated with realistic Initiatives, Milestones, and Stories
- Quick reference card distributed (printed or shared digitally)
- Parking lot visible on whiteboard or flip chart
- Recording is confirmed running before you begin talking
- Task sheet for that session is ready to distribute

> **Recording note:** Remind attendees at the start of each session that it is being recorded. Keep demo actions deliberate and narrated — recordings are only useful if someone watching alone can follow what you’re clicking and why.

-----

-----

# PART 1 — Foundations

**Duration:** 45 minutes | **Goal:** Attendees can navigate Jira, understand the ERM hierarchy, and use the Kanban board for daily work

-----

## Pre-Session Checklist (Part 1 Specific)

- Part 1 task sheet ready to distribute
- Board filtered to show active Stories with a mix of statuses (so the board looks like real work, not empty)
- User settings page accessible — know the path before you’re on camera

-----

## P1-Section 1 — Why We’re Moving to Jira (0:00–0:08)

**Objective:** Establish the problem before introducing the tool. Anchor to the prior state so the audience understands what changes for them personally.

### Talking Points

- “Before we look at anything in Jira, I want to spend two minutes on why we’re doing this.”
- Name the prior state explicitly: work was managed individually across Excel, PowerPoint, Teams, and Outlook. Everyone had their own system. No shared visibility.
- The result: status required hunting people down. Work fell through the cracks between tools. Leadership had no single place to look. None of that is anyone’s fault — it’s what happens without a shared system.
- Jira is not a mandate to work differently for its own sake. It is the shared system that replaces the fragmented one. Once everyone is using it consistently, you always know who owns what, what’s in progress, and what’s stuck — without a meeting or an email chain.
- We are not going fully agile. No sprints, no story points. We are using Jira’s structure with estimated start and end dates. The goal is visibility and accountability, not a methodology overhaul.
- By the end of Part 1, everyone will be able to find their work, update it, and navigate the board. Part 2 will go deeper.

-----

## P1-Section 2 — The ERM Work Hierarchy (0:08–0:18)

**Objective:** Translate Jira’s three-level structure into ERM language with concrete examples. This is the most important conceptual block in the entire series — if this doesn’t land, nothing else will.

### Talking Points

**Lead with the translation, not Jira’s native terms.**

> “Jira has three levels we’ll use. What we call an Initiative, Jira calls an Epic. What we call a Milestone, Jira calls a Feature. Stories are Stories in both. Use our terms — the tool will reflect that.”

**The Kanban analogy — use this early:**

> “Think of the Kanban board like a to-do list made visible for the whole team. Every card on the board is a piece of work. The columns tell you where that work stands. That’s it. Everything else builds on that.”

**Initiative (Epic in Jira) — ~12 months**

- The umbrella for a full year of work within a major program or risk domain.
- Example: *Launch Risk Metrics Program*, *2025 Enterprise Risk Assessment*, *Board Reporting Framework*
- Created by ERM leadership. If you think something needs to be a new Initiative, raise it — don’t create one on your own.
- On the Plan view, these appear as the top-level timeline bars.

**Milestone (Feature in Jira) — few months**

- A workstream or phase within an Initiative. Think of it as a major deliverable block.
- Example: *Define Metrics & Thresholds*, *Develop Automated Data Pipeline*, *Build Reporting & Alert System*
- Milestones group all the Stories beneath them. Their status in the Plan reflects the roll-up of that work.

**Story — 2–3 weeks**

- A discrete task. One owner. One deliverable. Completable in two to three weeks by one person.
- Example: *Draft KRI definitions for operational risk category*, *Build extraction query for source data*, *Conduct UAT with ERM team*
- This is where most team members will spend their time — creating and updating Stories.

**The size test — teach it explicitly:**

> “If you’re unsure where something belongs, use the time horizon. About a year → Initiative. A few months → Milestone. Two to three weeks → Story. If a Story keeps growing past three weeks, split it or flag it.”

**The title rule — say it now, reinforce it throughout:**

> “A Story title should be verb-led and specific enough that someone else could pick it up and know what done looks like. ‘KRI work’ tells no one anything. ‘Draft KRI definitions for operational risk category’ tells everyone.”

-----

## P1-Section 3 — Navigation & the Kanban Board (0:18–0:28)

**Objective:** Show one clear path through the tool. No feature tour. No tangents. Get them oriented with the Board as the primary daily view.

> Facilitator note: Live demo on projected screen with ERM project open. Narrate every click out loud. Recording viewers need to be able to follow without seeing the room.

### Talking Points & Click Path

**Logging in and orienting**

- “When you log in, you’ll land on a home dashboard. Don’t worry about what’s on it — our first stop is the Board.”
- Left sidebar → Board. “This is where your daily work lives.”

**Reading the board**

- Walk the columns out loud: To Do, In Progress, In Review, Done.
- “In Review has two sub-statuses — In Peer Review and Work Complete. We’ll cover what each means shortly.”
- Point to a card. “Every card is a Story. The card shows the title, the assignee, and the current status at a glance.”

**Opening and reading a Story**

- Click on a card. Walk through each field: title, assignee, status, parent Milestone, start date, due date.
- “One place. Everything you need to know about a piece of work. Current — as long as people keep it updated.”

**Finding your own work**

- Show the Assignee filter at the top of the board. Filter to your name.
- “This is your starting point every morning. Filter to yourself, see what’s open, and work from there.”

**Updating status**

- Drag a card from one column to another. “That’s all a status update is.”
- Also show: open a ticket → click the status dropdown → select new status. “Two ways to do the same thing.”

**Quick look at the Plan view**

- Left sidebar → Plan. “This is the leadership and project overview — Initiative and Milestone bars on a timeline.”
- “You’ll use this to check overall progress or pull a status update together. Your daily work happens on the Board. We’ll go deeper on Plan in Part 2.”
- Switch back to Board.

-----

## P1-Section 4 — User Settings & Notifications (0:28–0:33)

**Objective:** Get everyone’s personal settings in a usable state before the hands-on block. Notifications especially — out-of-the-box Jira is noisy.

### Talking Points & Click Path

- Profile icon (top right) → Account Settings or Profile.
- **Display name:** Confirm it shows your actual name. Matters for Assignee fields and @mentions.
- **Notifications:** This is the most important setting to touch on Day 1.
  - Default Jira notifications are high-volume. If left unconfigured, people will start ignoring them and miss real updates.
  - Recommended baseline: notify on items assigned to you, items you’re watching, and @mentions. Turn off broad project-wide notifications.
  - Show where to find notification preferences and let attendees adjust during the hands-on block.
- **Email vs. in-app:** Jira can notify via email or in-app bell icon. Preference is personal — just make sure it’s deliberate, not default.

> Facilitator note: Don’t spend more than 5 minutes here. The point is to make them aware and give them a minute during hands-on to configure. This is not a deep settings walkthrough.

-----

## P1-Section 5 — Hands-On Practice (0:33–0:42)

**Objective:** Every attendee completes real actions in the tool. Protect this block — it’s where retention happens.

> Distribute the task sheet before starting. Walk the room. Answer questions at the desk, not from the front.

### Part 1 Task Sheet

> Complete these in order. Ask a neighbor before raising your hand.

1. **Navigate to the Board.** Left sidebar → Board.
1. **Filter to your name.** Use the Assignee filter at the top. How many Stories are assigned to you?
1. **Open a Story** assigned to you. Read the title, status, parent Milestone, and due date.
1. **Update the status** of one Story. Drag the card to a new column — or open the item and use the status dropdown.
1. **Add a comment.** Open a Story → scroll to Activity → Add a comment. Write a brief status note.
1. **Create a new Story.** + Create → Type: Story → link to a Milestone → set title, assignee, start date, due date → Save.
1. **Check your notifications.** Profile icon → Account Settings → Notifications. Adjust to your preference.
1. **Bonus:** Switch to Plan view. Find the Initiative that contains the Milestone you linked your Story to.

### Facilitator Notes While Walking the Room

- The date fields trip people up. Know the field names (“Start date” / “Due date”) in your version of Jira and be ready to point to them directly.
- If someone creates an unlinked Story, use it as a live teaching moment: “This is what happens when you skip the parent Milestone — it won’t appear in the Plan.”
- Step 6 is the critical one. Make sure everyone creates at least one Story with all fields populated before time is up.
- Common question: “Can I edit someone else’s Story?” Have the permissions answer ready from your testing.

-----

## P1-Section 6 — Close & Preview of Part 2 (0:42–0:45)

**Objective:** Address parked questions, reinforce the reference card, set expectations for Part 2.

### Talking Points

- Address parking lot items if time allows.
- “The reference card covers everything we did today — hierarchy on one side, status definitions and click paths on the other. Keep it.”
- “Between now and Part 2, the one thing to do: open Jira, find your Stories, and make sure they reflect where things actually stand. If a status is wrong, fix it. That’s the habit that makes this work.”
- Preview Part 2: “Next session we’ll go deeper — linking items across the hierarchy, using filters to slice the board, the Plan view in full, and how to think about work in a more structured way as we mature our use of the tool.”
- Confirm Part 2 date and time.

-----

-----

# PART 2 — Going Deeper

**Duration:** 45 minutes | **Goal:** Attendees can link items across the hierarchy, use filters effectively, navigate the Plan view, and begin thinking about work structurally

> **Assumption:** Attendees have completed Part 1 and have at least one Story they created and own in the system.

-----

## Pre-Session Checklist (Part 2 Specific)

- Confirm recording is running
- Have a Story ready that demonstrates a linking scenario (a Story linked to wrong Milestone, or an unlinked Story)
- Board filtered to show a realistic mix of statuses — not a clean slate
- Know your filter options in advance; test them before the session
- Part 2 task sheet ready to distribute

-----

## P2-Section 1 — Quick Recap & Common Questions from Part 1 (0:00–0:05)

**Objective:** Re-anchor the group before going deeper. Surface anything that broke or confused people after Part 1.

### Talking Points

- “Before we go further — what questions came up after Part 1? What broke, what was confusing, what did you try that didn’t work?”
- Take 2–3 questions max. Anything complex goes to the parking lot.
- Re-state the core frame: “Board is daily work. Plan is project overview. Stories are the unit of work — one person, two to three weeks, verb-led title. Everything in Part 2 builds on that.”

-----

## P2-Section 2 — Linking Items Across the Hierarchy (0:05–0:18)

**Objective:** Teach attendees how to properly connect Stories to Milestones and Milestones to Initiatives, and what breaks when those links are missing.

### Talking Points

**Why linking matters**

- Unlinked Stories are invisible in the Plan view. They exist on the Board but don’t contribute to the Initiative or Milestone’s progress tracking.
- The hierarchy only works if every Story is connected to its parent Milestone, and every Milestone to its parent Initiative.
- This is the most common error in early Jira adoption — items created in isolation that drift.

**How to link a Story to a Milestone (live demo)**

- Open a Story. Find the parent field (usually labeled “Epic Link” or “Parent” depending on Jira configuration — confirm your field name before the session).
- Click the field → search for the Milestone name → select it → Save.
- Show how it now appears under that Milestone in the Plan view.

**How to link a Milestone to an Initiative**

- Open a Milestone (Feature). Find the parent Initiative (Epic) field. Link it the same way.
- “If a Milestone isn’t linked to an Initiative, it floats — it won’t appear in the Initiative’s Plan bar.”

**Re-linking: fixing a wrong parent**

- Open the Story or Milestone → click the parent field → change the selection.
- “This is common in early use. Don’t hesitate to fix it — it takes ten seconds.”

**Creating a Story from inside a Milestone (the preferred method)**

- Navigate to the Milestone → click to add a child Story from within it.
- “This method automatically sets the parent link. It’s faster and eliminates the most common error.”

**What to check if a Story isn’t showing in the Plan:**

1. Is it linked to a Milestone?
1. Is that Milestone linked to an Initiative?
1. Does it have start and end dates? (Undated items may not render on the timeline.)

-----

## P2-Section 3 — Filters & Board Management (0:18–0:28)

**Objective:** Teach attendees how to slice the Board to find what they need — by assignee, by Initiative, by status — and how to use saved filters.

### Talking Points

**Why filters matter as the board grows**

- Right now the board may feel manageable. As more Stories are created, an unfiltered board becomes noise.
- Filters let you scope your view to exactly what’s relevant — your work, your team’s work, one Initiative at a time.

**Assignee filter (covered in Part 1 — reinforce it)**

- Top of the Board → Assignee dropdown → select a name.
- “This is your daily starting point. Always filter to yourself before reviewing your work.”

**Filtering by Initiative (Epic filter)**

- Top of the Board → Epic (or Initiative) filter → select the Initiative name.
- “Now the board shows only Stories that belong to that program. Use this when you’re preparing a project update or reviewing progress on a specific Initiative.”

**Filtering by label or other fields (if configured)**

- Walk through any additional filters configured in your Jira project.
- Keep this grounded in what’s actually available — don’t teach filters that don’t exist in your instance.

**Searching within Jira**

- Search bar (top of screen) → type a Story number or keyword.
- “If you know a ticket number from an email or message, this is the fastest way to find it.”

**Saved filters and board views (if applicable)**

- If your Jira instance supports saved filters or custom board views, show how to save a filter for reuse.
- “Set it up once, click it every morning. No reconfiguring.”

**What good board hygiene looks like**

- A well-maintained board should have very few items sitting in “In Progress” for more than a week without a comment update.
- “If you look at the board and everything is In Progress, that’s a signal — either the work is actually stuck, or the statuses aren’t being updated. Both are worth knowing.”

-----

## P2-Section 4 — The Plan View in Full (0:28–0:35)

**Objective:** Teach attendees how to read and use the Plan (Gantt) view for project progress and leadership reporting.

### Talking Points

**When to use the Plan vs. the Board**

- Board = daily delivery. Where am I? What’s next? What needs to move?
- Plan = project progress. Are we on track? What’s coming up? What’s at risk?
- Leadership will likely use the Plan view. Team members will mostly use the Board. But everyone should know how to read the Plan.

**Navigating the Plan (live demo)**

- Left sidebar → Plan.
- Show Initiative bars at the top level. Expand to show Milestones beneath them. Expand further to show Stories.
- “The bars are driven by the start and end dates on each item. If a Story has no dates, it won’t render correctly on the timeline — another reason dates are required.”

**Reading the timeline**

- Identify what’s on track, what’s overdue, and what’s upcoming.
- “An overdue bar — one that extends past today without being marked Done — is a flag. It means either the work is late or the dates haven’t been updated.”

**Using the Plan for a status update**

- “If you’re pulling together a status update for leadership, open the Plan, filter to the relevant Initiative, and screenshot or export. The visual gives immediate context without digging through individual tickets.”

**Adjusting dates from the Plan view**

- Drag a bar to extend or shift it. “You can update dates directly here — you don’t have to open every individual ticket.”
- Note: this only works if the team member has edit permissions. Confirm in advance.

**What the Plan can’t tell you**

- It shows dates and status, not narrative. It won’t explain why something is late.
- “The Plan is the map. The comments inside each Story are the story. You need both.”

-----

## P2-Section 5 — Thinking About Work Structurally (0:35–0:40)

**Objective:** Introduce the mindset shift from individual task management to structured, visible, connected work — without overcomplicating it.

### Talking Points

**The shift from individual to shared**

- Before Jira: everyone managed work in their own system. Status lived in someone’s head or their personal spreadsheet.
- With Jira: work is visible by default. You don’t have to ask someone for a status update — you look.
- The implication: what you put in Jira (or don’t) affects the whole team’s ability to see reality.

**Thinking in Stories, not tasks**

- A task is something you do. A Story is something with a clear definition of done, an owner, and a time horizon.
- “Before creating a Story, ask: what does done actually look like? If I handed this to someone else tomorrow, would they know when it was finished? If not, the title or description needs work.”

**Thinking about flow, not just completion**

- Jira’s value isn’t just knowing what’s done — it’s knowing where things are stuck.
- “If something has been In Progress for two weeks with no comment, that’s a signal. Either it’s stuck and needs help, or the status hasn’t been updated. Either way, the board is telling you something.”

**As we mature: what comes next**

- We are not using story points or sprints yet. That may change.
- “The discipline we build now — consistent status updates, proper linking, realistic dates — is what makes any future maturity possible. Get the basics right first.”

-----

## P2-Section 6 — Hands-On Practice (0:40–0:43)

**Objective:** Reinforce Part 2 concepts through direct action. Shorter block than Part 1 — by now they should be faster in the tool.

### Part 2 Task Sheet

> Complete these in order.

1. **Check your Stories from Part 1.** Are they linked to the correct Milestone? If not, fix the parent link now.
1. **Filter the board by one Initiative.** Use the Epic filter. How many Stories are currently In Progress under that Initiative?
1. **Navigate to the Plan view.** Find the Initiative you just filtered. Expand it to see its Milestones and Stories.
1. **Identify one overdue or undated Story** in the Plan. Open it and add or correct the dates.
1. **Find a Story using the search bar.** Use a keyword or ticket number from a real item you know exists.
1. **Bonus:** Create a Story from inside a Milestone (navigate to the Milestone → add child Story). Compare this to how you created one from the Board in Part 1.

-----

## P2-Section 7 — Close & Next Steps (0:43–0:45)

**Objective:** Reinforce what was covered, address parked questions, set concrete next steps.

### Talking Points

- Address parking lot items if time allows — 1–2 max, others follow up async.
- “You now have the full picture: how to navigate the board, how the hierarchy connects, how to use filters to find what you need, and how to read the Plan.”
- **The three habits that make this work:**
1. Update your Story status the day it changes — not at the end of the week.
1. Every Story has an owner, a parent Milestone, and a due date. No exceptions.
1. Use comments for progress updates. The Description is for scope; Comments are for what’s happening.
- “The recordings of both sessions are available at [location]. Share them with anyone who missed a session or needs a refresher.”
- “Questions as they come up: [Teams channel / contact name]. Don’t let a Jira question become a reason to stop using it — ask.”

-----

-----

## Facilitator Notes — Both Sessions

**If a section runs long:** Cut the hands-on block last. If you have to compress something, compress the talking points sections, not the time attendees spend in the tool.

**If logins don’t work:** Pair the attendee with a neighbor. Do not troubleshoot live for more than 90 seconds — it kills momentum for the room and creates dead air on the recording.

**If someone asks a complex or edge-case question mid-session:** “Good one — parking lot. Let’s keep moving so we protect hands-on time.” Follow up after or via Teams.

**Recording-specific considerations:**

- Narrate every action out loud. Clicking without speaking is dead air on the recording.
- When demoing, move deliberately — pause briefly before clicking so viewers can follow.
- Avoid saying “as you can see here” — describe what you’re pointing to explicitly for audio-only context.
- Start each session by stating what it covers: “This is Part 1 of the ERM Jira training. Today we’ll cover…”

**Post-Part-1 action:** Within 48 hours, send attendees the recording link and a reminder to update their Story statuses before Part 2.

**Post-Part-2 action:** Within one week, send the finalized team norms document. Without a written anchor, the agreements made in training will drift within a month.