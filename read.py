import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import sounddevice as sd
import noisereduce as nr

# fs, data = wav.read('temp.wav')
# plt.plot(data)
# plt.show()
# sd.play(data, fs)
# sd.wait()

fp, data = wav.read('./tmp/temp.wav')
t, n = wav.read('./tmp/static.wav')
ret = nr.reduce_noise(audio_clip=data, noise_clip=n, verbose=True)
print(ret)
ret = np.array(ret)
print(ret)
wav.write('./tmp/denoised.wav', rate=fp, data=ret)