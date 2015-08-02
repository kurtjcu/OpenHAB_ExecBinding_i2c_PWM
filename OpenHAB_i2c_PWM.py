#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import sys
import argparse

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
pwm = PWM(0x40, debug=True)

#define On 100%
RLYON = 0, 4069
#define Off 0%
RLYOFF = 0, 0


def setServoPulse(channel, pulse):
    pulseLength = 1000000                   # 1,000,000 us per second
    pulseLength /= 60                       # 60 Hz
    print "%d us per period" % pulseLength
    pulseLength /= 4096                     # 12 bits of resolution
    print "%d us per bit" % pulseLength
    pulse *= 1000
    pulse /= pulseLength
    pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(90)                        # Set frequency to 60 Hz

# Argument parsing
parser = argparse.ArgumentParser(description='Controls PWM hat from Adafruit')
parser.add_argument('-t', action="store", dest="time", default=1, type=int, nargs='?')
parser.add_argument('-a', action="store", dest="action", default='test',nargs='?')
parser.add_argument('-v', action="store", dest="valueNum", default=0, type=int, nargs='?')
parser.add_argument('-r', action="store", dest="relayNum", default=-1, type=int, nargs='?')

args = parser.parse_args()

slpTime = args.time





if args.relayNum != -1:
    print "Relay %s" % args.relayNum
    print "Value %s" % args.valueNum
    if args.valueNum == 1:
        pwm.setPWM(args.relayNum, *RLYON)
    else:
        pwm.setPWM(args.relayNum, *RLYOFF)
    quit()

# test function
elif args.action == 'test':
    # turn on and off  relays on all channels
    print "in Test"

    for x in range(0, 15):
        pwm.setPWM(x, *RLYOFF)

    for x in range(0, 15):
        time.sleep(slpTime)
        pwm.setPWM(x, *RLYON)

    for x in range(0, 15):
        time.sleep(slpTime)
        pwm.setPWM(x, *RLYOFF)

    time.sleep(slpTime)
    quit()

else:
    print "where am i"
    quit()
