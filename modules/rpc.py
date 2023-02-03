from configparser import ConfigParser
from pypresence import Presence
from modules.yandexmusic import MYAPI
import time

config = ConfigParser()

config.read('info/config.ini')

dRPC = Presence(client_id=config.get('main', 'ds'))
dRPC.connect()

class MRPC:
    def Clear():
        dRPC.clear()
    def mywavePresence():
        dRPC.update(
            details="Моя волна",
            large_image="https://github.com/maj0roff/YandexMusicDiscordRPC/raw/main/fallback-black_2.gif",
            small_image="https://github.com/maj0roff/YandexMusicDiscordRPC/blob/main/logo.png?raw=true",
            large_text=f"На своей волне"
        )
    def updatePresence(aritst, song, image_link, song_link):
        btns = [
            {
                "label": "Слушать",
                "url": song_link
            },
        ]
        dRPC.update(
            details=song,
            state=aritst,
            large_image=image_link,
            small_image="https://github.com/maj0roff/YandexMusicDiscordRPC/blob/main/logo.png?raw=true",
            large_text=f"{aritst} - {song}",
            buttons=btns
        )

    def ForceUpdate():
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
                #print(f"[Яндекс Музыка] Слушаем {artist} - {song}")
                MRPC.updatePresence(artist, song, image_link, song_link)
        except Exception as e:
            print(e)
            MRPC.mywavePresence()

    def callPresence():
        while True:
            switch = 0
            lasttrack = 0
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
                    #print(f"[Яндекс Музыка] Слушаем {artist} - {song}")
                    MRPC.updatePresence(artist, song, image_link, song_link)
            except Exception as e:
                print(e)
                MRPC.mywavePresence()            
            time.sleep(0.01)