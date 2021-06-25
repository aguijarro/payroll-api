# src/tests/test_employees.py


import json


def test_employees(test_app):
    # Given
    client = test_app.test_client()
    # When
    resp = client.get('/employees')
    data = json.loads(resp.data.decode())
    # Then
    assert resp.status_code == 200
    assert len(data) == 2


def test_single_employee(test_app):
    # Given
    employee_id = 1
    # When
    client = test_app.test_client()
    resp = client.get(f'/employees/{employee_id}')
    data = json.loads(resp.data.decode())
    # Then
    assert resp.status_code == 200
    assert 1 == data['id']
    assert 'Andrea' == data['name']
    assert 'HourlySalaryEmployee' == data['contractTypeName']
    assert 1 == data['roleId']
    assert 'Administrator' == data['roleName']
    assert data['roleDescription'] is None
    assert 10000.0 == data['hourlySalary']
    assert 50000.0 == data['monthlySalary']


