"""
Author: Zachary Stewart
Date: 6/30/2022

Description: Test project to experiment with Raspberry PI + Sense Hat joystick event detection
"""

# import SenseHat module
from sense_hat import SenseHat
#import random module
import random

# initialize instance of SenseHat
sense = SenseHat()

# sense.stick.

# while True:
#   for event in sense.stick.get_events():
#     print("The joystick was {} {}".format(event.action, event.direction))

# from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
# from signal import pause

# x = 3
# y = 3
# sense = SenseHat()

# def clamp(value, min_value=0, max_value=7):
#     return min(max_value, max(min_value, value))

# def pushed_up(event):
#     global y
#     if event.action != ACTION_RELEASED:
#         y = clamp(y - 1)

# def pushed_down(event):
#     global y
#     if event.action != ACTION_RELEASED:
#         y = clamp(y + 1)

# def pushed_left(event):
#     global x
#     if event.action != ACTION_RELEASED:
#         x = clamp(x - 1)

# def pushed_right(event):
#     global x
#     if event.action != ACTION_RELEASED:
#         x = clamp(x + 1)

# def refresh():
#     sense.clear()
#     sense.set_pixel(x, y, 255, 255, 255)

# sense.stick.direction_up = pushed_up
# sense.stick.direction_down = pushed_down
# sense.stick.direction_left = pushed_left
# sense.stick.direction_right = pushed_right
# sense.stick.direction_any = refresh
# refresh()
# pause()

"""
# Game, single pixel (blinks to different colors randomly) when move, leave previous pixel colored with last color
"""

# Starting position
x = random.randrange(0, 8)
y = random.randrange(0, 8)

print("x: " + str(x) + " | y: " + str(y))
