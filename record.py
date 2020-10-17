
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



# print(o)
#
# exit(122)
# sd.play('./tmp/float32speech.wav')
# sd.wait()

fs=16000
myrecording = sd.rec(int(4 * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()  # Wait until recording is finished
print('finished')
sd.play(myrecording, fs)

write(f'./tmp/test.wav', fs, myrecording)

# data, fs = sf.read('./tmp/float32speech.wav', dtype='float32')
#
# plt.plot(data)
# plt.show()
# print(sd.wait()fs)
# sd.play(data, fs)
#
# sd.wait()



# import pyaudio
# import wave
#
# chunk = 1024  # Record in chunks of 1024 samples
# sample_format = pyaudio.paInt16  # 16 bits per sample
# channels = 1
# fs = 44100  # Record at 44100 samples per second
# seconds = 3
# filename = "output.wav"
#
# p = pyaudio.PyAudio()  # Create an interface to PortAudio
#
# print('Recording')
#
# stream = p.open(format=sample_format,
#                 channels=channels,
#                 rate=fs,
#                 frames_per_buffer=chunk,
#                 input=True)
#
# frames = []  # Initialize array to store frames
#
# # Store data in chunks for 3 seconds
# for i in range(0, int(fs / chunk * seconds)):
#     data = stream.read(chunk)
#     frames.append(data)
#
# # Stop and close the stream
# stream.stop_stream()
# stream.close()
# # Terminate the PortAudio interface
# p.terminate()
#
# print('Finished recording')
#
# # Save the recorded data as a WAV file
# wf = wave.open(filename, 'wb')
# wf.setnchannels(channels)
# wf.setsampwidth(p.get_sample_size(sample_format))
# wf.setframerate(fs)
# wf.writeframes(b''.join(frames))
# wf.close()
#
#
#
# fs, data = read('output.wav')
# plt.plot(data)
# plt.show()
#
#
#
# # def save_wave_file(filepath, data):
# #     wf = wave.open(filepath, 'wb')
# #     wf.setnchannels(1)
# #     wf.setsampwidth(2)
# #     wf.setframerate(16000)
# #     wf.writeframes(b''.join(data))
# #     wf.close()
# #
# # pa = PyAudio()
# #
# # stream = pa.open(format=paFloat32, channels=1,
# #                  rate=16000, input=True, frames_per_buffer=2000, )
# # my_buf = []
# # # count = 0
# # t = time.time()
# # while time.time() < t + 6:  # 秒
# #     string_audio_data = stream.read(2000)
# #     my_buf.append(string_audio_data)
# # # print('录音结束.')
# # save_wave_file('./tmp/static.wav', my_buf)
# # stream.close()