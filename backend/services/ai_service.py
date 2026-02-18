class AIService:
    def analyze_task(self, description, deadline=None):
        risk_level = "Low"
        complexity = "Low"
        warnings = []

        # Safe lowercase conversion
        description_lower = description.lower().strip() if description else ""

        # HIGH RISK KEYWORDS (expanded)
        high_risk_keywords = [
            "payment",
            "security",
            "auth",
            "authentication",
            "authorization",
            "login",
            "signup",
            "jwt",
            "token",
            "encrypt",
            "money",
            "transfer",
            "database",
            "migration",
            "production",
            "credential",
            "password"
        ]

        # MEDIUM RISK KEYWORDS
        medium_risk_keywords = [
            "api",
            "service",
            "deploy",
            "update",
            "refactor",
            "integration",
            "backend"
        ]

        # RISK DETECTION (High priority first)
        if description_lower:
            for keyword in high_risk_keywords:
                if keyword in description_lower:
                    risk_level = "High"
                    break

            # Only check medium if still Low
            if risk_level == "Low":
                for keyword in medium_risk_keywords:
                    if keyword in description_lower:
                        risk_level = "Medium"
                        break

        # HIGH COMPLEXITY KEYWORDS
        high_complexity_keywords = [
            "system",
            "architecture",
            "engine",
            "integrate",
            "integration",
            "full-stack",
            "platform",
            "microservice",
            "scalable"
        ]

        # MEDIUM COMPLEXITY KEYWORDS
        medium_complexity_keywords = [
            "feature",
            "component",
            "page",
            "endpoint",
            "cache",
            "module",
            "implementation"
        ]

        # COMPLEXITY DETECTION
        if description_lower:
            for keyword in high_complexity_keywords:
                if keyword in description_lower:
                    complexity = "High"
                    break

            if complexity == "Low":
                for keyword in medium_complexity_keywords:
                    if keyword in description_lower:
                        complexity = "Medium"
                        break

        # Missing Information Checks
        if not deadline:
            warnings.append("No deadline specified")

        if not description_lower:
            warnings.append("Description is empty")

        return {
            "risk_level": risk_level,
            "complexity": complexity,
            "ai_warning": ", ".join(warnings) if warnings else None
        }


# Singleton instance
ai_service = AIService()