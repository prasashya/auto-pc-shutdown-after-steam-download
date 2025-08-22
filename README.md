# Steam Auto Shutdown

A simple Python script that monitors your Steam download folder and automatically shuts down your PC once downloads are finished.

## Features
- Monitors Steam's downloading folder for changes  
- Detects when downloads are complete  
- Shuts down the system automatically after a set idle time  

## Requirements
- Python 3.x  
- Windows OS (uses `shutdown /s /t 0` command)  

## Installation
1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/yourusername/steam-auto-shutdown.git
   cd steam-auto-shutdown


Edit the script to set your Steam downloading folder path:
download_folder = r"C:\Program Files (x86)\Steam\steamapps\downloading"

Adjust the idle time limit if needed:
idle_time_limit = 30  # seconds

Run the script from Command Prompt or PowerShell:
python steam_shutdown.py


## Notes
Works only on Windows (uses Windows shutdown command).
You can stop it anytime using Ctrl + C.
Make sure to save all your work before running the script.
