#chap3- problem 14

from BeautifulSoup import BeautifulSoup
import urllib
import re
 
def getlink(url):
    '''
    Extacts all html links from a webpage
    
    '''
    html_page = urllib.urlopen(url)
    soup = BeautifulSoup(html_page)
    links = []
 
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))
 
    return links

d=getlink('http://python.org')
for x in d:
    print x
