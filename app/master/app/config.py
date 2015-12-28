#!/usr/bin/python
# -*- coding: utf-8 -*-
class appConfig:
    import socket
    dk=0     # 如果服務器不是80端口，請設此為1,url將等于下方，否則設此為0。
    url ="http://125.65.110.179:45679"
    APPPASS='1034'  #終級密碼
    APPNAME='TRLc'
    dbname='db.sqlite' #APP數據庫路徑
    tshock_dbname='TSHOCK/tshock/tshock.sqlite'  #Tshock數據庫路徑
    me = {"user":'user', "admin":'admin', "superadmin":'superadmin'}
