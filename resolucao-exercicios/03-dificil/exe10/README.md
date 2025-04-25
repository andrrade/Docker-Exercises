## 1️⃣0️⃣ Evitar execução como root 🔴

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)

Ao rodar containers com o usuário root, você expõe seu sistema a riscos maiores em 
caso de comprometimento. Neste exercício, você deverá criar um Dockerfile para 
uma aplicação simples (como um script Python ou um servidor Node.js) e configurar 
a imagem para rodar com um usuário não-root.

Você precisará:

a. Criar um usuário com useradd ou adduser no Dockerfile.

b. Definir esse usuário como o padrão com a instrução USER.

c. Construir a imagem e iniciar o container.

d. Verificar se o processo está rodando com o novo usuário usando docker exec 
<container> whoami.

## 💡 Resolução Exercício 10

01. Crie o diretório `exe10` e acesse-o:
   
```bash
mkdir exe10
```

```bash
cd exe10
```

02. Abra o VSCode com `code .` para criar o `Dockerfile` e o `script`

```bash
code .
```

![image](https://github.com/user-attachments/assets/3ef06df7-7872-483d-b0e1-2483e990329a)

03. Crie o script

![image](https://github.com/user-attachments/assets/f2e6648d-e118-42f6-ae3e-0ee883ee1fae)

```python
import os
from datetime import datetime

print("✅ Container rodando como userTeste!")
print(f"👤 UID/GID: {os.getuid()}/{os.getgid()}")
print(f"👤 whoami: {os.popen('whoami').read().strip()}")
print(f"👤 id: {os.popen('id').read().strip()}")

hora_execucao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"⏰ Horário de execução: {hora_execucao}")

print("👋 Fim do script")

# Mantém o container rodando (Ctrl + C para parar)
while True:
    pass 
```

04. Crie o Dockerfile

[Imagem Python utilizada](https://hub.docker.com/layers/library/python/3.12.10-alpine3.21/images/sha256-3025e0b31da85cd9240d41fc61b979fc8303ae3e46464e7df33272b9f3420039)

![image](https://github.com/user-attachments/assets/75ba7f44-8eba-42c8-9963-4b0b876bb863)

```dockerfile
  FROM python:3.12.10-alpine3.21
  
  RUN addgroup -S groupTeste && \
      adduser -S -G groupTeste -h /app userTeste && \
      mkdir -p /app && \
      chown userTeste:groupTeste /app
  
  WORKDIR /app
  
  COPY --chown=userTeste:groupTeste exe10.py .
  RUN chmod 744 exe10.py
  
  USER userTeste
  
  CMD ["python", "exe10.py"]
```

05. Voltar para o terminal e subir o container

```bash
docker build -t exe10-image .
```

```bash
docker run -d --name exe10-container exe10-image
```

![image](https://github.com/user-attachments/assets/f9c1fdf5-86a2-43c1-a9d3-1a4f835e48ec)

06. Entrar no terminal para testar

```bash
docker exec -it exe10-container sh
```

```bash
python /app/exe10.py
```

![image](https://github.com/user-attachments/assets/cbadcef4-5ebf-477d-aec5-701c57950d81)

> [!NOTE]
> Para sair do script: `CTRL + C`

07. Testar comandos para provar que não tenho permissão

```bash
adduser hacker
```

```bash
touch /etc/arquivo-teste
```

```bash
apk add bash
```

![image](https://github.com/user-attachments/assets/f35930e1-8ac5-469c-a7da-3b9146c96e47)

08. Provando que não sou o root

```bash
whoami
```

```bash
id
```

```bash
ls -l /app
```

```bash
cat exe10.py && echo
```

![image](https://github.com/user-attachments/assets/1f6366d2-c0f9-42a4-b78c-5eeabd89f131)
