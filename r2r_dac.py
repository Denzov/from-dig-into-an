
import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    
    def set_number(self, cnt):
        for i in range(len(self.gpio_bits)):
            led_st = int(bool(cnt & (0b1 << i)))
            GPIO.output(self.gpio_bits[i], led_st)

    def set_voltage(self, voltage):
        duty = int(voltage / self.dynamic_range * 255) % 256
        self.set_number(duty)


    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        dac = R2R_DAC([22, 27, 17, 26, 25, 21, 20, 16], 3.155, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()