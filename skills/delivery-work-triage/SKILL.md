---
name: delivery-work-triage
description: Triage new or incoming delivery work for Linear: find duplicates, request missing evidence, accept, snooze, decline, route, return for refinement, size, and recommend backlog placement. Use for triage inboxes, intake queues, bug/request review, or deciding what should happen to newly raised work.
---

# Delivery Work Triage

Make an explicit decision without turning triage into a full refinement workshop.

## Source precedence

Use this order: (1) current task instructions, (2) the workspace's own framework/templates/policies, (3) bundled generic defaults, (4) external sources. Never replace a local decision with generic “best practice” without identifying the conflict.

## Tool behaviour

When connected to Linear or Notion, inspect the canonical records before reasoning. Use Linear for executable work and Notion for durable artefacts. Link rather than duplicate. If tools are unavailable, return paste-ready Markdown and field mappings. Never claim that a remote record changed unless the tool confirms it.

Do not invent business facts, priorities, owners, estimates, dates, thresholds, commitments, or success targets. Mark missing material as a question, assumption, or blocker.


## Accountabilities

- The accountable owner orders the backlog and resolves value/scope trade-offs.
- People who will deliver and verify the work lead feasibility and sizing.
- Sponsor/stakeholder input is used when intent or external impact needs clarification.
- Triage recommends; it does not invent authority.

## Workflow

1. Read the issue, linked context, duplicate candidates, blockers, current objective, and backlog neighbourhood.
2. Normalize the request into problem/outcome, affected scope, evidence, urgency driver, and submitter need.
3. Check duplicate/related/blocking relations before creating or accepting more work.
4. Choose one disposition from [the decision model](references/triage-decision-model.md): accept, needs information, return for refinement, duplicate, snooze, decline/close, or route.
5. If accepted, classify work type, propose an owner/accountable hat, identify sizing participants, and recommend relative placement with reasons. Backlog position is priority; do not create fake ties.
6. Apply the definition ladder. Only near-term work needs near-term detail.
7. Record the decision and reason on the canonical issue. Preserve submitter context and link any durable Notion artefact.

## Output

For one issue:

- **Disposition**
- **Reason and evidence**
- **Missing information / refinement needed**
- **Duplicate, dependency, and related-work links**
- **Recommended owner, work type, and backlog neighbourhood**
- **Paste-ready Linear comment / property changes**

For a batch, use `templates/triage-record.md` or an equivalent table with one row per issue and a second list for questions that need human decisions. Never imply the suggested order has been accepted unless an accountable owner confirms it.
