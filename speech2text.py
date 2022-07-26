import speech_recognition as sr
r = sr.Recognizer()
print('started.. you can speak now..')
with sr.Microphone() as source:
    rec_audio = r.record(source, duration=5)
    print('record has stoped.. recognizing ur speech.. wait for ur speech2text output')
    mytext = r.recognize_google(rec_audio)
    print(mytext)