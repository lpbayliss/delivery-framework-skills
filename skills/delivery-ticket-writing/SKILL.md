---
name: delivery-ticket-writing
description: Draft, split, or improve delivery tickets for Linear using portable deliverable, bug, spike, debt, and child-task templates. Use whenever the user asks to create a ticket, story, issue, bug report, spike, debt item, acceptance criteria, or to turn notes/Notion context into work, even if they do not mention this skill.
---

# Delivery Ticket Writing

Create a discrete, deliverable unit of work with a clear why and demonstrable completion evidence. Prefer the workspace template when one exists.

## Source precedence

Use this order: (1) current task instructions, (2) the workspace's own framework/templates/policies, (3) bundled generic defaults, (4) external sources. Never replace a local decision with generic “best practice” without identifying the conflict.

## Tool behaviour

When connected to Linear or Notion, inspect the canonical records before reasoning. Use Linear for executable work and Notion for durable artefacts. Link rather than duplicate. If tools are unavailable, return paste-ready Markdown and field mappings. Never claim that a remote record changed unless the tool confirms it.

Do not invent business facts, priorities, owners, estimates, dates, thresholds, commitments, or success targets. Mark missing material as a question, assumption, or blocker.


## Workflow

1. Inspect the request, parent initiative/project, linked Notion artefacts, nearby Linear issues, and workspace template.
2. Select a ticket type: deliverable, bug, spike, debt, or child task. Read [ticket types](references/ticket-types.md).
3. Separate known facts from assumptions. Ask only for missing information that materially changes scope, priority, safety, or acceptance.
4. Draft the smallest independently demonstrable result. Split mixed outcomes or unrelated risks.
5. Write acceptance criteria as observable outcomes, not an implementation checklist. Use Given/When/Then only where it improves precision.
6. Scale test, release, recovery, and observability detail to risk. A trivial change can use one line; a risky change may require linked Notion plans.
7. Preserve the outcome and decisions on the Linear issue; link substantial design/specification material in Notion.
8. Run the quality check below and return either the final ticket or a blocked draft with targeted questions.

## Quality check

- Title names the result or problem, not an activity such as “work on”.
- One owner/accountable hat is identifiable.
- Why/outcome and scope are distinct.
- Acceptance criteria demonstrate Done.
- Non-goals or boundaries prevent likely scope drift where needed.
- Dependencies and unknowns are explicit; genuine uncertainty becomes a spike.
- Testing, release/recovery, and observation are proportionate.
- No fabricated estimate, priority, deadline, or business claim.

## Output

Return:

1. **Ticket type and title**
2. **Linear properties** — owner, team/project/cycle, priority, estimate, labels only when known
3. **Description** — paste-ready Markdown using the selected bundled file in `templates/`
4. **Linked context** — canonical Notion/Linear links
5. **Open questions / assumptions** — omit when empty
6. **Split recommendation** — only when needed
