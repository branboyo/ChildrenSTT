
from flask import Flask, render_template, request
# Requires python 3.0+
# pip3 install pyaudio
# pip3 install speechrecognition
# brew install portaudio∏

# To test in terminal: 
# >>> python3, >>> from stt import check, >>> check("string")
app = Flask(__name__)

@app.route('/')
def main():
    return app.send_static_file('home.html')

@app.route('/alpha')
def alpha():
    return app.send_static_file('alpha.html')

@app.route('/alpha/apple')
def apple():
    return render_template('lesson.html', key = 'APPLE', next = '/alpha/banana', back = '/alpha', lesson = '1', part = '1', yt = 'https://www.youtube.com/embed/491-YZrgjxk?rel=0')

@app.route('/alpha/banana')
def banana():
    return render_template('lesson.html', key = 'BANANA', next = '/alpha/close', back = '/alpha/apple', lesson = '1', part = '2', yt = 'https://www.youtube.com/embed/-ocYrqMe1ag?rel=0')

@app.route('/alpha/close')
def close():
    return render_template('lesson.html', key = 'CLOSE', next = '/alpha/dog', back = '/alpha/banana', lesson = '1', part = '3', yt = 'https://www.youtube.com/embed/9SXr4uhafio?rel=0')

@app.route('/alpha/dog')
def dog():
    return render_template('lesson.html', key = 'DOG', next = '/alpha/ear', back = '/alpha/close', lesson = '1', part = '4', yt = 'https://www.youtube.com/embed/P-ImIwb79sE?rel=0')

@app.route('/alpha/ear')
def ear():
    return render_template('lesson.html', key = 'EAR', next = '/alpha/flower', back = '/alpha/dog', lesson = '1', part = '5', yt = 'https://www.youtube.com/embed/rb9z3iRN5E4?rel=0')

@app.route('/alpha/flower')
def flower():
    return render_template('lesson.html', key = 'FLOWER', next = '/alpha/golf', back = '/alpha/ear', lesson = '1', part = '6', yt = 'https://www.youtube.com/embed/55ItxbQqVQM?rel=0')

@app.route('/alpha/golf')
def golf():
    return render_template('lesson.html', key = 'GOLF', next = '/unregistered', back = '/alpha/flower', lesson = '1', part = '7', yt = 'https://www.youtube.com/embed/icVisKkTYb0?rel=0')


if __name__ == "__main__":
    app.run()