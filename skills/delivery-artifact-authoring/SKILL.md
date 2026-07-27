---
name: delivery-artifact-authoring
description: Create or improve delivery artefacts for Notion and linked Linear work: specifications, design documents, test plans, release plans, monitoring/measurement plans, dashboard briefs, and postmortems. Use when the user asks for a spec, design, test strategy, rollout/rollback plan, observability plan, success measures, decision record, or incident/project postmortem.
---

# Delivery Artefact Authoring

Create the minimum durable artefact that resolves uncertainty and supports the next delivery decision. Prefer a few lines on the Linear ticket for small work and a linked Notion page for substantial or cross-cutting work.

## Source precedence

Use this order: (1) current task instructions, (2) the workspace's own framework/templates/policies, (3) bundled generic defaults, (4) external sources. Never replace a local decision with generic “best practice” without identifying the conflict.

## Tool behaviour

When connected to Linear or Notion, inspect the canonical records before reasoning. Use Linear for executable work and Notion for durable artefacts. Link rather than duplicate. If tools are unavailable, return paste-ready Markdown and field mappings. Never claim that a remote record changed unless the tool confirms it.

Do not invent business facts, priorities, owners, estimates, dates, thresholds, commitments, or success targets. Mark missing material as a question, assumption, or blocker.


## Workflow

1. Select an artefact from [the artefact catalogue](references/artefact-catalogue.md).
2. Read the initiative/ticket, preceding artefacts, decisions, evidence, constraints, and workspace template.
3. Identify the decision this artefact must support and its reviewers.
4. Draft only supported facts. Label assumptions, options, unresolved questions, decision owners, and any `framework gap` where the workspace/source has no approved policy or template.
5. Scale sections to size and risk. Delete irrelevant headings rather than filling them with boilerplate.
6. Check traceability: intended outcome → design/scope → acceptance/testing → release/recovery → observation/learning.
7. Put durable depth in Notion and concise execution facts/links on Linear.
8. Return review questions and the next gate this artefact enables.

## Quality rules

- Specifications explain problem, outcome, scope, evidence, and success without prematurely locking implementation.
- Designs explain how intent will be realized, alternatives/trade-offs, boundaries, failure modes, and review decisions.
- Test plans explain confidence: scope, approach, environments/data, ownership, entry/exit evidence, and regression.
- Release plans explain sequencing, rollout, communication, recovery/rollback, verification, and ownership.
- Monitoring plans distinguish outcome measures, health signals, dashboards, and actionable alerts.
- Postmortems are factual, blameless, systemic, reviewed, and produce owned preventive actions.

## Output

Return a paste-ready artefact using the selected file under `templates/`, a Linear linkage block, open questions, reviewers, and next-gate evidence.
