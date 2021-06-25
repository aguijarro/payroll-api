class PayrollSystem:
    def __init__(self, employees):
        self.employees = employees

    def get_payroll_data(self):
        for index, employee in enumerate(self.employees):
            if employee['contractTypeName'] == 'HourlySalaryEmployee':
                self.employees[index]['annual_salary'] = 120 * employee['hourlySalary'] * 12
            else:
                self.employees[index]['annual_salary'] = 120 * employee['monthlySalary'] * 12

        return self.employees
