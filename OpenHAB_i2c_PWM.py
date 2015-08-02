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


# Argument parsing
parser = argparse.ArgumentParser(description='Controls PWM hat from Adafruit')
parser.add_argument('-t', action="store", dest="time", default=1, type=int, nargs='?')
parser.add_argument('-a', action="store", dest="action", default='test',nargs='?')
parser.add_argument('-v', action="store", dest="valueNum", default=0, type=int, nargs='?')
parser.add_argument('-r', action="store", dest="relayNum", default=-1, type=int, nargs='?')
parser.add_argument('-p', action="store", dest="pwmNum", default=-1, type=int, nargs='?')
parser.add_argument('-f', action="store", dest="pwmFreq", default=--1, type=int, nargs='?')


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

elif args.pwmNum != -1:
    print "PWM %s" % args.pwmNum
    print "Value %s" % args.valueNum
    print "on %s" % str((args.valueNum*4069)/100)
    print "off %s" % str(4069-((args.valueNum*4069)/100))
    if args.valueNum == 1:
        pwm.setPWM(args.pwmNum, 0, args.valueNum)
    quit()

elif args.pwmFreq != -1:
    print "setting PWM Freq = %s" % str(args.pwmFreq)
    pwm.setPWMFreq(args.pwmFreq)

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
