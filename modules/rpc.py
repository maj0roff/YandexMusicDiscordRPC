from configparser import ConfigParser
from pypresence import Presence

config = ConfigParser()

config.read('info/config.ini')

dRPC = Presence(client_id=config.get('main', 'dsappid'))
dRPC.connect()

class MRPC:
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
