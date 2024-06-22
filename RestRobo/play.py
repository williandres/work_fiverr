import json
import time
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Controller as KeyboardController, Key

time.sleep(5)
events_file = 'profiles/events421.json'  

# Cargar eventos desde el archivo JSON
def load_events_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

events = load_events_from_file(events_file)

mouse_controller = MouseController()
keyboard_controller = KeyboardController()


def execution_mouse(event):
    if event['event'] == 'move':
        mouse_controller.position = tuple(event['position'])
    elif event['event'] == 'click' and event['pressed'] == True:
        time.sleep(1)
        if event['button'] == "Button.left":
            mouse_controller.press(Button.left)
        elif event['button'] == "Button.right":
            mouse_controller.press(Button.right)
    elif event['event'] == 'click' and event['pressed'] == False:
        time.sleep(1)
        if event['button'] == "Button.left":
            mouse_controller.release(Button.left)
        elif event['button'] == "Button.right":
            mouse_controller.release(Button.right)
    #on scroll - click scroll

def execution_keyboard(event):
    time.sleep(1)
    key = str(event['key']).replace("'", "")
    if event['event'] == 'press' and key != 'null':
        if '.' in key:
            key = globals()[key]
        keyboard_controller.press(Key.space)
    elif event['event'] == 'release' and key != 'null':
        if '.' in key:
            key = globals()[key]
        keyboard_controller.release(Key.space)



# Reproducir los eventos
def replay_events(events):
    for event in events:
        print('illo')
        print(event)
        if event['type'] == 'mouse':
            execution_mouse(event)
        elif event['type'] == 'keyboard':
            execution_keyboard(event)

replay_events(events)
