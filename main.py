
import RPi.GPIO as GPIO

leds = [22, 27, 17, 26, 25, 21, 20, 16]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

# GPIO.cleanup()


while True:
    # GPIO.output(leds[0], 0)
    GPIO.output(leds, 0)

    pass

try:
    pass
finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()