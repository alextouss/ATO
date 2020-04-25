from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime,timedelta
import locale


#Réglages
pd.set_option('max_columns', 8)
pd.set_option('expand_frame_repr', False)
locale.setlocale(locale.LC_ALL, 'fr_FR')

#URL du jour
url_jo = 'https://www.legifrance.gouv.fr/affichJO.do?idJO=JORFCONT000041804056'
soup_jo = BeautifulSoup(requests.get(url_jo).text, 'html5lib')

# Chercher le titre "Avis divers" dans son titre parent "Avis et communications" et s'y positionner
avis_divers_li = soup_jo.find("h4", text="Avis divers").find_parent('li')

# Chercher le titre "Ministère des solidarités et de la santé" dans son titre parent "Avis divers" et s'y positionner
min_sante_li = avis_divers_li.find("h5", text="Ministère des solidarités et de la santé").find_parent('li')

article_list_li = min_sante_li.find('ul').findAll('li')

#Pour chaque li on récupère le titre de l'article et son url
article_list = []
for li in article_list_li:
    i = li.find("a").text
    j = li.span["resource"]
    article_list.append((i, j))


def is_cip(i, j):
    return (
            i == 'Avis relatif aux prix de spécialités pharmaceutiques' or i == "Avis relatif aux prix d'une spécialité pharmaceutique")

delais_application = "quatrième"
def date_application(x):
    if delais_application in x:
        return my_jo_date + timedelta(days=4)

output_rows_cip = []
#On regarde si chaque article est un CIP
for i, j in article_list:
    if is_cip(i, j):
        url = j
        soup = BeautifulSoup(requests.get(url).text, 'html5lib')

        # Chercher la date du JO dans < div class ="enteteTexte" >
        jo = soup.find('div', attrs={'class': 'enteteTexte'}).text
        #Isoler la date du JO
        my_jo_date = jo.replace("\n", " ").replace("\t", "").strip().split(' ')[3:6]
        my_jo_date = ' '.join(my_jo_date)
        my_jo_date = datetime.strptime(my_jo_date, '%d %B %Y')

        # Chercher le texte
        texte = soup.find('div', attrs={'class': 'article'}).p.text
        # Cleaner le texte
        texte= texte.replace("\n", " ").replace("\t", "")

        # Chercher le tableau
        table = soup.find('tbody')

        # les <th> et <td> sont tous les deux dans les <tr>. La premiere <tr> contient uniquement des <th> et les suivantes des <td>
        for table_row in table.findAll('tr'):
            #On itère uniquement dans les lignes du tableau qui ne sont pas l'entete (uniquement les <tr> contenant des <td>)
            if table_row.find('td'):
                cells_data = table_row.findAll('td')

                # on recupère le contenu des <td> qu'on met dans une liste et on ajoute aussi les autre éléments contenu dans l'article
                output_row_tr = []
                for column in cells_data:
                    output_row_tr.append(column.text.replace("\n", ""))
                output_row_tr.append(my_jo_date)
                output_row_tr.append(date_application(texte))
                # On transforme cette liste en une tuple
                output_row_tr = tuple(output_row_tr)
                # Un tuple est ajouté à la liste des CIP du jour pour chaque <tr>
                output_rows_cip.append(output_row_tr)




col_list = ['N° CIP', 'Présentation', 'PFHT', 'PPTTC', 'JO date', 'Application date']


panda_data = pd.DataFrame(output_rows_cip, columns=col_list)
print(panda_data)
panda_data.to_csv('mydoc2.csv')
