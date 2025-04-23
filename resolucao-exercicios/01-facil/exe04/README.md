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

05. Subir o container

```bash
docker-compose up -d
```

![image](https://github.com/user-attachments/assets/e2dd9ab4-1d19-4854-98a2-2e7ac4b06e9e)

06. Ver a porta que ele está rodando para acessar a aplicação

```bash
docker ps
```

![image](https://github.com/user-attachments/assets/b45a889f-a794-4bca-8e63-e18ee2b77f87)

07. Abrir no navegador

```bash
http://localhost:8000
```

![image](https://github.com/user-attachments/assets/9253f9af-431a-4486-b774-b61cbe06d3cc)
