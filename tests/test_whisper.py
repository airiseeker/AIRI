from faster_whisper import WhisperModel

print("🌸 Loading model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("✅ Model loaded.")

segments, info = model.transcribe(
    "data/audio/input.wav",
    language="id"
)

print("\n===== HASIL =====")

for segment in segments:
    print(segment.text)