# Typing-Deputy

## Overview

**Typing-Deputy** is a typing assistant that helps fix typos, casing, and punctuation errors in real-time. It utilizes Mistral 7B locally via Ollama.


## Features

- **Real-time Correction:** Correct typos, casing, and punctuation as you type.
- **Customizable Shortcuts:** Use F1 to fix the current line and F2 to fix the current selection.

## Installation
You would need to have Ollama installed on your local machine.

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Typing-Deputy.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the main script:

    ```bash
    python main.py
    ```

## Structure

- **utils/listener.py:** Defines the `Listener` class that listens for specific keyboard events and triggers corresponding callbacks.

- **utils/config.py:** Contains configuration settings and templates for Ollama integration.

- **utils/assistant.py:** Implements the `Assistant` class for text correction and manipulation usingOllama.

- **main.py:** Entry point of the Typing Deputy program, initializes the Assistant and Listener.

## Usage

- Press **F1** to fix the current line.
- Press **F2** to fix the current selection.

## Dependencies

- [pynput](https://pynput.readthedocs.io/en/latest/): Library to monitor and control input devices.

- [pyperclip](https://pyperclip.readthedocs.io/en/latest/): Cross-platform clipboard module for Python.

- [httpx](https://www.python-httpx.org/): Async HTTP client.

## Contributing

Feel free to contribute by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.