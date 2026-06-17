from datetime import datetime

from database.db import SessionLocal
from database.auth import AuditHistory


def save_audit(
    user_email,
    website_url,
    risk_score
):

    db = SessionLocal()

    audit = AuditHistory(
        user_email=user_email,
        website_url=website_url,
        risk_score=risk_score,
        created_at=str(
            datetime.now()
        )
    )

    db.add(audit)

    db.commit()

    db.close()


def get_audits(
    user_email
):

    db = SessionLocal()

    audits = (
        db.query(AuditHistory)
        .filter(
            AuditHistory.user_email
            == user_email
        )
        .all()
    )

    db.close()

    return audits