import math
import time
import re
import pyttsx3
import sys
import speech_recognition as sr

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

def au(so):
    engine.say(so)
    engine.runAndWait()


def digicon(inputunit,outputunit,val):
    if "TB" in inputunit or "terabyte" in inputunit:
        if outputunit=="byte" or outputunit=="B":
            out=str((val)*(1.099511628e+12))
            audio=out+" Byte"
            print(audio)
            au(audio)
        if outputunit=="kilobyte" or outputunit=="KB":
            out=str((val)*(1073741824))
            audio=out+" KB"
            print(audio)
            au(audio)

        if outputunit=="MB" or outputunit=="megabyte":
            out=str((val)*(1048576))
            audio=(out+" MB")
            print(audio)
            au(audio)
        if outputunit=="GB" or outputunit=="gigabyte":
            out=str((val)*(1024))
            audio=(out+" GB")
            print(audio)
            au(audio)
    if "GB" in inputunit or "gigabyte" in inputunit:
        if outputunit=="byte" or outputunit=="B":
            out=str((val)*(1073741824))
            audio=(out+" Byte")
            print(audio)
            au(audio)
        
        if outputunit=="kilobyte" or outputunit=="KB":
            out=str((val)*(1048576))
            audio=(out+" KB")
            print(audio)
            au(audio)

        if outputunit=="MB" or outputunit=="megabyte":
            out=str((val)*(1024))
            audio=(out," MB")
            print(audio)
            au(audio)
    elif ("MB" in inputunit) or ("megabyte" in inputunit):
        if outputunit=="byte"or outputunit=="B":
            out=str((val)*(1048576))
            audio=(out+" Byte")
            print(audio)
            au(audio)
        if outputunit=="kilobyte" or outputunit=="KB":
            out=str((val)*(1024))
            audio=(out+" KB")
            print(audio)
            au(audio)
    elif ("KB" in inputunit) or("kilobyte" in inputunit):
        if outputunit=="byte" or outputunit=="B":
            out=str((val)*(1024))
            audio=(out+" Byte")
            print(audio)
            au(audio)





if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Plz say convertion digital storage value :")
        audio = r.listen(source)
        try:
            outstr= r.recognize_google(audio)
            print("You said : {}".format(outstr))
            a=str(outstr)
            #a="convert 1 TB equal to MB"
            g=a.split()
            outputunit=g[-1]
            print("output unit : {}".format(outputunit))
            delforiu=g[:-1]
            str1 = " "
            foriu = (str1.join(delforiu))
            val= " ".join(re.findall(r"[0-9]+", a))
            print("value : {}".format(val))
            print("input unit : {}".format(foriu))
            digicon(foriu,outputunit,int(val))
        except:
            print("Sorry could not recognize your voice")

