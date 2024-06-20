# basic-raspi
IoT 개발자과정 라즈베리파이 리포지토리

## 1일차
- 라즈베리파이
    - 옴의 법칙
        - V(전압) = I(전류)R(저항)
    - 키르히호프
    - GPIO 설정함수
        - GPIO.setmode(GPIO.BOARD) - wPi
        - GPIO.setmode(GPIO.BCM) - BCM
        - GPIO.setup(channel, GPIO.mode)
            - channel: 핀번호, mode: IN/OUT
        - GPIO.cleanup()
    
    - GPIO 출력함수
        - GPIO.output(channel, state)
            - channel: 핀번호, state: HIGH/LOW or 1/0 or True/False
    
    - GPIO 입력함수
        - GPIO.input(channel)
            - channel: 핀번호, 반환값: H/L or 1/0 or T/F

    - 시간지연 함수
        - time.sleep(secs)