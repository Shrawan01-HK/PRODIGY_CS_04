# Simple-Keyloger
# Keylogger Application

This repository contains a Python-based keylogger application with a graphical user interface (GUI) built using Tkinter. The application captures and logs keystrokes to a file, allowing users to monitor keyboard activity.

## Overview

The Keylogger application provides an easy-to-use interface for starting and stopping the logging of keystrokes. It utilizes the `pynput` library to listen for keyboard events and records each key press along with a timestamp.

### Key Features

- **Start and Stop Logging**: Users can start and stop the keylogger using buttons in the GUI.
- **Log File Creation**: Keystrokes are saved to a file named `keylog.txt`, which can be opened directly from the application.
- **Real-Time Feedback**: The GUI updates to reflect the current status of the keylogger, informing users when it is active or stopped.
- **Threaded Execution**: The keylogger runs in a separate thread, allowing the GUI to remain responsive while logging keystrokes.

## How It Works

1. **User Interface**: The application features buttons to start and stop the keylogger, along with labels to display the current status and log file path.
2. **Keylogger Functionality**:
   - When started, the keylogger begins to listen for key presses using `pynput.keyboard.Listener`.
   - Each key press is recorded in `keylog.txt` with a timestamp.
3. **Stopping the Keylogger**: Users can stop the keylogger at any time, which closes the log file and updates the interface accordingly.

## Example Usage

1. Launch the application.
2. Click "Start Keylogger" to begin logging keystrokes.
3. Perform keyboard activities to capture logs.
4. Click "Stop Keylogger" to stop logging and open the log file.

## Requirements

- Python 3.x
- Tkinter (included with standard Python installations)
- Pynput library (`pip install pynput`)

## License

This project is open-source and licensed under the MIT License. Use it responsibly and ensure compliance with legal regulations regarding keylogging. Contributions and improvements are welcome!
