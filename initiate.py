

# def denoiser(file):
#     print('start den')
#     fp, data = wav.read(file)
#     t, n = wav.read('./tmp/static.wav')
#     ret = nr.reduce_noise(audio_clip=data, noise_clip=n, verbose=False)
#     ret = np.asarray(ret, dtype='float32')
#     wav.write('./tmp/denoised.wav', rate=fp, data=ret)
#     sd.play(ret,16000)
#     sd.wait()
#     print('finished denoise')

import wave
import requests
import time
import base64
import numpy as np
from pyaudio import *
import noisereduce as nr
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
import denoise
import pyttsx3 as pt
import re
import random

SEC = 4
framerate = 16000  # 采样率
num_samples = 1024  # 采样点
channels = 1  # 声道
sampwidth = 2  # 采样宽度2bytes
FILEPATH = 'speech.wav'

base_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
APIKey = "*******"
SecretKey = "*******"

HOST = base_url % (APIKey, SecretKey)


def getToken(host):
    res = requests.post(host)
    return res.json()['access_token']


def save_wave_file(filepath, data):
    wf = wave.open(filepath, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()


def my_record(sec, wake_val: float=0.05):
    print('record')
    # pa = PyAudio()
    # stream = pa.open(format=paInt16, channels=channels,
    #                  rate=framerate, input=True, frames_per_buffer=num_samples)
    # my_buf = []
    # # count = 0
    # t = time.time()
    # # print('正在录音...')
    #
    # while time.time() < t + 2:  # 秒
    #     string_audio_data = stream.read(num_samples)
    #     my_buf.append(string_audio_data)
    # # print('录音结束.')
    # save_wave_file(FILEPATH, my_buf)
    # stream.close()
    while True:
        test = sd.rec(int(16000*0.5), 16000,1)
        sd.wait()
        # plt.plot(recc)
        # plt.show()
        for i in test:
            if i > wake_val:

                recc = sd.rec(int(sec * framerate), samplerate=framerate, channels=1, dtype='int16')
                sd.wait()
                # denoise.denoiser(FILEPATH)
                recc = np.concatenate((test, recc))
                wav.write(FILEPATH, framerate, recc)

                return


def get_audio(file):
    # fp, data = wav.read(file)
    # t, n = wav.read('./tmp/static.wav')
    # print(n.dtype)
    # print(data.dtype)
    # data.dtype = 'float32'
    #
    # ret = nr.reduce_noise(audio_clip=data,
    #                       noise_clip=n, verbose=False)
    # ret = np.asarray(ret)
    # print(ret)
    # plt.plot(ret)
    # # plt.plot(data)
    # # plt.plot(n)
    # plt.show()
    #
    # print(ret)
    # wav.write(file, rate=fp, data=ret)
    with open(file, 'rb') as f:
        data = f.read()
    return data


def speech2text(speech_data, token, dev_pid=1537):
    FORMAT = 'wav'
    RATE = '16000'
    CHANNEL = 1
    CUID = '*******'
    SPEECH = base64.b64encode(speech_data).decode('utf-8')

    data = {
        'format': FORMAT,
        'rate': RATE,
        'channel': CHANNEL,
        'cuid': CUID,
        'len': len(speech_data),
        'speech': SPEECH,
        'token': token,
        'dev_pid': dev_pid
    }
    url = 'https://vop.baidu.com/server_api'
    headers = {'Content-Type': 'application/json'}
    # r=requests.post(url,data=json.dumps(data),headers=headers)
    # print('正在识别...')
    r = requests.post(url, json=data, headers=headers)
    Result = r.json()
    print(Result)
    if 'result' in Result:
        return Result['result'][0]
    else:
        return ' '


# def openbrowser(text):
#     maps = {
#         '百度': ['百度', 'baidu'],
#         '腾讯': ['腾讯', 'tengxun'],
#         '网易': ['网易', 'wangyi']
#
#     }
#     if text in maps['百度']:
#         webbrowser.open_new_tab('https://www.baidu.com')
#     elif text in maps['腾讯']:
#         webbrowser.open_new_tab('https://www.qq.com')
#     elif text in maps['网易']:
#         webbrowser.open_new_tab('https://www.163.com/')
#     else:
#         webbrowser.open_new_tab('https://www.baidu.com/s?wd=%s' % text)
def get_mean():
    data, fs = sf.read('./tmp/static.wav', dtype='float32')
    d = [abs(i) for i in data]
    return np.average(d)*5

def initiate():
    devpid = 1737  # input('1536：普通话(简单英文),1537:普通话(有标点),1737:英语,1637:粤语,1837:四川话\n')
    print(get_mean())
    my_record(2, get_mean())
    t = time.time()
    denoise.denoiser(FILEPATH)
    TOKEN = getToken(HOST)
    speech = get_audio(FILEPATH)
    result = speech2text(speech, TOKEN, int(devpid))
    print(time.time()-t)
    if type(result) == str:
        return result
    # if type(result) == str:
    #     openbrowser(result.strip('，'))
    # flag = input('Continue?(y/n):')

def waitcall():
    activations = ['iris', 'Irish', 'irish', 'IRS', 'iris']
    reps = ['at your service', 'i am listening', 'may i help you sir', 'what can i do for you']
    engine = pt.engine.Engine()
    while True:
        ret = initiate()
        if ret:
            print(ret)
            for i in activations:
                if i in ret:
                    engine.say('yes sir?')
                    engine.say(random.choice(reps))
                    engine.runAndWait()
                    return True

def recognize_command():
    my_record(4, get_mean()*0.8)
    denoise.denoiser(FILEPATH)
    TOKEN = getToken(HOST)
    speech = get_audio(FILEPATH)
    result = speech2text(speech, TOKEN, int(1737))
    if type(result) == str:
        return result

if __name__ == '__main__':
    sentence = ['']
    activations = ['iris', 'Irish', 'irish', 'IRS']
    engine = pt.engine.Engine()
    while True:
        initiate()
        print(sentence)
        last = sentence[-1]
        last = last.split(' ')
        for i in last:
            if i in activations:
                engine.say('yes sir?')
                engine.runAndWait()
                break
