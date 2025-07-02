import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import smtplib
import mtranslate

# Initialize TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 for male, 1 for female
engine.setProperty("rate", 170)

def speak(text):
    print(f"[AI] {text}")
    engine.say(text)
    engine.runAndWait()

def command():
    content = ""
    while content.strip() == "":
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            content = recognizer.recognize_google(audio, language='en-in')
            content = mtranslate.translate(content, to_language="en")
            print("You said:", content)
        except:
            print("Could not understand. Try again.")
    return content

def main_process():
    wikipedia.set_lang("en")
    
    while True:
        request = command().lower()

        if "hello" in request:
            speak("Welcome, how can I help you.")

        elif "play music" in request:
            speak("Playing music")
            songs = [
                "https://www.youtube.com/watch?v=yJg-Y5byMMw",
                "https://www.youtube.com/watch?v=TW9d8vYrVFQ",
                "https://www.youtube.com/watch?v=U6cPjurCOmQ"
            ]
            webbrowser.open(random.choice(songs))

        elif "say time" in request:
            now = datetime.datetime.now().strftime("%H:%M")
            speak("The current time is " + now)

        elif "say date" in request:
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            speak("Today's date is " + date)

        elif "new task" in request:
            task = request.replace("new task", "").strip()
            if task:
                speak("Adding task: " + task)
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")

        elif "speak task" in request:
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.read()
                speak("Tasks for today: " + tasks)
            except FileNotFoundError:
                speak("No tasks found.")

        elif "show work" in request:
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.read()
                notification.notify(title="Today's Work", message=tasks)
            except FileNotFoundError:
                speak("No tasks to show.")

        elif "open youtube" in request:
            webbrowser.open("https://www.youtube.com")

        elif "open" in request:
            query = request.replace("open", "").strip()
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif "wikipedia" in request:
            query = request.replace("wikipedia", "").strip()
            try:
                result = wikipedia.summary(query, sentences=2)
                speak(result)
            except wikipedia.exceptions.DisambiguationError:
                speak("That topic is too broad. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("No matching Wikipedia page found.")
            except Exception:
                speak("Something went wrong while searching Wikipedia.")

        elif "search google" in request:
            query = request.replace("search google", "").strip()
            webbrowser.open("https://www.google.com/search?q=" + query)

        elif "send whatsapp" in request:
            try:
                # Update with your number and message
                pwk.sendwhatmsg("+910123456789", "Hi, how are you", 2, 10, 30)
                speak("WhatsApp message scheduled.")
            except:
                speak("Could not send WhatsApp message.")

        elif "send email" in request:
            try:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("your_email@gmail.com", "your_app_password")
                message = "This is the message.\n\nThanks by JARVES."
                s.sendmail("your_email@gmail.com", "receiver_email@gmail.com", message)
                s.quit()
                speak("Email sent.")
            except:
                speak("Failed to send email.")

        elif "clear chat" in request:
            speak("Memory cleared. But I don't store anything yet.")

        else:
            speak("Sorry, I can't understand this command yet.")

if __name__ == "__main__":
    main_process()
