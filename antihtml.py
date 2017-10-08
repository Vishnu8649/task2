import re,sys,urllib

def antihtml():
    url=sys.argv[-1]
    st=urllib.urlopen(url).read()
    #a=re.split('<(?![< >]).*[\s*.*]*>',st)
    a=re.split('<.*\s*.*>',st)
    for x in a:
        if x!=' 'or x!=''or x!='\n':
            print x.strip()+' ',

antihtml()
