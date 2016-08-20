from StateBase import StateLoop
import time
from IO import Display


class TempState(StateLoop):
    def __init__(self, name, display):
        super(TempState, self).__init__(name, display)

    def initialize(self):
        self._start = time.time()

    def update(self):
        temp = "-12.3"
        self._display.showString(temp)