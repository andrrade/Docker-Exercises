## 1️⃣2️⃣ Corrigir vulnerabilidades encontradas 🔴

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)

Após identificar vulnerabilidades com ferramentas como o Trivy, o próximo passo é 
corrigi-las. Imagens grandes e genéricas frequentemente trazem bibliotecas 
desnecessárias e vulneráveis, além de usarem o usuário root por padrão. Neste 
exercício, você irá trabalhar com um exemplo de Dockerfile com más práticas e 
aplicar melhorias para construir uma imagem mais segura e enxuta. Identifique as 
melhorias e gere uma nova versão de Dockerfile.

![image](https://github.com/user-attachments/assets/635092a9-dbf1-4b8e-9da7-2b092801f2d2)

## 💡 Resolução Exercício 12

```txt
flask==1.1.1
requests==2.22.0
```

antes:

```dockerfile
# Dockerfile vulnerável
FROM python:3.9 
WORKDIR /app 
COPY requirements.txt . 
RUN pip install --r requirements.txt
COPY . . 
CMD ["python", "app.py"]
```

depois:

[Imagem Python utilizada](https://hub.docker.com/layers/library/python/3.9-slim/images/sha256-d57e6f8e0ed5afc48afda19a0a42728a45088d243259b1d8f589b05ed8eb4adb)

```dockerfile
# Use uma imagem base slim para reduzir o tamanho da imagem
FROM python:3.9-slim

# Criação de um usuário não-root para melhorar a segurança
RUN useradd -m appuser

# Defina o diretório de trabalho e altere para o novo usuário
WORKDIR /app
USER appuser

# Copiar somente o requirements.txt para otimizar o cache de build
COPY requirements.txt .

# Instalar dependências de maneira mais segura e eficiente
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copiar o restante dos arquivos da aplicação (no caso, nada)
# Caso você não tenha arquivos adicionais, pode comentar esta linha
# COPY . .

# Deixar o contêiner rodando com um comando simples
CMD ["python", "-m", "http.server", "5000"]
```

atualização requirements
```bash
flask==2.2.5
requests==2.31.0
```

```py
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    user = os.getenv("USER", "desconhecido")
    return f"Olá, mundo! Rodando como usuário: {user}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

