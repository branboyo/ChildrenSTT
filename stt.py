import speech_recognition as sr

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")   

        audio = r.listen(source)
        try:
            print("You said : {}".format(text))
            text = r.recognize_google(audio)
        except Exception as e:
            print("Error:" + str(e))

main()
