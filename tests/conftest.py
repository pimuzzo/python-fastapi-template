import pytest
from app.services.user_service import _reset_users


@pytest.fixture(autouse=True)
def clean_fake_db():
    _reset_users()
