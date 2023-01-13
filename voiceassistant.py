import speech_recognition
import pyttsx3
import datetime
import os


mic = speech_recognition.Microphone(device_index=1)

print(speech_recognition.Microphone.list_microphone_names())

#print(speech_recognition.Microphone.list_microphone_names()[1])



recognizer = speech_recognition.Recognizer()


import pyttsx3

engine = pyttsx3.init()

def speak(audio):

    engine.say(audio)
    engine.runAndWait()


def getCommand():
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("say something")
            audio = recognizer.listen(source)


        words = recognizer.recognize_google(audio, None, "en-US", True)
        print(words['alternative'][0]['transcript'])
        data=words['alternative'][0]['transcript']
        print(data)
        return data



speak ('Hello mohamed, How can I help You!')
while True:

     speech=getCommand()

     if "hello" in speech:
         print("Hello to you")
         speak("Hello to you")


     elif "how are you" in speech:
         print("iam well thanks")
         speak("iam well thanks")
         
     elif "thank you" in speech:
         print("you are welcome")
         speak("you are welcome") 
      
     elif "how old are you" in speech:
         print("since i was invented")
         speak("since i was invented")

     elif "do you have a family" in speech:
         print("i do not have a family the way a person would")
         speak("i do not have a family the way a person would")



     elif "where are you from" in speech:
         print("i from egypt")
         speak("i from egypt")

     elif "iam sad" in speech:
         print("no man i well play you a playlist to ahmed kamel than will lead you to suicide")
         speak("no man i well play you a playlist to ahmed kamel than will lead you to suicide")
         songs_dir = "Music/AhmedKamel"
         songs =os.listdir(songs_dir)
         os.starfile(os.path.join(songs_dir, songs[0]))


     elif "remeber that" in speech:

         speak("what should I remember")
         data=getCommand()
         speak("you asked me to remember"+data)
         remember=open("Data.txt","w")
         remember.write(data)
         remember.close()



     elif "today plan" in speech:
         remember=open("Data.txt","r")
         speak("you said me to remember that" + remember.read())


     elif "search" in speech:
         speak("what should i search")

         data=getCommand()
         import webbrowser as wb
         wb.register('chrome', None)
         wb.open("http://www.google.com/search?q=" +data)

     else:
         print("Huh?")
         speak("Sorry")

















