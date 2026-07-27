# Lifecycle map

| Named gate / milestone | Transition | Question | Sufficient evidence pattern |
|---|---|---|---|
| Scoping | Idea/request → Discovery | Is this worth investigating? | named problem, sponsor hat, plausible value/evidence |
| Planning | Discovery → Refinement | Do we know what outcome and rough scope are worth elaborating? | coherent specification and decision |
| Refining | Refinement → Triage | Can deliverers assess and size this without reopening the why? | proportionate design/test/release thinking and intentional tickets |
| Executing | Triage → Development | Is this ordered and ready enough to pull? | owner, outcome, completion evidence, size/dependencies and risk controls |
| Validating | Development → Monitoring | Is the result Done? | available, tested, observable, and recoverable/reversible proportional to risk |
| Analysing & Learning | Monitoring → Learned/closed | Do observed results answer the intended question? | outcome/health evidence and explicit follow-up/no-action decisions |

## Movement rules

- Move backward when a later phase reveals a missing earlier decision.
- Split work when one item crosses independent outcomes or risk profiles.
- Pause when the revisit condition is explicit; close when intent no longer exists.
- Do not confuse ceremony completion, status changes, or document existence with gate evidence.
