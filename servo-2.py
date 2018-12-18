# works best duty cycle 2% to 12%

import RPi.GPIO as GPIO
import sys
from time import sleep

duty = int(sys.argv[1])
pw = (duty / 100) * 20
pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 50)
print("pin {} : duty {} : pulse width {}".format(pin, duty, pw))
p.start(duty)
sleep(1)
p.stop()

GPIO.cleanup()

