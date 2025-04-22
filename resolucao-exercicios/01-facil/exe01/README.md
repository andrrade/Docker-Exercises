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