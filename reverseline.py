#chap2-problem 18
import sys

def reverse():
    f=open(sys.argv[-1],'r')
    d=f.readlines()
    d1=[]
    for x in d:
        d1.append(x.split())
    for x in d1:
        x.reverse()
        for a in x:
            print a,
        print ''
reverse()
    
        
