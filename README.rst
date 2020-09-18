Introduction
============

SPI driver for the Texas Instruments DRV8305 Three-Phase Gate Driver.

Patterned after the Adafruit BME280 CircuitPython driver, since that's what I had lying around to hack, test, and compare against.

Installation and Dependencies
=============================

This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure that the driver and all dependencies are available on the
CircuitPython filesystem.  This can be most easily achieved by downloading and
installing the latest
`Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_
on your device.

Installing from PyPI
--------------------

On supported GNU/Linux systems like the BeagleBone Black, you can install the driver locally `from
PyPI <https://pypi.org/project/otterworks-circuitpython-drv8305/>`_. To install for current user:

.. code-block:: shell

    pip3 install --user otterworks-circuitpython-drv8305

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install otterworks-circuitpython-drv8305

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install otterworks-circuitpython-drv8305

Usage Example
=============

.. code-block:: python

    import time

    import board
    import busio
    import digitalio

    import otterworks_drv8305

    spi = busio.SPI(board.SCK_1, board.MISO_1, board.MOSI_1)
    cs = digitalio.DigitalInOut(board.P9_17))
    drv8305 = otterworks_drv8305.OtterWorks_DRV8305(spi, cs)

    while True:
        print(drv8305._get_warning_watchdog_reset())
        time.sleep(1)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/bluesquall/OtterWorks_CircuitPython_DRV8305/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

TODO: build and share on readthedocs.org
