# python-fastapi-template

A simple and idiomatic REST API boilerplate in Python using [FastAPI](https://fastapi.tiangolo.com/), designed for clarity, modularity and extensibility.  
Built to showcase best practices in Python backend development and serve as a solid foundation for future projects.

## ✨ Features

- 🧱 Modular project structure (`api/`, `models/`, `services/`, etc.)
- 🔀 Routing with versioned endpoints
- 📄 OpenAPI docs auto-generated (`/docs`, `/redoc`)
- ✅ Data validation and typing with Pydantic v2
- 🧪 Async-ready test setup with `pytest`, `httpx`, `pytest-asyncio` (in progress)
- 🐳 Minimal Docker support (in progress)
- 🧰 Designed as a reusable starter template

## 📦 Technologies

- Python 3.11+
- FastAPI
- Uvicorn (ASGI server)
- Pydantic v2

## 🚀 Getting Started

```bash
# Install dependencies
poetry install

# Run the development server
poetry run uvicorn app.main:app --reload
```
