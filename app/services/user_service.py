from app.models.user import User, UserCreate

_fake_db: list[User] = []


async def save_user(user: UserCreate) -> User:
    user_id = len(_fake_db) + 1
    new_user = User(id=user_id, **user.model_dump())
    _fake_db.append(new_user)
    return new_user


async def get_all_users() -> list[User]:
    return _fake_db
