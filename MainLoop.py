__author__ = 'teddycool'
#State-switching and handling of general rendering

import time
from IO import Display
from States import TestState
from States import TimeState
from States import TempState

#Global GPIO used by all...
import RPi.GPIO as GPIO

class MainLoop(object):
    def __init__(self):
        self._gpio= GPIO
        self._gpio.setmode(self._gpio.BOARD)
        self._display=Display.Display(self._gpio)

    def initialize(self):
        print "Mainloop initialize"
        self._testState = TestState.TestState("TestState", self._display)
        self._timeState = TimeState.TimeState("TimeState", self._display)
        self._tempState = TempState.TempState("TempState", self._display)
        self._tempState.initialize()
        self._currentState = self._testState
        self._lastStateChange = time.time()

    def update(self):
        self._currentState.update()
        #TODO: improve statemachine
        if time.time() - self._lastStateChange > 3:
            if self._currentState._statename == "TestState":
                self._currentState = self._timeState
                #print "Current state: " + self._currentState._statename
            else:
                if self._currentState._statename == "TimeState":
                    self._currentState = self._tempState
                else:
                    if self._currentState._statename == "TempState":
                        self._currentState = self._timeState
            self._lastStateChange = time.time()
            print "Current state: " + self._currentState._statename


    def __del__(self):
        self._gpio.cleanup()
        print "MainLoop cleaned up"


