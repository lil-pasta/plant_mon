import time
import board, busio
from adafruit_seesaw.seesaw import Seesaw

i2c = busio.I2C(board.SCL, board.SDA)
ss = Seesaw(i2c, addr=0x36)

def get_moist():
    # values are between 200 (very dry) and 2000 (very wet)
    return ss.moisture_read()
