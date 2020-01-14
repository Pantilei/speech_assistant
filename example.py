import wolframalpha
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
print(type(engine))
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[len(voices)-1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 2) as source:
        print('Listening...')
        r.pause_threshhold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language = 'en-En')
        print('Command: '+ query + '\n')
    except sr.UnknownValueError:
        speak("Sorry, I could not understand you, please type the command")
        print("Command: ")
    return query
query = command()

client = wolframalpha.Client('UWTRKV-PVW9XARRRY')

res = client.query(query)
print(query)
speak(query)
result = next(res.results).text
print(next(res.results).text)
speak(next(res.results).text)
