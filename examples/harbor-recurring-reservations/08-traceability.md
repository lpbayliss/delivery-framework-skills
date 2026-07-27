# Cross-skill traceability

[← Back to showcase](README.md)

## Decision chain

| Decision/evidence | First established in the story | Consumed by | Durable/execution record |
|---|---|---|---|
| Delivery system needs reset | starting workspace evidence | backlog reset | Notion policy record + Linear issue changes |
| Request merits investigation | triage evidence/disposition | lifecycle checkpoint A | Linear HBR-117 + linked Notion spec |
| Outcome and rough scope are agreed | specification | Planning gate | Notion specification + concise Linear decision |
| Contract/failure/recovery are understood | HBR-121 design decision | ticket writing, Refining gate | Notion design + Linear dependency |
| HBR-124 is independently demonstrable | deliverable acceptance | readiness audit, kickoff, delivery | Linear HBR-124 |
| Alert response is unresolved | readiness audit | lifecycle checkpoint C, refinement agenda | Linear HBR-125 finding |
| Mixed repair scope must split | readiness audit | lifecycle checkpoint C, release plan | Linear HBR-126 split decision |
| Release is tested, observable, recoverable | test/release/monitoring evidence | Validating gate and staged rollout | linked Notion plans + Linear stage decisions |
| Intended outcome observed | 14-day evidence | review and lifecycle checkpoint D | Notion outcome review + Linear closure |
| Review waiting needs an experiment | retrospective facts/hypothesis | experiment ticket | Notion retro + Linear experiment |

## Gate evidence

| Gate | Evidence used | Result in this story |
|---|---|---|
| Scoping | problem, Sponsor, plausible June evidence | investigation justified |
| Planning | agreed problem, outcome, scope, non-goals, success observation | pass after specification |
| Refining | contract/failure decisions, artefacts, intentional tickets | pass after HBR-121 and drafting |
| Executing | item-level owner, acceptance, estimate, dependencies, risk controls | HBR-124 pass; HBR-125 fail; HBR-126 conditional |
| Validating | live/tested/observable/recoverable evidence | passed at staged release decisions |
| Analysing & Learning | 14-day outcome and health evidence plus explicit follow-up | pass; initiative outcome closed |

## Framework principles demonstrated

- One initiative Owner persists through phases; discipline ownership remains domain-specific.
- Work can move backward: readiness gaps return to Refinement rather than being waved through Triage.
- Artefact existence is not gate passage; the content is tested against the gate's purpose.
- Detail is earned by position: `HBR-130` remains lightweight while pulled-next work carries deeper evidence.
- Blocked work remains WIP; an expedite names displacement.
- Done is more than merged code: live, tested, observable, and recoverable.
- Outcome/health evidence is compared with predeclared observations after release.
- Learning becomes explicit work or an explicit no-action decision.

## Deliberate non-claims

The example does not claim:

- access to or mutation of a real Linear/Notion workspace;
- that a named date automatically sets priority or commitment;
- that its WIP limit, estimates, stage percentages/durations, objectives, or cadence fit another team;
- that a feature flag alone proves recoverability;
- that a dashboard without an alert responder/runbook is production-ready;
- that one successful 14-day window guarantees permanent absence of defects;
- that a ceremony, status, or document automatically approves a gate;
- that every framework gap has an organizationally approved answer.

## Skill coverage check

- [x] `delivery-backlog-reset`
- [x] `delivery-work-triage`
- [x] `delivery-lifecycle-guidance`
- [x] `delivery-ticket-writing`
- [x] `delivery-artifact-authoring`
- [x] `delivery-readiness-audit`
- [x] `delivery-ceremony-facilitation`
