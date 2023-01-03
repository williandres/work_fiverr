import os
import time
from pynput.keyboard import Key, Controller

def install(exe):
    keyboard = Controller()
    os.startfile(exe)

    time.sleep(3)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(8)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def run():
    path = os.getcwd()
    dir = [ f.path for f in os.scandir('./')]
    for f in dir:
        if f[-4:] == '.exe':
            install(f'{path}\{f[2:]}')

if __name__ == '__main__':
    run()