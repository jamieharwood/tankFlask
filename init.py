#!/usr/bin/env python3

from pumpStatusClass import PumpStatus
from ledcontrolClass import ledcontrol
from sensorStateClass import sensorState
from weatherClass import weather
from controlClass import control
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Trilby tanks, Wecome..."

@app.route('/pumpStateRead')
def pumpStateRead():
    myPumpStatus = PumpStatus()
    
    myPumpStatus.getStatus()
    
    returnString = {'hosestate': str(myPumpStatus.hosestate),  'irrigationstate': str(myPumpStatus.irrigationstate), 'pumpstate': str(myPumpStatus.pumpstate), 'eventname': myPumpStatus.eventname}
    
    return json .dumps(returnString)

@app.route('/pumpStateWrite')
def pumpStateWrite():
    myPumpStatus = PumpStatus()
    
    myPumpStatus.setStatus(1,  1,  1,  'Remote state update!')
    
    returnString = {'pumpStateWrite': 'Pump state updated'}
    
    return json .dumps(returnString)

@app.route('/ledStateRead')
def ledStateRead():
    myLedControl = ledcontrol()
    
    myLedControl.getStatus()
    
    return 'Code to be completed'

@app.route('/ledStateWrite/<float:led>/<float:ledGreen>/<float:ledRed>')
def ledStateWrite(led,  ledGreen, ledRed):
    myLedControl = ledcontrol()
    
    myLedControl.getStatus()
    myLedControl.setWeatherGreen(ledGreen)
    myLedControl.setWeatherRed(ledRed)
    
    returnString = {'ledStateGreen':  str(ledGreen),  'ledStateRed': str(ledRed)}
    
    
    return json.dumps(returnString)

@app.route('/sensorStateWrite/<string:sensorId>/<string:sensorType>/<int:sensorValue>')
def sensorStateWrite(sensorId,  sensorType, sensorValue):
    mySensorState = sensorState()
    
    mySensorState.setSensorID(sensorId)
    mySensorState.setSensorType(sensorType)
    mySensorState.setSensorValue(sensorValue)
    mySensorState.setSatus()

    returnString = {'state':  str(200)}

    return json .dumps(returnString)

@app.route('/levelStateWrite/<string:sensorId>/<string:sensorType>/<int:sensorValue>')
def levelStateWrite(sensorId,  sensorType, sensorValue):
    mySensorState = sensorState()
    
    mySensorState.setSensorID(sensorId)
    mySensorState.setSensorType(sensorType)
    mySensorState.setSensorValue(sensorValue)
    mySensorState.setSatus()

    returnString = {'state':  str(200)}

    return json.dumps(returnString)

@app.route('/getWeatherGraph/')
def getWeatherGraph():
    myWeather = weather()
    
    returnString = myWeather.getWeatherGraph()

    return json .dumps(returnString)

@app.route('/getControlStates/')
def getControlStates():
    myControl = control()
    
    returnString = myControl.isWet()
    
    returnString = {'isWet':  myControl.isWet(),  'isLevel': myControl.isLevel(),  'isHose': myControl.isHose(),  'isSunrise': myControl .isSunrise(),  'isSunset': myControl .isSunset()}
    
    return json .dumps(returnString)


@app.route('/isWet/')
def isWet():
    myControl = control()
    
    returnString = myControl.isWet()

    return json.dumps(returnString)

@app.route('/isLevel/')
def isLevel():
    myControl = control()
    
    returnString = myControl.isLevel()

    return json.dumps(returnString)

@app.route('/isHose/')
def isHose():
    myControl = control()
    
    returnString = myControl.isHose()

    return json.dumps(returnString)
    
@app.route('/isSunrise/')
def isSunrise():
    myControl = control()
    
    returnString = myControl .isSunrise()

    return json.dumps(returnString)

@app.route('/isSunset/')
def isSunset():
    myControl = control()
    
    returnString = myControl .isSunset()

    return json.dumps(returnString)


if __name__ == '__main__':
	app.run(debug=True)
