## 1️⃣2️⃣ Corrigir vulnerabilidades encontradas 🔴

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)

Após identificar vulnerabilidades com ferramentas como o Trivy, o próximo passo é 
corrigi-las. Imagens grandes e genéricas frequentemente trazem bibliotecas 
desnecessárias e vulneráveis, além de usarem o usuário root por padrão. Neste 
exercício, você irá trabalhar com um exemplo de Dockerfile com más práticas e 
aplicar melhorias para construir uma imagem mais segura e enxuta. Identifique as 
melhorias e gere uma nova versão de Dockerfile.

![image](https://github.com/user-attachments/assets/635092a9-dbf1-4b8e-9da7-2b092801f2d2)

```dockerfile
# Dockerfile vulnerável
FROM python:3.9 
WORKDIR /app 
COPY requirements.txt . 
RUN pip install --r requirements.txt
COPY . . 
CMD ["python", "app.py"]
```

```txt
flask==1.1.1
requests==2.22.0
```

## 💡 Resolução Exercício 12

01. Crie um diretório chamado `exe12` e entre nele

```bash
mkdir exe12
```

```bash
cd exe12
```

02. Abra o VSCode
   
```bash
code .
```

![image](https://github.com/user-attachments/assets/1d65a434-e601-48d7-9a8c-20c83ef3161d)

03. Crie o arquivo `app.py`

![image](https://github.com/user-attachments/assets/8b3d2f0b-9bba-4fbc-883d-6bd0a071bf9e)

```py
from flask import Flask
import os
import grp
import pwd

app = Flask(__name__)

@app.route("/")
def hello():
    user_name = os.getenv("USER", "Usuário não encontrado")
    
    user_group_id = os.getgid()
    group_name = grp.getgrgid(user_group_id).gr_name
    
    user_info = pwd.getpwuid(os.getuid())
    username = user_info.pw_name
    
    return f"Olá, mundo! Rodando como usuário: {username} no grupo: {group_name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

04. Crie o arquivo `requirements.txt`

![image](https://github.com/user-attachments/assets/b23b37f1-7d40-4129-a41b-9d6458bc6a6c)

```
flask==2.2.5
requests==2.32.0
urllib3==1.26.19
idna==3.7
setuptools==70.0.0
```

05. Crie o arquivo `Dockerfile`

[Imagem Python utilizada](https://hub.docker.com/layers/library/python/3.9-slim/images/sha256-d57e6f8e0ed5afc48afda19a0a42728a45088d243259b1d8f589b05ed8eb4adb)

![image](https://github.com/user-attachments/assets/886e3e07-a3b2-466a-a62e-20bca31fd00b)

```dockerfile
# Dockerfile Melhorado
FROM python:3.9-slim

RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y && apt-get clean

RUN apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libpq-dev \
    perl-base \
    zlib1g \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade setuptools==70.0.0

RUN groupadd -r grupoTeste && useradd -r -g grupoTeste userTeste

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R userTeste:grupoTeste /app

USER userTeste

EXPOSE 5000

CMD ["python", "app.py"]
```

06. Verifique se os arquivos foram criados corretamente
   
```bash
ls
```

07. Suba o container
   
```bash
docker build -t exe12-image .
```

```bash
docker run -d --name exe12-container -p 5000:5000 exe12-image
```

![image](https://github.com/user-attachments/assets/74b072c1-255a-4184-a70a-dffd4ef33edb)

08. Acesse pelo navegador
   
```bash
http://localhost:5000
```

![image](https://github.com/user-attachments/assets/a1919456-716e-40d5-a2fe-aa4cc1819165)

09. Abra o terminal
    
```bash
docker exec -it exe12-container sh
```

10. Verfique se não é o root
    
```bash
whoami
```

```bash
groups
```

11. Saia do terminal
    
```bash
exit
```

![image](https://github.com/user-attachments/assets/846eeb0c-35a4-4949-ae54-32bb2dbc511c)

12. Compare a imagem usada anteriormente com a nova que foi desenvolvida

a. Gere o relatório da imagem anterior

```bash
trivy image --severity HIGH,CRITICAL --format json python:3.9 > resultado1.json
```

```bash
jq -r '
  "| Pacote | Versão atual | Correção disponível | Severidade | Ação sugerida |",
  "|--------|--------------|---------------------|------------|---------------|",
  (.Results[] | select(.Vulnerabilities != null) | .Vulnerabilities[] |
    "| \(.PkgName) | \(.InstalledVersion) | \(.FixedVersion // "❌ Não") | \(.Severity) | \(
      if .FixedVersion then
        "Atualizar para a versão \(.FixedVersion)"
      else
        "Considerar substituição ou monitorar atualizações futuras"
      end
    ) |"
  )
' resultado1.json | uniq | column -t -s '|' > relatorio1.md
```

![image](https://github.com/user-attachments/assets/f829d218-3c3a-4c1d-aeaf-ff3034c228ae)

b. Gere o relatório da nova imagem 

```bash
trivy image --severity HIGH,CRITICAL --format json exe12-image > resultado2.json
```

```bash
jq -r '
  "| Pacote | Versão atual | Correção disponível | Severidade | Ação sugerida |",
  "|--------|--------------|---------------------|------------|---------------|",
  (.Results[] | select(.Vulnerabilities != null) | .Vulnerabilities[] |
    "| \(.PkgName) | \(.InstalledVersion) | \(.FixedVersion // "❌ Não") | \(.Severity) | \(
      if .FixedVersion then
        "Atualizar para a versão \(.FixedVersion)"
      else
        "Considerar substituição ou monitorar atualizações futuras"
      end
    ) |"
  )
' resultado2.json | uniq | column -t -s '|' > relatorio2.md
```

![image](https://github.com/user-attachments/assets/81874f48-2e2b-45a8-991b-cde7d01e5720)

c. Veja o relatório da imagem anterior

```
cat relatorio1.md
```

![image](https://github.com/user-attachments/assets/1316bf94-7b45-4a79-94ac-0b76990049ce)

d. Veja o relatório da nova imagem
```
cat relatorio2.md
```

![image](https://github.com/user-attachments/assets/e7f694b2-6d43-448f-b9a4-5fad014dacb6)

e. Liste o número de vulnerabilidades da imagem anterior

> [!NOTE]
> Tirei 2 porque são as linhas do cebeçalho

```
echo $(( $(wc -l < relatorio1.md) - 2 ))
```

f. Liste o número de vulnerabilidades da nova imagem

```
echo $(( $(wc -l < relatorio2.md) - 2 ))
```

![image](https://github.com/user-attachments/assets/efa07922-a573-4ca6-b2cc-62d49cde7b45)

### Conclusão do Exercício
Após identificar vulnerabilidades com ferramentas como o **Trivy**, o próximo passo foi corrigir as falhas e otimizar o Dockerfile para construir uma imagem mais segura e eficiente.

**Problemas Iniciais:**
- Imagens genéricas, como `python:3.9`, frequentemente contêm pacotes desnecessários que podem ser vulneráveis.
- O uso do usuário `root` por padrão aumenta o risco de escalonamento de privilégios e a exposição a falhas de segurança.
- Dependências desnecessárias podem ser instaladas sem critério, aumentando o tamanho da imagem e as potenciais vulnerabilidades.

---

### **Melhorias Implementadas:**

1. **Escolha de uma Imagem Base Mais Segura e Atualizada:**
   - Optei por utilizar a imagem `python:3.9-slim`, uma versão mais enxuta, com menos pacotes instalados por padrão, o que reduz a superfície de ataque. Além disso, ela está sempre atualizada, garantindo que os pacotes de sistema estejam na versão mais recente, com as correções de segurança já aplicadas.

2. **Redução do Tamanho da Imagem e Melhora na Segurança:**
   - Ao instalar pacotes com `apt-get`, removi as listas de pacotes (`rm -rf /var/lib/apt/lists/*`), evitando que arquivos desnecessários ficassem na imagem final, o que ajuda a mantê-la mais enxuta e segura.
   - Usei a flag `--no-install-recommends` para instalar apenas os pacotes essenciais, evitando que dependências adicionais e potencialmente vulneráveis fossem incluídas na imagem.

3. **Segurança de Usuário:**
   - Criei um usuário específico (`userTeste`) e um grupo (`grupoTeste`) para rodar a aplicação. Essa prática reduz o risco de escalonamento de privilégios, pois a aplicação não será executada como `root`. Isso também segue uma das boas práticas de segurança recomendadas no uso de containers.

4. **Gerenciamento de Dependências:**
   - Atualizei o `setuptools` para a versão mais recente e instalei as dependências do projeto diretamente do arquivo `requirements.txt`, garantindo que o ambiente estivesse sempre atualizado sem usar o cache de pacotes, o que contribui para uma imagem mais enxuta e sem dependências desnecessárias.

---

### **Resultados:**

Após implementar as melhorias, comparei a imagem anterior, que usava a versão `python:3.9`, com a nova imagem criada (`exe12-image`). O resultado foi significativo:

- **Imagens Analisadas:**
  - A imagem anterior, baseada em `python:3.9`, apresentou **46 pacotes** com severidade **high** ou **critical**, mostrando que existiam várias vulnerabilidades e atualizações pendentes.
  - A nova imagem, `exe12-image`, apresenta apenas **7 pacotes** com severidade **high** ou **critical**. Isso demonstra uma grande redução nas vulnerabilidades após a aplicação das melhorias de segurança.

- **Ações Sugeridas:**
  - Nenhuma ação sugerida pela nova versão é de atualização, já que todas as versões de pacotes essenciais estão atualizadas. O único alerta que permanece é "Considerar substituição ou monitorar atualizações futuras", o que indica que, apesar de estarmos em uma versão mais segura, há sempre a necessidade de monitorar novas vulnerabilidades ou atualizações nos pacotes no futuro.
  
Essa comparação mostra a efetividade das práticas de segurança e otimização aplicadas, que resultaram em uma imagem significativamente mais segura e com menos vulnerabilidades conhecidas.
