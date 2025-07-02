import speech_recognition as sr
import mtranslate

def get_command():
    content = ""
    while content.strip() == "":
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎙 Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            content = recognizer.recognize_google(audio, language='en-in')
            content = mtranslate.translate(content, to_language="en")
            print("🗣 You Said:", content)
        except sr.UnknownValueError:
            print("😕 Couldn't understand audio. Please try again.")
        except sr.RequestError:
            print("❌ Google Speech Recognition not available.")
        except Exception as e:
            print(f"⚠️ Unknown error: {e}")

    return content
