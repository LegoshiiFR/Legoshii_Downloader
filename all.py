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
    print("\n>TikGen est un logiciels python permettant de télécharger, modifier, créer des vidéos TikTok gratuitement ! \n> Souhaitez vous le télécharger ?")
    rps = input("[Y/N] : ")
    if rps == "Y":
        print("Téléchargement en cours...")
        import urllib.request
        urllib.request.urlretrieve("https://legoshii.iglao.fr/shop/storage/TikGen-V1.zip", 'TikGen-V1.zip')
        print("Téléchargement réussi !")
    else:
        print("Fermer le programme.")