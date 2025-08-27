import pytest
from app.models.user import UserCreate
from app.services.user_service import save_user, get_all_users


@pytest.mark.asyncio
async def test_save_user():
    user = UserCreate(name="Simone", email="simone@example.com")
    saved_user = await save_user(user)
    assert saved_user.name == "Simone"
    assert saved_user.email == "simone@example.com"


@pytest.mark.asyncio
async def test_get_all_users_empty():
    users = await get_all_users()
    assert isinstance(users, list)
    assert len(users) > 0
