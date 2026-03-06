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
   - API V1 Items: http://127.0.0.1:8000/api/v1/items
   - Documentation (Swagger UI): http://127.0.0.1:8000/docs
