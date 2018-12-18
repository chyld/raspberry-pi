import RPi.GPIO as GPIO
from time import sleep

pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 50)
p.start(2)

try:
    while True:
        for i in range(2, 13):
            print("Duty cycle:", i)
            p.ChangeDutyCycle(i)
            sleep(1)
except:
    print("Error, cleaning up")
    p.stop()
    GPIO.cleanup()

