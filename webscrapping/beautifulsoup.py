from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR')

url_jo='https://www.legifrance.gouv.fr/affichJO.do?idJO=JORFCONT000041804056'
soup_jo = BeautifulSoup(requests.get(url_jo).text, 'html5lib')

#Chercher le titre "Avis divers" dans son titre parent "Avis et communications" et s'y positionner
avis_divers_li=soup_jo.find("h4", text="Avis divers").find_parent('li')

#Chercher le titre "Ministère des solidarités et de la santé" dans son titre parent "Avis divers" et s'y positionner
min_sante_li=avis_divers_li.find("h5",text="Ministère des solidarités et de la santé").find_parent('li')

article_list_li=min_sante_li.find('ul').findAll('li')
article_list=[]
for li in article_list_li:
    i=li.find("a").text
    j=li.span["resource"]
    article_list.append((i,j))

def is_cip(i,j):
    return (i=='Avis relatif aux prix de spécialités pharmaceutiques'or i=="Avis relatif aux prix d'une spécialité pharmaceutique")

"""for i,j in article_list:"
   if is_cip(i,j):
       url=j
       soup = BeautifulSoup(requests.get(url).text, 'html5lib')"""


url = "https://www.legifrance.gouv.fr/affichTexte.do;jsessionid=1A545D8BEAEBF39CFD601BB3311B19B2.tplgfr23s_3?cidTexte=JORFTEXT000041804784&dateTexte=&oldAction=rechJO&categorieLien=id&idJO=JORFCONT000041804056"
soup = BeautifulSoup(requests.get(url).text, 'html5lib')

# Chercher la date du JO < div class ="enteteTexte" >
jo= soup.find('div',attrs={'class': 'enteteTexte'}).text
texte= soup.find('div', attrs={'class': 'article'}).p.text

table = soup.find('tbody')
output_rows = []
for table_row in table.findAll('tr'):
    if table_row.find('td'):
        cells_data = table_row.findAll('td')
        output_row = []
        for column in cells_data:
            output_row.append(column.text.replace("\n",""))
        my_jo_date=jo.replace("\n"," ").replace("\t","").strip().split(' ')[3:6]
        my_jo_date=' '.join(my_jo_date)
        my_jo_date= datetime.strptime(my_jo_date,'%d %B %Y')
        output_row.append(my_jo_date)
        output_row.append(jo.replace("\n"," ").replace("\t","").strip())
        output_row.append(texte.replace("\n", " ").replace("\t", "").strip())
        output_row=tuple(output_row)
        output_rows.append(output_row)


panda_data=pd.DataFrame(output_rows)
panda_data.to_csv('mydoc.csv')
