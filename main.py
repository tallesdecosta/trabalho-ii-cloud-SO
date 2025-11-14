from flask import Flask, jsonify
import os
import platform
import psutil
import json

app = Flask(__name__)

TEAM_MEMBERS = {
    "equipe": "Equipe: Danton Talles, Gabriel Losekann",
    "autores": [
        "Danton Talles",
        "Gabriel Losekann"
    ]
}

@app.route('/info')
def info():

    return jsonify(TEAM_MEMBERS)

@app.route('/metricas')
def metricas():

    pid = os.getpid()
    proc = psutil.Process(pid)
    mem_mb = round(proc.memory_info().rss / (1024 ** 2), 2)
    cpu_percent = psutil.cpu_percent(interval=0.1)
    os_info = f"{platform.system()} ({platform.release()})"

    data = {
        "equipe": TEAM_MEMBERS['equipe'],  # Item 3a
        "pid": pid,                        # Item 3b
        "memoria_usada_mb": mem_mb,        # Item 3c
        "cpu_percent": cpu_percent,        # Item 3d
        "sistema_operacional": os_info     # Item 3e
    }
    
    return jsonify(data)

@app.route('/')
def index():
    
    pid = os.getpid()
    proc = psutil.Process(pid)
    mem_mb = round(proc.memory_info().rss / (1024 ** 2), 2)
    cpu_percent = psutil.cpu_percent(interval=0.1)
    os_info = f"{platform.system()} ({platform.release()})"

    return f"""
    <div style="font-family: sans-serif;">
        <p><strong>Nome:</strong> {TEAM_MEMBERS['equipe']}</p>
        <p><strong>PID:</strong> {pid}</p>
        <p><strong>Memória usada:</strong> {mem_mb} MB</p>
        <p><strong>CPU:</strong> {cpu_percent}%</p>
        <p><strong>Sistema Operacional:</strong> {os_info}</p>
    </div>
    """

if __name__ == '__main__':

    app.run(debug=True, port=5000)

