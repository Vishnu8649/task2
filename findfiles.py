import os

def findfiles(dir):
    for x in sorted(os.listdir(dir)):
        if os.path.isdir(dir+'/'+x)==True:
            findfiles(dir+'/'+x)
        else:
            print dir+'/'+x


