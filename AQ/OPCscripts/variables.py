# -*- coding: utf-8 -*-
"""
Created on 06/05/2019
@author: Daniel Jarvis
Variables for the sensors operation
"""
#All the needed varaibles
#RPI3 Name
RPINAME="AQRPI4"
#Desired operation mode

#folder locations 
#FOLDER = '/home/pi/AQ/OPCData/' #for raw data
#FOLDERCODE='/home/pi/AQ/OPCscripts/' #For the scpirs locaton 
FOLDER = '/home/pi/OPC-N3_python/AQ/OPCData/' #for raw data
FOLDERCODE='/home/pi/OPC-N3_python/AQ/OPCscripts/' #For the scpirs locaton 
#Operation location, if using with GPS use area name, add inital lat and lon
LOC=['KP_Home','Lat','lon'] #Add test name into this too, say aersol and calbration ...

#Intergration names
integration=10

#OPCN3 attempts before reset. Number of try in to get a responce from the OPCN3, if excessed reset SPI connection 
AT=30
#Check internet connect, URL to ping
URL = 'https://github.com/JarvisSan22/OPC-N3_python'

MODE= "GPS"   #"GPS"   "Normal"
#Note if GPS is on it takes up "/dev/ttyACM0" port, so for OPNC2 and N3 use be carfull and check /dev/

##Desired sensors to run on RPI3
OPCON="ON"
RUNSEN=["SDS011_K1"]  #add your OPC name for OPCN3 or OPCN2)
#RUNSEN=["OPCN3_7","OPCN3_N2"]
#Sensor ports for deried sensors, if you dont know check the /dev folder
#RUNPORT=["/dev/ttyACM0","/dev/ttyUSB0"]
RUNPORT=["/dev/ttyUSB0"]
#RUNPORT=["/dev/ttyUSB1"]
#Temp sensors port number, if a DHT11 or 22 is running get the por  
#DHTON="ON"
DHTON="OFF"
DHTNAMES=["DHT22_1"]
DHTPINS=[14] #check the pin
