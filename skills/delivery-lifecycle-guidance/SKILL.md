---
name: delivery-lifecycle-guidance
description: Diagnose where an initiative or work item sits in a delivery lifecycle and identify the next phase, gate, owner, ceremony, and artefact. Use when the user asks “what happens next?”, whether work is ready to move, who should own a decision, or how a request moves from idea through delivery and learning.
---

# Delivery Lifecycle Guidance

Use the lifecycle as a decision map, not a waterfall. Work may move backward when evidence exposes a gap, and artefact depth scales with risk.

## Source precedence

Use this order: (1) current task instructions, (2) the workspace's own framework/templates/policies, (3) bundled generic defaults, (4) external sources. Never replace a local decision with generic “best practice” without identifying the conflict.

## Tool behaviour

When connected to Linear or Notion, inspect the canonical records before reasoning. Use Linear for executable work and Notion for durable artefacts. Link rather than duplicate. If tools are unavailable, return paste-ready Markdown and field mappings. Never claim that a remote record changed unless the tool confirms it.

Do not invent business facts, priorities, owners, estimates, dates, thresholds, commitments, or success targets. Mark missing material as a question, assumption, or blocker.


## Workflow

1. Read the initiative, Linear state/order, linked Notion artefacts, current owner, and observed evidence.
2. Map evidence to [the lifecycle map](references/lifecycle-map.md). Do not infer a phase from a status name alone.
3. Identify the current unresolved decision and accountable hat.
4. Test the relevant exit gate. Separate satisfied evidence, missing evidence, and irrelevant generic requirements.
5. Recommend one next move: progress, remain, return, split, pause, close, or monitor.
6. Name the smallest next artefact or ceremony needed. Avoid generating documents that do not resolve a decision.
7. State what belongs in Linear and what belongs in Notion.

## Output

Use `templates/lifecycle-assessment.md` as the default paste-ready structure.

- **Current phase and confidence**
- **Evidence**
- **Gate assessment**
- **Next decision and accountable hat**
- **Next action / ceremony / artefact**
- **Linear and Notion updates**
- **Risks or contradictions**

Never claim that a gate passed merely because a document exists; assess whether the evidence supports the gate's purpose.
