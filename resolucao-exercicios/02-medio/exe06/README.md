## 6️⃣ Criando e rodando um container multi-stage 🟡

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)

Utilize um multi-stage build para otimizar uma aplicação Go, reduzindo o tamanho 
da imagem final. Utilize para praticar o projeto [GS PING](https://github.com/docker/docker-gs-ping) desenvolvido em Golang.

## 💡 Resolução Exercício 6

01. Criar pasta do exercício 6 e entrar nela

```bash
mkdir exe06
```

```bash
cd exe06
```

![image](https://github.com/user-attachments/assets/29dff2c6-64f4-4c3e-b58a-e03e0068be02)

02. Pegar o link para clonar o repositório

![image](https://github.com/user-attachments/assets/a00f5ebc-bbc1-4504-9587-322b220a4092)

03. Coloque `git clone` antes do link copiado para executar o comando:

```bash
git clone https://github.com/docker/docker-gs-ping.git
```

04. Entrar dentro do diretório `docker-gs-ping`

```bash
cd docker-gs-ping
```

05. Remover o arquivo `Dockerfile` e `Dockerfile.multistage` para abrir o VSCode e criar um próprio

> [!NOTE]
> Senão não tem graça se já estivesse tudo pronto

```bash
rm Dockerfile
```

```bash
rm Dockerfile.multistage
```

![image](https://github.com/user-attachments/assets/0ce47619-dd5f-4f26-b0a2-73cb13608393)

06. Abra o VSCode

```bash
code .
```

06. Arquivo `Dockerfile`

```dockerfile
FROM golang:1.19

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY *.go ./

RUN CGO_ENABLED=0 GOOS=linux go build -o /docker-gs-ping

EXPOSE 8080

CMD [ "/docker-gs-ping" ]
```

![image](https://github.com/user-attachments/assets/c2399436-ece9-434b-acb0-354bfaa4ca6f)

06. Arquivo `Dockerfile.multistage`

![image](https://github.com/user-attachments/assets/f989363a-420a-4d4b-8600-15f3451c29b0)


```dockerfile
FROM golang:1.19 AS build-stage

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY *.go ./

RUN CGO_ENABLED=0 GOOS=linux go build -o /docker-gs-ping

FROM build-stage AS run-test-stage
RUN go test -v ./...

FROM gcr.io/distroless/base-debian11 AS build-release-stage

WORKDIR /

COPY --from=build-stage /docker-gs-ping /docker-gs-ping

EXPOSE 8080

USER nonroot:nonroot

ENTRYPOINT ["/docker-gs-ping"]
```

06. Subir um container COM multistage

```bash
docker build -t exe06-multi -f Dockerfile.multistage .
```

06. Subir um container SEM multistage

```bash
docker build -t exe06-normal -f Dockerfile .
```

![image](https://github.com/user-attachments/assets/18759ff4-aa6f-4d2c-aa94-ebac42aa252e)

07. Olhar o tamanho das imagens para ver a diferença

```bash
docker images | grep exe06-
```

![image](https://github.com/user-attachments/assets/ff229d38-3461-41de-8aa3-49ec56e6c1bc)

08. Rodar container COM multistage na porta 8080
  
```bash
docker run -d -p 8080:8080 --name gs-ping-multi exe06-multi
```

09. Rodar container SEM multistage na porta 8081

```bash
docker run -d -p 8081:8080 --name gs-ping-multi exe06-multi
```

![image](https://github.com/user-attachments/assets/617f97a2-c141-46d6-98c3-979bb734876d)

07. Abrir no navegador

```bash
curl http://localhost:8080 && echo
```

```bash
curl http://localhost:8081 && echo
```

> [!NOTE]
> Esses comandos são para serem executado no terminal

```bash
http://localhost:8080
```

```bash
http://localhost:8081
```

> [!NOTE]
> Esses são para copiar e colar no navegador

![image](https://github.com/user-attachments/assets/fdf17a42-94b0-4374-a0db-75d96f875ef7)

![image](https://github.com/user-attachments/assets/e7b2c1c7-ec59-419f-8e69-76bf9f464acf)
