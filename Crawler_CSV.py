import csv

def crawl_csv(monfichierexcel):
    contenu = []
    with open(monfichierexcel,'r') as lecture:
        sitewebs = csv.reader(lecture)
        for siteweb in sitewebs:
            contenu.append(sitewebs)
    print(contenu)
