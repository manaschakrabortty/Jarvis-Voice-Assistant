import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init() 


def Speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key="sk-proj-y8JNgNcf6w9906qKJ77IT3BlbkFJBu8f5A0rCDclxHKJkE1t",)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def  processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open amajon" in c.lower():
        webbrowser.open("https://amajon.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link= musicLibrary.music[song]
        webbrowser.open(link)
    else:
        output= aiProcess(c)
        Speak(output)
    
if __name__ =="__main__":
    Speak("Initializing Jarvish..")
    while True:
        r = sr.Recognizer()
        
        
        print("rechogning...")
        try:
            with sr.Microphone() as source:
                print("listiening..")
                audio = r.listen(source, timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower()  == "jarvis"):
                Speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis active..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))














