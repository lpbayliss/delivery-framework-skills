# Fictional source context: Harbor recurring reservations

[← Back to showcase](README.md)

> Everything in this directory is fictional. Names, identifiers, dates, measurements, policies, and decisions exist only to demonstrate the skills. References such as `Linear HBR-124` and `Notion: Recurring Reservation Specification` are labels, not live records.

## Workspace

**Harbor** is a fictional web application used by community workshops to reserve shared rooms and equipment.

The Harbor delivery group uses:

- **Linear** for issues, execution status, owners, estimates, dependencies, backlog order, and concise decision summaries;
- **Notion** for specifications, design decisions, test/release/monitoring plans, reviews, and retrospectives;
- two-week cycles for planning and review, while urgent operational work can enter through an explicit interrupt path.

Local policy:

- one initiative Owner remains accountable end to end;
- backlog position is priority;
- a pulled-next item needs an owner, why, demonstrable acceptance, estimate, dependency treatment, and risk-proportionate test/release/observation thinking;
- Done means live, tested, observable, and recoverable;
- blocked work counts as WIP;
- cycle planning uses the ordered backlog and reserves capacity for operational/debt work according to a locally agreed allowance; this example does not prescribe a universal percentage.

## Fictional people and hats

| Person | Hat in this story |
|---|---|
| Maya Chen | Initiative Owner and product decision-maker |
| Noor Singh | Sponsor |
| Elena Park | Designer |
| Theo Brooks | Server engineer |
| Priya Nair | Web engineer |
| Jordan Lee | Quality engineer |
| Sam Okafor | Operational/release reviewer |
| Casey Morgan | Ceremony facilitator for the reset and review |

## Starting delivery-system evidence

On 2026-07-06 the team inspects the fictional canonical Linear board represented by this story:

- 14 issues are in a started status;
- five additional pieces of side work are being discussed or performed outside Linear;
- no single trusted backlog order exists;
- the team has not held refinement for six weeks;
- four started issues are blocked;
- three started issues have no current owner;
- two started issues have rolled over twice;
- no local WIP limit or expedite trade-off rule is written down.

The reset participants later make these explicit decisions:

- Casey facilitates and Maya scribes the reset.
- keep six started issues active;
- give each kept issue one owner and next action;
- pause five started issues and record revisit triggers;
- close three started issues because intent no longer exists;
- capture the five side-work items in Linear, merging two as duplicates, routing one operational alert through the interrupt path, and accepting the remaining two into normal intake;
- order the next eight candidate issues;
- adopt a WIP limit of six started issues for a two-week trial;
- book weekly refinement and twice-weekly flow reviews, both to be reviewed after two cycles.
- update the fictional canonical Linear records during the workshop, publish the fictional Notion decision record, and send the fictional cadence invitations; no live external tool is used by this repository example.
- Casey facilitates the first cycle of flow reviews; Maya coordinates the first refinement, after which both facilitation hats rotate.

## Incoming request

On 2026-07-07 Noor submits fictional Linear intake `HBR-117`:

> “Fix recurring reservations before the 12 September partner onboarding.”

Initial linked evidence:

- Between 2026-06-01 and 2026-06-30, support classified 24 requests as stale future reservations after an organiser edited a recurring series.
- A manual review of 40 affected series edits found nine that left at least one stale future occurrence.
- Seven of those nine required staff to cancel or move a conflicting reservation manually.
- The 12 September date comes from a scheduled onboarding of four partner workshops. Noor owns any decision to change that date; it is not automatically a delivery commitment.
- Search found related issue `HBR-88`, closed after correcting single-occurrence edits. It does not cover edits to the future portion of a recurring series.
- Maya confirms the triage disposition to accept `HBR-117` into Discovery; this is investigation approval, not a delivery commitment.

## Discovery decisions

Recorded in **Notion: Recurring Reservation Specification** on 2026-07-09:

- **Problem:** Editing the future portion of a recurring reservation series can leave stale future occurrences, creating conflicts and manual correction work.
- **Affected group:** workshop organisers who manage recurring room or equipment reservations, plus staff resolving conflicts.
- **Intended outcome:** organisers can change future dates, times, or reserved resources for a recurring series without stale future occurrences remaining.
- **Success observation:** during the first 14 complete days after full rollout, every tracked eligible future-series edit reconciles without a stale occurrence; the review must also report sample size and instrumentation gaps.
- **Health guardrails:** recurring-series edit API error rate stays below the existing 1% service objective and p95 latency stays below the existing 800 ms objective during each rollout stage.
- **Scope:** edits to dates, times, and reserved resources for future occurrences in an active recurring series; preserve historical occurrences and audit history.
- **Non-goals:** redesigning the calendar, changing single-occurrence exception behaviour, changing conflict policy, or importing external calendars.
- **Initiative Owner:** Maya Chen.
- **Sponsor:** Noor Singh.

## Refinement decisions

Recorded between 2026-07-10 and 2026-07-13:

- `HBR-121` timeboxed spike resolved the API contract and failure behaviour.
- Server, web, quality, and operational hats reviewed the design evidence on 2026-07-13 and recorded no unresolved implementation blocker.
- The chosen design stores a new series revision, generates the future occurrence set, validates conflicts, and swaps the future set in one transaction. Historical occurrences are not rewritten.
- The team considered mutating occurrences individually but rejected it because partial state and retries would be harder to control. It considered asynchronous eventual replacement but rejected it for this scope because the agreed contract requires no visible stale/partial future set after success.
- A feature flag controls use of the new edit path.
- The new path retains the existing authorization and conflict rules.
- Re-running the reconciliation operation with the same revision is idempotent.
- If validation or persistence fails, the existing future occurrence set remains active and the API returns a structured failure; partial replacement is not allowed.
- Rollout stages are 10% of eligible series for 24 hours, 50% for 24 hours, then 100%, provided success and health evidence pass at each stage.
- Maya owns each rollout-stage decision using Sam's operational evidence; this is a fictional local decision, not a universal gate-approval rule.
- Recovery is to disable the feature flag, leaving the previous edit path available. Any failed reconciliation is safe to retry after the issue is corrected.
- Jordan owns test-plan coordination; implementation and quality evidence remain whole-team responsibilities.

Planned work:

| Linear ID | Type | Summary | Owner | Estimate | Dependency | Planned horizon |
|---|---|---|---|---:|---|---|
| HBR-121 | Spike | Resolve recurring-series edit contract and failure behaviour | Theo | 3 | None | Done |
| HBR-124 | Deliverable | Update future recurring reservations without stale occurrences | Priya | 5 | HBR-121 | Pulled next |
| HBR-125 | Deliverable | Add reconciliation outcome dashboard and release alerts | Sam | 3 | HBR-121 | Pulled next |
| HBR-126 | Deliverable | Repair stale future occurrences found before rollout | Theo | 5 | HBR-124 | Near term |
| HBR-127 | Task | Document support verification and recovery steps | Jordan | 1 | HBR-124, HBR-125 | Near term |
| HBR-130 | Idea | Redesign recurring-reservation editor | Maya | Unestimated | None | Later |

At the first readiness audit:

- `HBR-124` has the complete specification, acceptance criteria, estimate, dependency, test plan, release plan, and observation plan.
- `HBR-125` identifies dashboard signals and alerts but has no named alert responder or runbook link.
- `HBR-126` combines automated repair, manual review tooling, and customer communication in one item; only automated repair is required before full rollout.
- `HBR-127` is near-term and appropriately lightweight.
- `HBR-130` has a durable title and one-line why; no further detail is justified yet.

## Delivery and observed results

The team later records these fictional facts:

- A kickoff on 2026-07-14 confirms the documented outcome, scope, design, test/release/monitoring expectations, and named delivery hats without changing the approved boundaries.
- `HBR-124`, `HBR-125`, and the automated-repair slice of `HBR-126` pass their tests.
- `HBR-127` support verification and recovery steps are completed before rollout.
- Sam becomes the alert responder and links the approved runbook before rollout.
- Rollout starts on 2026-08-10 and reaches 100% on 2026-08-12 after both staged gates pass.
- The feature flag remains available through the 14-day outcome review.
- During the first 14 complete days after full rollout, 186 eligible recurring-series edits are observed; zero leave a stale future occurrence.
- Edit API error rate is 0.3% and p95 latency is 620 ms over that review window.
- Support receives one question about finding the “future occurrences” control; it is usability feedback, not a stale-occurrence defect.
- No rollback occurs.

## Retrospective evidence

At the 2026-08-28 showcase/review, the team accepts the 14-day outcome evidence, creates a separate discoverability follow-up, retains the feature flag until a later control-removal decision, and closes the initiative outcome.

The review demonstrates the successful future-series edit, preserved history, the dashboard/alert response path, and the automated-repair result. Maya owns the control-removal decision after the 2026-09-12 partner onboarding and a review of post-onboarding health, using Sam's operational evidence.

At the retrospective on the same date, the team also finds:

- `HBR-124` waited 31 hours for its first substantive code review;
- two other cycle items waited more than one working day for first review;
- no review-request owner or visible review queue existed;
- no production defect is attributed to review delay.

The team agrees one two-cycle experiment: create a visible review-request queue, nominate a daily review coordinator, and review median request-to-first-substantive-review time after two cycles. No numeric target is invented before the baseline is measured.

Priya owns queue setup before the next cycle, Casey owns adding the two-cycle review to the retrospective agenda, and Maya owns keeping the experiment visible in the ordered Linear backlog.
