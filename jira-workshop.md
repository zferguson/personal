# ERM Jira Training — Facilitator Outline & Talking Points

**Duration:** 60 minutes | **Audience:** ERM team, basic technical skills | **Format:** Live demo + hands-on

-----

## Pre-Session Checklist (Before Anyone Arrives)

- All attendees have Jira logins that work and can access the ERM project
- Your demo screen is projected and readable from the back of the room
- Jira project is pre-populated with realistic ERM content (Initiatives, Milestones, Stories)
- One-page quick reference card is printed or shared digitally
- Task sheet is printed or shared — one per person (see Hands-On section below)
- Parking lot visible on whiteboard or flip chart
- Backup person identified if group is large (10+)

-----

## Section 1 — Why This Matters (0:00–0:08)

**Objective:** Frame the problem Jira solves before touching the tool. Get buy-in before showing anything.

### Talking Points

- Start with the pain, not the product. Ask the group: “How do you currently track who owns what on a project?” Let someone answer. Validate the friction they name.
- The problem isn’t effort — it’s visibility. Work gets lost in email. Status requires hunting people down. No one has a single place to look.
- Jira is not a task manager for its own sake. It is a visibility and accountability tool. If it’s used consistently, you always know what’s in progress, what’s stuck, and what’s done — without asking anyone.
- We are not going fully agile. No story points, no sprints. Just a clean structure for tracking work with start dates, end dates, and owners.
- One hour from now, everyone in this room will know how to find their work, update it, and create new items. That’s the goal.

-----

## Section 2 — The ERM Work Hierarchy (0:08–0:20)

**Objective:** Translate Jira’s structure into ERM language. This is the most important conceptual moment in the session — if this doesn’t land, nothing else will.

### Talking Points

**Lead with the translation, not the Jira terms.**

> “Jira has three levels we’ll use. What we call an Initiative, Jira calls an Epic. What we call a Milestone, Jira calls a Feature. And Stories are Stories. Functionally, use our terms — the tool will reflect that.”

**Initiative (Epic in Jira) — ~12 months**

- A major program or risk domain. Think of it as the umbrella for a full year of work.
- Example: *Launch Risk Metrics Program*, *2025 Enterprise Risk Assessment*, *Board Reporting Framework*
- Initiatives are created by leadership. If you think something needs to be a new Initiative, raise it — don’t create one unilaterally.
- On the Plan view, these are the top-level bars on the timeline.

**Milestone (Feature in Jira) — few months**

- A workstream or phase within an Initiative. Think of it as a major deliverable or phase gate.
- Example under *Launch Risk Metrics Program*: *Define Metrics & Thresholds*, *Develop Automated Data Pipeline*, *Build Reporting & Alert System*
- Milestones group all the Stories beneath them. Their status on the Plan reflects the roll-up of the work inside.

**Story — 2–3 weeks**

- A discrete task. One owner. One deliverable. Should be completable in two to three weeks by one person.
- Example: *Draft KRI definitions for operational risk category*, *Build extraction query for source data*, *Conduct UAT with ERM team*
- This is where most of you will spend your time in Jira — creating and updating Stories.

**The size test — teach this explicitly:**

> “If you’re not sure where something belongs, use the time horizon. About a year → Initiative. A few months → Milestone. Two to three weeks → Story. If a Story keeps growing past three weeks, either split it or flag it — it may need to become its own Milestone.”

**Common mistakes to name now so they don’t happen later:**

- Creating a Story that’s actually a Milestone in scope (multi-month, multi-person)
- Leaving a Story unlinked to a Milestone — it won’t show in the Plan view
- Titling a Story vaguely: “KRI work” tells no one anything. “Draft KRI definitions for operational risk” tells everyone exactly what done looks like

-----

## Section 3 — Live Demo: Navigation & the Board (0:20–0:32)

**Objective:** Show one clear path through the tool. Do not wander. Do not give a feature tour.

> Facilitator note: Do this yourself on a projected screen with the pre-configured ERM project open. Narrate every click out loud.

### Talking Points & Click Path

**Finding the Board**

- “When you log in, you’ll land on a dashboard. To get to our board, use the left sidebar and click Board.”
- Show the board. Name the columns out loud: To Do, In Progress, In Review, Done. Point out that In Review contains two sub-statuses — In Peer Review and Work Complete.

**Reading a card**

- Click on any Story card. Walk through each field: title, assignee, status, parent Milestone, start date, due date.
- “This is everything you need to know about a piece of work. One place, always current — if people update it.”

**Finding work assigned to you**

- Show the Assignee filter at the top of the board. Filter to your own name. “This is how you find your work every morning.”

**Navigating the hierarchy**

- From a Story, click the parent Milestone link. Show how it rolls up to the Initiative.
- “You can always see context — where this Story fits in the bigger picture.”

**The Plan view (briefly)**

- Switch to Plan via the left sidebar. Show the Initiative and Milestone bars on the timeline.
- “This is the leadership view. You’ll use this to check overall project progress or prepare a status update. Your daily work happens on the Board, not here.”
- Switch back to the Board. Keep the focus there.

-----

## Section 4 — Hands-On Practice (0:32–0:50)

**Objective:** Every attendee completes a sequence of real actions in the tool. This is the session — protect this time.

> Facilitator note: Distribute the task sheet before this block. Walk the room. Answer questions at the desk, not from the front. Keep a running eye on who’s stuck.

### Task Sheet (distribute printed or shared)

> Complete these in order. Ask a neighbor before raising your hand.

1. **Find the board.** Use the left sidebar → Board.
1. **Filter to your name.** Use the Assignee filter at the top. How many Stories are assigned to you?
1. **Open a Story** assigned to you. Read the title, status, due date, and parent Milestone.
1. **Update the status** of one Story. Drag the card to a new column, or open the item and use the status dropdown.
1. **Add a comment** to a Story. Open item → scroll to Activity → Add a comment. Write anything — this is practice.
1. **Create a new Story.** Click + Create → Type: Story → link it to a Milestone → set a title, assign it to yourself, add a start date and due date → Save.
1. **Bonus:** Switch to the Plan view. Find the Initiative that contains the Milestone you just linked your Story to.

### Talking Points While Walking the Room

- Watch for the date field — it trips people up. If someone can’t find the calendar widget, show them the field name (“Start date” / “Due date”) and confirm which version of Jira they’re seeing.
- If someone creates an unlinked Story, use it as a live teaching moment for the group: “This is what happens when you skip the parent Milestone — it won’t show in the Plan.”
- Validate when people get through step 6. That’s the critical action — create, link, date, assign.
- Common question: “Can I edit someone else’s Story?” Answer depends on permissions you’ve confirmed. Have the answer ready.

-----

## Section 5 — Workflow Norms & Team Agreements (0:50–0:57)

**Objective:** Establish shared expectations. These decisions don’t live in Jira — they live in the team. Training is the right moment to set them.

> Facilitator note: These should be decided in advance where possible. If not, use this as a live discussion and document what the group agrees to. Capture on whiteboard.

### Talking Points

**Status definitions — make them concrete, not abstract**

- *Open* = assigned and not started. This is the default for every new Story.
- *In Progress* = you have actively started working on it. Move it the day you begin — not the day before, not retroactively.
- *In Peer Review* = your work is done; you’re waiting for someone else to review it.
- *Work Complete* = review passed; waiting for final sign-off or stakeholder acceptance.
- *Done* = fully closed. No open questions, no pending actions.
- *Cancelled* = will not be completed. Always add a comment explaining why before closing.

**Update frequency**

- Minimum expectation: update status whenever it changes. Don’t let a card sit in “In Progress” for three weeks untouched.
- Recommended: quick scan of your open Stories at the start or end of each week.

**Creation authority**

- Who creates Initiatives: [confirm and state]
- Who creates Milestones: [confirm and state]
- Who creates Stories: [all team members / confirm]

**Description vs. Comments**

- Description = scope. What the Story is, what done looks like, any relevant links. Set it when you create the ticket and don’t touch it again.
- Comments = progress. Updates, blockers, decisions, anything time-stamped. If you’re telling someone where things stand, it goes in Comments.

**Overdue Stories**

- If a due date slips, update the due date AND add a comment explaining why. Do not leave an overdue Story open and silent.

**The one norm that determines whether this works:**

> “Jira only works if it reflects reality. A Story still showing ‘Open’ that’s been active for two weeks defeats the entire purpose. The five seconds it takes to drag a card is what gives everyone — including leadership — an accurate picture without a status meeting.”

-----

## Section 6 — Questions & Close (0:57–1:00)

**Objective:** Address parked questions, reinforce the reference card, set expectations for next steps.

### Talking Points

- Return to the parking lot on the whiteboard. Address anything time allows.
- Point to the quick reference card: “Side 1 has the hierarchy and status definitions. Side 2 has the click paths and team norms we just agreed to. This is your cheat sheet — keep it.”
- “If you run into something the card doesn’t cover, [contact / Teams channel] is the right place to ask.”
- “Over the next week, the most important thing is to update any Stories you own to the correct status. If the board looks wrong, fix it. That’s the first habit to build.”
- Do not end by asking “any other questions?” End by stating what happens next: “We’ll do a quick check-in [timeframe] to see how it’s going and answer anything that’s come up.”

-----

## Facilitator Notes

**If you run long in Sections 1–3:** Cut the Plan view demo entirely. The Board is what they’ll use daily. Plan is secondary and can be covered in a follow-up.

**If hands-on runs over:** Do not cut it. Compress the norms section instead — email the norms doc within 24 hours rather than covering everything live.

**If someone has a complex Jira question mid-session:** “Great one for the parking lot — let’s keep moving so everyone gets hands-on time.”

**If logins don’t work for some attendees:** Pair them with someone who is logged in. Do not spend more than two minutes troubleshooting live — it kills momentum for the room.

**Post-training:** Within one week, send the team norms as a written document. Without a written anchor, the agreements from today will drift.