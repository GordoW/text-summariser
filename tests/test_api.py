from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_summarise_text():
    response = client.post(
        "/summarise",
        json={
            "text": "Artificial intelligence is reshaping software development. Developers now use AI assistants and agent-based workflows to generate code, automate testing, and catch bugs in real time. This shifts human roles from writing every line of code to managing high-level intent, drastically cutting development time."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "summary" in data
    assert "original_word_count" in data
    assert "summary_word_count" in data

def test_summarise_text_too_short():
    response = client.post(
        "/summarise",
        json={
            "text": "hi"
        }
    )

    assert response.status_code == 422

def test_summarise_response_structure():
    response = client.post(
        "/summarise",
        json={
            "text": "Artificial intelligence is reshaping software development. Developers now use AI assistants and agent-based workflows to generate code, automate testing, and catch bugs in real time. This shifts human roles from writing every line of code to managing high-level intent, drastically cutting development time."
        }
    )

    data = response.json()

    assert isinstance(data["summary"], str)
    assert isinstance(data["original_word_count"], int)
    assert isinstance(data["summary_word_count"], int)