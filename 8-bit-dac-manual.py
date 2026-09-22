import RPi.GPIO as GPIO
import time

leds = [22, 27, 17, 26, 25, 21, 20, 16]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

dynamic_range = 3.072

def number_to_dac(cnt):
    for i in range(8):
        led_st = int(bool(cnt & (0b1 << i)))
        print(led_st)
        GPIO.output(leds[i], led_st)

def voltage_to_number(v):
    if not(0 <= v <= dynamic_range):
        return 0
    return int(v / dynamic_range * 255)

try:
    while True:
        try:
            voltage = float(input('Введите напряжение в Вольтах:'))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        except ValueError:
            print('Не число. Попробуй снова.')

finally:
    number_to_dac(0)
    GPIO.cleanup()