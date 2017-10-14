import os

def py(dir):
    count=0
    for x in os.listdir(dir):
        if os.path.isdir(dir+'/'+x)==True:
            py(dir+'/'+x)
        else:
            if x.split('.')[-1]=='py':
                count =count+1
    print dir,count
