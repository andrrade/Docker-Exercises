> [!WARNING]
> **Ainda estou fazendo os exercícios**, só criei o repositório para ir me organizando melhor.  
> Irei postando atualizações por aqui :)

<p align="center">
  <img src="https://github.com/user-attachments/assets/b21e8645-8683-41ce-8db3-2543c02561ae" alt="Logo dos Exercícios" width="500">
</p>
<br>

# Avaliação 2 - Lista de Exercícios 🐋

# Sumário 📝

## 🟢 Fácil

- [1º Exercício](#1%EF%B8%8F⃣-rodando-um-container-básico-)
- [2º Exercício](#2%EF%B8%8F⃣-criando-e-rodando-um-container-interativo-)
- [3º Exercício](#3%EF%B8%8F⃣-listando-e-removendo-containers-)
- [4º Exercício](#4%EF%B8%8F⃣-criando-um-dockerfile-para-uma-aplicação-simples-em-python-)

## 🟡 Médio

- [5º Exercício](#5%EF%B8%8F⃣-criando-e-utilizando-volumes-para-persistência-de-dados-)
- [6º Exercício](#6%EF%B8%8F⃣-criando-e-rodando-um-container-multi-stage-)
- [7º Exercício](#7%EF%B8%8F⃣-construindo-uma-rede-docker-para-comunicação-entre-containers-)
- [8º Exercício](#8%EF%B8%8F⃣-criando-um-compose-file-para-rodar-uma-aplicação-com-bd-)

## 🔴 Difícil

- [9º Exercício](#9%EF%B8%8F⃣-criando-uma-imagem-personalizada-com-um-servidor-web-e-arquivos-estáticos-)

---

## 👣 1º Passo: Configuração do Ambiente

Para realizar os exercícios de Docker, utilizei as seguintes ferramentas e configurações:

- 🪟 **Sistema Operacional:** Windows  
- 🐧 **WSL:** [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/) com [Ubuntu 25.04.1 LTS](https://documentation.ubuntu.com/server/)  
- 🐳 **Gerenciador de Containers:** [Rancher Desktop](https://rancherdesktop.io/) — alternativa gratuita ao [Docker Desktop](https://www.docker.com/products/docker-desktop/)  
- 💻 **Editor de Código:** [Visual Studio Code](https://code.visualstudio.com/)  

## 👣 2º Passo: Organização dos Exercícios no WSL

Para manter os exercícios organizados, dentro do diretório home do WSL, criei uma pasta chamada `docker-exercises`. Cada exercício foi armazenado em um subdiretório separado, como `exe01`, `exe02`, etc.

![image01](https://github.com/user-attachments/assets/b3206469-6561-4215-b2a3-f178a68c7cce)

Comandos Utilizados:

```bash
mkdir docker-exercises
```

```bash
cd docker-exercises
```

```bash
mkdir exe-01
```

# 🟢 Fácil

## 1️⃣ Rodando um container básico 🟢

[🔼 Voltar ao Sumário](#sumário-)

a. Execute um container usando a imagem do Nginx e acesse a página
padrão no navegador.

b. Exemplo de aplicação: Use a [landing page do TailwindCSS](https://github.com/tailwindtoolbox/Landing-Page) como site estático dentro do container.

## 💡 Resolução Exercício 1

01. Criar o diretório `exe01` e acessá-lo:
   
![image02](https://github.com/user-attachments/assets/b16ef3c2-1ca0-487e-bf01-5ae3286e1c25)

Comandos Utilizados:

```bash
mkdir exe01
```

```bash
cd exe01
```

02. Clonar o repositório que contém a [Landing-Page](https://github.com/tailwindtoolbox/Landing-Page)

![image03](https://github.com/user-attachments/assets/4fe22256-b6aa-443b-a2c3-ded601716844)

03. No final do link adicione um ponto `.` para copiar para o diretório atual:

```bash
https://github.com/tailwindtoolbox/Landing-Page.git .
```

04. Remover os arquivos `README.md` e `LICENSE`
  
05. Abrir o VSCode com `code .` para criar o `Dockerfile`

![image04](https://github.com/user-attachments/assets/9805d84b-8066-4814-a1ad-42f3b085b21d)

06. Criar um arquivo Dockerfile

![image05](https://github.com/user-attachments/assets/dfcce0c1-f7e2-4293-9384-6839fa2111e0)

```bash
FROM nginx:latest
COPY . /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

07. Voltando para o terminal veja se o Dockerfile criado está lá
  
08. Crie o container:

```bash
docker build -t site-tailwind .
```

![image06](https://github.com/user-attachments/assets/e3d9596d-2067-46b9-970a-31fb6dd0d1ff)

09. Rode o container

```bash
docker run -d -p 8080:80 --name container-tailwind site-tailwind
```

![image07](https://github.com/user-attachments/assets/c142e684-d1e7-434c-b9c7-8ee2c4aff2d6)

10. Acesse o navegador e digite `http://localhost:8080`

![image08](https://github.com/user-attachments/assets/2147565e-4ad2-4629-9780-ed38d11d1c21)

---

## 2️⃣ Criando e rodando um container interativo 🟢

[🔼 Voltar ao Sumário](#sumário-)

a. Inicie um container Ubuntu e interaja com o terminal dele.

b. Exemplo de aplicação: Teste um script Bash que imprime logs do
sistema ou instala pacotes de forma interativa.

## 💡 Resolução Exercício 1

01. t
   
![image09](https://github.com/user-attachments/assets/86b79d7a-1f6a-4e83-ba56-8c03847cef45)

2. `code .`

3. t

```shell
#!/bin/bash

PURPLE='\033[0;35m'
DEFAULT='\033[0m'

echo -e "${PURPLE}Atualizando pacotes...${DEFAULT}"
apt update && apt upgrade -y
echo ""

echo -e "${PURPLE}=== Logs do Sistema ===${DEFAULT}"
echo "Data e Hora: $(date)"
echo ""

bash
```

![image](https://github.com/user-attachments/assets/fb13c0d4-29c9-4d90-a538-44cd7539c85a)

4.  t

```Dockerfile
FROM ubuntu:latest

COPY logs.sh /logs.sh
RUN chmod +x /logs.sh

CMD ["/logs.sh"]
```

![image](https://github.com/user-attachments/assets/e1c9c7fe-a872-4911-a71c-7980531afb71)

```bash
docker build -t ubuntu-logs .
```

```bash
docker run -it ubuntu-logs
```

![image](https://github.com/user-attachments/assets/c91762fb-019a-4c40-a67f-82e01d116690)

![image](https://github.com/user-attachments/assets/a3591bdd-70e5-4681-96b3-8fe490688f53)

---

## 3️⃣ Listando e removendo containers 🟢

[🔼 Voltar ao Sumário](#sumário-)

a. Liste todos os containers em execução e parados, pare um container
em execução e remova um container específico.

b. Exemplo de aplicação: Gerenciar containers de testes criados para
verificar configurações ou dependências.

---

## 4️⃣ Criando um Dockerfile para uma aplicação simples em Python 🟢

[🔼 Voltar ao Sumário](#sumário-)

a. Crie um Dockerfile para uma aplicação Flask que retorna uma
mensagem ao acessar um endpoint.

b. Exemplo de aplicação: Use a API de exemplo [Flask Restful API
Starter](https://github.com/gothinkster/flask-realworld-example-app) para criar um endpoint de teste.

---

# 🟡 Médio

## 5️⃣ Criando e utilizando volumes para persistência de dados 🟡

[🔼 Voltar ao Sumário](#sumário-)

a. Execute um container MySQL e configure um volume para armazenar
os dados do banco de forma persistente.

b. Exemplo de aplicação: Use o sistema de login e cadastro do [Laravel
Breeze](https://github.com/laravel/breeze), que usa MySQL.

---

## 6️⃣ Criando e rodando um container multi-stage 🟡

[🔼 Voltar ao Sumário](#sumário-)

a. Utilize um multi-stage build para otimizar uma aplicação Go,
reduzindo o tamanho da imagem final.

b. Exemplo de aplicação: Compile e rode a API do [Go Fiber Example](https://github.com/gofiber/recipes)
dentro do container.

---

## 7️⃣ Construindo uma rede Docker para comunicação entre containers 🟡

[🔼 Voltar ao Sumário](#sumário-)

a. Crie uma rede Docker personalizada e faça dois containers, um
Node.js e um MongoDB, se comunicarem.

b. Exemplo de aplicação: Utilize o projeto [MEAN Todos](https://github.com/drmikeh/mean-todos) para criar um
app de tarefas usando Node.js + MongoDB.

---

## 8️⃣ Criando um compose file para rodar uma aplicação com BD 🟡

[🔼 Voltar ao Sumário](#sumário-)

a. Utilize Docker Compose para configurar uma aplicação Django com
um banco de dados PostgreSQL.

b. Exemplo de aplicação: Use o projeto [Django Polls](https://github.com/ahmeddelattarr/PollsApp_django) App para criar
uma pesquisa de opinião integrada ao banco.

---

# 🔴 Difícil

## 9️⃣ Criando uma imagem personalizada com um servidor web e arquivos estáticos 🔴

[🔼 Voltar ao Sumário](#sumário-)

a. Construa uma imagem baseada no Nginx ou Apache, adicionando um
site HTML/CSS estático.

b. Exemplo de aplicação: Utilize a [landing page do Creative Tim](https://github.com/creativetimofficial/material-kit) para
criar uma página moderna hospedada no container

<p align="center">
  <br>
  <img src="https://github.com/user-attachments/assets/bb94fd8d-3b58-44e0-bb4a-d25f7bfd9da6" alt="CompassUOL Logo" width="250">
</p>
