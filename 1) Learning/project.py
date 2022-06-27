"""
Author: Zachary Stewart
Date: 6/27/2022

Description: Test project to learn the basics of Raspberry PI + Sense Hat
"""

# import SenseHat module
from sense_hat import SenseHat
# initialize instance of SenseHat
sense = SenseHat()

sense.show_message("test")
# sense.show_letter('z')

# print("test")