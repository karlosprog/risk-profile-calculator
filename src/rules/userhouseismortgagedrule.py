from src.helper.constshelper import ConstsHelper
from src.model.riskprofile import RiskProfile
from src.rules.ruleinterface import RuleInterface


class UserHouseIsMortgagedRule(RuleInterface):
    def apply(self, risk_profile: RiskProfile):
        if len(risk_profile.personal_information.house) == 0:
            return
        ownership_status = risk_profile.personal_information.house['ownership_status']
        if ownership_status == ConstsHelper.MORTGAGED:
            risk_profile.disability_score = risk_profile.disability_score + 1
            risk_profile.home_score = risk_profile.home_score + 1

