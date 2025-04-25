## 1️⃣2️⃣ Corrigir vulnerabilidades encontradas 🔴

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)

Após identificar vulnerabilidades com ferramentas como o Trivy, o próximo passo é 
corrigi-las. Imagens grandes e genéricas frequentemente trazem bibliotecas 
desnecessárias e vulneráveis, além de usarem o usuário root por padrão. Neste 
exercício, você irá trabalhar com um exemplo de Dockerfile com más práticas e 
aplicar melhorias para construir uma imagem mais segura e enxuta. Identifique as 
melhorias e gere uma nova versão de Dockerfile.

![image](https://github.com/user-attachments/assets/635092a9-dbf1-4b8e-9da7-2b092801f2d2)

## 💡 Resolução Exercício 12

antes:

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
01

```bash
mkdir exe12
```

```bash
cd exe12
```

```bash
code .
```

02

![image](https://github.com/user-attachments/assets/9f874b8e-6336-4aba-ab27-f57b62d54c64)

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

03

![image](https://github.com/user-attachments/assets/be048749-1824-4691-a234-5499386ffbda)

```
flask==2.2.5
requests==2.32.0
urllib3==1.26.19
idna==3.7
setuptools==70.0.0
```

04

[Imagem Python utilizada](https://hub.docker.com/layers/library/python/3.9-slim/images/sha256-d57e6f8e0ed5afc48afda19a0a42728a45088d243259b1d8f589b05ed8eb4adb)

![image](https://github.com/user-attachments/assets/bce5a2f5-a7d4-46b6-926c-929b1b7643a8)

```dockerfile
# Use uma imagem base mais segura e atualizada
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

```bash
ls
```

```bash
docker build -t exe12-image .
```

```bash
docker run -d --name exe12-container -p 5000:5000 exe12-image
```

![image](https://github.com/user-attachments/assets/4a4c29cf-94d9-4fcf-b48f-519e556f9b8f)

```bash
http://localhost:5000
```

![image](https://github.com/user-attachments/assets/a1919456-716e-40d5-a2fe-aa4cc1819165)

```bash
docker exec -it exe12-container sh
```

```bash
whoami
```

```bash
groups
```

```bash
exit
```

![image](https://github.com/user-attachments/assets/846eeb0c-35a4-4949-ae54-32bb2dbc511c)

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

```
cat relatorio1.md
```

```
cat relatorio2.md
```

```
echo $(( $(wc -l < relatorio1.md) - 2 ))
```

```
echo $(( $(wc -l < relatorio2.md) - 2 ))
```



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
