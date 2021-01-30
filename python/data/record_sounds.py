#!/usr/bin/env python3
# pip3 install sounddevice --user
# pip3 install numpy
# pip3 install scipy

# Uses http://www.portaudio.com/ which is a
# portable c library for audio recording
# PortAudio provides samples in raw PCM format. That means each sample is an amplitude to be given to the DAC (digital-to-analog converter) in your sound card.
# For paFloat32, this is a floating-point value from -1.0 to 1.0
# The sound card converts this values to a proportional voltage that then drives your audio equipment

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
