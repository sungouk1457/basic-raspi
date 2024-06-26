import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import RPi.GPIO as GPIO
import time

fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f]
fndSegs = [22, 4, 12, 16, 20, 27, 25]
fndSels = [24, 17, 5, 6]
red = 26
blue = 19
green = 13
buzzer = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)

for fndSeg in fndSegs:
    GPIO.setup(fndSeg, GPIO.OUT)
    GPIO.output(fndSeg, 0)

for fndSel in fndSels:
    GPIO.setup(fndSel, GPIO.OUT)
    GPIO.output(fndSel, 1)

Buzz = GPIO.PWM(buzzer, 440)
Buzz.start(0)

form_class = uic.loadUiType("./testgui.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.fnd_timer = QTimer(self)
        self.fnd_timer.timeout.connect(self.updateFND)
        self.led_timer = QTimer(self)
        self.led_timer.timeout.connect(self.changeLED)
        self.led_state = 0  

        self.btnstart.clicked.connect(self.startFND)
        self.btnstop.clicked.connect(self.stopFND)
        self.btn_on.clicked.connect(self.startLED)
        self.btn_off.clicked.connect(self.stopLED)
        self.btn_buzzeron.clicked.connect(self.startBuzzer)
        self.btn_buzzeroff.clicked.connect(self.stopBuzzer)
        self.btncleanup.clicked.connect(self.cleanup)

        self.lcdNumber.display(0)

        self.count_fnd = 0
        self.fnd_running = False
        self.buzzer_on = False

    def startFND(self):
        if not self.fnd_running:
            self.fnd_running = True
            self.fnd_timer.start(1)

    def stopFND(self):
        self.fnd_running = False
        self.fnd_timer.stop()
        self.clearFND()

    def updateFND(self):
        if self.fnd_running:
            if self.count_fnd <= 9999:
                self.displayFND(self.count_fnd)
                self.displayLCD(self.count_fnd)
                self.count_fnd += 1
            else:
                self.stopFND()

    def displayFND(self, num):
        d1000 = num // 1000
        d100 = (num % 1000) // 100
        d10 = (num % 100) // 10
        d1 = num % 10
        
        for i, d in enumerate([d1, d10, d100, d1000]):
            fndOut(int(d), i)
            time.sleep(0.001)

    def clearFND(self):
        for sel in fndSels:
            GPIO.output(sel, GPIO.HIGH)
        for seg in fndSegs:
            GPIO.output(seg, GPIO.LOW)
    
    def toggleBuzzer(self):
        if not self.buzzer_on:
            self.startBuzzer()
        else:
            self.stopBuzzer()

    def startBuzzer(self):
        Buzz.ChangeFrequency(440)  
        Buzz.ChangeDutyCycle(50)
        self.buzzer_on = True

    def stopBuzzer(self):
        Buzz.ChangeDutyCycle(0)
        self.buzzer_on = True

    def startLED(self):
        self.led_timer.start(1000)

    def stopLED(self):
        self.led_timer.stop()
        GPIO.output(red, True)
        GPIO.output(blue, True)
        GPIO.output(green, True)

    def changeLED(self):
        if self.led_state == 0:
            GPIO.output(red, False)
            GPIO.output(blue, True)
            GPIO.output(green, True)
            self.led_state = 1
        elif self.led_state == 1:
            GPIO.output(red, True)
            GPIO.output(blue, False)
            GPIO.output(green, True)
            self.led_state = 2
        elif self.led_state == 2:
            GPIO.output(red, True)
            GPIO.output(blue, True)
            GPIO.output(green, False)
            self.led_state = 0

    def displayLCD(self, num):
        self.lcdNumber.display(num)

    def cleanup(self):
        self.fnd_timer.stop()
        self.led_timer.stop()
        GPIO.cleanup()
        self.lcdNumber.display(0)
        self.count_fnd = 0
        self.clearFND()

    def closeEvent(self, event):
        self.cleanup()
        event.accept()

def fndOut(data, sel):
    for i in range(0, 7):
        GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i))
    
    for j in range(0, 4):
        if j == sel:
            GPIO.output(fndSels[j], GPIO.LOW)
        else:
            GPIO.output(fndSels[j], GPIO.HIGH)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())
