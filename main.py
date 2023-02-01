import time
from modules.rpc import MRPC
from modules.yandexmusic import MYAPI

def mainLoop():
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
    mainLoop()
