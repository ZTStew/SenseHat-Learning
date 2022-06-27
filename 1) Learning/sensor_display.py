"""
Author: Zachary Stewart
Date: 6/27/2022

Description: Test project to learn the basics of Raspberry PI + Sense Hat
  Test sensor display commands



"""

# import SenseHat module
from sense_hat import SenseHat
# initialize instance of SenseHat
sense = SenseHat()

# displays full message, then displays last letter, 'h'

# displays "test"
sense.show_message("test")

# shows only 'h'
sense.show_letter('z')
sense.show_letter('a')
sense.show_letter('c')
sense.show_letter('h')
