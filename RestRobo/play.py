import json
import time
import inspect
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Controller as KeyboardController, Key
import openapp

class EventReplayer:
    def __init__(self):
        self.key_mapping = {}
        for name, obj in inspect.getmembers(Key):
            if not name.startswith('__') and not callable(obj):
                self.key_mapping[f'Key.{name}'] = obj

        self.mouse_controller = MouseController()
        self.keyboard_controller = KeyboardController()

    def load_events_from_file(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def execution_mouse(self, event):
        if event['event'] == 'click' and event['pressed'] == True:
            self.mouse_controller.position = tuple(event['position'])
            if event['button'] == "Button.left":
                self.mouse_controller.press(Button.left)
            elif event['button'] == "Button.right":
                self.mouse_controller.press(Button.right)
            elif event['button'] == "Button.middle":
                self.mouse_controller.press(Button.middle)
        elif event['event'] == 'click' and event['pressed'] == False:
            if event['button'] == "Button.left":
                self.mouse_controller.release(Button.left)
            elif event['button'] == "Button.right":
                self.mouse_controller.release(Button.right)
            elif event['button'] == "Button.middle":
                self.mouse_controller.release(Button.middle)
        elif event['event'] == 'scroll':
            self.mouse_controller.scroll(int(event['dx']), int(event['dy']))

    def execution_keyboard(self, event):
        key = str(event['key']).replace("'", "")
        if event['event'] == 'press' and key != 'null':
            if '.' in key and key != '.':
                key = self.key_mapping[key]
            self.keyboard_controller.press(key)
        elif event['event'] == 'release' and key != 'null':
            if '.' in key and key != '.':
                key = self.key_mapping[key]
            self.keyboard_controller.release(key)

    def replay_events(self, profile, fileapp, extra_delay):
        events = self.load_events_from_file(profile)
        last_timestamp = None
        openapp.main(fileapp)
        for event in events[1:]:
            if last_timestamp is not None:
                delay = event['timestamp'] - last_timestamp
                time.sleep(delay+extra_delay)
            last_timestamp = event['timestamp']
            print(event)
            if event['type'] == 'mouse':
                self.execution_mouse(event)
            elif event['type'] == 'keyboard':
                self.execution_keyboard(event)


