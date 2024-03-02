from pynput import keyboard

class Listener:
    def __init__(self):
        self.ears = keyboard.GlobalHotKeys({
            "<112>": self.did_press_f1,
            "<113>": self.did_press_f2
        })

    def did_press_f1(self):
        return True

    def did_press_f2(self):
        return True

    def start(self):
        with self.ears as ears:
            ears.join()
            