from configparser import ConfigParser
from yandex_music import Client
from modules.getToken import token
from PyQt6.QtWidgets import QMessageBox

config = ConfigParser()

config.read('info/config.ini')

if len(config.get("main","ym")) <= 2:
    print("[Яндекс Музыка] Замечен первый запуск, для работы приложения войдите в аккаунт яндекса, в открывшемся окне.")
    config.set("main", "ym", token.get_token())
    print("[Яндекс Музыка] Успешный запуск")
    with open("info/config.ini", "w") as config_file:
        config.write(config_file)
    
    client = Client(config.get("main", "ym")).init()
else:
    print("[Яндекс Музыка] Успешный запуск")
    client = Client(config.get("main", "ym")).init()


class MYAPI:
    def ForceUpdateToken():
        config.set("main", "ym", token.get_token())
        print("[Яндекс Музыка] Успешный запуск")
        with open("info/config.ini", "w") as config_file:
            config.write(config_file)
            
        client = Client(config.get("main", "ym")).init()

    def get_current_track():
        queue = client.queues_list()
        if len(queue) == 0:
            raise "nothing playing"

        queue = client.queue(queue[0].id)
        if queue.context.id == 'user:onyourwave':
            return {
                "title" : "Моя волна",
                "link" : None,
                "image" : "https://github.com/maj0roff/YandexMusicDiscordRPC/raw/main/fallback-black_2.gif",
                "id" : "wave",
                "artist" : None
            }
            
        track = queue.get_current_track().fetch_track()

        return {
            "title" : track.title,
            "link" : f"https://music.yandex.ru/album/{track['albums'][0]['id']}/track/{track['id']}/",
            "image" : f"https://{track.cover_uri.replace('%%', '1000x1000')}",
            "id" : track.id,
            "artist" : ", ".join(track.artists_name())
        }


