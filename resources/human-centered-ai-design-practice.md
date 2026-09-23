# Human-Centered AI Design Practice

Use with Chapter 16 and Appendix B of *The Amplified Engineer*. Leave with a
system comparison and one justified next design decision. You do not need a
model, customer data, or a finished application to begin.

## Start with the supplied case

Meridian's dispute dashboard calls a case “closed” when internal reconciliation
finishes. A customer may still need an explanation or a correction. Staff
switch between two systems and copy notes to answer questions. The proposed AI
feature drafts explanations; it must not authorize refunds or close disputes.

Everything in this case, including observations and numbers, is fictional.
Use it to practice reasoning, not as evidence of product performance or user
research. For a fifteen-minute first pass, complete the comparison and answer
the decision questions. For a real project, continue through the research and
testing records below.

### Map the system before choosing a tool

**Current inputs:** dispute ID, two authorized payment records, and the
customer's message. **Steps:** find the records, compare their states, write an
explanation, review it, and provide the correction route. **Output:** a checked
response stating what is known and what the customer can do next.

**Boundary:** opening the case through accepted response, including inspection
and correction. Exclude no difficult case silently. Count unresolved work
separately. “Accepted” means the response agrees with the permitted records,
does not promise an unverified refund, and provides a usable next step.

Three candidate paths perform this same job:

- **A — Current process:** staff find and reconcile records manually.
- **B — Conventional improvement:** a shared timeline joins authorized records
  and supplies fixed status text; staff resolve exceptions.
- **C — AI-assisted improvement:** the same timeline plus an AI explanation
  draft; staff check its claims and correct or replace it before sending.

Both B and C still need authorization, accurate records, accessible interaction,
and recovery. A does not become defective simply because people perform it.

### Compare complete work

The invented exercise uses twenty comparable cases per path. Every case meets
acceptance after correction. No response is sent automatically. Minutes below
are total staff effort across those twenty cases, not elapsed delivery time.

| Effort category | A: current | B: timeline | C: timeline + AI |
|---|---:|---:|---:|
| Find records and prepare response | 180 | 120 | 70 |
| Inspect and correct | 60 | 60 | 130 |
| Total staff minutes | 240 | 180 | 200 |
| Initial responses needing correction | 6 | 3 | 8 |
| Unresolved cases after correction | 0 | 0 | 0 |

Before reading the interpretation, answer:

1. What bottleneck does B address? What additional work does C automate?
2. Which path uses least complete staff effort? Calculate its reduction from A.
3. Which attractive claim could someone make by reporting only C's preparation
   time? What evidence would that claim omit?
4. What can these data establish about correctness before review, customer
   understanding, accessibility, elapsed delivery, or production scale?
5. Choose the next experiment and name evidence that would change your choice.

**Suggested interpretation:** B removes fragmented lookup and reduces staff
work by 60 minutes, or 25 percent of A's 240 minutes. C automates drafting and
uses 40 fewer minutes than A, about 16.7 percent less, but 20 more than B.
Its fast draft conceals the greatest correction effort. B is the better next
candidate on this measure. The supplied acceptance rule explains why zero
unresolved cases does not mean zero initial errors. Neither these totals nor
that rule establish customer comprehension, accessible use, elapsed time,
operating cost, or scale. Check those separately before choosing a deployment.

**Changed assumption:** suppose a targeted improvement reduces C's inspection
and correction effort from 130 to 70 minutes without changing the case mix or
acceptance standard. Its total becomes 140 minutes. It would then use 40 fewer
minutes than B, about 22.2 percent less. That is a reason to investigate C,
provided the reduction is observed and errors, privacy, user understanding,
and other obligations still meet the agreed criteria. It is not permission to
remove review merely to produce the better number.

For a real comparison, record dates, versions, case selection, exclusions,
reviewer experience, and case difficulty. Alternate order or use comparable
sets to reduce practice effects. Include failed and unresolved attempts. Use
representative loads and exception rates before claiming scalability. Record
per-case evidence as well as averages so severe failures remain visible.

## Observe before proposing

With permission, ask a person to show the current task. Explain the purpose,
what you will record, who can see it, and when it will be deleted. Participation
must be voluntary. Avoid unnecessary personal data; synthetic practice is
preferable when real records are not needed or authorized.

Ask:

- What are you trying to complete, and why does it matter now?
- Show me what you usually do next.
- Where do you stop, repeat, check elsewhere, or ask another person?
- What do you expect this status or control to mean?
- What happens when the usual path fails?

Do not begin with “Would AI help?” or demonstrate your preferred solution
first. Those prompts can narrow what the person tells you.

Record each finding separately:

- **Observed action and context:**
- **Participant's words:**
- **Your interpretation, still to test:**
- **Broader activity served by this task:**
- **Other people receiving work or consequences:**
- **Unrepresented people or conditions:**

**Worked observation:** a participant stops at the green “closed” status and
says, “Then the money is back.” The inference is that the label implies a
refund. The next test asks what people believe a revised status means; it does
not assume that one participant represents everyone.

## Define the design decision

- Person, situation, and desired outcome:
- Current path and demonstrated bottleneck:
- Conventional software or process alternative:
- Proposed AI role, and decisions it cannot make:
- Fixed obligations, including privacy and accessibility:
- Affected people, including those who do not operate the interface:
- Who can change the decision, and how dissent reaches them:
- Evidence needed to proceed, narrow, retain the current path, or stop:

For this case, a suitable outcome is: “The customer can identify the recorded
state, understand what remains unresolved, and request correction.” A faster
draft alone does not demonstrate that outcome.

## Test the interaction, not just the answer

Recruit people who resemble the intended users, including relevant access and
language needs. Agree on accommodations and let people use familiar assistive
technology. A colleague simulating a disability is not equivalent evidence.
Keep test accounts and records safe. In a live service, do not withhold needed
help to preserve a study protocol.

Use these neutral tasks on a prototype:

1. Find the current state of this dispute. Explain what has and has not happened.
2. Find the information supporting the explanation.
3. The record contains a mistake. Show how you would request correction.
4. An explanation cannot be generated. Show how you would continue.
5. Return after an interruption and find your place.

Avoid naming the controls participants should use. Observe before coaching;
record any assistance. Afterward ask what they expected, what surprised them,
and what they would do if they disagreed.

For each task record **completion, wrong turns, error severity, assistance,
time where meaningful, the participant's interpretation, and the revision to
try**. A short test finds problems; it does not establish universal usability.

### Selected accessibility and usability checks

For web interfaces, start with these WCAG 2.2 references and inspect the whole
applicable standard for the intended conformance scope:

- Keyboard operation and no trap: 2.1.1 and 2.1.2.
- Visible, unobscured focus: 2.4.7 and 2.4.11.
- Text resizing and reflow: 1.4.4 and 1.4.10.
- Meaningful labels and error identification: 3.3.2 and 3.3.1.
- Programmatic name, role, and value: 4.1.2; status messages: 4.1.3.

Inspect status communication, familiar language, consistency, control, and
error recovery using Nielsen's heuristics. Record the actual device, browser,
assistive technology, settings, task, result, and unresolved limitation.
Automated scans and these selected checks are not a conformance certificate.

AI speech or caption features need task-specific evaluation too. Check names,
qualifying details, and correction routes. Provide a usable alternative when
speech is impractical or would disclose private information.

## Review harms and explanations

Complete one record per material concern:

- Affected person or group and plausible harm:
- Data, model behavior, business rule, or interface contributing to it:
- Relevant condition or group to compare, with authorized data handling:
- Evidence and its limits:
- Mitigation, accountable owner, and retest:
- Deployment monitoring and stop or escalation condition:

Keep sensitive records out of public issues and unapproved AI services. Decide
purpose, access, retention, and deletion before collection. Removing names
alone does not establish anonymity or regulatory compliance. Route applicable
privacy obligations to a qualified owner.

An explanation review asks what the recipient needs to do next. Can they tell
which information was used, which claim it supports, what remains uncertain,
and how to obtain correction? An engineer inspecting a prediction may need a
different explanation from the affected customer.

LIME approximates behavior near a prediction; SHAP attributes model output to
features under a chosen setup. Neither proves causal effects, fairness, or the
correctness of a generated explanation. For generated text, check consequential
claims against permitted sources; a fluent account of the model's supposed
reasoning is not a verified execution trace.

## Select and exercise oversight

Use the [Agent Action Safety Check](agent-action-safety-check.md) to define
permissions. Then compare controls for this particular action:

| Control | Useful when | Limitation to test |
|---|---|---|
| Advisory output | A person must make and perform the consequential decision | The recommendation can still mislead; check evidence and reviewer competence |
| Approval before action | A reviewer can inspect the proposed target and effect in time | Review overload or unclear evidence can turn approval into a rubber stamp |
| Bounded automation | Conditions can be enforced and consequences are acceptable within a narrow scope | The boundary may omit a dangerous case; test exceptions and permissions |
| Monitoring and intervention | Failures can be detected and operation can be stopped or recovered | Detection may come after irreversible harm; add preventive controls |

These controls can work together. Complete this selection record:

- Exact action and affected person:
- Consequence severity, uncertainty, and reversibility:
- Time before harm, detection time, and available intervention time:
- Reviewer expertise, capacity, evidence, and authority to refuse:
- Selected controls and the alternative rejected, with reason:
- Enforcement point, owner, stop condition, and safe fallback:
- Failure injected, expected response, observed response, and remaining risk:
- Evidence required before increasing autonomy:

**Practice:** choose controls for (a) tagging an internal case, (b) sending its
AI-drafted explanation to a customer, and (c) issuing a refund. Do not infer
that a control suitable for the tag is sufficient for the other actions.

**Suggested reasoning:** a reversible tag may qualify for bounded automation
if misrouting consequences, limits, and recovery have been tested. A customer
message needs review of claims and recipients before sending in this example;
monitoring cannot make a misleading message unread. Refund execution is
outside the example's authorized scope and remains blocked. Test missing
sources, a wrong account, an unsupported claim, and an unavailable reviewer.
Expected behavior is a stop or safe fallback, not automatic continuation.

A different application may justify a different selection. Explain how its
risk, timing, evidence, and human capacity differ. Do not claim that the
presence of an approval button establishes ethical or reliable operation.

## Close the loop with a decision

**Worked revision:** replace ambiguous “closed” with the specific recorded
state; expose the evidence and accessible correction route; announce updated
status to assistive technology; retain a non-AI fallback. In the fictional
case, the correction control initially fails keyboard access. Fix it and
repeat that task and adjacent navigation. Do not label it resolved solely
because code changed.

- Finding in the participant's meaning:
- Selected change and rejected alternative, with reason:
- Owner:
- Retest task and result, or explicitly pending evidence:
- What participants are told about the decision:
- Next monitoring point and condition for stopping or narrowing AI:

**Learning check:** explain why the selected path fits the user's activity,
which evidence changed your decision, and what new observation could reverse
it. Then apply the method to a different task. A completed worksheet is a
reasoning record, not proof of human learning or production readiness.

## Sources and further practice

Primary references, accessed September 23, 2026:

- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Nielsen's usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [NIST AI Risk Management Framework](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
- [LIME paper](https://arxiv.org/abs/1602.04938)
- [SHAP documentation](https://shap.readthedocs.io/en/latest/)

Use the [Whole-Task Evidence Record](reader-action-workbook.md) and
[Almost-Right Tax Ledger](almost-right-tax-ledger.md) to continue measuring the
chosen path. Report a problem through [Errata](../ERRATA.md) without including
participant identities or confidential research records.
