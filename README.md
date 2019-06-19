# 小说阅读器

## spider
爬取指定小说章节内容，保存至sqlite3数据库

## composite
调用百度语音合成API，合成语音数据保存至数据库

## player
读取章节内容，解析后从语音合成数据库中取出语音数据，使用pygame库播放

- *novel_chapter*：记录小说章节文字内容
- *novel_name*：要爬取的小说名和小说首页地址
- *novel_read*：记录合成的语音数据
- *novel_schedule*：记录本次播放进度

#### 后期计划
后期再增加前端页面，通过页面来增加爬取小说信息。可以展示小说播放进度、合成进度。

---
![公众号](https://upload-images.jianshu.io/upload_images/9101119-d69e29ae475ea954.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)