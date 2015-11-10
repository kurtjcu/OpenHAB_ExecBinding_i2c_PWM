#!/usr/bin/python

import time
from threading import Thread

from Adafruit_PWM_Servo_Driver import PWM
from bottle import route, run


# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
pwm = PWM(0x40, debug=True)

# define On 100%
RLYOFF = 0, 4069
# define Off 0%
RLYON = 0, 0

head_offset = 0
foot_offset = 2

vibrate_head_offset = 8
vibrate_foot_offset = 9


@route('/')
def index():
    return 'hello, world'


@route('/head/up/<status>')
def head_up(status='off'):
    set_head_up(status)
    return 'ack'


@route('/head/down/<status>')
def head_down(status='off'):
    set_head_down(status)
    return 'ack'


@route('/foot/up/<status>')
def foot_up(status='off'):
    set_foot_up(status)
    return 'ack'


@route('/foot/down/<status>')
def foot_down(status='off'):
    set_foot_down(status)
    return 'ack'


@route('/preset/<preset_name>')
def preset(preset_name="none"):
    if preset_name == "flat":
        Thread(target=set_preset_flat).start()
        return 'ack'
    elif preset_name == "all_off":
        Thread(target=set_preset_flat).start()
        pwm.setPWM(vibrate_head_offset, 0, 0)
        pwm.setPWM(vibrate_foot_offset, 0, 0)
        return 'ack'
    else:
        return 'unknown preset'

@route('/vibrate/head/<speed>')
def vibrate_head(speed = 0):
    pwm.setPWM(vibrate_head_offset, 0, 30 * int(speed))
    return "ack"

@route('/vibrate/foot/<speed>')
def vibrate_foot(speed = 0):
    pwm.setPWM(vibrate_foot_offset, 0, 30 * int(speed))
    return "ack"

@route('/freq/<frequency>')
def set_freq(frequency=100):
    pwm.setPWMFreq(int(frequency))
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


def set_preset_flat(delay_time=10):
    set_head_down("on")
    set_foot_down("on")
    time.sleep(delay_time)
    set_head_down('off')
    set_foot_down('off')


run(server="meinheld", host="0.0.0.0", port=5151, reloader=True)
