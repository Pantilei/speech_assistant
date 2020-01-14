'''
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone(device_index=2) as source:
	print("Say something...")
	audio = r.listen(source)

query = r.recognize_google(audio, language = "ru-Ru")
print("You said: " + query.lower())
'''

import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime


opts = {
    "alias": ('кеша','кеш','инокентий','иннокентий','кишун','киш',
              'кишаня','кяш','кяша','кэш','кэша'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси'),
    "cmds": {
        "ctime": ('текущее время','сейчас времени','который час'),
        "radio": ('включи музыку','воспроизведи радио','включи радио'),
        "stupid1": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты')
    }
}

def speak(what):
	print(what)
	speak_engine.say(what)
	speak_engine.runAndWait()
	speak_engine.stop()

def callback(recognizer, audio):
	try:
		voice = recognizer.recognize_google(audio,lang="ru-Ru").lower()
		print("[log] Распознано: " + voice )

        if voice.startswith(opts["alias"]):
            # обращаются к Кеше
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
            
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
            
            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])


	except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")

def recognize_cmd(cmd):
	RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
   
    return RC

def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
   
    elif cmd == 'radio':
        # воспроизвести радио
        os.system("E:\\Music\\CHELENTANO\\3db81fc4dd11c0.mp3")
   
    elif cmd == 'stupid1':
        # рассказать анекдот
        speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")
   
    else:
        print('Команда не распознана, повторите!')


r = sr.Recognizer()
m = sr.Microphone(device_index = 2)

with m as source:
	r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[4].id)

# forced cmd test
#speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")
 
speak("Добрый день, повелитель")
speak("Кеша слушает")
 
stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1) # infinity loop