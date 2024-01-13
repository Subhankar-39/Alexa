import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests

def talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            command = r.recognize_google(audio, language='en-in')
            print(f"You said: {command}\n")
        except Exception as e:
            print(e)
            print("Please say the command again.")
            return "None"
        return command.lower()

def play_music(song):
    talk('playing ' + song)
    pywhatkit.playonyt(song)

def get_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk('Current time is ' + time)

def get_info(person):
    try:
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    except:
        talk("Sorry, I could not find any information on that person.")

def tell_joke():
    talk(pyjokes.get_joke())

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        play_music(song)
    elif 'time' in command:
        get_time()
    elif 'who is' in command:
        person = command.replace('who is', '')
        get_info(person)
    elif 'date' in command:
        talk('Sorry, I cannot do that right now.')
    elif 'are you single' in command:
        talk('I am in a relationship with Wifi.')
    elif 'joke' in command:
        tell_joke()
    elif 'end' in command:
        talk('Goodbye!')
        exit()
    elif 'what is your name' in command:
        talk('I am Alexa')
    else:
        talk('Please say the command again.')

if __name__ == "__main__":
    talk("Hi, I'm Alexa. How can I help you today?")
    while True:
        run_alexa()
