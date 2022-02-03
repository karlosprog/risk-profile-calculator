from src.helper.constshelper import ConstsHelper
from src.model.riskprofile import RiskProfile
from src.rules.ruleinterface import RuleInterface


class UserDoesNotHaveHouseRule(RuleInterface):
    def apply(self, risk_profile: RiskProfile):
        user_has_house = len(risk_profile.personal_information.house) > 0

        if not user_has_house:
            risk_profile.home = ConstsHelper.INELIGIBLE
