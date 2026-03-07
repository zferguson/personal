# Ferguson Insights — Claude Code Agent Library

## Directory Structure

```
.claude/agents/
├── business-development/
│   ├── proposal-writer.md
│   ├── prospect-researcher.md
│   └── pricing-strategist.md
├── client-delivery/
│   ├── analytics-reporter.md
│   ├── dashboard-spec-writer.md
│   ├── data-profiler.md
│   ├── sql-engineer.md
│   └── executive-translator.md
├── internal-operations/
│   ├── sow-drafter.md
│   ├── invoice-tracker.md
│   └── time-estimator.md
├── thought-leadership/
│   ├── linkedin-writer.md
│   └── case-study-builder.md
└── technical/
    ├── code-reviewer.md
    ├── etl-architect.md
    └── documentation-writer.md
```

---

## Business Development (Finding & Winning Work)

### proposal-writer.md
**Purpose:** Draft consulting proposals and pitch decks for RIAs, broker-dealers,
insurance firms, and fintechs.
**Why it matters:** Proposals are where deals are won or lost. This agent should
know your service lines (reporting modernization, executive dashboards, fractional
analytics leadership, data strategy) and tailor language to financial services buyers
who care about compliance, auditability, and ROI — not technical jargon.
**Key behaviors:** Mirror the prospect's language from discovery calls, quantify
expected outcomes, include relevant case studies, produce clean scope/timeline/pricing
sections, and flag scope creep risks before the client signs.

### prospect-researcher.md
**Purpose:** Research potential clients before outreach or discovery calls.
**Why it matters:** Walking into a call with an RIA knowing their AUM, tech stack
(from ADV filings or job postings), and recent regulatory actions is a competitive
advantage over generalist consultants.
**Key behaviors:** Pull from SEC EDGAR/IARD, firm websites, LinkedIn, press releases.
Summarize: firm size, likely pain points, tech maturity signals, and conversation
starters. Flag if they've recently hired or lost analytics staff (opportunity signal).

### pricing-strategist.md
**Purpose:** Help estimate project pricing, evaluate hourly vs. fixed vs. retainer
models, and pressure-test margins.
**Why it matters:** Underpricing is the #1 way solo consultants bleed money. This
agent should challenge your instinct to "just charge $150/hr" and model out what
the engagement actually costs you in time, opportunity cost, and deliverable risk.
**Key behaviors:** Estimate hours by deliverable, apply contingency multipliers for
ambiguous scope, compare against market rates for financial services analytics
consulting, and flag when a project should be value-priced instead of time-priced.

---

## Client Delivery (Doing the Work)

### analytics-reporter.md
**Purpose:** Transform raw data into structured, insight-driven reports for technical
and executive audiences.
**Why it matters:** This is the core deliverable for most engagements. See the
detailed version already built out.

### dashboard-spec-writer.md
**Purpose:** Produce detailed dashboard specifications that a BI developer (or you)
can build from.
**Why it matters:** Clients ask for "a dashboard" but mean wildly different things.
This agent forces clarity: metric definitions, calculation logic, dimensions, filters,
refresh cadence, alert thresholds, and wireframe layouts — before anyone touches
Tableau or Power BI.
**Key behaviors:** Require a business question per dashboard section, define every
metric with both plain-English and technical definitions, specify grain, call out
where source data doesn't support the requested view.

### data-profiler.md
**Purpose:** Profile unfamiliar datasets quickly — structure, quality, distributions,
anomalies, join candidates.
**Why it matters:** Every new client engagement starts with "here's our data." The
first 2-4 hours of profiling determine whether your project estimate was right or
you're about to eat scope. This agent should be ruthlessly systematic.
**Key behaviors:** Row counts, column types, null rates, cardinality, min/max/mean
for numerics, value frequency for categoricals, date range/gaps, duplicate detection.
Output a structured assessment with a data quality score and a list of questions
for the client.

### sql-engineer.md
**Purpose:** Write, optimize, and debug SQL for Snowflake, Databricks, and
standard ANSI SQL.
**Why it matters:** You'll write SQL daily. This agent should produce clean,
commented, CTE-based queries and catch common mistakes: join fanouts, incorrect
window function framing, timezone mishandling, and implicit type coercion.
**Key behaviors:** Always use CTEs over nested subqueries, comment business logic,
validate row counts at each join, handle NULLs explicitly, and prefer deterministic
results (no ORDER BY without tiebreakers).

### executive-translator.md
**Purpose:** Translate technical findings into language that C-suite and
non-technical stakeholders act on.
**Why it matters:** The gap between "what the data shows" and "what the CFO hears"
is where consultants either build trust or lose credibility. This agent bridges
that gap without dumbing things down.
**Key behaviors:** Lead with business impact, not methodology. Use analogies from
financial services (risk, exposure, yield). Frame findings as decisions to be made,
not facts to absorb. Flag when a finding needs caveating vs. when caveats will
undermine the message.

---

## Internal Operations (Running the Business)

### sow-drafter.md
**Purpose:** Draft Statements of Work with clear scope, deliverables, timelines,
assumptions, acceptance criteria, and change order provisions.
**Why it matters:** Vague SOWs are how consultants end up doing 3x the work for 1x
the price. This agent should be adversarial about scope — if a deliverable is
ambiguous, it forces clarification before the SOW is finalized.
**Key behaviors:** Every deliverable gets: description, format, acceptance criteria,
and estimated hours. Assumptions section must include data access, client
responsiveness SLAs, and out-of-scope items. Include a change order clause template.

### invoice-tracker.md
**Purpose:** Track hours, generate invoice drafts, and flag overdue payments or
budget burn rates.
**Why it matters:** Solo consultants lose money through underbilling and late
invoicing more than through any other operational failure.
**Key behaviors:** Summarize hours by project/client, compare actuals to SOW
estimates, flag when a project is approaching budget ceiling, draft professional
invoice line items, and remind you of outstanding receivables.

### time-estimator.md
**Purpose:** Estimate level of effort for new projects and individual deliverables.
**Why it matters:** Estimation accuracy directly determines profitability. This
agent should use historical patterns and force you to decompose vague tasks into
concrete steps before estimating.
**Key behaviors:** Break deliverables into subtasks, apply complexity multipliers
(new client data = 1.5x, regulated environment = 1.3x, ambiguous requirements =
2x), present optimistic/realistic/pessimistic ranges, and track estimate vs. actual
over time to calibrate.

---

## Thought Leadership (Building the Brand)

### linkedin-writer.md
**Purpose:** Draft LinkedIn posts that demonstrate analytics expertise and attract
inbound leads from financial services professionals.
**Why it matters:** LinkedIn is the primary channel for B2B consulting lead gen in
financial services. But most consultant posts are either too generic ("data is
important!") or too technical for the buyer audience.
**Key behaviors:** Write in your voice (direct, practical, no buzzword fluff). Each
post should have one clear insight, grounded in a real scenario (anonymized). Use
the hook-insight-implication structure. No hashtag spam. Aim for posts that a
compliance officer or COO at a mid-size RIA would find useful enough to share.

### case-study-builder.md
**Purpose:** Turn completed engagements into structured case studies for the
website and proposals.
**Why it matters:** Case studies are the highest-converting sales asset for
consulting. But writing them after the fact is painful, so they never get done.
This agent should make it fast.
**Key behaviors:** Follow the Situation-Problem-Approach-Result (SPAR) framework.
Quantify outcomes. Anonymize appropriately. Produce two versions: a 1-pager for
proposals and a longer website version. Flag when you're missing outcome data and
need to follow up with the client.

---

## Technical (Code & Infrastructure Quality)

### code-reviewer.md
**Purpose:** Review Python and SQL code for correctness, readability, and
maintainability before delivering to clients.
**Why it matters:** Client-facing code reflects on your professionalism. A sloppy
notebook or uncommented script undermines the "expert consultant" positioning.
**Key behaviors:** Check for: PEP 8/257 compliance, hardcoded values that should be
configs, missing error handling, undocumented assumptions, security issues (exposed
credentials, SQL injection in parameterized queries), and reproducibility (pinned
dependencies, seed values).

### etl-architect.md
**Purpose:** Design data pipelines, transformation logic, and data flow
architectures for client environments.
**Why it matters:** Several of your service lines (reporting modernization, data
strategy) involve designing how data moves and transforms. This agent should think
in terms of sources, staging, transformation, and serving layers.
**Key behaviors:** Produce data flow diagrams (in mermaid or ASCII), define
transformation rules with business logic documentation, specify idempotency and
error handling requirements, and flag vendor lock-in risks. Optimize for
maintainability over cleverness — the client's team has to live with this after
you leave.

### documentation-writer.md
**Purpose:** Produce technical documentation, data dictionaries, and runbooks
for client handoff.
**Why it matters:** The deliverable that separates a $150/hr contractor from a
$300/hr consultant is documentation. If the client can maintain and extend your
work after you leave, they'll hire you again. If they can't, they resent the
dependency.
**Key behaviors:** Write for the person who inherits this in 6 months with no
context. Include: purpose, architecture overview, setup/dependencies, configuration,
common tasks, troubleshooting, and known limitations. Use the "README, then deep
docs" pattern.

---

## What I Deliberately Left Out

- **Social media agents beyond LinkedIn** — TikTok/Instagram/Twitter are not where
  your B2B financial services buyers discover consultants. Don't split focus.
- **Generic "AI assistant" or "chatbot" agents** — too vague to be useful.
- **Separate agents per platform (Snowflake agent, Tableau agent, etc.)** — platform
  context belongs in the sql-engineer or dashboard-spec-writer prompts as conditional
  instructions, not as standalone agents.
- **"Strategy" agents** — strategy is thinking, not a prompt. An agent that says
  "think strategically" adds nothing. The prospect-researcher and pricing-strategist
  cover the parts of strategy that benefit from structured prompts.
