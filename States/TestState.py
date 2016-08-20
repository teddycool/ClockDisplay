from StateBase import StateLoop
import time
from IO import Display

class TestState(StateLoop):
    def __init__(self, name, display):
        super(TestState, self).__init__(name, display)

    def initialize(self):
        self._start=time.time()


    def update(self):
        self._display.testAllSegments()