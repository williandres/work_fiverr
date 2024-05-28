import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ChangeFileNameHandler(FileSystemEventHandler):
    n = 514
    def on_created(self, event):
        if not event.is_directory:
            self.rename_file(event.src_path)
    
    def rename_file(self, src_path):
        directory, filename = os.path.split(src_path)
        new_filename = get_number() + '.png'
        new_filepath = os.path.join(directory, new_filename)
        os.rename(src_path, new_filepath)
        print(f"Renamed '{src_path}' to '{new_filepath}'")


def get_number():
    nombre_archivo = 'num.txt'
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read().strip()
        numero = contenido
    nuevo_numero = int(numero) + 1
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(str(nuevo_numero))

    return numero

if __name__ == "__main__":
    path_to_watch = "/home/willian/Pictures/Screenshots"
    event_handler = ChangeFileNameHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=False)
    
    print(f"Monitoring '{path_to_watch}' for new files...")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
