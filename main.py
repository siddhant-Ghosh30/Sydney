# since this is a mega project, I'll install alot of packages
# and since it's a mega project, I'll install them in a virtual environment

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai
import sys 
import keys # this will store my API keys


recognizer = sr.Recognizer()
engine = pyttsx3.init()

 # API key from newsapi.org get your own 

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #Female voice for Sydney cause uk

def say(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command): # from client.py

    # Directly configure the API key for this project (Gemini)
    # from google AI Studio

    # Configure the API key for the Generative AI model
    genai.configure(api_key=keys.api_key_gemini)

    # Initialize the model with the API key specifically for this instance
    model = genai.GenerativeModel('gemini-1.5-flash')

    # system_role = "You are a female virtual assistant named Sidney skilled in general tasks like Alexa and Google Cloud."
    # # user_role = command 
    # response = model.generate_content(f"{system_role}. {command} ") # prompt engineering at it's finest fr bhai
    # return (response.text)

    response = model.generate_content(command)
    return (response.text) 


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/in/siddhantghosh/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open spotify" in c.lower():
        webbrowser.open("https://open.spotify.com/?nd=1&flow_ctx=c3ced48b-a253-4651-ba4e-3c284c13d2c2%3A1722993184")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={keys.newsapi}")

        if r.status_code == 200:
            # parse the JSON response
            data = r.json()
            # extract the articles
            articles = data.get('articles', [])

            # announce the headlines
            for article in articles:
                say(article['title'])
    
    elif "stop" in c.lower():
        a = sys.exit()

    else:
        # Imma let Gemini handle the request
        output = aiProcess(c)
        say(output)
    

    
    

if __name__ == "__main__":
    say("Initializing Sydney. . ...")
    while True:

    # listen for the wake word "Sidney"
    # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognising...") # since it takes time to recognise I put this for UX
       

        # recognize speech using Google cause Sphinx is just not it:(
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)#, timeout = 3, phrase_time_limit=1) 
            word = r.recognize_google(audio)
            # print(word)
            if(word.lower() == "sidney" or word.lower() == "sydney"):
                say("yes")
                # listen for my command
                with sr.Microphone() as source:
                    print("Sydney Active..")
                    audio = r.listen(source)#, timeout= 3, phrase_time_limit=1)
                    command = r.recognize_google(audio)
                    # print(command)
                    processCommand(command)
                    command = r.recognize_google(audio)

        except sr.UnknownValueError:
            print("I'm sorry, I could not understand audio")
        except sr.RequestError as e:
            print("Sidney error; {0}".format(e))
        except sr.WaitTimeoutError as w:
            print(" ")
        
        