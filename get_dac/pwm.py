
import RPi.GPIO as GPIO

import signal_generator as sg
import time

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(gpio_pin, pwm_frequency)
        self.pwm.start(0)
        
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        duty = voltage / self.dynamic_range * 100
        # print(duty)
        self.pwm.ChangeDutyCycle(duty)


amplitude = 1
signal_frequency = 1
sampling_frequency = 10000

if __name__ == "__main__":
    dac = PWM_DAC(12, 500, 3.3, True)

    try:
        while True:
            try:
                dac.set_voltage(sg.line_amp(signal_frequency, time.time())*amplitude*2)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()