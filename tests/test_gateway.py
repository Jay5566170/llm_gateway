from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_complete_gateway_flow():

    # 1. Create user
    user_response = client.post(
        "/create-user",
        params={
            "email": "test@example.com"
        }
    )

    assert user_response.status_code == 200

    user_data = user_response.json()

    api_key = user_data["api_key"]

    assert api_key is not None


    # 2. Test invalid API key
    bad_response = client.post(
        "/generate",
        headers={
            "x-api-key": "wrong-key"
        },
        json={
            "prompt": "hello"
        }
    )

    assert bad_response.status_code in [401,403]


    # 3. Generate LLM response
    response = client.post(
        "/generate",
        headers={
            "x-api-key": api_key
        },
        json={
            "prompt": "Explain AI in one sentence"
        }
    )


    assert response.status_code == 200


    data = response.json()

    assert "response" in data
    assert "conversation_id" in data


    conversation_id = data["conversation_id"]


    # 4. Check conversations list

    conversations = client.get(
        "/conversations"
    )

    assert conversations.status_code == 200


    # 5. Check conversation history

    history = client.get(
        f"/conversations/{conversation_id}"
    )


    assert history.status_code == 200


    history_data = history.json()


    assert len(history_data["messages"]) >= 2