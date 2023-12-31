Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-is31fl3743/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/framework_is31fl3743/en/latest/
    :alt: Documentation Status

.. image:: https://github.com/FrameworkComputer/CircuitPython_IS31FL3743/workflows/Build%20CI/badge.svg
    :target: https://github.com/FrameworkComputer/CircuitPython_IS31FL3743/actions/
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

CircuitPython driver for the IS31FL3743 RGB Matrix IC.

This driver supports the following hardware: Lumissil IS31FL3743 LED controller.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-is31fl3743/>`_. To install for current user:

.. code-block:: shell

    pip3 install framework-circuitpython-is31fl3743

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install framework-circuitpython-is31fl3743

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install framework-circuitpython-is31fl3743

Usage Example
=============

Matrix:

.. code:: python

    from framework_is31fl3743.matrix import Matrix
    import board
    import busio
    with busio.I2C(board.SCL, board.SDA) as i2c:
        display = Matrix(i2c)
        display.fill(18 * 11)


Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/is31fl3743/en/latest/>`_.

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/FrameworkComputer/CircuitPython_is31fl3743/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
