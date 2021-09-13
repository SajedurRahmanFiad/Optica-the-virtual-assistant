import datetime
import pytz
import pyttsx3
import speech_recognition as sr
import os
import requests
from googletrans import Translator
import random
import pyjokes
import wikipedia
from countryinfo import CountryInfo
import smtplib
import webbrowser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from tkinter import filedialog
from tkinter import *
import cv2
import freegames
import serial.tools.list_ports
import pyfirmata
import socket
import pywhatkit




###############################################      Variables and initializations     ##########################################################

os.system("title Artificial Intelligence")
trans = Translator()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 130)
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
            # For other voices :
            #       HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0
            #       HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
engine.setProperty('voice', voice_id)

city = requests.get('https://ipinfo.io/').json()['city']
IST = pytz.timezone('Asia/'+city)
greetings = ["Hi sir", "Hi", "Hello", "Hello Sir", "Hola?", "I am here sir?", "Yes sir?", "How can I help you sir?", "How may I help you sir?"]
endings = ["bye, take care", "Bye Sir, have a good day", "Ok, Bye, take care", "Bye, have a good day"]
thanking = ["Thanks", "Thank You", "Thanks you sir", "Thanks a lot", "Thanks you so much"]
welcome = ["Welcome sir", "you are most welcome", "my pleasure", "Sounds good"]
I_am_fine = ["I am fine, what about you?", "I am well, what about you?", "I am good, what about you?", "I am well, thanks", "I am fine, thanks", "I am good, thanks"]

Countries = [
    'united states', 'afghanistan', 'albania', 'algeria', 'american Samoa','andorra','angola','anguilla','antarctica', 'antigua', 'argentina', 'armenia', 'aruba', 'australia', 'austria', 'azerbaijan', 'bahamas', 'bahrain',
    'bangladesh', 'barbados','belarus','belgium','belize','benin','bermuda','bhutan','bolivia','bosnia','botswana','bouvet','brazil','brunei','bulgaria','burkina faso', 'burundi','cambodia','cameroon','canada','capeverde','cayman',
    'central african republic','chad','chile','china','christmas islands','cocos islands','colombia','comoros','congo','cook islands','costa rica','cote d`ivoire','croatia','cuba','cyprus','czech republic','denmark','djibouti','dominica',
    'dominican republic','east timor','ecuador','egypt','el salvador','equatorial guinea','eritrea','estonia','ethiopia','falkland islands','malvinas','faroe islands','fiji','finland','france','french guiana','french polynesia',
    'french s territories','gabon','gambia','georgia','germany','ghana','gibraltar','greece','greenland','grenada','guadeloupe','guam','guatemala','guinea','guinea bissau','guyana','haiti','honduras','hong kong','hungary','iceland',
    'india','indonesia','iran','iraq','ireland','israel','italy','jamaica','japan','jordan','kazakhstan','kenya','kiribati','north korea','south korea','kuwait','kyrgyzstan','laos','latvia','lebanon','lesotho','liberia','libya',
    'liechtenstein','lithuania','luxembourg','macau','macedonia','madagascar','malawi','malaysia','maldives','mali','malta','marshall islands','martinique','mauritania','mauritius','mayotte','mexico','micronesia','moldova','monaco',
    'mongolia','montserrat','morocco','mozambique','myanmar','namibia','nauru','nepal','netherlands','netherlands antilles','new caledonia','new zealand','nicaragua','niger','nigeria','niue','norfolk islands','northern mariana islands',
    'norway','oman', 'pakistan','palau','panama','papua new guinea','paraguay','peru','philippines','pitcairn','poland','portugal','puerto rico','qatar','reunion','romania','russia','rwanda','saint kitts and nevis','saint lucia',
    'st vincent', 'grenadines','samoa','san marino', 'sao tome','saudi arabia','senegal','seychelles','sierra leone','singapore','slovakia','slovenia','solomon islands','somalia','south africa','spain','sri lanka','st helena','st pierre',
    'sudan','suriname','swaziland','sweden','switzerland','syrian arab republic','syria','taiwan','tajikistan','tanzania','thailand','togo','tokelau','tonga','trinidad','Tobago','tunisia','turkey','turkmenistan','tuvalu','Uganda','Ukraine',
    'united arab emirates','united kingdom','uk','us','uruguay','uzbekistan','Vanuatu','vatican city','venezuela','vietnam','virgin islands','western sahara','yemen','yugoslavia','zaire','zambia','zimbabwe']

ordinal_numbers = ['', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth',
    'twentieth', 'twenty first', 'twenty second', 'twenty third', 'twenty fourth', 'twenty fifth', 'twenty sixth', 'twenty seventh', 'twenty eighth', 'twenty ninth', 'thirtieth', 'thirty first', 'thirty second']

hardwareFound, board, lightOn = True, "", False

days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#################################################################################################################################################################################################################################################




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
def strip_brackets(string):
    string = "" + str(string)
    d = 0
    k = 0
    out = ''
    for i in string:
        if d < 1:
            if i == '>':
                k-=1
            if i =="<":
                k +=  1
        if k < 1:
            if i == '(':
                    d += 1
            if d > 0:
                    out += ' '
            else:
                    out += i
            if i == ')' :
                    d -= 1
        else:
            out +=i
    return out


def wishMe():
    speak("Us salaamu Alai coom ")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    elif hour>=18 and hour<0:
        speak('Good Evening')

        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Callibrating...")
        r.adjust_for_ambient_noise(source, duration=1)
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('         Recognizing...')
        query = r.recognize_google(audio, language='en')
        print(f"                   You: {query}\n")
        print("                         ")
    except Exception as e:
        return "None"
    return query


def OpenFile(caption):
        Tk().withdraw()
        filename = filedialog.askopenfilename(initialdir = "/",title = caption,filetypes = (("Images",".jpg .jpeg .png"),("all files","*.*")))
        return filename

    
def SendMail():
        print("[INFO] Getting things ready...\n")
        time.sleep(1)
        speak("Please enter your email address")
        sender_address = input("Sender : ")
        speak("Enter your password")
        sender_pass = input("Password : ")
        speak("Enter Receiver's email address")
        receiver_address = input("Receiver : ")
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        speak("enter the subject of the mail?")
        message['Subject'] = input("\nSubject :  ")
        speak("enter the content of the mail?")
        mail_content = input("Content :  ")
        message.attach(MIMEText(mail_content, 'plain'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        print("\n[INFO] Sending...\n")
        session.starttls()
        try:
            session.login(sender_address, sender_pass)
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            speak("Congratulations! the Mail sent succesfully")
            print('\n[INFO] Successfully sent the mail\n\n')
        except:
            print("\n[INFO] Failed to send email\n")
            webbrowser.open('https://myaccount.google.com/lesssecureapps', new=1)
            speak("Sorry, failed to send the mail. Maybe turning on Allowing less secure apps will work")

            
def pronounce():
    word = input("I'll pronounce this - ")
    speak("Enter the word or sentence here")
    speak(word)
    
    
def toBangla(word):
    translated = trans.translate(word, dest='bn')
    return str(translated.text)


def toEnglsh(word):
    try:
        translated = trans.translate(word, dest='en')
    except:
        return word
    return str(translated.text)


def initialize_hardware():
    global board
    global hardwareFound
    
    print("[INFO] Initializing...")
    time.sleep(1)
    try:
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if "Arduino" in p.description:
                port = list(p)[0]

        board = pyfirmata.Arduino(port)
        print("[INFO] Communication Successfully established...\n\n")
        hardwareFound = True
    except:
        print("[INFO] Failed to communicate...(Not a problem at all)\n\n")
        hardwareFound = False


def write(pin, state):
    board.digital[pin].write(state)


def connected():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

    
def main():
   global lightOn

   wishMe()
   while True:
       
        if connected():
            pass
        else:
            os.system('cls')
            print("\nOops! You are disconnected. Try connecting to the internet\n")
            os.system('pause')
            quit()

            
        hour = int(datetime.datetime.now(IST).strftime('%H')) % 12
        minute = int(datetime.datetime.now(IST).strftime('%M'))
        query = takeCommand().lower()



        ##  Hardware part  #######################
        
        if ('light' in query or 'led' in query) and 'on' in query:  # If asked to turn the ight on
            if hardwareFound == True:  # If arduino is connected
                if lightOn != True: # If the light is turned off
                    speak('Turning the light on')
                    write(13, 1)
                    lightOn = True

                else:  # If the light is turned on
                    speak("Hey! the light is already turned on")
                    
            else:  # If arduino isn't connected
                speak(random.choice(["Sorry, You don't have an arduino connected", "Please try connecting the arduino first"]))


        elif ('light' in query or 'led' in query) and ('off' in query or 'of' in query):  # If asked to turn the light off
            if hardwareFound:  # If arduino is connected
                if lightOn: # If the light is turned on
                    speak('Turning the light off')
                    write(13, 0)
                    lightOn = False

                else:  # If the light is turned off
                    speak("Hey! the light is already turned off")
                    
            else:  # If arduino isn't connected
                speak(random.choice(["Sorry, You don't have an arduino connected", "Please try connecting the arduino first"]))

        ##  Hardware part ends here  ############



        elif 'open' in query:
            what_to_open = query.replace('open ', '').strip().upper()

            
            #########################################        Opening softwares and files        ########################################
            if what_to_open.find('BROWSER') != -1 or what_to_open.find('GOOGLE') != -1 or what_to_open.find('CHROME') != -1:
                try:
                    os.startfile('C:\\Program Files\Google\Chrome\Application\chrome.exe')
                    speak("Sure, here is Google Chrome")
                except FileNotFoundError:
                    speak("Sorry, I can't navigate google chrome or it doesn't exist in your computer")

            elif what_to_open.find('NOTE') != -1 or what_to_open.find('NOTES') != -1 or what_to_open.find('NOTEPAD') != -1:
                try:
                    os.system('notepad')
                    speak("Sure, here is your notepad")
                except FileNotFoundError:
                    speak("Sorry, I can't navigate that")

            elif 'CALCULATOR' in what_to_open:
                try:
                    os.system('calc')
                    speak("Sure, here is your calculator")
                except FileNotFoundError:
                    speak("Sorry, I can't navigate that")

            elif 'YOUTUBE' in what_to_open:
                speak("Opening youtube")
                webbrowser.open('https://youtube.com', new=1)
            
            else:
                speak("I'm not sure I understand or I don't know what it is.")
            ############################################################################################################################


        elif 'draw' in query:
            speak("What should I draw? Select an image")
            img = OpenFile("Select an image")
            FileName, extension = os.path.splitext(img)
            print("[INFO] Drawing...")
            grey_img = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY)
            invert = cv2.bitwise_not(grey_img)
            blur = cv2.GaussianBlur(invert, (21, 21), 0)
            inverted_blur = cv2.bitwise_not(blur)
            final = cv2.divide(grey_img, inverted_blur, scale=256.0)
            cv2.imwrite((os.path.join(os.environ['USERPROFILE'], 'Desktop') + "\My Sketch.png"), final)
            time.sleep(3)
            speak("Done. I have saved my sketch to your Desktop")


        elif 'you' in query and ('good' in query or 'awesome' in query or 'cool' in query or 'great' in query):
            speak(random.choice(thanking) + ". Please leave a feedback about me.")
            os.startfile("Feedback.exe")
            os.system('pause')


        elif 'time' in query:
            if minute == 0:
                speak("It's " + str(hour) + " o clock")

            elif minute == 5:
                speak("It's quarter past " + str(hour))

            elif minute == 30:
                speak("It's half past " + str(hour))

            elif minute == 35:
                speak("It's 25 to " + str(hour+1))

            elif minute == 45:
                speak("It's quarter to " + str(hour+1))

            elif minute == 55:
                speak("It's 5 to " + str(hour+1))

            else:
                speak("It's " + str(hour) + " hours and " + str(minute) + " minutes")


        elif 'date' in query and 'today' in query:
            date = int(datetime.datetime.now().day)
            month = int(datetime.datetime.now().month)
            year = int(datetime.datetime.now().year)
            speak("It's " + ordinal_numbers[date] + " " + months[month] + " " + str(year))


        elif ' day ' in query and 'today' in query:
            speak("Today is " + str(datetime.datetime.today().strftime("%A")))

            
        elif 'translate' in query or 'meaning' in query:
            speak("Enter the word or sentence here")
            word = input("The word is ")
            speak("It's pronounciation is " + word.strip())
            print("[MEANING] " + word+ "  =>  "+ toBangla(word.lower())+ "\n")

            
        elif "introduce" in query or "who are you" in query:
            speak("I am Optica, your virtual assistant. That's all I know about myself.")

            
        elif "pronounce" in query:
            pronounce()

            
        elif 'mail' in query:
            SendMail()

            
        elif 'ip address' in query:
            speak("Here is your ip address")
            os.system('ipconfig')

            
        elif query.find('hello') != -1 or query.find('hi ') != -1 or query.find('hai ') != -1 or query.find('hey') != -1 or query.find('hay') != -1:
            speak(random.choice(greetings))

            
        elif 'how' in query and 'you' in query:
            speak(random.choice(I_am_fine))

            
        elif "what's up" in query:
            speak("Alright, what about you?")

                
        elif query.find('name') != -1 and query.find('my') == -1:
            speak("My name is optica")


        elif query.find('thanks') != -1:
            speak(random.choice(welcome))

            
        elif query.find('welcome') != -1:
            speak("That's alright")

            
        elif 'thank' in query:
            speak(random.choice(welcome))

            
        elif query.find('shutdown') != -1:
            speak("Shutting down your pc")
            os.system("shutdown /s /t 1")

            
        elif query.find('restart pc') != -1:
            speak("Shutting down your pc")
            os.system("shutdown /r /t 1")

            
        elif query.find('bye') != -1:
            speak(random.choice(endings) + ". don't forget to leave a feedback about me.")
            exit()

            
        elif 'you mind' in query:
            speak("No I won't mind")

            
        elif query.find('joke') != -1 or query.find('jokes') != -1:
            speak(pyjokes.get_joke())

            
        elif query.find('song') != -1:
            speak(random.choice(["Sorry, I can't sing", "Pardon me, I can't sing"]))

            
        elif "you from" in query:
            speak("I am from your computer")

            
        elif "you optica" in query:
            speak("Yes")

            
        elif "capital" in query:
                if query.find('what') == -1 or query.find('is') == -1 or query.find('the') == -1 or query.find('of') == -1:
                    speak("Pronounce the sentence correctly correctly")
                else:
                    country = ((query.replace('capital of ', '')).replace('what is', '')).replace('the', '').lower().strip()
                    
                    print("Countries : " + country.capitalize())
                    if country in Countries:
                        try:
                                capital = CountryInfo(country.strip()).capital()
                                print("Capital : " + capital)
                                speak("The capital of " + country + " is " + capital)
                                
                        except KeyError:
                                speak("Maybe " + country + " is itself a city or it does not have a capital")
                    else:
                        speak("Sorry, country not found or you pronounced incorrectly")

                        
        elif "currency" in query:
                if query.find('what') == -1 or query.find('is') == -1 or query.find('the') == -1 or query.find('of') == -1:
                    speak("say the sentence correctly")
                else:
                    try:
                        country = ((query.replace('currency of ', '')).replace('what is', '')).replace('the', '').lower().strip()
                    except KeyError:
                            pass
                        
                    print("Countries : " + country.capitalize())    
                    if country in Countries:
                        currency = CountryInfo(country.strip()).currencies()
                        print("Currency : " + currency)
                        speak("The currency of " + country + " is " + str(currency))
                        
                    else:
                        speak("Sorry, country not found or you pronounced incorrectly")

                        
        elif query.find('who is') != -1 or query.find("who was") != -1 or query.find('what is') != -1 or query.find('what was') != -1 or query.find('do you know') != -1 or query.find('can you say') != -1:
                        if query.find('who is') != -1:
                            person = query.replace('who is', '')
                            
                        elif query.find('who was') != -1:
                            person = query.replace('who was', '')
                            
                        elif query.find('what is') != -1:
                            person = query.replace('what is', '')
                            
                        elif query.find('what was') != -1:
                            person = query.replace('what was', '')
                            
                        elif query.find('what was') != -1:
                            person = query.replace('do you know', '')
                            
                        elif query.find('what was') != -1:
                            person = query.replace('can you say', '')
                            
                        elif query.find('about') != -1:
                            person = person.replace('about', '')
                            
                        try:
                            speak(strip_brackets(wikipedia.summary(person, sentences=1)))
                            print("\n")
                            
                        except Exception as e:
                            try:
                                pywhatkit.info(e.options[0])
                                print("\n")
                                speak("This is what I found on google")
                            except:
                                speak("I don't know, ask me about someone or something else")

                                
        elif ('you ' and ' doing') in query:
                speak("I am just talking to you")

                
        elif 'play' in query and not 'game' in query:
                song = query.replace('play', '')
                speak('playing ' + song)
                pywhatkit.playonyt(song)

                
        elif 'write' in query:
            speak("What should I write? enter here and press enter twice")
            text = input("Handwriting : ")
            time.sleep(3)
            pywhatkit.text_to_handwriting(text, os.path.join(os.environ['USERPROFILE'], 'Desktop') + "\My Handwriting.jpg")
            speak("Done. My handwriting has been saved to your desktop\n")

            
        elif 'play' in query and 'game' in query:
                speak("Which game would you like to play?")
                print('''    Games :
            1. Snake
            2. Cannon
            3. Memory
            4. Connect
            5. Flappy Dot
            6. Number Puzzle
                      ''')
                game = takeCommand().lower()
                if 'snake' in game or '1' in game:
                    os.system("python -m freegames.snake")
                    
                elif 'canon' in game or '2' in game:
                    os.system("python -m freegames.cannon")
                    
                elif 'memory' in game or '3' in game:
                    os.system("python -m freegames.memory")
                    
                elif 'connect' in game or '4' in game:
                    os.system("python -m freegames.connect")
                    
                elif 'flappy' in game or '5' in game:
                    os.system("python -m freegames.flappy")
                    
                elif 'number' in game or '6' in game:
                    os.system("python -m freegames.tiles")
                    
                else:
                    speak("I can't find the game " + game + " in this list")
                    pass

                
        elif 'how to' in query:
                speak("Let's watch this video on " + query)
                pywhatkit.playonyt(query)


        elif query.find('created') != -1 or query.find('creator') != -1 or query.find('made') != -1:
                speak(random.choice(["My creator is Saji dur rahman fiad sir"], ["Saji dur rahman fiad sir made me"]))

                
        elif 'you' in query and 'know' in query:
            speak('Yes I know')
        else:
            if query == "none":
                print("     Pardon me, I didn't catch that.\n")
            else:
                try:
                    print(query.capitalize())
                    pywhatkit.info(query)
                    print("\n")
                    speak(random.choice(["Here is what I found on google", "This is what I found on google", "I found this on google", "I fount this on wikipedia", "This is what I found in wikipedia"]))
                except:
                    print("     Pardon me, I didn't catch that.\n")

                    
if __name__ == "__main__":
    if connected():
        pass
    else:
        os.system('mode 800')
        os.system('color 4')
        print("\n\nNo Internet Connection\n\n")
        os.system('color 7')
        print('''                                                                     `.--://+++++++//:--.`
                                                                     .-/+sssssssssssssssssssssss+/-.
                                                                 .:+sssssssssssssssssssssssssssssssss+:.
                                                              ./sssssssssssssssssssssssssssssssssssssssso/.
                                                           `:ossssssssssssssssssssssssssssssssssssssssssssso:`
                                                         ./ssssssssssssssso+/:-.``     ``.-:/+ssssssssssssssss/`
                                                       `+ssssssssssssso/-`                     `-/osssssssssssss/`
                                                      :sssssssssssssss:                            `:ossssssssssss:
                                                    .ossssssssssssssssso.                             ./ssssssssssso`
                                                   -sssssssssssssssssssss+`                             `/sssssssssss-
                                                  :ssssssssss+./sssssssssss/-:/+ossssssso+/:.`            `+ssssssssss-
                                                 :ssssssssss:   .+sssyhdmNMMMMMMMMMMMMMMMMMMMMNdy+-`        :ssssssssss-
                                                .ssssssssss.     -ymMMMMMMMMMMMMNmmmmmmNNMMMMMMMMMMMds:`     .ssssssssss.
                                               `osssssssss.   :yNMMMMMMMNmdhhyys:        `.-/oydMMMMMMMMh+`   .ssssssssso
                                               /sssssssss- .sNMMMMMNhosyssssssssso-             `-+yNMMMMMMh/  :sssssssss:
                                              `sssssssss+:hMMMMMNy:`   -osssssyyhhhs//::-`           -omMMMMMNo`+sssssssss
                                              -sssssssss:yMMMMh/        .sdmNMMMMMMMMMMMMMMmhs/.        -yNMMMm/-sssssssss-
                                              /sssssssso  .yy.      `:smMMMMMMMMMMMMMMMMMMMMMMMMNh+.      `od+   sssssssss/
                                              ossssssss+          :yNMMMMMMmhhdhyyyyyyyyyooymMMMMMMMd+`          +ssssssss+
                                              ossssssss/        /mMMMMMms/`   :sssssssssss/` `:odMMMMMNs.        +ssssssss+
                                              +ssssssss+        -yMMNs-        `+syyyyysssss-    .omMMN+`        +ssssssss+
                                              /sssssssss          -+`      `:oydNMMMMMMMNNdhyo.     :+`          sssssssss/
                                              -sssssssss-               `/hNMMMMMMMMMMMMMMMMMNd+`               -sssssssss-
                                               ssssssssso              :NMMMMMds+:---+hhdmMMMMMMd:              osssssssso
                                               :sssssssss:              -hMh/`        .ossshmMMdyso.           :sssssssss:
                                                osssssssss-               `       `...` -ssssyysssss/`        -ssssssssso
                                                .ssssssssss-                  `+hNMMMMMms:/sssssssssss:      -ssssssssss`
                                                 -ssssssssss/                 -hMMMMMMMMNo`.+sssssssssso.   /ssssssssss.
                                                  -sssssssssso.                 -hMMMMNo`    -sssssssssss+-ossssssssss.
                                                   .ossssssssss+.                 :hNo`       `/sssssssssssssssssssso.
                                                    `+sssssssssss+-                 .           .+sssssssssssssssss+`
                                                      -sssssssssssso/.                            -sssssssssssssso-
                                                       `:ssssssssssssss+:.                     .:+ssssssssssssss:
                                                         `:sssssssssssssssso+/:-...```...-:/+ossssssssssssssso:`
                                                            -+sssssssssssssssssssssssssssssssssssssssssssss+-
                                                              `:osssssssssssssssssssssssssssssssssssssss+:`
                                                                 `-/ossssssssssssssssssssssssssssssso/-`
                                                                     `.:/ossssssssssssssssssssso/:.`
                                                                           ``.-::://///:::-.``
                                                         ''')

        speak("You are not connected to the internet. Please try again later\n")
        os.system('pause')
        quit()
    os.system('cls')
    print("[INFO] Starting Artificial Intelligence...\n")
    initialize_hardware()
    time.sleep(1)
    main()
