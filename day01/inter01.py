#interrupt

import RPi.GPIO as GPIO
import time

#핀 설정
red = 16
switch = 6

#인터럽트 변수
intFlag = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)

def ledBlink(channel):
	global intFlage
	if intFlag == False:
		GPIO.output(red,True)
		intFlag = True
	else:
		GPIO.output(red, False)
		intFlag = False

#인터럽트 설정(switch핀 에 rising신호가 잡히면 callback함수를 실행
GPIO.add_event_detect(switch, GPIO,RISING, callback=ledBlink)

try:
	while True:
		pass

except KeyboardInterrupt:
	GPIO.cleanup()
