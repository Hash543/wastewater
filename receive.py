#!/usr/bin/env python
import json
import minimalmodbus
CURL_HOST = "da-tung.com";
instrument = minimalmodbus.Instrument('COM5', 1) # port name, slave address (in decimal)
instrument.serial.baudrate = 9600
## Read temperature (PV = ProcessValue) ##
# Registernumber, number of decimals
ph = instrument.read_register(0, 1 , 4) 
# ec = 導電度
ec = instrument.read_register(6, 1 , 4) 
# tss = 懸浮粒子
tss = instrument.read_register(13, 1 , 4) 
curlData = json.dumps({"ph": ph,"ec": ec,"tss": tss})

print ("ph")
print (ph)
print ("ec")
print (ec)
print ("tss")
print (tss)
print(curlData)