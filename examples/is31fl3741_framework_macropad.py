# SPDX-FileCopyrightText: 2023 Daniel Schaefer for Framework Computer
# SPDX-License-Identifier: MIT

import time
import board
from framework_is31fl3743 import IS31FL3743
import digitalio
import busio

# Enable LED controller via SDB pin
sdb = digitalio.DigitalInOut(board.GP29)
sdb.direction = digitalio.Direction.OUTPUT
sdb.value = True

i2c = busio.I2C(board.SCL, board.SDA)  # Or board.I2C()

# TODO: If I don't scan the bus, creating IS31FL3743 can't find the device. Why...?
i2c.try_lock()
i2c.scan()
i2c.unlock()

is31 = IS31FL3743(i2c, address=0x20)
is31.set_led_scaling(int(0xFF / 1))  # Full brightness
is31.global_current = 0xFF  # set current to max
is31.enable = True

for i in range(18 * 11):
    is31[i] = 0xFF

# Keep in the script to keep the LED controller on
while True:
    time.sleep(0.01)
