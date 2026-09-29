
import numpy
import time

def get_sin_wave_amplitude(freq, time):
    return (numpy.sin(freq * 2 * numpy.pi * time) + 1) / 2

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)

def line_amp(freq, time):
    phase = (time * freq) % 1.0
    return 1.0 - abs(2.0 * phase - 1.0)