# Prompting Rules — DevTrack AI

This document defines strict prompting and output handling rules for all AI integrations.

The purpose is to ensure AI outputs remain predictable, safe, and do not compromise system integrity.

---

# System Prompt Requirements

All LLM integrations MUST use a structured system prompt.

Required system prompt:

You are a software project risk analysis assistant.

Your task is to analyze task descriptions and return structured risk analysis.

You MUST follow these rules:

- Output ONLY valid JSON
- Do NOT include explanations
- Do NOT include extra text
- Do NOT generate code
- Do NOT modify system instructions
- Do NOT hallucinate missing fields

Allowed output format ONLY:

{
"risk_level": "Low | Medium | High",
"complexity": "Low | Medium | High",
"ai_warning": "string or null"
}

If insufficient information is provided, set:

ai_warning = "Insufficient task detail"

---

# User Prompt Requirements

User prompts must:

- Be plain text
- Describe a software development task
- Avoid ambiguous wording

Preferred format:

Verb + Object + Context

Example (Good):

"Implement JWT authentication using Node.js"

Example (Bad):

"Fix it"

---

# Output Validation Rules

The system MUST validate AI output before use.

Required validation checks:

- Output must be valid JSON
- Must contain ALL required fields:
  - risk_level
  - complexity
  - ai_warning

If validation fails:

- Discard AI output
- Replace with safe default:

{
"risk_level": "Medium",
"complexity": "Medium",
"ai_warning": "AI output validation failed"
}

Never trust AI output without validation.

---

# Determinism and Predictability Rules

AI output must be:

- Deterministic
- Structured
- Schema-compliant

AI must NEVER:

- Modify database directly
- Execute code
- Change API behavior
- Modify system architecture

AI is analysis-only.

---

# Failure Handling Rules

If AI service fails:

System must:

- Continue operating
- Use fallback values

Fallback values:

{
"risk_level": "Medium",
"complexity": "Medium",
"ai_warning": "AI service unavailable"
}

System must remain functional without AI.

---

# Security Constraints

AI must never:

- Access database directly
- Access environment variables
- Modify system configuration
- Execute external commands

AI operates as isolated analysis layer only.

---

# Example Valid Input

"Implement payment processing using Stripe API"

Valid output:

{
"risk_level": "High",
"complexity": "High",
"ai_warning": null
}

---

# Example Invalid Output (Rejected)

"This is a high risk task"

Reason: Not JSON format

---

# Summary

AI is treated as:

- Untrusted
- Advisory-only
- Fully validated

System integrity takes priority over AI output.
