from StateBase import StateLoop
import time
from IO import Display


class TimeState(StateLoop):
    def __init__(self, name, display):
        super(TimeState, self).__init__(name, display)

    def initialize(self):
        self._start = time.time()

    def update(self):
        self._display.showTime()