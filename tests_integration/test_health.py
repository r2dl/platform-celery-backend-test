def test_health(client):
    response = client.get("/health")
    assert response.status == "200 OK"
    assert response.json == {"health_check": "passed"}
