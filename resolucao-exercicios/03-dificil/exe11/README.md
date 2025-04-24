## 1️⃣1️⃣ Analisar imagem Docker com Trivy 🔴

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)

Trivy é uma ferramenta open source para análise de vulnerabilidades em imagens 
Docker. Neste exercício, você irá analisar uma imagem pública, como python:3.9 ou 
node:16, em busca de vulnerabilidades conhecidas.

Você deverá:

a. Instalar o Trivy na sua máquina (via script ou pacote).

b. Rodar trivy image <nome-da-imagem> para analisar.

c. Identificar vulnerabilidades com severidade HIGH ou CRITICAL.

d. Anotar os pacotes ou bibliotecas afetadas e sugerir possíveis ações (como 
atualização da imagem base ou substituição de dependências).

## 💡 Resolução Exercício 11

a. [instalacao](https://trivy.dev/v0.57/getting-started/installation/)

```bash
sudo apt-get install wget gnupg
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | sudo tee /usr/share/keyrings/trivy.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb generic main" | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update
sudo apt-get install trivy
```

```bash
trivy --version
```

b. 
```bash
trivy image python:3.9
```

c. 
```bash
trivy image --severity HIGH,CRITICAL python:3.9
```

