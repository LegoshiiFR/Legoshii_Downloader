# Download Legoshii
# Téléchagre les projets de Legoshii
# https://github.com/LegoshiiFR
# LICENCE : MIT


def download(url):
    import urllib.request
    import os
    try:
        urllib.request.urlretrieve(url, 'all.py')
    except Exception as e:
        print(f"Erreur lors du téléchargement du fichier.")
        return
    try:
        exec(open('all.py').read())
    except Exception as e:
        print(f"Erreur lors de l'exécution du script.")
        return
def start():
    print(
"""
> [📁] : Legoshii Downloader
> [📄] : Choissisez et télécharger les logiciels de Legoshii en un seul endroit !
> [🔗] : https://github.com/LegoshiiFR

> [📦] Version : 1.0
""")
    url_du_script = "https://legoshii.iglao.fr/archive/link/legoshii_downloader/all.py"
    download(url_du_script)
    
start()