#chap3- problem 
import os,sys
dir=sys.argv[-1]
d=dir
par=len(dir.split('/'))
def dirtree(dir):

    '''
    Prints directory tree for a given directory

    '''
    if dir==d:
        print d.split('/')[-1]
    for x in sorted(os.listdir(dir)):
            if os.path.isdir(dir+'/'+x):
                print (len(dir.split('/'))-par)*'|  '+'|--'+x
                dirtree(dir+'/'+x)
            elif x==sorted(os.listdir(dir))[-1]:
                print (len(dir.split('/'))-par)*'|  '+'\--'+x
            else :
                print (len(dir.split('/'))-par)*'|  '+'|--'+x
dirtree(dir)
