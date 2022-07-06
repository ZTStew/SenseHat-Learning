"""
Author: Zachary Stewart
Date: 07/05/2022

Description: Program detects the temperature and humidity. Records it in a local .csv file. Runs calculations like high, low, average, mean
"""

# import SenseHat module
from sense_hat import SenseHat
# import time module
import time
from datetime import datetime
import pytz

# initialize instance of SenseHat
sense = SenseHat()
UTC = pytz.utc
EST = pytz.timezone('America/New_York')
format = '%m/%d/%Y %I:%M %p'

while True:
  # Get Temperature
  # temperature is inaccurate due to sensor proximity to the Raspberry PI CPU
  temperature_c = sense.get_temperature_from_humidity()
  # temperature_c = sense.get_temperature_from_pressure()
  temperature_f = ((temperature_c * 9/5) + 32)
  # temperature_c = temperature_c - (temperature_c % .1)
  temperature_c = round(temperature_c)
  # temperature_f = temperature_f - (temperature_f % .1)
  temperature_f = round(temperature_f)

  # Get Humidity
  humidity = sense.get_humidity()

  # Time Stamp
  # ts = time.time()
  time_stamp = datetime.now(EST)

  # Print Results
  print("### --- ### --- @@@ --- ### --- ###")
  print("Temperature C:", temperature_c)
  print("Temperature F:", temperature_f)
  print("Humidity:", humidity)
  print("Time", time_stamp.strftime(format))

  time.sleep(10)