import time
import busio, board
import adafruit_veml7700

i2c = busio.I2C(board.SCL, board.SDA)
veml = adafruit_veml7700.VEML7700(i2c)

def get_lux():
    return veml.lux

