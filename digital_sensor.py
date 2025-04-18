import adafruit_dht #type: ignore
import board #type: ignore
import time

dht_device = adafruit_dht.DHT11(board.D17)

def read_digital():
    prom0, prom1 = 0, 0
    for i in range(3):
        try:
            for i in range(5):
                temp = dht_device.temperature
                hume = dht_device.humidity
                if temp is not None and hume is not None:
                    prom0 += temp * 10
                    prom1 += hume * 10
                    time.sleep(1.5)
            return prom0 / 5, prom1 / 5
        except RuntimeError as error:
            time.sleep(2)
    return False, False
if __name__ == "__main__":
    print(read_digital())