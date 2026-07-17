from pathlib import Path

from .recorder import Recorder
from .whisper_engine import WhisperEngine


class Listener:
    def __init__(
        self,
        duration: int = 5,
        model_name: str = "base",
        device: str = "cpu",
        compute_type: str = "int8",
    ):
        self.recorder = Recorder(duration=duration)

        self.whisper = WhisperEngine(
            model_name=model_name,
            device=device,
            compute_type=compute_type,
        )

        self.audio_path = Path("data/audio/input.wav")

    def listen(self) -> str:
        audio = self.recorder.record(self.audio_path)

        text = self.whisper.transcribe(audio)

        return text