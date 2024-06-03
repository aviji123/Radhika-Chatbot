import nltk
import wikipedia
from nltk.chat.util import Chat, reflections
from patterns import patterns
import speech_recognition as sr 
import pyttsx3

def voice_in(): 
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        r.pause_threshold = 0.7  
        audio = r.listen(source)   
        try: 
            input1 = r.recognize_google(audio) 
            input = (input1 + "?")
            return input
        except Exception as e: 
            print(e)   
            return "None"



def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def search_wikipedia(query):
    try:
        return wikipedia.summary(query, sentences=1)
    except wikipedia.exceptions.DisambiguationError as e:
        return "Please Say Again"
    except wikipedia.exceptions.PageError as e:
        return "Sorry, I couldn't find any information on that topic."

chatbot = Chat(patterns, reflections)

print("Hey Its Radhika. Type 'quit' to exit.")
while True:
    inp = voice_in()
    print(inp)
    user_input = inp
    response = chatbot.respond(user_input)
    if user_input.lower() == 'quit?':
        break 
    if response:
        print("Radhika:", response)
        speak(response)
    else:
        wiki_response = search_wikipedia(user_input)
        print("Radhika:", wiki_response)
        speak(wiki_response)
    if user_input.lower() == 'quit':
        break 