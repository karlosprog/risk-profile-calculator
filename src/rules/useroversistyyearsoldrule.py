from src.helper.constshelper import ConstsHelper
from src.model.riskprofile import RiskProfile
from src.rules.ruleinterface import RuleInterface


class UserOverSixtyYearsOldRule(RuleInterface):
    def apply(self, risk_profile: RiskProfile):
        if risk_profile.personal_information.age > 60:
            risk_profile.disability = ConstsHelper.INELIGIBLE
            risk_profile.life = ConstsHelper.INELIGIBLE
