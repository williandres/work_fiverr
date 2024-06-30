import os
import subprocess
import platform
import time

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

def open_application(app_name, is_path=False):
    system = platform.system()
    try:
        if system == 'Linux':
            if is_path:
                proc = subprocess.Popen([app_name])
            else:
                proc = subprocess.Popen([app_name])
            time.sleep(25)
            print('Full screen')
            subprocess.run(['wmctrl', '-r', app_name, '-b', 'add,fullscreen'])
        elif system == 'Windows':
            if is_path:
                proc = subprocess.Popen([app_name], shell=True)
            else:
                proc = subprocess.Popen(['start', app_name], shell=True)
            time.sleep(5)  
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
            if is_path:
                proc = subprocess.run(['open', app_name], check=True)
            else:
                proc = subprocess.run(['open', f'/Applications/{app_name}'], check=True)
            time.sleep(1)  
            script = f"""
            tell application "{app_name.replace('.app', '')}"
                activate
                tell application "System Events" to keystroke "f" using {{"control down", "command down"}}
            end tell
            """
            subprocess.run(["osascript", "-e", script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error {app_name}: {e}")
    except FileNotFoundError:
        print(f"{app_name} is not installed or was not found in the PATH.")

def save_applications_to_file(apps, filename):
    with open(filename, 'w') as file:
        for i, app in enumerate(apps):
            file.write(f"{i + 1}. {app}\n")

def main():
    system = platform.system()
    if system == 'Linux':
        apps = get_applications_linux()
    elif system == 'Windows':
        apps = get_applications_windows()
    elif system == 'Darwin':
        apps = get_applications_macos()
    else:
        print(f"Unsupported system: {system}")
        return

    save_applications_to_file(apps, "applications_list.txt")

    #1949
    choice = '1949'

    try:
        choice_num = int(choice)
        app_name = apps[choice_num - 1]
        print('Opening... ', app_name)
        open_application(app_name)
    except ValueError:
        app_path = choice
        print('Opening executable... ', app_path)
        open_application(app_path, is_path=True)

if __name__ == "__main__":
    pass
    #main()
