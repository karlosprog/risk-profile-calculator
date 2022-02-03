from src.helper.constshelper import ConstsHelper
from src.model.riskprofile import RiskProfile
from src.rules.ruleinterface import RuleInterface


class UserIsMarriedRule(RuleInterface):
    def apply(self, risk_profile: RiskProfile):
        marital_status = risk_profile.personal_information.marital_status
        if marital_status == ConstsHelper.MARRIED:
            risk_profile.disability_score = risk_profile.disability_score - 1
            risk_profile.life_score = risk_profile.life_score + 1

