from StateBase import StateLoop
import time
from IO import Display
import urllib2


class TempState(StateLoop):
    def __init__(self, name, display):
        super(TempState, self).__init__(name, display)

    def initialize(self):
        self._start = time.time()
        self._temp = self._getTemp()
        self._lastTempRead= time.time()

    def update(self):
        if time.time() - self._lastTempRead > 30:
            self._temp = self._getTemp()
            self._lastTempRead = time.time()
        self._display.showString(self._temp)


    def _getTemp(self):

        try:
            response = urllib2.urlopen("http://www.sundback.com/ws/getCurrentOutTemp.php")
            test = response.read()
        except:
            test = "-"

        test = test+'g'

        if len(test) == 1:
            test = '   ' + test
        else:
            if len(test) == 2:
                test = '  ' + test
            else:
                if len(test) == 3:
                    test = ' ' + test
        return test