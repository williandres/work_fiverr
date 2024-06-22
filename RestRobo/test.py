import os
import subprocess
import platform
import time
from pynput import mouse
from pynput.mouse import Button, Controller

def on_move(x, y):
    pass
    # print('Pointer moved to {0}'.format(
    #     (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        # return False
        pass

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
    return False

#
##
###
####
####
###
##
#

def get_applications_linux():
    paths = ['/usr/bin', '/usr/local/bin']
    apps = []
    for path in paths:
        if os.path.exists(path):
            apps.extend(os.listdir(path))
    return sorted(set(apps))

def get_applications_windows():
    start_menu = os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs')
    apps = []
    for root, dirs, files in os.walk(start_menu):
        for file in files:
            if file.endswith('.lnk'):
                apps.append(file.replace('.lnk', ''))
    return sorted(set(apps))

def get_applications_macos():
    path = '/Applications'
    apps = [app for app in os.listdir(path) if app.endswith('.app')]
    return sorted(set(apps))

def open_application(app_name):
    system = platform.system()
    try:
        if system == 'Linux':
            # Abrir la aplicación y ponerla en pantalla completa
            proc = subprocess.Popen([app_name])
            time.sleep(5)  # Esperar un segundo para que la aplicación se inicie
            subprocess.run(['wmctrl', '-r', app_name, '-b', 'add,fullscreen'])
        elif system == 'Windows':
            # Abrir la aplicación y maximizar la ventana
            proc = subprocess.Popen(['start', app_name], shell=True)
            time.sleep(5)  # Esperar un segundo para que la aplicación se inicie
            script = f"""
            $app = Get-Process | Where-Object {{ $_.MainWindowTitle -like "*{app_name}*" }}
            $hwnd = $app.MainWindowHandle
            $null = [void][System.Runtime.InteropServices.Marshal]::GetType("System.Object")
            Add-Type @"
            using System;
            using System.Runtime.InteropServices;
            public class User32 {{
                [DllImport("user32.dll", SetLastError=true)]
                public static extern bool ShowWindowAsync(IntPtr hWnd, int nCmdShow);
            }}
            "@
            [User32]::ShowWindowAsync($hwnd, 3)  # 3 = SW_MAXIMIZE
            """
            subprocess.run(["powershell", "-Command", script], check=True)
        elif system == 'Darwin':
            # Abrir la aplicación y maximizar la ventana
            proc = subprocess.run(['open', f'/Applications/{app_name}'], check=True)
            time.sleep(1)  # Esperar un segundo para que la aplicación se inicie
            script = f"""
            tell application "{app_name.replace('.app', '')}"
                activate
                tell application "System Events" to keystroke "f" using {{"control down", "command down"}}
            end tell
            """
            subprocess.run(["osascript", "-e", script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al intentar abrir {app_name}: {e}")
    except FileNotFoundError:
        print(f"{app_name} no está instalado o no se encontró en el PATH.")

def save_applications_to_file(apps, filename):
    with open(filename, 'w') as file:
        for i, app in enumerate(apps):
            file.write(f"{i + 1}. {app}\n")
    print(f"Lista de aplicaciones guardada en {filename}")

def main():
    system = platform.system()
    if system == 'Linux':
        apps = get_applications_linux()
    elif system == 'Windows':
        apps = get_applications_windows()
    elif system == 'Darwin':
        apps = get_applications_macos()
    else:
        print(f"Sistema operativo no soportado: {system}")
        return

    filename = "applications_list.txt"
    save_applications_to_file(apps, filename)

    choice = 1949  # Este valor debería ser reemplazado por la selección del usuario
    app_name = apps[choice - 1]
    print('Abriendo ', app_name)
    open_application(app_name)

if __name__ == "__main__":
    main()
    mouse = Controller()
    mouse.position = (46, 284)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(2)
    mouse.position = (49, 514)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(2)
    mouse.position = (224, 350)
    mouse.press(Button.left)
    mouse.release(Button.left)
# # Collect events until released
#     with mouse.Listener(
#             on_move=on_move,
#             on_click=on_click,
#             on_scroll=on_scroll) as listener:
#         listener.join()

#     # ...or, in a non-blocking fashion:
#     listener = mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll)
# listener.start()