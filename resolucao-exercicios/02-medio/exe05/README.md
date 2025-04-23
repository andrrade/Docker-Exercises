## 5️⃣ Criando e utilizando volumes para persistência de dados 🟡

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)

Execute um container MySQL e configure um volume para armazenar os dados do 
banco de forma persistente. Para aplicar esse conceito você pode utilizar o [react-express-mysql](https://github.com/docker/awesome-compose/tree/master/react-express-mysql)

## 💡 Resolução Exercício 5

01. Crie o diretório `exe05` e entre nele

![image](https://github.com/user-attachments/assets/47936a2e-9282-4c7c-8e61-075845d55ba8)

```bash
mkdir exe05
```

```bash
cd exe05
```

02. Pegar o link para clonar o repositório

[Link do Repositório Completo](https://github.com/docker/awesome-compose)

![image](https://github.com/user-attachments/assets/e9e1ed82-e1db-4e88-baad-a0c4c266adfc)

03. Coloque `git clone` antes do link copiado para executar o comando:

```bash
git clone https://github.com/docker/awesome-compose.git
```

>[!NOTE]
> Precisamos apenas do direório react-express-mysql, por isso vamos remover todo o resto e deixar apenas o necessário

```bash
cp -r awesome-compose/react-express-mysql/* .
```

```bash
rm -rf awesome-compose
```

![image](https://github.com/user-attachments/assets/dfa573ea-7350-4236-8311-79a7a433cd7a)

05. Subir o container

```bash
docker-compose up -d
```

![image](https://github.com/user-attachments/assets/ba47abf6-2555-40c5-abbe-665b5693bd41)

06. Vendo e inspecionando volumes:

![image](https://github.com/user-attachments/assets/62c11384-d176-4008-88ae-fc6248b949b0)

```bash
docker volume ls
```

```bash
docker volume inspect exe05_db-data
```

07. Listando os containers

![image](https://github.com/user-attachments/assets/295aa009-19a9-488d-a84b-631119859658)

```bash
docker ps
```

08. Veja a senha para acessar o MySQL e guarde-a

![image](https://github.com/user-attachments/assets/855631eb-847f-4e00-a5cc-1010c2ba2435)

```bash
cat db/password.txt && echo
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
> Utilize a senha recebida após o comando `cat db/password.txt && echo`

```bash
db-btf5q
```

![image](https://github.com/user-attachments/assets/159b7053-53bd-4ffd-b227-f9d8b1c8c8b5)

11. Dentro do MySQL, execute:

```sql
SHOW DATABASES;
```

```sql
USE example;
```

```sql
SHOW TABLES;
```

12. Crie uma tabela para teste:

```sql
CREATE TABLE alunos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100)
);
```

13. Veja se foi

```sql
SHOW TABLES;
```

14. Insira dados na tabela

```sql
INSERT INTO alunos (nome) VALUES ('Laura');
```

```sql
SELECT * FROM alunos;
```
![image](https://github.com/user-attachments/assets/2246fbc6-7427-43c6-83f5-bceff2975b5e)

14. Saia dos terminais, execute esse comando duas vezes:

```bash
exit
```

![image](https://github.com/user-attachments/assets/8e672555-9a84-442a-a985-603fe73a3a89)

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
