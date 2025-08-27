import httpx
import pytest

from app.main import app


@pytest.mark.asyncio
async def test_create_user():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/users/", json={"name": "Simone", "email": "simone@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Simone"
    assert data["email"] == "simone@example.com"

@pytest.mark.asyncio
async def test_get_users():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/api/v1/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
