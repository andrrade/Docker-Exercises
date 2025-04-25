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