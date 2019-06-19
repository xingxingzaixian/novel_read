/*
 Navicat Premium Data Transfer

 Source Server         : 小说阅读
 Source Server Type    : SQLite
 Source Server Version : 3012001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3012001
 File Encoding         : 65001

 Date: 15/06/2019 22:16:34
*/

-- ----------------------------
-- Table structure for novel_chapter
-- ----------------------------
DROP TABLE IF EXISTS "novel_chapter";
CREATE TABLE "novel_chapter" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "title" text, --章节名称
  "chapter" text,  --章节地址
  "content" text,  --章节内容
  "flag" integer DEFAULT 0,  --是否已经翻译
  "chapter_id" integer,  --章节顺序ID
  "novel_url" text  --小说首页地址
);

-- ----------------------------
-- Table structure for novel_name
-- ----------------------------
DROP TABLE IF EXISTS "novel_name";
CREATE TABLE "novel_name" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" text NOT NULL, --小说名
  "url" text NOT NULL   --小说首页地址
);

-- ----------------------------
-- Table structure for novel_read
-- ----------------------------
DROP TABLE IF EXISTS "novel_read";
CREATE TABLE "novel_read" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "text" text, --合成文字
  "content" blob DEFAULT '' --合成音频内容
);

-- ----------------------------
-- Table structure for novel_schedule
-- ----------------------------
DROP TABLE IF EXISTS "novel_schedule";
CREATE TABLE "novel_schedule" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" text,   --小说名
  "tag" integer, --小说顺序ID
  "url" text     --小说主页地址
);