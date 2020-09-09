import time
import busio, board
import adafruit_ahtx0

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ahtx0.AHTx0(i2c)

def get_temp():
    temp_c = sensor.temperature
    temp_f = (temp_c * 9.0/5)+32
    return temp_f

def get_hum():
    return sensor.relative_humidity
