#chap3- problem 10

import urllib,json

def myip():
    '''
    prints ip address of the user

    '''
    response=urllib.urlopen('http://httpbin.org/get').read()
    data=json.loads(response)[u'origin']
    print 'Your Public IP Address is\n',data
myip()
