def test_service(client):
    response = client.get("/service")
    assert response.status == "200 OK"
    assert "results" in response.json
    assert isinstance(response.json["results"], list)
