import os
from datetime import datetime

print("✅ Container rodando como userTeste!")
print(f"👤 UID/GID: {os.getuid()}/{os.getgid()}")
print(f"👤 whoami: {os.popen('whoami').read().strip()}")
print(f"👤 id: {os.popen('id').read().strip()}")

hora_execucao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"⏰ Horário de execução: {hora_execucao}")

print("👋 Fim do script")

# Mantém o container rodando (Ctrl + C para parar)
while True:
    pass 