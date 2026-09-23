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

## Begin with a human outcome

Use Chapter 2's intent questions before proposing a feature. State who needs
what outcome, the circumstances that constrain them, and what would count as
success. Separate observation from assumption. Keep both the outcome and the
solution revisable when research exposes a mistake.

**Practice:** a college requests a chatbot because working students miss support
appointments. Interviews suggest the available appointment hours conflict with
students' shifts. Compare clearer booking instructions, different service
hours, and an AI-assisted route. What evidence would distinguish inability to
find an appointment from inability to attend it?

**Suggested reasoning:** first verify the scheduling constraint with affected
students and service staff. A chatbot may help discovery but cannot create
staff availability by itself. Define success as receiving the needed support
under feasible conditions, then test the service arrangement as well as the
interface. Do not treat chatbot use as proof that the student's need was met.
This is a fictional exercise, not a finding about an actual college.

## Decide who receives the time

Use with Chapter 10. All figures below are invented weekly totals for a
comparable workload meeting the same acceptance criteria. They illustrate
allocation, not a measured saving or a prediction for your team.

| Work | Current path | AI-assisted path |
|---|---:|---:|
| Prepare changes | 30 hours | 20 hours |
| Review and repair | 10 hours | 18 hours |
| Complete staff effort | 40 hours | 38 hours |

The manager proposes ten additional hours of delivery commitments. A junior
engineer needs two hours of supervised practice. The reviewer is already
handling an after-hours queue. Staff have differing constraints outside work;
none should have to disclose private circumstances in this exercise.

Before reading the interpretation:

1. Calculate net capacity. Whose workload falls and whose rises?
2. Explain why a team total cannot establish that the review queue is manageable.
3. Propose an allocation and name what commitment must change to make it real.
4. Define the evidence and review date that would make you revise it.

**Suggested interpretation:** preparation falls by ten hours while review rises
by eight, leaving two hours of net staff capacity. Ten new hours of commitments
would overallocate the stated saving by eight. First address the reviewer
bottleneck: redistribute qualified work, improve the workflow, reduce scope, or
hold expansion. The two-hour practice session also needs a mentor and usable
calendar time. Count both people's effort; one hour together consumes two staff
hours. The aggregate saving does not establish that either person is available.

A defensible decision is to hold the delivery increase, schedule a bounded
learning session by explicitly reducing another commitment, and review queue
age, rework, accepted outcomes, and after-hours load at the next checkpoint.
Another allocation may be justified; explain whose needs it serves and what
it defers. Do not silently finance the plan with personal time.

**Changed assumption:** the assisted review total falls from eighteen to twelve
hours without reducing quality or changing the workload. Net capacity is now
eight hours. Reconsider the allocation, but verify that the reduction is real
and schedulable. It still does not decide how much should go to delivery,
learning, or reducing overload. That requires an accountable decision with
affected people.

Record the beneficiary, shifted burden, selected allocation, displaced
commitment, owner, review date, and evidence that could reverse the decision.
Treat capability requirements and justified non-use separately from enthusiasm
or tool activity. This is leadership practice, not an assertion of employment
law or a guarantee of an unchanged role.

## Trace privacy, authority, and wider harm

Use Chapter 16's data and consequence review. Stay with synthetic records for
this exercise. The following proposed extensions are fictional:

- Retain all dispute messages indefinitely “for future training.”
- Rank customers by repeated help requests and staff by time spent per case.
- Accept a familiar-sounding voice message as authority to change payment details.

For each proposal, identify the legitimate outcome, necessary data, possible
harm, a less intrusive alternative, and the decision owner. Map collection,
model/provider access, logs, stored outputs, recipients, retention, and deletion.
Include access isolation, protected storage/transmission, and an incident route.
Name what privacy or legal review must resolve before real data is used.

**Suggested reasoning:** an unspecified future purpose does not justify
indefinite retention. A masked message may still identify someone through its
content or linked records. Help frequency and handling time may reflect
accessibility barriers or case complexity; using them to penalize people could
compound an existing disadvantage. A recognizable voice may be synthetic.
Verify a consequential instruction through an established authenticated route;
retain the block on refund execution in this case.

A practical test record names **input, expected protection, observed result,
owner, and unresolved risk**. For example:

- Ask for another account's records: access must be denied independently of
  what the model says.
- Request deletion: trace covered copies and derived stores; identify any
  required retention exception or provider limitation rather than promising
  universal erasure.
- Submit generated evidence: preserve its status as unverified, retain the
  source distinction, and require the applicable authentication or review.
- Challenge a classification: the person must have a usable correction route
  to someone able to change the decision.

Encryption and access controls do not settle whether collection or profiling
is appropriate. An anonymity claim needs evidence about re-identification risk.
Have qualified owners resolve applicable legal obligations; a completed
worksheet does not establish compliance.

**Transfer:** change the system to a job-opportunity recommender or a public
information feed. Who might repeatedly lose visibility? Could personalization
reinforce exclusion or narrow the information people encounter? Could generated
content mislead people about who said something? Name a relevant measure,
mitigation, and stop condition. Consider autonomy and well-being without
inferring mental health from activity counts. Compare a proposed benefit with
its distribution across people, not only an overall average.

## Harder case: protection that can also exclude

A fictional payment service must choose its next fraud-review pilot. The goal
is to reduce unauthorized transfers while allowing legitimate customers to
complete urgent payments. This is a separate practice case; it does not expand
Meridian's dispute assistant's authority. Every number below is invented for
reasoning, not a product benchmark or a claim about a population.

The team replays three approaches against the same 1,000 historical transfer
requests. Later investigation labeled 40 as unauthorized and 960 as legitimate.
For this exercise, assume those labels are correct. In real work, challenge
label quality and how the cases were selected. Each request receives one
classification per approach; “flagged” means routed for review, not proven fraud.

| Approach | Unauthorized requests flagged | Legitimate requests flagged | Total review cases |
|---|---:|---:|---:|
| A: existing transaction rules | 20 of 40 | 30 of 960 | 50 |
| B: AI using transaction fields already permitted for review | 28 of 40 | 52 of 960 | 80 |
| C: AI also using persistent device and location histories | 34 of 40 | 106 of 960 | 140 |

For this exercise, plan a pilot window of 1,000 requests with the replay’s case
mix; verify that workload assumption before real deployment. The window has
capacity for 80 reviews. Assume comparable effort per case
for this first calculation. The replay says nothing about actual queue times,
prevented losses, reviewer decisions, or customer experience. An unflagged
unauthorized request is a miss in this replay; it is not a measured loss.

A volunteer usability session adds conflicting evidence. Some participants
value the extra protection. Two people who share a device could not complete
the proposed verification step without assistance. One participant feared a
legitimate urgent payment would miss its deadline. These observations expose
failure paths; the small, self-selected session cannot estimate how common
they are. The replay has no reliable subgroup breakdown, and dollar severity
is not supplied. C's additional data collection has not received privacy review.

For a live pilot, a flag could prompt a staffed check or a temporary hold.
Either can burden legitimate customers. A hold may protect against a transfer
that cannot be recovered, but “temporary” is not a sufficient limit: specify
who resolves it, by when, and what happens if the queue is unavailable. Do not
assume that an explanation, consent screen, or human approval removes the harm.

### Make the decision before reading the reasoning

1. Calculate missed unauthorized requests, review-capacity use, and additional
   legitimate flags for each approach. State which benefits the replay cannot
   establish. Do not collapse the decision into one accuracy number.
2. Choose a next step: retain A while repairing verification, test B within a
   defined boundary, investigate C without live consequences, or propose a
   different bounded combination. Name the evidence your choice lacks.
3. Define permitted data, the action a flag may trigger, maximum unresolved
   delay, an accessible correction route, and who can suspend the pilot. State
   what happens when review capacity is exhausted. A hybrid needs fresh testing;
   its results cannot be inferred by adding the rows above.
4. Explain who benefits and who bears costs. Give the strongest objection an
   affected customer, reviewer, and privacy owner could make to your choice.
   Identify one observation that would reverse your decision.

### Worked reasoning: a conditional choice

A misses 20 labeled unauthorized requests, B misses 12, and C misses 6. Their
review demand is 50, 80, and 140 cases. Relative to A, B flags eight more
unauthorized requests and 22 more legitimate requests. C flags six more
unauthorized requests than B but 54 more legitimate requests and requires 60
reviews beyond capacity. Flags found are not losses prevented. Different harm
severity, review effort, or customer constraints could change the judgment.

One defensible choice is a shadow evaluation of B with no new customer-facing
action, while retaining A's current process and repairing accessible
verification. B reaches the stated capacity ceiling with no buffer; a replay
cannot justify assuming that every review will fit a live window. Measure
actual handling time and bursts, resolve the failed verification path with
users, and obtain the applicable privacy review before introducing a new hold.
The owner of the pilot must define the release conditions and a tested fallback.
Shadow evaluation still needs permitted data use and protected records. Budget
its analysis separately from live review: shared staffing requires a smaller
shadow sample or additional capacity, not double-counting the same reviewers.

The strongest objection is that waiting leaves additional unauthorized
requests undetected by the live rules. That cost matters. If failures under A
are causing serious harm and a safely staffed, accessible route is available,
a limited live B pilot may be better justified. Its scope, hold deadline,
queue-overload response, and review authority need explicit evidence. Returning
to A on overload also restores A's misses; record that residual risk rather
than calling the fallback safe by definition.

C's better detection deserves investigation, but the current record cannot
justify live use. Its queue exceeds capacity, additional collection remains
unreviewed, and legitimate flags increase substantially. A narrower data design
or more capacity might change the case; neither improvement is established by
these numbers. Retaining A while repairing its worst failure may also be a
reasoned choice if the team cannot yet support B. State the harms accepted
during that interval and the deadline for reconsideration.

### Change the evidence

Now reduce review capacity from 80 to 55 during the pilot window. A fits only
under the equal-effort assumption; B exceeds capacity by 25 and C by 85.
Revise your choice before looking for a convenient new threshold. Threshold
changes alter both misses and legitimate flags and require another evaluation.
If you restrict the pilot, explain how cases are selected and who might lose
protection or access. Do not silently drop cases from the queue.

Then suppose capacity returns to 80, but user testing shows that the proposed
recovery route still excludes people using shared devices. Extra capacity does
not repair that barrier. Decide what must change before the affected path can
go live, and what protection remains available in the meantime.

A strong response uses the supplied arithmetic, distinguishes replay findings
from live outcomes, acknowledges the best objection, and connects each control
to a failure it can actually interrupt. Several decisions can meet that
standard. “Choose the most accurate model” and “always keep a human involved”
leave the central tradeoffs unresolved.

## Show what you can now justify

Apply the method to a new case before consulting the worked answers. Produce:

- a human outcome grounded in context, with assumptions still to test;
- a comparison including a credible conventional alternative;
- one privacy/data-flow record and one harm pathway affecting another person;
- controls justified by authority, consequence, and time to intervene;
- an accessible way to understand, challenge, and recover the result; and
- a decision with evidence, owner, limitation, and condition for revision.

Ask a colleague to change one assumption and challenge your decision. If the
reasoning no longer holds, revise it. Missing user evidence should remain
explicitly pending. This demonstrates a reasoning attempt; actual competence
requires feedback, repeated application, and evidence from real contexts.

## Sources and further practice

Primary references, accessed September 23, 2026:

- [NIST human-centered design overview](https://www.nist.gov/itl/iad/human-centered-technologies/human-factors-human-centered-design) — ISO-derived principles; page updated May 27, 2026 and marked no longer maintained.
- [Digital.gov HCD principles](https://digital.gov/guides/hcd/introduction/principles)
- [NIST Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1)
- [NIST de-identification guidance](https://csrc.nist.gov/pubs/ir/8053/final)
- [EDPB Opinion 28/2024](https://www.edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf)

- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [Nielsen's usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [NIST AI Risk Management Framework](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
- [LIME paper](https://arxiv.org/abs/1602.04938)
- [SHAP documentation](https://shap.readthedocs.io/en/latest/)

Use the [Whole-Task Evidence Record](reader-action-workbook.md) and
[Almost-Right Tax Ledger](almost-right-tax-ledger.md) to continue measuring the
chosen path. Report a problem through [Errata](../ERRATA.md) without including
participant identities or confidential research records.
