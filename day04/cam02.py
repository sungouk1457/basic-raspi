from picamera2 import Picamera2
import RPi.GPIO as GPIO
import time
import datetime

swPin=21

picam2=Picamera2()
camera_config=picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()

GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin,GPIO.IN)
try:
    while True:
		if(GPIO.input(swPin)==True):
			now=datetime.datetime.now()
			print(now)
			filename = now.strftime("%Y-%m-%d %H:%M:%S")
			picam2.capture_file(filename+".jpg")
	time.sleep(2)
except KeyboardInterrupt:
	GPIO.cleanup()
