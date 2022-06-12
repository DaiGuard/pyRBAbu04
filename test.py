#! /usr/bin/env python

import RPi.GPIO as GPIO
import spidev
import time
import datetime


GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0, 1)

spi.max_speed_hz = 1000000
spi.mode = 3

print('Output pin A,B: ', end='')
pin = input()


vol = 0
while True:
    #print('Voltage (0~4095): ', end='')
    #vol = int(input())
    print('Exec {}: {}'.format(pin, vol))

    data = [0x00, 0x00]

    try:
        vol += 1
        if vol > 4095:
            vol = 0;

        GPIO.output(25, 1)

        if pin == 'A':
            pass
        elif pin == 'B':
            data[0] |= 0x80
        else:
            raise Exception('unknow pin name')

        #data[0] |= 0x20
        data[0] |= 0x10

        data[0] |= ((vol >> 8) & 0x0f)
        data[1] |= (vol & 0xff)

        print('Data[ {} {} ]'.format(hex(data[0]), hex(data[1])))

        res = spi.xfer2(data)

        print('Result: {}'.format(res))

        #time.sleep(0.1)

        GPIO.output(25, 0)

    except Exception as e:
        print(e)

spi.close()
