import time

from actuator import run_motor
from inputs import heat_index
from prediction import get_prediction
from mqtt_handler import publish_msg
import os
from dotenv import load_dotenv

load_dotenv()
get_prediction()

INTERVAL = float(os.getenv('INTERVAL'))

try:
    run_motor(6)
    while True:
        heat_index_val, humidity, temperature = heat_index()
        print(heat_index_val, humidity, temperature)
        publish_msg(temperature, humidity, heat_index_val)
        run_motor(heat_index_val)

        time.sleep(INTERVAL)
except:
    raise 'Failed to read data from sensor'
