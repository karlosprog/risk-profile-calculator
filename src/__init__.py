import os
from flask import Flask, Blueprint
from flask_restx import Api, Resource, fields

from src.model.personalinformation import PersonalInformation
from src.model.riskprofile import RiskProfile
from src.services.ruleservice import RuleService
from flask_sqlalchemy import SQLAlchemy

# declaring global variables to expose the flask app instantiated
app = Flask(__name__)
api_v1 = Blueprint("api", __name__, url_prefix="/api/1")
api = Api(api_v1,
          version='1.0',
          title='Risk Profile Calculator API',
          description='Simple Risk Profile Calculator'
          )
app.register_blueprint(api_v1)
ns = api.namespace('RiskProfileCalculator', description='Risk Profile Calculator API')
rule_service = RuleService()

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)

# declaring models

personalInformationHouse = ns.model('PersonalInformationHouse', {
    'ownership_status': fields.String
})

personalInformationVehicle = ns.model('PersonalInformationVehicle', {
    'year': fields.Integer
})

personalInformationModel = ns.model('PersonalInformationModel', {
    'age': fields.Integer(readonly=False),
    'dependents': fields.Integer(readonly=False),
    'house': fields.Nested(personalInformationHouse),
    'income': fields.Integer(readonly=False),
    'marital_status': fields.String(readonly=False),
    'risk_questions': fields.List(fields.Integer),
    'vehicle': fields.Nested(personalInformationVehicle)
})

riskProfileModel = ns.model(
    "RiskProfile",
    {
        "auto": fields.String(required=True, description="The vehicle's score"),
        "disability": fields.String(required=True, description="The disability's score"),
        "home": fields.String(required=True, description="The home's score"),
        "life": fields.String(required=True, description="The life's score")
    }
)


# declaring class controllers below (as it has only 1 controller, I didn't create a file for each controller)

@ns.route('/risk-profile/')
class RiskProfileController(Resource):

    @ns.expect(personalInformationModel)
    @ns.marshal_with(riskProfileModel, code=200)
    def post(self):
        payload = ns.payload
        personal_information = PersonalInformation()
        personal_information.from_model(payload)
        risk_profile = RiskProfile(personal_information)
        rule_service.apply_rules(risk_profile)
        return risk_profile

