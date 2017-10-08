import re,sys,urllib

def link():
    url=sys.argv[-1]
    data=urllib.urlopen(url).read()
    urls=re.findall('"(http\S*)"',data)
    for x in urls:
        print x

link()
