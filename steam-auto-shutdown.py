import os
import time
import subprocess

download_folder = r"C:\Program Files (x86)\Steam\steamapps\downloading"  # Replace with your steam download folder path  
idle_time_limit = 30

def get_folder_size(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total += os.path.getsize(fp)
    return total

print("Monitoring Steam downloads... (Press Ctrl+C to stop)")
last_size = get_folder_size(download_folder)
idle_seconds = 0

while True:
    time.sleep(5)
    current_size = get_folder_size(download_folder)

    if current_size != last_size:
        idle_seconds = 0
        last_size = current_size
    else:
        idle_seconds += 5

    if idle_seconds >= idle_time_limit:
        print("Download finished. Shutting down...")
        subprocess.run("shutdown /s /t 0", shell=True)
        break
