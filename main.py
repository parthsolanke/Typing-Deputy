from utils.listener import Listener
from utils.assistant import Assistant

def main():
    """
    Entry point of the Typing Deputy program.
    """
    print("Typing Deputy started ...🚨")
    assistant = Assistant()
    listener  = Listener(
        f1_callback=assistant.fix_current_line,
        f2_callback=assistant.fix_current_selection
    )
    listener.start()

if __name__ == "__main__":
    main()