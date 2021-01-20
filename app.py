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

@app.route('/alpha')
def alpha():
    return render_template('alpha.html')

@app.route('/alpha/apple')
def apple():
    return render_template('lesson.html', key = 'Apple', next = '/alpha/atlas', lesson = '1', part = '1')

@app.route('/alpha/atlas')
def atlas():
    return render_template('lesson.html', key = 'Atlas', next = '/alpha/aunt', lesson = '1', part = '2')

@app.route('/alpha/aunt')
def ant():
    return render_template('lesson.html', key = 'Aunt', next = '/unregistered', lesson = '1', part = '3')



if __name__ == "__main__":
    app.run()