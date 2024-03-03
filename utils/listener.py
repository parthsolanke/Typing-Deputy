from pynput import keyboard

class Listener:
    def __init__(self, f1_callback, f2_callback):
        self.ears = keyboard.GlobalHotKeys({
            "<112>": self.pressed_f1,
            "<113>": self.pressed_f2
        })
        self.f1_callback = f1_callback
        self.f2_callback = f2_callback
        
    def pressed_f1(self):
        self.f1_callback()
        
    def pressed_f2(self):
        self.f2_callback()
    
    def start(self):
        self.ears.__enter__()
        self.ears.join()


