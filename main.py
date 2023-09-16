from pyautogui import *
import subprocess
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import subprocess
def process_exists(process_name):
    progs = str(subprocess.check_output('tasklist'))
    if process_name in progs:
        return True
    else:
        return False

if process_exists('nest.exe'):
    print("radi")
else:
    subprocess.Popen('E:\\Ninja Legends\\Ninja Legends.exe')
    sleep(2)
    click(1303,115)
    sleep(0.5)
    click(1100,830)
    sleep(0.5)
    click(895,367)
    sleep(0.5)
    click(1637,881)
    sleep(1)
    click(1625,230)


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
count=0
sleep(3)
click(96,556)
sleep(0.5)
click(644,257)
sleep(0.5)
while pyautogui.locateOnScreen('srca.png',confidence=0.8)==None:
    while keyboard.is_pressed('q') == False:
        if(count<1):
            click(1855,89)
            click(1855,89)
        click(392,818)
        sleep(1)
        click(1125,591)
        sleep(1)
        click(1119,890)
        sleep(1)
        click(1119,890)
        sleep(1)
        click(1116,590)
        sleep(1)
        click(1349,341)
        sleep(1)
        click(1362,884)
        sleep(1)
        click(1349,341)
        sleep(1)
        click(1832,600)
        sleep(1)
        click(96,556)
        sleep(0.5)
        click(644,257)
        sleep(0.5)
        if count==2:
            click(1329,975)
            sleep(0.5)
            click(945,711)
            sleep(0.5)
        click(495,509)
        sleep(0.5)
        click(897,372)
        sleep(0.5)
        click(1323,368)
        sleep(0.5)
        print(count)
        while pyautogui.locateOnScreen('claim1.png',confidence=0.8,grayscale=True)== None:
            click(945,711)
            print("napadam")
            sleep(3)
       
        print("kraj misije")
        click(961,803)
        count=count+1
        sleep(3)
        """
        if pyautogui.locateOnScreen('lvlup.png')!= None:
            click(1879,799)
            print("Level up")
            sleep(3)
            count=count+1
        else:
            count=count+1
            print("agane")
