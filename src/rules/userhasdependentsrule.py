from src.model.riskprofile import RiskProfile
from src.rules.ruleinterface import RuleInterface


class UserHasDependentsRule(RuleInterface):
    def apply(self, risk_profile: RiskProfile):
        if risk_profile.personal_information.dependents > 0:
            risk_profile.disability_score = risk_profile.disability_score + 1
            risk_profile.life_score = risk_profile.life_score + 1

