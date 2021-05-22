from urllib.parse import quote_from_bytes
from PIL import Image
import pyttsx3
import speech_recognition as sr 
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception:
        print("Say that again please...")  
        return "None"
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(" Hy Good Morning!")

    elif hour>=12 and hour<18:
        speak("Hy Good Afternoon!")   

    else:
        speak("Hy Good Evening!")
        
    speak("I am Jini! Your personal assistant, May I know your good name?")
    print("Hy I am Jini! Your personal assistant, May I know your good name?")
    name = takeCommand()
    print(" 1) Rotate\n 2) Crop\n 3) Resize\n 4) Histogram\n 5) Transpose\n")
    speak("Ok! Mr." + name + "you have some choices to manipulate the image, please select one of them. Rotate, crop ,  resize , histogram  or  transpose for image")
    


def rotate():
    try:
        img = Image.open(r"E:\Harsh\Projects\ImageManipulation\pyimage.jpg")
        
        speak("What shoud be the angle for rotating the image. please say only number: ")
        print("What shoud be the  angle for rotating the image")
        
        n = takeCommand()
        img = img.rotate(int(n))
        
        img.save(r"E:\Harsh\Projects\ImageManipulation\outputImages\rotated img.jpg")
        speak("Ok Done! successfully rotated and saved, Now showing the image.")
        img.show()
    
    except IOError:
        pass

    
def crop():
    try:
        img = Image.open(r"E:\Harsh\Projects\ImageManipulation\pyimage.jpg")
        
        h,k =img.size
        print("Original size of image = ",str(h) + "*" +str(k))
    
        speak("what should be the width?")
        print("what should be the width?")
        width = takeCommand()
        
        speak("What should be the Height?")
        print("What should be the Height?")
        height = takeCommand()
        area = (0, 0, int(width), int(height)) 
        img = img.crop(area) 
          
        #Saved in the same relative location 
        img.save(r"E:\Harsh\Projects\ImageManipulation\outputImages\cropped_picture.jpg")  
        speak("Ok Done! successfully Cropped and saved, Now showing the image.")
        img.show()
          
    except IOError: 
        pass
    
def resize():
    try:
        img = Image.open(r"E:\Harsh\Projects\ImageManipulation\pyimage.jpg")
        h,k =img.size
        print("Original size of image = ",str(h) + "*" +str(k))
    
        
        speak("What should be the new width for image?" )
        print("What should be the new width for image?" )
        width = takeCommand()
        speak("What should be the new height? ")
        print("What should be the new height? ")
        height = takeCommand()
        
        p = (int(width), int(height))
        img = img.resize(p)
        h,k = img.size
        img.save(r"E:\Harsh\Projects\ImageManipulation\outputImages\Resized_img.jpg")
        speak("All right! successfully Resized and saved, Now showing the image.")
        print("New Size : " + str(h) + "*" + str(k))
        img.show()
        
    except IOError:
        pass
    
def histogram():
    try:
        img = Image.open(r"E:\Harsh\Projects\ImageManipulation\pyimage.jpg")
        print (img.histogram())
        speak("Histogram of image is on your screen.")
    except IOError:
        pass

def transpose():
    try:
        img = Image.open(r"E:\Harsh\Projects\ImageManipulation\pyimage.jpg")
        transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        transposed_img.save(r"E:\Harsh\Projects\ImageManipulation\outputImages\transposed_img.jpg")
        speak("Ok done! successfully transposed & saved, now showing the traansposed image.")
        transposed_img.show()
        
    except IOError:
        pass
        

if __name__ == "__main__":    
    wishMe()

    query = takeCommand().lower()  
    if 'rotate' in query:
        rotate()
    elif 'crop' in query:
        crop()
    elif 'resize' in query:
        resize()
    elif 'histogram' in query:
        histogram()
    elif 'transpose' in query:
        transpose()

print('Thanks for giving your time. . I am always here to help you.')
speak('Thanks for giving your time. . I am always here to help you.')
            
        
    