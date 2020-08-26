#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import time

import board
import busio
import otterworks_drv8305

spi = busio.SPI(board.SCK_1, board.MISO_1, board.MOSI_1)
cs = digitalio.DigitalInOut(board.P9_15)
drv8305 = otterworks_drv8305.OtterWorks_DRV8305(spi, cs)

while True:
    print(drv8305._get_warning_watchdog_reset())
    time.sleep(3)
