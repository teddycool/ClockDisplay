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
        #TODO: make some sanity-check
        response =  urllib2.urlopen("http://www.sundback.com/ws/getCurrentOutTemp.php")
        return response.read()


if __name__ == "__main__":
    print 'OutTemp test...'

    ot = OutTemp()
    ot.initialize()
    test = ot.update()
    print test
    print len(test)