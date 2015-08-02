#!/usr/bin/python
import os
import json
import minimalmodbus
import urllib
import pycurl
import pprint
from StringIO import StringIO

buffer = StringIO()
CURL_HOST = "http://da-tung.com"
CURL_PATH = "/jobs/receive.php?"
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) # port name, slave address (in decimal)
instrument.serial.baudrate = 9600
## Read temperature (PV = ProcessValue) ##
# Registernumber, number of decimals
ph = instrument.read_register(0, 1 , 4) 
# ec = 
ec = instrument.read_register(6, 1 , 4) 
# tss = 
tss = instrument.read_register(13, 1 , 4) 
url = CURL_HOST + CURL_PATH
c = pycurl.Curl()
c.setopt(c.URL, url )
#pprint.pprint(c.POST)
postData = {"ph": ph,"ec": ec,"tss": tss,"cid": os.getenv('CUSTOMERID')};
c.setopt(c.POSTFIELDS, urllib.urlencode(postData))

c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
print(url)
print(buffer.getvalue())
print(os.getenv('CUSTOMERID'))