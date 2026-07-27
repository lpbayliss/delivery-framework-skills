# Evaluation

Each skill owns:

- `evals/evals.json`: three representative output cases with objective quality assertions.
- `evals/trigger-evals.json`: ten positive and ten difficult negative trigger cases.

The repository validator checks shape, uniqueness, links, and trigger balance. These are test definitions, not proof of model behaviour. For a behavioural release check, run representative prompts with the target model, preserve outputs, grade the assertions, and compare against a no-skill baseline where practical.

Recommended release sample:

1. Ticket authoring: unknown properties remain unknown; acceptance is observable.
2. Triage: an underspecified urgent request is not accepted on invented urgency.
3. Readiness: distant lightweight work is not falsely failed.
4. Ceremony: review and retro end in decisions/actions, not generic discussion.
5. Artefact: release plan does not invent thresholds.
6. Lifecycle: document existence is not treated as gate passage.
7. Backlog reset: the real tool and follow-through are preserved.

## Behavioural smoke run — 2026-07-27

Independent agents executed 12 representative cases across all seven skills and wrote the outputs outside the repository for inspection. Coverage included:

- ticket authoring, underspecified triage, and horizon-sensitive readiness;
- sprint review, retrospective, release planning, and specification authoring;
- all three lifecycle cases and sprint-free/continuous-flow backlog resets.

All 12 outputs passed all five assertions: **60/60 PASS**. No fabricated owners, dates, priorities, thresholds, remote mutations, or organization-specific claims were found. One specification case produced moderate but justified boilerplate because its prompt referred to discovery notes without supplying them; the output correctly remained a source-ingestion scaffold instead of inventing content.

This is behavioural smoke evidence, not a statistically rigorous benchmark or trigger-optimization result. The reusable eval definitions remain the source for future model/version comparisons.
