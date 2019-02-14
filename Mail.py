import smtplib
from Liste import *


def EnvoiMail(Login,MotDePasse,Receveur,CorpsMail):
    if (pingDomaineEmail(Receveur) == True):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(Login, MotDePasse)
        server.sendmail(Login, Receveur, CorpsMail)
        server.quit()
    else :
        print("L'adresse",Receveur,"est invalide.")


