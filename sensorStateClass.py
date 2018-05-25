#!/usr/bin/env python3

import psycopg2

class sensorState:
    dbIPaddress = 'localhost'
    dbname = 'tank'
    user = 'tank'
    password = 'skinner2'
    dbconn = psycopg2.extensions.connection
    dbCur = psycopg2.extensions.cursor
    
    sensorId = 0
    sendorIp = '0.0.0.0'
    rssi = 0
    sensorType = ''
    sensorValue = 0.0
    sensormedium = ''
    sensorprovider = ''

    def __init__(self):
        self.dbconn = psycopg2.connect(host = self.dbIPaddress, dbname = self.dbname, user = self.user, password = self.password)
        self.dbconn.autocommit = True
        self.dbCur = self.dbconn.cursor()
        
        #self.getStatus()

    def __call__(self):
        self.dbconn = psycopg2.connect(host = self.dbIPaddress, dbname = self.dbname, user = self.user, password = self.password)
        self.dbconn.autocommit = True
        self.dbCur = self.dbconn.cursor()

    def getStatus(self,  sensorId):
        self.sensorId = sensorId
        
        sql = "select * from sensorStatus where sensorid = '{0}'".replace('{0}',  self.sensorId)
        self.dbCur.execute(sql)
        rows = self.dbCur.fetchall()
        
        for row in rows:
            self.sensorType = row[1]
            self.sensorvalue = row[2]
    
    def setSatus(self):
        sql = "insert into sensorStates (sensorid, sensortype, sensorvalue, enabled) values( '{0}', '{1}', {2}, 1 )"
        sql = sql.replace('{0}',  self.sensorId)
        sql = sql.replace('{1}',  self.sensorType)
        sql = sql.replace('{2}',  str(self.sensorvalue))
        
        print(sql)
        
        self.dbCur.execute(sql)

    def setHeartbeat(self):
        sql = "insert into sensorHeartbeats (sensorid, ip, rssi) values('{0}', '{1}', {2})"
        sql = sql.replace('{0}',  self.sensorId)
        sql = sql.replace('{1}',  self.sensorIp)
        sql = sql.replace('{2}',  self.rssi)
        
        print(sql)
        
        self.dbCur.execute(sql)
        
    def registration(self):
        # http://harwoods.no-ip.org:5000/sensorRegistration/t1/t2/t3/t4
        sql = "select sensorid from sensorresistration where sensorid = '{0}'".replace('{0}',  self.sensorId)
        
        self.dbCur.execute(sql)
        rows = self.dbCur.fetchall()
        
        if len(rows) == 0:
            sql = "insert into sensorresistration (sensorid, sensortype, sensormedium, provider) values('{0}', '{1}', '{2}', '{3}')"
            sql = sql.replace('{0}',  self.sensorId)
            sql = sql.replace('{1}',  self.sensorType)
            sql = sql.replace('{2}',  self.sensormedium)
            sql = sql.replace('{3}',  self.sensorprovider)
            
            print(sql)
            
            self.dbCur.execute(sql)
        else:
            print('Sensor already exists.')
        
# sensorId
    def setSensorID(self, sensorId):
            self.sensorId = sensorId
            #self.setSatus()
            
    def getSensorID(self):
            return self.sensorId
 
 # sensorIp
    def setSensorIP(self, sensorIp):
            self.sensorIp = sensorIp
            #self.setSatus()
            
    def getSensorIP(self):
        return self.sensorIp

# sensor rssi
    def setSensorRssi(self, rssi):
            self.rssi = rssi
    
    def getSensorRssi(self):
        return self.rssi

# sensorType
    def setSensorType(self, sensorType):
            self.sensorType = sensorType
            #self.setSatus()
            
    def getSensorType(self):
            return self.sensorType

# sensorvalue
    def setSensorValue(self, sensorvalue):
            self.sensorvalue = sensorvalue
            #self.setSatus()
            
    def getSensorValue(self):
            return self.sensorvalue

# sensormedium
    def setSensorMedium(self, sensormedium):
            self.sensormedium = sensormedium
            
    def getSensorMedium(self):
            return self.sensorMedium
            
# sensorprovider
    def setSensorProvider(self, sensorprovider):
            self.sensorprovider = sensorprovider
            
    def getSensorProvider(self):
            return self.sensorProvider
