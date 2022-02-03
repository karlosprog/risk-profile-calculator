from src.helper.constshelper import ConstsHelper
from src.model.riskprofile import RiskProfile
from src.rules.ruleinterface import RuleInterface


class UserDoesNotHaveVehicleRule(RuleInterface):
    def apply(self, risk_profile: RiskProfile):
        user_has_vehicle = len(risk_profile.personal_information.vehicle) > 0

        if not user_has_vehicle:
            risk_profile.auto = ConstsHelper.INELIGIBLE
