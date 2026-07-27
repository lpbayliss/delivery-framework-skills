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
