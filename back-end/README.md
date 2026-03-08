# FastAPI Project

## Structure

```text
app/
├── api/          # API routes
│   └── v1/       # Version 1 of API
├── core/         # Core config, security
├── db/           # Database session, base
├── models/       # Database models
├── schemas/      # Pydantic models
└── services/     # Business logic
tests/            # Tests
```

## Migrations (Alembic)

1. Generate a new migration revision:
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```

2. Apply migrations to the database:
   ```bash
   alembic upgrade head
   ```

## Getting Started

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Access the API:
   - Root: http://127.0.0.1:8000/
   - API V1 Samples: http://127.0.0.1:8000/api/v1/samples
   - Documentation (Swagger UI): http://127.0.0.1:8000/docs
