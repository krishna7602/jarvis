import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import chatgpt
import os




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    
    speak("I am Jarvis sir. please tell me how may i help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.......")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except:
        print("say that again please.....")
        return "None"
    return query

        





if __name__ == "__main__":
    speak("Welcome to the World of Artificial intellegence")
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia......')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("according to wikipedia....")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is{strtime}")
            print(strtime)

        elif 'vs code' in query:
              codePath="C:\\Users\\monda\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
              os.startfile(codePath)                           


        elif 'open chrome' in query:
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)

        elif 'lead code' in query:
            webbrowser.open("leetcode.com")