import RPi.GPIO as GPIO
from time import sleep

pin = 18
interval = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.LOW)

try:
    print("Blinking LED")
    while True:
        GPIO.output(pin, GPIO.HIGH)
        sleep(interval)
        GPIO.output(pin, GPIO.LOW)
        sleep(interval)
except:
    print("Error, cleaning up")
    GPIO.cleanup()

