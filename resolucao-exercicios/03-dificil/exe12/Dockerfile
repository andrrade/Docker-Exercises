# Dockerfile Melhorado
FROM python:3.9-slim

RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y && apt-get clean

RUN apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libpq-dev \
    perl-base \
    zlib1g \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade setuptools==70.0.0

RUN groupadd -r grupoTeste && useradd -r -g grupoTeste userTeste

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R userTeste:grupoTeste /app

USER userTeste

EXPOSE 5000

CMD ["python", "app.py"]