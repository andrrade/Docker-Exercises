## 8️⃣ Criando um compose file para rodar uma aplicação com BD 🟡

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)

Utilize Docker Compose para configurar uma aplicação com um banco de 
dados PostgreSQL, use para isso o projeto [pgadmin](https://github.com/docker/awesome-compose/tree/master/postgresql-pgadmin).

## 💡 Resolução Exercício 8

01. Criar pasta do exercício 8 e entrar nela

```bash
mkdir exe08
```

```bash
cd exe08
```

02. Pegar o link para clonar o repositório

[Link do Repositório Completo](https://github.com/docker/awesome-compose)

![image](https://github.com/user-attachments/assets/85947827-afef-408d-bcf9-2a7d254a0844)

03. Coloque `git clone` antes do link copiado para executar o comando:

```bash
git clone https://github.com/docker/awesome-compose.git
```

>[!NOTE]
> Precisamos apenas do direório `postgresql-pgadmin`, por isso vamos remover todo o resto e deixar apenas o necessário

```bash
cp -r awesome-compose/postgresql-pgadmin ./
```

```bash
rm -rf awesome-compose
```

04. Entrar dentro do diretório `postgresql-pgadmin`

```bash
cd postgresql-pgadmin
```

![image](https://github.com/user-attachments/assets/0c95d552-caa1-4d51-ad3f-e00fcf5587cb)

07. Subir container

```bash
docker compose up --build -d
```

![image](https://github.com/user-attachments/assets/b51fbde1-22f8-478b-8085-43c2ef219424)

08. Testar networking com ping

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

09. Mostrar funcionando na porta `3000`

```bash
http://localhost:3000
```

> [!NOTE]
> Abrir no navegador.

https://github.com/user-attachments/assets/5e02edf9-a8cb-404c-9474-9ae50ff7ede2
