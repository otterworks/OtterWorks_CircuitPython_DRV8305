#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
import subprocess
import time

import board
import busio
import digitalio
import otterworks_drv8305

logging.basicConfig(format='%(asctime)s\t%(levelname)s\t%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %z', level=logging.DEBUG,
        handlers=[RotatingFileHandler('drv8305monitor.log',
            maxBytes=10000000, backupCount=13)])

# on beaglebone black, make sure SPI_0 pins are configured
subprocess.run(["config-pin", "P9_17", "spi_cs"])
subprocess.run(["config-pin", "P9_18", "spi"])
subprocess.run(["config-pin", "P9_21", "spi"])
subprocess.run(["config-pin", "P9_22", "spi_sclk"])

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = digitalio.DigitalInOut(board.P9_17)
drv8305 = otterworks_drv8305.OtterWorks_DRV8305(spi, cs)

while True:

    wwr = drv8305._get_warning_watchdog_reset() # TODO: wrap _get methods

    if wwr.fault:
        level = logging.CRITICAL
    else:
        level = logging.INFO
    logging.log(level, "fault: {}".format(wwr.fault == True))

    if wwr.overtemp:
        level = logging.CRITICAL
    else:
        level = logging.INFO
    logging.log(level, "overtemperature: {}".format(wwr.overtemp == True))

    if wwr.pvdd_ov:
        level = logging.CRITICAL
    else:
        level = logging.INFO
    logging.log(level, "PVDD overvoltage: {}".format(wwr.pvdd_ov == True))

    if wwr.overtemp:
        level = logging.CRITICAL
    else:
        level = logging.INFO
    logging.log(level, "PVDD undervoltage: {}".format(wwr.pvdd_uv == True))

    if wwr.overtemp:
        level = logging.CRITICAL
    else:
        level = logging.INFO
    logging.log(level, "charge pump undervoltage: {}".format(wwr.vchp_uv == True))

    # TODO: temp 1-4, vds_status

    oc = drv8305._get_overcurrent()
    logging.debug("high-side overcurrents: A = {a}, B = {b}, C = {c}".format(
        a = (oc.high_a == True), b = (oc.high_b == True), c = (oc.high_c == True)))
    logging.debug("low-side overcurrents: A = {a}, B = {b}, C = {c}".format(
        a = (oc.low_a == True), b = (oc.low_b == True), c = (oc.low_c == True)))
    logging.debug("sense overcurrents: A = {a}, B = {b}, C = {c}".format(
        a = (oc.sense_a == True), b = (oc.sense_b == True), c = (oc.sense_c == True)))

    drive = drv8305._get_drive_control()
    logging.debug("active freewheeling: {}".format(drive.active_freewheeling == True))
    logging.debug("PWM mode: {}".format(drive.pwm_mode))
    logging.debug("dead time: {}".format(drive.dead_time))
    logging.debug("blanking: {}".format(drive.vds_sense_blanking))
    logging.debug("deglitch: {}".format(drive.vds_sense_deglitch))

    time.sleep(3)
