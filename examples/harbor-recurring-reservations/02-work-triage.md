# Skill execution: delivery-work-triage

[← Back to showcase](README.md)

**Input:** Noor's request and linked evidence in [00-source-context.md](00-source-context.md).

**Item:** fictional Linear intake `HBR-117`.

**Output type:** completed triage decision.

## Normalized request

- **Problem:** Editing the future portion of a recurring reservation series can leave stale future occurrences, causing reservation conflicts and manual correction.
- **Affected scope:** organisers managing recurring reservations and staff resolving conflicts.
- **Evidence:** 24 classified support requests in June; nine stale results in a 40-edit manual review; seven required manual correction.
- **Requested timing:** before 12 September partner onboarding.
- **Date source:** onboarding of four partner workshops; Sponsor Noor owns any decision to change it.
- **Requested outcome:** future-series edits do not leave stale occurrences.

## Duplicate and relationship check

- `HBR-88` is related but not a duplicate. It corrected single-occurrence edits and is already closed.
- No existing issue covers edits to the future portion of a recurring series.
- Record `HBR-88` as **related**; do not reopen or duplicate its scope.

## Disposition

**Accept into Discovery.**

The problem and initial evidence justify investigation, but the request is not Ready for implementation. The exact outcome, scope boundary, success observation, contract, and recovery approach still need decisions.

## Reason and evidence

- The request identifies an observed problem rather than only a preferred feature.
- Impact has multiple evidence points, while the 40-edit review has an explicit sample boundary.
- The named date has a traceable source but is not converted into a delivery promise.
- Existing related work has been checked and is not equivalent.
- Investigation is warranted; build scope is not yet approved.

## Missing refinement

Before implementation triage:

1. Agree the affected edit types and explicit non-goals.
2. Name the intended outcome and review window.
3. Decide how to observe stale occurrences and service health.
4. Resolve API contract, transaction/failure behaviour, compatibility, and recovery.
5. Produce risk-proportionate testing and staged-release plans.
6. Split the initiative into independently demonstrable tickets.

## Recommended ownership, type, and placement

- **Initiative Owner:** Maya Chen.
- **Sponsor:** Noor Singh.
- **Work type now:** discovery initiative/request, not yet a deliverable ticket.
- **Sizing participants later:** server, web, quality, and operational hats.
- **Backlog neighbourhood:** place in the ordered Discovery queue according to Maya's trade-off decision. The named date and evidence are inputs; triage does not claim an accepted rank.

## Paste-ready Linear comment

```markdown
**Triage disposition: Accept into Discovery**

The request is supported by June evidence: 24 classified support requests; a manual review found stale future occurrences after 9 of 40 affected series edits, with 7 requiring manual correction. The 12 September date comes from onboarding four partner workshops and remains context, not an implementation commitment.

HBR-88 is related, not duplicate: it covers single-occurrence edits, not future-series edits.

Before implementation triage, Discovery/Refinement must agree the outcome, edit scope and non-goals, success observation, API/failure behaviour, recovery, and risk-proportionate test/release plans. Maya Chen is the initiative Owner; Noor Singh is Sponsor.

**Next action:** create/link the canonical Notion specification and return intentional deliverable tickets to Triage when the Refining gate evidence exists.
```

## Suggested property changes

- Disposition/status: workspace equivalent of **Accepted / Discovery**.
- Owner: Maya Chen.
- Sponsor/context: Noor Singh in the linked initiative context.
- Relation: `HBR-88` as related.
- Due date, estimate, priority, cycle: unchanged until authorized decisions exist.
- Notion link: add when the specification is created.
