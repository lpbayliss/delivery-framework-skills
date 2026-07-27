# Framework gaps and portability decisions

The supplied framework is a proposal and contains deliberate flexibility plus unfinished areas. The public skills must expose these as questions or generic defaults, not claim that the source approved details it did not define.

| Source gap or ambiguity | Portable skill behavior |
|---|---|
| Definition of Ready and Definition of Done are referenced as gates, but their canonical templates are unfinished. | Use the source's prose and readiness ladder as **generic defaults**; prefer a workspace definition and label any proposed addition. |
| Ticket and document templates/examples are placeholders. | Bundle practical templates derived from the source and research, clearly presented as replaceable starting points. |
| “Documentation lives on the ticket” and Notion is the documentation home. | Keep substantial canonical documents in Notion; link them and record consequential/current decisions on the Linear issue. |
| One initiative Owner is required, while some phases have multiple discipline leads. | Preserve one end-to-end initiative Owner. Treat discipline leads as accountable for their domain input; do not invent a single phase approver. |
| Artefact authors, reviewers, and approvers are mostly unspecified. | Ask for or recommend reviewers by required expertise. Never fabricate approval authority. |
| Ceremony attendance differs between records. | Invite roles needed for the intended decision. Treat broad stakeholder attendance as contextual, not universally mandatory. Preserve explicitly required delivery/quality/design participation where a workspace adopts it. |
| Postmortem details are sparse. | Retain the source's systemic-prevention purpose; use Google SRE only as a supplementary, replaceable facilitation default for incidents. Support significant project events separately. |
| `Critical Service` is an empty artefact. | Do not invent or publish a definition. Ignore it until a workspace defines it. |
| Development and Monitoring both “produce” dashboards/monitors. | Treat Development as creating initial observability and Monitoring as operating, validating, and tuning it unless local documentation says otherwise. |
| Gate approvers, waivers, and exception authority are not defined. | Assess evidence and name the decision needed; do not claim a gate has organizational approval without a confirmed authority. |
| A fixed maintenance-capacity percentage appears without scope or override rules. | Do not generalize the number. Require the workspace's explicit allowance/policy during planning. |
| Stakeholder examples are unfinished. | Use the generic definition: people or groups with relevant information, expertise, responsibility, interest, or impact. Do not invent organization-specific stakeholder classes. |

These decisions preserve the source's intent while preventing public skills from turning local or unfinished material into universal policy.