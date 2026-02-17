class AIService:
    def analyze_task(self, description, deadline=None):
        risk_level = "Low"
        complexity = "Low"
        warnings = []

        description_lower = description.lower() if description else ""

        # Risk Analysis Rules
        high_risk_keywords = ["payment", "security", "auth", "authentication", "money", "transfer", "database", "migration", "production"]
        medium_risk_keywords = ["api", "service", "deploy", "update", "refactor"]
        
        if any(keyword in description_lower for keyword in high_risk_keywords):
            risk_level = "High"
        elif any(keyword in description_lower for keyword in medium_risk_keywords):
            risk_level = "Medium"

        # Complexity Analysis Rules
        high_complexity_keywords = ["system", "architecture", "engine", "integrate", "full-stack", "platform"]
        medium_complexity_keywords = ["feature", "component", "page", "endpoint", "cache"]

        if any(keyword in description_lower for keyword in high_complexity_keywords):
            complexity = "High"
        elif any(keyword in description_lower for keyword in medium_complexity_keywords):
            complexity = "Medium"
        
        # Missing Information Check
        if not deadline:
            warnings.append("No deadline specified")
        
        if not description:
             warnings.append("Description is empty")

        return {
            "risk_level": risk_level,
            "complexity": complexity,
            "ai_warning": ", ".join(warnings) if warnings else None
        }

ai_service = AIService()
