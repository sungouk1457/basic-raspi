import RPi.GPIO as GPIO
import time

segment_pins = [26, 13, 16, 20, 21, 19, 12]
digit_pins = [6, 22, 27, 25]
button_pin = 17

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
    GPIO.setwarnings(False)
    for pin in segment_pins:
        GPIO.setup(pin, GPIO.OUT)

    for pin in digit_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

    GPIO.setup(button_pin, GPIO.IN)

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
    current_number = 1

    try:
        while True:
            display_number(current_number)

            if GPIO.input(button_pin) == GPIO.HIGH:
                current_number += 1
                if current_number > 9999:
                    current_number = 1
                time.sleep(0.2)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
