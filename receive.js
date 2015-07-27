log = console.log;
var serialport = require("serialport");
var SerialPort = serialport.SerialPort; // localize object constructor

var sp = new SerialPort("COM5", {
  baudrate: 9600,
  parser: serialport.parsers.raw,
  dataCallback: function(aaa , b , c){
    log(aaa);
    log(b);
    log(c);
  }

});