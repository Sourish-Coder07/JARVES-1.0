import pyttsx3
from user_config import voice_id, speech_rate

engine = pyttsx3.init()

# Apply user settings from user_config
voices = engine.getProperty('voices')
try:
    engine.setProperty('voice', voices[voice_id].id)
except IndexError:
    print("⚠️ Invalid voice ID in user_config. Using default voice.")
engine.setProperty("rate", speech_rate)

def speak(text):
    print(f"JARVES: {text}")
    engine.say(text)
    engine.runAndWait()
