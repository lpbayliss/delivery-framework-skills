# Skill execution: delivery-ticket-writing

[← Back to showcase](README.md)

The skill turns the approved outcome into one independently demonstrable deliverable and small execution tasks. Substantial context remains in Notion.

## Parent deliverable: HBR-124

### Ticket type and title

**Deliverable — Update future recurring reservations without stale occurrences**

### Linear properties

| Property | Value |
|---|---|
| Owner | Priya Nair |
| Team / project | Harbor delivery / not assigned in the supplied story |
| Cycle | Set when pulled; not inferred by this draft |
| Priority | Determined by backlog position |
| Estimate | 5 |
| Dependency | HBR-121 (Done) |
| Related | HBR-88 |
| Linked Notion | Recurring Reservation Specification; Design Decision; Test/Release/Monitoring Plan |

### Description

```markdown
## Outcome / why

Organisers can edit dates, times, or reserved resources for the future portion of an active recurring reservation series without stale future occurrences remaining. This removes a demonstrated source of booking conflicts and manual correction.

## Scope

- Create a new series revision for an eligible future-series edit.
- Generate and validate the replacement future-occurrence set.
- Swap the future set in one transaction while preserving historical occurrences and audit history.
- Return the agreed structured failure if validation or persistence fails.
- Route the new path through the approved feature flag.

## Acceptance criteria

1. Given an active recurring series with future occurrences, when an organiser changes a future date, time, or reserved resource and validation succeeds, then the future occurrence set matches the new series revision and no occurrence from the replaced future set remains active.
2. Historical occurrences and their audit history are unchanged by a future-series edit.
3. When the edit would create a conflict under the existing conflict policy, no partial replacement is visible and the API returns the agreed structured conflict response.
4. When persistence fails, the previous future occurrence set remains active and the API returns the agreed structured failure.
5. Repeating reconciliation for the same series revision does not create duplicate occurrences or a second visible state change.
6. When the feature flag is disabled, eligible edits use the previous path.
7. Reconciliation outcomes and failures emit the signals defined in the linked monitoring plan.

## Non-goals

- Redesigning the calendar or recurring-reservation editor.
- Changing single-occurrence exception behaviour.
- Changing conflict policy.
- Importing external calendars.
- Repairing stale occurrences created before this change; that is HBR-126.

## Context and decisions

June evidence found 24 classified support requests and stale results in 9 of 40 reviewed affected edits. The canonical specification defines the outcome and review window. HBR-121 records the transaction, idempotency, failure, and compatibility decisions.

## Dependencies / risks / unknowns

- HBR-121 must remain the canonical contract decision.
- HBR-125 must be ready before production rollout so failures are observable and actionable.
- Historical data preservation and concurrent edits are high-risk regression areas.
- Full rollout depends on the automated-repair slice of HBR-126. HBR-127 support steps remain linked near-term work, not a hard gate in this draft.

## Test approach

Use the linked plan. Cover successful edit types, preserved history, conflict rejection, persistence failure, concurrency, repeated reconciliation/idempotency, feature-flag paths, authorization, and existing single-occurrence behaviour.

## Release, recovery, and observation

Roll out to 10% of eligible series for 24 hours, then 50% for 24 hours, then 100%, only when the linked outcome and health gates pass. Disable the feature flag to recover. Observe stale-occurrence reconciliation, API errors, p95 latency, and alert/runbook readiness.
```

### Open questions

None remain for `HBR-124` at the documented readiness checkpoint. A cycle assignment is made only when the accountable team pulls it.

## Proposed child execution tasks

These are cheap draft sub-items, not claims that Linear created or numbered them. The labels below are illustrative local references; the parent holds the why and acceptance.

### HBR-124-A — Implement transactional future-set replacement

```markdown
## Action
Implement the approved series-revision generation, validation, and atomic future-set swap behind the feature flag.

## Completion evidence
Code review complete; focused automated tests pass for success, conflict, persistence failure, history preservation, and idempotency.

## Parent ticket
HBR-124

## Dependency / blocker
HBR-121 contract decision.
```

### HBR-124-B — Integrate the future-series edit client

```markdown
## Action
Use the approved API contract for eligible future-series edits and render its structured failure outcomes without changing single-occurrence behaviour.

## Completion evidence
Supported edit flow and failure states pass the linked acceptance/test cases in the representative environment.

## Parent ticket
HBR-124

## Dependency / blocker
HBR-124-A available in the test environment.
```

### HBR-124-C — Execute staged release verification

```markdown
## Action
Run the approved 10% and 50% release-stage checks and record evidence for the 100% decision.

## Completion evidence
Each stage decision records reconciliation outcome, API error rate, p95 latency, anomalies, decision owner, and rationale.

## Parent ticket
HBR-124

## Dependency / blocker
HBR-125 responder/runbook complete; automated-repair slice of HBR-126 available.
```

## Split rationale

Observability (`HBR-125`) and pre-existing-data repair (`HBR-126`) remain separate deliverables because they have independent completion evidence and risk. The three child tasks above do not duplicate parent context or become separately prioritized outcomes.
