import smtplib, ssl

smtp_server = 'smtp.gmail.com'
port = 465
sender = "pan.comrat@gmail.com"
password = 'Greedisgood'

receiver = "ianulov.pantilei@mail.ru"
message = """\
From: {}
To: {}
Subject: Hi there!

This message was send by python
""".format(sender, receiver)

context = ssl.create_default_context()
# encrypted connection from the starttls

with smtplib.SMTP_SSL(smtp_server, port, context = context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)

'''
#port = 587
try:
    #here we create server object
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    # here we create encrypted connection
    server.starttls(context=context)
    server.ehlo()
    # now, when the connection is encrypted we can login
    server.login(sender, password)
    # and check is connection is established
    print('It worked')
except Exception as e:
    print(e)
'''
