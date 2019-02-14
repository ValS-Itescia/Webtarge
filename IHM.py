from tkinter import filedialog
from tkinter import *
from Crawler_CSV import *
from Crawler import *
from Mail import *

fenetre = Tk()
# Dimensionnage de la fenetre
w = 900 # Largeur de la fenetre
h = 350 # Hauteur de la fenetre

# Recupere les infos de l'écran
ws = fenetre.winfo_screenwidth()
hs = fenetre.winfo_screenheight()

# Calcule les coordonnées X et Y de l'écran
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# Voir la dimension de l'écran et placer
fenetre.wm_geometry('%dx%d+%d+%d' % (w, h, x, y))

# Fin du dimensionnage de la fenetre


def OpenCSV():
    fenetretrois = Toplevel(fenetre)    # Ouvre une nouvelle fenêtre
    mail = StringVar()                  # Initialise une Variable
    # Ouvre un CSV et le lis
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    ListeMail = (crawl_csv(filename))
    #Construit un nouveau Label avec une variable changeante
    LabelMail = Label(fenetretrois, textvariable=mail)
    LabelMail.pack()
    #Séparation de la liste avec un argument ligne par ligne
    mail.set('\n'.join([str(myelement) for myelement in ListeMail ]))
    #Bouton qui lance la fonction PréparationMails
    boutonMailling = Button(fenetretrois, text="EnvoyerMail", command=lambda: PreparationMails(ListeMail))
    boutonMailling.pack()

    boutonQuit = Button(fenetretrois, text="Fermer", command=fenetretrois.destroy)
    boutonQuit.pack()




def OpenURL():
    mail = StringVar()  #Initialise une variable
    #Construit un nouveau label
    label = Label(fenetre, text="Saisissez votre URL")
    label.pack()
    #Construit un Entry pour récupérer l'url
    ligne_url = Entry(fenetre, width=90)
    ligne_url.pack()
    #Bouton qui lance la fonction ShowURl avec l'url en paramètre
    boutonURL2 = Button(fenetre, text="Valider URL", command=lambda: ShowURL(ligne_url.get()))
    boutonURL2.pack()

def ShowURL(url):
    mail = StringVar()  #Initialise une variable
    # Construit une nouvelle fenêtre"
    fenetredeux = Toplevel(fenetre)
    # Récupère les mails présent dans le code source de la page de l'url
    listeMail = crawler(url)

    LabelMail = Label(fenetredeux, textvariable=mail, width=100)
    LabelMail.pack()
    mail.set('\n'.join([str(myelement) for myelement in listeMail]))

    boutonMailling = Button(fenetredeux, text="EnvoyerMail", command=lambda: PreparationMails(listeMail))
    boutonMailling.pack()

    boutonQuit = Button(fenetredeux, text="Fermer", command=fenetredeux.destroy)
    boutonQuit.pack()

def PreparationMails(listeMail):
    listeMail = listeMail
    texte = StringVar()
    fenetreMail = Toplevel(fenetre)

    CMail = Label(fenetreMail, text="Ecrire corps du Mail")
    CMail.pack()

    CorpsMail = Text(fenetreMail, height=10)
    CorpsMail.pack()

    LabelLogin = Label(fenetreMail, text="Ecrire votre Login")
    LabelLogin.pack()

    Login = Entry(fenetreMail , text="Insérez votre Login")
    Login.pack()

    MDPLabel = Label(fenetreMail, text="Ecrire votre Mot De Passe")
    MDPLabel.pack()

    MDP = Entry(fenetreMail,text="Insérez votre mot de passe",show="*")
    MDP.pack()

    boutonContinue = Button(fenetreMail, text="Envoyer les Mails aux destinataires ?", command=lambda : EnvoisDesMails(listeMail,Login.get(),MDP.get(),CorpsMail.get()))
    boutonContinue.pack()
    boutonQuit = Button(fenetreMail, text="Retour", command=fenetreMail.destroy)
    boutonQuit.pack()

def EnvoisDesMails(listeMails,Login,MDP,Message):
    supprimerDoublon(listeMails)
    for mail in listeMails :
        EnvoiMail(Login, MDP, mail, Message)






label = Label(fenetre, text="Choisissez")
label.pack()

boutonCSV =Button(fenetre, text="Importer CSV", command= lambda: OpenCSV())
boutonCSV.pack()

boutonURL =Button(fenetre, text="Importer URL", command= lambda: OpenURL())
boutonURL.pack()

boutonQuit=Button(fenetre, text="Fermer", command=fenetre.quit)
boutonQuit.pack()

fenetre.mainloop()

