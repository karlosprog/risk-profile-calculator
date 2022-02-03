from src.helper.constshelper import ConstsHelper
from src.model.riskprofile import RiskProfile
from src.rules.incomeisabovetwohundredrule import IncomeIsAboveTwoHundredRule
from src.rules.userdoesnothavehouserule import UserDoesNotHaveHouseRule
from src.rules.userdoesnothaveincomerule import UserDoesNotHaveIncome
from src.rules.userdoesnothavevehiclerule import UserDoesNotHaveVehicleRule
from src.rules.userhasdependentsrule import UserHasDependentsRule
from src.rules.userhouseismortgagedrule import UserHouseIsMortgagedRule
from src.rules.userismarriedrule import UserIsMarriedRule
from src.rules.useroversistyyearsoldrule import UserOverSixtyYearsOldRule
from src.rules.userunderthirtyyearsoldrule import UserUnderThirtyYearsOldRule
from src.rules.uservehicleproducedlastfiveyearsrule import UserVehicleProducedLastFiveYearsRule

''' 
Service implemented using the Rule Pattern.
Every business rule must be implemented in a new class that implements the RuleInterface.
'''
class RuleService:
    def __init__(self):
        self.rule_list = []
        self.rule_list.append(UserDoesNotHaveIncome())
        self.rule_list.append(UserDoesNotHaveVehicleRule())
        self.rule_list.append(UserDoesNotHaveHouseRule())
        self.rule_list.append(UserOverSixtyYearsOldRule())
        self.rule_list.append(UserUnderThirtyYearsOldRule())
        self.rule_list.append(IncomeIsAboveTwoHundredRule())
        self.rule_list.append(UserHouseIsMortgagedRule())
        self.rule_list.append(UserHasDependentsRule())
        self.rule_list.append(UserIsMarriedRule())
        self.rule_list.append(UserVehicleProducedLastFiveYearsRule())

    def apply_rules(self, risk_profile: RiskProfile):
        for rule in self.rule_list:
            rule.apply(risk_profile)
        self.calc_final_score(risk_profile)

    def calc_final_score(self, risk_profile: RiskProfile):
        self.calc_score(risk_profile, 'auto', risk_profile.auto_score)
        self.calc_score(risk_profile, 'disability', risk_profile.disability_score)
        self.calc_score(risk_profile, 'home', risk_profile.home_score)
        self.calc_score(risk_profile, 'life', risk_profile.life_score)

    def calc_score(self, risk_profile: RiskProfile, score_type_name, score_value):
        current_value = getattr(risk_profile, score_type_name)
        if current_value == ConstsHelper.INELIGIBLE:
            return
        if score_value <= 0:
            setattr(risk_profile, score_type_name, ConstsHelper.ECONOMIC)
        elif score_value == 1 or score_value == 2:
            setattr(risk_profile, score_type_name, ConstsHelper.REGULAR)
        elif score_value >= 3:
            setattr(risk_profile, score_type_name, ConstsHelper.RESPONSIBLE)
