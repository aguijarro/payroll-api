# src/tests/test_payroll.py


import json


def test_payroll(test_app):
    # Given
    client = test_app.test_client()
    # When
    resp = client.get('/payroll')
    data = json.loads(resp.data.decode())
    # Then
    assert resp.status_code == 200
    assert 'Salary!' in data['message']
    assert 'success' in data['status']