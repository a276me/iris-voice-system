from scipy.io import wavfile
import sounddevice as sd
# import speech_recognition as sr
import os
from pyaudio import PyAudio, paInt16, paFloat32
from scipy.io.wavfile import *
from random import randint
import time
import wave
import base64
import matplotlib.pyplot as plt
import soundfile as sf

def disturbance():
    fs = 16000
    record = sd.rec(int(fs*0.01), fs, 1,)
    sd.wait()
    for i in record:
        if i > 0.1:
            print('detected')
            return True

disturbance()