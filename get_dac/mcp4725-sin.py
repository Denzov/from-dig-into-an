import mcp4725_driver as mcp
import signal_generator as sg
import time
import numpy


amplitude = 1
signal_frequency = 1
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = mcp.MCP4725(5)
        
        while True:
            try:
                # dac.set_voltage(3)
                dac.set_voltage(sg.get_sin_wave_amplitude(signal_frequency, time.time())*amplitude*2)
                # print(sg.get_sin_wave_amplitude(signal_frequency, time0)*amplitude*2)
                # print(sg.get_sin_wave_amplitude(signal_frequency, time0))
                sg.wait_for_sampling_period(sampling_frequency)
                
            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()