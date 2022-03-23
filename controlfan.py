from time import sleep
from pathlib import Path
import parallel

port = parallel.Parallel("/dev/parport0")

ON_THRESHOLD = 65
OFF_THRESHOLD = 55
SLEEP_INTERVAL = 5

def get_temp():
    temperature = Path('/sys/class/thermal/thermal_zone0/temp').read_text()
    return int(temperature) / 1000

while(True):

    temp = get_temp()
    print(temp)
    if temp > ON_THRESHOLD:
         port.setData(0x1)
    elif temp < OFF_THRESHOLD:
        port.setData(0x0)
    sleep(SLEEP_INTERVAL)