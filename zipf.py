#chap3- problem 11
import zipfile,sys

def zipf():
    '''
    compresses given files to 
    new zipfile     
        
    '''
    f=sys.argv[2:]
    z=sys.argv[1]
    if z.split('.')[-1]!='zip':
        print 'invalid zip file name'
    elif zipfile.is_zipfile(z):
        print 'Already exists retry with another name'
    else:
        zf=zipfile.ZipFile(z,mode='w')
        try:
            for x in f:
                zf.write(x,arcname=x)
            print '\nFILE', z,'::'
            for name in zf.namelist():
                print name
        finally:
            zf.close()
zipf() 
