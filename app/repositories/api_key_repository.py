from sqlalchemy.orm import Session

from app.models.api_key import APIKey


def create_api_key(
    db: Session,
    user_id: int,
    key: str
):

    api_key = APIKey(
        user_id=user_id,
        key=key
    )

    db.add(api_key)
    db.commit()
    db.refresh(api_key)

    return api_key



def get_api_key(
    db: Session,
    key: str
):

    return (
        db.query(APIKey)
        .filter(
            APIKey.key == key,
            APIKey.active == True
        )
        .first()
    )