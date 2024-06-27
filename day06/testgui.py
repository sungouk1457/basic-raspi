import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import RPi.GPIO as GPIO
import time

red = 26
blue = 19
green = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)

form_class = uic.loadUiType("./testgui.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_on.clicked.connect(self.btn1Function)
        self.btn_off.clicked.connect(self.btn2Function)

    def btn1Function(self):
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
    print("LED ON Button clicked")
    
    def btn2Function(self):
        PIO.output(red,True)
        GPIO.output(blue,True)
        GPIO.output(green,True)
        print("LED OFF Button clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
