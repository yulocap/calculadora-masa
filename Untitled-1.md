FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# El puerto 8080 es el que Railway usa por defecto
CMD ["python", "main.py"]