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

    def songTitle():
        lQ = client.queue(client.queues_list()[0].id)
        last_track_id = lQ.get_current_track()
        last_track = last_track_id.fetch_track()
        return last_track.title

    def songArtist():
        lQ = client.queue(client.queues_list()[0].id)
        lQid = lQ.get_current_track()
        last_track = lQid.fetch_track()
        return ', '.join(last_track.artists_name())
    
    def songLink():
        lQ = client.queue(client.queues_list()[0].id)
        lQid = lQ.get_current_track()
        lQlt = lQid.fetch_track()
        return f"https://music.yandex.ru/album/{lQlt['albums'][0]['id']}/track/{lQlt['id']}/"
        
    def songID():
        lQ = client.queue(client.queues_list()[0].id)
        return lQ.get_current_track()

    def songImage():
        queues = client.queues_list()
        lQ = client.queue(queues[0].id)
        lQid = lQ.get_current_track()
        lQlt = lQid.fetch_track()
        return "https://" + lQlt.cover_uri.replace("%%", "1000x1000")