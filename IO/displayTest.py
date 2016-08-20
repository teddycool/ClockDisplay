#!/usr/bin/python
# Bert's code re-written for common anode LED arrays.

import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#LED pin == GPIO == segment / digit
# 11     ==  24  == a
# 07     ==  12  == b
# 04     ==  19  == c
# 02     ==  21  == d
# 01     ==  23  == e
# 10     ==  22  == f
# 05     ==  15  == g
# 03     ==  11  == dp

segments = (26,40,33,29,23,32,35,31)

for segment in segments:
  GPIO.setup(segment, GPIO.OUT)
  GPIO.output(segment, 1)

# 12     ==  26  == digit 1
# 09     ==  18  == digit 2
# 08     ==  16  == digit 3
# 06     ==  13  == digit 4

digits = (24,36,38,37)
for digit in digits:
  GPIO.setup(digit, GPIO.OUT)
  GPIO.output(digit, 0)

num = {' ':(1,1,1,1,1,1,1),
'0':(0,0,0,0,0,0,1),
'1':(1,0,0,1,1,1,1),
'2':(0,0,1,0,0,1,0),
'3':(0,0,0,0,1,1,0),
'4':(1,0,0,1,1,0,0),
'5':(0,1,0,0,1,0,0),
'6':(0,1,0,0,0,0,0),
'7':(0,0,0,1,1,1,1),
'8':(0,0,0,0,0,0,0),
'9':(0,0,0,0,1,0,0)}

try:
  while True:
    n = time.ctime()[11:13] + time.ctime()[14:16]
    s = str(n).rjust(4)

    for digit in range(4):
      for loop in range(0,7):
        GPIO.output(segments[loop], num[s[digit]][loop])
        if (int(time.ctime()[18:19])%2 == 0) and (digit == 1):
          GPIO.output(31, 0)
        else:
          GPIO.output(31, 1)

      GPIO.output(digits[digit], 1)
      time.sleep(0.001)
      GPIO.output(digits[digit], 0)

except KeyboardInterrupt:
  GPIO.cleanup()