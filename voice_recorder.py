import sounddevice as sd
import soundfile as sf

def record_audio(filename="audio_files/input.wav", duration=5, samplerate=16000):
    print("🎤 Speak now...")

    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="int16",
        device=1   # استخدم المايك رقم 1
    )

    sd.wait()

    sf.write(filename, recording, samplerate)

    print("✅ Recording finished.")
    