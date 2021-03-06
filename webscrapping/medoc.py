from bs4 import BeautifulSoup
import urllib.request
urlpage = 'https://www.legifrance.gouv.fr'
page = urllib.request.urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
table = soup.find('table', attrs={'class': 'tableSorter'})
results = table.find_all('tr')
cpy = table.find_all(class_="company-name")
print(cpy)
cpy_list = [cp.get_text() for cp in cpy]
print(cpy_list)


