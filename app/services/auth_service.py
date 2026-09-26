from app.repositories.api_key_repository import get_api_key


def validate_api_key(
    db,
    key: str
):

    api_key = get_api_key(
        db,
        key
    )

    if not api_key:
        return None

    return api_key.user_id