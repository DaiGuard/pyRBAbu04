#! /usr/bin/env python

import RPi.GPIO as GPIO
import spidev
import sys
import time
import datetime

# Define pin number
SPI_ID=0
SPI_CN=1
SPI_MAX_SPEED_HZ=1000000
SPI_MODE=3
DAC_CS_PIN = 25

# module variables
spi = None

def open():
    global spi

    spi = spidev.SpiDev()
    spi.open(SPI_ID, SPI_CN)

    spi.max_speed_hz = SPI_MAX_SPEED_HZ
    spi.mode = SPI_MODE

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DAC_CS_PIN, GPIO.OUT)

def close():
    global spi

    if spi is not None:
        spi.close()

def output(ch: int, val: float):
    """_summary_

    Args:
        ch (int): _description_
        val (float): _description_

    Raises:
        Exception: _description_
    """
    global spi
    
    data = [0x00, 0x00]

    try:
        if val < 0.0 or val > 1.0:
            raise ValueError('over range input value')

        vol = int(4095*val)

        GPIO.output(DAC_CS_PIN, 1)

        if ch in [0, 1]:
            if ch == 1:
                data[0] |= 0x80
        else:
            raise ValueError('over range input channel')
        
        data[0] |= 0x10

        data[0] |= ((vol >> 8) & 0x0f)
        data[1] |= (vol & 0xff)

        res = spi.xfer2(data)

        GPIO.output(DAC_CS_PIN, 0)

    except Exception as e:
        print("\033[31m{}\033[0m".format(e), file=sys.stderr)
