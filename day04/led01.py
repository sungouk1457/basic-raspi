import RPi.GPIO as GPIO
import time

a = 26
b = 13
c = 16
d = 20
e = 21
f = 19
g = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)
GPIO.setup(f, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)

try:
    while True:
        GPIO.output(a, False) #1
        GPIO.output(b, True)
        GPIO.output(c, True)
        GPIO.output(d, False)
        GPIO.output(e, False)
        GPIO.output(f, False)
        GPIO.output(g, False)
        time.sleep(1)

        GPIO.output(a, True)#2
        GPIO.output(b, True)
        GPIO.output(c, False)
        GPIO.output(d, True)
        GPIO.output(e, True)
        GPIO.output(f, False)
        GPIO.output(g, True)
        time.sleep(1)

        GPIO.output(a, True)#3
        GPIO.output(b, True)
        GPIO.output(c, True)
        GPIO.output(d, True)
        GPIO.output(e, False)
        GPIO.output(f, False)
        GPIO.output(g, True)
        time.sleep(1)

        GPIO.output(a, False)#4
        GPIO.output(b, True)
        GPIO.output(c, True)
        GPIO.output(d, False)
        GPIO.output(e, False)
        GPIO.output(f, True)
        GPIO.output(g, True)
        time.sleep(1)

        GPIO.output(a, True)#5
        GPIO.output(b, False)
        GPIO.output(c, True)
        GPIO.output(d, True)
        GPIO.output(e, False)
        GPIO.output(f, True)
        GPIO.output(g, True)
        time.sleep(1)

        GPIO.output(a, True)#6
        GPIO.output(b, False)
        GPIO.output(c, True)
        GPIO.output(d, True)
        GPIO.output(e, True)
        GPIO.output(f, True)
        GPIO.output(g, True)
        time.sleep(1)

        GPIO.output(a, True)#7
        GPIO.output(b, True)
        GPIO.output(c, True)
        GPIO.output(d, False)
        GPIO.output(e, False)
        GPIO.output(f, True)
        GPIO.output(g, False)
        time.sleep(1)

        GPIO.output(a, True)#8
        GPIO.output(b, True)
        GPIO.output(c, True)
        GPIO.output(d, True)
        GPIO.output(e, True)
        GPIO.output(f, True)
        GPIO.output(g, True)
        time.sleep(1)

        GPIO.output(a, True)#9
        GPIO.output(b, True)
        GPIO.output(c, True)
        GPIO.output(d, True)
        GPIO.output(e, False)
        GPIO.output(f, True)
        GPIO.output(g, True)
        time.sleep(1)

        GPIO.output(a, True)#0
        GPIO.output(b, True)
        GPIO.output(c, True)
        GPIO.output(d, True)
        GPIO.output(e, True)
        GPIO.output(f, True)
        GPIO.output(g, False)
        time.sleep(1)

except KeyboardInterrupt:  # Ctrl + C
    GPIO.cleanup()
