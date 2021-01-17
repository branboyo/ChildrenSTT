import speech_recognition as sr
from flask import Flask, render_template, request
# Requires python 3.0+
# pip3 install pyaudio
# pip3 install speechrecognition
# brew install portaudio

# To test in terminal: 
# >>> python3, >>> from stt import check, >>> check("string")
app = Flask(__name__)
@app.route('/')
def main():
    return render_template('home.html')

@app.route('/alpha.html')
def alpha():
    return render_template('alpha.html')

@app.route('/apple.html')
def apple():
    return render_template('apple.html')

def check(string):
 
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Listening...")
 
        audio = r.listen(source, phrase_time_limit=3)
        trans = r.recognize_google(audio)
        try:
            if (trans == string):
                return True
            else:
                return False
 
        except Exception as e:
            print("Error:  " + str(e))

        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())

