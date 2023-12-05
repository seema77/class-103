import time
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler # on_create

source=""
dest=""

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):  # creates folder according to ur file type
        print(event)


event_handler=FileMovementHandler()
observer=Observer()
observer.schedule(event_handler,source,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running.....")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
