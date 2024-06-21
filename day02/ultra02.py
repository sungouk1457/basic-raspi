import RPi.GPIO as GPIO
import time

def measure():
   GPIO.output(trigPin, True)
   time.sleep(0.00001)
   GPIO.output(trigPin, False)
   start = time.time()

   while GPIO.input(echoPin) == False:
      start = time.time()
   while GPIO.input(echoPin) == True:
      stop = time.time()
      elapsed = stop - start
   distance = (elapsed * 19000) / 2

   return distance


trigPin = 18
echoPin = 23
piezoPin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)
#Buzz.start(50)

try:
   while True:
      distance = measure()
      print("Distance: %.2f cm" %distance)
      if(distance < 50 and distance > 30):
         Buzz.start(25)
         Buzz.ChangeFrequency(200)
         time.sleep(1)
         Buzz.ChangeFrequency(100)
         time.sleep(1)
      elif(distance <=30 and distance >10):
         Buzz.start(25)
         Buzz.ChangeFrequency(300)
         time.sleep(0.5)
         Buzz.ChangeFrequency(200)
         time.sleep(0.5)
      elif(distance <= 10 and distance>5):
         Buzz.start(25)
         Buzz.ChangeFrequency(400)
         time.sleep(0.25)
         Buzz.ChangeFrequency(300)
         time.sleep(0.25)
      elif(distance <= 5 and distance>0):
         Buzz.start(25)
         Buzz.ChangeFrequency(500)
         time.sleep(0.1)
         Buzz.ChangeFrequency(400)
         time.sleep(0.1)
      else:
         Buzz.stop()

      time.sleep(0.2)

except KeyboardInterrupt:
   Buzz.stop()
   GPIO.cleanup()
