import pyttsx3 as pt
import sys
import random
import scipy.io.wavfile as wav
import sounddevice as sd

def shutdown(cmd):
    e = pt.Engine()
    e.say("good bye sir")
    e.runAndWait()
    sys.exit(101)

def record_denoiser(cmd):
    e = pt.Engine()
    e.say("Recording a new noise file")
    e.runAndWait()
    e.say("please remain silent for the best possible effect")
    e.runAndWait()
    e.say("starting in 3, 2, 1")
    e.runAndWait()
    fs = 16000
    myrecording = sd.rec(int(4 * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    e.say("finished")
    e.runAndWait()
    sd.play(myrecording, fs)
    sd.wait()
    wav.write(f'./tmp/static.wav', fs, myrecording)


routes = [
    {'name': 'shutdown', 'main': shutdown, 'keys': ['exit','shutdown','shut down']},
    {'name': 'new denoiser', 'main': record_denoiser, 'keys': ['denoiser','record','new denoiser','e nois']}
]