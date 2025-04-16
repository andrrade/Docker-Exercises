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
- [8º Exercício](#8%EF%B8%8F⃣-criando-um-compose-file-para-rodar-uma-aplicação-com-banco-de-dados-)

## 🔴 Difícil

- [9º Exercício](#9%EF%B8%8F⃣-criando-uma-imagem-personalizada-com-um-servidor-web-e-arquivos-estáticos-)

---

# 🟢 Fácil

## 1️⃣ Rodando um container básico 🟢

[🔼 Voltar ao Sumário](#sumário-)

a. Execute um container usando a imagem do Nginx e acesse a página
padrão no navegador.

b. Exemplo de aplicação: Use a [landing page do TailwindCSS](https://github.com/tailwindtoolbox/Landing-Page) como site estático dentro do container.

---

## 2️⃣ Criando e rodando um container interativo 🟢

[🔼 Voltar ao Sumário](#sumário-)

a. Inicie um container Ubuntu e interaja com o terminal dele.

b. Exemplo de aplicação: Teste um script Bash que imprime logs do
sistema ou instala pacotes de forma interativa.

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

b. Exemplo de aplicação: Compile e rode a API do [Go Fiber Example](https://github.com/gofiber/recipes/tree/main/docker-multistage-build)
dentro do container.

---

## 7️⃣ Construindo uma rede Docker para comunicação entre containers 🟡

[🔼 Voltar ao Sumário](#sumário-)

a. Crie uma rede Docker personalizada e faça dois containers, um
Node.js e um MongoDB, se comunicarem.

b. Exemplo de aplicação: Utilize o projeto [MEAN Todos](https://github.com/luanphandinh/mean-todo) para criar um
app de tarefas usando Node.js + MongoDB.

---

## 8️⃣ Criando um compose file para rodar uma aplicação com BD 🟡

[🔼 Voltar ao Sumário](#sumário-)

a. Utilize Docker Compose para configurar uma aplicação Django com
um banco de dados PostgreSQL.

b. Exemplo de aplicação: Use o projeto [Django Polls](https://github.com/databases-io/django-polls) App para criar
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