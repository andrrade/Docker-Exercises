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
