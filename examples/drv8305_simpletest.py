#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import time

import board
import busio
import digitalio
import otterworks_drv8305

# on beaglebone black, make sure SPI_1 pins are configured
# subprocess.run(["config-pin", "P9_17", "spi_cs"])
subprocess.run(["config-pin", "P9_18", "spi"])
subprocess.run(["config-pin", "P9_21", "spi"])
subprocess.run(["config-pin", "P9_22", "spi_sclk"])

cs = digitalio.DigitalInOut(board.P9_15)
cs.switch_to_output()
cs.value = False

spi = busio.SPI(board.SCK_1, board.MISO_1, board.MOSI_1)
drv8305 = otterworks_drv8305.OtterWorks_DRV8305(spi, cs)

while True:
    print("FAULT: %r" % (drv8305._get_warning_watchdog_reset().wwr.fault == True))
    time.sleep(3)
