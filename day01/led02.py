import RPi.GPIO as GPIO
import time 

red = 16
blue = 20
green = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)

try:
	while True:
		GPIO.output(red,False)
		GPIO.output(blue,True)
		GPIO.output(green,True)
		time.sleep(1)
		
		GPIO.output(red,True)
		GPIO.output(blue,False)
		GPIO.output(green,True)
		time.sleep(1)
		
		GPIO.output(red,True)
		GPIO.output(blue,True)
		GPIO.output(green,False)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()

