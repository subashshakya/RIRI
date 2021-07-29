# RIRI the voice assistant

import speech_recognition as sr 
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

# speech_recognition is for audio input
# webbrowser handles the url routing 
# time is self explanatory

r = sr.Recognizer()

def record_voice(ask = False):
    with sr.Microphone() as source:
        if ask:
            speaking_RIRI(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
        except sr.RequestError:
            print('Sorry, my speech service is down')
        return voice_data

def speaking_RIRI(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    ran = random.randint(1, 10000)
    audio_file = 'audio-' + str(ran) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def response(voice_data):
    if 'what is your name' in voice_data:
        print('My name is RIRI')
    if 'what can you do' in voice_data:
        speaking_RIRI('i can do alot of things')
    if 'search' in voice_data:
        search = record_voice('what do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('here is what i found for your search')
    if 'search location' in voice_data:
        location = record_voice('where do you want to go?')
        url = 'https://google.nl/maps/place' + location + '/&amp;'
        webbrowser.get().open(url)
        print('here is your desired location')
    if 'who created you' in voice_data:
        speaking_RIRI('subash')
    if 'exit' in voice_data:
        exit()

time.sleep(1)
print('How may I help you?')
while 1:
    voice_data = record_voice()
    response(voice_data)