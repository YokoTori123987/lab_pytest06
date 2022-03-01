from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, '../lab_pytest06')        
from main import app

client = TestClient(app)

def test_call_test_input_year_api():
    input = "2540"
    output = 25
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}

def test_call_test_input_zero_api():
    input = "0"
    output = "Can't input less than zero"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}

def test_call_test_input_year_a_api():
    input = "2566"
    output = "Can't input less than zero"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}
