import os

def linepy(dir):
    for x in os.listdir(dir):
        if os.path.isdir(dir+'/'+x)==True:
            linepy(dir+'/'+x)
        else:
            if x.split('.')[-1]=='py':
                count =0
                f=open(dir+'/'+x,'r').readlines()
                for line in f:
                    if line!='\n' or line[0]!='#':
                        count+=1
                print dir+'/'+x, 'lines=',count

                    

