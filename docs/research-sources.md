# Research sources

The supplied framework was the primary design input. These sources supplement it and are not allowed to silently override an explicit workspace decision.

## Delivery and flow

- [Manifesto for Agile Software Development](https://agilemanifesto.org/) — primary values behind iterative, collaborative delivery; it does not prescribe a ticket template or ceremony set.
- [The Scrum Guide (2020)](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf) — purposes of planning, Daily Scrum, review, retrospective, backlog refinement, goals, and Definition of Done.
- [The Kanban Guide (May 2025)](https://kanbanguides.org/the-kanban-guide) — Definition of Workflow, explicit policies, WIP control, pull, work-item age, throughput, cycle time, and continuous improvement.
- [DORA software delivery performance metrics](https://dora.dev/guides/dora-metrics) — delivery outcome measures, small batches, context-sensitive measurement, and warnings against cross-team competition or metrics as targets.
- [DORA: working in small batches](https://dora.dev/capabilities/working-in-small-batches/) — reducing risk and increasing feedback through smaller changes.
- [INVEST in Good Stories (Bill Wake)](https://xp123.com/invest-in-good-stories-and-smart-tasks/) — a heuristic for discussing story quality, not a mandatory gate.
- [Cucumber Gherkin reference](https://cucumber.io/docs/gherkin/reference) — Given/When/Then syntax where example-based acceptance improves precision; not required for every criterion.
- [MoSCoW prioritisation (Agile Business Consortium)](https://www.agilebusiness.org/resource/what-is-moscow-prioritization/) — optional scope-negotiation vocabulary; it does not replace a single relative backlog order.

## Reliability and learning

- [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — symptom-oriented, low-noise alerting; dashboards; latency, traffic, errors, and saturation.
- [Google SRE: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) — blameless systemic learning, impact/timeline/contributing causes, preventive actions, review, and publication.
- [Google SRE: Example Postmortem](https://sre.google/sre-book/example-postmortem/) — a concrete incident record shape.

## Linear

- [Concepts](https://linear.app/docs/conceptual-model) — issues, workflows, projects, cycles, initiatives, and views.
- [Triage](https://linear.app/docs/triage) — accept, duplicate, decline, snooze, request information, and responsibility.
- [Issue templates](https://linear.app/docs/issue-templates) — standard/form templates and default properties.
- [Issue relations](https://linear.app/docs/issue-relations) — blocked, blocking, related, and duplicate.
- [Cycles](https://linear.app/docs/use-cycles) — repeating time boxes, rollover, capacity, and the distinction from releases.

## Notion

- [Database templates](https://www.notion.com/help/database-templates) — repeatable page structures and template-local properties.
- [Database properties](https://www.notion.com/help/database-properties) — status, people, dates, URLs, relations, rollups, and metadata.
- [Relations and rollups](https://www.notion.com/help/relations-and-rollups) — connected databases and aggregate properties.
- [Views, filters, sorts, and groups](https://www.notion.com/help/views-filters-and-sorts) — multiple views over the same database.
- [Documents database for product teams](https://www.notion.com/help/guides/documents-database-for-product-teams) — document templates, properties, and linked views.

## Limits on generalization

- Scrum events are authoritative only when a team claims to use Scrum; the skills use their purposes as adaptable facilitation guidance.
- Kanban's current guide defines required elements for a Kanban system; teams not claiming Kanban can still use the flow insights without being labelled Kanban.
- DORA metrics are application/service-level improvement measures, not team ranking tools.
- Google SRE examples are reliability patterns, not universal incident thresholds.
- Linear and Notion capabilities depend on workspace configuration and plan.
