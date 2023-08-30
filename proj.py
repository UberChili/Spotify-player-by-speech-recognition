from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import webbrowser as web
import pyautogui
from time import sleep
#import pyttsx3, pywhatkit
import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language='es-ES')
            rec = rec.lower(0)          
    except:
        pass
    print("Rec: {}".format(rec))
    return rec

# Need to fill this with dev user's id and secret
client_id = ""
client_secret= ""
flag = 0

author = ''
song = ''


def escucharcancion():
    global song
    talk("Qué canción quieres escuchar?")
    print("Qué canción quieres escuchar?")
    rec = listen()
    if "" in rec:
        song = rec.upper()
        empezar()
    else: 
        pass


def empezar():
    global flag
    global song

    if len(author) > 0:
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
        result = sp.search(author)

        for i in range(0, len(result["tracks"]["items"])):
            name_song = result["tracks"]["items"][i]["name"].upper()

            if song in name_song:
                flag = 1
                web.open(result["tracks"]["items"][i]["uri"])
                sleep(2)
                pyautogui.press("enter")
                break
            
    if flag == 0:
        song = song.replace(" ", "%20")
        web.open(f'spotify:search:{song}')
        sleep(2)
        for i in range(4):                
            pyautogui.press("tab")
        pyautogui.press("enter")
      
     
escucharcancion()
