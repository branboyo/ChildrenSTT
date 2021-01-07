import speech_recognition as sr
# Requires python 3.0+
# pip3 install pyaudio
# pip3 install speechrecognition
# brew install portaudio
 
def main():
 
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        print("Listening...")
 
        audio = r.listen(source, phrase_time_limit=2)
 
        try:
            if (r.recognize_google(audio) == "Daniel is gay"):
                print("Very true brother")
            else:
                print("You have said: " + r.recognize_google(audio))
 
        except Exception as e:
            print("Error:  " + str(e))

        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
 
main()
