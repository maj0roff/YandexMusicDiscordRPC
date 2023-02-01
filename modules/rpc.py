from configparser import ConfigParser
from pypresence import Presence

config = ConfigParser()

config.read('info/config.ini')

dRPC = Presence(client_id=config.get('main', 'dsappid'))


class MRPC:
    def connect():
        dRPC.connect()
    def mywavePresence():
        dRPC.update(
            details="Моя волна",
            large_image="https://github.com/maj0roff/YandexMusicDiscordRPC/blob/main/mywave.png?raw=true",
            small_image="https://github.com/maj0roff/YandexMusicDiscordRPC/blob/main/logo.png?raw=true",
            large_text=f"Слушает мою волну"
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
