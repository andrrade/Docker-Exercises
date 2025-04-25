## 2️⃣ Criando e rodando um container interativo 🟢

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)

Inicie um container Ubuntu e interaja com o terminal dele. Teste um script Bash que 
imprime logs do sistema ou instala pacotes de forma interativa.

## 💡 Resolução Exercício 2

01. Crie uma pasta para realizar o exercício 2

```bash
mkdir exe02
```

02. Entre nela

```bash
cd exe02/
```

03. Abra o VSCode

```bash
code .
```

![image](https://github.com/user-attachments/assets/c3546bb1-7e3b-4065-be46-180815e3849e)


04. Crie o arquivo `logs.sh`

![image](https://github.com/user-attachments/assets/19845e52-3425-473b-9c5b-adf953db6584)

```shell
#!/bin/bash

PURPLE='\033[0;35m'
DEFAULT='\033[0m'

echo -e "${PURPLE}Atualizando pacotes...${DEFAULT}"
apt update && apt upgrade -y
echo ""

echo -e "${PURPLE}=== Logs do Sistema ===${DEFAULT}"
echo "Data e Hora (Brasil): $(date '+%d/%m/%Y %H:%M:%S')"
echo ""

bash
```

05. Crie o arquivo `Dockerfile`

Selecionei a versão ubuntu:25.04: [Imagem Ubuntu](https://hub.docker.com/layers/library/ubuntu/25.04/images/sha256-9a302811bba2ae9533ddae0b563af29c112f1262329e508f13c0c532d5ba7c19)

![image](https://github.com/user-attachments/assets/9f1e590c-f2dc-4308-86c9-1528c5a549c1)

```Dockerfile
FROM ubuntu:25.04

ENV TZ="America/Sao_Paulo"

RUN apt-get update

RUN apt-get install -y tzdata

RUN dpkg-reconfigure --frontend noninteractive tzdata

COPY logs.sh /logs.sh
RUN chmod +x /logs.sh

CMD ["/logs.sh"]
```

06. Crie o container

```bash
docker build -t exe02 .
```

07. Rode ele

```bash
docker run -it exe02
```

![image](https://github.com/user-attachments/assets/ce57f0d2-6918-4de7-946e-37c318d61410)

08. Extra: Mostrei com `ls` que os comandos estão sendo realizados no terminal do container Ubuntu, para sair, basta digitar `exit`
