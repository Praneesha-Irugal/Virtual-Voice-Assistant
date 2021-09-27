import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import time
import pyjokes
import smtplib
from selenium import webdriver




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
print(voices[0].id)
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', 176)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# voice to text.#############################################################
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query


# funtion for wish ###############################################################
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I :%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good Morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"Good evening, its {tt}")
    speak("What can i do for you today?")

###################----Github-------############################################
def gitbb():
    iuse = 'your github username'
    upass = 'your password'

    speak("What is you project name")
    contentz = takecommand().lower()
    speak("okay... creating new project...")
    directory = contentz
    parent_dir = "E:/My Project/" #change the path into your pc path
    # Path
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '% s' created" % directory)
    # Parent Directory path


    drive = webdriver.Chrome(r"E:\IrugalTwo\chromedriver.exe")
    drive.get('https://github.com/login')

    user = drive.find_element_by_id('login_field')
    user.send_keys(iuse)

    pas = drive.find_element_by_id('password')
    pas.send_keys(upass)

    sign = drive.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/div/input[12]')
    sign.submit()

    time.sleep(6)
    new = drive.find_element_by_xpath('/html/body/div[4]/div/aside/div[2]/div[1]/div/h2/a')
    new.click()

    time.sleep(5)
    entern = drive.find_element_by_xpath('/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input')
    entern.send_keys(contentz)

    searchonit = drive.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/div[4]/div[1]/label/input[2]')
    searchonit.click()

    ckcrpo = drive.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button')
    ckcrpo.submit()

    speak("you project is created ")

    speak("opening visual studio code ")
    npath = "add your pc path"
    os.startfile(npath)

    return "none"


###############----send email function----#########################
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login("your email address", "password")
    server.sendmail("your mail", to, content)
    server.close()

##############################---main function that take all commands-----#################
def TaskExecution():
    wish()
    while True:

        query = takecommand().lower()

        ###########################system commanding #####################

        if "open notepad" in query:
            speak(f"If you have a busy schedule, you likely want to make the most out of each day. If there's a lot on your plate, this can feel overwhelming. However, basic organizational skills and time management can help you have a productive daily routine. You can begin the day with a healthy breakfast, a glass of water, and a workout. This will assure you go into work or school energized. Prioritize your tasks based on importance. Give yourself breaks to assure you don't burn out. At home, focus on things like cleaning and planning for the next day. Also, make sure to do something to unwind. Self-care is as important to productivity as work.")
            npath = "add your pc path"
            os.startfile(npath)

        elif "close the notepad" in query or "close notepad" in query:
            speak("Okay, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "new project" in query:
            speak("okay. let's start")
            gitbb().lower()

        elif "i want to complete my notes" in query or "open my note taking app" in query or "i want complete my notes" in query:
            speak("opening notion")
            npath = "add your pc path"
            os.startfile(npath)

        elif "i changed my mind so close it" in query or "i change my mind so close it" in query:
            speak("Okay, closing notion")
            os.system("taskkill /f /im Notion.exe")

        elif "open command prompt" in query:
            speak("Got it, opening command prompt")
            os.system("start cmd")

        elif "close command prompt" in query:
            speak("okay, i will")
            os.system("taskkill /f /im cmd.exe")

        elif "play some music" in query or "i am boring " in query:
            music_dir = "add your pc path"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))


        ###################----online Task----#######################################

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia..........")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open netflix" in query or "open net pic" in query:
            webbrowser.open("www.netflix.com")

        elif "open disney" in query:
            webbrowser.open("www.disneyplus.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open stackoverflow" in query or "open stack overflow " in query:
            webbrowser.open("www.stackoverflow.com")

        elif "search on google" in query or "search google" in query:
            speak("what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        # need to be upgrade
        # elif "send message " or "send massages" or "send a massage" in query:
        #    kit.sendwhatmsg("phone number that you want to send mzg", "sir, this is a test", 16,18)

        elif "play my favourite song in youtube" in query or "play my favourite song in youtube" in query:
            # sgtp =takecommand().lower()
            kit.playonyt("Spirit Here I Am Lyrics")

        elif "i want to send email" in query or "email" in query or "gmail" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                speak("Whom should i send?")
                to = input("Enter email address:")
                sendEmail(to, content)
                speak("email has been sent!")

            except Exception as e:
                print(e)
                speak("i am not able to send this email")

        elif "hello" in query or "hey" in query:
            speak("Hello, may i help you with something?")

        elif "how are you " in query:
            speak("I am fine, what about you?")

        elif "also good" in query or "thanks" in query:
            speak("oh that is great to hear from you")

        elif "thank you" in query or "thanks" in query:
            speak("it's my pleasure!")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takecommand().lower())
            time.sleep(a)
            print(a)

        elif"you can sleep" in query or "sleep now" in query:
            speak("okay, i am going to sleep, you can call me anytime.")
            sys.exit()





if __name__ == '__main__':
    TaskExecution()






