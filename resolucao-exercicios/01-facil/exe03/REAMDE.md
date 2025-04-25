## 3️⃣ Listando e removendo containers 🟢

[🔼 Voltar ao Sumário](https://github.com/andrrade/Docker-Exercises-CompassUOL?tab=readme-ov-file#sum%C3%A1rio-)


Liste todos os containers em execução e parados, pare um container em execução e 
remova um container específico.

## 💡 Resolução Exercício 3

01. Liste todos os containers (em execução e parados)
  
```bash
docker ps -a
```

![image](https://github.com/user-attachments/assets/73bb4656-b11f-4759-8166-10303451f5cf)

02. Mostrando também no RancherDesktop que o container está rodando:

![image](https://github.com/user-attachments/assets/d24231fb-b5c8-4856-91e6-0c44decd6aff)

03. Parando o container em execução: `container-exe01`

```bash
docker stop <ID_DO_CONTAINER>
```

04. Mostrando que o container está parado
![image](https://github.com/user-attachments/assets/3b5d42da-8e9b-48cb-b359-17fa258d5d1b)

05. Mostrando também no RancherDesktop
![image](https://github.com/user-attachments/assets/54aa6939-a5a9-423f-90c1-3522b012131f)


06. Removendo o container: `container-exe01`
   
```bash
docker rm <ID_DO_CONTAINER>
```

07. Mostrando que o container foi removido:
  
![image](https://github.com/user-attachments/assets/84487fb5-c5ae-490f-a0f5-cc756b765de1)

08. Mostrando também no RancherDesktop
![image](https://github.com/user-attachments/assets/089e5dda-3e0d-4bdc-9eb1-194baae1e861)
