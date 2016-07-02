import threading
import requests

class LoripsumThread(threading.Thread):
    lock = threading.Lock()

    def __init__(self, filename):
        threading.Thread.__init__(self)
        self.filename = filename

    def run(self):
        r = requests.get('http://loripsum.net/api/1/short')

        LoripsumThread.lock.acquire()
        with open(self.filename, 'a') as fn:
            fn.write(r.content)
        LoripsumThread.lock.release()
