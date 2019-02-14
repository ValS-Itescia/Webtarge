
def ecriture(filename,text):
    mail = open(filename,"a")
    mail.write(text)
    mail.close()

def lecture(filename,text):
    mail = open(filename,"r")
    print(mail.read())
    mail.close()




text="Test@test.com"+'\n'+"Test2@wanadoo.com"+'\n'+"Test3@orange.fr"+'\n'
filename="mail_list.txt"
ecriture(filename,text)
