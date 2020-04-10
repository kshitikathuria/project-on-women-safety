
# importing speech recognition package from google api 
import speech_recognition as sr  
from twilio.rest import Client
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula 
from selenium import webdriver # to control browser operations 
  
num = 1
def assistant_speaks(output): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("PerSon : ", output) 
  
    toSpeak = gTTS(text = output, lang ='en', slow = False) 
    # saving the audio file given by google text to speech 
    file = str(num)+".mp3"  
    toSpeak.save(file) 
      
    # playsound package is used to play the same file. 
    playsound.playsound(file, True)  
    os.remove(file) 
  
  
  
def get_audio(): 
  
    rObject = sr.Recognizer() 
    audio = '' 
  
    with sr.Microphone() as source: 
        print("Speak...") 
          
        # recording the audio using speech recognition 
        audio = rObject.listen(source, phrase_time_limit = 5)  
    print("Stop.") # limit 5 secs 
  
    try: 
  
        text = rObject.recognize_google(audio, language ='en-US') 
        print("You : ", text) 


        return text 
  
    except: 
  
        assistant_speaks("Could not understand your audio, PLease try again !") 
        return 0
  
  
# Driver Code 
if __name__ == "__main__": 
    assistant_speaks("u listening ?") 
    name ='Human'
    name = get_audio() 
    assistant_speaks("Hello, " + name + '.') 
      
    while(1): 
  
        assistant_speaks("speak the code to send the  message") 
        text = get_audio().lower() 
  
        if text == "help":

 
            client = Client("AC6229d65065d6e2700a821c30aa881320", "1d495c1eccff6f471e33ff085e28494c")

            # change the "from_" number to your Twilio number and the "to" number
            # to the phone number you signed up for Twilio with, or upgrade your
            # account to send SMS to any phone number
            client.messages.create(to="+918171220661",
            from_="+18588776023",
            body="Help me !")
            print("message has been send succesfully to the registered mobile number")
            continue

  
        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
            assistant_speaks("Ok bye, "+ name+'.') 
            break
  
        # calling process text to process the query 
        process_text(text) 


