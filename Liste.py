import Read_Write
import os

# Creation de ma liste et l'affiche
liste = ["test@test.fr","test@test.fr","test@orange.fr","test@free.fr"]
print(liste)

# fonction qui supprime les doublons de ma liste
def delete_duplicate(liste):
    liste = list(set(liste))
    return liste

# Affichage de ma liste sans doublons
liste_propre = delete_duplicate(liste)
print(liste_propre)

# -----------------------------------------
# Verification si email valide

def checkmail(mail):
    if "@" in mail and (mail[-4:] == ".com" or mail[-3:] == ".fr"):
        print("L'adresse mail est valide")
    else:
        print("L'adresse mail est invalide")


mail = "test@test.com"
checkmail(mail)

# -----------------------------------------
# Supprimer d'un mail

mail = "test@orange.fr"
def delete_mail(mail,liste):
    if mail in liste:
        liste.remove(mail)
    return liste

delete_mail(mail,liste)
print(liste)

# -----------------------------------------
# Ping une adresse mail
mail = "test@orange.fr"


def pingDomaineEmail(mail):
    ping = False
    domain = mail[mail.find("@"):]
    domaine = domain.replace("@","")
    reponse = os.system("ping -c 1 " + domaine)
    if reponse == 0:
        print(domaine," est accessible")
        ping = True
    else:
        print(domaine," est innacessible")
        ping = False
    return ping
pingDomaineEmail(mail)

# -----------------------------------------
