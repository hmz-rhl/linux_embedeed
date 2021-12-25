from sense_hat import SenseHat
#import keyboard
#import time
#import json
#import pygame

#import json

sense = SenseHat()
#sense.clear()
#temp = sense.get_temperature()

pression = sense.get_pressure()
#humidity = sense.get_humidity()
#data = {"temperature" : temp, "pressure": pression, "humidity":humidity}
#sense.set_rotation(180)
print(round(pression,2))
#sense.scroll_speed = 0.001
#chrono = 30;

#for i in range(chrono, 9, -1):
  #sense.show_message(str(i))

#for i in range(57, 47, -1):
 # sense.show_letter(chr(i))
  #time.sleep(1)

#g = [0,255,0]
#for i in range(0,5):

 # g = [0,255,0]
  #sense.set_pixels([
  #g,g,g,g,g,g,g,g,
  #g,g,g,g,g,g,g,g,
  #g,g,g,g,g,g,g,g,
  #g,g,g,g,g,g,g,g,
  #g,g,g,g,g,g,g,g,
  #g,g,g,g,g,g,g,g,
  #g,g,g,g,g,g,g,g,
  #g,g,g,g,g,g,g,g])
  #time.sleep(0.3)
  #g = [255,0,0]
  #sense.set_pixels([
  #g,g,g,g,g,g,g,g,
  #g,g,g,g,g,g,g,g,
  #g,g,g,g,g,g,g,g,
  #g,g,g,g,g,g,g,g,
  #g,g,g,g,g,g,g,g,
 # "g,g,g,g,g,g,g,g,
#  g,g,g,g,g,g,g,g,
  #g,g,g,g,g,g,g,g])
  #time.sleep(0.3)

