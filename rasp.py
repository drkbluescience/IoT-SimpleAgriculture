https://trinket.io/sense-hat

import time
from datetime import datetime
import urllib.request
from sense_hat import SenseHat

sense = SenseHat()
myAPI= ''
baseURL ='' % myAPI

def update_value(mode):
  value=0
  if mode == "temp":
    temp= sense.temp
    temp_value= temp + 0
    value= temp_value
  elif mode == "humi":
    humi = sense. humidity
    humi_value= humi + 0
    value= humi_value
  elif mode == "pres":
    pres=sense.pressure
    pres_value= pres + 0
    value= pres_value
  return value

while True:
  time.sleep(5.0)
  now = datetime.now()
  current_time= now.strftime("%H: %M: %S")
  print("Current Time= ", current_time)
  print("Temp: ", update_value("temp"))
  print("Humidity: ", update_value("humi"))
  print("Pressure: ", update_value("pres"))
  temp= update_value("temp")
  humi= update_value("humi")
  pres= update_value("pres")
  
  #sending the data to thingspeak
  url = urllib.request
  conn = url.urlopen(baseURL+'&field1='+str(temp)+'&field2='+str(humi)+'field3='+str(pres))
  print(conn.read())
  
conn.close()
