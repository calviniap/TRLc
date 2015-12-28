#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import request,redirect,url_for,session,abort,flash,render_template,make_response
from io import *
from flask.ext.script import Manager
from PythonServerRun import app
from app.Model import MODEL
from app.Views import Views
from app.config import *
from app.conn import *
import json
import datetime
import random
import urllib.request
from werkzeug.security import generate_password_hash,check_password_hash
from flask_bootstrap import Bootstrap
from flask import jsonify


u=user()
views=Views()
manager = Manager(app)
app.secret_key =(b'\xfd^\x0eGL\n\x02\xb8J\x90\xae\xfe\xa2Alf\xc7\xa8w\xa6-z\x89\t')

def create_app():
  Bootstrap(app)
  return app

@manager.command
@app.route('/')
@app.route('/index')
@app.route('/index/')
def index():
    if(session.get('me')!=appConfig.me['user'] and session.get('me')!=appConfig.me['admin'] and session.get('me')!=appConfig.me['superadmin']):
        data=MODEL.UI('login.html','Login')
        return views.put(data)
    data=MODEL.UI('index.html',appConfig.APPNAME)
    return views.put(data)

@app.route('/getmybox', methods=['GET', 'POST'])
def getmybox():
    return 'ID:'+str(session.get('id'))+'&nbsp;|&nbsp;NAME:'+str(session.get('name'))+'&nbsp;|&nbsp;QQ:'+str(session.get('QQ'))+'&nbsp;|&nbsp;等級:'+str(session.get('level'))+'&nbsp;|&nbsp;方幣:'+str(session.get('COIN'))+'&nbsp;&nbsp;<br>簽名:<p>'+str(session.get('signature'))+'</p>'



@app.route('/getnew', methods=['GET', 'POST'])
def getnew():
    if(USER.select().where(USER.name==session.get('name'))):
        for user in USER.select().where(USER.name==session.get('name')):
            session['id']=user.id
            session['name']=user.name
            session['password']=user.password
            session['QQ']=user.qq
            session['signature']=user.signature
            session['COIN']=user.coin
            session['level']=user.level
            session['ban']=user.Ban
        return 'success'


@app.route('/checklog', methods=['GET', 'POST'])
def checklog():
    username=request.form['username']
    userpass=request.form['userpass']
    if(username==''):
        return ("用戶名不能為空！")
    if(userpass==''):
        return ("密碼不能為空！")
    if(USER.select().where(USER.name==username)):
        for user in USER.select().where(USER.name==username):
            if(check_password_hash(user.password,userpass)):
                session['id']=user.id
                session['name']=user.name
                session['QQ']=user.qq
                session['signature']=user.signature
                session['COIN']=user.coin
                session['level']=user.level
                session['ban']=user.Ban
                if(user.level==3):
                    session['me']=appConfig.me['superadmin']
                elif(user.level==2):
                    session['me']=appConfig.me['admin']
                elif(user.level==1):
                    session['me']=appConfig.me['user']
                else:
                    session.pop('me', None)
                return ("歡迎回來!")
            return ("密碼錯誤！")
    return ("沒有這個用戶！")

@app.route('/out')
def out():
    session.pop('me', None)
    if(appConfig.dk==1):
        return redirect(appConfig.url)
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/user')
@app.route('/user/')
@app.route('/user/<username>')
def user(username):
    return username

@app.route('/admin')
@app.route('/admin/')
def admin():
    if(session.get('me')==appConfig.me['superadmin']):
        data=MODEL.UI('admin.html')
        return views.put(data)
    return ''

@app.route('/getlog/<log>')
def getlog(log):
    f=open('TSHOCK/tshock/'+log,"r")
    return f.read()
    f.close()

@app.route('/user_add/<name>/<qq>/<signature>')
def user_add(name,qq,signature):
    return u.add(name,qq,signature)

@app.route('/user_del/<id>')
def user_del(id):
    return (u.del_(id))

@app.route('/user_edit/<id>/<qq>/<signature>/<coin>')
def user_edit(id,qq,signature,coin):
    return u.edit(id,qq,signature,coin)

@app.route('/getuserbyid/<id>/<m>')
def getuserbyid(id,m):
    return u.getbyid(id,m)

@app.route('/getuserbyname/<name>/<m>')
def getuserbyname(name,m):
    return u.getbyname(name,m)

@app.route('/getalluser')
def getalluser():
    return u.getalluser()


@app.route('/register')
def register():
    data=MODEL.register('register.html')
    return views.put(data)

@app.route('/register_get',methods=['GET', 'POST'])
def register_get():
    if(session.get('registered')==True):
        return ("你已經有自己的賬號了")
    username=request.form['username'].replace('/','').replace('<','').replace('>','').replace('%','')
    userpass=request.form['userpass'].replace('/','').replace('<','').replace('>','').replace('%','')
    qq=request.form['qq'].replace('/','').replace('<','').replace('>','').replace('~','')
    signature=request.form['signature'].replace('/','').replace('<','').replace('>','').replace('%','').replace('&','').replace(';','')
    if(username !='' and userpass !='' and  signature !=''):
        return u.add(username,userpass,qq,signature)

@app.route('/clearregistered')
def clearregistered():
    session['registered']=False
    return ("OK")

@app.route('/menu/<type>')
def menu(type):
    if(type=='server'):
        data=MODEL.tab_server('tab/server.html')
    if(type=='group'):
        data=MODEL.tab_group('tab/group.html')
    if(type=='player'):
        data=MODEL.UI('tab/player.html')
    if(type=='item'):
        data=MODEL.UI('tab/item.html')
    if(type=='Projectile'):
        data=MODEL.UI('tab/Projectile.html')
    if(type=='block'):
        data=MODEL.UI('tab/block.html')
    if(type=='lindi'):
        data=MODEL.UI('tab/lindi.html')
    if(type=='howse'):
        data=MODEL.UI('tab/howse.html')
    if(type=='tpa'):
        data=MODEL.UI('tab/tpa.html')
    if(type=='wanjiaziliao'):
        data=MODEL.UI('tab/wanjiaziliao.html')
    if(type=='user'):
        data=MODEL.tab_user('tab/user.html')
    return views.put(data)

@app.route('/save/<a>/<b>',methods=['GET', 'POST'])
def save(a,b):
    if(a=='server'):
        if(b=='server_name'):
            server_name=request.form['server_name']
            CONFIG.update(name=server_name).where(CONFIG.id==1).execute()
            return '成功!'
        if(b=='server_url'):
            server_url=request.form['server_url']
            CONFIG.update(url=server_url).where(CONFIG.id==1).execute()
            return '成功!'
        if(b=='canregister'):
            canregister=request.form['canregister']
            CONFIG.update(canregister=canregister).where(CONFIG.id==1).execute()
            return '成功!'
        if(b=='serveronline'):
            serveronline=request.form['serveronline']
            CONFIG.update(serveronline=serveronline).where(CONFIG.id==1).execute()
            return '成功!'

@app.route('/edituser/<a>',methods=['GET', 'POST'])
def edituser(a):
    id=request.form['id']
    if a == 'selectlevel':
        level=request.form['level']
        USER.update(level=level).where(USER.id==id).execute()
        return 'success'
    elif a == 'selectban':
        ban=request.form['ban']
        USER.update(Ban=ban).where(USER.id==id).execute()
        return 'success'
    elif a == 'QQ':
        QQ=request.form['QQ']
        USER.update(qq=QQ).where(USER.id==id).execute()
        return 'success'
    elif a == 'signature':
        signature=request.form['signature']
        USER.update(signature=signature).where(USER.id==id).execute()
        return 'success'
    elif a == 'COIN':
        COIN=request.form['COIN']
        USER.update(coin=COIN).where(USER.id==id).execute()
        return 'success'




@app.route('/test',methods=['GET', 'POST'])
def test():
    return  ''



if __name__ == "__main__":
    manager.run()
