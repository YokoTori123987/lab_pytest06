from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, '../lab_pytest06')        
from main import app

client = TestClient(app)

def test_call_test_api():
    input = "2540"
    output = 25
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}

# def test_call_api():
#     input = "A"
#     output = "no"
#     response = client.get("/service/getage/str?year="+input)
#     assert response.status_code == 200
#     assert response.json() == {"age": input + output}
