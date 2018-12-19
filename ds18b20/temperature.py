# example
# pi@raspberrypi:/sys/bus/w1/devices/28-8000002b0f4a $ cat w1_slave 
# 4b 01 ff ff 7f ff ff ff 50 : crc=50 YES
# 4b 01 ff ff 7f ff ff ff 50 t=20687

# you may want to include a 5k pull up resistor on data line
# you may need to enable 1-wire in rasperry pi config
# by default the 1-wire works on pin 7 or gpio 4

import sys
import os
from time import sleep

# run as root
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices'
files = os.listdir(base_dir)
device = list(filter(lambda f: f[:2] == '28', files))[0]
filename = os.path.join(base_dir, device, 'w1_slave')

def get_temp():
    with open(filename, 'r') as f:
        lines = f.readlines()
        celsius = int(lines[1].strip().split(' ')[-1][2:])
        celsius /= 1000
        fahrenheit = (celsius * (9/5)) + 32
        return fahrenheit

while True:
    t = get_temp()
    print(t)
    sleep(1)

