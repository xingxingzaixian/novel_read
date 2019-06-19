# encoding: utf-8
"""
@version: 1.0
@author: 
@file: composite
@time: 2019-06-15 22:42
@desc: 调用百度语音合成API合成数据
"""
from aip import AipSpeech
from requests.exceptions import ChunkedEncodingError
from db_api import DbApi

class NovelSpeak:
    def __init__(self):
        self.db = DbApi()

        """ 你的 APPID AK SK """
        APP_ID = '16416498'
        API_KEY = 'oEWGafQkaUGqmsmPbfkE5OMx'
        SECRET_KEY = '6jdsUcH0PXz5TYoELU47u58W5vPV9lwf'
        self.client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def run(self):
        while True:
            try:
                text, id_ = self.db.get_translate_info()
                print(id_)
                for line in text.split("。"):
                    content = self.client.synthesis(line.strip(), 'zh', 1, {"per": 0})
                    if not isinstance(content, dict):
                        self.db.save_voice_data(line.strip(), content)
            except ChunkedEncodingError as e:
                print(e)
            else:
                self.db.save_translate_schedule(id_)

    def __del__(self):
        self.db.release()

if __name__ == '__main__':
    obj = NovelSpeak()
    obj.run()