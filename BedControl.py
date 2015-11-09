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
RLYOFF = 0, 4069
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


if args.end_of_bed == "head":
    if args.direction == "up":
        pwm.setPWM(head_offset + 1, *RLYOFF)
        if args.status == "off":
            pwm.setPWM(head_offset, *RLYOFF)
        elif args.status == "on":
            pwm.setPWM(head_offset, *RLYON)
    elif args.direction == "down":
        pwm.setPWM(head_offset + 1, *RLYON)
        if args.status == "off":
            pwm.setPWM(head_offset, *RLYOFF)
        elif args.status == "on":
            pwm.setPWM(head_offset, *RLYON)

elif args.end_of_bed == "foot":
    if args.direction == "up":
        pwm.setPWM(foot_offset + 1, *RLYOFF)
        if args.status == "off":
            pwm.setPWM(foot_offset, *RLYOFF)
        elif args.status == "on":
            pwm.setPWM(foot_offset, *RLYON)
    elif args.direction == "down":
        pwm.setPWM(foot_offset + 1, *RLYON)
        if args.status == "off":
            pwm.setPWM(foot_offset, *RLYOFF)
        elif args.status == "on":
            pwm.setPWM(foot_offset, *RLYON)






