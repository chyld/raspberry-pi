# pip install Adafruit_DHT
import Adafruit_DHT
import sys
from time import sleep

# uses broadcom pin number, not board number
pin = 18
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)

if humidity is not None and temperature is not None:
    temperature = temperature * 9/5.0 + 32
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)

