#!/usr/bin/env python

import psycopg2

class Log:
    dbIPaddress = 'localhost'
    dbname = 'tank'
    user = 'tank'
    password = 'skinner2'
    dbconn = psycopg2.extensions.connection
    dbCur = psycopg2.extensions.cursor
    
    sensorid = ''
    ip = '0.0.0.0'
    rssi = '0'
    freemem = '0'
    resthost = ''
    logtext = ''

    # __file = uio.open("tank.log", "a", encoding="utf-8")
    # __output = uio.StringIO()

    def __init__(self):
        self.dbconn = psycopg2.connect(host = self.dbIPaddress, dbname = self.dbname, user = self.user, password = self.password)
        self.dbconn.autocommit = True
        self.dbCur = self.dbconn.cursor()

    def __call__(self):
        self.dbconn = psycopg2.connect(host = self.dbIPaddress, dbname = self.dbname, user = self.user, password = self.password)
        self.dbconn.autocommit = True
        self.dbCur = self.dbconn.cursor()

    def setLogEntry(self):
        sql = "insert into log (sensorid, ip, rssi, freemem, resthost, text) values( '{0}', '{1}', {2}, {3}, '{4}', '{5}' )"
        sql = sql.replace('{0}',  self.sensorId)
        sql = sql.replace('{1}',  self.ip)
        sql = sql.replace('{2}',  str(self.rssi))
        sql = sql.replace('{3}',  str(self.freemem))
        sql = sql.replace('{4}',  self.resthost)
        sql = sql.replace('{5}',  self.logtext)
        
        print(sql)
        
        self.dbCur.execute(sql)


