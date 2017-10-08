#chap3- problem 3
import os,sys,time
def status():
    '''
    prints size and modified date of\
     files in given directory
    
    '''
    dir=sys.argv[1]
    val=os.listdir(dir)
    t=time.ctime
    for x in val:
        print(x+'\t'+str(os.stat(dir+x)\
        .st_size)+'\t'+str(t(os.stat(dir+x)\
        .st_mtime)))
status()
