import RPi.GPIO as GPIO
import time

red = 16

GPIO.setmode(GPIO.BCM)

GPIO.setup(red,GPIO.OUT)

try:
	while True:
		key = input("키 입력: ")
		if(key == "o"):
			GPIO.output(red,False)
		elif(key == "x"):
			GPIO.output(red,True)
except KeyboardInterrupt:
	GPIO.cleanup()
