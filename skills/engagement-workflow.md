# Ferguson Insights — Typical Engagement Workflow

## Engagement Profile: Reporting Modernization for a Mid-Size RIA

**Client archetype:** $500M–$2B AUM RIA, 10–30 advisors, 2–4 custodian relationships, currently
running monthly reporting through Excel with manual data pulls. No dedicated analytics staff —
reporting is owned by an operations manager or a junior associate who inherited the spreadsheets.

**Typical scope:** Replace manual Excel-based reporting with automated Tableau/Power BI dashboards.
Usually 3–5 dashboards covering AUM overview, advisor performance, client retention, and
revenue/billing reconciliation.

**Typical duration:** 8–12 weeks
**Typical value:** $25K–$50K fixed fee

---

## Phase 1: Business Development (Weeks -2 to 0)

### Step 1.1 — Prospect Research

| | Without Agents | With Agents |
|---|---|---|
| **Task** | Manually search SEC IARD, LinkedIn, firm website, job boards | Load `prospect-researcher` agent with firm name |
| **What you do** | Open 6–8 browser tabs, copy/paste notes into a doc | Provide firm name and known details, review structured output |
| **Output** | Scattered notes | Structured brief: AUM, ADV flags, tech stack signals, likely pain points, conversation starters |
| **Time** | 60–90 min | 15–20 min |
| **Savings** | — | ~60 min |

**What the agent actually does:** Structures your research into a pre-call brief with sections
for firm overview, regulatory signals (any ADV amendments, disclosures), technology signals
(job postings mentioning specific tools, vendor relationships), likely pain points based on
firm size/structure, and suggested discovery questions. You still do the searching — the agent
organizes and interprets what you find.

### Step 1.2 — Discovery Call

| | Without Agents | With Agents |
|---|---|---|
| **Task** | Have the call, take notes | Have the call, take notes |
| **Time** | 45–60 min | 45–60 min |
| **Savings** | — | None — this is human work |

**No agent involved.** This is relationship building and problem diagnosis. No agent replaces
your ability to hear what the COO is actually worried about versus what they say they want.
The prospect-researcher output makes you better prepared, but the call itself is all you.

### Step 1.3 — Proposal & SOW

| | Without Agents | With Agents |
|---|---|---|
| **Task** | Draft proposal from scratch or from a template | Load `proposal-writer` agent, feed it discovery call notes |
| **What you do** | Write 3–5 page proposal, agonize over wording, second-guess pricing | Review and edit agent draft, focus on pricing strategy and scope precision |
| **Output** | Proposal + SOW | Same, but with tighter scope boundaries and explicit assumptions |
| **Time** | 3–4 hours | 45–75 min drafting + 30 min review |
| **Savings** | — | ~2 hours |

**Agent handoff:**
1. `proposal-writer` produces the pitch narrative and service description
2. `pricing-strategist` pressure-tests your proposed fee against hours, complexity, and market rates
3. `sow-drafter` produces the formal scope with deliverables, acceptance criteria, assumptions, exclusions, and change order terms

**Where the agent earns its keep:** The `sow-drafter` is adversarial about scope. When you type
"clean up their data," it asks: how many sources, what format, what's the definition of clean,
and who signs off? This prevents the scope creep that kills consulting margins.

### Phase 1 Total

| | Without Agents | With Agents | Savings |
|---|---|---|---|
| Prospect Research | 75 min | 20 min | 55 min |
| Discovery Call | 60 min | 60 min | 0 |
| Proposal + SOW | 3.5 hrs | 1.5 hrs | 2 hrs |
| **Phase Total** | **~5.5 hrs** | **~2.5 hrs** | **~3 hrs** |

---

## Phase 2: Data Discovery & Profiling (Weeks 1–2)

### Step 2.1 — Data Intake & Profiling

| | Without Agents | With Agents |
|---|---|---|
| **Task** | Client sends exports from Schwab, Fidelity, Orion. You explore manually in Python/SQL. | Load `data-profiler` agent, feed it each file |
| **What you do** | Write ad hoc pandas code, check shapes, nulls, types, eyeball distributions | Review structured profile output, focus on business-logic anomalies the agent can't catch |
| **Output** | Mental model of the data + scattered notebook cells | Standardized data profile per source: row counts, column inventory, null rates, type issues, cardinality, date ranges, join candidates, quality score |
| **Time** | 4–6 hours across sources | 1.5–2 hours |
| **Savings** | — | ~3.5 hours |

**What you still own:** The agent profiles structure, but you interpret meaning. It can tell you
there are 847 null values in `account_type`. It can't tell you that's because Schwab sends
institutional accounts without that field and the client's ops team has been manually filling
it in (sometimes). That insight comes from you asking the client the right question.

### Step 2.2 — Data Quality Assessment & Client Questions

| | Without Agents | With Agents |
|---|---|---|
| **Task** | Compile findings, write up data issues, draft questions for client | Load `analytics-reporter` (technical audience mode), feed it profiling results |
| **What you do** | Write a data quality memo manually | Review agent's structured assessment, add context from client conversations |
| **Output** | Data quality document with issues, questions, and risks to timeline | Same, but faster and more consistently structured |
| **Time** | 2–3 hours | 45–60 min |
| **Savings** | — | ~1.5 hours |

**Key agent behavior:** The `analytics-reporter` in technical mode flags issues that have
project risk implications: "4 custodian sources with different account ID formats suggest
a master mapping table is needed — this was not scoped. Recommend adding 8–12 hours for
entity resolution or flagging as a change order." That's the kind of structured thinking
you'd do eventually, but the agent surfaces it immediately.

### Phase 2 Total

| | Without Agents | With Agents | Savings |
|---|---|---|---|
| Data Profiling | 5 hrs | 1.75 hrs | 3.25 hrs |
| Quality Assessment | 2.5 hrs | 1 hr | 1.5 hrs |
| **Phase Total** | **~7.5 hrs** | **~2.75 hrs** | **~4.75 hrs** |

---

## Phase 3: Build (Weeks 3–8)

### Step 3.1 — SQL / Data Modeling

| | Without Agents | With Agents |
|---|---|---|
| **Task** | Write transformation queries: staging, cleaning, joining, aggregating | Load `sql-engineer` agent, describe the transformations needed |
| **What you do** | Write SQL from scratch, debug joins, handle edge cases | Describe business logic in plain English, review and refine generated SQL |
| **Output** | Production-ready SQL in Snowflake/Databricks | Same, with inline comments and validation checks built in |
| **Time** | 20–30 hours over the build phase | 10–15 hours |
| **Savings** | — | ~12 hours |

**Important nuance:** The savings here are concentrated in the routine work — staging tables,
standard aggregations, date spine generation, slowly changing dimensions. The hard SQL — the
query where you're trying to calculate advisor-level net flows with custodian transfers
excluded and fee-only accounts treated differently — that still takes the same amount of
your brain time. The agent writes the first draft faster, but you're debugging business
logic either way.

### Step 3.2 — Dashboard Specifications

| | Without Agents | With Agents |
|---|---|---|
| **Task** | Define every metric, dimension, filter, layout for each dashboard | Load `dashboard-spec-writer`, describe each dashboard's purpose |
| **What you do** | Write specs in a Word doc or Confluence, go back and forth with stakeholder | Review agent specs, validate metric definitions against client's language |
| **Output** | Dashboard specification document | Same, with calculation logic, grain definitions, and wireframes |
| **Time** | 8–12 hours across all dashboards | 3–5 hours |
| **Savings** | — | ~6 hours |

### Step 3.3 — Dashboard Build (Tableau/Power BI)

| | Without Agents | With Agents |
|---|---|---|
| **Task** | Build dashboards in the BI tool | Build dashboards in the BI tool |
| **Time** | 15–25 hours | 15–25 hours |
| **Savings** | — | Minimal — this is hands-on tool work |

**No meaningful agent involvement.** Agents can't click around Tableau for you. The
dashboard-spec-writer saved time upstream by making the build phase more efficient (fewer
"wait, what does this metric mean?" interruptions), but the actual build time is roughly
the same. If you're using Tableau's API or writing calculated fields, the `sql-engineer`
agent can help with LOD expressions or complex calcs, saving maybe 1–2 hours.

### Step 3.4 — Code Review & Documentation

| | Without Agents | With Agents |
|---|---|---|
| **Task** | Review your own SQL/Python, write handoff docs | Load `code-reviewer` then `documentation-writer` |
| **What you do** | Self-review (poorly, because you wrote it), write docs from memory | Agent reviews code for issues you're blind to; agent drafts docs from code + specs |
| **Output** | Reviewed code + technical documentation | Same, but docs are structured for the client's team, not for you |
| **Time** | 6–8 hours | 2.5–4 hours |
| **Savings** | — | ~4 hours |

**Where this really matters:** The `documentation-writer` produces docs written for the person
who inherits your work in 6 months — not for you. This is the deliverable that gets you
rehired. Most consultants skip or rush documentation because it's boring. The agent makes
it fast enough that you actually do it.

### Phase 3 Total

| | Without Agents | With Agents | Savings |
|---|---|---|---|
| SQL / Data Modeling | 25 hrs | 12.5 hrs | 12.5 hrs |
| Dashboard Specs | 10 hrs | 4 hrs | 6 hrs |
| Dashboard Build | 20 hrs | 19 hrs | 1 hr |
| Code Review & Docs | 7 hrs | 3 hrs | 4 hrs |
| **Phase Total** | **~62 hrs** | **~38.5 hrs** | **~23.5 hrs** |

---

## Phase 4: Delivery & Presentation (Weeks 9–10)

### Step 4.1 — Executive Summary & Findings Report

| | Without Agents | With Agents |
|---|---|---|
| **Task** | Write the final deliverable report summarizing what was built, key findings, and recommendations | Chain: `analytics-reporter` → `executive-translator` |
| **What you do** | Stare at a blank doc, try to remember what the COO cares about, write and rewrite | Feed the analytics-reporter your data/findings, then run the output through executive-translator for the COO version |
| **Output** | Executive summary + detailed findings | Two versions: executive (2–3 pages) and technical appendix |
| **Time** | 4–6 hours | 1.5–2 hours |
| **Savings** | — | ~3.5 hours |

**The chain in action:**
1. `analytics-reporter` takes your query results and raw findings → produces structured analysis with metrics in context (not naked numbers)
2. `executive-translator` takes that output → rewrites for the COO: leads with business impact, frames findings as decisions, drops methodology into an appendix

This is where the agents produce the most visible quality improvement. The COO doesn't see
your SQL or your Tableau workbook. They see this report. Making it sharp, concise, and
decision-oriented is what separates a $200/hr consultant from a $300/hr one.

### Step 4.2 — Client Presentation

| | Without Agents | With Agents |
|---|---|---|
| **Task** | Present findings, demo dashboards, handle questions | Same |
| **Time** | 60–90 min + 30 min prep | 60–90 min + 15 min prep |
| **Savings** | — | ~15 min (better prep materials reduce prep time) |

### Step 4.3 — Handoff Documentation

| | Without Agents | With Agents |
|---|---|---|
| **Task** | Final handoff: runbooks, data dictionary, maintenance guide | `documentation-writer` produces from existing specs and code |
| **Time** | 4–6 hours | 1.5–2 hours |
| **Savings** | — | ~3 hours |

### Phase 4 Total

| | Without Agents | With Agents | Savings |
|---|---|---|---|
| Executive Report | 5 hrs | 1.75 hrs | 3.25 hrs |
| Presentation | 1.5 hrs | 1.25 hrs | 0.25 hrs |
| Handoff Docs | 5 hrs | 1.75 hrs | 3.25 hrs |
| **Phase Total** | **~11.5 hrs** | **~4.75 hrs** | **~6.75 hrs** |

---

## Phase 5: Post-Engagement (Ongoing)

### Step 5.1 — Case Study

| | Without Agents | With Agents |
|---|---|---|
| **Task** | Write up the engagement as a case study for your website/proposals | Load `case-study-builder`, feed it the SOW, report, and outcomes |
| **Time** | 2–3 hours (or never, because you "don't have time") | 30–45 min |
| **Savings** | — | ~2 hours |

### Step 5.2 — LinkedIn Post

| | Without Agents | With Agents |
|---|---|---|
| **Task** | Write a thought leadership post based on what you learned | Load `linkedin-writer` with the anonymized scenario |
| **Time** | 45 min (or never) | 15 min |
| **Savings** | — | ~30 min |

### Step 5.3 — Invoice & Time Reconciliation

| | Without Agents | With Agents |
|---|---|---|
| **Task** | Reconcile hours, draft final invoice, check against SOW budget | Load `invoice-tracker` with time entries and SOW terms |
| **Time** | 30–45 min | 10–15 min |
| **Savings** | — | ~25 min |

### Phase 5 Total

| | Without Agents | With Agents | Savings |
|---|---|---|---|
| Case Study | 2.5 hrs | 0.6 hrs | 1.9 hrs |
| LinkedIn | 0.75 hrs | 0.25 hrs | 0.5 hrs |
| Invoice | 0.6 hrs | 0.2 hrs | 0.4 hrs |
| **Phase Total** | **~3.85 hrs** | **~1.05 hrs** | **~2.8 hrs** |

---

## Full Engagement Summary

| Phase | Without Agents | With Agents | Time Saved | % Reduction |
|-------|---------------|-------------|------------|-------------|
| 1. Business Development | 5.5 hrs | 2.5 hrs | 3.0 hrs | 55% |
| 2. Data Discovery | 7.5 hrs | 2.75 hrs | 4.75 hrs | 63% |
| 3. Build | 62.0 hrs | 38.5 hrs | 23.5 hrs | 38% |
| 4. Delivery | 11.5 hrs | 4.75 hrs | 6.75 hrs | 59% |
| 5. Post-Engagement | 3.85 hrs | 1.05 hrs | 2.8 hrs | 73% |
| **Total** | **90.35 hrs** | **49.55 hrs** | **40.8 hrs** | **45%** |

---

## What This Means Financially

### Scenario A: Same clients, more margin
- Engagement priced at $35,000 fixed fee
- Without agents: 90 hours → effective rate of $389/hr
- With agents: 50 hours → effective rate of $700/hr

### Scenario B: More clients, same hours
- With 90 hours freed up, you could run nearly 2 engagements in the time 1 used to take
- Annual capacity goes from ~5–6 engagements to ~9–10
- Revenue potential: $175K–$210K → $315K–$350K (solo, no subcontractors)

### Scenario C: Same output, better life
- Work 50 hours per engagement instead of 90
- Use the freed time for business development, Georgia Tech coursework, or not working
- This is the underrated option — burnout kills solo consultants faster than bad pricing

---

## Honest Caveats

**The 45% reduction is a ceiling, not a floor.** In your first 2–3 engagements, expect more
like 20–25% savings as you refine the agents and learn what prompts produce usable output
versus what needs heavy editing.

**The Build phase savings are the most variable.** If the client's data is clean and
well-structured (rare), you'll save more. If it's a disaster of inconsistent CSVs and
undocumented business logic, the agents help less because the bottleneck is understanding,
not execution.

**You need to actually build the agents first.** Budget 15–20 hours upfront to build and
test the 5–6 core agents. Then expect to iterate after each engagement. By engagement 3–4,
the agents are well-calibrated to your actual workflow.

**The biggest risk:** Spending 40 hours perfecting agent files for a business that has zero
clients yet. Build the minimum viable agents, land the first client, then refine based on
real work.
