## 1️⃣0️⃣ Evitar execução como root 🔴

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)

Ao rodar containers com o usuário root, você expõe seu sistema a riscos maiores em 
caso de comprometimento. Neste exercício, você deverá criar um Dockerfile para 
uma aplicação simples (como um script Python ou um servidor Node.js) e configurar 
a imagem para rodar com um usuário não-root.

Você precisará:

a. Criar um usuário com useradd ou adduser no Dockerfile.

b. Definir esse usuário como o padrão com a instrução USER.

c. Construir a imagem e iniciar o container.

d. Verificar se o processo está rodando com o novo usuário usando docker exec 
<container> whoami.

## 💡 Resolução Exercício 10
