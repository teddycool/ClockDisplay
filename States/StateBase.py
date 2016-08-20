
__author__ = 'teddycool'

#Parent-class for all state-loops

class StateLoop(object):

    def __init__(self, statename, display):
        self._statename = statename
        self._display=display
        print "New Stete created: " + statename

    def initialize(self):
        return

    def update(self):
        return