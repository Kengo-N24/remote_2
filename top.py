from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

import os
import time

import webbrowser

target_dir = r'C:\Users\kengo\iCloudDrive\iCloud~com~omz-software~Pythonista3'
target_file = '*.txt'

i = 0

class FileChangeHandler(PatternMatchingEventHandler):

  def on_modified(self, event):
          global i
          i += 1
          if i % 3 == 1:
            time.sleep(2)
            f = open(r"C:\Users\kengo\iCloudDrive\iCloud~com~omz-software~Pythonista3\youtube\output.txt", 'r' , encoding='UTF-8')
            url = f.read()
            print(url)
            webbrowser.open(url)
            f.close()
            print(i,"Hi")
          else:
            print(i)

if __name__ == "__main__":
  event_handler = FileChangeHandler([target_file])
  observer = Observer()
  observer.schedule(event_handler, target_dir, recursive=True)
  observer.start()

  try:
      while True:
             time.sleep(0.1)
  except KeyboardInterrupt:
         observer.stop()
  observer.join()

