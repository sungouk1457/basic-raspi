import RPi.GPIO as GPIO
import time

pins = [26, 13, 16, 20, 21, 19, 12]

patterns = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1]   # 9
]

button_pin = 25

GPIO.setmode(GPIO.BCM)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

GPIO.setup(button_pin, GPIO.IN)

def display_number(number):
    pattern = patterns[number]
    for pin, state in zip(pins, pattern):
        GPIO.output(pin, state)

try:
    current_number = 0
    display_number(current_number)

    while True:
        button_state = GPIO.input(button_pin)
        if button_state == GPIO.HIGH:
            current_number = (current_number + 1) % 10
            display_number(current_number)
            time.sleep(0.3)

except KeyboardInterrupt:
    GPIO.cleanup()
