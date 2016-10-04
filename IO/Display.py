#Python class handling a 7-segment 4 digit display
#Inspired by: https://www.raspberrypi.org/forums/viewtopic.php?f=37&t=91796
#CL5642BH-33 4 digits with 'time-colon' from ebay: http://www.ebay.com/itm/381691780455
#To be used in a 'loop'- environemnt, each time the code is called the display is lit for a short while


import time
import string

#Connection dependent BCM mode, actual pin-no. NOT GPIO-no
SEGMENTS = (5, 15, 29, 21, 19, 7, 31, 23)     #IO used for each segments = a,b,c,d,e,f,g,dp
DIGITS = (3, 11, 13, 33)                        #IOs to enable each digit


class Display(object):

    def __init__(self,gpio):

        self._segments = SEGMENTS
        self._digits = DIGITS
        self._gpio=gpio
        self._dimfactor = 0.0 #full power


        for segment in self._segments:
            self._gpio.setup(segment,  self._gpio.OUT)
            self._gpio.output(segment, 1)

        for digit in self._digits:
            self._gpio.setup(digit,  self._gpio.OUT)
            self._gpio.output(digit, 0)

        #build valid chars with the segments, common anode means 0 = turn on segment
        self._chars = { ' ':(1,1,1,1,1,1,1,1),
                        '0':(0,0,0,0,0,0,1,1),
                        '1':(1,0,0,1,1,1,1,1),
                        '2':(0,0,1,0,0,1,0,1),
                        '3':(0,0,0,0,1,1,0,1),
                        '4':(1,0,0,1,1,0,0,1),
                        '5':(0,1,0,0,1,0,0,1),
                        '6':(0,1,0,0,0,0,0,1),
                        '7':(0,0,0,1,1,1,1,1),
                        '8':(0,0,0,0,0,0,0,1),
                        '9':(0,0,0,0,1,0,0,1),
                        '.':(1,1,1,1,1,1,1,0),
                        '-':(1,1,1,1,1,1,0,1),
                        'h':(1,1,0,1,0,0,0,1),
                        'H':(1,0,0,1,0,0,0,1),
                        'd':(1,0,0,0,0,1,0,1),
                        'b':(1,1,0,0,0,0,0,1),
                        'A':(0,0,0,1,0,0,0,1),
                        'F':(0,1,1,1,0,0,0,1),
                        'C':(0,1,1,0,0,0,1,1),
                        'E':(0,1,1,0,0,0,0,1),
                        'g':(0,0,1,1,1,0,0,1),
                        '*':(0,0,0,0,0,0,0,0), #TEST: ALL segments including dp
                        }

    #Show system time
    def showTime(self):
        n = time.ctime()[11:13] + time.ctime()[14:16]

        s = str(n).rjust(4)
        print s
        print len(s)
        #TODO: replace with showString and handle time-colon

        for digit in range(4):
            for loop in range(0, len(self._segments)):
                self._gpio.output(self._segments[loop], self._chars[s[digit]][loop])
                if (int(time.ctime()[18:19]) % 2 == 0) and (digit == 1):
                    self._gpio.output(self._segments[7], 0)
                else:
                    self._gpio.output(self._segments[7], 1)

            self._gpio.output(self._digits[digit], 1)
            time.sleep(0.001)
            self._gpio.output(self._digits[digit], 0)
            #Dimming factor
            time.sleep(self._dimfactor)


    def showString(self,s):
        #special handling of dp...
        #depending on the dsplay, dp is only allowed in string-position 3.
        print s
        print len(s)
        dp = string.find(s, '.')
        dpseg = False
        if dp == 3: #n.
            dpseg=True
            dp=dp-1
        s = string.replace(s, '.', '')

        for digit in range(len(s)):
            for segment in range(0, len(self._segments)):
                self._gpio.output(self._segments[segment], self._chars[s[digit]][segment])
            if dpseg and dp == digit:
                self._gpio.output(self._segments[segment], self._chars['.'][segment])

            self._gpio.output(self._digits[digit], 1)
            time.sleep(0.001)
            self._gpio.output(self._digits[digit], 0)
            # Dimming factor
            time.sleep(self._dimfactor)

    def testAllSegments(self):
        self.showString('****')


    def setDimFactor(self, factor=0):
        factor = float(factor)
        if factor in range(0,6):
            self._dimfactor=factor/1000


if __name__ == '__main__':
    import RPi.GPIO as GPIO
    print "Testcode for Display"
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    disp = Display(GPIO)
    starttime =time.time()
    dimfactor = 0

    try:
        while True:
            disp.testAllSegments()
            if time.time()- starttime > 2:
                dimfactor = dimfactor + 1
                disp.setDimFactor(dimfactor)
                starttime = time.time()

    except KeyboardInterrupt:
        GPIO.cleanup()
