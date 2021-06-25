import requests

from src.api.employees.schemas import EmployeeMessage
from pydantic import ValidationError


class EmployeeDatabase:
    def __init__(self):
        r = requests.get('http://masglobaltestapi.azurewebsites.net/api/employees')
        self.data = r.json()

    def get_employee_data(self):
        employee_messages = []
        for employee in self.data:
            try:
                employee_messages.append(EmployeeMessage(**employee).dict())
            except ValidationError as e:
                print(e.json())
        return employee_messages
