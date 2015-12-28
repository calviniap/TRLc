#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import os
from flask import render_template,url_for,redirect,session
from app.config import *
from app.Views import Views
from flask import url_for
import time
import json
from werkzeug.security import generate_password_hash,check_password_hash
from peewee import *
from app.Model import *

views=Views()
db = SqliteDatabase(appConfig.dbname)
from flask import make_response

class USER(Model):
    id=IntegerField(200)
    name = CharField(unique=True)
    password = CharField(200)
    qq=IntegerField(unique=True)
    signature = CharField()
    coin=IntegerField()
    level=IntegerField()
    Ban=IntegerField()
    class Meta:
        database = db

class CONFIG(Model):
    name=CharField()
    url=CharField()
    canregister=IntegerField()
    serveronline=IntegerField()
    class Meta:
        database = db

if(os.path.exists(appConfig.dbname)):
    db = SqliteDatabase(appConfig.dbname)
else:
    db = SqliteDatabase(appConfig.dbname)
    #USER.create_table()
    db.execute_sql('''
    CREATE TABLE "USER" (
    "ID"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "NAME"  TEXT NOT NULL,
    "PASSWORD"  TEXT NOT NULL,
    "QQ"  INT NOT NULL,
    "signature"  TEXT,
    "COIN"  INTEGER NOT NULL  DEFAULT 0,
    'level' INTEGER NOT NULL  DEFAULT 0,
    'Ban' INTEGER NOT NULL  DEFAULT 0,
    UNIQUE ("NAME"),
    UNIQUE ("QQ")
    );
    ''')

    db.execute_sql('''
    CREATE TABLE "CONFIG" (
    "ID"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "NAME"  TEXT NOT NULL,
    "URL"  TEXT NOT NULL,
    'canregister' INTEGER NOT NULL  DEFAULT 0,
    'serveronline' INTEGER NOT NULL  DEFAULT 0
    );
    ''')
    db.execute_sql("INSERT INTO CONFIG (NAME,URL) VALUES ('NAME','URL')")

class user:
    def add(self,name,password,qq,signature):
        if(CONFIG.select().where(CONFIG.id==1)):
            for data in CONFIG.select().where(CONFIG.id==1):
               if(data.canregister !=1):
                   return ("對不起！本站已關閉新成員注冊.")
        password=generate_password_hash(password)
        if(USER.select().where(USER.name==name)):
            return "用戶已存在"
        if(USER.select().where(USER.qq==qq)):
            return "QQ號碼重復"
        USER.insert(name=name,password=password,qq=qq,signature=signature).execute()
        session['registered']=True
        return ("注冊完成")

    def del_(self,id):
        USER.delete().where(USER.id == id).execute()
        return '1'

    def edit(self,id,qq,signature,coin):
        USER.update(qq=qq,signature=signature,coin=coin).where(USER.id == id).execute()
        return '1'

    def getbyid(self,id,m):
        for data in USER.select().where(USER.id==id):
            if(m=='id'):
                return str(data.id)
            if(m=='name'):
                return data.name
            if(m=='password'):
                return data.password
            if(m=='qq'):
                return str(data.qq)
            if(m=='signature'):
                return data.signature
            if(m=='coin'):
                return str(data.coin)
            return ("沒有找到")

    def getbyname(self,name,m):
        for data in USER.select().where(USER.name==name):
            if(m=='id'):
                return str(data.id)
            if(m=='name'):
                return data.name
            if(m=='password'):
                return data.password
            if(m=='qq'):
                return str(data.qq)
            if(m=='signature'):
                return data.signature
            if(m=='coin'):
                return str(data.coin)
            return ("沒有找到")

    def getalluser(self):
        dictList = []
        for data in USER.select():
             dict = {
                "ID":data.id,
                "NAME":data.name,
                "QQ":data.qq,
                "signature":data.signature,
                "COIN":data.coin,
                }
             dictList.append(dict)

        return MODEL.UI('wanjiaziliao.html','用戶列表',dictList)
