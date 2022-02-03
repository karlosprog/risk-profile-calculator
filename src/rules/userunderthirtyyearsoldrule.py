from src.model.riskprofile import RiskProfile
from src.rules.ruleinterface import RuleInterface


class UserUnderThirtyYearsOldRule(RuleInterface):
    def apply(self, risk_profile: RiskProfile):
        if risk_profile.personal_information.age < 30:
            risk_profile.auto_score = risk_profile.auto_score - 2
            risk_profile.disability_score = risk_profile.disability_score - 2
            risk_profile.home_score = risk_profile.home_score - 2
            risk_profile.life_score = risk_profile.life_score - 2
