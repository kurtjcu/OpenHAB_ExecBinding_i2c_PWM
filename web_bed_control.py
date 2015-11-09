#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import sys
import argparse
from bottle import route, run, template


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


@route('/')
def index():
    return 'hello, world'

@route('/head/up/<status>')
def tune(status = 'off'):
    set_head_up(status)
    return 'ack'

@route('/head/down/<status>')
def tune(status = 'off'):
    set_head_down(status)
    return 'ack'

@route('/foot/up/<status>')
def tune(status = 'off'):
    set_foot_up(status)
    return 'ack'

@route('/foot/down/<status>')
def tune(status = 'off'):
    set_foot_down(status)
    return 'ack'


def set_head_up(state):
    pwm.setPWM(head_offset + 1, *RLYOFF)
    pwm.setPWM(head_offset + 5, *RLYOFF)
    if state == "on":
        pwm.setPWM(head_offset, *RLYON)
        pwm.setPWM(head_offset + 4, *RLYON)
    else:
        pwm.setPWM(head_offset, *RLYOFF)
        pwm.setPWM(head_offset + 4, *RLYOFF)

def set_head_down(state):
    pwm.setPWM(head_offset + 1, *RLYON)
    pwm.setPWM(head_offset + 5, *RLYON)
    if state == "on":
        pwm.setPWM(head_offset, *RLYON)
        pwm.setPWM(head_offset + 4, *RLYON)
    else:
        pwm.setPWM(head_offset, *RLYOFF)
        pwm.setPWM(head_offset + 4, *RLYOFF)

def set_foot_up(state):
    pwm.setPWM(foot_offset + 1, *RLYOFF)
    pwm.setPWM(foot_offset + 5, *RLYOFF)
    if state == "on":
        pwm.setPWM(foot_offset, *RLYON)
        pwm.setPWM(foot_offset + 4, *RLYON)
    else:
        pwm.setPWM(foot_offset, *RLYOFF)
        pwm.setPWM(foot_offset + 4, *RLYOFF)

def set_foot_down(state):
    pwm.setPWM(foot_offset + 1, *RLYON)
    pwm.setPWM(foot_offset + 5, *RLYON)
    if state == "on":
        pwm.setPWM(foot_offset, *RLYON)
        pwm.setPWM(foot_offset + 4, *RLYON)
    else:
        pwm.setPWM(foot_offset, *RLYOFF)
        pwm.setPWM(foot_offset + 4, *RLYOFF)



run(host="0.0.0.0", port=5151)






