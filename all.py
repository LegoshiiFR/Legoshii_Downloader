import os
os.system(f"title 🔎 Legoshii Downloader - Téléchargement des packages")
def __main__():
    os.system("cls")
    print(
    """[📦] : Version 1.0.3
[📁] : Legoshii Downloader - Téléchargement des packages
[📄] : Choissisez et télécharger les logiciels :

[1] : TikGen (Python)
[2] : Gen_Tools (Python)
[3] : Video Converter (Python)
"""    
    )
    nombre = float(input("Entrez un nombre : "))
    if nombre == 1:
        print("\n\n>TikGen est un logiciels python permettant de télécharger, modifier, créer des vidéos TikTok gratuitement ! \n> Souhaitez vous le télécharger ?")
        rps = input("[Y/N] : ")
        if rps == "Y" or rps == "y":
            if os.path.exists('TikGen-V1.zip'):
                os.remove('TikGen-V1.zip')
                download('TikGen')
            else:
                download('TikGen')
    elif nombre == 2:
        print("\n\n>Gen_Tools est un logiciels python permettant de générer des comptes (non mis à jour) ! \n> Souhaitez vous le télécharger ?")
        rps = input("[Y/N] : ")
        if rps == "Y" or rps == "y":
            if os.path.exists('Gen_Tools.exe'):
                os.remove('Gen_Tools.exe')
                download('Gen_Tools')
            else:
                download('Gen_Tools')
    elif nombre == 3:
        print("\n\n>Video Converter est un logiciels python permettant de convertir des vidéos (payany) ! \n> Souhaitez vous l'acheter ?")
        rps = input("[Y/N] : ")
        if rps == "Y" or rps == "y":
            download('Video_Converter')
    else:
        print("Fermer le programme.")
def download(logiciel):
    import time
    import urllib.request
    if logiciel == 'TikGen':
        url = "https://github.com/LegoshiiFR/Legoshii_Downloader/releases/download/V1/TikGen-V1.zip"
        destination = 'TikGen-V1.zip'
    elif logiciel == 'Gen_Tools':
        url = "https://github.com/LegoshiiFR/Legoshii_Downloader/releases/download/V1/Gen_Tools.exe"
        destination = 'Gen_Tools.exe'
    elif logiciel == 'Video_Converter':
         import webbrowser
         webbrowser.open("https://ko-fi.com/s/8d4991f5da")
    from rich.progress import Progress
    with Progress() as progress:
        task = progress.add_task("[cyan]Téléchargement en cours...", total=100)
        def download_hook(blocks_transferred, block_size, total_size):
            progress.update(task, advance=(blocks_transferred * block_size / total_size) * 100)
        urllib.request.urlretrieve(url, destination, reporthook=download_hook)

    print("\n>  Téléchargement réussi !")
    time.sleep(3)
    __main__()
__main__()