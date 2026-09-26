import uuid

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_complete_gateway_flow():

    # Create a unique user every test run
    email = f"test_{uuid.uuid4()}@example.com"

    # 1. Create user
    user_response = client.post(
        f"/create-user?email={email}"
    )

    assert user_response.status_code == 200

    user_data = user_response.json()

    assert "api_key" in user_data

    api_key = user_data["api_key"]


    # 2. Generate response using API key
    generate_response = client.post(
        "/generate",
        headers={
            "x-api-key": api_key
        },
        json={
            "prompt": "Explain what an LLM gateway is in one sentence"
        }
    )

    assert generate_response.status_code == 200

    generation_data = generate_response.json()

    assert "response" in generation_data
    assert "conversation_id" in generation_data


    conversation_id = generation_data["conversation_id"]


    # 3. Check conversations list
    conversations_response = client.get(
        "/conversations"
    )

    assert conversations_response.status_code == 200

    conversations = conversations_response.json()

    assert len(conversations) > 0


    # 4. Check specific conversation
    conversation_response = client.get(
        f"/conversations/{conversation_id}"
    )

    assert conversation_response.status_code == 200

    conversation = conversation_response.json()

    assert "messages" in conversation

    assert len(conversation["messages"]) == 2


    # 5. Verify user + assistant messages exist
    messages = conversation["messages"]

    assert messages[0]["role"] == "user"
    assert messages[1]["role"] == "assistant"