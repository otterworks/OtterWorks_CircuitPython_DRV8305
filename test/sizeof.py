#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ctypes import sizeof
import otterworks_drv8305

print('sizeof(_DRV8305_SPI_Word) ={}'.format(sizeof(otterworks_drv8305._DRV8305_SPI_Word)))
print('sizeof(_Warning_Watchdog_Reset_Flags) ={}'.format(sizeof(otterworks_drv8305._Warning_Watchdog_Reset_Flags)))
print('sizeof(_Overcurrent_Flags) ={}'.format(sizeof(otterworks_drv8305._Overcurrent_Flags)))
print('sizeof(_IC_Fault_Flags) ={}'.format(sizeof(otterworks_drv8305._IC_Fault_Flags)))
print('sizeof(_VGS_Fault_Flags) ={}'.format(sizeof(otterworks_drv8305._VGS_Fault_Flags)))
print('sizeof(_Gate_Control) ={}'.format(sizeof(otterworks_drv8305._Gate_Control)))
print('sizeof(_Drive_Control) ={}'.format(sizeof(otterworks_drv8305._Drive_Control)))
print('sizeof(_IC_Operation_Control) ={}'.format(sizeof(otterworks_drv8305._IC_Operation_Control)))
print('sizeof(_Shunt_Amplifier_Control) ={}'.format(sizeof(otterworks_drv8305._Shunt_Amplifier_Control)))
print('sizeof(_Voltage_Regulator_Control) ={}'.format(sizeof(otterworks_drv8305._Voltage_Regulator_Control)))
print('sizeof(_Voltage_Sense_Control) ={}'.format(sizeof(otterworks_drv8305._Voltage_Sense_Control)))
