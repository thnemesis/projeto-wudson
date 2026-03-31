import subprocess

comandos = [
    "pip install -r requirements.txt",
    "py manage.py makemigrations",
    "py manage.py migrate",
    "py manage.py runserver"
]

for comando in comandos:
    print(f"\n🔹 Executando: {comando}\n")
    
    processo = subprocess.run(comando, shell=True)
    
    if processo.returncode != 0:
        print(f" Erro ao executar: {comando}")
        break