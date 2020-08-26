# The MIT License (MIT)
#
# Copyright (c) 2020 M J Stanway for Otter Works LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`otterworks_drv8305` - Otter Works DRV8305 - 
=========================================================================================

CircuitPython driver for Texas Instruments DRV8305 Three-Phase Gate Driver

* Author(s): bluesquall
"""
import math
from time import sleep
from micropython import const

try:
    import struct
except ImportError:
    import ustruct as struct


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/bluesquall/OtterWorks_CircuitPython_DRV8305.git"

_DRV8305_WARNING_WATCHDOG_REGISTER = const(0x01)
_DRV8305_OV_VDS_FAULT_REGISTER = const(0x02)
_DRV8305_IC_FAULT_REGISTER = const(0x03)
_DRV8305_VGS_FAULT_REGISTER = const(0x04)
_DRV8305_HS_GATE_DRIVE_CONTROL_REGISTER = const(0x05)
_DRV8305_LS_GATE_DRIVE_CONTROL_REGISTER = const(0x06)
_DRV8305_GATE_DRIVE_CONTROL_REGISTER = const(0x07)
_DRV8305_RESERVED_REGISTER = const(0x08) # for completeness -- appears to always be zero
_DRV8305_IC_OPERATION_REGISTER = const(0x09)
_DRV8305_SHUNT_AMPLIFIER_CONTROL_REGISTER = const(0x0A)
_DRV8305_VOLTAGE_REGULATOR_CONTROL_REGISTER = const(0x0B)
_DRV8305_VDS_SENSE_CONTROL_REGISTER = const(0x0C)

class OtterWorks_DRV8305:
    """Driver for DRV8305 Three-Phase Gate Driver"""

    def __init__(self, spi, cs, baudrate=100000):
        # check for a known response to confirm the DRV8395 is there

        """
        import adafruit_bus_device.spi_device as spi_device  # pylint: disable=import-outside-toplevel

        self._spi = spi_device.SPIDevice(spi, cs, baudrate=baudrate)
        super().__init__()
        """

    def _read_register(self, register): # DRV8305 transactions are always 2 bytes
        query = 1 << 15 # read
        query |= (register & 0x0F) << 11) # address is 4-bit nibble
        # data bits [10:0] do not matter for a read command
        control = query.to_bytes(2, 'big')
        response = bytearray(2)
        self._spi.write_readinto(control, response)
        return response # N.B. first 5 bits of response don't matter

    def _write_register(self, register, value):
        command = 0 << 15 | (register & 0x0F) << 11).to_bytes(2, 'big')
        response = bytearray(2)
        self._spi.write_readinto(query, response)
        if response not 0x0000:
            raise ValueError("something bad happened")

    def _get_warning_watchdog_reset(self):
        return self._read_register(_DRV8305_WARNING_WATCHDOG_REGISTER)

    def _get_overcurrent(self):
        return self._read_register(_DRV8305_OV_VDS_FAULT_REGISTER)

    @property
    def mode(self):
        """
        Operation mode
        Allowed values are the constants MODE_*
        """
        return self._mode

    @mode.setter
    def mode(self, value):
        if not value in _DRV8305_MODES:
            raise ValueError("Mode '%s' not supported" % (value))
        self._mode = value
        # self._write_ctrl_meas()


