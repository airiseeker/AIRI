import sounddevice as sd
import soundfile as sf
from pathlib import Path


class Recorder:
    def __init__(self,
                 sample_rate=16000,
                 channels=1,
                 duration=5):

        self.sample_rate = sample_rate
        self.channels = channels
        self.duration = duration

    def record(self, output_path):

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        print("🎙️ AIRI sedang mendengarkan...")

        audio = sd.rec(
            int(self.duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="float32"
        )

        sd.wait()

        sf.write(output_path, audio, self.sample_rate)

        print("✅ Rekaman selesai.")

        return output_path