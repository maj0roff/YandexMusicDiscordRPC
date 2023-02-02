import os
from configparser import ConfigParser

config = ConfigParser()
config.read('info/config.ini')
if len(config.get("main","yandexmusictoken")) <= 2:
    print("[Яндекс Музыка] Установка необходимых пакетов.")
    os.system('pip install yandex-music --upgrade')
    os.system('pip install selenium')
    os.system('pip install pypresence')
    os.system('pip install yandex_music')
    os.system('pip install webdriver_manager')
    os.system('pip install keyboard')
    os.system('pip install pywin32')
    os.system('pip install win32co')

import time
from modules.rpc import MRPC
from modules.yandexmusic import MYAPI
from threading import Thread
import keyboard
import win32gui, win32con

isHidden = 0
def windowControl_HideShow():
    hwnd = win32gui.GetForegroundWindow()
    global isHidden
    if isHidden == 0:
        isHidden = 1
        #print(isHidden)
        win32gui.ShowWindow(hwnd , win32con.SW_HIDE)
    elif isHidden == 1:
        isHidden = 0
        #print(isHidden)
        win32gui.ShowWindow(hwnd , win32con.SW_SHOW)
    
def windowControl():
    keyboard.add_hotkey("ctrl+f9", windowControl_HideShow)
        

def app():
    print("[Яндекс Музыка] Для того что-бы скрыть или показать окно консоли нажмите Ctrl+F9")
    switch = 0
    lasttrack = 0
    while True:
        try:
            songid = MYAPI.songID()
            artist = MYAPI.songArtist()
            song = MYAPI.songTitle()
            image_link = MYAPI.songImage()
            song_link = MYAPI.songLink()
            if songid != lasttrack:
                lasttrack = songid
                switch = 1
            if switch == 1:
                switch = 0
                print(f"[Яндекс Музыка] Слушаем {artist} - {song}")
                MRPC.updatePresence(artist, song, image_link, song_link)
        except Exception as e:
            #print(e)
            MRPC.mywavePresence()            
        time.sleep(0.01)

if __name__ == "__main__":
    t1 = Thread(target=app)
    t2 = Thread(target=windowControl)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
