import os

import RPi.GPIO as GPIO
from dotenv import load_dotenv

load_dotenv()

GPIO.setmode(GPIO.BCM)

servo_pin = int(os.getenv('SERVO_PIN'))

GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)


def set_angle(heat_index):

    angle = 0
    if heat_index < 27:
        angle = 0 + ((36 / 27) * heat_index)
    elif heat_index < 32:
        angle = 36 + ((36 / 5) * (heat_index - 27))
    elif heat_index < 40:
        angle = 72 + ((36 / 8) * (heat_index - 32))
    elif heat_index < 51:
        angle = 108 + ((36 / 11) * (heat_index - 40))
    else:
        angle = 162

    angle = 180 - angle

    duty = angle / 18 + 2.5
    pwm.ChangeDutyCycle(duty)


def run_motor(heat_index):
    set_angle(heat_index)
