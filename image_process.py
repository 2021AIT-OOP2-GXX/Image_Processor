import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import Processor

BASEDIR = os.path.abspath(os.path.dirname(__file__))
OUT_DIR = "./output_images/"


def get_ext(filename):
    return os.path.splitext(filename)[-1].lower()


class WatchChangeHandler(FileSystemEventHandler):

    def on_modified(self, event):
        if event.is_directory:
            return
        if get_ext(event.src_path) in ('.jpg', '.jpeg'):
            print('%s has been modified.' % event.src_path)

            Processor.GrayScaleProcessor().process(event.src_path)


if __name__ == '__main__':
    print('watch on %s' % BASEDIR + "/upload_images")

    event_handler = WatchChangeHandler()

    observer = Observer()
    observer.schedule(event_handler, BASEDIR + "/upload_images", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
