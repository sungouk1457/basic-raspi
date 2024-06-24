from flask import Flask
import RPi.GPIO as GPIO

red = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(red,GPIO.OUT)
app=Flask(__name__)


@app.route("/led/<state>")
def led(state):
	if state == "on":
		GPIO.output(red,False)
		return "on"
	elif state == "off":
		GPIO.output(red,True)
		return "off"
	elif state == "clear":
		GPIO.cleanup()
		return "GPIO Cleanup()"

if __name__ == "__main__":
	app.run(host="0.0.0.0",port="10001",debug=True)
