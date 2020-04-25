from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR')
my_string = '17 avril 2020'

my_string=datetime.strptime(my_string,'%d %B %Y',)
print(my_string)