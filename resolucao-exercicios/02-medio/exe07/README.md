## 7️⃣ Construindo uma rede Docker para comunicação entre containers 🟡

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)

Crie uma rede Docker personalizada e faça dois containers, um Node.js e um 
MongoDB, se comunicarem, sugestão, utilize o projeto [React Express + Mongo](https://github.com/docker/awesome-compose/tree/master/react-express-mongodb).

## 💡 Resolução Exercício 7

01. Criar pasta do exercício 7 e entrar nela

```bash
mkdir exe07
```

```bash
cd exe07
```

![image](https://github.com/user-attachments/assets/e5b66d2f-c4a5-4212-a832-d5ddcd8cf7af)

02. Pegar o link para clonar o repositório

[Link do Repositório Completo](https://github.com/docker/awesome-compose)

![image](https://github.com/user-attachments/assets/85947827-afef-408d-bcf9-2a7d254a0844)

03. Coloque `git clone` antes do link copiado para executar o comando:

```bash
git clone https://github.com/docker/awesome-compose.git
```

>[!NOTE]
> Precisamos apenas do direório react-express-mongodb, por isso vamos remover todo o resto e deixar apenas o necessário

```bash
cp -r awesome-compose/react-express-mongodb ./
```

```bash
rm -rf awesome-compose
```

04. Entrar dentro do diretório `react-express-mongodb`

```bash
cd react-express-mongodb
```

05. Abrir o VSCode

```bash
code .
```

![image](https://github.com/user-attachments/assets/910cf1c3-946e-4847-9aed-05252baccbf5)

06. Alterar o `Dockerfile` do diretório backend

![image](https://github.com/user-attachments/assets/317c9d5f-7d22-446c-9d97-2705335064f6)

```bash
FROM node:lts-buster-slim AS development

RUN apt-get update && apt-get install -y --no-install-recommends iputils-ping && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY package.json /usr/src/app/package.json
COPY package-lock.json /usr/src/app/package-lock.json
RUN npm ci

COPY . /usr/src/app

EXPOSE 3000

CMD [ "npm", "run", "dev" ]

FROM development as dev-envs
RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends git
EOF

RUN <<EOF
useradd -s /bin/bash -m vscode
groupadd docker
usermod -aG docker vscode
EOF

COPY --from=gloursdocker/docker / /
CMD [ "npm", "run", "dev" ]
```

07. Alterar o `Dockerfile` do diretório frontend

![image](https://github.com/user-attachments/assets/637898ea-8cc0-4e63-828d-aa99b4636fd0)

```bash
FROM node:lts-buster AS development

RUN apt-get update && apt-get install -y --no-install-recommends iputils-ping && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY package.json /usr/src/app
COPY package-lock.json /usr/src/app

RUN npm ci

COPY . /usr/src/app

EXPOSE 3000

CMD ["npm", "start"]

FROM development as dev-envs
RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends git
EOF

RUN <<EOF
useradd -s /bin/bash -m vscode
groupadd docker
usermod -aG docker vscode
EOF

COPY --from=gloursdocker/docker / /
CMD [ "npm", "start" ]
```

08. Subir container

```bash
docker compose up --build -d
```

![image](https://github.com/user-attachments/assets/b51fbde1-22f8-478b-8085-43c2ef219424)

09. Testar as networks com ping

```bash
docker ps
```

![image](https://github.com/user-attachments/assets/281f42cc-998a-41aa-b241-4f7bb35a7b77)

a. Testar comunicação do Backend com o MongoDB

```bash
docker exec -it react-express-mongodb-backend-1 ping -c 4 react-express-mongodb-mongo-1
```

> [!NOTE]
> Verifica se o backend pode se comunicar com o MongoDB.

![image](https://github.com/user-attachments/assets/0e313f41-3cef-4ce0-a3d8-8b8d3df9165b)

b. Testar comunicação do Frontend com o Backend

```bash
docker exec -it react-express-mongodb-frontend-1 ping -c 4 react-express-mongodb-backend-1
```

> [!NOTE]
> Verifica se o frontend pode se comunicar com o backend.

![image](https://github.com/user-attachments/assets/0f14aa13-ddd1-4614-bebc-095a2b294792)


c. Testar comunicação do Backend com o Frontend

```bash
docker exec -it react-express-mongodb-backend-1 ping -c 4 react-express-mongodb-frontend-1
```

> [!NOTE]
> Verifica se o backend pode se comunicar com o frontend.

![image](https://github.com/user-attachments/assets/4f7f1b03-4bbe-4fdd-b742-fadef818fd43)

10. Mostrar funcionando na porta `3000`

```bash
http://localhost:3000
```

> [!NOTE]
> Abrir no navegador.

https://github.com/user-attachments/assets/5e02edf9-a8cb-404c-9474-9ae50ff7ede2
