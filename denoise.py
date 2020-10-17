import scipy.io.wavfile as wav
import noisereduce as nr
import sounddevice as sd
import numpy as np
import pyaudio
import matplotlib.pyplot as plt
import soundfile as sf
import time

def denoiser(file):
    data, fs = sf.read(file, dtype='int16')
    noise, fs = sf.read('./tmp/static.wav', dtype='int16')
    data = list(data)
    for i in range(len(data)):
        data[i] = float(data[i])
    data = np.array(data, dtype='float32')

    noise = list(noise)
    for i in range(len(noise)):
        noise[i] = float(noise[i])
    noise = np.array(noise, dtype='float32')

    ret = nr.reduce_noise(data, noise_clip=noise, verbose=False)
    ret = np.array(ret, dtype='int16')
    wav.write('speech.wav', fs, ret)

# def denoiser2(data):
#     noise, fs = sf.read('./tmp/static.wav', dtype='float32')
#     print(noise)
#     print(data)
#     ret = nr.reduce_noise(data, noise_clip=noise[:len(data)], verbose=False)
#     ret = np.array(ret, dtype='int16')
#     return ret




