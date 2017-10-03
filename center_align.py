#chap2- problem 23
import sys

def center_align():
'''
inputs text file

outputs center aligned file

'''
    f=open(sys.argv[-1],'r')
    lines=f.readlines()
    c=0
    for x in lines:
        if len(x)>c:
            c=len(x)
    for x in lines:    
        if len(x)<c:
            print ((c-len(x))/2)*' ',
        print x,

center_align()
             
