from src.api.employees.models import EmployeeDatabase
from src.api.employees.business_logics import PayrollSystem


class EmployeeActions:
    def __init__(self):
        employee_database = EmployeeDatabase()
        payroll_employee = PayrollSystem(employee_database.get_employee_data())
        self.employee_data = payroll_employee.get_payroll_data()

    def get_all_employees(self):
        return self.employee_data

    def get_employee_by_id(self, employee_id):
        employee = [employee for employee in self.employee_data if employee['id'] == employee_id]
        if not employee:
            return None
        return employee[0]

