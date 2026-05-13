# Jira Training — Facilitator Guide
## Enterprise Risk Management | 60-Minute Session

---

## Pre-Session Checklist

- [ ] Confirm all attendees have Jira Cloud access and can log into the ERM project
- [ ] Stand up a sandbox area in ERM (or a throwaway sub-project) for hands-on practice
- [ ] Pre-create one Example Epic, one Example Feature, and one Example Story using realistic ERM content — do not use Lorem Ipsum
- [ ] Share the Participant Guide (HTML) and Agenda with attendees at least 24 hours before the session
- [ ] Open your Jira browser tab to the ERM project board before the session starts
- [ ] Have a shared doc open (Confluence, Notion, or similar) to capture unanswered questions live
- [ ] Confirm screen share is working if remote

---

## Session Structure

### 0:00–5:00 — Orientation (5 min)

**Objective:** Set context. Establish what Jira is and isn't for this team before anything else.

**Talking points:**
- Jira is the ERM team's system of record. It tracks work across three levels of granularity: Epics, Features, and Stories.
- We are not an agile team. You will not hear "sprints," "velocity," "story points," or "retrospectives" in this session. Those do not apply.
- The project key is ERM. Every ticket gets an ID automatically: ERM-001, ERM-002, etc.
- By the end of this hour, you will be able to create work items at all three levels, link them correctly, find your own work, and run a basic search.

**Watch for:** Anyone who has a strong prior Jira mental model from an agile context. Flag early that the ERM setup is intentionally different — don't let agile assumptions contaminate the session.

---

### 5:00–15:00 — Work Hierarchy & Mental Model (10 min)

**Objective:** Get everyone to the same conceptual starting point before touching the tool.

**Talking points:**
- The three-level hierarchy is a decomposition model, not a process.
  - **Epic:** A major strategic initiative. 6–12 months. Think program-level goals.
  - **Feature:** A major deliverable within an Epic. 1–3 months. Should produce a tangible output.
  - **Story:** A discrete, assignable unit of work. 1–3 weeks. One person, one clear outcome.
- Use a real ERM example to anchor this. For instance: an annual risk appetite review program could be an Epic; the board presentation deck could be a Feature; drafting the narrative section could be a Story.
- The nesting is strict: Stories belong to Features, Features belong to Epics. Orphaned items break rollup reporting.
- The key diagnostic: if one person can complete it in under three weeks, it's a Story. If it spans months and has multiple sub-deliverables, it's a Feature or Epic.

**Check for understanding:** Before moving on, ask: "If I'm writing a risk register update that will take two weeks, what level does that belong at?" Answer should be Story. If you get mixed answers, spend another 2 minutes here — do not move on with confusion at this level.

---

### 15:00–35:00 — Hands-On: Creating & Linking Work Items (20 min)

**Objective:** Everyone creates at least one item at each level and links them correctly.

**This block is the highest-value segment. Do not cut it. If time is short, cut from navigation or orientation instead.**

#### Facilitator demo first (5 min)

Walk through creating a Story from scratch, narrating every field decision out loud:
- Title — action-oriented, names who does what
- Description — context and relevant references
- Acceptance Criteria — specific, verifiable, checklist format
- Assignee — one person only
- Reporter — the stakeholder who owns the outcome
- Priority — relative to other open work
- Start Date and Target End Date — required; Due Date only if there's a hard deadline
- Parent Feature — link it now, not later

Then link the Story to a Feature, and the Feature to an Epic. Explicitly show the Parent field — emphasize this is not the generic "Link" button.

#### Participant practice (15 min)

Have participants:
1. Create a Story based on a real or realistic piece of their own work
2. Fill out all required fields
3. Create a Feature and link the Story to it
4. Link the Feature to an existing Epic (one you've pre-created, or have them create their own)

**Watch the room (or screen shares) during this block.** Common failure points:
- Using the generic "Link" button instead of the Parent field
- Leaving Acceptance Criteria blank ("I'll fill it in later")
- Assigning to a team rather than an individual
- Not filling in Start Date or Target End Date

Correct these live, not after the session.

---

### 35:00–43:00 — Navigation, Views & Workflow (8 min)

**Objective:** Everyone can find their work and understands status conventions.

**Views (4 min):**
- **Board view:** Column-based by status. Best for active work visibility across the team.
- **Backlog view:** Flat list of unstarted work. Use for planning and triaging what's next.
- **List view:** Tabular. Best for sorting by date, reviewing multiple fields, bulk-scanning tickets.
- Demonstrate navigating between all three using the same Story so attendees can see it's the same item, different lens.
- Demonstrate using Global Search: `G G` to focus, then type a name or ticket ID.

**Plans (4 min):**
- Plans is a Gantt-style timeline that plots the full Epic → Feature → Story hierarchy against dates. It is the highest-value view for this team given the multi-month work horizon.
- Open Plans from the left sidebar. Show the hierarchy toggle — start at Epic level, then expand to Feature and Story.
- Explain that date bars are driven by Start Date and Target End Date on each ticket. A missing bar means a missing field — which is a data quality enforcement point.
- Show the Colour by Assignee option. Point out how it surfaces concentration and gaps immediately.
- Demo the zoom control: weeks for tactical, quarters for strategic.
- **Critical norm to establish explicitly:** Plans writes changes directly to live tickets with no undo prompt. Dragging a bar reschedules the ticket. Only edit your own work in Plans.
- Demonstrate one drag/reschedule on a sandbox ticket so they see the write-back behavior, then undo it.

**Workflow & status (4 min):**
- Walk through the four statuses: To Do → In Progress → In Review → Done
- Establish the norm explicitly: you move your own tickets. Status reflects current reality, not intent.
- Move a Story through its full lifecycle live so they see what a transition looks like.
- Cover blocked tickets: use the Flag feature in Jira Cloud, add a blocking comment, tag the relevant person. Do not park blocked work in In Progress without flagging it.

---

### 43:00–53:00 — JQL & Filters (10 min)

**Objective:** Every attendee can write at least one JQL query and save a filter.

**Introduce JQL (3 min):**
- JQL is a simple text-based search syntax. It is not code — it reads almost like English.
- Access it via: Filters > Advanced issue search > switch to JQL tab.
- Basic structure: `field = value AND field = value`

**Demo these four queries, one at a time:**

All open tickets assigned to you:
```
project = ERM AND assignee = currentUser() AND statusCategory != Done
```

All Stories currently In Progress:
```
project = ERM AND issuetype = Story AND status = "In Progress"
```

All open work under a specific Epic (replace ERM-001 with an actual Epic key):
```
project = ERM AND "Epic Link" = ERM-001 AND statusCategory != Done
```

Items with a due date in the next 14 days:
```
project = ERM AND due <= 14d AND statusCategory != Done
```

**Participant practice (4 min):**
Have each attendee write and run the first query (assigned to me, not done). Confirm results look right. If someone's query returns nothing or errors, debug live — it is almost always a spacing or quote issue.

**Saving a filter (3 min):**
- Run the query > click "Save as" > name it descriptively (e.g., "My Open ERM Stories")
- Share it: open saved filter > Details > set permissions to team or project
- Have each attendee save their query before moving on.

---

### 53:00–58:00 — Norms & Conventions (5 min)

**Objective:** Establish shared expectations before people go off and use the tool independently.

Deliver these as explicit team rules, not suggestions. Read from the list or display it — do not paraphrase loosely.

1. **Status currency:** You move your own tickets. Status reflects today's reality.
2. **Description and AC before In Progress:** If it's blank, fill it out before you start work.
3. **All Stories link to a Feature:** No orphaned Stories. If you can't find a parent, flag it.
4. **One assignee per Story:** If work is genuinely shared, split into separate Stories.
5. **No story points:** We use dates. Don't fill in the estimate field.
6. **Comments over DMs:** If you resolve something about a ticket in Slack or email, add a summary comment to the ticket.

Capture any contested norms or open questions in the shared doc and commit to resolving them before EOD.

---

### 58:00–60:00 — Wrap (2 min)

- Point to the Participant Guide — it has all field definitions, JQL queries, and norms in one place
- Point to the shared doc where unanswered questions are captured
- Name a single person (or channel) for follow-up questions — don't leave it ambiguous
- Hard stop at 60 minutes

---

## Common Failure Modes to Watch For

| Issue | Symptom | Response |
|---|---|---|
| Agile context contamination | Attendees ask about sprints, velocity, or points | Redirect clearly: "We don't use those. I'll explain what we use instead." |
| Hierarchy confusion | Items created at wrong level | Return to the time-range heuristic. Under 3 weeks = Story. |
| Generic link vs. parent | Items show as linked but don't appear in hierarchy views | Demo the Parent field specifically; explain why the generic Link button is different |
| Blank acceptance criteria | Attendees skip the AC field | Enforce the norm now, not later. Stop and have them fill it in. |
| JQL errors | Query returns nothing or throws an error | Usually missing quotes around multi-word values (e.g., `"In Progress"` not `In Progress`) |
| Orphaned Stories | Attendees forget to set parent | Check during hands-on block; prompt before they save |
| Plans date bars missing | Attendees open Plans and see blank bars | Missing Start Date or Target End Date on the ticket — use it as a live demonstration of why those fields are required |
| Plans edits on wrong tickets | Attendee drags someone else's bar accidentally | Reinforce the norm: Plans is read-only by default for other people's work; only edit your own |

---

## Post-Session Actions

- [ ] Share the Participant Guide link in team channel if not already distributed
- [ ] Post the agreed team norms in the designated reference location (Confluence, Notion, etc.)
- [ ] Resolve all questions captured in the shared doc within 24 hours
- [ ] Schedule a 30-minute check-in for 2 weeks out to capture friction points before they become habits
