from core.voice_recorder import record_audio
from core.speech_to_text import speech_to_text
from core.chatbot import ask_chatbot
from core.text_to_speech import text_to_speech
import os

# إنشاء المجلد إذا لم يكن موجودًا
os.makedirs("audio_files", exist_ok=True)

# 1- تسجيل الصوت
record_audio()

# 2- تحويل الصوت إلى نص
user_text = speech_to_text("audio_files/input.wav")
print(f"\n🎤 You: {user_text}")
print(repr(user_text))
# 3- إرسال النص إلى Cohere
response = ask_chatbot(user_text)
print(f"\n🤖 Assistant: {response}")

# 4- تحويل الرد إلى صوت
text_to_speech(response)

print("\n✅ Voice response saved as: audio_files/response.mp3")

