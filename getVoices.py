'''
import pyttsx3

engine = pyttsx3.init()
print(engine)
print(type(engine))
voices = engine.getProperty('voices')
print(voices)
print(type(voices))
'''
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice',voice.id)
    engine.say('Hello World!')
    engine.runAndWait()
