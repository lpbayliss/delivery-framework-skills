# Design decisions inherited from the supplied framework

The supplied Notion export is the primary basis for this collection. These decisions were retained even where external sources use different names or narrower methods.

## Retained decisions

- **Linear is the system of record for delivery work.** Tickets, child tasks, order, status, blockers, progress, and current decisions live there.
- **Notion holds durable context and substantial artefacts.** Specifications, designs, test/release plans, retrospectives, and postmortems link back to executable Linear work.
- **The backlog is an ordered ledger of intent.** Position is priority; work no longer intended is explicitly closed with a reason.
- **Ownership is singular and role-based.** Owner, Sponsor, Design, Quality, Engineering, and Stakeholder are hats rather than fixed job titles.
- **Lifecycle language is explicit.** Discovery, Refinement, Triage, Development, and Monitoring are separated by evidence-based gates.
- **Refinement and Triage are different concepts.** Refinement elaborates intent into buildable work; Triage reviews, sizes, and orders incoming work. A workspace may combine them in one recurring session, but the decisions remain distinct.
- **Detail is earned by position and risk.** Active and next work need enough evidence to finish or pull; distant work remains lightweight.
- **Ready and Done are evidence, not status labels.** Ready covers outcome, demonstrable completion, manageable scope, dependencies, and risk-proportionate test/release thinking. Done includes availability to intended users, verification, observability, and a risk-proportionate recovery path.
- **Ceremonies have an MC/facilitator and intended output.** They may be merged, resized, or renamed deliberately.
- **Review demonstrates outcomes rather than narrating tickets.** Retrospective improves the working system and ends in owned experiments.
- **Delivery closes the loop.** Monitoring compares observed behaviour/outcomes with intent; learnings become explicit work or explicit no-action decisions.

## Deliberate portability changes

The public skills do not retain:

- organization names, internal links, or internal-only tools;
- fixed capacity percentages, urgency thresholds, or incident triggers;
- assumptions that every team uses sprints or Scrum;
- job-title-specific staffing requirements;
- claims that one artefact size suits all work.

Where the source contained a fixed local convention that would be unsafe to generalize, the skill requires the workspace policy or an explicit decision instead of inventing a universal default.

## Research relationship

The Scrum Guide, Kanban Guide, DORA, Google SRE, Linear documentation, and Notion documentation were used to:

- clarify ceremony purpose and flow concepts;
- fill gaps in postmortems, alerting, and product capabilities;
- add warnings against over-generalization;
- verify current Linear and Notion concepts.

They do not override the retained decisions above.