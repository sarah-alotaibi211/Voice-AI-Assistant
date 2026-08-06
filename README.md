# Voice-AI-Assistant
A Python voice assistant that converts speech to text, generates AI responses using Cohere, and converts the response back to speech.




## Overview
Voice AI Assistant is a Python application that records the user's voice, converts it into text, generates an AI response using Cohere, and converts the response back into speech.

## Features
- Record voice from the microphone.
- Convert speech to text.
- Generate AI responses using Cohere.
- Convert text responses to speech.
- Play the generated audio response.

## Technologies Used
- Python
- Cohere API
- SpeechRecognition
- Whisper
- gTTS
- playsound
- python-dotenv

## Project Structure
Voice-AI-Assistant/
│
├── audio_files/
│   ├── input.wav
│   └── response.mp3
│
├── core/
│   ├── chatbot.py
│   ├── speech_to_text.py
│   ├── text_to_speech.py
│   └── voice_recorder.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

## Installation


1. Install the required libraries.
pip install -r requirements.txt

2. Create a .env file and add your Cohere API key.
COHERE_API_KEY=your_api_key_here

3. Run the project.
python main.py

## How It Works

1. Record the user's voice.
2. Convert speech to text.
3. Send the text to Cohere.
4. Receive the AI response.
5. Convert the response to speech.
6. Play the generated audio.

## Screenshots

### Voice Recording
(Add a screenshot here)

### Speech to Text
(Add a screenshot here)

### AI Response
(Add a screenshot here)

### Text to Speech
(Add a screenshot here)

## Author

Sarah Saud Alotaibi
