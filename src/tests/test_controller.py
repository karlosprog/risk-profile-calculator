import json


def test_calc_risk_profile_by_example(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/api/1/RiskProfileCalculator/risk-profile/',
        data=json.dumps({
            "age": 35,
            "dependents": 2,
            "house": {"ownership_status": "owned"},
            "income": 0,
            "marital_status": "married",
            "risk_questions": [0, 1, 0],
            "vehicle": {"year": 2018}
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'regular' in data['auto']
    assert 'ineligible' in data['disability']
    assert 'economic' in data['home']
    assert 'regular' in data['life']


def test_calc_risk_profile_is_ineligible_all(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/api/1/RiskProfileCalculator/risk-profile/',
        data=json.dumps({
            "age": 80,
            "dependents": 2,
            "house": {},
            "income": 0,
            "marital_status": "married",
            "risk_questions": [0, 1, 0],
            "vehicle": {}
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'ineligible' in data['auto']
    assert 'ineligible' in data['disability']
    assert 'ineligible' in data['home']
    assert 'ineligible' in data['life']


def test_calc_risk_profile_user_does_not_have_income_vehicles_houses(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/api/1/RiskProfileCalculator/risk-profile/',
        data=json.dumps({
            "age": 20,
            "dependents": 2,
            "house": {},
            "income": 0,
            "marital_status": "married",
            "risk_questions": [0, 1, 0],
            "vehicle": {}
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'ineligible' in data['auto']
    assert 'ineligible' in data['disability']
    assert 'ineligible' in data['home']
    assert 'economic' in data['life']


def test_calc_risk_profile_user_is_over_sixty_years_old(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/api/1/RiskProfileCalculator/risk-profile/',
        data=json.dumps({
            "age": 61,
            "dependents": 20,
            "house": {"ownership_status": "owned"},
            "income": 8000,
            "marital_status": "married",
            "risk_questions": [0, 1, 0],
            "vehicle": {"year": 2018}
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'economic' in data['auto']
    assert 'ineligible' in data['disability']
    assert 'economic' in data['home']
    assert 'ineligible' in data['life']


def test_calc_risk_profile_is_under_thirty_years_old(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/api/1/RiskProfileCalculator/risk-profile/',
        data=json.dumps({
            "age": 20,
            "dependents": 2,
            "house": {"ownership_status": "owned"},
            "income": 0,
            "marital_status": "married",
            "risk_questions": [0, 1, 0],
            "vehicle": {"year": 2018}
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'economic' in data['auto']
    assert 'ineligible' in data['disability']
    assert 'economic' in data['home']
    assert 'economic' in data['life']


def test_calc_risk_profile_user_income_is_above_two_hundred(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/api/1/RiskProfileCalculator/risk-profile/',
        data=json.dumps({
            "age": 35,
            "dependents": 0,
            "house": {"ownership_status": "owned"},
            "income": 150,
            "marital_status": "single",
            "risk_questions": [0, 1, 0],
            "vehicle": {"year": 2014}
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'economic' in data['auto']
    assert 'economic' in data['disability']
    assert 'economic' in data['home']
    assert 'economic' in data['life']


def test_calc_risk_profile_user_house_is_mortgaged(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/api/1/RiskProfileCalculator/risk-profile/',
        data=json.dumps({
            "age": 61,
            "dependents": 0,
            "house": {"ownership_status": "mortgaged"},
            "income": 2050,
            "marital_status": "single",
            "risk_questions": [1, 1, 1],
            "vehicle": {"year": 2020}
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'economic' in data['auto']
    assert 'ineligible' in data['disability']
    assert 'economic' in data['home']
    assert 'ineligible' in data['life']


def test_calc_risk_profile_user_has_dependents(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/api/1/RiskProfileCalculator/risk-profile/',
        data=json.dumps({
            "age": 33,
            "dependents": 2,
            "house": {"ownership_status": "owned"},
            "income": 9000,
            "marital_status": "married",
            "risk_questions": [0, 1, 1],
            "vehicle": {"year": 2019}
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'economic' in data['auto']
    assert 'economic' in data['disability']
    assert 'economic' in data['home']
    assert 'regular' in data['life']


def test_calc_risk_profile_user_is_married(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/api/1/RiskProfileCalculator/risk-profile/',
        data=json.dumps({
            "age": 33,
            "dependents": 2,
            "house": {"ownership_status": "mortgaged"},
            "income": 0,
            "marital_status": "married",
            "risk_questions": [0, 0, 0],
            "vehicle": {"year": 2000}
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'economic' in data['auto']
    assert 'ineligible' in data['disability']
    assert 'regular' in data['home']
    assert 'regular' in data['life']


def test_calc_risk_profile_user_vehicle_was_produced_last_five_years(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/api/1/RiskProfileCalculator/risk-profile/',
        data=json.dumps({
            "age": 90,
            "dependents": 0,
            "house": {"ownership_status": "owned"},
            "income": 1000,
            "marital_status": "single",
            "risk_questions": [0, 0, 0],
            "vehicle": {"year": 2020}
        }),
        content_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'economic' in data['auto']
    assert 'ineligible' in data['disability']
    assert 'economic' in data['home']
    assert 'ineligible' in data['life']


def test_calc_risk_profile_with_wrong_address_must_fail(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/api/1/RiskProfileCalculator/risk-profilexxxx/',
        data=json.dumps({
            "age": 90,
            "dependents": 0,
            "house": {"ownership_status": "owned"},
            "income": 1000,
            "marital_status": "single",
            "risk_questions": [0, 0, 0],
            "vehicle": {"year": 2020}
        }),
        content_type='application/json',
    )
    assert resp.status_code != 200


def test_calc_risk_profile_with_wrong_address_must_fail(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/api/1/RiskProfileCalculator/risk-profilexxxx/',
        data=json.dumps({
            "age": 90,
            "dependents": 0,
            "house": {"ownership_status": "owned"},
            "income": 1000,
            "marital_status": "single",
            "risk_questions": [0, 0, 0],
            "vehicle": {"year": 2020}
        }),
        content_type='application/json',
    )
    assert resp.status_code != 200