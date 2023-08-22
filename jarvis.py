import pyttsx3
import datetime
import speech_recognition as sr

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Sorry, I encountered an error while trying to process your request:", e)
        return ""

if __name__ == "__main__":
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    wishMe()
    speak("Sir, I am Jarvis. Please tell me how may I help you.")
    
    while True:
        query = takeCommand()
        
        if "hello" in query:
            speak("Hello! How can I assist you?")
        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
        elif "goodbye" in query:
            speak("Goodbye! Have a great day.")
            break
        
        # Add more conditions to handle other user queries
        
        else:
            speak("I'm sorry, I don't understand that command.")

