# from profilemodels import personalInformationModel


class PersonalInformation:
    def __init__(self):
        self.age = 0
        self.dependents = 0
        self.house = {'ownership_status': ''}
        self.income = 0
        self.marital_status = ""
        self.risk_questions = [0, 0, 0]
        self.vehicle = {'year': 2018}

    def from_model(self, model):
        self.age = model['age']
        self.dependents = model['dependents']
        self.house = model['house']
        self.income = model['income']
        self.marital_status = model['marital_status']
        self.risk_questions = model['risk_questions']
        self.vehicle = model['vehicle']
