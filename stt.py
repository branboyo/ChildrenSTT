import speech_recognition as sr

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")   
        audio = r.listen(source,timeout=3, phrase_time_limit=3)
        try:
            print("You said : " + r.recognize_google(source))
        except Exception as e:
            print("Error:" + str(e))

main()
