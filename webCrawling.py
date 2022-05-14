from gettext import find
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

tom = urlopen("https://es.wikipedia.org/w/index.php?title=Especial:Buscar&search=web+crawling&go=Go&ns0=1&ns100=1&ns104=1")
soup = bs(tom.read())

for link in soup.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

for link in soup.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])