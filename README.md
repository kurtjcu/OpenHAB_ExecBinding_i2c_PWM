# OpenHAB_ExecBinding_i2c_PWM
python script and openhab examples to control an adafruit i2c PWM board via python script.



#usage

Relay
-----

-r is to set a relay (default = 0)

use with -v for value (default = 0)




set out 1 to Off
 sudo python OpenHAB_i2c_PWM.py -r 1 -v 0

set out 1 to On
 sudo python OpenHAB_i2c_PWM.py -r 1 -v 1



Test
----
-t for time between relay sequence in seconds(optional)




#references


adafruit board used
-------------------
https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/

Adafruit library
----------------
https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code

(use the /Adafruit_PWM_Servo_Driver/)

OpenHAB
-------
Https://openhab.org

OpenHAB Exec Binding
--------------------
https://github.com/openhab/openhab/wiki/Exec-Binding




#inspiration

mostly based on the ideas from here.
http://www.element14.com/community/community/design-challenges/forget-me-not/blog/2014/08/11/elro-coco-with-openhab



