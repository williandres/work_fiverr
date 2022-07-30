import subprocess
import os
import time
from pynput.keyboard import Key, Controller

def install(exe):
    keyboard = Controller()
    os.startfile(exe)

    time.sleep(1)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(5)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def run():
    dir = [ f.path for f in os.scandir('./assets') if f.is_dir() ]
    for dirs in dir:
        for f in os.listdir(dirs):
            if f[-4:] == '.exe':
                path = f
        install(dirs + "/" + path)


if __name__ == '__main__':
    run()