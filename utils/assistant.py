from pynput.keyboard import Key, Controller
from utils.config import (
    OLLAMA_ENDPOINT,
    OLLAMA_CONFIG,
    generate_corrected_text
    )
import platform
import pyperclip
import time
import httpx

class Assistant:
    """
    A class representing an assistant for text correction and manipulation.

    Attributes:
        keyboard (Controller): The keyboard controller for simulating key presses.

    Methods:
        get_device_type: Returns the type of the device (mac or windows).
        fix_text: Fixes the given text using an external API.
        fix_current_line: Fixes the text in the current line.
        fix_current_selection: Fixes the text in the current selection.
    """

    def __init__(self):
        self.keyboard = Controller()

    def get_device_type(self):
        """
        Returns the type of the device (mac or windows).

        Returns:
            str: The device type.
        """
        if platform.system() == "Darwin":
            return "mac"
        elif platform.system() == "Windows":
            return "windows"
        else:
            raise "Unknown"
        
    def fix_text(self, text):
        """
        Fixes the given text using an external API.

        Args:
            text (str): The text to be fixed.

        Returns:
            str: The fixed text.
        """
        prompt = generate_corrected_text(text)
        response = httpx.post(
            OLLAMA_ENDPOINT,
            json={"prompt": prompt, **OLLAMA_CONFIG},
            headers={"Content-Type": "application/json"},
            timeout=10
            )
        if response.status_code != 200:
            print(f"Failed to fix text: {response.status_code}")
            return text
        return response.json()["response"].strip()

    def fix_current_line(self):
        """
        Fixes the text in the current line.
        """
        if self.get_device_type() == "mac":
            self.keyboard.press(Key.cmd)
            self.keyboard.press(Key.shift)
            self.keyboard.press(Key.left)
            
            self.keyboard.release(Key.cmd)
            self.keyboard.release(Key.shift)
            self.keyboard.release(Key.left)
            self.fix_current_selection() 
        else:
            self.keyboard.press(Key.ctrl)
            self.keyboard.press(Key.shift)
            self.keyboard.press(Key.left)
            
            self.keyboard.release(Key.ctrl)
            self.keyboard.release(Key.shift)
            self.keyboard.release(Key.left)
            self.fix_current_selection()

    def fix_current_selection(self):
        """
        Fixes the text in the current selection.
        """
        if self.get_device_type() == "mac":
            with self.keyboard.pressed(Key.cmd):
                self.keyboard.tap("c")
        else:
            with self.keyboard.pressed(Key.ctrl):
                self.keyboard.tap("c")
                
        time.sleep(0.1)
        text = pyperclip.paste()
        if not text:
            return
        fixed_text = self.fix_text(text)
        if fixed_text == text:
            return
        
        pyperclip.copy(fixed_text)
        time.sleep(0.1)
        
        if self.get_device_type() == "mac":
            with self.keyboard.pressed(Key.cmd):
                self.keyboard.tap("v")
        else:
            with self.keyboard.pressed(Key.ctrl):
                self.keyboard.tap("v")
