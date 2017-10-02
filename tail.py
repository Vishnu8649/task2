#chap2-problem 19-2

import sys
def tail():
    f=open(sys.argv[-1],'r')
    d=f.readlines()
    if len(d)>10:
        for x in reversed(range(1,11)):
            print d[-x],
    else:
        for x in d:
            print x,
tail()

