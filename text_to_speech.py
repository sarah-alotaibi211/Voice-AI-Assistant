from gtts import gTTS
from playsound import playsound

def text_to_speech(text, output_file="audio_files/response.mp3"):
    tts = gTTS(text=text, lang="en")
    tts.save(output_file)

    print("🔊 Playing response...")
    playsound(output_file)
    