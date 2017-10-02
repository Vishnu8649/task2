import sys
def head():
    f=open(sys.argv[-1],'r')
    d=f.readlines()
    if len(d)>10:
        for x in range(10):
            print d[x],
    else:
        for x in d:
            print x,
head()
