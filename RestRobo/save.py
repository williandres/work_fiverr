import json
import time
from pynput import mouse, keyboard

events = []
running = True

#-----------------------------------------Mouse-----------------------------------------#
def on_move(x, y):
    event = {
        'type': 'mouse',
        'event': 'move',
        'position': (x, y),
        'timestamp': time.time()
    }
    events.append(event)

def on_click(x, y, button, pressed):
    if not running:
        return False
    event = {
        'type': 'mouse',
        'event': 'click',
        'position': (x, y),
        'button': str(button),
        'pressed': pressed,
        'timestamp': time.time()
    }
    events.append(event)
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))

def on_scroll(x, y, dx, dy):
    if not running:
        return False
    event = {
        'type': 'mouse',
        'event': 'scroll',
        'position': (x, y),
        'dx': dx,
        'dy': dy,
        'timestamp': time.time()
    }
    events.append(event)
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))

#-----------------------------------------Keyboard-----------------------------------------#
def on_press(key):
    if not running:
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
    events.append(event)

def on_release(key):
    global running
    if not running:
        return False
    event = {
        'type': 'keyboard',
        'event': 'release',
        'key': str(key),
        'timestamp': time.time()
    }
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        running = False
        return False
    events.append(event)

#-----------------------------------------Ejecucion-----------------------------------------#
def save_events_to_file(filename, events, fileapp):
    data = {
        'fileapp': fileapp,
        'delay': 1,
        'events': events
    }
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f'Saved {filename}')

def main(fileapp):
    with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as mouse_listener, \
        keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_listener:
        while running:
            pass

    save_events_to_file(f'profiles/events.json', events, fileapp)

if __name__ == "__main__":
    pass
    #main('app url')