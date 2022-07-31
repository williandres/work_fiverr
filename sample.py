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

    time.sleep(10)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def run():
    path = os.getcwd()
    dir = [ f.path for f in os.scandir('./') if f.is_dir() ]
    for dirs in dir:
        for f in os.listdir(dirs):
            if f[-4:] == '.exe':
                install(f'{path}\{dirs[2:]}\{f}')

if __name__ == '__main__':
    run()