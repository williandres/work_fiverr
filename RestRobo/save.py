import json
import time
from pynput import mouse, keyboard
from datetime import date
import openapp

class EventRecorder:
    def __init__(self):
        self.events = []
        self.running = True

    #-----------------------------------------Mouse-----------------------------------------#
    def on_move(self, x, y):
        event = {
            'type': 'mouse',
            'event': 'move',
            'position': (x, y),
            'timestamp': time.time()
        }
        self.events.append(event)

    def on_click(self, x, y, button, pressed):
        if not self.running:
            return False
        event = {
            'type': 'mouse',
            'event': 'click',
            'position': (x, y),
            'button': str(button),
            'pressed': pressed,
            'timestamp': time.time()
        }
        self.events.append(event)
        print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))

    def on_scroll(self, x, y, dx, dy):
        if not self.running:
            return False
        event = {
            'type': 'mouse',
            'event': 'scroll',
            'position': (x, y),
            'dx': dx,
            'dy': dy,
            'timestamp': time.time()
        }
        self.events.append(event)
        print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))

    #-----------------------------------------Keyboard-----------------------------------------#
    def on_press(self, key):
        if not self.running:
            return False
        try:
            event = {
                'type': 'keyboard',
                'event': 'press',
                'key': key.char,
                'timestamp': time.time()
            }
            print('alphanumeric key {0} pressed'.format(key.char))
        except AttributeError:
            event = {
                'type': 'keyboard',
                'event': 'press',
                'key': str(key),
                'timestamp': time.time()
            }
            print('special key {0} pressed'.format(key))
        self.events.append(event)

    def on_release(self, key):
        if not self.running:
            return False
        event = {
            'type': 'keyboard',
            'event': 'release',
            'key': str(key),
            'timestamp': time.time()
        }
        print('{0} released'.format(key))
        if key == keyboard.Key.esc:
            self.running = False
            return False
        self.events.append(event)

    #-----------------------------------------Ejecucion-----------------------------------------#
    def save_events_to_file(self, filename, name, description, fileapp):
        self.events.insert(0, {
            'key': "RestRobo",
            'tittle': name,
            'description': description,
            'app': fileapp,
            'creation date': str(date.today().strftime("%d/%m/%Y"))
        })
        with open(filename, 'w') as file:
            json.dump(self.events, file, indent=4)
        print(f'Saved {filename}')
        self.events = []
        self.running = True

    def main(self, filename, name, description, fileapp):
        self.events = []
        self.running = True
        openapp.main(fileapp)
        with mouse.Listener(on_click=self.on_click, on_scroll=self.on_scroll) as mouse_listener, \
             keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as keyboard_listener:
            while self.running:
                pass

        self.save_events_to_file(filename, name, description, fileapp)
