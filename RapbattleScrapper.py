from bs4 import BeautifulSoup
import urllib2
 
url = "http://www.reddit.com/r/rapbattles"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
 
for anchor in soup.find_all('a'):
    print(anchor.get('href', '/')) 