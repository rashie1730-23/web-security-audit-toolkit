import hashlib
from database.db import SessionLocal
from database.auth import User


def register_user(
    name,
    email,
    password
):

    db = SessionLocal()

    existing_user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if existing_user:
        return False, "User already exists"

    hashed_password = hashlib.sha256(
        password.encode()
    ).hexdigest()

    user = User(
        name=name,
        email=email,
        password=hashed_password
    )

    db.add(user)

    db.commit()

    db.close()

    return True, "Registration Successful"
def login_user(
    email,
    password
):

    db = SessionLocal()

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        return False, None

    entered_hash = hashlib.sha256(
        password.encode()
    ).hexdigest()

    if entered_hash == user.password:
        return True, user

    return False, None