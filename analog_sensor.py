import board #type: ignore
import busio #type: ignore
import adafruit_ads1x15.ads1015 as ADS  #type: ignore
from adafruit_ads1x15.analog_in import AnalogIn #type: ignore
from time import sleep


i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)

def read_hume():
    prom1, prom2, prom3 = 0, 0, 0
    for i in range(5):
        chan1 = AnalogIn(ads, ADS.P0)  # valor sensor humedad 1
        chan2 = AnalogIn(ads, ADS.P1)  # valor sensor humedad 2
        chan3 = AnalogIn(ads, ADS.P2)  # valor sensor humedad 3
        prom1 += chan1.value
        prom2 += chan2.value
        prom3 += chan3.value
        sleep(0.2)
    return prom1 / 5, prom2 / 5, prom3 / 5

def read_luz():
    prom0 = 0
    for i in range(5):
        chan0 = AnalogIn(ads, ADS.P3)
        prom0 += chan0.value
        sleep(0.2)
    return prom0 / 5

if __name__ == "__main__":
    print(read_hume())
    print(read_luz())