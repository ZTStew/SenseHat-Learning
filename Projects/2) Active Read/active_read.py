"""
Author: Zachary Stewart
Date: 6/28/2022

Description: Test project to learn the basics of Raspberry PI + Sense Hat
  Program actively reads and displays what the user inputs as they input it


SCRAPED PROJECT. Sense Hat Emulator DOES NOT SUPPORT 'pynput' modules



"""

# import SenseHat module
# from sense_hat import SenseHat
# import msvcrt


from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()