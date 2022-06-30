"""
Author: Zachary Stewart
Date: 6/30/2022

Description: Test project to experiment with Raspberry PI + Sense Hat temperature and humidity sensors
"""
# -*- coding: utf-8 -*-

# import SenseHat module
from sense_hat import SenseHat
# import time module
import time

# initialize instance of SenseHat
sense = SenseHat()

"""
# Test basic humidity functions

humidity = sense.get_humidity()
print("Humidity: %s %%rH" % humidity)

# alternatives
print(sense.humidity)
"""

"""
# Test out basic temperature functions

temperature_c = sense.get_temperature()
print("Temperature: %s C" % temperature_c)
temperature_f = (temperature_c * 9/5) + 32
print("Temperature: %s F" % temperature_f)

# alternatives
# print(sense.temp)
# print(sense.temperature)

print(sense.get_temperature_from_humidity())
"""
"""
# Takes temperature, prints to display

temperature_c = sense.get_temperature()

print(temperature_c - (temperature_c % .1))
sense.show_message(str(temperature_c - (temperature_c % .1)) + "C")
"""

"""
# Make display fill based on temperature

while True:
  temperature_c = sense.get_temperature()
  temperature_c = round(temperature_c)

  print(temperature_c)
  temperature_f = (temperature_c * 9/5) + 32
  print("Temperature: %s F" % temperature_f)

  arr = []
  color_cold = [35, 241, 238]
  color_mild = [231, 241, 35]
  color_warm = [230, 126, 34]
  color_hot = [255, 35, 35]
  empty_color = [255, 255, 255]

  for i in range(64):
    # print(i)
    if i <= temperature_c:
      if i <= 10:
        arr.append(color_cold)
      elif i <= 18:
        arr.append(color_mild)
      elif i <= 30:
        arr.append(color_warm)
      else:
        arr.append(color_hot)
    else:
      arr.append(empty_color)

  sense.set_pixels(arr)

  time.sleep(0.5)
"""

"""
# Display humidity
"""

arr = []
color = [127, 127, 255]

humidity = sense.get_humidity()
humidity = round(humidity * .64)
print(humidity)

for i in range(64):
  if i < humidity:
    arr.append(color)
    c = color[0]
    color = [c - 2, c - 2, 255]
  else:
    arr.append([255, 255, 255])

sense.set_pixels(arr)
