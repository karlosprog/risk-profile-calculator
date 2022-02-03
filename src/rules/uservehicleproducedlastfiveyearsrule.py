from src.model.riskprofile import RiskProfile
from src.rules.ruleinterface import RuleInterface
from datetime import date


class UserVehicleProducedLastFiveYearsRule(RuleInterface):
    def apply(self, risk_profile: RiskProfile):
        if len(risk_profile.personal_information.vehicle) == 0:
            return
        current_date = date.today()
        vehicle_year = risk_profile.personal_information.vehicle['year']
        if current_date.year - vehicle_year <= 5:
            risk_profile.auto_score = risk_profile.auto_score + 1

