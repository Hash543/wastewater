#!/usr/bin/python
import os
import json
import minimalmodbus
import urllib
import pycurl
import pprint
import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
chanel = 7
from StringIO import StringIO
##Define a function named Blink()
try:
	buffer = StringIO()
	CURL_HOST = "http://www.da-tung.com"
	CURL_PATH = "/jobs/receive.php?"
	i = 1
	while i < 10:
		try:
			instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) # port name, slave address (in decimal)
			instrument.serial.baudrate = 9600
			## Read temperature (PV = ProcessValue) ##
			# Registernumber, number of decimals
			ph = instrument.read_register(0, 1 , 4) 
			# ec = 
			ec = instrument.read_register(6, 1 , 4) 
			# tss = 
			tss = instrument.read_register(13, 1 , 4) 	
			i = 10
			dataList = [ph,ec,tss]
		except:
			print ("retry comminucation!!")
			time.sleep(10)
			i += 1
	url = CURL_HOST + CURL_PATH
	c = pycurl.Curl()
	c.setopt(c.URL, url )
	#pprint.pprint(c.POST)
	postData = {"ph": dataList[0],"ec": dataList[1],"tss": dataList[2],"cid": os.getenv('CUSTOMERID')};
	c.setopt(c.POSTFIELDS, urllib.urlencode(postData))

	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()
	decodejson = json.loads(buffer.getvalue());
	if decodejson['notice'] == "true" :
		os.system("sudo python /home/pi/wastewater/RPIONotice.py")
except Exception as inst:
   	print type(inst)     # the exception instance
   	print inst.args      # arguments stored in .args
   	print inst           # __str__ allows args to be printed directly
   	x, y = inst.args
   	print 'x =', x
   	print 'y =', y
else:
	print(url);
	print(buffer.getvalue());
	print(os.getenv('CUSTOMERID'))
