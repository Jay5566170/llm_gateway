from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.services.auth_service import validate_api_key


def require_api_key(
    x_api_key: str = Header(),
    db: Session = Depends(get_db)
):

    user_id = validate_api_key(
        db,
        x_api_key
    )

    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    return user_id