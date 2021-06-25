from flask import Blueprint
from flask_restx import Resource, Api
from src.api.employees.actions import EmployeeActions

employees_blueprint = Blueprint('employees', __name__)
api = Api(employees_blueprint)


class EmployeesList(Resource):
    def get(self):
        employee_action = EmployeeActions()
        employees = employee_action.get_all_employees()
        if not employees:
            api.abort(404, f"Employees database is empty")
        return employees, 200


class Employees(Resource):
    def get(self, employee_id):
        employee_action = EmployeeActions()
        employee = employee_action.get_employee_by_id(employee_id)
        if not employee:
            print('aqui')
            api.abort(404, f"Employee {employee_id} does not exist")
        return employee, 200


api.add_resource(EmployeesList, '/employees')
api.add_resource(Employees, '/employees/<int:employee_id>')

