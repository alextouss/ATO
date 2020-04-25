from bs4 import BeautifulSoup
file = open("koesio.html", "r")
soup = BeautifulSoup(file, 'html.parser')
table = soup.find('table', attrs={'class': 't-data-grid'})
tbody = soup.find('tbody')
userRightName = tbody.find_all('td','userRightName')
allowed = tbody.find_all('td','allowed')
rights_list = [rights.get_text() for rights in userRightName]
allowed_li = [allowed.get_text() for allowed in allowed]
print(rights_list)
print(allowed_li)

