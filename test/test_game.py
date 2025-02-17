import requests

def test_welcome():
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200

def test_invalid_move():
    response = requests.post("http://localhost:5000/move", json={"current_room": "start", "direction": "south"})
    assert response.status_code == 400

def test_valid_move():
    response = requests.post("http://localhost:5000/move", json={"current_room": "start", "direction": "north"})
    assert response.status_code == 200
