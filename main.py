#be sure to install pyaudio before importing speech_recognition as sr

import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, subject, message):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('hotspurs11b@gmail.com', 'GrandmaDatingSantaOnChristmas')
    email = EmailMessage()
    email['From'] = 'hotspurs11b@gmail.com'
    email ['To'] = receiver
    email ['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    #once you finish code above, you will not need code in lines 37-39
    #server.sendmail(
                #'bryanblanco472@gmail.com',
                #'Hi Dude, make sure you come to the party tonight or else i will just talk to santa clause instead'
                #)


email_list = {
    'Stranger 1': 'Hotspurs11b@gmail.com',
    'Stranger 2': 'bryanblanco472@gmail.com',
    'pink': 'jennie@blackpink.com',
    'bts': 'diamond@bts.com'

}



# install pyttsx3 through terminal before starting these codes below
def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    #test email by typing print
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()

    send_email(receiver, subject, message)
    
    #if you want to send more emails, try the code below from lines 67-71
    talk('Hey john, your email is now sent')
    talk('Do you want to send more emails?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()