#chap3- problem 6
import re,sys,urllib

def antihtml():
    '''
    Prints webpage contents by striping html tags

    '''
    url=sys.argv[-1]
    st=urllib.urlopen(url).read()
    a=re.split('<[^>]*>',st)
    #a=re.split('<.*\s*.*>',st)
    for x in a:
        print x.strip()

antihtml()
