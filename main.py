# This main file contains back end scripting of key strokes
# Another file named key_gui will be used for user interface
# We will also try using sqlite for database in this project.

import pynput

from pynput.keyboard import Key, Listener


def on_press(key):
    print("{0} pressed".format(key))


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
