# Jira Training — Participant Task List
## Enterprise Risk Management | Hands-On Practice

Complete these tasks during the session. All work should be done in the ERM project sandbox unless the facilitator directs otherwise.

---

## Block 1 — Creating & Linking Work Items
*Session time: 15:00 – 35:00*

1. **Create a Story** using a real or realistic piece of your own work. Fill in every required field before saving:
   - Title (action-oriented — who does what)
   - Description (context and any relevant references)
   - Acceptance Criteria (specific, verifiable conditions — use a numbered list)
   - Assignee (yourself)
   - Reporter (your stakeholder or manager)
   - Priority
   - Start Date and Target End Date

2. **Create a Feature** that your Story logically belongs to. Give it a title that names the deliverable, not the activity.

3. **Link your Story to your Feature** using the Parent field (not the generic Link button).

4. **Link your Feature to an existing Epic** — use one the facilitator has pre-created, or create your own.

5. **Verify the hierarchy** by opening your Epic and confirming your Feature appears under it, and your Story appears under the Feature.

6. **Find a Story created by a teammate** using the search bar or board view. Confirm you can see their fields.

---

## Block 2 — Navigation, Views & Plans
*Session time: 35:00 – 43:00*

7. **Find your Story in Board view.** Confirm it appears in the correct status column.

8. **Find the same Story in List view.** Sort the list by Start Date.

9. **Move your Story through two status transitions:**
   - To Do → In Progress
   - In Progress → In Review

10. **Flag your Story as blocked:** use the flag icon in Jira Cloud and add a comment explaining a hypothetical blocker. Then unflag it.

11. **Open Plans** from the left sidebar. Use the Hierarchy toggle to view Epics only, then expand to show Features and Stories beneath them.

12. **Apply Colour by Assignee** using the Colour by control. Identify which team members have work plotted on the current timeline.

13. **Change the zoom level** to Quarters. Confirm you can see the full date range of at least one Epic's bar.

14. **Do not drag or reschedule any items in Plans.** Observe only — Plans writes changes directly to live tickets with no confirmation step.

---

## Block 3 — JQL & Filters
*Session time: 43:00 – 53:00*

15. **Navigate to Advanced Issue Search** (Filters > Advanced issue search) and switch to the JQL editor.

16. **Write and run this query** — confirm it returns your open tickets:
    ```
    project = ERM AND assignee = currentUser() AND statusCategory != Done
    ```

17. **Write and run a second query** that filters by a specific status:
    ```
    project = ERM AND issuetype = Story AND status = "In Progress"
    ```

18. **Save your first query as a named filter.** Use a descriptive name such as "My Open ERM Stories."

19. **Share your saved filter** with at least one teammate by setting permissions in the filter's Details panel.

---

## Completion Check

Before the session ends, confirm you can answer yes to each of the following:

- [ ] I can create a Story with all required fields filled out
- [ ] I can link a Story to a Feature and a Feature to an Epic using the Parent field
- [ ] I can find my work in Board view, List view, and Plans
- [ ] I know how to move a ticket between statuses
- [ ] I understand that Plans edits write back to live tickets immediately
- [ ] I can write a basic JQL query and save it as a filter
- [ ] I know where the team norms reference document lives

---

*Reference the Participant Guide for field definitions, JQL examples, and team norms.*
