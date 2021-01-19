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

if __name__ == "__main__":
    app.run()