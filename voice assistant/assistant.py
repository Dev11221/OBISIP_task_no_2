import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def talk(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = recognizer.listen(source)
            command = recognizer.recognize_google(voice)
            command = command.lower()
            print("You said:", command)
            return command
    except:
        talk("Sorry, I didn't catch that.")
        return ""

def run_assistant():
    command = listen()

    if "hello" in command or "hi" in command:
        talk("Hello! How can I help you?")
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {time}")
    elif "date" in command:
        date = datetime.datetime.now().strftime('%A, %B %d, %Y')
        talk(f"Today is {date}")
    elif "search" in command:
        query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        talk(f"Searching for {query}")
        webbrowser.open(url)
    elif "open youtube" in command:
        search_term = command.replace("open youtube", "").strip()
        talk(f"searching for {search_term} on YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query= {search_term} ")  
    else:
        talk("Sorry, I didn't understand that.")
run_assistant()        

