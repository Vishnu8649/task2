#chap2-problem 20
import sys
def grep():
    f=open(sys.argv[-2],'r')
    d=f.readlines()
    word=sys.argv[-1]
    for x in d:
        if word in x:
            print x,

grep()

