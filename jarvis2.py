import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os, sys

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

client = wolframalpha.Client('UWTRKV-PVW9XARRRY')

def speak(audio):
    print('Computer: '+ audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')
    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')
    if currentH >= 18 and currentH < 0:
        speak('Good Evening!')

greetMe()
speak(' Hello Mr. Pantilei, I am your assistant!')
speak('How can I help you?')

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 2) as source:
        print('Listening...')
        r.pause_threshhold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-En')
        print('User: '+ query + '\n')
    except sr.UnknownValueError:
        speak('Sorry, I couldn\'t understand you! Can you type the command?')
        query = str(input('Command: '))
    return query

if __name__ == '__main__':
    while True:

        query = myCommand()
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
        elif 'open google' in query:
            speak('okey')
            webbrowser.open('www.google.com')
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing', 'I am fine', 'Nice', 'I am good, and feel full of energy']
            speak(random.choice(stMsgs))
        elif 'email' in query:
            speak('Who is the recipient')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("ianulov.pantilei@gmail.com", 'Panian007')
                    server.sendmail('ianulov.pantilei@gmail.com', "ianulov.pantilei@mail.ru", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye mr. Ianulov, have a good day.')
            sys.exit()
        elif 'play music' in query:
            music_folder ="E://Music//"
            music = ["0fb6f0d460bd", "Leps_Grigorij_Angel_zavtrashnego_dnya","MilieGlazaa"]
            random_music = music_folder + random.choice(music)+'.mp3'
            os.system(random_music)
            speak('Okay, here is your music! Enjoy!')


        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Mr. Ianulov!')
