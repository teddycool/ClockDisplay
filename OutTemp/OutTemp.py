#This class will fetch outdoor temperature an humidity from a network connected sensor mounted on the outside

import time
import string
import urllib2

class OutTemp(object):

    def __init__(self):
        return


    def initialize(self):
        return


    def update(self):
        response =  urllib2.urlopen("http://www.sundback.com/ws/getCurrentOutTemp.php")
        return response.read()


if __name__ == "__main__":
    print 'OutTemp test...'

    ot = OutTemp()
    ot.initialize()
    test = ot.update()
    if len(test) == 1:
        test = '   ' + test
    if len(test) == 2:
        test = '  ' + test
    if len(test) == 3:
        test = ' ' + test

    print len(test)