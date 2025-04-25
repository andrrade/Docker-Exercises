## 9️⃣ Criando uma imagem personalizada com um servidor web e arquivos estáticos 🔴

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)

Construa uma imagem baseada no Nginx ou Apache, adicionando um site 
HTML/CSS estático. Utilize a [landing page do Creative Tim](https://github.com/creativetimofficial/material-kit) para criar uma página 
moderna hospedada no container.

## 💡 Resolução Exercício 9

01. Crie o diretório `exe09` e acesse-o:
   
![image02](https://github.com/user-attachments/assets/b16ef3c2-1ca0-487e-bf01-5ae3286e1c25)

Comandos Utilizados:

```bash
mkdir exe09
```

```bash
cd exe09
```

![image](https://github.com/user-attachments/assets/c311308a-86f8-49a6-8868-a2cd5ad12c45)

02. Clone o repositório que contém a [landing page do Creative Tim](https://github.com/creativetimofficial/material-kit)

![image](https://github.com/user-attachments/assets/2836bbfa-419f-437d-a53a-0102ada8f9e7)

03. Add `git clone` antes do link copiado

```bash
git clone https://github.com/creativetimofficial/material-kit.git
```

04. Entre na pasta `material-kit`

```bash
cd material-kit
```

05. Abra o VSCode com `code .` para criar o `Dockerfile`

```bash
code .
```

![image](https://github.com/user-attachments/assets/4105b1c4-e3d6-4105-af73-57155a9c0ff0)

06. Crie um arquivo Dockerfile

[Imagem Nginx](https://hub.docker.com/layers/library/nginx/stable-alpine/images/sha256-6566fca4271325b15a944d32e0bbdfab5fba0447713689d5a610d2c8077d3c9f)

![image](https://github.com/user-attachments/assets/9952c28c-b53b-4784-9be5-ab7b4c72b041)

```bash
FROM nginx:stable-alpine

RUN rm -rf /usr/share/nginx/html/*

COPY ./ /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```
  
07. Crie o container:

```bash
docker build -t exe09-image .
```

08. Rode o container

```bash
docker run -d -p 8080:80 --name exe09-container exe09-image
```

![image](https://github.com/user-attachments/assets/27dfbd47-beec-4077-9af2-ccd4d13367a4)

09. Acesse o navegador e digite:

```bash
http://localhost:8080
```

https://github.com/user-attachments/assets/4ecb5c68-4b9d-474b-bf3a-7736090a5b1a

10. Extra: Prova de que o container estava rodando:

```bash
docker ps
```

![image](https://github.com/user-attachments/assets/e877f96c-6da2-46d4-b042-7e73e8cea53f)

```bash
docker images
```

![image](https://github.com/user-attachments/assets/fcecb3ef-b3b7-46aa-a52e-803900b62c4e)
