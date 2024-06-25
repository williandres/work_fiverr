from pynput.keyboard import Key
import inspect

# Crear un diccionario vacío para los mapeos
key_mapping = {}
# Iterar sobre los atributos de la clase Key
for name, obj in inspect.getmembers(Key):
    if not name.startswith('__') and not callable(obj):
        key_mapping[f'Key.{name}'] = obj

print(key_mapping)