# Readiness ladder

| Horizon | Evidence expected | Common finding |
|---|---|---|
| In flight | owner, next action, completion evidence, blocker/unblock owner, current record | inactive WIP, hidden blocker, no finish path |
| Pulled next | outcome/why, demonstrable acceptance, small enough, size where used, dependencies, test/release/observation proportional to risk | ambiguous Done, mixed scope, unresolved dependency |
| Near term | accountable hat, why, rough size, dependencies and unknowns | no reason, stale intent, unknown treated as certainty |
| Later | durable title, one-line why, work type | excessive detail or work no longer intended |

## Audit rules

- A missing field is not automatically a defect; ask whether it is needed for the next decision.
- An artefact link is not proof that its content is current or sufficient.
- Repeated rollover is a signal to inspect scope, blockage, ordering, or capacity.
- Blocked work remains WIP.
- Use work-item age and local service expectations when available; do not invent a universal stale threshold.
- Do not use backlog size or field-completion percentage as a success measure.
