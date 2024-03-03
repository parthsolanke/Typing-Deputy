from pynput import keyboard

class Listener:
    """
    A class that listens for specific keyboard events and triggers the corresponding callbacks.

    Args:
        f1_callback (function): The callback function to be called when F1 key is pressed.
        f2_callback (function): The callback function to be called when F2 key is pressed.
    """

    def __init__(self, f1_callback, f2_callback):
        self.ears = keyboard.GlobalHotKeys({
            "<112>": self.pressed_f1,
            "<113>": self.pressed_f2
        })
        self.f1_callback = f1_callback
        self.f2_callback = f2_callback
        
    def pressed_f1(self):
        """
        Callback function for F1 key press event.
        """
        self.f1_callback()
        
    def pressed_f2(self):
        """
        Callback function for F2 key press event.
        """
        self.f2_callback()
    
    def start(self):
        """
        Starts listening for keyboard events.
        """
        self.ears.__enter__()
        self.ears.join()


