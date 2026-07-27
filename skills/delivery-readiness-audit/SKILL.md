---
name: delivery-readiness-audit
description: Audit Linear backlogs, cycles, projects, or issue lists to find work that is stale, blocked, oversized, unowned, or under-refined for its position. Use for “what needs refinement?”, backlog health checks, cycle readiness, carryover reviews, or preparing a refinement session.
---

# Delivery Readiness Audit

Find the smallest set of corrections that make current and near-term delivery trustworthy. Do not score distant work against near-term standards.

## Source precedence

Use this order: (1) current task instructions, (2) the workspace's own framework/templates/policies, (3) bundled generic defaults, (4) external sources. Never replace a local decision with generic “best practice” without identifying the conflict.

## Tool behaviour

When connected to Linear or Notion, inspect the canonical records before reasoning. Use Linear for executable work and Notion for durable artefacts. Link rather than duplicate. If tools are unavailable, return paste-ready Markdown and field mappings. Never claim that a remote record changed unless the tool confirms it.

Do not invent business facts, priorities, owners, estimates, dates, thresholds, commitments, or success targets. Mark missing material as a question, assumption, or blocker.


## Workflow

1. Establish scope: active work, next cycle/pull set, near term, and later. If order is unavailable, say so; do not infer priority from labels alone.
2. Read issues and linked canonical documents. Inspect owner, status, age, blockers, next action, acceptance criteria, size, dependencies, test/release thinking, and success observation.
3. Apply [the readiness ladder](references/readiness-ladder.md) by position and risk.
4. Detect failure modes: no owner, no next action, inactive/aging WIP, hidden blocker, mixed outcomes, ambiguous Done, missing dependency decision, repeated rollover, stale intent, premature detail, or missing production confidence.
5. Separate **must fix before pull**, **refine soon**, **flow intervention**, and **leave alone**.
6. Propose a focused refinement agenda ordered by delivery risk and proximity. Do not rewrite every issue unless asked.

## Output

Use `templates/readiness-audit.md` as the default paste-ready report shape.

- **Scope and assumptions**
- **Executive finding** — whether current/near-term work is trustworthy
- **Issue table** — issue, horizon, finding, evidence, action, owner/decision needed
- **Refinement shortlist** — ordered and timeboxed
- **Flow concerns** — blocked/aging/carryover/WIP patterns, without invented thresholds
- **Suggested Linear views/filters** — only capabilities actually available
- **Non-findings** — items intentionally left lightweight
