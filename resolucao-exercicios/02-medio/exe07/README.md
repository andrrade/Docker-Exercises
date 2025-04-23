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

02. Pegar o link para clonar o repositório

[Link do Repositório Completo](https://github.com/docker/awesome-compose)

03. Coloque `git clone` antes do link copiado para executar o comando:

```bash
git clone https://github.com/docker/awesome-compose.git
```

>[!NOTE]
> Precisamos apenas do direório react-flask-mongodb, por isso vamos remover todo o resto e deixar apenas o necessário

```bash
cp -r awesome-compose/react-express-mongodb ./
```

```bash
rm -rf awesome-compose
```




04. Entrar dentro do diretório `flask` e `app`

```bash
cd react-express-mongodb
```

docker compose up --build -d
docker ps

backend
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

frontend
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

comandos
```bash
docker compose up --build -d
```

```bash
docker exec -it react-express-mongodb-backend-1 ping -c 4 mongo
```

```bash
docker exec -it react-express-mongodb-frontend-1 ping -c 4 backend
```
