#!/usr/bin/env python

import psycopg2
import datetime

class weather():
    datestamp = datetime.datetime.now()
    weather = ""
    temp_c = 0
    wind_dir = ""
    wind_mph = 0
    wind_gust_mph = 0
    windchill_c = 0
    feelslike_c = 0
    visibility_mi = 0
    trend = ""
    
    def __init__(self):
        self.dbconn = psycopg2.connect(host='localhost', dbname='tank', user='tank', password='skinner2')
        self.dbconn.autocommit = True
        self.dbCur = self.dbconn.cursor()
        
        self.getWeather()
        self.getRecentTrend()

    def __call__(self):
        self.dbconn = psycopg2.connect(host='localhost', dbname='tank', user='tank', password='skinner2')
        self.dbconn.autocommit = True
        self.dbCur = self.dbconn.cursor()
    
    def getWeather(self):
        sql = "SELECT * FROM weather where datestamp = (select max(datestamp) from weather);"
        
        self.dbCur.execute(sql)
        rows = self.dbCur.fetchall()
        
        if len(rows) > 0:
            for row in rows:
                self.datestamp = row[1]
                self.weather = row[2]
                self.temp_c = float(row[3])
                self.wind_dir = row[4]
                self.wind_mph = float(row[5])
                self.wind_gust_mph = float(row[6])
                self.windchill_c = float(row[7])
                self.feelslike_c = float(row[8])
                self.visibility_mi = float(row[9])
    
    def getRecentTrend(self):
        
        sql = "select weather, count(weather) as hits from (select weather as hits from public.weather order by datestamp desc limit 24) as weather group by weather.* order by hits desc"
        
        self.dbCur.execute(sql)
        rows = self.dbCur.fetchall()
        
        if len(rows) > 0:
            for row in rows:
                self.trend = row[0]
                break
    
    def isTrend(self,  trend):
        if (self.trend == "(" + trend + ")"):
            return True
        else:
            return False

    def getWeatherGraph(self):
        elementCount = 0
        sql = "select temp_c from weather order by datestamp desc limit 32"
        returnString = ''
        #element = '\'{0}\': {1}'
        element = '{1}'
        
        self.dbCur.execute(sql)
        rows = self.dbCur.fetchall()
        totalRows = len(rows)
        
        if len(rows) > 0:
            for row in rows:
                resultStr = element
                
                # resultStr = resultStr.replace('{0}',  str(elementCount))
                resultStr = resultStr.replace('{1}',  str(row[0]))
                
                elementCount += 1
                if elementCount < totalRows:
                    returnString += resultStr + ", "
                else:
                    returnString += resultStr
                
        return '[{2}]'.replace('{2}',  returnString)
    
    
