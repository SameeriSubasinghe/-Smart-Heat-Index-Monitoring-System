import os

import Adafruit_DHT
import RPi.GPIO as GPIO
from dotenv import load_dotenv

load_dotenv()

GPIO.setmode(GPIO.BCM)

sensor = Adafruit_DHT.DHT11
pin = os.getenv('DHT_PIN')


def celsius_to_fahrenheit(degree):
    return (9 * degree) / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def calculate_heat_index(temperature, relative_humidity):
    temperature_in_fahrenheit = celsius_to_fahrenheit(temperature)
    # temperature_in_fahrenheit = temperature

    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -0.22475541
    c5 = -0.00683783
    c6 = -0.05481717
    c7 = 0.00122874
    c8 = 0.00085282
    c9 = -0.00000199

    heat_index = c1 + c2*temperature_in_fahrenheit + c3*relative_humidity + c4*temperature_in_fahrenheit*relative_humidity + c5*temperature_in_fahrenheit**2 + c6*relative_humidity**2 + c7*temperature_in_fahrenheit**2*relative_humidity + c8*temperature_in_fahrenheit*relative_humidity**2 + c9*temperature_in_fahrenheit**2*relative_humidity**2

    return fahrenheit_to_celsius(heat_index)

def heat_index():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return calculate_heat_index(temperature, humidity), humidity, temperature
