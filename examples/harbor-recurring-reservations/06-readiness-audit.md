# Skill execution: delivery-readiness-audit

[← Back to showcase](README.md)

**Scope:** active recurring-reservation initiative, pulled-next candidates, near-term tasks, and one later idea.

**Audit point:** before cycle selection.

## Scope and assumptions

- Backlog order and fictional issue records are available from the story source.
- `HBR-121` is Done and treated as dependency evidence, not current WIP.
- The audit tests each item at its current horizon; later work is not scored against pulled-next standards.
- No universal age or staleness threshold is introduced.

## Executive finding

The initiative is **partly ready but not yet trustworthy as one release set**. `HBR-124` can be pulled when capacity/order allow. `HBR-125` lacks actionable alert ownership. `HBR-126` mixes three outcomes and must be split before the rollout-critical repair slice can be assessed. `HBR-127` and `HBR-130` are appropriately lightweight for their positions.

## Issue findings

| Issue | Horizon | Finding | Evidence | Required action | Owner / decision |
|---|---|---|---|---|---|
| HBR-124 | Pulled next | Ready for pull | owner, why, observable acceptance, estimate 5, HBR-121 done, linked test/release/monitoring evidence | preserve order; assign cycle only when pulled | Maya orders; Priya delivers |
| HBR-125 | Pulled next | Must fix before pull/release | dashboard signals exist, but no responder or runbook link | name responder, link runbook, verify alert actionability | Sam resolves; Maya accepts release dependency |
| HBR-126 | Near term / release dependency | Return for split/refinement | combines automated repair, manual-review tooling, and communication | split automated repair as independent deliverable; route optional outcomes separately | Maya + Theo |
| HBR-127 | Near term | Leave lightweight | owner, action, estimate 1, and dependencies are sufficient for current position | add detailed verification only as it moves to pull | Jordan |
| HBR-130 | Later | Leave alone | durable title and one-line why; no approved near-term intent | no design, estimate, or acceptance work yet | Maya revisits if order changes |

## Refinement shortlist — 35 minutes

| Time | Item | Decision required | Expected output |
|---:|---|---|---|
| 0–10m | HBR-125 | Who responds and where is the approved response path? | Sam named; runbook linked; alert check recorded |
| 10–25m | HBR-126 | What is required for release versus optional follow-up? | automated-repair ticket with independent acceptance; other outcomes split/routed |
| 25–30m | HBR-124 dependency check | Is the release set coherent after the fixes? | dependencies/relations confirmed; no reopened scope |
| 30–35m | Read-back | Which items are eligible for next pull and who owns remaining decisions? | explicit disposition and Linear updates |

Do not use session time on `HBR-130` unless its backlog position changes.

## Flow concerns

- `HBR-125` would create an observable-but-unowned alert path; a dashboard alone is not production confidence.
- `HBR-126`'s mixed outcomes hide the smallest release-critical result and could create carryover.
- A cycle assignment must not be used as evidence of readiness.
- Blocked work remains WIP if any item starts before its decision is resolved.

## Suggested Linear views

Only where the fictional workspace supports the fields/relations:

- pulled-next work missing an owner, acceptance, estimate, or dependency treatment;
- production-facing work missing release/monitoring links;
- blocked started work with no unblock owner/next action;
- work rolled over more than once for inspection, not automatic failure;
- later work with excessive detail, to avoid premature refinement.

## Non-findings

- `HBR-127` is not defective for lacking a full release plan at near-term position; it inherits release context from its parent dependencies.
- `HBR-130` is not defective for being unestimated and lacking acceptance criteria while it remains Later.
- `HBR-124` is not blocked by optional manual-review tooling once `HBR-126` is split correctly.

## Paste-ready summary

```markdown
**Readiness audit:** HBR-124 is ready for pull when order/capacity allow. HBR-125 must name an alert responder and link the response runbook. HBR-126 must split automated repair from manual tooling and communication before its release-critical slice can be assessed. Leave HBR-127 and HBR-130 lightweight at their current horizons.
```
