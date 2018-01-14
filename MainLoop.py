__author__ = 'teddycool'
#State-switching and handling of general rendering

import time
from IO import Display
from OutTemp import MqttTemp
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
        self._temp = MqttTemp.MqttTemp("ev39/temp")

    def initialize(self):
        print "Mainloop initialize"
        self._testState = TestState.TestState("TestState", self._display)
        self._timeState = TimeState.TimeState("TimeState", self._display)
        self._tempState = TempState.TempState("TempState", self._display)
        self._tempState.initialize(self._temp)
        self._display.setDimFactor(3)
        self._currentState = self._testState
        self._lastStateChange = time.time()

    def update(self):
        self._currentState.update()
        #TODO: improve statemachine
        if time.time() - self._lastStateChange > 2:
            self._lastStateChange = time.time()
            if self._currentState._statename == "TempState":
                self._currentState=self._timeState
            else:
                self._currentState = self._tempState
            print "Current state: " + self._currentState._statename
        #time.sleep(1)


    def __del__(self):
        self._gpio.cleanup()
        print "MainLoop cleaned up"


