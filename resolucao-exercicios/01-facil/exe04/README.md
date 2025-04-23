## 4️⃣ Criando um Dockerfile para uma aplicação simples em Python 🟢

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)

Crie um Dockerfile para uma aplicação Flask que retorna uma mensagem ao acessar 
um endpoint, para isso utilize o projeto [Docker Flask](https://github.com/docker/awesome-compose/tree/master/flask/app)

## 💡 Resolução Exercício 4

01. Criar pasta do exercício 4 e entrar nela

![image](https://github.com/user-attachments/assets/309d8288-d7b3-49b4-8247-ab3de50ec21c)

```bash
mkdir exe04
```

```bash
cd exe04
```

02. Pegar o link para clonar o repositório

[Link do Repositório Completo](https://github.com/docker/awesome-compose)

![image](https://github.com/user-attachments/assets/e13274d7-5e2e-4b4e-ae34-404dd598152e)

03. Coloque `git clone` antes do link copiado para executar o comando:

```bash
git clone https://github.com/docker/awesome-compose.git
```

>[!NOTE]
> Precisamos apenas do direório flask, por isso vamos remover todo o resto e deixar apenas o necessário

```bash
cp -r awesome-compose/flask ./
```

```bash
rm -rf awesome-compose
```

![image](https://github.com/user-attachments/assets/1d128f21-dc8a-49b7-a4f7-7c6f50f83ef4)

04. Entrar dentro do diretório `flask` e `app`

```bash
cd flask/app
```

05. Remover o arquivo `Dockerfile` para abrir o VSCode e criar um próprio
> [!NOTE]
> Senão não tem graça se já estivesse tudo pronto

![image](https://github.com/user-attachments/assets/bcbca674-d94e-4b52-92b4-b87700817b32)

05. Arquivo Dockerfile

![image](https://github.com/user-attachments/assets/28325dc9-db49-4e1f-acb2-15b802e18769)

```dockerfile
FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

EXPOSE 8000

ENTRYPOINT ["python3"]
CMD ["app.py"]
```

06. Subir o container

```bash
docker build -t exe04-image .
```

```bash
docker run -d -p 8000:8000 --name exe04-container exe04-image
```

![image](https://github.com/user-attachments/assets/528ecc4e-09c2-423d-8705-2b1019ca86f9)

07. Abrir no navegador

```bash
curl http://localhost:8000 && echo
```
> [!NOTE]
> Esse comando é para ser executado no terminal

```bash
http://localhost:8000
```

> [!NOTE]
> Esse é para copiar e colar no navegador

![image](https://github.com/user-attachments/assets/9253f9af-431a-4486-b774-b61cbe06d3cc)
