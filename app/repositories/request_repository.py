from sqlalchemy.orm import Session

from app.models.request_log import RequestLog


def create_request_log(
    db: Session,
    prompt: str,
    response: str,
    provider: str
):

    log = RequestLog(
        prompt=prompt,
        response=response,
        provider=provider
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log