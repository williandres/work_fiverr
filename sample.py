import subprocess
import os
import time
from pynput.keyboard import Key, Controller

def install(exe):
    keyboard = Controller()
    #os.system(exe)

    time.sleep(1)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(10)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    keyboard.press('a')
    keyboard.release('a')

def run():
    time.sleep(10)
    dir = [ f.path for f in os.scandir('./') if f.is_dir() ]
    for dirs in dir:
        for f in os.listdir(dirs):
            if f[-4:] == '.exe':
                install(dirs + "/" + f)


if __name__ == '__main__':
    run()