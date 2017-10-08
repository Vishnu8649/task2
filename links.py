#chap3- problem 8

import re,sys,urllib

def link():
    '''
    prints all urls linked with agiven webpage

    '''
    url=sys.argv[-1]
    data=urllib.urlopen(url).read()
    urls=re.findall('"(http\S*)"',data)
    for x in urls:
        print x

link()
