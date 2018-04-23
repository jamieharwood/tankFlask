#!/usr/bin/env python3
from sensorStateClass import sensorState
import json


def main():
    mySensorState = sensorState()
    mySensorState.setSensorID('33841b00')
    mySensorState.setSensorType('switch-user')
    mySensorState.setSensorValue(1)
    mySensorState.setSatus()

    returnString = {'state':  str(200)}

    print(json .dumps(returnString))
    
main()
    
    
