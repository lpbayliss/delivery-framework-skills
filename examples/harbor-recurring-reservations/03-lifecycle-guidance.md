# Skill execution: delivery-lifecycle-guidance

[← Back to showcase](README.md)

This file applies the lifecycle skill at four points to show forward movement, a conditional gate, and evidence-based closure. A gate result describes evidence; it does not invent organizational approval.

## Checkpoint A — after intake triage

### Current phase and confidence

**Discovery — high confidence.** The problem, Sponsor, Owner, and plausible evidence support investigation. The intended outcome, boundaries, and success observation are not yet agreed.

### Evidence

Present:

- named problem and affected group;
- June support/sample evidence;
- Sponsor Noor Singh and Owner Maya Chen;
- traceable source for the requested date;
- related-work check against `HBR-88`.

Missing:

- agreed outcome and scope/non-goals;
- success observation and health guardrails;
- a decision to elaborate a solution.

### Gate assessment

**Planning gate — `fail`.** Investigation is justified, but the evidence does not yet establish what outcome and rough scope are worth refining.

### Next decision and resolver

Maya, with Sponsor and required domain hats, must agree the outcome, scope boundary, and evidence needed to judge it.

### Next action / artefact

Create **Notion: Recurring Reservation Specification**. Do not write an implementation backlog yet.

### System updates

- **Linear:** keep `HBR-117` in Discovery with next decision and Notion link placeholder.
- **Notion:** hold the durable problem/evidence/outcome/scope decision.

## Checkpoint B — after discovery and technical spike

### Current phase and confidence

**Refinement, ready to return to Triage — high confidence.** The specification and `HBR-121` resolve the problem, outcome, boundaries, contract, failure behaviour, recovery, and intended ticket split.

### Evidence

- specification contains problem, affected group, outcome, success observation, scope, and non-goals;
- `HBR-121` resolves transaction and failure behaviour;
- design preserves history and prevents partial replacement;
- test, staged release, recovery, and monitoring decisions exist;
- intentional tickets `HBR-124` through `HBR-127` are drafted.

### Gate assessment

**Refining gate — `pass`.** Deliverers can assess and size the work without reopening the core why or contract.

### Next decision and resolver

Triage participants must size, test readiness, and place each ticket in one relative order. Maya owns the final backlog trade-off; delivery and quality hats own feasibility input.

### Next action / ceremony

Run focused refinement/triage using the ticket set and linked Notion artefacts.

### System updates

- **Linear:** create/link intentional issues, relations, owners, estimates, and concise decisions.
- **Notion:** retain canonical specification, design, test, release, and monitoring plans.

## Checkpoint C — after the first readiness audit

### Current phase and confidence

**Mixed: `HBR-124` can progress; `HBR-125` and `HBR-126` must remain in Refinement — high confidence.** One initiative can contain work at different readiness states.

### Gate assessment by item

| Item | Executing gate | Evidence-based decision |
|---|---|---|
| HBR-124 | `pass` | owner, outcome, acceptance, estimate, dependency, test/release/observation evidence are present |
| HBR-125 | `fail` | alert responder and runbook are unresolved, so production confidence is incomplete |
| HBR-126 | `conditional` | automated-repair outcome can be split and sized; manual tooling and communication remain separate decisions |
| HBR-127 | not assessed for pull | near-term lightweight task; dependency sequence is enough for its current horizon |
| HBR-130 | not assessed for pull | later idea is intentionally lightweight |

### Next decisions and resolvers

- Sam confirms the alert response owner and runbook for `HBR-125`.
- Maya and Theo split the rollout-critical automated repair from optional manual tooling/communication in `HBR-126`.

### Next move

- Pull `HBR-124` when capacity and final backlog order allow.
- Return `HBR-125` and `HBR-126` gaps to Refinement.
- Do not block `HBR-124` on unrelated later-detail work.

## Checkpoint D — after the 14-day full-rollout review

### Current phase and confidence

**Monitoring, ready for Analysing & Learning — high confidence.** The feature is live at 100%, tested, observable, and recoverable; the agreed outcome window is complete.

### Evidence

- the 10% and 50% advance gates passed, enabling 100% rollout;
- feature flag recovery remains available;
- 186 eligible edits observed over 14 complete days;
- zero stale future occurrences observed;
- API error rate 0.3% against existing objective below 1%;
- p95 latency 620 ms against existing objective below 800 ms;
- one usability question recorded; no stale-occurrence defect and no rollback.

### Gate assessment

**Analysing & Learning gate — `pass`.** The supplied evidence answers the intended outcome and health questions for the defined observation window.

### Next decision and resolver

Maya closes the initiative outcome review and decides follow-up disposition with the team:

- create a separate usability ticket for discoverability feedback;
- retain the feature flag until the planned control-removal decision;
- continue normal service monitoring;
- do not invent more scope for the closed outcome.

### System updates

- **Linear:** close delivered issues with evidence links; create the usability follow-up; record explicit no-action decisions.
- **Notion:** publish the outcome review and retrospective; link follow-up issues.

### Risks or contradictions

- The 14-day result supports this stated review, not a universal guarantee that stale occurrences can never recur.
- Removing the feature flag is a separate recovery-control decision, not implied by outcome success.
