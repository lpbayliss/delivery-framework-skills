# Generic delivery framework basis

## Status and scope

This repository distils a supplied delivery-framework export into portable defaults. It deliberately removes organization names, internal tools, fixed percentages, and claims that a practice fits every context. The supplied framework outweighed external research whenever it made a clear process decision; external sources were used to fill gaps and make facilitation safer.

## Principles

- Visibility, traceability, and clarity: work, status, and material reasoning are inspectable.
- Clear ownership: each initiative and work item has one accountable owner; roles are hats, not job titles.
- Clear expectations: outcome, ready-enough conditions, completion evidence, and success measures are explicit before work is pulled.
- Continuous planning: backlog care happens continuously; formal planning confirms more than it discovers.
- Outcomes over output: shipped work is evaluated against its intended effect.
- Small and safe delivery: use thin slices, controlled release, observability, and a recovery path proportional to risk.
- Closed feedback loop: learnings, bugs, and debt become explicit backlog decisions.

## Lifecycle

`Scoping → Discovery → Planning gate → Refinement → Refining gate → Triage → Executing gate → Development → Validating gate → Monitoring → Analysing & Learning`

The sequence is stable; effort and artefact depth scale to size and risk.

| Phase | Purpose | Default lead hat | Typical output / exit evidence |
|---|---|---|---|
| Discovery | Understand the problem, evidence, intended outcome, and rough scope | Sponsor | Specification; decision that investigation is worth elaborating |
| Refinement | Turn intent into buildable work | Owner | Tickets, design, test and release thinking proportional to risk |
| Triage | Review, size, and order candidate work | People who will deliver/verify it | Accepted and ordered work, or a clear return/decline/duplicate decision |
| Development | Build, review, test, release, and make observable | Delivery team | Completion evidence meeting Done |
| Monitoring | Compare observed behaviour and outcomes with intent | Owner | Dashboard/observations, learnings, and explicit follow-up decisions |

## Gate defaults

- **Scoping:** problem can be named, a sponsor hat exists, and potential value justifies investigation. This is not a build commitment.
- **Planning:** problem, intended outcome, rough scope, and supporting evidence are coherent enough to elaborate.
- **Refining:** designs and plans are proportionate; tickets have care and intent; work can be assessed and sized.
- **Executing:** work is ordered, sized where the workspace requires sizing, and meets the local Definition of Ready.
- **Validating:** completion evidence is satisfied; the result is available to intended users, observable, and recoverable/reversible to the extent risk requires.
- **Analysing & Learning:** observed results have been compared with intended outcomes; learnings are captured as explicit work or no-action decisions.

## Definition ladder

Detail is earned by position:

- **In flight:** owner, next action, completion evidence, blocker/unblock owner, and production-testing note where relevant. Do not retrofit ceremonial prose.
- **Pulled next:** why/outcome, demonstrable acceptance criteria, size, dependencies, test approach, release/recovery approach, and success observation proportional to risk.
- **Near term:** owner or accountable hat, why, rough size, dependencies, and material unknowns.
- **Later:** durable title, one-line why, and work type. Nothing more unless risk or policy requires it.

## Tool boundary

Linear is the system of record for work. Notion holds durable context and substantial artefacts. Link rather than duplicate. See [Notion and Linear model](notion-linear-model.md).
