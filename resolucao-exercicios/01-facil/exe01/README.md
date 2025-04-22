## 1️⃣ Rodando um container básico 🟢

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)

Execute um container usando a imagem do Nginx e acesse a página padrão no 
navegador. Use a [landing page do TailwindCSS](https://github.com/tailwindtoolbox/Landing-Page) como site estático dentro do 
container.

## 💡 Resolução Exercício 1

01. Crie o diretório `exe01` e acesse-o:
   
![image02](https://github.com/user-attachments/assets/b16ef3c2-1ca0-487e-bf01-5ae3286e1c25)

Comandos Utilizados:

```bash
mkdir exe01
```

```bash
cd exe01
```

02. Clone o repositório que contém a [Landing-Page](https://github.com/tailwindtoolbox/Landing-Page)

![image03](https://github.com/user-attachments/assets/4fe22256-b6aa-443b-a2c3-ded601716844)

03. No final do link adicione um ponto `.` para copiar para o diretório atual:

```bash
git clone https://github.com/tailwindtoolbox/Landing-Page.git .
```

04. Remova os arquivos `README.md` e `LICENSE`

```bash
rm -f LICENSE README.md
```

05. Abra o VSCode com `code .` para criar o `Dockerfile`

```bash
code .
```
![image](https://github.com/user-attachments/assets/e306f9f6-c684-470c-a4ce-7f03586fdd8a)

06. Crie um arquivo Dockerfile

[Imagem Nginx](https://hub.docker.com/layers/library/nginx/stable-alpine/images/sha256-6566fca4271325b15a944d32e0bbdfab5fba0447713689d5a610d2c8077d3c9f)

![image](https://github.com/user-attachments/assets/e12c9ea6-8072-4029-abdd-ed17fb07ab23)

```bash
FROM nginx:stable-alpine
COPY . /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```
  
07. Crie o container:

```bash
docker build -t exe01 .
```

08. Rode o container

```bash
docker run -d -p 8080:80 --name container-exe01 exe01
```

![image](https://github.com/user-attachments/assets/ddb83720-d96a-4c10-84a1-712e41d986ed)

09. Acesse o navegador e digite:

```bash
http://localhost:8080
```

![image08](https://github.com/user-attachments/assets/2147565e-4ad2-4629-9780-ed38d11d1c21)

10. Extra: Prova de que o container estava rodando:

![image](https://github.com/user-attachments/assets/77297953-f4ad-494d-9adb-575d48ee8fee)
