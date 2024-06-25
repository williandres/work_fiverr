import json
import time
import inspect
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Controller as KeyboardController, Key

time.sleep(5)
events_file = 'profiles/events262.json'  

key_mapping = {}
# Iterar sobre los atributos de la clase Key
for name, obj in inspect.getmembers(Key):
    if not name.startswith('__') and not callable(obj):
        key_mapping[f'Key.{name}'] = obj

# Cargar eventos desde el archivo JSON
def load_events_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

events = load_events_from_file(events_file)

mouse_controller = MouseController()
keyboard_controller = KeyboardController()



def execution_mouse(event):
    # if event['event'] == 'move':
    #     mouse_controller.position = tuple(event['position'])
    if event['event'] == 'click' and event['pressed'] == True:
        mouse_controller.position = tuple(event['position'])
        time.sleep(1)
        if event['button'] == "Button.left":
            mouse_controller.press(Button.left)
        elif event['button'] == "Button.right":
            mouse_controller.press(Button.right)
        elif event['button'] == "Button.middle":
            mouse_controller.press(Button.middle)
    # elif event['event'] == 'click' and event['pressed'] == False:
    #     time.sleep(1)
    #     if event['button'] == "Button.left":
    #         mouse_controller.release(Button.left)
    #     elif event['button'] == "Button.right":
    #         mouse_controller.release(Button.right)
    #     elif event['button'] == "Button.middle":
    #         mouse_controller.release(Button.middle)
    elif event['event'] == 'scroll':
        mouse_controller.scroll(int(event['dx']), int(event['dy']))

def execution_keyboard(event):
    time.sleep(1)
    key = str(event['key']).replace("'", "")
    if event['event'] == 'press' and key != 'null':
        if '.' in key:
            key = key_mapping[key]
        keyboard_controller.press(key)
    elif event['event'] == 'release' and key != 'null':
        if '.' in key:
            key = key_mapping[key]
        keyboard_controller.release(key)



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
