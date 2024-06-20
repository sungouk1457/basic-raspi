import RPi.GPIO as GPIO
import time

switch = 6
red = 16
blue = 20
green = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)

index = 0
last_state=GPIO.input(switch)

try:
	while True:
		current_state = GPIO.input(switch)
		if last_state == GPIO.HIGH and current_state == GPIO.LOW:
			if index == 0:
				GPIO.output(red, False)
				GPIO.output(blue, True)
				GPIO.output(green, True)
				index = 1
			elif index == 1:
				GPIO.output(red, True)
				GPIO.output(blue, False)
				GPIO.output(green, True)
				index = 2
			elif index == 2:
				GPIO.output(red, True)
				GPIO.output(blue, True)
				GPIO.output(green, False)
				index = 0
		last_state = current_state  
		time.sleep(0.1)  

except KeyboardInterrupt:
	GPIO.cleanup()
