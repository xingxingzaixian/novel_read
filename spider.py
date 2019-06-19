# encoding: utf-8
"""
@version: 1.0
@author: 
@file: spider
@time: 2019-06-02 17:43
@desc: 爬取小说章节内容并保存到数据库
"""
import requests
from lxml import etree
import chardet
from db_api import DbApi

class CollectNovels:
    def __init__(self, url):
        self.session = requests.session()
        self.session.headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"

        self.db = DbApi()

        self.url = url
        self.chapter_id = -1

    def get_chapters(self):
        r = self.session.get(url)
        r.encoding = chardet.detect(r.content).get("encoding", "utf-8")
        html = etree.HTML(r.text)
        for item in html.xpath("//dl/dd/a"):
            yield url + item.attrib["href"]

    def get_content(self, url):
        # 如果已经爬取了，就不再爬取
        crawled, chapter_id = self.db.has_chapter_crawl(url)
        if crawled:
            self.chapter_id = chapter_id
            return

        r = self.session.get(url)
        r.encoding = chardet.detect(r.content).get("encoding", "utf-8")
        html = etree.HTML(r.text)
        title = html.xpath(r'//*[@class="bookname"]/h1')[0].text
        print(title)
        for info in html.xpath("//div[@id='content']"):
            text = info.xpath("string(.)")
            self.chapter_id += 1
            self.db.save_content(title, text.strip(), url, self.chapter_id, self.url)

    def run(self):
        for href in self.get_chapters():
            self.get_content(href)

    def __del__(self):
        self.db.release()
        print("del")

if __name__ == '__main__':
    url = "https://www.biquge.info/40_40289/"
    obj = CollectNovels(url)
    obj.run()