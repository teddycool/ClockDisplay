# ClockDisplay
Using a raspberry pi wth a connected 4-digit 7-segment display to show current time but also outdoor temperature and humidity and some other values. It's a work in progress and not finished....

Hardware:
Raspberry pi with rasbian
RealTimeClock module (option)
CL5642BH-33 4 digits with 'time-colon' from ebay: http://www.ebay.com/itm/381691780455
8 resistors 560 Ohm (Dependent of display. This is choosen to make the display as bright as possible. A dim-factor in the software turns down the brightness depending on the surrounding light)
board and cables

Software:
'GameLoop'-concept with Main.py as starting-point. All classes/objects has __init__, initialize and update methods. Each module is supposed to have a "if __name__ == "__main__"" contruction for testing.
