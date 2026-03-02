from TTS.api import TTS

tts = TTS(model_name="tts_models/en/vctk/vits")

tts.tts_to_file(
    text=open("data/script.txt").read(),
    file_path="assets/audio/narration.wav"
)

print("✅ Voiceover generated")
