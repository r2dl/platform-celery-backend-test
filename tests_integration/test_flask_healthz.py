def test_live(client):
    response = client.get("/healthz/live")
    assert response.status == "200 OK"


def test_ready(client):
    response = client.get("/healthz/ready")
    assert response.status == "200 OK"
