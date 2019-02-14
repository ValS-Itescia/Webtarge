import urllib.request
import re
import csv

# fonction
def crawler(url):
    web = urllib.request.urlopen(url).read()
    mails = re.findall("[\w.-]+@[\w.-]+",str(web))
    return supprimerDoublon(mails)

def supprimerDoublon(liste):
    liste = list(set(liste))
    return liste

