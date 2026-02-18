# AI Agent System Boundaries

This document defines strict constraints for AI agents modifying this repository.

## Allowed modifications

AI agents may modify:

- frontend/components/
- frontend/pages/
- backend/routes/
- backend/schemas/

## Restricted modifications

AI agents MUST NOT modify:

- backend/models/task_model.py
- database schema
- validation rules
- docker-compose.yml

Schema changes require explicit human approval.

## Required guarantees

AI-generated code MUST:

- preserve API contracts
- maintain backward compatibility
- not break existing endpoints
- include error handling

## Validation requirement

All new inputs must be validated using Marshmallow schemas.

AI agents must never bypass validation.

## Failure safety

If AI is unsure, it must:

- return existing behavior
- not introduce breaking changes
