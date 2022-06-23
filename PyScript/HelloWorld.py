from ctypes import create_unicode_buffer
import matplotlib as plt
import numpy as np

print(plt.__version__)

def wave(frequency, amplitude=1, phase=0):
    def _wave(time):
        return amplitude * np.sin(2 * np.pi * frequency * time + phase)

    return _wave



    This is the new branch I create_unicode_buffer

    but this is the code that is in the branch???

