""" Example for using the SGP30 with CircuitPython and the Adafruit library"""

import time
import board
import busio
import adafruit_sgp30

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

print("SGP30 serial #", [hex(i) for i in sgp30.serial])

sgp30.iaq_init()
sgp30.set_iaq_baseline(0x190, 0x0)

elapsed_sec = 0

time.sleep(30)
while True:
    sgp30.eCO2
    sgp30.TVOC
    time.sleep(1)
    elapsed_sec += 1
    if elapsed_sec > 10:
        elapsed_sec = 0
        print(
            "**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x"
            % (sgp30.baseline_eCO2, sgp30.baseline_TVOC)
        )
with open('baseline.txt', 'w') as f:
    f.write(f"{hex(sgp30.baseline_eCO2)}, {hex(sgp30.baseline_TVOC)}")
