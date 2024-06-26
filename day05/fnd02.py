import RPi.GPIO as GPIO
import time

segment_pins = [26,13,16,20,21,19,12]
digit_pins = [6,22,27,25]

segment_patterns = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [0, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 1, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 0, 0, 1, 1]   # 9
]

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in segment_pins:
        GPIO.setup(pin, GPIO.OUT)
    for pin in digit_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

def display_number(number):
    digits = [int(d) for d in str(number).zfill(4)]
    for i in range(4):
        GPIO.output(digit_pins[i], GPIO.LOW)
        pattern = segment_patterns[digits[i]]
        for pin, state in zip(segment_pins, pattern):
            GPIO.output(pin, state)
        time.sleep(0.005)
        GPIO.output(digit_pins[i], GPIO.HIGH)
def main():
    setup()
    try:
        number =1234
        while True:
            display_number(number)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
