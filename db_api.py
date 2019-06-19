# encoding: utf-8
"""
@version: 1.0
@author: 
@file: db_api
@time: 2019-06-15 22:39
"""
import os
import sqlite3

class DbApi:
    def __init__(self):
        curdir = os.path.abspath(os.path.dirname(__file__))
        db_path = os.path.join(curdir, "novel.db")
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    # 保存小说章节内容
    def save_content(self, title, text, url, chapter_id, home_url):
        self.cursor.execute("select * from novel_chapter where chapter='%s'" % url)
        if not self.cursor.fetchone():
            self.cursor.execute("insert into novel_chapter(title, chapter, content, chapter_id, novel_url) values (?, ?, ?, ?, ?)", (title, url, text, chapter_id, home_url))
            self.conn.commit()

    # 章节内容是否已经爬取过了
    def has_chapter_crawl(self, url):
        self.cursor.execute("select chapter_id from novel_chapter where chapter='%s'" % url)
        result = self.cursor.fetchone()
        if not result:
            return False, None
        return True, result[0]

    # 获取最近一次播放的章节信息
    def get_last_chapter(self, url):
        self.cursor.execute("select tag, url from novel_schedule where url='%s'" % url)
        result = self.cursor.fetchone()
        if result:
            return result[0], result[1]
        return 0, None

    # 获取章节内容文本内容
    def get_chapter_content(self, tag, home_url):
        # 如果传入的章节地址为空，则取第一个章节进行播放
        if not tag:
            tag = 0
        self.cursor.execute("select title, content from novel_chapter where chapter_id=%s and novel_url='%s'" % (tag, home_url))
        result = self.cursor.fetchone()
        if result:
            return result
        return None

    # 获取文本对应的合成语音数据
    def get_voice_data(self, text):
        self.cursor.execute("select content from novel_read where text='%s'" % text)
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    # 获取需要合成的章节数据
    def get_translate_info(self):
        self.cursor.execute("select id, content from novel_chapter where flag=0")
        result = self.cursor.fetchone()
        if result:
            return result[1], result[0]
        return None, None

    # 保存翻译进度
    def save_translate_schedule(self, id_):
        if id_:
            self.cursor.execute("update novel_chapter set flag=1 where id=%s" % id_)
            self.conn.commit()

    # 保存合成数据
    def save_voice_data(self, line, content):
        self.cursor.execute("select * from novel_read where text='%s'" % line)
        if not self.cursor.fetchone():
            self.cursor.execute("insert into novel_read(text, content) values (?, ?)", (line, sqlite3.Binary(content)))
            self.conn.commit()

    def save_play_schedule(self, tag, home_url):
        if tag:
            self.cursor.execute("update novel_schedule set tag=%d where url='%s'" % (tag, home_url))
            self.conn.commit()

    def release(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()