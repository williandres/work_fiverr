import json
import time
import inspect
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Controller as KeyboardController, Key

#-----------------------------------------Preload-----------------------------------------#


def load_events_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)



#-----------------------------------------Functions-----------------------------------------#

def execution_mouse(event):
    if event['event'] == 'click' and event['pressed'] == True:
        mouse_controller.position = tuple(event['position'])
        if event['button'] == "Button.left":
            mouse_controller.press(Button.left)
        elif event['button'] == "Button.right":
            mouse_controller.press(Button.right)
        elif event['button'] == "Button.middle":
            mouse_controller.press(Button.middle)
    elif event['event'] == 'click' and event['pressed'] == False:
        if event['button'] == "Button.left":
            mouse_controller.release(Button.left)
        elif event['button'] == "Button.right":
            mouse_controller.release(Button.right)
        elif event['button'] == "Button.middle":
            mouse_controller.release(Button.middle)
    elif event['event'] == 'scroll':
        mouse_controller.scroll(int(event['dx']), int(event['dy']))

def execution_keyboard(event):
    key = str(event['key']).replace("'", "")
    if event['event'] == 'press' and key != 'null':
        if '.' in key and key != '.':
            key = key_mapping[key]
        keyboard_controller.press(key)
    elif event['event'] == 'release' and key != 'null':
        if '.' in key and key != '.':
            key = key_mapping[key]
        keyboard_controller.release(key)

#-----------------------------------------Ejecucion-----------------------------------------#
def replay_events(profile):
    events = load_events_from_file(profile)
    last_timestamp = None
    for event in events:
        if last_timestamp is not None:
            delay = event['timestamp'] - last_timestamp
            time.sleep(delay)
        last_timestamp = event['timestamp']
        print(event)
        if event['type'] == 'mouse':
            execution_mouse(event)
        elif event['type'] == 'keyboard':
            execution_keyboard(event)

# time.sleep(5)
# print('Now!')

# key_mapping = {}
# for name, obj in inspect.getmembers(Key):
#     if not name.startswith('__') and not callable(obj):
#         key_mapping[f'Key.{name}'] = obj

# mouse_controller = MouseController()
# keyboard_controller = KeyboardController()

#replay_events('profiles/events.json')
