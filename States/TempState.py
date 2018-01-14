from StateBase import StateLoop
import time
from IO import Display
import urllib2


class TempState(StateLoop):
    def __init__(self, name, display):
        super(TempState, self).__init__(name, display)

    def initialize(self, mqtttemp):
        self._start = time.time()
        self._mqtttemp = mqtttemp
        self._temp = self._mqtttemp.read()
        self._lastTempRead= time.time()

    def update(self):
        if time.time() - self._lastTempRead > 30:
            self._temp = self._mqtttemp.read()
            self._lastTempRead = time.time()
        self._display.showString(self._temp)
