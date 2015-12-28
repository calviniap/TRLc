/*
Navicat SQLite Data Transfer

Source Server         : D
Source Server Version : 30808
Source Host           : :0

Target Server Type    : SQLite
Target Server Version : 30808
File Encoding         : 65001

Date: 2015-12-06 11:22:55
*/

PRAGMA foreign_keys = OFF;

-- ----------------------------
-- Table structure for USER
-- ----------------------------
DROP TABLE IF EXISTS "main"."USER";
CREATE TABLE "USER" (
"ID"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
"NAME"  TEXT NOT NULL,
"QQ"  INTEGER NOT NULL,
"MAIL"  VACHAR NOT NULL,
"COIN"  INTEGER NOT NULL DEFAULT 0
);
