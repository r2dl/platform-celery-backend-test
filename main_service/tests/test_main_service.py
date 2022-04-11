import json


def test_service_get(client):
    response = client.get("/")
    assert response.status_code == 200


#
# def test_service_post(client):
#     data = {"example": "post"}
#     headers = {"Content-Type": "application/json", "Accept": "application/json"}
#     response = client.post("/", data=json.dumps(data), headers=headers)
#     assert response.status_code == 201


def test_service_delete(client):
    response = client.delete("/")
    assert response.status_code == 202
