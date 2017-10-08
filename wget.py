#chap3- problem 5
import sys,urllib

def wget():
    '''
    saves a webpage for given url to html file
    
    '''
    url=sys.argv[-1]
    if url.split('/')[-1]=='':
        f=open('index.html','w+')
        f.write(urllib.urlopen(url).read())
    else:
        f=open(url.split('/')[-1],'w+')
        f.write(urllib.urlopen(url).read())
wget()
