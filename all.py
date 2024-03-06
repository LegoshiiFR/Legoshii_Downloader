import os
os.system(f"title 🔎 Legoshii Downloader - Téléchargement des packages")
def __main__():
    import time
    import datetime
    os.system("cls")
    current_time = datetime.datetime.now().strftime("%d-%m %H:%M:")
    print(
    """[📦] : Version 1.0.4
[📁] : Legoshii Downloader - Téléchargement des packages
[📄] : Choissisez et télécharger les logiciels :

[🕰️] : {}

[1] : TikGen (Python)
[2] : Gen_Tools (Python)
[3] : Video Converter (Python)
[4] : Custom_Installer
[5] : Anime Downloader
""".format(current_time)
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
        else:
            os.system("cls")
            __main__()
    elif nombre == 2:
        print("\n\n>Gen_Tools est un logiciels python permettant de générer des comptes (non mis à jour) ! \n> Souhaitez vous le télécharger ?")
        rps = input("[Y/N] : ")
        if rps == "Y" or rps == "y":
            if os.path.exists('Gen_Tools.exe'):
                os.remove('Gen_Tools.exe')
                download('Gen_Tools')
            else:
                download('Gen_Tools')
        else:
            os.system("cls")
            __main__()
    elif nombre == 3:
        print("\n\n>Video Converter est un logiciels python permettant de convertir des vidéos (payany) ! \n> Souhaitez vous l'acheter ?")
        rps = input("[Y/N] : ")
        if rps == "Y" or rps == "y":
            download('Video_Converter')
        else:
            os.system("cls")
            __main__()
    elif nombre == 4:
        print("\n\n Custom_Installer est un programme vous permettant de créer votre propre installateur de logiciel ou de fichier (un setup) ! \n> Souhaitez vous l'utiliser ?")
        rps = input("[Y/N] : ")
        if rps == "Y" or rps == "y":
            download('Custom_Installer')
        else:
            os.system("cls")
            __main__()
    elif nombre == 5:
        print("\n\n Anime Downloader est un programme vous permettant de télécharger vos animés en un seul endroit et rapidement ! \n> Souhaitez vous l'utiliser ?")
        rps = input("[Y/N] : ")
        if rps == "Y" or rps == "y":
            download('Anime_Downloader')
        else:
            os.system("cls")
            __main__()
    else:
        print("Fermer le programme.")
        time.sleep(2)
        os.system("exit")
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
    elif logiciel == 'Custom_Installer':
        import webbrowser
        webbrowser.open("https://legoshii.iglao.fr/project/custom_installer")
    elif logiciel == 'Anime_Downloader':
        import webbrowser
        webbrowser.open("https://legoshii.iglao.fr/archive/anime_downloader")
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