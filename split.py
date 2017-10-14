import sys

def split():
    fname=sys.argv[-1]
    nlines=int(sys.argv[-2])
    f=open(fname,'r')
    d=f.readlines()
    c=[]
    if len(d)>nlines:
        str1=''
        for x in range(len(d)):
            if (x+1)%nlines==0:
                str1+=d[x]
                c.append(str1)
                str1=''
            elif x+1==len(d):
                str1+=d[x]
                c.append(str1)
            else:
                str1+=d[x]
        print c
        for x in range(len(c)):
            f=open(fname.split('.')[0]+str(x)+'.'+fname.split('.')[-1],'w')
            f.write(c[x])
            f.close()
    
split()
