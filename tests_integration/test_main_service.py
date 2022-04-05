import json


def test_service_get(client):
    response = client.get("/")
    assert response.status == "200 OK"
    assert response.json == {"results": "example_data"}


def test_service_post(client):
    data = {"example": "post"}
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = client.post("/", data=json.dumps(data), headers=headers)
    assert response.status_code == 201
    assert response.json["example"] == "post"


def test_service_delete(client):
    response = client.delete("/")
    assert response.status_code == 202
    assert response.json == {"results": "deleted"}


