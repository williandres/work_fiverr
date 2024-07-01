import play
import os
import subprocess
import platform
from save import EventRecorder



def is_executable_valid(executable):
    if platform.system() == 'Linux':
        return os.access(executable, os.X_OK)
    elif platform.system() == 'Windows':
        return executable.endswith('.exe') and os.path.isfile(executable)
    elif platform.system() == 'Darwin':
        return executable.endswith('.app') and os.path.isdir(executable)
    else:
        return False


def record_steps(name, description, executable, folder_path = 'sources/profiles'):
    #Validate
    name = str(name)
    description = str(description)
    executable = str(executable)

    if not name.strip():
        print("- Empty name")
        return [1,'Empty name']

    if any(file_name == name+'.json' for file_name in os.listdir(folder_path)):
        print(f"- '{name}' already exist '{folder_path}'.")
        return [2,str(name) + " already exist " + str(folder_path) + "."]

    if not os.path.isfile(executable):
        print(f"- '{executable}' doesn't exists.")
        return [3,str(executable) + " doesn't exists."]
    if not is_executable_valid(executable):
        print(f"'{executable}' is not a valid executable.")
        return [4,str(executable) + " is not a valid executable."]

    #Execution
    filename = folder_path + '/' + name + '.json'

    recorder = EventRecorder()
    recorder.main(filename, name, description, executable)
    return [5, 'Success saving!']

