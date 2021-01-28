#!/usr/bin/env python3
# pip3 install sounddevice --user
# pip3 install numpy
# pip3 install scipy

import sounddevice as sd
import numpy as np

fs=44100
duration = 5  # seconds
myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64')
print("Recording Audio")
sd.wait()
print("Audio recording complete , Play Audio")
sd.play(myrecording, fs)
sd.wait()
print(f"Type {type(myrecording)} shape {myrecording.shape}")
print(f"value {myrecording[0]}")

with open('./myrecording', 'wb') as file:
    np.save(file, myrecording)

print("Play Audio Complete")
