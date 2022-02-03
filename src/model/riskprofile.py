class RiskProfile:
    def __init__(self, p_personal_information):
        self.personal_information = p_personal_information
        base_score = self.calc_base_score(p_personal_information.risk_questions)
        self.auto = ""
        self.auto_score = 0
        self.disability = ""
        self.disability_score = 0
        self.home = ""
        self.home_score = 0
        self.life = ""
        self.life_score = 0

    def calc_base_score(self, risk_questions):
        total = 0
        for risk in risk_questions:
            total = total + risk

        return total


