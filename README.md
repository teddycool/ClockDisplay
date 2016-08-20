# ClockDisplay
Using a raspberry pi wth a connected 4-digit 7-segment display to show current time but also outdoor temperature and humidity and some other values.

Hardware:
Raspberry pi with rasbian
RealTimeClock module
CL5642BH-33 4 digits with 'time-colon' from ebay: http://www.ebay.com/itm/381691780455
8 resistors 560 Ohm
board and cables

Software:
'GameLoop'-concept with Main.py as starting-point. All classes/objects has __init__, initialize and update methods. Each module is supposed to have a "if __name__ == "__main__"" contruction for testing.
