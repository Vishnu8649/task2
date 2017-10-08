import urllib,json

def myip():
    response=urllib.urlopen('http://httpbin.org/get').read()
    data=json.loads(response)[u'origin']
    print 'Your Public IP Address is\n',data
myip()
