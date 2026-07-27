# Delivery Framework Skills

Portable Agent Skills for facilitating software and knowledge-work delivery with **Linear** as the work system of record and **Notion** as the durable documentation system.

The reusable skills and framework documentation are generic: they contain no real organization-specific claims, names, thresholds, or policy. The `examples/` directory uses clearly labelled fictional data only. When a workspace has its own delivery framework, templates, definitions, or tool conventions, those local decisions take precedence.

## Skills

| Skill | Use it for |
|---|---|
| `delivery-ticket-writing` | Draft or improve deliverable, bug, spike, debt, and task tickets |
| `delivery-work-triage` | Review incoming work and decide accept, clarify, duplicate, snooze, decline, or refine |
| `delivery-readiness-audit` | Find active or near-term tickets that are not ready enough for their position |
| `delivery-ceremony-facilitation` | Prepare, run, and record kickoff, planning, stand-up/flow review, refinement, review, retrospective, and postmortem sessions |
| `delivery-artifact-authoring` | Create specifications, designs, test plans, release plans, monitoring plans, and postmortems |
| `delivery-lifecycle-guidance` | Locate work in the delivery lifecycle and identify the next accountable decision, artefact, or gate |
| `delivery-backlog-reset` | Run a focused reset that makes current work visible, orders the near-term backlog, and commits operating cadences |

## Shared operating model

- Keep delivery work, status, ordering, blockers, estimates, and progress in Linear.
- Keep durable reasoning and substantial artefacts in Notion; link them from Linear.
- Preserve decisions on the ticket even when discussion happens elsewhere.
- Give every initiative and work item one accountable owner.
- Treat the backlog as an ordered ledger of intent, not a storage bin.
- Scale detail to proximity, size, and risk. Do not refine the whole backlog equally.
- Prefer small, demonstrable, observable, and recoverable changes.
- Close the loop: observations and learnings become explicit work or explicit no-action decisions.

See [framework basis](docs/framework-basis.md), [inherited design decisions](docs/design-decisions.md), [source gaps and portability decisions](docs/framework-gaps.md), [tool model](docs/notion-linear-model.md), and [research sources](docs/research-sources.md).

## End-to-end example

The [Harbor recurring reservations showcase](examples/harbor-recurring-reservations/README.md) executes all seven skills against one fictional story—from backlog reset and intake through artefacts, readiness, staged release, review, retrospective, and outcome closure.

## Install

### Claude Code plugin

```bash
claude plugin marketplace add lpbayliss/delivery-framework-skills
claude plugin install delivery-framework@delivery-framework-skills
```

### Individual skills

Build deterministic `.skill` and Claude app `.zip` files:

```bash
python3 scripts/package_skill.py
python3 scripts/check_packages.py
```

Upload a file from `dist/<skill-name>.zip` in Claude's Skills settings, or use the corresponding `.skill` archive with compatible clients.

## Validate

```bash
python3 scripts/check.py
python3 scripts/package_skill.py
python3 scripts/check_packages.py
```

## Source precedence

Every skill follows this order:

1. Explicit instructions for the current task.
2. The current workspace's documented framework, templates, definitions, and policies.
3. The generic defaults bundled here.
4. External research and product documentation.

The original source export used to derive these generic defaults is intentionally not published. It may contain internal context and is not needed to use the skills.

## License

MIT. External sources are cited, not copied as bundled source material.
