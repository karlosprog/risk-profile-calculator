from src.helper.constshelper import ConstsHelper
from src.model.riskprofile import RiskProfile
from src.rules.ruleinterface import RuleInterface


class UserDoesNotHaveIncome(RuleInterface):
    def apply(self, risk_profile: RiskProfile):
        user_income = risk_profile.personal_information.income

        if user_income <= 0:
            risk_profile.disability = ConstsHelper.INELIGIBLE

