import sys,urllib

def wget():
    url=sys.argv[-1]
    if url.split('/')[-1]=='':
        f=open('index.html','w+')
        f.write(urllib.urlopen(url).read())
    else:
        f=open(url.split('/')[-1],'w+')
        f.write(urllib.urlopen(url).read())
wget()
