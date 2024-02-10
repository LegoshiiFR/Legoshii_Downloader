print(
"""


> Veuillez sélectionner l'option que vous souhaitez :
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
        import urllib.request
        from rich.progress import Progress

        url = "https://github.com/LegoshiiFR/Legoshii_Downloader/releases/download/V1/TikGen-V1.zip"
        destination = 'TikGen-V1.zip'

        with Progress() as progress:
            task = progress.add_task("[cyan]Téléchargement en cours...", total=100)

            def download_hook(blocks_transferred, block_size, total_size):
                progress.update(task, advance=(blocks_transferred * block_size / total_size) * 100)

            urllib.request.urlretrieve(url, destination, reporthook=download_hook)

        print(">  Téléchargement réussi !")
elif nombre == 2:
    print("\n\n>Gen_Tools est un logiciels python permettant de générer des comptes (non mis à jour) ! \n> Souhaitez vous le télécharger ?")
    rps = input("[Y/N] : ")
    if rps == "Y" or rps == "y":
        import urllib.request
        from rich.progress import Progress

        url = "https://github.com/LegoshiiFR/Legoshii_Downloader/releases/download/V1/Gen_Tools.exe"
        destination = 'Gen_Tools.exe'

        with Progress() as progress:
            task = progress.add_task("[cyan]Téléchargement en cours...", total=100)

            def download_hook(blocks_transferred, block_size, total_size):
                progress.update(task, advance=(blocks_transferred * block_size / total_size) * 100)

            urllib.request.urlretrieve(url, destination, reporthook=download_hook)

        print(">  Téléchargement réussi !")
elif nombre == 3:
    print("\n\n>Video Converter est un logiciels python permettant de convertir des vidéos (payany) ! \n> Souhaitez vous l'acheter ?")
    rps = input("[Y/N] : ")
    if rps == "Y" or rps == "y":
        import webbrowser
        webbrowser.open("https://ko-fi.com/s/8d4991f5da")
else:
    print("Fermer le programme.")