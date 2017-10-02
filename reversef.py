import sys

def reverse():
    f=open(sys.argv[-1],'r')
    d=f.readlines()
    d.reverse()
    for x in d:
        print x,
reverse()
