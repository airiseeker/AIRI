import os
import sys

print(os.getcwd())
print(sys.path)

from airi.stt.recorder import Recorder

recorder = Recorder(duration=5)

audio_path = recorder.record("data/audio/input.wav")

print(audio_path)