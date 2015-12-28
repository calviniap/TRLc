#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template, url_for
from app.Views import Views
from app.config import *
from peewee import *

view = Views()
db = SqliteDatabase(appConfig.dbname)
tshockdb = SqliteDatabase('tshock.sqlite')

class CONFIG(Model):
    name = CharField()
    url = CharField()
    canregister = IntegerField()
    serveronline = IntegerField()
    class Meta:
        database = db

class GroupList(Model):
    GroupName = CharField()
    Parent = CharField()
    Commands = CharField()
    ChatColor = CharField()
    Prefix = CharField()
    Suffix = CharField()
    class Meta:
        database = tshockdb

class USER(Model):
    name=CharField()
    password=CharField()
    qq=IntegerField()
    signature=CharField()
    coin=IntegerField()
    level=IntegerField()
    ban=IntegerField()
    class Meta:
        database = db

class MODEL:
    def UI(url, title_='', data=''):  # Flat UI界面
        return render_template(url,
                               title=title_,
                               bootstrapcss =url_for('static', filename='Flat-UI-master/dist/css/vendor/bootstrap/css/bootstrap.min.css'),
                               flatuicss    =url_for('static', filename='Flat-UI-master/dist/css/flat-ui.min.css'),
                               democss      =url_for('static', filename='Flat-UI-master/docs/assets/css/demo.css'),
                               jquery       =url_for('static', filename='Flat-UI-master/dist/js/vendor/jquery.min.js'),
                               videojs      =url_for('static', filename='Flat-UI-master/dist/js/vendor/video.js'),
                               flatuimin    =url_for('static', filename='Flat-UI-master/dist/js/flat-ui.min.js'),
                               application  =url_for('static', filename='Flat-UI-master/docs/assets/js/application.js'),
                               mypath       ='/static',
                               registercss  =url_for('static', filename='style/register.css'),
                               defaultcss   =url_for('static', filename='style/default.css'),
                               stylesheet   =url_for('static', filename='style/stylesheet.css'),
                               datas        =data,  # 傳輸數據
                               )

    def login(self, url):
        return render_template(url, title='Log in')

    def register(url):
        return MODEL.UI(url, 'Register')

    def tab_server(url):
        dictList = []
        for data in CONFIG.select():
            if (data.canregister == 1):
                canregisterchecked = 'checked="checked"'
            else:
                canregisterchecked = ''
            if (data.serveronline == 1):
                serveronlinechecked = 'checked="checked"'
            else:
                serveronlinechecked = ''
            dict = {
                "NAME"               : data.name,
                "URL"                : data.url,
                "CANREGISTER"        : data.canregister,
                "canregisterchecked" : canregisterchecked,
                "serveronlinechecked": serveronlinechecked,
            }
            dictList.append(dict)
        return MODEL.UI(url, '', dictList)

    def tab_group(url):
        dictList = []
        for data in GroupList.select():
            dict = {
                "GroupName": data.GroupName,
                "Parent"   : data.Parent,
                "Commands" : data.Commands,
                "ChatColor": data.ChatColor,
                "Prefix"   : data.Prefix,
                "Suffix"   : data.Suffix,
            }
            dictList.append(dict)
        return MODEL.UI(url, '', dictList)

    def tab_user(url):
        dictList = []
        for data in USER.select():
            if data.level == 1:
                selectlevel1='selected = selected'
            else:
                selectlevel1=''
            if data.level == 2:
                selectlevel2='selected = selected'
            else:
                selectlevel2=''
            if data.level == 3:
                selectlevel3='selected = selected'
            else:
                selectlevel3=''
            if data.ban == 0:
                selectban0='selected = selected'
            else:
                selectban0=''
            if data.ban == 1:
                selectban1='selected = selected'
            else:
                selectban1=''
            dict = {
                "ID"   :data.id,
                "NAME" :data.name,
                "QQ"   :data.qq,
                "signature" :data.signature,
                "COIN" :data.coin,
                "level":data.level,
                "ban"  :data.ban,
                "selectlevel1":selectlevel1,
                "selectlevel2":selectlevel2,
                "selectlevel3":selectlevel3,
                "selectban0":selectban0,
                "selectban1":selectban1,
                }
            dictList.append(dict)

        return MODEL.UI(url,'用戶列表',dictList)
