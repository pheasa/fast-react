FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip==26.0.1
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install debugpy

COPY . .

# CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"] // Start the application with debugpy for remote debugging
CMD ["gunicorn", "main:app", "-w", "3", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "--timeout", "60", "--max-requests", "500", "--max-requests-jitter", "50"]