# OpenHAB_ExecBinding_i2c_PWM
python script and openhab examples to control an adafruit i2c PWM board via python script.



#setup

follow all adafruit setup for smbus/i2c etc from product page.

clone this repo.

inside the repo directory do:
```
chmod +x OpenHAB_i2c_PWM.py
```
to make the script executable.

make sure you have the openhab exec binding in your addons directory.

Edit your OPENHAB  .items to contain something similar to this

```
//Exec Bindings  
Switch i2cPWM_RLY01 "Exec" (exec) {exec=">[ON:/bin/sh@@-c@@/home/pi/OpenHAB_ExecBinding_i2c_PWM/OpenHAB_i2c_PWM.py -r 0 -v 1] >[OFF:/bin/sh@@-c@@/home/pi/OpenHAB_ExecBinding_i2c_PWM/OpenHAB_i2c_PWM.py -r 0 -v 0]"}
Switch i2cPWM_RLY02 "Exec" (exec) {exec=">[ON:/bin/sh@@-c@@/home/pi/OpenHAB_ExecBinding_i2c_PWM/OpenHAB_i2c_PWM.py -r 1 -v 1] >[OFF:/bin/sh@@-c@@/home/pi/OpenHAB_ExecBinding_i2c_PWM/OpenHAB_i2c_PWM.py -r 1 -v 0]"}

//TODO: Add PWM binding here(need to work out passing value to this binding).
```

#usage

PWM
---
-p is for setting PWM ON time @output (default = 0)
use with v- to set ON time[0-100]

set out 1 to 50% on
```
sudo python OpenHAB_i2c_PWM.py -p 1 -v 50
```
 
set out 1 to 90% on
```
sudo python OpenHAB_i2c_PWM.py -p 1 -v 90
```

Relay
-----
-r is to set a relay @output (default = 0)
use with -v for value (default = 0)

set out 1 to Off
```
sudo python OpenHAB_i2c_PWM.py -r 1 -v 0
```

set out 1 to On
```
sudo python OpenHAB_i2c_PWM.py -r 1 -v 1
```


Frequency
---------

-f is to set the PWM frequency

set frequency to 120 hz
```
sudo python OpenHAB_i2c_PWM.py -f 120 
```
 
 
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



