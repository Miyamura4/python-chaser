import threading
import time
import win32gui
import win32con
from threading import Thread
import pyautogui

pic = pyautogui.screenshot()
print("Hello guys. Thats my python chase program.")


def whilfix(delad):
    a = {}
    k = 0
    png2 = '.png'
    while k < 1000:
        time.sleep(delad)
        pic = pyautogui.screenshot()
        pic.save(str(k) + png2)
        print("screnshot saved")
        k += 1


def windowEnumHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


def bringToFront(window_name):
    top_windows = []
    win32gui.EnumWindows(windowEnumHandler, top_windows)
    for i in top_windows:
        # print(i[1])
        if window_name.lower() in i[1].lower():
            # print("found", window_name)
            win32gui.ShowWindow(i[0], win32con.SW_SHOWMAXIMIZED)
            win32gui.SetForegroundWindow(i[0])
            break


def mains(prog1, pidors):
    while True:
        time.sleep(pidors)
        pyautogui.press("alt")
        bringToFront(prog1)


def pidor(prog2, gandons):
    while True:
        time.sleep(gandons)
        pyautogui.press("alt")
        bringToFront(prog2)


#def gandon(prog3):
# while True:
# df = input("Select a delay in seconds: ")
# pyautogui.press("alt")
# bringToFront(prog3)
# time.sleep(df)
# pic = pyautogui.screenshot()
#  pic.save('1.png')


das = input("Enter a window count(maximum 2): ")
das = int(das)

if das < 2:
    prog1 = input("Enter window name: ")
    pidors = input("Enter delay(in seconds): ")
    dass = input("screenshot save delay: ")
    pidors = int(pidors)
    wf = threading.Thread(target=whilfix, args=([dass]), name='sds')
    wf.start()
    thr = threading.Thread(target=mains, args=(prog1, pidors), name='pidorsdad')
    thr.start()
else:
    prog1 = input("Enter window 1 name: ")
    prog2 = input("Enter window 2 name: ")
    pidorss = input("Enter window 1 delay(in seconds): ")
    gandonss = input("Enter window 2 delay(in seconds): ")
    delad = input("screenshot save delay: ")
    pidorss = int(pidorss)
    delad = int(delad)
    gandonsg = int(gandonss)
    wf = threading.Thread(target=whilfix, args=([delad]), name='sds')
    wf.start()
    thr = threading.Thread(target=mains, args=(prog1, pidorss), name='pidor')
    thr.start()
    tdr = threading.Thread(target=pidor, args=(prog2, gandonsg), name='pidorsda')
    tdr.start()
