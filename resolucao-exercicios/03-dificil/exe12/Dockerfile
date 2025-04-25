FROM python:3.9-slim

RUN useradd -m appuser

WORKDIR /app
USER appuser

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["python", "-m", "http.server", "5000"]