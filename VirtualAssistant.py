import speech_recognition as sr
from gtts import gTTS
import os
import time
from googlesearch import search
import webbrowser


def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'temp_voice.mp3'
    tts.save(filename)
    os.system(f'start {filename}')

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language='en')
        print(f"You said: {text}")
    except Exception as e:
        print("Sorry, I didn't understand that.")
        return None

    return text.lower()



def google_search(query):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)

def process_command(command):
    if 'hello' in command:
        speak('Hello! How can I help you?')
    elif 'information' in command or 'search' in command:

        speak('What would you like me to search for?')
        query = recognize_speech()
        if query:
            # Remove the word 'search' from the query string
            query = query.replace('search', '').strip()
            google_search(query)
            speak(f'Searching for {query} on Google.')
    else:
        speak("I'm sorry, I didn't understand the command. Please try again.")

def main():
    speak('Welcome to the virtual assistant. Say "Hey Siri" to activate me...')
    while True:
        command = recognize_speech()
        if command and 'siri' in command:
            speak('Say Search followed by what you want me to search up to search things')
            command = recognize_speech()
            if command:
                process_command(command)
        time.sleep(1)

if __name__ == '__main__':
    main()
