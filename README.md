![image](https://github.com/user-attachments/assets/dd3e431f-4690-4a93-9b44-76aa48524dbf)> [!WARNING]
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

Execute um container usando a imagem do Nginx e acesse a página padrão no 
navegador. Use a [landing page do TailwindCSS](https://github.com/tailwindtoolbox/Landing-Page) como site estático dentro do 
container.

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

Inicie um container Ubuntu e interaja com o terminal dele. Teste um script Bash que 
imprime logs do sistema ou instala pacotes de forma interativa.

## 💡 Resolução Exercício 2

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

Liste todos os containers em execução e parados, pare um container em execução e 
remova um container específico.

## 💡 Resolução Exercício 3

![image](https://github.com/user-attachments/assets/d97a3b14-aa2a-43c4-a941-d1794c563086)

![image](https://github.com/user-attachments/assets/88621bce-f553-4cba-953b-6aa54a4ac9c1)

```bash
docker ps -a
```

```bash
docker stop ID
```

![image](https://github.com/user-attachments/assets/2d9c511f-7a43-453f-8ab8-55e93581d217)

```bash
docker rm ID
```

---

## 4️⃣ Criando um Dockerfile para uma aplicação simples em Python 🟢

[🔼 Voltar ao Sumário](#sumário-)

Crie um Dockerfile para uma aplicação Flask que retorna uma mensagem ao acessar 
um endpoint, para isso utilize o projeto [Docker Flask](https://awesome-compose/flask/app%20at%20master%20%C2%B7%20docker/awesome-compose)

## 💡 Resolução Exercício 4

---

# 🟡 Médio

## 5️⃣ Criando e utilizando volumes para persistência de dados 🟡

[🔼 Voltar ao Sumário](#sumário-)

Execute um container MySQL e configure um volume para armazenar os dados do 
banco de forma persistente. Para aplicar esse conceito você pode utilizar o [react-express-mysql](https://github.com/docker/awesome-compose/tree/master/react-express-mysql)

## 💡 Resolução Exercício 5

---

## 6️⃣ Criando e rodando um container multi-stage 🟡

[🔼 Voltar ao Sumário](#sumário-)

Utilize um multi-stage build para otimizar uma aplicação Go, reduzindo o tamanho 
da imagem final. Utilize para praticar o projeto [GS PING](https://github.com/docker/docker-gs-ping) desenvolvido em Golang.

## 💡 Resolução Exercício 6

---

## 7️⃣ Construindo uma rede Docker para comunicação entre containers 🟡

[🔼 Voltar ao Sumário](#sumário-)

Crie uma rede Docker personalizada e faça dois containers, um Node.js e um 
MongoDB, se comunicarem, sugestão, utilize o projeto [React Express + Mongo](https://github.com/docker/awesome-compose/tree/master/react-express-mongodb).

## 💡 Resolução Exercício 7

---

## 8️⃣ Criando um compose file para rodar uma aplicação com BD 🟡

[🔼 Voltar ao Sumário](#sumário-)

Utilize Docker Compose para configurar uma aplicação com um banco de 
dados PostgreSQL, use para isso o projeto [pgadmin](https://github.com/docker/awesome-compose/tree/master/postgresql-pgadmin).

## 💡 Resolução Exercício 8

---

# 🔴 Difícil

## 9️⃣ Criando uma imagem personalizada com um servidor web e arquivos estáticos 🔴

[🔼 Voltar ao Sumário](#sumário-)

Construa uma imagem baseada no Nginx ou Apache, adicionando um site 
HTML/CSS estático. Utilize a [landing page do Creative Tim](https://github.com/creativetimofficial/material-kit) para criar uma página 
moderna hospedada no container.

## 💡 Resolução Exercício 9

## 1️⃣0️⃣ Evitar execução como root 🔴

[🔼 Voltar ao Sumário](#sumário-)

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

---

## 💡 Resolução Exercício 10

## 1️⃣1️⃣ Analisar imagem Docker com Trivy 🔴

[🔼 Voltar ao Sumário](#sumário-)

Trivy é uma ferramenta open source para análise de vulnerabilidades em imagens 
Docker. Neste exercício, você irá analisar uma imagem pública, como python:3.9 ou 
node:16, em busca de vulnerabilidades conhecidas.
Você deverá:
a. Instalar o Trivy na sua máquina (via script ou pacote).
b. Rodar trivy image <nome-da-imagem> para analisar.
c. Identificar vulnerabilidades com severidade HIGH ou CRITICAL.
d. Anotar os pacotes ou bibliotecas afetadas e sugerir possíveis ações (como 
atualização da imagem base ou substituição de dependências).

---

## 💡 Resolução Exercício 11

## 1️⃣2️⃣ Corrigir vulnerabilidades encontradas 🔴

[🔼 Voltar ao Sumário](#sumário-)

Após identificar vulnerabilidades com ferramentas como o Trivy, o próximo passo é 
corrigi-las. Imagens grandes e genéricas frequentemente trazem bibliotecas 
desnecessárias e vulneráveis, além de usarem o usuário root por padrão. Neste 
exercício, você irá trabalhar com um exemplo de Dockerfile com más práticas e 
aplicar melhorias para construir uma imagem mais segura e enxuta. Identifique as 
melhorias e gere uma nova versão de Dockerfile.

![image](https://github.com/user-attachments/assets/635092a9-dbf1-4b8e-9da7-2b092801f2d2)

---

## 💡 Resolução Exercício 12

--- 

<p align="center">
  <br>
  <img src="https://github.com/user-attachments/assets/bb94fd8d-3b58-44e0-bb4a-d25f7bfd9da6" alt="CompassUOL Logo" width="250">
</p>
