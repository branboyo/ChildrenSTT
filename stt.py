import speech_recognition as sr
# Requires python 3.0+
# pip3 install pyaudio
# pip3 install speechrecognition
# brew install portaudio

# To test in terminal: 
# >>> python3, >>> from stt import check, >>> check("string")
 
def check(string):
 
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Listening...")
 
        audio = r.listen(source, phrase_time_limit=3)
        trans = r.recognize_google(audio)
        try:
            if (trans == string):
                print("Very true brother")
            else:
                print("You have said:" + trans)
 
        except Exception as e:
            print("Error:  " + str(e))

        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())

