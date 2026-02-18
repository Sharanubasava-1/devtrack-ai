# Prompting Rules for AI Agents

AI agents must follow these output constraints.

## Output format

AI must generate structured, deterministic code.

No ambiguous or partial code allowed.

## Safety requirements

AI must NOT:

- modify database schema without migration
- remove validation logic
- remove error handling

## Stability rules

AI changes must be:

- backward compatible
- minimal
- isolated

## Verification requirement

Generated code must:

- compile
- run without errors
- maintain API contract integrity
