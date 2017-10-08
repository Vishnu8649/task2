#chap3- problem 2

import os,sys

def extcount():
    dir=sys.argv[1]
    lis=os.listdir(dir)
    new={}
    for x in lis:
        k=x.split('.')
        if len(k)==1:
            new['files']=new.get('files',0)+1
        elif k[1] not in new:
            new[k[1]]=1
        else:
            new[k[1]]+=1
    for x in new:
        print new[x],x
extcount()
