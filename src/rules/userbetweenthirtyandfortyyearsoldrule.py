from src.model.riskprofile import RiskProfile
from src.rules.ruleinterface import RuleInterface


class UserBetweenThirtyAndFortyYearsOldRule(RuleInterface):
    def apply(self, risk_profile: RiskProfile):
        age = risk_profile.personal_information.age
        if 30 <= age <= 40:
            risk_profile.auto_score = risk_profile.auto_score - 1
            risk_profile.disability_score = risk_profile.disability_score - 1
            risk_profile.home_score = risk_profile.home_score - 1
            risk_profile.life_score = risk_profile.life_score - 1
