"""
Author: Zachary Stewart
Date: 6/27/2022

Description: Test project to learn the basics of Raspberry PI + Sense Hat
  Test sensor display commands



"""

# import SenseHat module
from sense_hat import SenseHat
# import time module
import time
# import random module
import random

# initialize instance of SenseHat
sense = SenseHat()

"""
# displays full message, then displays last letter, 'h'

# displays "test"
sense.show_message("test")

# shows only 'h'
sense.show_letter('z')
sense.show_letter('a')
sense.show_letter('c')
sense.show_letter('h')
"""

"""
# displays each character with half second between

# testing how sleep works with .show_letter

# display 'z'
sense.show_letter('z')
# wait half a second
time.sleep(0.5)
# display 'a'
sense.show_letter('a')
# wait half a second
time.sleep(0.5)
# display 'c'
sense.show_letter('c')
# wait half a second
time.sleep(0.5)
# display 'h'
sense.show_letter('h')
"""

"""
# testing show_message paramerters
# scroll_speed -> larger numbers = slower
sense.show_message(text_string="text_string", scroll_speed=0.2, text_colour=[182, 59, 204], back_colour=[106, 209, 64])
"""

"""
# takes user input word, prints out on display each letter of word

word = ""

while word != "exit":

  word = input("Word:")

  for i in range(len(word)):
    print(word[i])
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    r_inverse = 255 - r
    g_inverse = 255 - g
    b_inverse = 255 - b

    sense.show_letter(s=word[i], text_colour=[r, g, b], back_colour=[r_inverse, g_inverse, b_inverse])
    if i < len(word) - 1:
      time.sleep(.5)

"""