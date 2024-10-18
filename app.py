import streamlit as st
import main


st.title('Sydney - Your Personal AI Assistant')

st.image(r"C:\Users\swagg\Downloads\sydneyforsid.png", width= 250)

st.info('Sydney is a virtual assistant that can help you with a variety of tasks. You can ask Sydney to open websites, play music, read the news, and more. Sydney is powered by the Generative AI model Gemini 1.5 Flash.')

st.warning('Please note that Sydney is a work in progress and may not be able to handle all requests.')

st.write('click the button below to start Sydney')

st.write("keywords: Sydney, open google, open instagram, open linkedin, open youtube, open spotify, play <song>, news, stop")

if st.button('Start Sydney'):
    st.write("Listening...")

    main.say("Initializing Sydney. . ...")
    while True:

    # listen for the wake word "Sidney"
    # obtain audio from the microphone
        r = main.sr.Recognizer()
        
        print("recognising...") # since it takes time to recognise I put this for UX
       

        # recognize speech using Google cause Sphinx is just not it:(
        try:
            with main.sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)#, timeout = 3, phrase_time_limit=1) 
            word = r.recognize_google(audio)
            # print(word)
            if(word.lower() == "sidney" or word.lower() == "sydney"):
                main.say("yes")
                # listen for my command
                with main.sr.Microphone() as source:
                    print("Sydney Active..")
                    audio = r.listen(source)#, timeout= 3, phrase_time_limit=1)
                    command = r.recognize_google(audio)
                    # print(command)
                    main.processCommand(command)
                    command = r.recognize_google(audio)

        except main.sr.UnknownValueError:
            print("I'm sorry, I could not understand audio")
        except main.sr.RequestError as e:
            print("Sidney error; {0}".format(e))
        except main.sr.WaitTimeoutError as w:
            print(" ")
