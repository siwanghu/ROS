#!/usr/bin/env python
#encoding=utf-8

from xml.dom.minidom import parse
import xml.dom.minidom

def getCruiseBegin():
    DOMTree = xml.dom.minidom.parse("position.xml")
    position = DOMTree.documentElement
    begin=position.getElementsByTagName("begin")[0]
    position={'x':float(begin.getElementsByTagName("x")[0].firstChild.data),\
              'y':float(begin.getElementsByTagName("y")[0].firstChild.data),\
              'z':float(begin.getElementsByTagName("z")[0].firstChild.data)}
    quaternion={'r1':float(begin.getElementsByTagName("r1")[0].firstChild.data),\
                'r2':float(begin.getElementsByTagName("r2")[0].firstChild.data),\
                'r3':float(begin.getElementsByTagName("r3")[0].firstChild.data),\
                'r4':float(begin.getElementsByTagName("r4")[0].firstChild.data)}
    return (position,quaternion)

def getCruiseEnd():
    DOMTree = xml.dom.minidom.parse("position.xml")
    position = DOMTree.documentElement
    end=position.getElementsByTagName("end")[0]
    position={'x':float(end.getElementsByTagName("x")[0].firstChild.data),\
              'y':float(end.getElementsByTagName("y")[0].firstChild.data),\
              'z':float(end.getElementsByTagName("z")[0].firstChild.data)}
    quaternion={'r1':float(end.getElementsByTagName("r1")[0].firstChild.data),\
                'r2':float(end.getElementsByTagName("r2")[0].firstChild.data),\
                'r3':float(end.getElementsByTagName("r3")[0].firstChild.data),\
                'r4':float(end.getElementsByTagName("r4")[0].firstChild.data)}
    return (position,quaternion)

def getPlaces():
    DOMTree = xml.dom.minidom.parse("position.xml")
    position = DOMTree.documentElement
    positions={}
    places=position.getElementsByTagName("place")
    for place in places:
        position={ 'x':float(place.getElementsByTagName("x")[0].firstChild.data),\
                   'y':float(place.getElementsByTagName("y")[0].firstChild.data),\
                   'z':float(place.getElementsByTagName("z")[0].firstChild.data)}
    
        quaternion={'r1':float(place.getElementsByTagName("r1")[0].firstChild.data),\
                    'r2':float(place.getElementsByTagName("r2")[0].firstChild.data),\
                    'r3':float(place.getElementsByTagName("r3")[0].firstChild.data),\
                    'r4':float(place.getElementsByTagName("r4")[0].firstChild.data)}
        positions[place.getAttribute("type")]=(position,quaternion)
    return positions