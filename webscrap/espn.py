from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
search = urlopen('https://www.espn.com.mx/busqueda/_/tipo/equipos/q/livingston')
bs_search = BeautifulSoup(search.read(), 'html.parser')
#print(bs_search)
a_tag_team = bs_search.find_all('section', {'href' : 'http://www.espn.com.mx/futbol/equipo/_/id/259/livingston'})

html = urlopen('https://www.espn.com.mx/futbol/equipo/plantel/_/id/258/hibernian')
bs = BeautifulSoup(html.read(), 'html.parser')


players = bs.find('table', {'class': 'Table'}).tbody
nameList = bs.find_all(class_ = "AnchorLink")
super_players = bs.find_all('a', {'href': re.compile('https:\/\/www.espn.com.mx\/futbol\/jugador\/')})
for name in a_tag_team:
    print(name)