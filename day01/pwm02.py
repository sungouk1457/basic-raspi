import RPi.GPIO as GPIO
import time

piezoPin = 13
melody = [130,146,164,174,195,220,246,261]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin,GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

try:
	while True:
		Buzz.start(25)
		key=int(input("키 입력: "))
		if(key in [1,2,3,4,5,6,7,8]):
			Buzz.ChangeFrequency(melody[key-1])
		elif key == 9:
			Buzz.stop()
except KeyboardInterrupt:
	GPIO.cleanup()
