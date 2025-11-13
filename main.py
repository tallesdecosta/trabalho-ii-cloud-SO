from flask import Flask
import os
import platform
import psutil
import json

app = Flask(__name__)

@app.route('/info')
def info():

    # (a) Integrantes
    team_members = "Equipe: Danton Talles, Gabriel Losekann"

    return f"""
    <div style="font-family: sans-serif;">
        <h1>Info</h1>
        <p>{team_members}</p>
    </div>
    """

@app.route('/metricas')
def metricas():

    process_id = os.getpid()
    
    current_process = psutil.Process(process_id)
    
    memory_info = current_process.memory_info()
    memory_usage_mb = memory_info.rss / (1024 ** 2)
    
    cpu_usage_percent = psutil.cpu_percent(interval=0.1)
    
    os_system = platform.system()
    os_release = platform.release()
    os_info = f"{os_system} {os_release}"


    return f"""
    <div style="font-family: sans-serif;">
        <h1>Metricas</h1>
        <p>
        {
            {
                'PID': os.getpid(), 
                'Memoria': memory_usage_mb,
                'Uso de CPU': cpu_usage_percent,
                'SO': os_info
            }
        }
        </p> 
    </div>
"""

@app.route('/')
def index():
    """
    Rota principal que exibe métricas do sistema.
    """

    process_id = os.getpid()
    
    current_process = psutil.Process(process_id)
    
    memory_info = current_process.memory_info()
    memory_usage_mb = memory_info.rss / (1024 ** 2)
    
    cpu_usage_percent = psutil.cpu_percent(interval=0.1)
    
    os_system = platform.system()
    os_release = platform.release()
    os_info = f"{os_system} {os_release}"

    return f"""
    <div style="font-family: sans-serif;">
        <h1>Monitoramento de Sistema</h1>
        <hr>
        <p>PID: {process_id}</p>
        <p>Memória (RSS): {memory_usage_mb:.2f} MB</p>
        <p>Uso de CPU: {cpu_usage_percent}%</p>
        <p>SO:{os_info}</p>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True, port=5000)