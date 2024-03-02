from pynput.keyboard import Key, Controller
import platform

keyboard = Controller()

def fix_current_line():
    pass

def fix_current_selection():
    pass    

def get_device_type():
    if platform.system() == "Darwin":
        return "mac"
    elif platform.system() == "Windows":
        return "windows"