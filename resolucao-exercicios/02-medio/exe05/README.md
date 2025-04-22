## 5️⃣ Criando e utilizando volumes para persistência de dados 🟡

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)

Execute um container MySQL e configure um volume para armazenar os dados do 
banco de forma persistente. Para aplicar esse conceito você pode utilizar o [react-express-mysql](https://github.com/docker/awesome-compose/tree/master/react-express-mysql)

## 💡 Resolução Exercício 5

01. Crie o diretório `exe05` e entre nele

```bash
mkdir exe05
```

```bash
cd exe05
```

02. Clonar repositório fornecido pelo link do enunciado

```bash
git clone https://github.com/docker/awesome-compose.git
```

03. Copiar só o conteúdo da pasta `react-express-mysql` pra `exe05`
  
```bash
cp -r awesome-compose/react-express-mysql/* .
```

04. Remover a pasta awesome-compose (já não precisamos mais)

```bash
rm -rf awesome-compose
```

05. Subir o projeto

```bash
docker-compose up -d
```

![image](https://github.com/user-attachments/assets/3e3847bb-6d7b-442e-ba4a-99e98c91385c)

06. Vendo e inspecionando volumes:

```bash
docker volume ls
```

```bash
docker volume inspect exe05_db-data
```

![image](https://github.com/user-attachments/assets/000e2b65-3e67-4184-9c39-1de671fcf1a9)

07. Listando os containers

```bash
docker ps
```

![image](https://github.com/user-attachments/assets/b4f1fa52-4caf-440e-9077-0c1a13d4ce89)

08. Veja a senha para acessar o MySQL e guarde-a

```bash
cat db/password.txt
```

09. Acesse o container do MySQL

```bash
docker exec -it exe05-db-1 bash
```

10. Dentro dele, acesse o MySQL com o usuário que tá no docker-compose.yml

```bash
mysql -u root -p
```

>[!NOTE]
> Utilize a senha recebida após o comando `cat db/password.txt`

11. Dentro do MySQL, execute:

```sql
SHOW DATABASES;
```

12. Crie uma tabela para teste:

```sql
USE example;

CREATE TABLE alunos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100)
);
```

13. Veja se foi

```bash
SELECT * FROM alunos;
```

14. Saia

```bash
exit
```

```bash
docker-compose down
```

```bash
docker-compose up -d
```

```bash
docker exec -it exe05-db-1 bash
```

```bash
mysql -u root -p
```

```sql
USE example;
```

```sql
SELECT * FROM alunos;
```

```bash
exit
```

```bash
docker-compose down
```

```bash
docker volume rm exe05_db-data
```

```bash
docker volume ls
```

```bash
docker-compose up -d
```

```bash
docker exec -it exe05-db-1 bash
```

```bash
mysql -u root -p
```

```sql
USE example;
```

```sql
SELECT * FROM alunos;
```
