#!/usr/bin/env python3

from pumpStatusClass import PumpStatus
from ledcontrolClass import ledcontrol
from sensorStateClass import sensorState
from weatherClass import weather
from controlClass import control
from sunrisesetClass import sunRiseSet
from LogClass import Log

from flask import Flask  #,  request  # , render_template
from flask_restful import Resource,  Api

app = Flask(__name__)
api = Api(app)


class PumpStateRead(Resource):
    def get(self):
        myPumpStatus = PumpStatus()
    
        myPumpStatus.getStatus()
    
        returnString = {'hosestate': str(myPumpStatus.hosestate),  'irrigationstate': str(myPumpStatus.irrigationstate), 'pumpstate': str(myPumpStatus.pumpstate), 'eventname': myPumpStatus.eventname}
    
        return returnString,  200


class PumpStateWrite(Resource):
    def get (self):
        myPumpStatus = PumpStatus()
    
        myPumpStatus.setStatus(1,  1,  1,  'Remote state update!')
    
        returnString = {'pumpStateWrite': 'Pump state updated'}
    
        return returnString,  200


class LedStateRead(Resource):
    def get(self):
        myLedControl = ledcontrol()
    
        myLedControl.getStatus()
    
        return 'Code to be completed',  404


class LedStateWrite(Resource):
    def get(self, led,  ledGreen, ledRed):
        myLedControl = ledcontrol()
    
        myLedControl.getStatus()
        myLedControl.setWeatherGreen(ledGreen)
        myLedControl.setWeatherRed(ledRed)
    
        returnString = {'ledStateGreen':  str(ledGreen),  'ledStateRed': str(ledRed)}
    
        return returnString,  200


class SensorStateWrite(Resource):
    def get(self,  sensorId,  sensorType, sensorValue):
        mySensorState = sensorState()
    
        mySensorState.setSensorID(sensorId)
        mySensorState.setSensorType(sensorType)
        mySensorState.setSensorValue(sensorValue)
        mySensorState.setSatus()

        returnString = {'state':  str(200)}

        return returnString, 200


class SensorRegistration(Resource):
    def get(self,  sensorId,  sensorType, sensorMedium,  provider):
        mySensorState = sensorState()
    
        mySensorState.setSensorID(sensorId)
        mySensorState.setSensorType(sensorType)
        mySensorState.setSensorMedium(sensorMedium)
        mySensorState.setSensorProvider(provider)
        mySensorState.registration()

        returnString = {'state':  str(200)}

        return returnString,  200


class SensorHeartbeat(Resource):
    def get(self, sensorId):
        mySensorState = sensorState()
    
        mySensorState.setSensorID(sensorId)
        # mySensorState.setSensorIP(sensorIp)
        mySensorState.setHeartbeat()

        returnString = {'state':  str(200)}

        return returnString,  200


class SensorHeartbeatIP(Resource):
    def get(self,  sensorId, sensorIp,  rssi):
        mySensorState = sensorState()
    
        mySensorState.setSensorID(sensorId)
        mySensorState.setSensorIP(sensorIp)
        mySensorState.setSensorRssi(rssi)
        mySensorState.setHeartbeat()

        returnString = {'state':  str(200)}

        return returnString,  200


class LevelStateWrite(Resource):
    def get(self,  sensorId,  sensorType, sensorValue):
        mySensorState = sensorState()
    
        mySensorState.setSensorID(sensorId)
        mySensorState.setSensorType(sensorType)
        mySensorState.setSensorValue(sensorValue)
        mySensorState.setSatus()

        returnString = {'state':  str(200)}

        return returnString, 200


class GetWeatherGraph(Resource):
    def get(self):
        myWeather = weather()
    
        returnString = myWeather.getWeatherGraph()

        return returnString,  200


class GetControlStates(Resource):
    def get(self):
        myControl = control()
    
        returnString = myControl.isWet()
    
        returnString = {'isWet':  myControl.isWet(),  'isLevel': myControl.isLevel(),  'isHose': myControl.isHose(),  'isSunrise': myControl .isSunrise(),  'isSunset': myControl .isSunset()}
    
        return returnString, 200



class IsWet(Resource):
    def get(self):
        myControl = control()
    
        returnString = myControl.isWet()

        return returnString, 200


class IsLevel(Resource):
    def get(self):
        myControl = control()
    
        returnString = myControl.isLevel()

        return returnString, 200


class IsHose(Resource):
    def get(self):
        myControl = control()
    
        returnString = myControl.isHose()

        return returnString, 200
    

class IsSunrise(Resource):
    def get(self):
        myControl = control()
    
        returnString = myControl .isSunrise()

        return returnString, 200


class IsSunset(Resource):
    def get(self):
        myControl = control()
    
        returnString = myControl .isSunset()

        return returnString, 200


class SunriseTime(Resource):
    def get(self):
        mySunRiseSet = sunRiseSet()
    
        mySunRiseSet.getSunriseset()
    
        returnString = str(mySunRiseSet.sunrise)
    
        return returnString, 200


class SunsetTime(Resource):
    def get(self):
        mySunRiseSet = sunRiseSet()
    
        mySunRiseSet .getSunriseset()
    
        returnString = str(mySunRiseSet.sunset)
        
        return returnString, 200

class LogEvents(Resource):
    def get(self,  sensorId, sensorIp,  rssi,  freemem,  resthost, logtext):
        myLog = Log()
    
        myLog.sensorId= sensorId
        myLog.sensorIp = sensorIp
        myLog.rssi =rssi
        myLog.freemem = freemem
        myLog.resthost = resthost
        myLog.logtext = logtext
        
        myLog.setLogEntry()

        returnString = {'state':  str(200)}

        return returnString,  200

api.add_resource(PumpStateRead, '/pumpStateRead')
api.add_resource(PumpStateWrite, '/pumpStateWrite')
api.add_resource(LedStateRead, '/ledStateRead')
api.add_resource(LedStateWrite, '/ledStateWrite/<float:led>/<float:ledGreen>/<float:ledRed>')
api.add_resource(SensorStateWrite, '/sensorStateWrite/<string:sensorId>/<string:sensorType>/<int:sensorValue>')
api.add_resource(SensorRegistration, '/sensorRegistration/<string:sensorId>/<string:sensorType>/<string:sensorMedium>/<string:provider>')
api.add_resource(SensorHeartbeat, '/sensorHeartbeat/<string:sensorId>')

api.add_resource(SensorHeartbeatIP ,'/sensorHeartbeatIP/<string:sensorId>/<string:sensorIp>/<string:rssi>')

api.add_resource(LevelStateWrite, '/levelStateWrite/<string:sensorId>/<string:sensorType>/<int:sensorValue>')
api.add_resource(GetWeatherGraph, '/getWeatherGraph/')
api.add_resource(GetControlStates, '/getControlStates/')
api.add_resource(IsWet, '/isWet')
api.add_resource(IsLevel, '/isLevel')
api.add_resource(IsHose, '/isHose')
api.add_resource(IsSunrise, '/isSunrise')
api.add_resource(IsSunset, '/isSunset')
api.add_resource(SunriseTime, '/sunriseTime')
api.add_resource(SunsetTime, '/sunsetTime')

api.add_resource(LogEvents ,'/logEvent/<string:sensorId>/<string:sensorIp>/<string:rssi>/<string:freemem>/<string:resthost>/<string:logtext>')

if __name__ == '__main__':
    app.run(debug=True)

