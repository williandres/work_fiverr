import json
import os
from pynput import mouse, keyboard
import random

# Listas para almacenar los eventos
events = []

# Variable global para controlar el estado de ejecución de los listeners
running = True


def on_move(x, y):
    event = {
        'type': 'mouse',
        'event': 'move',
        'position': (x, y)
    }
    events.append(event)

# Funciones para el mouse
def on_click(x, y, button, pressed):
    if not running:
        return False
    event = {
        'type': 'mouse',
        'event': 'click',
        'position': (x, y),
        'button': str(button),
        'pressed': pressed
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
        'dy': dy
    }
    events.append(event)
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))

# Funciones para el teclado
def on_press(key):
    if not running:
        return False
    try:
        event = {
            'type': 'keyboard',
            'event': 'press',
            'key': key.char
        }
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        event = {
            'type': 'keyboard',
            'event': 'press',
            'key': str(key)
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
        'key': str(key)
    }
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        running = False
        return False
    events.append(event)
# Función para guardar eventos en archivos JSON
def save_events_to_file(filename, events):
    with open(filename, 'w') as file:
        json.dump(events, file, indent=4)
    print(f'Eventos guardados en {filename}')

# Iniciar los listeners para el mouse y el teclado
with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouse_listener, \
     keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_listener:
    while running:
        pass

# Guardar los eventos al finalizar
save_events_to_file(f'profiles/events{random.randint(0, 1000)}.json', events)


