from src.model.riskprofile import RiskProfile
from src.rules.ruleinterface import RuleInterface


class IncomeIsAboveTwoHundredRule(RuleInterface):
    def apply(self, risk_profile: RiskProfile):
        if risk_profile.personal_information.income > 200:
            risk_profile.auto_score = risk_profile.auto_score - 1
            risk_profile.disability_score = risk_profile.disability_score - 1
            risk_profile.home_score = risk_profile.home_score - 1
            risk_profile.life_score = risk_profile.life_score - 1

