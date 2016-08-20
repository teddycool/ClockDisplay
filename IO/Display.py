#Python class handling a 7-segment 4 digit display
#Inspired by: https://www.raspberrypi.org/forums/viewtopic.php?f=37&t=91796
#CL5642BH-33 4 digits with 'time-colon' from ebay: http://www.ebay.com/itm/381691780455
#To be used in a 'loop'- environemnt, each time the code is called the display is lit for a short while

import RPi.GPIO as GPIO
import time
import sys
import string

#Connection dependent
SEGMENTS = (26, 40, 33, 29, 23, 32, 35, 31)
DIGITS = (24, 36, 38, 37)


class Display(object):

    def __init__(self):

        self._segments = SEGMENTS #IO used for each segment = a,b,c,d,e,f,g,dp
        self._digits = DIGITS #IOs to enable each digit

        for segment in self._segments:
            GPIO.setup(segment, GPIO.OUT)
            GPIO.output(segment, 1)

        for digit in self._digits:
            GPIO.setup(digit, GPIO.OUT)
            GPIO.output(digit, 0)

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
                        '*':(0,0,0,0,0,0,0,0)}

    #Show system time
    def showTime(self):
        n = time.ctime()[11:13] + time.ctime()[14:16]

        s = str(n).rjust(4)

        for digit in range(4):
            for loop in range(0, len(self._segments)):
                GPIO.output(self._segments[loop], self._chars[s[digit]][loop])
                if (int(time.ctime()[18:19]) % 2 == 0) and (digit == 1):
                    GPIO.output(self._segments[7], 0)
                else:
                    GPIO.output(self._segments[7], 1)

            GPIO.output(self._digits[digit], 1)
            time.sleep(0.001)
            GPIO.output(self._digits[digit], 0)


    def showString(self,s):
        #special handling of dp...
        #depending on the dsplay, dp is only allowed in string-position 3.

        dp = string.find(s, '.')
        dpseg = False
        if dp == 3: #n.
            dpseg=True
            dp=dp-1
        s = string.replace(s, '.', '')
        for digit in range(len(s)):
            for segment in range(0, len(self._segments)):
                GPIO.output(self._segments[segment], self._chars[s[digit]][segment])
            if dpseg and dp == digit:
                    GPIO.output(self._segments[segment], self._chars['.'][segment])

            GPIO.output(self._digits[digit], 1)
            time.sleep(0.001)
            GPIO.output(self._digits[digit], 0)

    def testAllSegments(self):
        self.showString('****')


if __name__ == '__main__':
    print "Testcode for Display"
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    disp = Display()


    try:
        while True:
            disp.testAllSegments()
    except KeyboardInterrupt:
        GPIO.cleanup()
