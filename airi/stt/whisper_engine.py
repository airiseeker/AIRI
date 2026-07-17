from faster_whisper import WhisperModel


class WhisperEngine:
    def __init__(
        self,
        model_name="base",
        device="cpu",
        compute_type="int8"
    ):
        self.model = WhisperModel(
            model_name,
            device=device,
            compute_type=compute_type
        )

    def transcribe(self, audio_path: str) -> str:
        segments, _ = self.model.transcribe(
            audio_path,
            language="id"
        )

        return " ".join(segment.text for segment in segments).strip()