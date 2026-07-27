# Notion and Linear interoperability model

## Default boundary

### Linear

Use for issues/tickets and sub-issues/tasks, owner, team, workflow status, backlog order, priority, estimate, cycle, project, blocking/related/duplicate relations, comments, current decisions, and progress.

### Notion

Use for durable specifications, design records, test strategies, release plans, monitoring plans, decision records, retrospectives, and postmortems. Database templates can standardize page structure; properties, relations, rollups, and views can make artefacts discoverable.

## Linking rules

- Put the canonical document URL on the Linear issue/project.
- Put the canonical Linear issue/project URL on the Notion page.
- Keep short acceptance and current execution facts on the issue; keep substantial reasoning in the document.
- Record the final decision or concise decision summary on the issue even when the detailed record lives in Notion.
- Do not maintain competing status fields in both systems unless ownership and synchronization are explicit.

## Capability caveats

- Linear Triage is a special inbox and may be disabled. A skill can still produce a triage decision table for manual use.
- Linear cycles are optional and are not releases.
- Workspace- and team-level Linear templates expose different properties; form templates and some triage automation may depend on plan/configuration.
- Notion database templates are local to a database. Relations in exported CSV become plain text and are not restored by re-import.
- Product behavior changes. Inspect the connected workspace and current official docs before bulk configuration.

## No-API mode

If Notion or Linear is not connected, return paste-ready Markdown plus a field mapping. Never claim that records were created or changed.
