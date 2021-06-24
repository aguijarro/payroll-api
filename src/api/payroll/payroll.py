from flask import Blueprint
from flask_restx import Resource, Api

payroll_blueprint = Blueprint('payroll', __name__)
api = Api(payroll_blueprint)


class PayRoll(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'Salary!'
        }


api.add_resource(PayRoll, '/payroll')
