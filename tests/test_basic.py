from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_home():
    res = client.get("/")
    assert res.status_code == 200
    assert "message" in res.json()

def test_reddit_endpoint_invalid():
    res = client.get("/reddit?subreddit=thissubredditsofake1234")
    assert res.status_code in [404, 400]

def test_reddit_endpoint_valid():
    res = client.get("/reddit?subreddit=python")
    assert res.status_code == 200
    data = res.json()
    assert "subreddit" in data
    assert "subscribers" in data
