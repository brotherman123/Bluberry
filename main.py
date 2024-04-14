#Modules
import speech_recognition as sr
import pyaudio
import gtts as gts
import time
import playsound as ps
import wikipedia as wiki


#Variables
recognizer = sr.Recognizer()
loctime = time.ctime()
language = 'en'
localtext2speech = gts.gTTS(text=loctime, lang=language, slow=False)
stoppingprogram = gts.gTTS(text='Shutting Down', lang=language, slow=False)
Serchresult = gts.gTTS(text='coolman', lang=language, slow=False)
stoppingprogram.save("stopping.mp3")
Serchresult.save("wikiresult.mp3")
localtext2speech.save("LocalTime.mp3")
recognizer.energy_threshold = 4000
p = pyaudio.PyAudio()
result = 12


#Functions



def capture_voice_input():
    with sr.Microphone() as source:
        print("listening...")
        audio = recognizer.listen(source)
    return audio
def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text
def process_voice_command(text):
    if "time" in text.lower():
        loctime = time.ctime()
        localtext2speech = gts.gTTS(text=loctime, lang=language, slow=False)
        print("The time is: ",loctime)
        localtext2speech.save("LocalTime.mp3")
        ps.playsound("LocalTime.mp3") 
    elif "search" in text.lower():
        text.replace('search', '')
        Serchresult = gts.gTTS(text=wiki.summary(text, sentences = 3), lang=language, slow=False)
        Serchresult.save("wikiresult.mp3")
        ps.playsound('wikiresult.mp3')
    elif "stop" in text.lower():
        ps.playsound("stopping.mp3") 
        exit("stopped program")
        return True
    else:
        print("You said: " + text)
    return False

#Main
def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)

if __name__ == "__main__":
    main()
