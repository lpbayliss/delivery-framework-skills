# Skill execution: delivery-artifact-authoring

[← Back to showcase](README.md)

**Canonical destination:** fictional Notion pages linked from `HBR-117`, `HBR-124`, `HBR-125`, and `HBR-126`.

**Decision supported:** whether the recurring-reservation change is understood, testable, safe to release, observable, and ready for outcome review.

These are generic, replaceable drafts based on this repository's published artefact catalogue—not claimed approved workspace policy.

## 1. Specification

### Problem and affected people

Editing the future portion of an active recurring reservation series can leave stale future occurrences. Organisers can then encounter reservation conflicts, while staff manually cancel or move stale reservations.

Affected groups:

- workshop organisers managing recurring room/equipment reservations;
- staff resolving reservation conflicts.

### Evidence

| Evidence | Scope / limitation |
|---|---|
| 24 support requests classified in June | classification reflects one month, not lifetime incidence |
| 9 stale results in 40 reviewed affected edits | manual sample; report sample size with conclusions |
| 7 of the 9 required manual correction | shows observed correction work, not total organization cost |

### Intended outcome and success observation

Organisers can change future dates, times, or reserved resources without stale future occurrences remaining.

For the first 14 complete days after full rollout, assess the outcome:

- every tracked eligible future-series edit reconciles without a stale occurrence;
- report eligible edit count and instrumentation gaps;

At each rollout stage, assess the existing service-health guardrails:

- recurring-series edit API error rate remains below the existing 1% objective;
- p95 latency remains below the existing 800 ms objective.

### Scope

- future dates, times, and reserved resources in an active recurring series;
- preservation of historical occurrences and audit history;
- structured failure with no partial replacement.

### Non-goals

Calendar/editor redesign, single-occurrence behaviour, conflict-policy change, and external calendar import.

### Requirements and constraints

- history is immutable through a future-series edit;
- replacement is atomic from the user's perspective;
- repeated reconciliation of the same revision is idempotent;
- existing authorization and conflict rules remain authoritative;
- recovery remains available through the feature flag.

### Assumptions and risks

- Instrumentation can distinguish eligible edits and stale outcomes; verify before rollout.
- Proposed risk to confirm during review: concurrent edits and historical-data boundaries may require elevated regression coverage.
- The 12 September onboarding is planning context, not acceptance evidence.

### Unresolved decisions

None for the Planning gate. Control-removal timing remains a later release decision.

## 2. Design decision record

### Context

`HBR-121` evaluates how to update a future series without exposing partial results or rewriting history.

### Goals / non-goals

Goals: atomic visible replacement, preserved history, deterministic retries, structured failures, and flag-controlled recovery. UI redesign and conflict-policy changes remain outside the design.

### Chosen design

1. Store a new series revision for the requested future edit.
2. Generate the candidate future occurrence set.
3. Validate authorization, series state, and existing conflict rules.
4. In one transaction, activate the new revision and replace the active future set.
5. Leave historical occurrences unchanged.
6. Emit reconciliation outcome telemetry.

### Failure behaviour

- Validation/conflict failure: no persistent replacement; return structured response.
- Persistence failure: transaction rolls back; previous future set remains active.
- Duplicate retry of the same revision: no duplicate occurrence or second visible transition.
- Feature flag disabled: previous edit path remains in use.

### Alternatives considered

| Option | Decision | Trade-off |
|---|---|---|
| Mutate occurrences individually | Rejected | exposes partial-state and retry complexity |
| Asynchronous eventual replacement | Rejected for this scope | extends stale/conflicting visibility and requires different user contract |
| Transactional revision swap | Chosen | clearer atomic contract; requires transaction and concurrency testing |

### Review decisions

Server, web, quality, and operational hats reviewed the design evidence and recorded no unresolved implementation blocker. This does not invent a universal organizational approval rule.

## 3. Test plan

### Proposed quality risks for reviewer confirmation

Stale occurrences, partial replacement, rewritten history, duplicate retries, concurrent edits, authorization regression, single-occurrence regression, and invisible production failure.

### Acceptance mapping

| Acceptance area | Verification |
|---|---|
| successful date/time/resource edit | API + end-to-end tests verify exact active future set |
| preserved history | regression test compares historical IDs/data/audit history |
| conflict and persistence failures | injected failure tests verify previous set remains active |
| idempotency | repeat same revision and verify no duplicate/state transition |
| flag recovery | tests cover both new and previous path |
| telemetry | integration test verifies outcome/failure signals |

### Proposed environments and data

- representative recurring series with past and future occurrences;
- boundary dates, daylight-saving changes where supported, resource conflicts, and concurrent edit attempts;
- sanitized fixtures only; no production data copied into tests.

### Entry evidence

Approved specification/design, stable contract from `HBR-121`, feature flag available, and representative fixtures.

### Exit evidence

Acceptance and regression tests pass; no unresolved release-blocking defect; dashboard signals visible; responder/runbook confirmed; recovery path checked in a representative environment.

### Ownership

Jordan owns test-plan coordination; implementation and quality remain whole-team responsibilities.

## 4. Release plan

### Release unit and prerequisites

Release `HBR-124` with `HBR-125` and the automated-repair slice of `HBR-126`. Keep `HBR-127` linked as near-term support documentation rather than silently promoting it to a hard gate.

Prerequisites:

- test exit evidence recorded;
- dashboard, alerts, responder, and runbook ready;
- automated repair available for identified pre-existing stale data;
- feature-flag disable path verified;
- stage decision owners confirmed.

### Stages

| Stage | Duration | Advance evidence | Decision owner |
|---|---:|---|---|
| 10% eligible series | 24 hours | no stale tracked outcome; error <1%; p95 <800 ms; no unresolved release blocker | Maya with Sam's health evidence |
| 50% eligible series | 24 hours | same gates plus review of cumulative anomalies | Maya |
| 100% rollout | n/a — reached after 50% advance decision | prior stage accepted | Maya |

After full rollout, run the separate outcome review over 14 complete days; it is not a third rollout-advance gate.

### Proposed communication plan — confirm before rollout

- Before rollout: support and workshop operations receive scope, expected behaviour, and recovery contact.
- At each stage: concise state/evidence/decision posted to the Linear project.
- On pause/recovery: current impact and next update trigger communicated; do not promise recovery timing without evidence.

### Recovery

Disable the feature flag to return eligible edits to the previous path. Preserve evidence, inspect affected revisions, and retry failed reconciliation only after the cause is addressed. Full data reversal is not assumed or required by this design.

### Completion

Full rollout accepted, 14-day outcome review recorded, residual issues dispositioned, recovery-control removal decided separately, and execution records closed with Notion evidence links.

## 5. Monitoring and measurement plan

### Outcome signal

For each eligible future-series edit, compare intended active future set with the persisted active set and record whether a stale occurrence remains. Dashboard shows numerator, denominator, and instrumentation gaps.

### Service health

- recurring-series edit API error rate against existing objective below 1%;
- p95 latency against existing objective below 800 ms;
- reconciliation failure count by structured category;
- queue/backlog signal only if the chosen implementation creates one (it does not in this design).

### Alerts and response

At the first readiness audit, the responder and runbook are unresolved. `HBR-125` must name a responder and link the approved runbook before release. The later fictional execution record confirms Sam as responder. Alerts cover actionable reconciliation failures and health-objective breach according to the local monitoring system. This document does not invent product-specific alert syntax.

### Dashboard audience

Delivery, quality, operations, Owner, and Sponsor during staged rollout/outcome review; normal operational audience afterward.

### Review and follow-up

- inspect at every rollout gate;
- publish the 14-complete-day outcome review;
- create Linear defects/debt/usability work for confirmed follow-up, or record explicit no action;
- Monitoring validates and tunes signals after Development creates initial instrumentation.

## Linear linkage block

- `HBR-117`: initiative and current outcome decision summary.
- `HBR-124`: specification/design/test/release/monitoring links and execution status.
- `HBR-125`: dashboard/alert implementation, responder, and runbook.
- `HBR-126`: pre-existing data repair scope.
- `HBR-127`: linked near-term support verification and recovery documentation; not a hard release gate in this plan.

## Reviewers and next gate

Required hats: Owner, server, web, quality, operational/release, and Designer for user-facing failure behaviour. The combined evidence supports assessment at the **Refining** gate; issue-level readiness still requires Triage/Executing assessment.
