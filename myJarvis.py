import speech_recognition as sr
import pyttsx3
import os, sys
import wolframalpha
import wikipedia
import random
import webbrowser
import datetime
# for sending email with html formating
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sayIt(audio):
    t = pyttsx3.init()
    voices = t.getProperty('voices')
    t.setProperty('voice', voices[len(voices)-3].id)
    t.say(audio)
    t.runAndWait()

def command():
    r = sr.Recognizer()
    print('Say your command!: ')
    with sr.Microphone(device_index = 2) as source:
        r.pause_threshhold = 3
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language = 'en-En')
        print('Your command: ' + query)
        cond = False
    except sr.UnknownValueError:
        print('I could not understand you, please write the command: ')
        sayIt('I could not understand you, please write the command: ')
        query = str(input('Your command: '))
    return query

def welcome():
    now = int(datetime.datetime.now().hour)
    if now >= 22 or now < 5:
        dayTime = 'Good night '
    elif now > 5 and now <= 11:
        dayTime = 'Good Morning '
    elif now > 11 and now <= 16:
        dayTime = 'Good Day '
    elif now > 16 and now < 22:
        dayTime = 'Good Evening '
    return dayTime

if __name__ == '__main__':
    now = welcome()
    sayIt(now + 'mr. Ianulov!')
    sayIt('Say your command!:')
    while True:
        audio = command()
        query = audio.lower()
        if 'bye' in query or 'see you later' in query:
            sayIt('See you later mr. Boss!')
            sys.exit()
        elif 'hello' in query:
            sayIt('Hello mr. Ianulov!')
        elif 'play' and 'music' in query:
            print('Here is your music: ')
            music = ['0d926aacfbff', "2fecc9345056", "5c115c2562ad", "44cc414cca91" ]
            musicPath = "E:\\Music\\Altenosfera\\"
            fullPath = musicPath + random.choice(music) +'.mp3'
            os.system(fullPath)
        elif 'open' and 'youtube' in query:
            sayIt('Gladly!')
            webbrowser.open("www.youtube.com")
        elif 'open' and 'gmail' in query:
            sayIt('Gladly!')
            webbrowser.open("www.gmail.com")
        elif 'how are you' in query or "what's up" in query or "are you ok" in query:
            answers = ['I am doing fine, thank you mr. Ianulov', 'Just fine,  mr. Ianulov', 'Nothing special,  mr. Ianulov', 'Doing my stuff,  mr. Ianulov']
            sayIt(random.choice(answers))
        elif 'email' in query or 'mail' in query:
            smtp_server = "smtp.gmail.com"
            port = 465
            sender = "pan.comrat@gmail.com"
            password = "Greedisgood"

            sayIt('Who is receiver?')
            print('Who is receiver?')
            rec = command().lower()
            if 'me' in rec:
                receiver = 'ianulov.pantilei@mail.ru'
            elif 'father' in rec:
                receiver = 'ianulov.pantilei@gmail.com'

            sayIt('What shoud I say?')
            print('What shoud I say?')
            t = command()

            sayIt('Subject of email?')
            print('Subject?')
            subject = command()

            message = MIMEMultipart("alternative")
            message["Subject"] = subject.capitalize()
            message["From"] = sender
            message["To"] = receiver
# Create the plain-text and HTML version of your message
            text = t
            html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="https://realpython.com/python-send-email/">See Email sending tutorial</a><br>
       <strong>{}</strong><br>
       <img src="https://media.proglib.io/wp-uploads/2018/09/ciwlCWa.png" alt="img">
    </p>
  </body>
</html>
""".format(t)
            # Turn these into plain/html MIMEText objects
            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
            message.attach(part1)
            message.attach(part2)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
                server.login(sender, password)
                server.sendmail(sender, receiver, message.as_string())

        else:
            try:
                try:
                    client = wolframalpha.Client('UWTRKV-PVW9XARRRY')
                    res = client.query(query)
                    ans = next(res.results).text
                    print('According to WolframAlpha: ' + ans)
                    sayIt('According to WolframAlpha: ' + ans)
                except:
                    res = wikipedia.summary(query, sentences = 2)
                    print('According to Wikipedia: ' + res)
                    sayIt('According to Wikipedia: ' + res)
            except:
                webbrowser.open('www.google.com')
        print('\n')
        sayIt('Do you have other request, mr. Ianulov?')
