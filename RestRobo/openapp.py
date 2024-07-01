import os
import subprocess
import platform
import time

def open_application(app_name, is_path=False):
    system = platform.system()
    try:
        if system == 'Linux':
            if is_path:
                proc = subprocess.Popen([app_name])
            else:
                proc = subprocess.Popen([app_name])
            time.sleep(3)
            print('Full screen')
            subprocess.run(['wmctrl', '-r', app_name, '-b', 'add,fullscreen'])
        elif system == 'Windows':
            if is_path:
                proc = subprocess.Popen([app_name], shell=True)
            else:
                proc = subprocess.Popen(['start', app_name], shell=True)
            time.sleep(3)  
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
            time.sleep(3)  
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

def main(fileapp):
    open_application(fileapp)


