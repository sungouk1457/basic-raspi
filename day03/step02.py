import RPi.GPIO as GPIO
import time

steps = [21,22,23,24]
GPIO.setmode(GPIO.BCM)

for stepPin in steps:
	GPIO.setup(stepPin, GPIO.OUT)
	GPIO.output(stepPin, 0)

try:
	while 1:
		for i in range(4):
			for j in range(4):
				GPIO.output(steps[j], 1 if (i == j) else 0)
				time.sleep(0.01)
except KeyboardInterrupt:
	GPIO.cleanup()
