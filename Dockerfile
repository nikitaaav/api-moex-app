# Используем базовый образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /api-moex-app

# Install the application dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY src ./src
COPY templates ./templates
COPY static ./static


CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]