from pynput.keyboard import Key, Controller
import platform
import pyperclip
import time

class Assistant:
    def __init__(self):
        self.keyboard = Controller()

    def get_device_type(self):
        if platform.system() == "Darwin":
            return "mac"
        elif platform.system() == "Windows":
            return "windows"
        else:
            raise "Unknown"

    def fix_current_line(self):
        pass

    def fix_current_selection(self):
        if self.get_device_type() == "mac":
            with self.keyboard.pressed(Key.cmd):
                self.keyboard.tap("c")
        else:
            with self.keyboard.pressed(Key.ctrl):
                self.keyboard.tap("c")
        
        time.sleep(0.1)
        text = pyperclip.paste()
        print(text)
