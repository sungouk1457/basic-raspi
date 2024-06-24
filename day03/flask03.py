# URL접속을 /led/on, /led/off로 접속하면 led를 on,off하는 웹페이지

from flask import Flask
import RPi.GPIO as GPIO

red = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(red,GPIO.OUT)
app=Flask(__name__)

@app.route("/led/on")
def on():
	GPIO.output(red,False)
	return "LED on"

@app.route("/led/off")
def off():
	GPIO.output(red,True)
	return "LED off"

if __name__ == "__main__":
	app.run(host="0.0.0.0",port="10001",debug=True)
