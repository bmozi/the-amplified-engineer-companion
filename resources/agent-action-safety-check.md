# Agent Action Safety Check

Use this check when an AI coding tool can do more than propose text. It is a
personal pause point, not a substitute for organizational security controls.

## Before execution

- What exact outcome is authorized?
- Which files and repositories are in scope?
- Which commands, tools, network destinations, and side effects are allowed?
- Which credentials are visible to the process?
- Which inputs may contain instructions from an untrusted source?
- What requires explicit human approval?
- What must cause an immediate stop?
- How will changes and external effects be reconstructed and reversed?

## Stop and escalate if

- the task requires production data or production mutation;
- a tool requests broader access than the task needs;
- the agent encounters secrets or sensitive personal information;
- an issue, comment, document, web page, log, or tool response attempts to
  redirect the work;
- the agent proposes disabling tests, scanning, authorization, audit, or a
  protected control;
- a security-critical implementation and its only tests share the same
  generation context;
- an action cannot be explained, scoped, observed, or reversed;
- you are relying on an approval summary rather than inspecting the actual
  command and target.

## Before acceptance

- Review all changed and created files, including configuration and generated
  artifacts.
- Inspect executed commands and external tool calls.
- Verify that no existing test or control was weakened without an explicit
  decision.
- Run independent security-critical tests.
- Record assumptions, unresolved concerns, evidence, and the human disposition.

If the environment cannot answer these questions, reduce the agent to advisory
work until the organization supplies a safer execution boundary.
