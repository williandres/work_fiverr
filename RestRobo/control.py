import play
import open
import save
import os
import subprocess
import platform

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
        return 'Fail'

    if any(file_name == name+'.json' for file_name in os.listdir(folder_path)):
        print(f"- '{name}' already exist '{folder_path}'.")
        return 'Fail'

    if not os.path.isfile(executable):
        print(f"- '{executable}' doesn't exists")
        return 'Fail'
    if not is_executable_valid(executable):
        print(f"El archivo '{executable}' no es un ejecutable válido.")
        return 'Fail'

    #
    return 'Succes'
