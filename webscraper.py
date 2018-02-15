#import bs4 as bs
import urllib


from bs4 import BeautifulSoup
import requests

#url  = input("Enter")
url = 'http://citotech.com.au'

sauce = urllib.urlopen(url).read()

# soup = bs.BeautifulSoup(sauce, 'lxml')
# url = raw_input('Enter -')

# html = urllib.urlopen(url).read()
# soup = bs4(html)

# for para in soup.find_all('a'):
#  print (para.get('href'))

# nav = soup.nav

#print nav
