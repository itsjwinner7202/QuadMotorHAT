import time
import gpiozero
from gpiozero import Motor, DigitalOutputDevice

def _create_motors():
	global M1, M2, M3, M4

	_e1 = DigitalOutputDevice(12, initial_value=True)
	_e2 = DigitalOutputDevice(16, initial_value=True)
	_e3 = DigitalOutputDevice(20, initial_value=True)
	_e4 = DigitalOutputDevice(21, initial_value=True)

	M1 = Motor(forward=26, backward=19, pwm=True)
	M2 = Motor(forward=13, backward=6, pwm=True)
	M3 = Motor(forward=5, backward=11, pwm=True)
	M4 = Motor(forward=9, backward=10, pwm=True)

_create_motors()

__all__ = ["M1", "M2", "M3", "M4"]