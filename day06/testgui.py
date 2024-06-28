import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import RPi.GPIO as GPIO
import time

# FND 데이터
fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f]

# FND 세그먼트 핀
fndSegs = [22, 4, 12, 16, 20, 27, 25]

# FND 선택 핀
fndSels = [21, 17, 5, 6]

# LED 핀
red = 26
blue = 19
green = 13

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

for fndSeg in fndSegs:
    GPIO.setup(fndSeg, GPIO.OUT)
    GPIO.output(fndSeg, GPIO.LOW)

for fndSel in fndSels:
    GPIO.setup(fndSel, GPIO.OUT)
    GPIO.output(fndSel, GPIO.HIGH)

form_class = uic.loadUiType("./testgui.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # QTimer 설정
        self.fnd_timer = QTimer(self)
        self.fnd_timer.timeout.connect(self.updateFND)
        self.led_timer = QTimer(self)
        self.led_timer.timeout.connect(self.changeLED)
        self.led_state = 0  # 초기 상태는 Red LED

        # 버튼 이벤트 연결
        self.btnstart.clicked.connect(self.startFND)
        self.btnstop.clicked.connect(self.stopFND)
        self.btn_on.clicked.connect(self.startLED)
        self.btn_off.clicked.connect(self.stopLED)
        self.btncleanup.clicked.connect(self.cleanup)

        # LCD 초기화
        self.lcdNumber.display(0)

        # FND 초기화
        self.count_fnd = 0
        self.fnd_running = False  # FND 동작 여부 플래그

    def startFND(self):
        if not self.fnd_running:
            self.fnd_running = True
            self.fnd_timer.start(1)  # 1ms 간격으로 FND 업데이트

    def stopFND(self):
        self.fnd_running = False
        self.fnd_timer.stop()

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
            fndOut(d, i)
            time.sleep(0.0001)
            fndOut(0x00, i)  # FND 초기화

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
        for fndSeg in fndSegs:
            GPIO.setup(fndSeg, GPIO.OUT)
            GPIO.output(fndSeg, GPIO.LOW)
        for fndSel in fndSels:
            GPIO.setup(fndSel, GPIO.OUT)
            GPIO.output(fndSel, GPIO.HIGH)

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

# 추가한 FND 동작 코드
def runFND():
    count = 0
    try:
        while True:
            count += 1
            d1000 = count // 1000
            d100 = (count % 1000) // 100
            d10 = (count % 100) // 10
            d1 = count % 10
            d = [d1, d10, d100, d1000]

            for i in range(3, -1, -1):
                fndOut(d[i], i)  # FND에 값을 출력
                time.sleep(0.001)  # 출력 시간 간격

            if count == 9999:
                count = -1

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    # FND를 별도의 스레드에서 실행
    import threading
    fnd_thread = threading.Thread(target=runFND)
    fnd_thread.start()

    # PyQt GUI 실행
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())
