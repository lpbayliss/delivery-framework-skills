# Skill execution: delivery-ceremony-facilitation

[← Back to showcase](README.md)

This showcase runs the skill for three ceremony moments. Kickoff includes its retained **pre-session facilitation pack** and a concise completed fictional record. Review and retrospective are shown as **completed fictional records** because their observations and decisions are supplied in [00-source-context.md](00-source-context.md).

## 1. Kickoff — HBR-124

The following is the retained pre-session facilitation pack prepared before the fictional 2026-07-14 kickoff.

### Outcome and decisions

Outcome: confirm shared intent, boundaries, roles, quality/release expectations, and unresolved decisions before material implementation.

Decisions needed:

1. Does every delivery hat interpret the outcome and non-goals consistently?
2. Are HBR-121's transaction/failure decisions sufficient to begin?
3. Are test, staged-release, observability, and recovery responsibilities understood?
4. What must be resolved before production rollout versus before implementation?

### Attendees by role

- Facilitator: Casey Morgan.
- Initiative Owner: Maya Chen.
- Delivery: Priya Nair and Theo Brooks.
- Quality: Jordan Lee.
- Operational/release: Sam Okafor.
- Design: Elena Park for user-visible failures.
- Sponsor Noor Singh: optional for intent/date questions; not required for implementation detail.

### Preparation

- Open `HBR-124`, dependency `HBR-121`, and `HBR-125`–`HBR-127`.
- Open the specification, design decision, test, release, and monitoring plans.
- Verify `HBR-124` acceptance/non-goals against canonical Notion decisions.
- Mark the alert responder/runbook and `HBR-126` split as rollout-readiness items.
- Do not create slides; facilitate from Linear and linked evidence.

### Timed agenda — 30 minutes

| Time | Flow | Facilitator prompt | Output |
|---:|---|---|---|
| 0–5m | Intent and evidence | “What outcome are we changing, and what would disprove success?” | shared outcome and measures |
| 5–10m | Scope/non-goals | “Which tempting adjacent changes are explicitly outside HBR-124?” | boundary confirmation |
| 10–18m | Design/failure walkthrough | “What remains active after each failure? What is retry behaviour?” | shared transaction/failure model |
| 18–24m | Quality/release/monitoring | “What evidence blocks implementation, pull, rollout, or stage advance?” | gate-specific responsibilities |
| 24–28m | Dependencies/owners | “Who resolves HBR-125 and HBR-126 readiness?” | named actions |
| 28–30m | Read-back | “What did we decide and where will it live?” | confirmed decisions/parking lot |

### Live-capture structure

| Observation / decision / action | Evidence/rationale | One owner | Review trigger | Record |
|---|---|---|---|---|
| `[capture live]` | `[source]` | `[name]` | `[trigger]` | Linear execution or Notion durable context |

Do not fabricate post-session minutes if this session has not occurred.

### Completed fictional kickoff record — 2026-07-14

- The group confirmed the documented outcome, scope, non-goals, design, test/release/monitoring expectations, and named delivery hats.
- No approved boundary changed.
- `HBR-125` responder/runbook ownership and the `HBR-126` split remained rollout/readiness actions, not hidden implementation assumptions.
- Linear retained the execution actions; Notion retained the durable design and planning evidence. These are story records only—no live tool mutation is claimed.

## 2. Showcase and review — completed fictional record

**Date:** 2026-08-28

**Facilitator:** Casey Morgan

**Goal:** inspect the recurring-reservation outcome, account for planned work, and adapt follow-up.

### Demonstrated evidence

| Item/evidence | Observation |
|---|---|
| HBR-124 | demonstrated editing future dates/resources with preserved history and no stale occurrence |
| HBR-125 | dashboard and actionable alert/runbook shown; Sam confirmed as responder |
| HBR-126 automated repair | rollout-required slice complete; optional manual tooling/communication excluded |
| 14-day outcome window | 186 eligible edits; zero stale future occurrences |
| Service health | error 0.3% against <1%; p95 620 ms against <800 ms |
| Support evidence | one discoverability question; no stale-occurrence defect |
| Recovery | feature flag remained available; no rollback invoked |

### Commitment accounting

- `HBR-124`, `HBR-125`, and automated-repair slice: finished and demonstrated.
- Optional `HBR-126` manual tooling/communication: not presented as committed scope.
- `HBR-127`: support verification/recovery steps completed before rollout; the example does not treat this lightweight task as an independent release gate.

### Decisions

| Decision | Rationale | Owner | Follow-up |
|---|---|---|---|
| Accept the 14-day outcome review | supplied outcome and health evidence pass the defined window | Maya | publish Notion outcome review |
| Create a separate discoverability ticket | support question is valid feedback but not a stale-occurrence defect | Maya | order through normal triage |
| Keep feature flag until explicit control-removal review | success does not itself prove recovery control is no longer needed | Maya | decide after 2026-09-12 onboarding and post-onboarding health review using Sam's evidence |
| Close initiative outcome | intended question is answered for the agreed window | Maya | link evidence and explicit follow-ups |

### Linear / Notion updates

- **Linear:** close delivered issues with evidence; create/link discoverability follow-up; record flag-removal decision trigger.
- **Notion:** retain review evidence, decisions/rationale, and links to canonical issues.

### Parked questions

- Longer-term incidence is normal monitoring, not a reason to keep the initiative indefinitely open.
- Calendar editor redesign remains `HBR-130`, ordered separately.

## 3. Retrospective — completed fictional record

**Date:** 2026-08-28

**Outcome:** improve review flow without blaming individuals or conflating it with product feedback.

### Facts

- `HBR-124` waited 31 hours for first substantive review.
- Two other cycle issues waited more than one working day.
- There was no visible review queue or review-request owner.
- No production defect was attributed to the delay.

Interpretation such as “reviewers were careless” was rejected because the evidence does not support personal causation.

### Pattern and hypothesis

Observed pattern: review requests waited without a visible queue or coordination ownership.

Working-system hypothesis: making the queue and daily coordination responsibility explicit may reduce waiting without requiring a permanent specialist reviewer.

### Experiment decision

| Field | Decision |
|---|---|
| Small reversible change | create a visible review-request queue and nominate a rotating daily review coordinator |
| Owner | Priya Nair owns setup; coordinator rotates daily |
| Baseline | measure current request-to-first-substantive-review time from available workflow data |
| Success signal | compare median wait after two cycles; no target invented before baseline |
| Guardrail | inspect defect/rework observations so speed is not optimized alone |
| Review trigger | after two complete cycles |
| Linear work | create one experiment issue linked to this retrospective |

### Actions

- Priya creates the queue and documents the request signal before the next cycle.
- Casey adds the experiment review to the retrospective agenda two cycles later.
- Maya ensures the experiment issue remains ordered and does not become invisible process side work.

### System records

- **Linear:** executable experiment, owner, review trigger, and current status.
- **Notion:** facts, hypothesis, decision rationale, experiment design, and later review result.

### Parking lot

- The discoverability question goes through product triage, not the retrospective.
- Broader engineering staffing is not inferred from three wait observations.
