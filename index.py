# Download Legoshii
# Téléchagre les projets de Legoshii
# https://github.com/LegoshiiFR
# LICENCE : MIT

# Véirification des modules
import importlib.util
import subprocess

if importlib.util.find_spec('rich') is None:
    print("Le module 'rich' n'est pas installé. Téléchargement en cours...")
    subprocess.run(["pip", "install", "rich"])

if importlib.util.find_spec('requests') is None:
    print("Le module 'requests' n'est pas installé. Téléchargement en cours...")
    subprocess.run(["pip", "install", "requests"])

def download(url):
    import urllib.request
    urllib.request.urlretrieve(url, 'all.py')
def start():
    import os
    import requests
    import time
    os.system(f"title 🔎 Legoshii Downloader - Gestionnaire de package")
    try:
        requests.get("http://www.google.com", timeout=5)
    except requests.ConnectionError:
        print("Pas de connexion Internet. Fermeture du programme ...")
        os.system("quit")
    print(
"""
> [📁] : Legoshii Downloader - Gestionnaire de package
> [📄] : Choissisez et télécharger les logiciels de Legoshii en un seul endroit !
> [🔗] : https://github.com/LegoshiiFR

> [📦] Version : 1.0
""")
    import time
    import subprocess
    time.sleep(2)
    from rich.progress import Progress
    with Progress() as progress:

        task = progress.add_task("[cyan]Chargement en cours...", total=100)

        for i in range(100):
            progress.update(task, advance=1)
            time.sleep(0.02)
    if os.path.exists('all.py'):
        os.remove('all.py')
    url_du_script = "https://github.com/LegoshiiFR/Legoshii_Downloader/releases/download/V1/all.py"
    download(url_du_script)
    os.system("cls")
    subprocess.run(["python", "all.py"])
    
start()