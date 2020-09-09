import time, os, atexit
import busio, board
import adafruit_sgp30

def save_base(sgp30):
    voc_base, eco2_base = sgp30.baseline_TVOC, sgp30.baseline_eCO2
    with open('vocsen/baseline.txt', 'w') as f:
        f.write(f"{hex(eco2_base)}, {hex(voc_base)}")

def load_base():
    voc_base, eco2_base = 0, 0
    #for testing purposes
    # with open('baseline.txt', 'r') as f:
    with open('vocsen/baseline.txt', 'r') as f:
        for line in f:
            voc_base = int(line.split(',')[1], 16)
            eco2_base = int(line.split(',')[0], 16)
    return [eco2_base, voc_base]

"""init shit"""
def start_sgp():
    i2c = busio.I2C(board.SCL, board.SDA)
    sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
    # base = load_base()
    sgp30.iaq_init()
    # sgp30.set_iaq_baseline(base[0], base[1])
    # print(f"baseline:: {sgp30.baseline_eCO2}\t{sgp30.baseline_TVOC}")
    return sgp30

"""the sensor takes ~20 seconds to "warm up" after init so
dont call this before that much time has passed"""
def get_voc(sgp30):
    # print(f"baseline:: {sgp30.baseline_eCO2}\t{sgp30.baseline_TVOC}")
    return [sgp30.eCO2, sgp30.TVOC, sgp30.baseline_eCO2, sgp30.baseline_TVOC]

"""for testing"""
if __name__ == '__main__':
    sgp = start_sgp()
    i = 0
    while True:
        if i > 10:
            print(f"baselines:: eco2 = {sgp.baseline_eCO2}\tTVOC = {sgp.baseline_TVOC}")
            i = 0
        else:
            print(f"eco2 = {get_voc(sgp)[0]}\tTVOC = {get_voc(sgp)[1]}")
            i+=1
            time.sleep(1)
