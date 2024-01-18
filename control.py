from pynput.mouse import Controller
from pynput.keyboard import Controller

def controlMouse():
    mouse = Controller()
    mouse.position(500,200) #(left-right,top to bottom)

def controlKeyboard():
    keyboard = Controller()
    keyboard.type('awesome whiskey')

controlKeyboard()
