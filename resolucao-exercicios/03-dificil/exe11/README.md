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

1. Criar um diretório chamado `exe11` e entrar nele

```bash
mkdir exe11
```

```bash
cd exe11
```

![image](https://github.com/user-attachments/assets/7384948b-78fa-4013-986e-0f32d1f5ede0)

### a. Instalar o Trivy

1. Verificar e Atualizar pacotes

```bash
sudo apt update -y && sudo apt upgrade -y
```

![image](https://github.com/user-attachments/assets/98a38f2c-429d-4088-94ce-5a81209c5399)

2. Fazer a instalação do Trivy

[Documentação da Instalação do Trivy](https://trivy.dev/v0.57/getting-started/installation/)

```bash
sudo apt-get install wget gnupg
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | sudo tee /usr/share/keyrings/trivy.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb generic main" | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update
sudo apt-get install trivy
```

![image](https://github.com/user-attachments/assets/95fe255d-48e8-4f07-b9db-3789556cda85)

3. Verificar se foi instalado corretamente

```bash
trivy --version
```

![image](https://github.com/user-attachments/assets/90a9539c-805f-4303-9e75-a30f71f31ac3)

### b. Rodar trivy image <nome-da-imagem> para analisar
> [!NOTE]
> A imagem escolhida foi `python:3.9`

```bash
trivy image python:3.9
```

![image](https://github.com/user-attachments/assets/bc904a06-b0d7-40b6-91d1-3a4729d212af)

### c. Filtrar por vulnerabilidades com severidade HIGH ou CRITICAL

```bash
trivy image --severity HIGH,CRITICAL python:3.9
```

![image](https://github.com/user-attachments/assets/9edfdd79-16fa-4568-9c7e-2147ea8811c4)

### d. Anotar os pacotes ou bibliotecas afetadas e sugerir possíveis ações

> [!IMPORTANT]
> Preferi deixar essa parte automatizada, segue os comandos abaixo:

1. Executar o Trivy e salvar a saída em JSON

```bash
trivy image --severity HIGH,CRITICAL --format json python:3.9 > resultado.json
```

```bash
ls
```

![image](https://github.com/user-attachments/assets/52f795d3-0b58-402a-ae9d-5f074f4a6869)

2. Processar o JSON e gerar o relatório em Markdown

```bash 
jq -r '[
    "| Pacote | Versão atual | Correção disponível | Severidade | Ação sugerida |",
    "|--------|--------------|---------------------|------------|---------------|",
    (.Results[] | .Vulnerabilities[] | 
      "| \(.PkgName) | \(.InstalledVersion) | \(.FixedVersion // "❌ Não") | \(.Severity) | \(
        if .FixedVersion then 
          "Atualizar para a versão \(.FixedVersion)" 
        else 
          "Considerar substituição ou monitorar atualizações futuras" 
        end
      ) |"
    )
  ] | .[]' resultado.json > relatorio.md
```

```bash
ls
```
![image](https://github.com/user-attachments/assets/e4886506-ef09-4e74-945b-7bd1f9102311)

3. Ler o arquivo criado

```bash
cat relatorio.md | column -t -s '|'
```

![image](https://github.com/user-attachments/assets/61fdd246-1427-4b22-8de3-b8fa3c0835b0)
