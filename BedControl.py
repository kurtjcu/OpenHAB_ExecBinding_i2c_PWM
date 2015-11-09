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
RLYOff = 0, 4069
#define Off 0%
RLYON = 0, 0

head_offset = 0
foot_offset = 2



# Argument parsing
parser = argparse.ArgumentParser(description='Controls PWM hat from Adafruit')

parser.add_argument('-e', action="store", dest="end_of_bed", default="head", type=str, nargs='?')
parser.add_argument('-d', action="store", dest="direction", default="up", type=str, nargs='?')
parser.add_argument('-s', action="store", dest="status", default="off", type=str, nargs='?')



args = parser.parse_args()


if end_of_bed == "head":
    if direction == "up":
        pwm.setPWM(head_offset + 1, *RLYOFF)
        if status == "off":
            pwm.setPWM(head_offset, *RLYOFF)
        elif status == "on":
            pwm.setPWM(head_offset, *RLYON)
    elif direction == "down":
        pwm.setPWM(head_offset + 1, *RLYON)
        if status == "off":
            pwm.setPWM(head_offset, *RLYOFF)
        elif status == "on":
            pwm.setPWM(head_offset, *RLYON)

elif end_of_bed == "foot":
    if direction == "up":
        pwm.setPWM(foot_offset + 1, *RLYOFF)
        if status == "off":
            pwm.setPWM(foot_offset, *RLYOFF)
        elif status == "on":
            pwm.setPWM(foot_offset, *RLYON)
    elif direction == "down":
        pwm.setPWM(foot_offset + 1, *RLYON)
        if status == "off":
            pwm.setPWM(foot_offset, *RLYOFF)
        elif status == "on":
            pwm.setPWM(foot_offset, *RLYON)






if args.relayNum != -1:
    if args.valueNum == 1:
        pwm.setPWM(args.relayNum, *RLYON)
    else:
        pwm.setPWM(args.relayNum, *RLYOFF)
    quit()

elif args.pwmNum != -1:
    pwm.setPWM(args.pwmNum, 0, (args.valueNum*4069)/100)
    quit()

elif args.pwmFreq != -1:
    pwm.setPWMFreq(args.pwmFreq)
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
