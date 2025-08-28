import logging

from app.models.user import User, UserCreate

log = logging.getLogger(__name__)

_fake_db: list[User] = []


async def save_user(user: UserCreate) -> User:
    log.debug("Creating user")
    user_id = len(_fake_db) + 1
    new_user = User(id=user_id, **user.model_dump())
    _fake_db.append(new_user)
    log.info("User created")
    return new_user


async def get_all_users() -> list[User]:
    log.debug("Reading all users")
    return _fake_db


# Clears the in-memory user store.
# Used only in tests to ensure isolation between runs.
def _reset_users():
    global _fake_db
    _fake_db = []
