import time
import RPi.GPIO as GPIO
LED = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)

while True:
    GPIO.output(LED, True)
    time.sleep(3)
    print(GPIO.output)
    GPIO.output(LED, False)
    time.sleep(3)