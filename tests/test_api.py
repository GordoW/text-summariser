from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_ai_health():
    response = client.get("/health/ai")

    assert response.status_code == 200

    data = response.json()

    assert "provider" in data
    assert "model" in data
    assert "llm_available" in data

def test_summarise():
    response = client.post(
        "/summarise",
        json={
            "text": "Artificial intelligence is reshaping software development. Developers now use AI assistants and agent-based workflows to generate code, automate testing, and catch bugs in real time. This shifts human roles from writing every line of code to managing high-level intent, drastically cutting development time."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data["summary"], str)
    assert isinstance(data["original_word_count"], int)
    assert isinstance(data["summary_word_count"], int)

def test_summarise_text_too_short():
    response = client.post(
        "/summarise",
        json={
            "text": "hi"
        }
    )

    assert response.status_code == 422

def test_summarise_when_llm_unavailable():

    # This test will be implemented properly
    # using mocking in the next step.

    assert True