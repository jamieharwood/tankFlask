#!/usr/bin/env python

import psycopg2
import datetime

class control():
    datestamp = datetime.datetime.now()
    
    def __init__(self):
        self.dbconn = psycopg2.connect(host='localhost', dbname='tank', user='tank', password='skinner2')
        self.dbconn.autocommit = True
        self.dbCur = self.dbconn.cursor()
        
    def __call__(self):
        self.dbconn = psycopg2.connect(host='localhost', dbname='tank', user='tank', password='skinner2')
        self.dbconn.autocommit = True
        self.dbCur = self.dbconn.cursor()
    
    def isWet(self):
        return self.getSensorValue("select sensortype, sensorvalue from public.\"sensorLatestDetail\" where sensortype = \'weather-wet\';")
    
    def isLevel(self):
        return self.getSensorValue("select sensortype, sensorvalue from public.\"sensorLatestDetail\" where sensortype = \'level\';")
    
    def isSunrise(self):
        return self.getSensorValue("select sensortype, sensorvalue from public.\"sensorLatestDetail\" where sensortype = \'sun-rise\';")
    
    def isSunset(self):
        return self.getSensorValue("select sensortype, sensorvalue from public.\"sensorLatestDetail\" where sensortype = \'sun-set\';")
    
    def isHose(self):
        return self.getSensorValue("select sensortype, sensorvalue from public.\"sensorLatestDetail\" where sensortype = \'switch-user\';")
    
    def getSensorValue(self,  sql):
        returnValue = 0
        
        self.dbCur.execute(sql)
        rows = self.dbCur.fetchall()
        
        if len(rows) > 0:
            for row in rows:
                returnValue = str(row[1])

        return returnValue
    
