# encoding: utf-8
"""
@version: 1.0
@author: 
@file: player
@time: 2019-06-15 22:40
"""

import time
import pygame
from io import BytesIO
from db_api import DbApi

class Player:
    def __init__(self, url , **kwargs):
        self.db = DbApi()
        self.volume = kwargs.get("volume", 1.0)
        self.frequency = kwargs.get("frequency", 16000)
        self.pygame_mixer = pygame.mixer
        self.pygame_mixer.init(frequency=self.frequency)
        self.home_url = url

    def run(self):
        self.pygame_mixer.music.set_volume(self.volume)
        self.tag, url = self.db.get_last_chapter(self.home_url)
        while True:
            result = self.db.get_chapter_content(self.tag, self.home_url)
            if result:
                self.tag += 1
                print(result[0])
                content = result[1].strip()
                for line in content.split("。"):
                    voice = self.db.get_voice_data(line.strip())
                    self.play(voice)
            else:
                break

    def play(self, voice):
        try:
            byte_obj = BytesIO()
            byte_obj.write(voice)
            byte_obj.seek(0, 0)
            self.pygame_mixer.music.load(byte_obj)
            self.pygame_mixer.music.play()
            while self.pygame_mixer.music.get_busy():
                time.sleep(0.1)
            self.pygame_mixer.stop()
        except Exception as e:
            print(e)

    def __del__(self):
        self.db.save_play_schedule(self.tag-1, self.home_url)
        self.db.release()

if __name__ == '__main__':
    url = "https://www.biquge.info/40_40289/"
    player = Player(url)
    player.run()